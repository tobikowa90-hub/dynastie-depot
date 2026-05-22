"""finnhub_client.py — FinnHub Free-Tier Read-Only-Wrapper für Dynastie-Depot.

Spec: docs/superpowers/specs/2026-05-22-finnhub-integration-design.md v0.3 (SPEC-LOCK).
Surface: get_quote / get_earnings / get_news / get_metrics — alle return dict|list|None.
Constraints: Read-Only-Surface v0.1 — get_metrics() liefert `_meta.for_scoring=False`-Marker;
backtest-ready-forward-verify Schritt 7 assertet `for_scoring=True` und failed bei FinnHub-Daten hard.

Cache: ~/.dynasty/finnhub_cache/<endpoint>/<key>.json, TTL pro Endpoint (§2.4).
Rate-Limit: Token-Bucket 60/min, block-statt-crash bei Erschöpfung.
Fail-Soft: 403 → None+WARN; 429 → Exp-Backoff (3 retries, 2/4/8s); Timeout 10s+1 retry; 401 → Hard-Crash.
"""

from __future__ import annotations

import json
import logging
import os
import threading
import time
from pathlib import Path
from typing import Any

import requests

log = logging.getLogger(__name__)

_BASE_URL = "https://finnhub.io/api/v1"
_DEFAULT_CACHE_ROOT = Path.home() / ".dynasty" / "finnhub_cache"


def _load_env_key() -> str:
    """Load FINNHUB_API_KEY: prefer process env, fallback to .env.finnhub in repo root."""
    key = os.environ.get("FINNHUB_API_KEY")
    if key:
        return key
    repo_root = Path(__file__).resolve().parents[1]
    env_file = repo_root / ".env.finnhub"
    if env_file.exists():
        for raw_line in env_file.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if line.startswith("FINNHUB_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError("FINNHUB_API_KEY not set (neither env nor .env.finnhub)")


class _TokenBucket:
    """Token-Bucket Rate-Limiter -- 60 tokens, 1 token/sec refill (Spec §2.3).

    Verhalten bei Erschoepfung: block bis Token verfuegbar (kein Crash).
    Thread-safe via threading.Lock.
    """

    def __init__(self, capacity: int = 60, refill_per_sec: float = 1.0) -> None:
        self._capacity = capacity
        self._refill_per_sec = refill_per_sec
        self._tokens = float(capacity)
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self) -> None:
        # Re-Check-Loop: nach Sleep MUSS erneut refill+check passieren, sonst
        # over-admit unter Concurrency (Codex-CP0-MED-2-Fix).
        while True:
            with self._lock:
                self._refill_locked()
                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    return
                wait_for = (1.0 - self._tokens) / self._refill_per_sec
            # Release lock during sleep -- other threads can attempt acquire
            time.sleep(wait_for)

    def _refill_locked(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._last_refill = now
        self._tokens = min(self._capacity, self._tokens + elapsed * self._refill_per_sec)


class _FileCache:
    """File-based JSON cache mit endpoint-spezifischer TTL (Spec §2.4).

    Layout: <root>/<endpoint>/<key>.json
    Schreib-Atomicity: write-temp + os.replace (verhindert kaputten File bei Crash).
    Read-Resilience: kaputter JSON → return None, kein Crash (Spec §2.5 A11).
    """

    def __init__(self, root: Path, ttl_seconds: int) -> None:
        self._root = root
        self._ttl = ttl_seconds

    def _path(self, endpoint: str, key: str) -> Path:
        # Key safe for filesystem (replace path separators)
        safe_key = key.replace("/", "_").replace("\\", "_")
        return self._root / endpoint / f"{safe_key}.json"

    def get(self, endpoint: str, key: str) -> Any | None:
        p = self._path(endpoint, key)
        if not p.exists():
            return None
        try:
            mtime = p.stat().st_mtime
            if time.time() - mtime > self._ttl:
                return None
            payload = json.loads(p.read_text(encoding="utf-8"))
            return payload
        except (json.JSONDecodeError, OSError, UnicodeDecodeError) as e:
            log.warning("Cache read failure for %s/%s: %s — bypassing", endpoint, key, e)
            return None

    def set(self, endpoint: str, key: str, value: Any) -> None:
        p = self._path(endpoint, key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
        tmp.replace(p)


class _FinnHubClient:
    def __init__(self, cache_root: Path = _DEFAULT_CACHE_ROOT) -> None:
        self._api_key = _load_env_key()
        self._cache_root = cache_root
        self._lock = threading.Lock()
        self._rate_limiter = _TokenBucket(capacity=60, refill_per_sec=1.0)
        # Per-endpoint TTL (Spec §2.4)
        self._caches = {
            "quote": _FileCache(cache_root / "quotes", ttl_seconds=60),
            "earnings": _FileCache(cache_root / "earnings", ttl_seconds=3600),
            "news": _FileCache(cache_root / "news", ttl_seconds=300),
            "metric": _FileCache(cache_root / "metrics", ttl_seconds=6 * 3600),
        }

    def _request(self, endpoint: str, params: dict) -> Any | None:
        """HTTP-Call mit Retry-Logik (Spec §2.5).

        - 401 → RuntimeError (hard-crash, A7)
        - 403 → None + log.warning (fail-soft, A5)
        - 429 → exp-backoff 2/4/8s, 3 retries (A8), dann None
        - Timeout → 1 retry (A9), dann None
        - 200 → resp.json()

        Token-Bucket-Policy (Codex-CP0-MED-3): Retries verbrauchen KEINE zusätzlichen
        Tokens — der Bucket-acquire passiert einmalig vor der ersten Request. 429-Retries
        sind Server-Side-Rate-Limit-Reaktion, NICHT Client-Side-Quota-Ereignis; doppelte
        Token-Consumption würde nur das Client-Budget verbrennen ohne Effekt.
        """
        self._rate_limiter.acquire()
        url = f"{_BASE_URL}{endpoint}"
        full_params = {**params, "token": self._api_key}

        # Timeout-Retry (1×, A9)
        timeout_attempts = 0
        # Rate-Limit-Retry (3×, A8)
        backoff_attempts = 0
        backoff_waits = [2.0, 4.0, 8.0]

        while True:
            try:
                resp = requests.get(url, params=full_params, timeout=10)
            except requests.Timeout:
                if timeout_attempts >= 1:
                    log.exception("FinnHub timeout exhausted for %s %s", endpoint, params)
                    return None
                timeout_attempts += 1
                continue

            if resp.status_code == 401:
                raise RuntimeError(
                    f"FinnHub auth failed: HTTP 401 — check .env.finnhub (response: {resp.text[:200]})"
                )
            if resp.status_code == 403:
                log.warning(
                    "FinnHub 403 for %s %s — Europäer Premium oder Endpoint restricted",
                    endpoint,
                    params,
                )
                return None
            if resp.status_code == 429:
                if backoff_attempts >= 3:
                    log.error("FinnHub 429 retries exhausted for %s %s", endpoint, params)
                    return None
                wait = backoff_waits[backoff_attempts]
                backoff_attempts += 1
                log.warning("FinnHub 429 — backoff %ss (retry %d/3)", wait, backoff_attempts)
                time.sleep(wait)
                continue
            if resp.status_code == 200:
                return resp.json()
            log.error(
                "FinnHub unexpected status %d for %s %s: %s",
                resp.status_code,
                endpoint,
                params,
                resp.text[:200],
            )
            return None

    def get_quote(self, symbol: str, force: bool = False) -> dict | None:
        if not force:
            cached = self._caches["quote"].get("quote", symbol)
            if cached is not None:
                return cached
        data = self._request("/quote", {"symbol": symbol})
        if data is not None:
            data["_fetched_at"] = time.time()
            self._caches["quote"].set("quote", symbol, data)
        return data
