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

    def test_pull_metrics_strips_banner_prefix(self) -> None:
        """defeatbeta-api emits an INFO banner before the JSON line; rsplit must isolate the last line."""
        banner = "defeatbeta-api v0.0.50\n[INFO] connecting\n"
        payload = json.dumps({"roe": 1.0, "peTTM": 2.0, "roic": 3.0})
        with patch("defeatbeta_subprocess.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout=banner + payload, stderr="")
            data = defeatbeta_subprocess.pull_metrics("MSFT")
        assert data == {"roe": 1.0, "peTTM": 2.0, "roic": 3.0}

    def test_pull_metrics_passes_symbol_as_last_arg(self) -> None:
        """Symbol must be the trailing positional so `sys.argv[1]` resolves correctly in WSL."""
        sample_out = json.dumps({"roe": 1.0, "peTTM": 2.0, "roic": 3.0})
        with patch("defeatbeta_subprocess.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout=sample_out, stderr="")
            defeatbeta_subprocess.pull_metrics("MSFT")
            cmd = mock_run.call_args.args[0]
        assert cmd[-1] == "MSFT"
        assert cmd[0] == "wsl.exe"
