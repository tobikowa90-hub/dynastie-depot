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

import logging
import os
import threading
from pathlib import Path

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


class _FinnHubClient:
    def __init__(self, cache_root: Path = _DEFAULT_CACHE_ROOT) -> None:
        self._api_key = _load_env_key()
        self._cache_root = cache_root
        # Rate-limiter + cache initialized in later tasks
        self._lock = threading.Lock()

    def get_quote(self, symbol: str, force: bool = False) -> dict | None:
        # Skeleton — full impl in Task 5
        url = f"{_BASE_URL}/quote"
        params = {"symbol": symbol, "token": self._api_key}
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 401:
            raise RuntimeError(f"FinnHub auth failed: HTTP 401 — check .env.finnhub")  # noqa: F541
        return None  # Placeholder, full logic later
