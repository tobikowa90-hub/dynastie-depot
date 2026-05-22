"""defeatbeta_subprocess.py — WSL-Bridge Tests (deterministisch via Mock)."""

from __future__ import annotations

import json
import subprocess
from unittest.mock import MagicMock, patch

import defeatbeta_subprocess


class TestDefeatbetaBridge:
    def test_pull_metrics_parses_json_stdout(self) -> None:
        sample_out = json.dumps({"roe": 27.45, "peTTM": 35.2, "roic": 26.7})
        with patch("defeatbeta_subprocess.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout=sample_out, stderr="")
            data = defeatbeta_subprocess.pull_metrics("MSFT")
        assert data["roe"] == 27.45
        assert data["peTTM"] == 35.2
        assert data["roic"] == 26.7

    def test_pull_metrics_subprocess_failure_returns_none(self) -> None:
        with patch("defeatbeta_subprocess.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="boom")
            data = defeatbeta_subprocess.pull_metrics("MSFT")
        assert data is None

    def test_pull_metrics_invalid_json_returns_none(self) -> None:
        with patch("defeatbeta_subprocess.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="not-json", stderr="")
            data = defeatbeta_subprocess.pull_metrics("MSFT")
        assert data is None

    def test_pull_metrics_timeout_returns_none(self) -> None:
        with patch("defeatbeta_subprocess.subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.TimeoutExpired(cmd="x", timeout=30)
            data = defeatbeta_subprocess.pull_metrics("MSFT")
        assert data is None
