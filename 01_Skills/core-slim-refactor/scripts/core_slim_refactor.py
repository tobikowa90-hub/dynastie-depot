"""core-slim-refactor v0.1 - Entry-point + 8-Phase orchestration.

Spec: docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as _dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from backlink import BacklinkReport, scan_backlinks  # noqa: E402
from config import ConfigError, ConfigObject, load_config  # noqa: E402
from patterns import (  # noqa: E402
    RowSet,
    classify_bucket_archive,
    classify_date_cut,
    classify_slim_convention,
    mutate_bucket_archive,
    mutate_date_cut,
    mutate_slim_convention,
)

# Exit codes per spec §4.1
EXIT_OK = 0
EXIT_CONFIG = 2
EXIT_AUDIT = 3
EXIT_CLASSIFY_EMPTY = 4
EXIT_MIGRATE_VIOLATION = 5
EXIT_BACKLINK_HIT = 6
EXIT_WRITE_ERROR = 7
EXIT_GATE_FAIL = 8
EXIT_REFERENCE_MISMATCH = 10
EXIT_APPROACH_RESET = 99


def _emit_phase(name: str, status: str) -> None:
    sys.stdout.write(f"=== {name} {status} ===\n")
    sys.stdout.flush()


def _repo_root() -> Path:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        )
        return Path(r.stdout.strip())
    except subprocess.CalledProcessError, FileNotFoundError:
        return Path.cwd()


def _force_fail_phase() -> str | None:
    return os.environ.get("CORE_SLIM_REFACTOR_FORCE_FAIL_PHASE")


def _maybe_force_fail(phase: str) -> None:
    if _force_fail_phase() == phase:
        raise RuntimeError(f"forced fail at {phase} (test sentinel)")


# P0: Pre-Audit-Baseline


def phase_p0(cfg: ConfigObject, args: argparse.Namespace, repo_root: Path) -> dict:
    _emit_phase("P0 Pre-Audit-Baseline", "START")
    target = repo_root / cfg.target["file"]
    if not target.exists():
        raise FileNotFoundError(f"target does not exist: {target}")

    baseline = {
        "target_path": target,
        "target_size": target.stat().st_size,
        "target_sha": hashlib.sha256(target.read_bytes()).hexdigest()[:12],
        "backup_path": target.with_suffix(target.suffix + ".pre-refactor.bak"),
    }
    if not args.dry_run:
        shutil.copy2(target, baseline["backup_path"])

    if cfg.audit["pre_run"] and not args.skip_audit:
        audit_path = repo_root / "03_Tools" / "system_audit.py"
        if audit_path.exists():
            r = subprocess.run(
                [sys.executable, str(audit_path), "--core"],
                capture_output=True,
                text=True,
                cwd=str(repo_root),
                check=False,
            )
            sys.stdout.write(r.stdout)
            if r.returncode != 0 and cfg.audit.get("fail_close_on_drift", True):
                _emit_phase("P0 Pre-Audit-Baseline", "FAIL")
                raise SystemExit(EXIT_AUDIT)

    _maybe_force_fail("P0")
    _emit_phase("P0 Pre-Audit-Baseline", "OK")
    return baseline


# P1: Config executed-guard (load+validate handled in main)


def phase_p1_executed_guard(cfg: ConfigObject, args: argparse.Namespace) -> None:
    _emit_phase("P1 Config-Load + Validate", "START")
    if cfg.executed is not None and not args.force_rerun:
        _emit_phase("P1 Config-Load + Validate", "FAIL")
        raise ConfigError(
            f"config has executed={cfg.executed!r} populated; refusing re-run. "
            f"Use --force-rerun to override (post-hoc documentation use-case)."
        )
    _maybe_force_fail("P1")
    _emit_phase("P1 Config-Load + Validate", "OK")


# P2: Classify


def phase_p2(cfg: ConfigObject, target_md: str) -> RowSet:
    _emit_phase("P2 Classify", "START")
    pattern = cfg.pattern
    block = cfg.pattern_block
    anchor = cfg.target.get("section")

    if pattern == "bucket-archive":
        rs = classify_bucket_archive(target_md, anchor, block)
    elif pattern == "slim-convention":
        rs = classify_slim_convention(target_md, anchor, block)
    else:  # date-cut
        rs = classify_date_cut(target_md, anchor, block)

    if not rs.archive and not rs.slim_targets:
        _emit_phase("P2 Classify", "FAIL")
        raise SystemExit(EXIT_CLASSIFY_EMPTY)

    _maybe_force_fail("P2")
    _emit_phase("P2 Classify", "OK")
    return rs


# P3: Backlink-Scan


def phase_p3(cfg: ConfigObject, repo_root: Path) -> BacklinkReport:
    _emit_phase("P3 Backlink-Scan", "START")
    scan_cfg = cfg.backlink_scan
    scan_paths = [repo_root / p for p in scan_cfg["scan_paths"]]
    report = scan_backlinks(
        scan_paths=scan_paths,
        search_terms=scan_cfg["search_terms"],
        case_sensitive=True,
    )

    on_match = scan_cfg.get("on_match", "fail_close")
    if report.hits:
        sys.stderr.write(report.summary() + "\n")
        if on_match == "fail_close":
            if not scan_cfg.get("skip_override_allowed", False):
                _emit_phase("P3 Backlink-Scan", "FAIL")
                raise SystemExit(EXIT_BACKLINK_HIT)
            sys.stderr.write("WARNING: P3 fail_close-bypass via skip_override_allowed=true\n")
        elif on_match == "warn_continue":
            sys.stderr.write("WARNING: P3 backlink-hits, continuing per warn_continue\n")
        elif on_match == "skip_if_override":
            sys.stderr.write("WARNING: P3 skip_if_override active\n")

    _maybe_force_fail("P3")
    _emit_phase("P3 Backlink-Scan", "OK")
    return report


# P4: Archive-Write


def phase_p4(
    cfg: ConfigObject,
    rowset: RowSet,
    repo_root: Path,
    timestamp: str,
    args: argparse.Namespace,
    baseline: dict,
) -> Path | None:
    _emit_phase("P4 Archive-Write", "START")
    block = cfg.pattern_block
    archive_cfg = block.get("archive", {})
    archive_path_str = archive_cfg.get("path")
    if not archive_path_str:
        _emit_phase("P4 Archive-Write", "FAIL")
        raise ConfigError(f"pattern={cfg.pattern} missing archive.path")
    archive_path = Path(archive_path_str)
    if not archive_path.is_absolute():
        archive_path = repo_root / archive_path

    header_template = archive_cfg.get("header_template", "# Archive\n")
    archived_rows = rowset.archive
    n_rows = len(archived_rows)
    n_bytes = sum(len(r.encode("utf-8")) for r in archived_rows)
    cut_date = block.get("cut_before", timestamp[:10])

    header = header_template.format(
        timestamp=timestamp,
        target_file=str(baseline["target_path"]),
        section=cfg.target.get("section") or "(no anchor)",
        n_rows=n_rows,
        n_bytes=n_bytes,
        cut_date=cut_date,
    )
    body = "\n".join(archived_rows)
    archive_content = header + "\n" + body + "\n"

    if args.dry_run:
        sys.stdout.write(
            f"[dry-run] would write {archive_path} ({len(archive_content)} bytes, {n_rows} rows)\n"
        )
    else:
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with archive_path.open("w", encoding="utf-8", newline="") as f:
                f.write(archive_content)
        except OSError as e:
            _emit_phase("P4 Archive-Write", "FAIL")
            raise SystemExit(EXIT_WRITE_ERROR) from e

    _maybe_force_fail("P4")
    _emit_phase("P4 Archive-Write", "OK")
    return archive_path


# P5: Source-Mutation


def phase_p5(
    cfg: ConfigObject,
    target_md: str,
    rowset: RowSet,
    archive_path: Path,
    timestamp: str,
    args: argparse.Namespace,
    baseline: dict,
) -> str:
    _emit_phase("P5 Source-Mutation", "START")
    block = cfg.pattern_block
    anchor = cfg.target.get("section")
    archive_link = (
        os.path.relpath(archive_path, baseline["target_path"].parent) if archive_path else ""
    )
    pointer_context = {
        "pointer_date": timestamp[:10],
        "n_rows": len(rowset.archive),
        "archive_size_kb": f"{sum(len(r.encode('utf-8')) for r in rowset.archive) / 1024:.1f}",
        "archive_link": archive_link.replace("\\", "/"),
        "archive_path": str(archive_path),
        "cut_date": block.get("cut_before", timestamp[:10]),
        "timestamp": timestamp,
        "target_file": str(baseline["target_path"]),
    }

    try:
        if cfg.pattern == "bucket-archive":
            new_md = mutate_bucket_archive(target_md, anchor, rowset, block, pointer_context)
        elif cfg.pattern == "slim-convention":
            slim_context = {"archive_link": pointer_context["archive_link"]}
            new_md = mutate_slim_convention(target_md, anchor, rowset, block, slim_context)
        else:
            new_md = mutate_date_cut(target_md, anchor, rowset, block, pointer_context)
    except Exception:
        _emit_phase("P5 Source-Mutation", "FAIL")
        raise

    _maybe_force_fail("P5")

    if args.dry_run:
        sys.stdout.write(
            "[dry-run] target would change; diff omitted (see Build-Gate-3 reference-match)\n"
        )
    else:
        try:
            with baseline["target_path"].open("w", encoding="utf-8", newline="") as f:
                f.write(new_md)
        except OSError as e:
            _emit_phase("P5 Source-Mutation", "FAIL")
            raise SystemExit(EXIT_WRITE_ERROR) from e

    _emit_phase("P5 Source-Mutation", "OK")
    return new_md


# P6: Pointer/Header-Prose Updates (placeholder in v0.1)


def phase_p6(cfg: ConfigObject, args: argparse.Namespace) -> None:
    _emit_phase("P6 Pointer/Header-Prose", "START")
    _maybe_force_fail("P6")
    _emit_phase("P6 Pointer/Header-Prose", "OK")


# P7: Hybrid-Gate


def phase_p7(cfg: ConfigObject, repo_root: Path, args: argparse.Namespace, baseline: dict) -> None:
    _emit_phase("P7 Hybrid-Gate", "START")
    p18_script = repo_root / "01_Skills" / "paragraph-18-sync" / "scripts" / "p18_sync.py"
    if not p18_script.exists():
        p18_cmd = ["paragraph-18-sync", "system-zustand", "--dry-run", "--json"]
    else:
        p18_cmd = [sys.executable, str(p18_script), "system-zustand", "--dry-run", "--json"]

    if args.dry_run:
        sys.stdout.write(f"[dry-run] would run: {' '.join(p18_cmd)}\n")
    else:
        try:
            r = subprocess.run(
                p18_cmd, capture_output=True, text=True, cwd=str(repo_root), check=False
            )
            sys.stdout.write(r.stdout)
            if r.returncode != 0:
                try:
                    data = json.loads(r.stdout)
                    if data.get("status") != "PASS":
                        _emit_phase("P7 Hybrid-Gate", "FAIL")
                        raise SystemExit(EXIT_GATE_FAIL)
                except (json.JSONDecodeError, KeyError) as parse_err:
                    sys.stderr.write(f"§18-Skill returned {r.returncode}; treating as FAIL\n")
                    _emit_phase("P7 Hybrid-Gate", "FAIL")
                    raise SystemExit(EXIT_GATE_FAIL) from parse_err
        except FileNotFoundError:
            sys.stderr.write(
                "WARNING: paragraph-18-sync not found; skipping §18-gate (operative runs MUST resolve)\n"
            )

    sys.stdout.write(
        f"\n=== CODEX HAND-OFF BUNDLE ===\n"
        f"target: {baseline['target_path']}\n"
        f"backup: {baseline['backup_path']}\n"
        f"baseline_sha: {baseline['target_sha']}\n"
        f"commit_msg_template: refactor(slim): {cfg.profile_name} (PIPELINE-Anchor required, §18-Sync-Set required)\n"
        f"post_audit_cmd: python 03_Tools/system_audit.py --core\n"
        f"codex_diff_cmd: git diff > /tmp/slim-refactor-{cfg.profile_name}.diff && /codex:codex-rescue\n"
        f"=== END BUNDLE ===\n"
    )

    _maybe_force_fail("P7")
    _emit_phase("P7 Hybrid-Gate", "OK")


# Main Orchestration


def _emit_sparring_hint(
    phase: str, exc: Exception, failure_log: list, cfg: ConfigObject | None, baseline: dict
) -> None:
    cfg_path = cfg.path if cfg else "(unknown)"
    sys.stderr.write(
        "\n=== APPROACH-RESET HINT (Karpathy §0) ===\n"
        f"Phase failed: {phase}\n"
        f"Exception: {type(exc).__name__}: {exc}\n"
        f"Last failures: {failure_log}\n"
        f"Workspace snapshot: {baseline.get('target_path')}@{baseline.get('target_sha')}\n"
        f"Backup available: {baseline.get('backup_path')}\n"
        f"Config: {cfg_path}\n"
        "\nSuggested next steps:\n"
        "  1. Inspect failure: read traceback above + check target file\n"
        "  2. Codex diagnostic: git diff > /tmp/slim-fail.diff && /codex:codex-rescue\n"
        f"  3. Config adjustment: edit {cfg_path}\n"
        "  4. Plan-pivot: /superpowers:brainstorming\n"
        "=== END HINT ===\n\n"
    )


def _restore_backup(baseline: dict) -> None:
    bak = baseline.get("backup_path")
    tgt = baseline.get("target_path")
    if bak and bak.exists() and tgt:
        shutil.copy2(bak, tgt)
        sys.stderr.write(f"Restored target from backup: {bak} -> {tgt}\n")


def _cleanup_archive_on_fail(archive_path: Path | None) -> None:
    if archive_path and archive_path.exists():
        try:
            archive_path.unlink()
            sys.stderr.write(f"Cleaned partial archive: {archive_path}\n")
        except OSError:
            pass


def _cleanup_backup_on_success(baseline: dict) -> None:
    bak = baseline.get("backup_path")
    if bak and bak.exists():
        with contextlib.suppress(OSError):
            bak.unlink()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="core-slim-refactor", description="v0.1")
    parser.add_argument("config", help="path to YAML config")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-audit", action="store_true")
    parser.add_argument("--force-rerun", action="store_true")
    args = parser.parse_args(argv)

    timestamp = _dt.datetime.now(_dt.UTC).isoformat(timespec="seconds")
    repo_root = _repo_root()

    failure_log: list[tuple[str, str]] = []
    baseline: dict = {}
    archive_path: Path | None = None
    cfg: ConfigObject | None = None

    try:
        try:
            cfg = load_config(args.config)
        except ConfigError as e:
            sys.stderr.write(f"P1 Config-Schema-Error: {e}\n")
            return EXIT_CONFIG

        try:
            phase_p1_executed_guard(cfg, args)
        except ConfigError as e:
            sys.stderr.write(f"P1 Executed-Guard: {e}\n")
            return EXIT_CONFIG

        baseline = phase_p0(cfg, args, repo_root)
        with baseline["target_path"].open(encoding="utf-8", newline="") as _f:
            target_md = _f.read()

        rowset = phase_p2(cfg, target_md)

        phase_p3(cfg, repo_root)

        archive_path = phase_p4(cfg, rowset, repo_root, timestamp, args, baseline)

        try:
            phase_p5(cfg, target_md, rowset, archive_path, timestamp, args, baseline)
        except Exception:
            _restore_backup(baseline)
            _cleanup_archive_on_fail(archive_path)
            raise

        try:
            phase_p6(cfg, args)
        except Exception:
            _restore_backup(baseline)
            raise

        phase_p7(cfg, repo_root, args, baseline)

        if not args.dry_run:
            _cleanup_backup_on_success(baseline)

        return EXIT_OK

    except SystemExit as e:
        if isinstance(e.code, int):
            return e.code
        return EXIT_WRITE_ERROR
    except Exception as e:  # noqa: BLE001 — top-level catch-all is intentional for the orchestrator
        sys.stderr.write(traceback.format_exc())
        _emit_sparring_hint("unknown-phase", e, failure_log, cfg, baseline)
        return EXIT_WRITE_ERROR


if __name__ == "__main__":
    sys.exit(main())
