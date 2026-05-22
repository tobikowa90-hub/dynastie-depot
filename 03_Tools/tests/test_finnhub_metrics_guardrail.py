"""get_metrics() Guardrail-Tests (Spec §2.2 + §9-R1 + A5)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest  # noqa: F401

import finnhub_client


class TestMetricsGuardrail:
    def test_returns_meta_block_with_for_scoring_false(self, tmp_path: Path, monkeypatch) -> None:
        """Spec §2.2: get_metrics() MUST return dict with _meta.for_scoring=False."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        sample = {"metric": {"peTTM": 35.2, "roeTTM": 0.42, "roiTTM": 0.27}}
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(status_code=200, json=lambda: sample),
        ):
            data = client.get_metrics("MSFT")
        assert data is not None
        assert "_meta" in data, "get_metrics() MUST include _meta block"
        assert data["_meta"]["for_scoring"] is False, (
            "v0.1 Read-Only-Surface: for_scoring MUST be False"
        )
        assert data["_meta"]["read_only"] is True
        assert data["_meta"]["source"] == "finnhub"
        assert "fetched_at" in data["_meta"]

    def test_returns_metrics_subset(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        sample = {"metric": {"peTTM": 35.2, "roeTTM": 0.42, "irrelevantField": 999}}
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(status_code=200, json=lambda: sample),
        ):
            data = client.get_metrics("MSFT")
        assert data["metrics"]["peTTM"] == 35.2
        assert data["metrics"]["roeTTM"] == 0.42

    def test_a5_europaeer_403_returns_none(self, tmp_path: Path, monkeypatch, caplog) -> None:
        """A5: get_metrics('RMS.PA') → None + WARN, kein Exception."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        with patch("finnhub_client.requests.get", return_value=MagicMock(status_code=403)):
            with caplog.at_level("WARNING"):
                data = client.get_metrics("RMS.PA")
        assert data is None
        assert any("403" in r.message for r in caplog.records)

    def test_get_metrics_module_function_works(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        # Force singleton-reset for isolated test
        monkeypatch.setattr(finnhub_client, "_singleton", None)
        monkeypatch.setattr(finnhub_client, "_DEFAULT_CACHE_ROOT", tmp_path / "cache")
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(status_code=200, json=lambda: {"metric": {}}),
        ):
            data = finnhub_client.get_metrics("MSFT")
        assert data is not None
        assert data["_meta"]["for_scoring"] is False

    def test_cache_poisoning_invalid_meta_triggers_refetch(
        self, tmp_path: Path, monkeypatch
    ) -> None:
        """CP1-MED-2: Cache mit manipuliertem _meta.for_scoring=True -> discard + refetch."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        # Poison cache: for_scoring=True (forbidden in v0.1)
        poisoned = {
            "metrics": {"peTTM": 99.9},
            "_meta": {
                "read_only": True,
                "for_scoring": True,
                "source": "finnhub",
                "fetched_at": 0.0,
            },
        }
        client._caches["metric"].set("metric", "MSFT", poisoned)
        # Network returns clean data
        clean = {"metric": {"peTTM": 35.2}}
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(status_code=200, json=lambda: clean),
        ):
            data = client.get_metrics("MSFT")
        assert data is not None
        assert data["_meta"]["for_scoring"] is False
        assert data["metrics"]["peTTM"] == 35.2  # from network, not cache

    def test_cache_missing_meta_triggers_refetch(self, tmp_path: Path, monkeypatch) -> None:
        """CP1-MED-2: Cache ohne _meta-Block -> discard + refetch."""
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
        client = finnhub_client._FinnHubClient(cache_root=tmp_path / "cache")
        client._caches["metric"].set("metric", "MSFT", {"metrics": {"peTTM": 99.9}})  # no _meta
        clean = {"metric": {"peTTM": 35.2}}
        with patch(
            "finnhub_client.requests.get",
            return_value=MagicMock(status_code=200, json=lambda: clean),
        ):
            data = client.get_metrics("MSFT")
        assert data["_meta"]["for_scoring"] is False
        assert data["metrics"]["peTTM"] == 35.2
