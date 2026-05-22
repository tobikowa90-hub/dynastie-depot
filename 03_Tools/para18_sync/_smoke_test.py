"""Smoke-Test-Suite für paragraph-18-sync validator (S1-S20, Spec §6).

Run: python -m pytest 03_Tools/para18_sync/_smoke_test.py -v
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "03_Tools" / "para18_sync" / "validator.py"


def _run_validator(
    args: list[str],
    cwd: Path | None = None,
    env_extra: dict[str, str] | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess:
    """Subprocess-Helper für validator.py-Aufrufe in Tests."""
    target_cwd = cwd if cwd is not None else ROOT
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *args],
        cwd=str(target_cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        timeout=timeout,
        check=False,
    )


@pytest.fixture
def temp_repo(tmp_path: Path) -> Path:
    """Init ein leeres Mini-Git-Repo für isolierte Tests."""
    subprocess.run(["git", "init", "-q"], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "config", "user.email", "test@test"], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=str(tmp_path), check=True)
    (tmp_path / "README.md").write_text("seed\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=str(tmp_path), check=True)
    return tmp_path


# --------------------------------------------------------------------------- #
# S18 — Subprocess/IO-Robustheit (Codex-M7)                                   #
# --------------------------------------------------------------------------- #


def test_s18b_non_git_repo_clean_fail(tmp_path: Path):
    """S18b: cwd ist kein git-Repo → sauberer FAIL P1, kein Python-Traceback."""
    r = _run_validator(["pipeline-item"], cwd=tmp_path)
    assert "Traceback" not in r.stderr, f"unexpected traceback in stderr: {r.stderr}"
    assert "Traceback" not in r.stdout, f"unexpected traceback in stdout: {r.stdout}"
    assert r.returncode == 1, f"expected exit=1 (P1), got {r.returncode}"


def test_s18d_missing_yaml_no_traceback(tmp_path: Path):
    """S18d: yaml-File missing → kein Python-Traceback (FAIL akzeptabel).

    Simuliert via Aufruf aus temp_repo OHNE event_typ_mapping.yaml im erwarteten Pfad.
    """
    subprocess.run(["git", "init", "-q"], cwd=str(tmp_path), check=True)
    r = _run_validator(["pipeline-item"], cwd=tmp_path)
    combined = r.stderr + r.stdout
    assert "Traceback" not in combined, f"unexpected traceback: {combined}"


def test_validator_help_renders():
    """Sanity: --help rendert argparse-usage ohne Exception."""
    r = _run_validator(["--help"])
    assert r.returncode == 0
    assert "para18_sync" in r.stdout
    assert "--also" in r.stdout
    assert "--verify-b" in r.stdout


def test_validator_no_args_exit_p2():
    """Sanity: no-args → FAIL P2 exit=2 (event_type required)."""
    r = _run_validator([])
    assert r.returncode == 2, f"expected exit=2 (P2), got {r.returncode}"
    assert "P2" in r.stderr


def test_flag_event_only_on_score_event():
    """Sanity: --flag-event auf pipeline-item → FAIL P2."""
    r = _run_validator(["pipeline-item", "--flag-event"])
    assert r.returncode == 2
    assert "P2" in r.stderr


# --------------------------------------------------------------------------- #
# S11 + S17 — P1 Ordering-Guard + Ticker-Identity (Codex-H3)                  #
# --------------------------------------------------------------------------- #


def _today() -> str:
    return time.strftime("%Y-%m-%d", time.localtime())


def _seed_score_history(repo: Path, *, ticker: str, date_iso: str) -> None:
    """Helper: lege minimal-valid score_history.jsonl mit date_iso + ticker an."""
    (repo / "00_Core").mkdir(exist_ok=True)
    (repo / "00_Core" / "score_history.jsonl").write_text(
        json.dumps({"timestamp": f"{date_iso}T11:00:00", "ticker": ticker}) + "\n",
        encoding="utf-8",
    )


def test_s11_score_event_stale_head(temp_repo: Path):
    """S11: score_history HEAD = gestern → FAIL P1 exit=1."""
    _seed_score_history(temp_repo, ticker="V", date_iso="2020-01-01")
    r = _run_validator(["score-flag-sparraten", "--ticker", "V"], cwd=temp_repo)
    assert r.returncode == 1, (
        f"expected exit=1 (P1 stale-HEAD), got {r.returncode} "
        f"stdout={r.stdout!r} stderr={r.stderr!r}"
    )
    assert "P1" in r.stderr
    assert "nicht heute" in r.stderr or "HEAD-date" in r.stderr


def test_s17_wrong_ticker_same_day(temp_repo: Path):
    """S17 (Codex-H3): HEAD-Append heute aber HEAD-Ticker != --ticker → FAIL P1."""
    _seed_score_history(temp_repo, ticker="TMO", date_iso=_today())
    r = _run_validator(["score-flag-sparraten", "--ticker", "V"], cwd=temp_repo)
    assert r.returncode == 1, (
        f"expected exit=1 (P1 wrong-ticker H3), got {r.returncode} "
        f"stdout={r.stdout!r} stderr={r.stderr!r}"
    )
    assert "P1" in r.stderr
    assert "H3" in r.stderr or "Ticker" in r.stderr


def test_s11b_score_event_missing_jsonl(temp_repo: Path):
    """S11b: score_history.jsonl fehlt komplett → FAIL P1 ohne Traceback."""
    r = _run_validator(["score-flag-sparraten", "--ticker", "V"], cwd=temp_repo)
    assert r.returncode == 1
    assert "Traceback" not in r.stderr + r.stdout
    assert "leer/fehlt" in r.stderr or "Pflicht" in r.stderr
