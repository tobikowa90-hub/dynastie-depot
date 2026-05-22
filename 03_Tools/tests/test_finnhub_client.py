"""Unit-tests for finnhub_client wrapper (Spec v0.3 Acceptance A3/A4/A7/A8/A9/A10/A11)."""

from __future__ import annotations

import time
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import requests

import finnhub_client


class TestAuth:
    def test_invalid_key_raises_runtime_error(self, tmp_path: Path, monkeypatch) -> None:
        """A7: 401 from FinnHub MUST hard-crash with clear error, not silent-None."""
        monkeypatch.setenv("FINNHUB_API_KEY", "invalid-key-xxx")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        mock_resp = MagicMock(status_code=401, text="Invalid API key")
        with patch("finnhub_client.requests.get", return_value=mock_resp):
            with pytest.raises(RuntimeError, match=r"FinnHub auth failed: HTTP 401"):
                client.get_quote("MSFT")

    def test_missing_key_raises_runtime_error(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.delenv("FINNHUB_API_KEY", raising=False)
        with pytest.raises(RuntimeError, match=r"FINNHUB_API_KEY not set"):
            finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")


class TestRateLimiter:
    def test_acquire_within_capacity_no_block(self) -> None:
        bucket = finnhub_client._TokenBucket(capacity=60, refill_per_sec=1.0)
        start = time.monotonic()
        for _ in range(60):
            bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed < 0.5, f"first 60 calls must not block, got {elapsed:.3f}s"

    def test_acquire_beyond_capacity_blocks(self, monkeypatch) -> None:
        """A3: 70 calls in 60s — calls 61-70 block; total wait < 12s."""
        sleep_calls: list[float] = []
        # Fake monotonic clock so refill happens deterministically
        clock = [0.0]

        # sleep advances the simulated clock — sonst kann das Re-Check-Loop nicht konvergieren
        def fake_sleep(s: float) -> None:
            sleep_calls.append(s)
            clock[0] += s

        monkeypatch.setattr(finnhub_client.time, "sleep", fake_sleep)
        monkeypatch.setattr(finnhub_client.time, "monotonic", lambda: clock[0])
        # Bucket MUST be created after patching so __init__ gets clock[0]=0.0 for _last_refill
        bucket = finnhub_client._TokenBucket(capacity=60, refill_per_sec=1.0)
        for i in range(70):
            bucket.acquire()
            clock[0] += 0.05  # 50ms per call simulated
        total_sleep = sum(sleep_calls)
        assert total_sleep < 12.0, f"total wait {total_sleep:.2f}s exceeded 12s budget"
        assert len(sleep_calls) > 0, "calls beyond capacity must trigger sleep"

    def test_concurrency_no_overadmit(self) -> None:
        """Codex-CP0-MED-2: Multi-Thread-Burst darf nicht > capacity admitten in window.

        10 Threads x 10 acquires each = 100 total acquires. Mit capacity=10 + refill=1/s
        muss Gesamtdauer >= 9s sein (10 sofort, 90 müssen warten ~9s einschl. refill).
        Akzeptiert effektiver Durchsatz <= bucket-rate.
        """
        import threading

        bucket = finnhub_client._TokenBucket(capacity=10, refill_per_sec=10.0)
        admit_times: list[float] = []
        lock = threading.Lock()

        def worker() -> None:
            for _ in range(10):
                bucket.acquire()
                with lock:
                    admit_times.append(time.monotonic())

        start = time.monotonic()
        threads = [threading.Thread(target=worker) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        elapsed = time.monotonic() - start
        # 100 acquires bei rate=10/s + capacity=10 -> mindestens ~9s
        # (10 sofort, 90 verbleibende benoetigen >= 9s bei 10/s refill)
        assert len(admit_times) == 100, f"expected 100 admits, got {len(admit_times)}"
        assert elapsed >= 8.5, f"over-admitted: 100 in {elapsed:.2f}s (expected >=8.5s @ rate=10/s)"


class TestFileCache:
    def test_cache_miss_returns_none(self, tmp_path: Path) -> None:
        cache = finnhub_client._FileCache(root=tmp_path, ttl_seconds=60)
        assert cache.get("quotes", "MSFT") is None

    def test_cache_hit_returns_value_within_ttl(self, tmp_path: Path) -> None:
        cache = finnhub_client._FileCache(root=tmp_path, ttl_seconds=60)
        cache.set("quotes", "MSFT", {"c": 419.09})
        assert cache.get("quotes", "MSFT") == {"c": 419.09}

    def test_cache_expired_returns_none(self, tmp_path: Path) -> None:
        import os as _os

        cache = finnhub_client._FileCache(root=tmp_path, ttl_seconds=60)
        cache.set("quotes", "MSFT", {"c": 419.09})
        # Backdate the file's mtime to 61 seconds ago to trigger TTL expiry
        p = cache._path("quotes", "MSFT")
        past = time.time() - 61
        _os.utime(p, (past, past))
        assert cache.get("quotes", "MSFT") is None

    def test_a11_corrupted_json_returns_none_no_crash(self, tmp_path: Path) -> None:
        """A11: Cache-Read-Failure → bypass, kein Crash."""
        cache = finnhub_client._FileCache(root=tmp_path, ttl_seconds=60)
        target = tmp_path / "quotes" / "MSFT.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("{ this is not json", encoding="utf-8")
        assert cache.get("quotes", "MSFT") is None  # bypass, kein Crash
        # And: set() must successfully overwrite the corrupted file
        cache.set("quotes", "MSFT", {"c": 419.09})
        assert cache.get("quotes", "MSFT") == {"c": 419.09}


class TestHttpRetry:
    def test_a8_rate_limit_exp_backoff(self, tmp_path: Path, monkeypatch) -> None:
        """A8: HTTP 429 → 3 retries with 2/4/8s waits; success at retry-3 returns data."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        sleeps: list[float] = []
        monkeypatch.setattr(finnhub_client.time, "sleep", lambda s: sleeps.append(s))  # noqa: PLW0108
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        responses = [
            MagicMock(status_code=429),
            MagicMock(status_code=429),
            MagicMock(status_code=429),
            MagicMock(status_code=200, json=lambda: {"c": 419.09}),
        ]
        with patch("finnhub_client.requests.get", side_effect=responses):
            data = client._request("/quote", {"symbol": "MSFT"})
        assert data == {"c": 419.09}
        assert sleeps == [2.0, 4.0, 8.0]

    def test_a8_rate_limit_exhausted_returns_none(self, tmp_path: Path, monkeypatch) -> None:
        """A8: 4 consecutive 429 → return None + log.error."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        monkeypatch.setattr(finnhub_client.time, "sleep", lambda s: None)
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        with patch("finnhub_client.requests.get", return_value=MagicMock(status_code=429)):
            data = client._request("/quote", {"symbol": "MSFT"})
        assert data is None

    def test_a9_timeout_retry_once(self, tmp_path: Path, monkeypatch) -> None:
        """A9: Timeout → 1 retry, then success returns data."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        monkeypatch.setattr(finnhub_client.time, "sleep", lambda s: None)
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        side_effects = [
            requests.Timeout("simulated timeout"),
            MagicMock(status_code=200, json=lambda: {"c": 419.09}),
        ]
        with patch("finnhub_client.requests.get", side_effect=side_effects):
            data = client._request("/quote", {"symbol": "MSFT"})
        assert data == {"c": 419.09}

    def test_a9_double_timeout_returns_none(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        monkeypatch.setattr(finnhub_client.time, "sleep", lambda s: None)
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        with patch("finnhub_client.requests.get", side_effect=requests.Timeout("x")):
            data = client._request("/quote", {"symbol": "MSFT"})
        assert data is None

    def test_403_returns_none_with_warn(self, tmp_path: Path, monkeypatch, caplog) -> None:
        """A5-Vorgriff: 403 (Europäer Premium) → None + WARN."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        with patch("finnhub_client.requests.get", return_value=MagicMock(status_code=403)):
            with caplog.at_level("WARNING"):
                data = client._request("/quote", {"symbol": "RMS.PA"})
        assert data is None
        assert any("403" in r.message for r in caplog.records)


class TestPublicApi:
    def test_a10_force_bypass(self, tmp_path: Path, monkeypatch) -> None:
        """A10: force=True bypasses cache → triggers network-hit even when cached."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        # Seed cache
        client._caches["quote"].set("quote", "MSFT", {"c": 100.0, "_fetched_at": 0.0})
        call_count = {"n": 0}

        def _track(*args, **kw):
            call_count["n"] += 1
            return MagicMock(status_code=200, json=lambda: {"c": 200.0})

        with patch("finnhub_client.requests.get", side_effect=_track):
            data1 = client.get_quote("MSFT")  # cache-hit
            data2 = client.get_quote("MSFT", force=True)  # bypass
        assert data1["c"] == 100.0
        assert data2["c"] == 200.0
        assert call_count["n"] == 1

    def test_get_earnings_uses_earnings_cache(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(
                status_code=200, json=lambda: [{"date": "2026-05-23", "epsActual": 3.5}]
            ),
        ):
            data = client.get_earnings("MSFT", "2026-05-01", "2026-07-01")
        assert data == [{"date": "2026-05-23", "epsActual": 3.5}]
        # Second call within TTL = cache-hit (no network)
        with patch("finnhub_client.requests.get", side_effect=AssertionError("must not call")):
            cached = client.get_earnings("MSFT", "2026-05-01", "2026-07-01")
        assert cached == data

    def test_get_news_uses_news_cache(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        items = [{"headline": "MSFT beats", "datetime": 1716000000}]
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(status_code=200, json=lambda: items),
        ):
            data = client.get_news("MSFT", "2026-05-15", "2026-05-22")
        assert data == items
