"""Smoke-Test-Suite für paragraph-18-sync validator (S1-S20, Spec §6).

Run: python -m pytest 03_Tools/para18_sync/_smoke_test.py -v
"""

from __future__ import annotations

import os
import subprocess
import sys
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


@pytest.mark.xfail(
    reason="P1 _is_git_repo()-Gate in main() noch nicht verdrahtet — fixt in Task 5 (Phase 4 P1)",
    strict=False,
)
def test_s18b_non_git_repo_clean_fail(tmp_path: Path):
    """S18b: cwd ist kein git-Repo → sauberer FAIL, kein Python-Traceback.

    TDD-Interleave: dieser Test ist Test-first für Task 5 P1-Verdrahtung.
    Wichtige Robustheits-Invariante (auch in Skeleton-State): kein Traceback.
    """
    r = _run_validator(["pipeline-item"], cwd=tmp_path)
    assert "Traceback" not in r.stderr, f"unexpected traceback in stderr: {r.stderr}"
    assert "Traceback" not in r.stdout, f"unexpected traceback in stdout: {r.stdout}"
    assert r.returncode != 0, f"expected non-zero exit (P1 missing), got {r.returncode}"


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
