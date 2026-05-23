import os
import shutil
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_DIR / "scripts"
ENTRY = SCRIPTS_DIR / "core_slim_refactor.py"
FIXTURES = SKILL_DIR / "tests" / "fixtures"


def _run(args: list[str], cwd: Path | None = None, env: dict | None = None):
    full_env = dict(os.environ)
    if env:
        full_env.update(env)
    return subprocess.run(
        [sys.executable, str(ENTRY), *args],
        cwd=cwd or SKILL_DIR,
        capture_output=True,
        text=True,
        env=full_env,
        check=False,
    )


def _write_throwaway_config(tmp_path, target_md):
    cfg = f"""schema_version: 1
profile_name: e2e-test
executed: null
target:
  file: {target_md}
  section: null
  section_anchor_alt: null
  append_only_immutable: false
pattern: bucket-archive
bucket_archive:
  classify:
    by: keyword
    keywords: ["Ruflo"]
    keep_keywords: []
    case_sensitive: true
  archive:
    path: {tmp_path / "arch.md"}
    header_template: |
      # Test Archive
      Cut: {{timestamp}}
      Source: {{target_file}} {{section}}
      Total Rows: {{n_rows}}
  pointer:
    insert_at: chronological
    template: "| {{pointer_date}} | RUFLO archived | {{n_rows}} | [a]({{archive_link}}) |"
backlink_scan:
  scan_paths: []
  search_terms: []
  on_match: warn_continue
  skip_override_allowed: true
audit:
  pre_run: false
  pre_run_pass_threshold: pass
  post_run_hint: false
  fail_close_on_drift: false
retry_policy:
  max_identical_phase_failures: 2
  identity_key: ["phase", "exception_class"]
"""
    cfg_path = tmp_path / "cfg.yaml"
    cfg_path.write_text(cfg, encoding="utf-8", newline="")
    return cfg_path


def test_dry_run_outputs_no_files(tmp_path):
    target = tmp_path / "target.md"
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target)
    cfg = _write_throwaway_config(tmp_path, str(target))
    result = _run([str(cfg), "--dry-run", "--skip-audit"])
    assert result.returncode == 0, f"stderr: {result.stderr}\nstdout: {result.stdout}"
    assert not (tmp_path / "arch.md").exists()
    assert target.read_text(encoding="utf-8") == (FIXTURES / "bucket_archive_sample.md").read_text(
        encoding="utf-8"
    )


def test_live_run_mutates_target_and_writes_archive(tmp_path):
    target = tmp_path / "target.md"
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target)
    cfg = _write_throwaway_config(tmp_path, str(target))
    result = _run([str(cfg), "--skip-audit"])
    assert result.returncode == 0, f"stderr: {result.stderr}\nstdout: {result.stdout}"
    assert (tmp_path / "arch.md").exists()
    new_content = target.read_text(encoding="utf-8")
    assert "Ruflo Sunset begin" not in new_content
    assert "RUFLO archived" in new_content


def test_rerun_guard_blocks_executed_without_force(tmp_path):
    target = tmp_path / "target.md"
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target)
    cfg = _write_throwaway_config(tmp_path, str(target))
    cfg_text = cfg.read_text(encoding="utf-8")
    cfg_text = cfg_text.replace(
        "executed: null",
        'executed:\n  timestamp: "2026-05-23T11:30:00Z"\n  commit_sha: "abc1234"\n  reference_archive_sha: "sha256:test"',
    )
    cfg.write_text(cfg_text, encoding="utf-8", newline="")
    result = _run([str(cfg), "--skip-audit"])
    assert result.returncode == 2, (
        f"expected exit 2 (config error), got {result.returncode}\n{result.stderr}"
    )
    assert "executed" in (result.stderr + result.stdout).lower()


def test_backup_restored_on_p5_simulated_fail(tmp_path):
    target = tmp_path / "target.md"
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target)
    original = target.read_text(encoding="utf-8")
    cfg = _write_throwaway_config(tmp_path, str(target))
    result = _run(
        [str(cfg), "--skip-audit"],
        env={"CORE_SLIM_REFACTOR_FORCE_FAIL_PHASE": "P5"},
    )
    assert result.returncode == 7
    assert target.read_text(encoding="utf-8") == original


def test_backup_restored_on_p7_sysexit(tmp_path):
    """CP18 HIGH-1 regression: P7 gate-fail signals via SystemExit (BaseException),
    not Exception. Rollback site must catch BOTH for atomicity to hold."""
    target = tmp_path / "target.md"
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target)
    original = target.read_text(encoding="utf-8")
    cfg = _write_throwaway_config(tmp_path, str(target))
    result = _run(
        [str(cfg), "--skip-audit"],
        env={"CORE_SLIM_REFACTOR_FORCE_FAIL_PHASE": "P7_SYSEXIT"},
    )
    assert result.returncode == 8, (
        f"expected exit 8 (gate-fail), got {result.returncode}\n{result.stderr}"
    )
    assert target.read_text(encoding="utf-8") == original, (
        "P7 SystemExit must trigger rollback — target was not restored"
    )
    assert not (tmp_path / "arch.md").exists(), "P7 rollback must cleanup partial archive"


def test_dry_run_matches_live_for_bucket_archive(tmp_path):
    """AK2 (Spec section 5.4): dry-run output describes the same delta as live run."""
    import re

    target_live = tmp_path / "live.md"
    target_dry = tmp_path / "dry.md"
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target_live)
    shutil.copy(FIXTURES / "bucket_archive_sample.md", target_dry)

    cfg_live = _write_throwaway_config(tmp_path, str(target_live))
    cfg_dry = tmp_path / "cfg_dry.yaml"
    cfg_dry.write_text(
        cfg_live.read_text(encoding="utf-8")
        .replace(str(target_live), str(target_dry))
        .replace(str(tmp_path / "arch.md"), str(tmp_path / "arch_dry.md")),
        encoding="utf-8",
        newline="",
    )

    r_live = _run([str(cfg_live), "--skip-audit"])
    assert r_live.returncode == 0, f"live: {r_live.stderr}"
    live_archive = (tmp_path / "arch.md").read_text(encoding="utf-8")

    r_dry = _run([str(cfg_dry), "--skip-audit", "--dry-run"])
    assert r_dry.returncode == 0, f"dry: {r_dry.stderr}"
    # Dry-run must NOT have written files
    assert not (tmp_path / "arch_dry.md").exists()
    assert target_dry.read_text(encoding="utf-8") == (
        FIXTURES / "bucket_archive_sample.md"
    ).read_text(encoding="utf-8")
    # Dry-run stdout MUST report row-count + bytes that match the live archive
    m = re.search(r"would write .* \((\d+) bytes, (\d+) rows\)", r_dry.stdout)
    assert m, f"dry-run output missing 'would write ...': {r_dry.stdout}"
    dry_bytes = int(m.group(1))
    dry_rows = int(m.group(2))
    live_rows = len([ln for ln in live_archive.splitlines() if ln.startswith("|")])
    assert dry_rows == live_rows, f"row-count mismatch: dry={dry_rows} live={live_rows}"
    # Timestamp + computed-relative-path differ between dry/live; tolerate ±200 bytes
    assert abs(dry_bytes - len(live_archive.encode("utf-8"))) <= 200, (
        f"byte-count drift >200: dry={dry_bytes} live={len(live_archive.encode('utf-8'))}"
    )
