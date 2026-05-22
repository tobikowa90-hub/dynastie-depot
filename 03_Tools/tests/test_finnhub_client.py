"""Unit-tests for finnhub_client wrapper (Spec v0.3 Acceptance A3/A4/A7/A8/A9/A10/A11)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

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
