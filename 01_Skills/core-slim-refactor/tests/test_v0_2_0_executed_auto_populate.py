"""v0.2.0 P7b Executed-Auto-Populate -- Spec SS3.3, AC3/AC3b/AC4/AC4b-f.

Disziplin-Regel #4: Alle Fixtures nutzen make_minimal_valid_cfg_yaml-Helper
(keine inline-YAMLs ohne Required-Fields).

Advisor-Drift-Korrekturen vs Plan-v1:
- _run(): positional arg (kein '--config'), CORE_SLIM_REFACTOR_SKIP_GATE=1 im env
- _make_minimal_setup: Helper statt inline-textwrap.dedent (Required-Fields-Pflicht)
- Exit-13 (EXIT_BOOKKEEPING_FAILED) -- Plan-Kommentar "Exit-12" war Tippfehler, Code korrekt 13
- P7b-Call-Site: nach phase_p7-OK, vor _cleanup_backup_on_success (archive_path Variable)
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "core_slim_refactor.py"

# _helpers Import (Disziplin-Regel #4)
sys.path.insert(0, str(ROOT / "tests"))
from _helpers import make_minimal_valid_cfg_yaml  # noqa: E402


def _make_minimal_setup(tmp_path: Path):
    """Liefert (cfg_path, target_path, archive_path) mit date-cut-Szenario.

    Disziplin-Regel #4: Uses make_minimal_valid_cfg_yaml Helper statt inline-YAML
    (inline textwrap.dedent fehlen Required-Fields, failen an _check_required_fields).
    """
    target = tmp_path / "target.md"
    target.write_text(
        "## 2026-05-10\nA\n## 2026-05-20\nB\n",
        encoding="utf-8",
        newline="\n",
    )
    archive = tmp_path / "archive.md"
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=target,
        archive_path=archive,
        schema_version=1,
        cut_before="2026-05-15",
        field="header",
        executed=None,
    )
    return cfg, target, archive


def _run(cfg: Path, *extra) -> subprocess.CompletedProcess:
    """Subprocess-Run mit P7-Gate-Bypass (CORE_SLIM_REFACTOR_SKIP_GATE=1).

    Advisor-Drift #1: positional arg (kein '--config' Prefix -- argparse ist positional).
    Advisor-Drift #2: SKIP_GATE env var -- sonst P7 fail-close mit EXIT_GATE_FAIL=8.
    """
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(cfg), *extra],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "CORE_SLIM_REFACTOR_SKIP_GATE": "1"},
        check=False,
    )


# ---------------------------------------------------------------------------
# AC3 -- Live-Run populates executed-Block
# ---------------------------------------------------------------------------


def test_live_run_populates_executed_block(tmp_path):
    cfg, _, _ = _make_minimal_setup(tmp_path)
    res = _run(cfg)
    assert res.returncode == 0, f"stderr={res.stderr!r}\nstdout={res.stdout!r}"
    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    ex = data["executed"]
    assert ex is not None, "executed block must be populated after live-run"
    assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", ex["timestamp"])
    assert re.match(r"^[0-9a-f]{64}$", ex["reference_archive_sha"])
    assert ex["commit_sha"] == "pending"


# ---------------------------------------------------------------------------
# AC4 -- --dry-run skips write-back
# ---------------------------------------------------------------------------


def test_dry_run_skips_writeback(tmp_path):
    cfg, _, _ = _make_minimal_setup(tmp_path)
    before = cfg.read_bytes()
    res = _run(cfg, "--dry-run")
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    assert cfg.read_bytes() == before, "dry-run must NOT mutate config"


# ---------------------------------------------------------------------------
# AC4b -- --dry-run --force-rerun BOTH skips (F-01 invariant: dry-run wins)
# ---------------------------------------------------------------------------


def test_dry_run_with_force_rerun_still_skips_writeback(tmp_path):
    cfg, _, _ = _make_minimal_setup(tmp_path)
    # Pre-populate executed to test re-run path
    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    data["executed"] = {
        "timestamp": "2026-01-01T00:00:00Z",
        "reference_archive_sha": "0" * 64,
        "commit_sha": "pending",
    }
    cfg.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8", newline="\n")
    before = cfg.read_bytes()
    res = _run(cfg, "--dry-run", "--force-rerun")
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    assert cfg.read_bytes() == before, "dry-run invariant takes precedence over --force-rerun"


# ---------------------------------------------------------------------------
# AC4c -- Live --force-rerun refreshes executed
# ---------------------------------------------------------------------------


def test_live_force_rerun_refreshes_executed(tmp_path):
    cfg, _, _ = _make_minimal_setup(tmp_path)
    # Pre-populate executed block with known stale values
    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    data["executed"] = {
        "timestamp": "2026-01-01T00:00:00Z",
        "reference_archive_sha": "0" * 64,
        "commit_sha": "pending",
    }
    cfg.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8", newline="\n")
    res = _run(cfg, "--force-rerun")
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    data2 = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    assert data2["executed"]["timestamp"] != "2026-01-01T00:00:00Z", "timestamp must be refreshed"
    assert data2["executed"]["reference_archive_sha"] != "0" * 64, "sha must be refreshed"


# ---------------------------------------------------------------------------
# AC4f -- --skip-executed-writeback flag keeps config unchanged
# ---------------------------------------------------------------------------


def test_skip_executed_writeback_flag(tmp_path):
    cfg, _, _ = _make_minimal_setup(tmp_path)
    before = cfg.read_bytes()
    res = _run(cfg, "--skip-executed-writeback")
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    assert cfg.read_bytes() == before, "--skip-executed-writeback must keep config unchanged"


# ---------------------------------------------------------------------------
# AC3b -- commit_sha is 'pending' literal on first run
# ---------------------------------------------------------------------------


def test_commit_sha_pending_literal_on_first_run(tmp_path):
    cfg, _, _ = _make_minimal_setup(tmp_path)
    _run(cfg)
    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    assert data["executed"]["commit_sha"] == "pending"


# ---------------------------------------------------------------------------
# AC4d -- Bookkeeping-Fail Exit-13 + Sidecar-Lock
# Direct Unit-Test via monkeypatch (no subprocess -- monkeypatch nicht in child-process)
# ---------------------------------------------------------------------------


def test_bookkeeping_fail_exit13_and_sidecar_lock(tmp_path, monkeypatch):
    """Simuliert atomaren os.replace-Fehler -> Exit-13 + Sidecar .executed-pending."""
    import importlib
    import os as _os

    cfg, _, _archive = _make_minimal_setup(tmp_path)

    # sys.path must be set BEFORE import (import executes at parse-time in CPython)
    script_dir = str(ROOT / "scripts")
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

    import core_slim_refactor as csr

    importlib.reload(csr)  # ensure fresh state

    def _raise_oserror(*a, **kw):
        raise OSError("simulated atomic-rename IO-Error")

    monkeypatch.setattr(_os, "replace", _raise_oserror)

    meta = {
        "timestamp": "2026-05-24T12:00:00Z",
        "reference_archive_sha": "a" * 64,
    }
    with pytest.raises(SystemExit) as ei:
        csr._phase_p7b_writeback_executed(cfg, meta)
    assert ei.value.code == 13, f"expected EXIT_BOOKKEEPING_FAILED=13, got {ei.value.code}"
    sidecar = cfg.with_suffix(cfg.suffix + ".executed-pending")
    assert sidecar.exists(), "Sidecar .executed-pending must be created on bookkeeping failure"
    side_data = yaml.safe_load(sidecar.read_text(encoding="utf-8"))
    assert side_data["timestamp"] == meta["timestamp"]
    assert side_data["reference_archive_sha"] == meta["reference_archive_sha"]
    assert side_data.get("commit_sha") == "pending"
    assert "_error" in side_data, "Sidecar must record _error field for User-Recovery-Path"


# ---------------------------------------------------------------------------
# AC4e -- PyYAML Comment-Loss documented behavior (Q1-Verdict)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# AC4g -- Sidecar-Lock cleared after successful --force-rerun (Lifecycle)
# ---------------------------------------------------------------------------


def test_sidecar_cleared_after_successful_force_rerun(tmp_path):
    """Advisor-Gap: stale .executed-pending must be cleaned up on successful write.
    --force-rerun scenario: prior F-03 left sidecar, operator re-runs with --force-rerun.
    After successful P7b write-back the sidecar must be unlinked.
    """
    cfg, _, _ = _make_minimal_setup(tmp_path)
    # Pre-populate executed block so --force-rerun is needed (guard at P1 rejects re-run)
    data = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    data["executed"] = {
        "timestamp": "2026-01-01T00:00:00Z",
        "reference_archive_sha": "0" * 64,
        "commit_sha": "pending",
    }
    cfg.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8", newline="\n")
    # Simulate a stale sidecar from a prior F-03 bookkeeping failure
    sidecar = cfg.with_suffix(cfg.suffix + ".executed-pending")
    sidecar.write_text("# stale sidecar from prior F-03\n", encoding="utf-8", newline="\n")
    assert sidecar.exists(), "precondition: stale sidecar must exist before run"
    res = _run(cfg, "--force-rerun")
    assert res.returncode == 0, f"stderr={res.stderr!r}\nstdout={res.stdout!r}"
    assert not sidecar.exists(), "sidecar must be unlinked after successful P7b write-back"
    # Config must have refreshed executed block
    data2 = yaml.safe_load(cfg.read_text(encoding="utf-8"))
    assert data2["executed"]["timestamp"] != "2026-01-01T00:00:00Z"


def test_pyyaml_comment_loss_accepted(tmp_path):
    """Q1-Verdict: PyYAML safe_dump loescht YAML-Kommentare beim Write-Back.
    Dieses Verhalten ist akzeptiert (ruamel.yaml v0.3-TODO).
    """
    cfg, _, _ = _make_minimal_setup(tmp_path)
    # Prepend a comment that will be lost after write-back
    body = cfg.read_text(encoding="utf-8")
    cfg.write_text(
        "# This comment will be LOST in v0.2.0 (Q1-Verdict, ruamel.yaml v0.3-TODO)\n" + body,
        encoding="utf-8",
        newline="\n",
    )
    res = _run(cfg)
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    new_body = cfg.read_text(encoding="utf-8")
    assert "# This comment will be LOST" not in new_body  # documented loss
