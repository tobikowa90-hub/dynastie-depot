"""v0.1.1 bugfix-tests (PIPELINE #80).

HIGH-1  pointer-context absolute-path leak (L264-276)
HIGH-3  audit.fail_close_on_drift default flip True -> False (L112)
HIGH-4  P0+P7 subprocess UTF-8 encoding + None-guard (L104-111 / L349-357)
MED-NEW P2 diagnostic + EXIT_ANCHOR_NOT_FOUND split (11 vs 4)
HIGH-2  Backup-lifecycle regression anchors (no code-bug; docs only)

Iron-Law: each test fails on current main (TDD-Red); fixes follow in subsequent
commits. See PIPELINE #80 body for scope + Karpathy 2-Phase rationale.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import core_slim_refactor as csr  # noqa: E402
from config import ConfigObject  # noqa: E402
from patterns import RowSet  # noqa: E402

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _make_cfg(tmp_path: Path, **overrides) -> ConfigObject:
    """Minimal ConfigObject for unit tests of individual phases."""
    audit = {"pre_run": True}
    audit.update(overrides.get("audit", {}))
    return ConfigObject(
        raw={},
        path=tmp_path / "fake.yaml",
        schema_version=1,
        profile_name="test",
        executed=None,
        target={"file": "target.md", "section": None},
        pattern="bucket-archive",
        pattern_block={
            "classify": {"by": "keyword", "keywords": [], "keep_keywords": []},
            "archive": {"path": str(tmp_path / "arch.md")},
        },
        backlink_scan={"scan_paths": [], "search_terms": [], "on_match": "warn_continue"},
        audit=audit,
        retry_policy={},
    )


def _args(**overrides) -> argparse.Namespace:
    base = {"dry_run": False, "skip_audit": False, "force_rerun": False}
    base.update(overrides)
    return argparse.Namespace(**base)


def _setup_target(tmp_path: Path, content: str = "# Target\n") -> Path:
    target = tmp_path / "target.md"
    target.write_text(content, encoding="utf-8", newline="")
    return target


def _setup_fake_audit(repo_root: Path) -> Path:
    """Place a fake system_audit.py inside fake repo_root/03_Tools/."""
    tools = repo_root / "03_Tools"
    tools.mkdir(parents=True, exist_ok=True)
    audit = tools / "system_audit.py"
    audit.write_text("import sys; sys.stdout.write('FAKE\\n'); sys.exit(0)\n", encoding="utf-8")
    return audit


# ---------------------------------------------------------------------------
# HIGH-4: subprocess UTF-8 encoding + None-guard
# ---------------------------------------------------------------------------


def test_high4_p0_subprocess_uses_utf8_encoding(monkeypatch, tmp_path):
    """phase_p0 MUST pass encoding='utf-8', errors='replace' to subprocess.run."""
    _setup_target(tmp_path)
    _setup_fake_audit(tmp_path)
    captured = {}

    def fake_run(*args, **kwargs):
        captured.update(kwargs)
        return SimpleNamespace(returncode=0, stdout="ok\n", stderr="")

    monkeypatch.setattr(csr.subprocess, "run", fake_run)
    cfg = _make_cfg(tmp_path)
    csr.phase_p0(cfg, _args(), tmp_path)

    assert captured.get("encoding") == "utf-8", (
        f"P0 missing encoding=utf-8 (got {captured.get('encoding')!r})"
    )
    assert captured.get("errors") == "replace", (
        f"P0 missing errors=replace (got {captured.get('errors')!r})"
    )


def test_high4_p0_none_stdout_guarded(monkeypatch, tmp_path):
    """phase_p0 must not crash if subprocess.run returns stdout=None."""
    _setup_target(tmp_path)
    _setup_fake_audit(tmp_path)

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=0, stdout=None, stderr=None)

    monkeypatch.setattr(csr.subprocess, "run", fake_run)
    cfg = _make_cfg(tmp_path)
    # Must not raise TypeError on sys.stdout.write(None)
    csr.phase_p0(cfg, _args(), tmp_path)


def test_high4_p7_subprocess_uses_utf8_encoding(monkeypatch, tmp_path):
    """phase_p7 MUST pass encoding='utf-8', errors='replace' to subprocess.run."""
    _setup_target(tmp_path)
    # Place fake p18 script so we hit the subprocess path
    p18_dir = tmp_path / "01_Skills" / "paragraph-18-sync" / "scripts"
    p18_dir.mkdir(parents=True, exist_ok=True)
    (p18_dir / "p18_sync.py").write_text("# fake\n", encoding="utf-8")
    captured = {}

    def fake_run(*args, **kwargs):
        captured.update(kwargs)
        return SimpleNamespace(returncode=0, stdout='{"status":"PASS"}', stderr="")

    monkeypatch.setattr(csr.subprocess, "run", fake_run)
    cfg = _make_cfg(tmp_path)
    baseline = {
        "target_path": tmp_path / "target.md",
        "backup_path": tmp_path / "target.md.pre-refactor.bak",
        "target_sha": "deadbeef",
    }
    csr.phase_p7(cfg, tmp_path, _args(dry_run=False), baseline)

    assert captured.get("encoding") == "utf-8", (
        f"P7 missing encoding=utf-8 (got {captured.get('encoding')!r})"
    )
    assert captured.get("errors") == "replace", (
        f"P7 missing errors=replace (got {captured.get('errors')!r})"
    )


def test_high4_p7_none_stdout_guarded(monkeypatch, tmp_path):
    """phase_p7 must not crash if subprocess.run returns stdout=None."""
    _setup_target(tmp_path)
    p18_dir = tmp_path / "01_Skills" / "paragraph-18-sync" / "scripts"
    p18_dir.mkdir(parents=True, exist_ok=True)
    (p18_dir / "p18_sync.py").write_text("# fake\n", encoding="utf-8")

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=0, stdout=None, stderr=None)

    monkeypatch.setattr(csr.subprocess, "run", fake_run)
    cfg = _make_cfg(tmp_path)
    baseline = {
        "target_path": tmp_path / "target.md",
        "backup_path": tmp_path / "target.md.pre-refactor.bak",
        "target_sha": "deadbeef",
    }
    # rc=0 + stdout=None -> after None-guard + json.loads('') -> json-parse-error -> SystemExit(GATE_FAIL)
    # Acceptable: must NOT raise TypeError. SystemExit on gate-fail is by-design.
    with pytest.raises(SystemExit) as exc:
        csr.phase_p7(cfg, tmp_path, _args(dry_run=False), baseline)
    assert exc.value.code == csr.EXIT_GATE_FAIL


# ---------------------------------------------------------------------------
# HIGH-3: audit.fail_close_on_drift default False (advisory)
# ---------------------------------------------------------------------------


def test_high3_fail_close_default_advisory(monkeypatch, tmp_path):
    """When audit.fail_close_on_drift is unset, default MUST be advisory (no exit)."""
    _setup_target(tmp_path)
    _setup_fake_audit(tmp_path)

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=1, stdout="drift\n", stderr="")

    monkeypatch.setattr(csr.subprocess, "run", fake_run)
    cfg = _make_cfg(tmp_path, audit={"pre_run": True})  # no fail_close_on_drift key
    # Must NOT raise SystemExit(EXIT_AUDIT); should warn and continue.
    csr.phase_p0(cfg, _args(), tmp_path)


def test_high3_fail_close_explicit_true_still_fails(monkeypatch, tmp_path):
    """Explicit opt-in fail_close_on_drift=true must still enforce."""
    _setup_target(tmp_path)
    _setup_fake_audit(tmp_path)

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=1, stdout="drift\n", stderr="")

    monkeypatch.setattr(csr.subprocess, "run", fake_run)
    cfg = _make_cfg(tmp_path, audit={"pre_run": True, "fail_close_on_drift": True})
    with pytest.raises(SystemExit) as exc:
        csr.phase_p0(cfg, _args(), tmp_path)
    assert exc.value.code == csr.EXIT_AUDIT


# ---------------------------------------------------------------------------
# HIGH-1: pointer-context absolute-path leak
# ---------------------------------------------------------------------------


def test_high1_pointer_context_no_absolute_paths(tmp_path):
    """pointer_context must NOT contain absolute Windows/POSIX paths for archive_path or target_file."""
    target = _setup_target(tmp_path, "# T\n- item\n")
    archive_path = tmp_path / "05_Archiv" / "arch.md"
    archive_path.parent.mkdir(parents=True, exist_ok=True)

    cfg = _make_cfg(tmp_path)
    baseline = {
        "target_path": target,
        "backup_path": target.with_suffix(".md.pre-refactor.bak"),
        "target_sha": "deadbeef",
    }

    rs = RowSet(archive=["- item\n"], keep=[], slim_targets=[])
    pctx = csr._build_pointer_context(
        cfg=cfg,
        rowset=rs,
        archive_path=archive_path,
        timestamp="2026-05-23T22:00:00+00:00",
        baseline=baseline,
    )

    for key in ("archive_path", "target_file", "archive_link"):
        val = pctx.get(key, "")
        assert not Path(val).is_absolute(), (
            f"pointer_context[{key!r}]={val!r} is absolute; expected relative"
        )


# ---------------------------------------------------------------------------
# MED-NEW: P2 diagnostic + EXIT_ANCHOR_NOT_FOUND (11) split
# ---------------------------------------------------------------------------


def test_mednew_exit_anchor_not_found_constant_exists():
    """EXIT_ANCHOR_NOT_FOUND = 11 must exist and differ from EXIT_CLASSIFY_EMPTY (4) and EXIT_MIGRATE_VIOLATION (5)."""
    assert hasattr(csr, "EXIT_ANCHOR_NOT_FOUND"), "EXIT_ANCHOR_NOT_FOUND not defined"
    assert csr.EXIT_ANCHOR_NOT_FOUND == 11
    assert csr.EXIT_CLASSIFY_EMPTY == 4
    assert csr.EXIT_MIGRATE_VIOLATION == 5


def test_mednew_p2_anchor_not_found_emits_exit_11(tmp_path):
    """When configured anchor is not present in target, exit code must be 11, not 4."""
    target = _setup_target(tmp_path, "# Header\n- row a\n- row b\n")
    cfg = _make_cfg(tmp_path)
    # Override target to point at a section that doesn't exist
    cfg.target = {"file": "target.md", "section": "## Nonexistent-Anchor"}

    with pytest.raises(SystemExit) as exc:
        csr.phase_p2(cfg, target.read_text(encoding="utf-8"))
    assert exc.value.code == csr.EXIT_ANCHOR_NOT_FOUND, (
        f"expected EXIT_ANCHOR_NOT_FOUND=11, got {exc.value.code}"
    )


def test_mednew_p2_classify_empty_emits_diagnostic(capsys, tmp_path):
    """P2 FAIL must emit a stderr diagnostic with classify stats (n_archive/n_slim/anchor)."""
    target = _setup_target(tmp_path, "# Header\n- nothing-matches-here\n")
    cfg = _make_cfg(tmp_path)
    # No anchor, but keywords don't match -> empty classify result -> EXIT_CLASSIFY_EMPTY
    cfg.pattern_block["classify"]["keywords"] = ["RufloDoesNotMatch"]

    with pytest.raises(SystemExit):
        csr.phase_p2(cfg, target.read_text(encoding="utf-8"))

    captured = capsys.readouterr()
    combined = captured.err + captured.out
    assert "n_archive" in combined or "n_matches" in combined, (
        f"P2 FAIL diagnostic missing classify stats; got:\n{combined}"
    )


# ---------------------------------------------------------------------------
# HIGH-2: Backup-lifecycle regression anchors (no code-fix; docs only)
# ---------------------------------------------------------------------------


def test_high2_backup_skipped_in_dry_run(tmp_path):
    """--dry-run must not write a .pre-refactor.bak file (by-design, documented behavior)."""
    _setup_target(tmp_path)
    _setup_fake_audit(tmp_path)
    cfg = _make_cfg(tmp_path, audit={"pre_run": False})
    baseline = csr.phase_p0(cfg, _args(dry_run=True), tmp_path)
    assert not baseline["backup_path"].exists(), (
        f"dry-run produced unexpected backup file at {baseline['backup_path']}"
    )


def test_high2_backup_created_in_non_dry_run(tmp_path):
    """non-dry P0 must create the backup file at baseline['backup_path']."""
    _setup_target(tmp_path, "ABC")
    cfg = _make_cfg(tmp_path, audit={"pre_run": False})
    baseline = csr.phase_p0(cfg, _args(dry_run=False), tmp_path)
    assert baseline["backup_path"].exists()
    assert baseline["backup_path"].read_text(encoding="utf-8") == "ABC"
