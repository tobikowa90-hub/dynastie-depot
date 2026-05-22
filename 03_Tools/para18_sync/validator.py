"""paragraph-18-sync validator — fail-close Verify-Orchestrator für §18-Bundle.

Spec: docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md (v0.3)
SSoT-Mirror: 01_Skills/paragraph-18-sync/references/event_typ_mapping.yaml
Anker: INSTRUKTIONEN.md §18 (Sync-Pflicht-Doktrin).

P1-P7 Phases-Pipeline (siehe SKILL.md):
  P1  Pre-Flight  (ordering, ticker-identity, dirty-predicate, quarterly-rollover)
  P2  Event-Klassifikation (parse + dedupe, Tippfehler-Reject)
  P3  Expected-Set-Compute (yaml-load + Union + xlsx-Selektion via SYSTEM.md)
  P4  Staging-Diff (4-Bucket: staged/unstaged_new/unstaged_preexisting/missing)
  P5  xlsx-Confirm (n/n Smoke-Test, skip = HARD FAIL exit=5)
  P6  Two-Commit-Same-Session-Protokoll (session_marker, TTL 4h)
  P7  Closure-Report (JSON + human)

Exit-Codes (Spec §7):
  0 = PASS
  1 = P1 fail
  2 = P2 fail
  3 = P3 fail
  4 = P4 fail
  5 = P5 fail
  6 = P6/B drift
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Exit-Codes (Spec §7)
EXIT_PASS = 0
EXIT_FAIL_P1 = 1
EXIT_FAIL_P2 = 2
EXIT_FAIL_P3 = 3
EXIT_FAIL_P4 = 4
EXIT_FAIL_P5 = 5
EXIT_FAIL_P6 = 6

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SESSION_MARKER = Path(__file__).parent / ".session_marker"
SESSION_TTL_SECONDS = 4 * 3600

VALID_EVENT_TYPES = {
    "score-flag-sparraten",
    "pipeline-item",
    "system-zustand",
    "critical-alert",
}


# --------------------------------------------------------------------------- #
# subprocess / git layer (Codex-M7, S18 Robustheit)                           #
# --------------------------------------------------------------------------- #


def _run_git(args: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    """git-Subprocess-Wrapper mit Robustheit (Codex-M7, S18).

    Returns (returncode, stdout, stderr). Kein Traceback bei missing git / non-repo.
    """
    target_cwd = cwd if cwd is not None else PROJECT_ROOT
    try:
        r = subprocess.run(
            ["git", *args],
            cwd=str(target_cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        return r.returncode, r.stdout or "", r.stderr or ""
    except FileNotFoundError:
        return 127, "", "git executable not in PATH"
    except subprocess.TimeoutExpired:
        return 124, "", "git timeout"


def _is_git_repo(cwd: Path | None = None) -> bool:
    rc, _out, _err = _run_git(["rev-parse", "--is-inside-work-tree"], cwd)
    return rc == 0


def get_staged_files(cwd: Path | None = None) -> list[str]:
    rc, out, _ = _run_git(["diff", "--cached", "--name-only"], cwd)
    return [ln.strip() for ln in out.splitlines() if ln.strip()] if rc == 0 else []


def get_unstaged_modified_files(cwd: Path | None = None) -> list[str]:
    rc, out, _ = _run_git(["diff", "--name-only"], cwd)
    return [ln.strip() for ln in out.splitlines() if ln.strip()] if rc == 0 else []


def get_untracked_files(cwd: Path | None = None) -> list[str]:
    rc, out, _ = _run_git(["ls-files", "--others", "--exclude-standard"], cwd)
    return [ln.strip() for ln in out.splitlines() if ln.strip()] if rc == 0 else []


def get_head_sha(cwd: Path | None = None) -> str:
    rc, out, _ = _run_git(["rev-parse", "HEAD"], cwd)
    return out.strip() if rc == 0 else ""


# --------------------------------------------------------------------------- #
# File-Classification (P4 4-Bucket, Spec §4)                                  #
# --------------------------------------------------------------------------- #


@dataclass
class FileClassification:
    staged: list[str] = field(default_factory=list)
    unstaged_new: list[str] = field(default_factory=list)
    unstaged_preexisting: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


def classify_files(
    expected: set[str],
    staged: list[str],
    current_unstaged: list[str],
    pre_existing_unstaged: list[str],
) -> FileClassification:
    """4-Bucket-Klassifikation pro Expected-File (Spec §4/§5).

    - staged: in Commit-Stage
    - unstaged_new: jetzt-dirty, war beim Pre-Snapshot nicht dirty → FAIL (G-01)
    - unstaged_preexisting: jetzt-dirty + Pre-Snapshot-dirty → WARN
    - missing: weder staged noch dirty → FAIL
    """
    staged_set = set(staged)
    cur_unstaged_set = set(current_unstaged)
    pre_set = set(pre_existing_unstaged)
    fc = FileClassification()
    for f in expected:
        if f in staged_set:
            fc.staged.append(f)
        elif f in cur_unstaged_set and f not in pre_set:
            fc.unstaged_new.append(f)
        elif f in cur_unstaged_set and f in pre_set:
            fc.unstaged_preexisting.append(f)
        else:
            fc.missing.append(f)
    return fc


# --------------------------------------------------------------------------- #
# CLI (argparse, Spec §3)                                                     #
# --------------------------------------------------------------------------- #


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="para18_sync",
        description="paragraph-18-sync validator (fail-close §18-Bundle-Verify)",
    )
    p.add_argument(
        "event_type",
        nargs="?",
        choices=[*sorted(VALID_EVENT_TYPES), "__none__"],
        default="__none__",
        help="Primary event type (4 zulässige Werte gemäß §18.1)",
    )
    p.add_argument(
        "--also",
        action="append",
        default=[],
        choices=sorted(VALID_EVENT_TYPES),
        help="Multi-Event-Union §18.2 (mehrfach erlaubt)",
    )
    p.add_argument(
        "--flag-event",
        action="store_true",
        help="Aktiviert flag_events.jsonl im Expected-Set (Pflicht bei score-flag-sparraten FLAG-Trigger)",
    )
    p.add_argument(
        "--no-flag-event",
        action="store_true",
        help="Score-Event ohne FLAG (Resolve-Pfad)",
    )
    p.add_argument(
        "--ticker",
        default=None,
        metavar="SYMBOL",
        help="Ticker (Pflicht-empfohlen bei score-flag-sparraten, Codex-H3 Identity-Guard)",
    )
    p.add_argument(
        "--allow-dirty",
        type=int,
        default=10,
        metavar="N",
        help="Dirty-Tree-Predicate-Schwelle (Default 10, Hard-Cap 100)",
    )
    p.add_argument(
        "--verify-b",
        action="store_true",
        help="Two-Commit-Protokoll Re-Invocation für Commit-B xlsx-Bundle (Codex-H1)",
    )
    p.add_argument(
        "--reset-session",
        action="store_true",
        help="Session-Marker löschen + restart",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Zeigt Expected-Set + Diff ohne Fail-close + ohne Marker-Write",
    )
    p.add_argument(
        "--json",
        dest="json_output",
        action="store_true",
        help="JSON-only Output (suppress human report)",
    )
    return p


# --------------------------------------------------------------------------- #
# main() — Phasen-Dispatch (Phasen P1-P7 werden in Tasks 5-12 implementiert)  #
# --------------------------------------------------------------------------- #


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.event_type == "__none__" and not args.verify_b and not args.reset_session:
        sys.stderr.write(
            "FAIL P2 — event-type required. Zulässig: "
            + ", ".join(sorted(VALID_EVENT_TYPES))
            + "\n"
        )
        return EXIT_FAIL_P2
    # Phasen-Dispatch wird in nachfolgenden Tasks ergänzt.
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
