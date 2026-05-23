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
