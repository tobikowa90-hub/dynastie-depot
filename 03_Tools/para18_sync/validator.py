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
  0  = PASS
  1  = P1 fail
  2  = P2 fail
  3  = P3 fail
  4  = P4 fail
  5  = P5 fail
  6  = P6/B drift
  99 = BUILD-INCOMPLETE-Sentinel (P2-P7 noch nicht implementiert, Build-Phase)
       — fail-close gegen false-positive PASS während Build (Codex-CP1-P1 2026-05-22).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import yaml

# Exit-Codes (Spec §7)
EXIT_PASS = 0
EXIT_FAIL_P1 = 1
EXIT_FAIL_P2 = 2
EXIT_FAIL_P3 = 3
EXIT_FAIL_P4 = 4
EXIT_FAIL_P5 = 5
EXIT_FAIL_P6 = 6
EXIT_BUILD_INCOMPLETE = 99  # Sentinel: P2-P7 noch nicht implementiert (Build-Phase)

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
# P1 Pre-Flight (Ordering + Ticker-Identity-Guard, Spec §4)                   #
# --------------------------------------------------------------------------- #


def _read_last_jsonl_record(path: Path) -> dict | None:
    """Liest letzte non-empty JSONL-Zeile. None wenn Datei fehlt, leer oder malformed."""
    if not path.exists():
        return None
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            lines = [ln for ln in fh if ln.strip()]
        if not lines:
            return None
        return json.loads(lines[-1])
    except (json.JSONDecodeError, UnicodeDecodeError, OSError):  # fmt: skip
        return None


def _today_iso() -> str:
    return time.strftime("%Y-%m-%d", time.localtime())


@dataclass
class PreFlightResult:
    ok: bool
    reason: str = ""
    quarterly_rollover_warn: bool = False
    pre_existing_unstaged: list[str] = field(default_factory=list)


def _resolve_project_root(cwd: Path | None = None) -> Path:
    """Auflösung der Repo-Wurzel relativ zu cwd via git rev-parse.

    Tests laufen in temp_repo (tmp_path) — die statische PROJECT_ROOT-Konstante würde
    immer auf das echte Projekt zeigen. cwd-aware Resolution macht den Validator
    test-isoliert (Plan-Hinweis Phase 4 / Task 5 Step 2).
    """
    if cwd is None:
        return PROJECT_ROOT
    rc, out, _err = _run_git(["rev-parse", "--show-toplevel"], cwd)
    if rc == 0 and out.strip():
        return Path(out.strip())
    return cwd


def _check_quarterly_rollover(root: Path) -> bool:
    """G-03: WARN wenn current-date Quartals-Wechsel-Monat ≤14d UND prev-Quartals-archive fehlt.

    §18.6 sieht quartalsweisen log.md-Roll-over vor. Bei Quartals-Wechsel ohne archive
    emittiert P1 einen non-blocking WARN-Flag.
    """
    now = time.localtime()
    if now.tm_mon not in (1, 4, 7, 10):
        return False
    if now.tm_mday > 14:
        return False
    cur_q = (now.tm_mon - 1) // 3 + 1
    prev_q = 4 if cur_q == 1 else cur_q - 1
    prev_year = now.tm_year - 1 if cur_q == 1 else now.tm_year
    archive_path = (
        root
        / "07_Obsidian Vault"
        / "Obsidian Mindmap"
        / "Investing Mastermind"
        / "archive"
        / "log"
        / f"log-{prev_year}-Q{prev_q}.md"
    )
    return not archive_path.exists()


def verify_pre_flight(
    event_type: str,
    *,
    ticker: str | None,
    flag_event: bool,
    allow_dirty: int = 10,
    expected: set[str] | None = None,
    cwd: Path | None = None,
) -> PreFlightResult:
    """P1 — Working-Tree-Sanity + Ordering-Guard + Ticker-Identity (Codex-H3) + Dirty-Predicate (M5) + Quartal (G-03).

    Score-Event-Pflichten:
      - score_history.jsonl HEAD-Append heute (sonst FAIL)
      - HEAD-Ticker == --ticker (Codex-H3 wrong-ticker-Drift-Schutz)
      - --flag-event: flag_events.jsonl HEAD-Append heute + Ticker-Match

    Dirty-Tree-Predicate (Codex-M5):
      |(unstaged ∪ untracked) \\ expected| ≥ allow_dirty → FAIL (Refactor-Drift-Schutz)
      allow_dirty > 100 → refuse (WIP zu groß)

    Quartals-Rollover (G-03): non-blocking WARN-Flag bei Quartals-Wechsel ≤14d ohne archive.

    cwd=None: nutze Process-cwd (test-isoliert via subprocess.cwd-Override).
    expected=None: kein Set-Vergleich → dirty-Predicate vergleicht gegen ∅.
    """
    if cwd is None:
        cwd = Path.cwd()
    if expected is None:
        expected = set()
    if not _is_git_repo(cwd):
        return PreFlightResult(False, "P1: not inside a git repo")

    root = _resolve_project_root(cwd)

    if event_type == "score-flag-sparraten":
        score_log = root / "00_Core" / "score_history.jsonl"
        rec = _read_last_jsonl_record(score_log)
        if rec is None:
            return PreFlightResult(
                False,
                "P1: score_history.jsonl leer/fehlt/malformed — "
                "`!Analysiere <ticker>` zuerst (HEAD-Append Pflicht).",
            )
        ts_field = rec.get("timestamp") or rec.get("date") or ""
        if not ts_field.startswith(_today_iso()):
            return PreFlightResult(
                False,
                f"P1: score_history HEAD-Append nicht heute (HEAD-date={ts_field}). "
                "`!Analysiere <ticker>` zuerst.",
            )
        if ticker:
            head_ticker = rec.get("ticker") or rec.get("symbol") or ""
            if head_ticker != ticker:
                return PreFlightResult(
                    False,
                    f"P1: score_history HEAD-Ticker `{head_ticker}` != --ticker `{ticker}` "
                    "(Codex-H3 wrong-ticker-Drift).",
                )

        if flag_event:
            flag_log = root / "00_Core" / "flag_events.jsonl"
            frec = _read_last_jsonl_record(flag_log)
            if frec is None:
                return PreFlightResult(
                    False,
                    "P1: --flag-event aber flag_events.jsonl leer/fehlt — "
                    "`archive_flag.py` zuerst.",
                )
            fts = frec.get("timestamp") or frec.get("date") or ""
            if not fts.startswith(_today_iso()):
                return PreFlightResult(
                    False,
                    f"P1: flag_events HEAD-Append nicht heute (HEAD-date={fts}).",
                )
            if ticker:
                fhead_ticker = frec.get("ticker") or frec.get("symbol") or ""
                if fhead_ticker != ticker:
                    return PreFlightResult(
                        False,
                        f"P1: flag_events HEAD-Ticker `{fhead_ticker}` != --ticker `{ticker}`.",
                    )

    # Dirty-Tree-Predicate (Codex-M5): (unstaged ∪ untracked) \ expected ≥ allow_dirty → FAIL
    if allow_dirty > 100:
        return PreFlightResult(
            False,
            "P1: --allow-dirty > 100 ist Refused (WIP zu groß, bitte git stash oder commit).",
        )
    cur_unstaged = set(get_unstaged_modified_files(cwd))
    untracked = set(get_untracked_files(cwd))
    pre_existing = sorted(cur_unstaged | untracked)
    excess = (cur_unstaged | untracked) - expected
    if len(excess) >= max(allow_dirty, 1):
        return PreFlightResult(
            False,
            f"P1: dirty-tree predicate triggered — {len(excess)} unrelated dirty/untracked files "
            f"(threshold={allow_dirty}). Cleanup oder --allow-dirty <N>.",
            pre_existing_unstaged=pre_existing,
        )

    # Quartals-Rollover (G-03, §18.6) — non-blocking WARN
    rollover_warn = _check_quarterly_rollover(_resolve_project_root(cwd))

    return PreFlightResult(
        True,
        quarterly_rollover_warn=rollover_warn,
        pre_existing_unstaged=pre_existing,
    )


# --------------------------------------------------------------------------- #
# P2/P3 — Event-Klassifikation + Expected-Set-Compute (Spec §4 P2/P3)         #
# --------------------------------------------------------------------------- #


YAML_PATH = (
    PROJECT_ROOT / "01_Skills" / "paragraph-18-sync" / "references" / "event_typ_mapping.yaml"
)


def load_event_mapping() -> dict:
    """Lädt SSoT-Mirror yaml (§18.1). Raises FileNotFoundError / yaml.YAMLError."""
    if not YAML_PATH.exists():
        raise FileNotFoundError(f"event_typ_mapping.yaml fehlt: {YAML_PATH}")
    with YAML_PATH.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def compute_union_set(
    events: list[str],
    *,
    flag_event: bool,
    mapping: dict,
    active_xlsx: list[str] | None = None,
) -> set[str]:
    """§18.2 Union — dedupe, Conditionals applizieren."""
    result: set[str] = set()
    for ev in events:
        node = mapping["event_types"].get(ev)
        if node is None:
            continue
        for f in node.get("required_files", []):
            result.add(f)
        if flag_event and ev == "score-flag-sparraten":
            cond = node.get("conditional", {}).get("flag_event", {})
            for f in cond.get("adds", []):
                result.add(f)
        if ev == "score-flag-sparraten" and active_xlsx:
            for x in active_xlsx:
                result.add(x)
    return result


ACTIVE_XLSX_BLOCK_HEADING = "## Active xlsx-Filenames"


def parse_active_xlsx_block(system_md: Path) -> dict[str, str]:
    """Parst `## Active xlsx-Filenames`-Block aus SYSTEM.md. Format: `- ToolName: Filename.xlsx`."""
    if not system_md.exists():
        return {}
    text = system_md.read_text(encoding="utf-8", errors="replace")
    result: dict[str, str] = {}
    in_block = False
    for line in text.splitlines():
        if line.strip().startswith(ACTIVE_XLSX_BLOCK_HEADING):
            in_block = True
            continue
        if in_block:
            if line.startswith("## ") and not line.startswith(ACTIVE_XLSX_BLOCK_HEADING):
                break
            m = re.match(
                r"^\s*[-*]\s*([A-Za-z0-9_]+)\s*:\s*([A-Za-z0-9_.+-]+\.xlsx)\s*$",
                line,
            )
            if m:
                result[m.group(1)] = m.group(2)
    return result


def resolve_active_xlsx(tool_stems: list[str]) -> tuple[list[str], list[str], str | None]:
    """Resolve xlsx-Files für gegebene Tool-Stems (Codex-M4 deterministisch).

    Reihenfolge: (1) SYSTEM.md Active-xlsx-Pin → (2) Glob+Semver-Pick → (3) Ambiguity-FAIL.

    Returns (resolved_paths, warnings, fail_reason). fail_reason ≠ None → P3-FAIL exit=3.
    """
    system_md = PROJECT_ROOT / "00_Core" / "SYSTEM.md"
    pin = parse_active_xlsx_block(system_md)
    resolved: list[str] = []
    warnings: list[str] = []
    tools_dir = PROJECT_ROOT / "03_Tools"
    for stem in tool_stems:
        if stem in pin:
            resolved.append(f"03_Tools/{pin[stem]}")
            continue
        matches = sorted(tools_dir.glob(f"{stem}_v*.xlsx"))
        if not matches:
            warnings.append(f"xlsx-Tool `{stem}` nicht in SYSTEM.md-Pin und kein Glob-Match")
            continue

        def _semver(p: Path) -> tuple[int, int]:
            m = re.search(r"_v(\d+)\.(\d+)", p.name)
            return (int(m.group(1)), int(m.group(2))) if m else (-1, -1)

        matches.sort(key=_semver, reverse=True)
        top = _semver(matches[0])
        tied = [m for m in matches if _semver(m) == top]
        if len(tied) > 1:
            return (
                [],
                warnings,
                (
                    f"P3: xlsx-Selektion ambiguous für `{stem}` — "
                    f"{len(tied)} Files mit gleicher Semver: {[m.name for m in tied]}. "
                    "Setze SYSTEM.md Active-xlsx-Block."
                ),
            )
        resolved.append(f"03_Tools/{matches[0].name}")
        warnings.append(
            f"SYSTEM.md Active-xlsx-Block fehlt für `{stem}`, Fallback Semver-Pick: {matches[0].name}"
        )
    return resolved, warnings, None


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

    if args.reset_session:
        if SESSION_MARKER.exists():
            SESSION_MARKER.unlink()
        sys.stdout.write(
            json.dumps({"verdict": "PASS", "phase": "reset", "action": "session_marker_deleted"})
            + "\n"
        )
        return EXIT_PASS

    if args.verify_b:
        # Two-Commit-Protokoll Re-Invocation wird in Task 11 (P6) implementiert.
        sys.stderr.write("FAIL P6 — --verify-b nicht implementiert (Task 11)\n")
        return EXIT_FAIL_P6

    if args.event_type == "__none__":
        sys.stderr.write(
            "FAIL P2 — event-type required. Zulässig: "
            + ", ".join(sorted(VALID_EVENT_TYPES))
            + "\n"
        )
        return EXIT_FAIL_P2

    if args.flag_event and args.event_type != "score-flag-sparraten":
        sys.stderr.write("FAIL P2 — --flag-event nur bei score-flag-sparraten erlaubt\n")
        return EXIT_FAIL_P2

    # P1 — Pre-Flight (Ordering + Ticker-Identity + Dirty-Predicate + Quartal-Rollover-WARN)
    # Erster P1-Pass ohne expected-Set (vor P2/P3). Task 7 reicht expected nach,
    # falls Dirty-Predicate mit echter Union getunt werden muss.
    pf = verify_pre_flight(
        args.event_type,
        ticker=args.ticker,
        flag_event=args.flag_event,
        allow_dirty=args.allow_dirty,
    )
    if not pf.ok:
        sys.stderr.write(f"FAIL P1 — {pf.reason}\n")
        return EXIT_FAIL_P1

    # P2 — Event-Klassifikation (parse + dedupe)
    events = [args.event_type, *(args.also or [])]
    seen: set[str] = set()
    events_dedup: list[str] = []
    for e in events:
        if e not in seen:
            seen.add(e)
            events_dedup.append(e)

    # P3 — yaml + Expected-Set + xlsx
    try:
        mapping = load_event_mapping()
    except (FileNotFoundError, yaml.YAMLError) as ex:
        sys.stderr.write(f"FAIL P3 — yaml-load: {ex}\n")
        return EXIT_FAIL_P3

    active_xlsx: list[str] = []
    xlsx_warnings: list[str] = []
    if "score-flag-sparraten" in events_dedup:
        node = mapping["event_types"]["score-flag-sparraten"]
        stems = node.get("required_xlsx_tools", [])
        active_xlsx, xlsx_warnings, fail = resolve_active_xlsx(stems)
        if fail:
            sys.stderr.write(f"FAIL P3 — {fail}\n")
            return EXIT_FAIL_P3

    expected = compute_union_set(
        events_dedup,
        flag_event=args.flag_event,
        mapping=mapping,
        active_xlsx=active_xlsx,
    )

    # Critical-Alert NO-OP-PASS (Spec §4 P3 + yaml-Node `no_op_pass: true`)
    if events_dedup == ["critical-alert"]:
        print(
            json.dumps(
                {
                    "verdict": "PASS",
                    "phase": "P7",
                    "events": events_dedup,
                    "no_op_pass": True,
                    "expected_files": sorted(expected),
                }
            )
        )
        return EXIT_PASS

    # Re-run P1 jetzt mit echtem expected-Set (Dirty-Predicate-Exempt: erwartete Files
    # zählen nicht gegen `--allow-dirty`-Schwelle).
    pf = verify_pre_flight(
        args.event_type,
        ticker=args.ticker,
        flag_event=args.flag_event,
        allow_dirty=args.allow_dirty,
        expected=expected,
    )
    if not pf.ok:
        sys.stderr.write(f"FAIL P1 — {pf.reason}\n")
        return EXIT_FAIL_P1

    # Dry-Run: informational Expected-Set-Snapshot, kein Bundle-Verify-Claim.
    if args.dry_run:
        print(
            json.dumps(
                {
                    "verdict": "DRY-RUN",
                    "events": events_dedup,
                    "expected_files": sorted(expected),
                    "xlsx_warnings": xlsx_warnings,
                    "quarterly_rollover_warn": pf.quarterly_rollover_warn,
                },
                indent=2,
            )
        )
        return EXIT_PASS

    # ---- BUILD-PHASE SENTINEL (Codex-CP1-P1) ----
    # P4-P7 sind in Tasks 9-12 des Implementation-Plans verdrahtet. Bis dahin
    # returnt validator EXIT_BUILD_INCOMPLETE für non-dry-run, non-critical-alert —
    # verhindert false-positive PASS-Verdikt für unsynced Bundles (Spec §7 fail-close).
    sys.stderr.write(
        "WARN — paragraph-18-sync Build-Phase: P4-P7 nicht implementiert (exit=99). "
        "P1-P3 PASS, aber Staging-Diff/xlsx-Confirm/Two-Commit/Closure folgen in Tasks 9-12.\n"
    )
    return EXIT_BUILD_INCOMPLETE


if __name__ == "__main__":
    raise SystemExit(main())
