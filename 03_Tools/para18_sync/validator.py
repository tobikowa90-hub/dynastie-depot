"""paragraph-18-sync validator — fail-close Verify-Orchestrator für §18-Bundle.

Spec: docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md (v0.3)
SSoT-Mirror: 01_Skills/paragraph-18-sync/references/event_typ_mapping.yaml
Anker: INSTRUKTIONEN.md §18 (Sync-Pflicht-Doktrin).

P1-P7 Phases-Pipeline (siehe SKILL.md):
  P1  Pre-Flight  (ordering, ticker-identity, dirty-predicate, quarterly-rollover)
  P2  Event-Klassifikation (parse + dedupe, Tippfehler-Reject)
  P3  Expected-Set-Compute (yaml-load + Union + xlsx-Selektion via SYSTEM.md)
  P4  Staging-Diff (4-Bucket: staged/unstaged_new/unstaged_preexisting/missing)
  P5  xlsx-Confirm (y/n Smoke-Test, skip = HARD FAIL exit=5)
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
    check_dirty: bool = True,
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
    check_dirty=False: skip dirty-predicate (für Pre-P3-Pass nötig, da expected
        dort noch ∅ ist und dirty-FAIL legitime Sync-States maskieren würde —
        Codex-CP2-HIGH-2 false-negative-Fix). Pre-existing-Unstaged-Snapshot
        wird trotzdem für P4 erfasst.
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

    # Pre-existing-Unstaged-Snapshot (für P4-Bucket-Klassifikation) — immer erfassen
    cur_unstaged = set(get_unstaged_modified_files(cwd))
    untracked = set(get_untracked_files(cwd))
    pre_existing = sorted(cur_unstaged | untracked)

    # Dirty-Tree-Predicate (Codex-M5): nur wenn check_dirty=True (Codex-CP2-HIGH-2 fix)
    if check_dirty:
        if allow_dirty > 100:
            return PreFlightResult(
                False,
                "P1: --allow-dirty > 100 ist Refused (WIP zu groß, bitte git stash oder commit).",
            )
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
    version_bump: bool = False,
) -> set[str]:
    """§18.2 Union — dedupe, Conditionals applizieren.

    Conditionals (yaml `conditional.<name>.adds`):
      - `flag_event`     → wenn `--flag-event` UND event=score-flag-sparraten → +flag_events.jsonl
      - `version_bump`   → wenn `--version-bump` UND event=system-zustand    → +CORE-MEMORY.md
                           (Codex-CP-Final-H1: yaml-conditional war definiert aber nie
                           applied → Spec-Drift §18.2 behoben.)
      - `session_close`  → yaml-Schema vorhanden für pipeline-item; v0.1 wird der
                           Session-Handover-Add manuell via `--also` getriggert,
                           kein eigener CLI-Flag (Gemini-D3-Carryover für v0.2).
    """
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
        if version_bump and ev == "system-zustand":
            cond = node.get("conditional", {}).get("version_bump", {})
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
# P4 — Staging-Diff (4-Bucket-Klassifikation, Spec §4 P4)                     #
# --------------------------------------------------------------------------- #


@dataclass
class P4Result:
    ok: bool
    classification: FileClassification
    spot_greps: dict[str, dict[str, int]] = field(default_factory=dict)
    reason: str = ""


def verify_staging(
    expected: set[str],
    pre_existing_unstaged: list[str],
    ticker: str | None = None,
    *,
    cwd: Path | None = None,
) -> P4Result:
    """P4 — Staging-Diff gegen Expected-Set + 4-Bucket (Spec §4).

    FAIL-Trigger:
      - MISSING (weder staged noch unstaged) → exit=4
      - UNSTAGED_NEW (G-01: dirty jetzt, sauber im Pre-Snapshot) → exit=4
        Hint: `git add <file>` Recovery.
    WARN-only:
      - UNSTAGED_PREEXISTING (Pre-existing-Dirty, Refactor-Drift-Schutz §18.4)
    Spot-Greps (non-blocking, nur wenn ticker gesetzt):
      - cached-diff -G<ticker> Hit-Count pro staged md/yaml → Plausibilitäts-Signal
        für Score-Move (kein Hard-Assert; Detektion-Hilfe für Reviewer).
    """
    staged = get_staged_files(cwd)
    cur_unstaged = get_unstaged_modified_files(cwd)
    fc = classify_files(expected, staged, cur_unstaged, pre_existing_unstaged)

    if fc.missing or fc.unstaged_new:
        parts = []
        if fc.missing:
            parts.append(f"MISSING: {sorted(fc.missing)}")
        if fc.unstaged_new:
            parts.append(f"UNSTAGED_NEW (G-01, run `git add`): {sorted(fc.unstaged_new)}")
        return P4Result(False, fc, reason="; ".join(parts))

    spot: dict[str, dict[str, int]] = {}
    if ticker:
        for f in fc.staged:
            if not (f.endswith(".md") or f.endswith(".yaml")):
                continue
            rc, out, _err = _run_git(["diff", "--cached", "-G", re.escape(ticker), "--", f], cwd)
            if rc != 0:
                continue
            hits = sum(
                1
                for ln in out.splitlines()
                if ln.startswith("+") and not ln.startswith("+++") and ticker in ln
            )
            spot[f] = {"symbol": ticker, "hits": hits}
    return P4Result(True, fc, spot_greps=spot)


# --------------------------------------------------------------------------- #
# P5 — xlsx-Smoke-Confirm (Spec §4 P5, manual-confirm v0.1)                   #
# --------------------------------------------------------------------------- #


def verify_xlsx_smoke(
    expected_xlsx: list[str],
    *,
    non_interactive_input: str | None = None,
) -> tuple[bool, str]:
    """P5 — User-Confirm-Prompt für xlsx-Smoke-Test gemäß `03_Tools/xlsx-smoke-test.md`.

    v0.1 = manual-confirm. v0.2 (post-#73b) ersetzt durch Sub-Skill-Auto-Call.

    Codex-H2-Fix: `skip`-Eingabe ist Hard-Fail (kein Bypass des xlsx-Smoke-Test
    bei xlsx-Pflicht-Set). User MUSS Smoke-Test korrekt durchführen (`y`),
    abbrechen (`n`) oder via `--dry-run` neu starten.

    Returns:
      (True, "manual-confirm")  — User-Confirm `y`
      (True, "not-applicable")  — Kein xlsx erwartet (no-op-PASS)
      (False, <reason>)         — `n`, `skip`, EOF, oder anderer Input
    """
    if not expected_xlsx:
        return True, "not-applicable"
    prompt = (
        f"P5 xlsx-Smoke-Test: {len(expected_xlsx)} File(s) → {expected_xlsx}\n"
        "Smoke-Test gemäß `03_Tools/xlsx-smoke-test.md` gelaufen + PASS? (y/n): "
    )
    if non_interactive_input is not None:
        ans = non_interactive_input.strip().lower()
    else:
        try:
            ans = input(prompt).strip().lower()
        except EOFError:
            return (
                False,
                "P5: EOF auf Confirm-Prompt — non-interactive ohne --dry-run nicht erlaubt",
            )
    if ans == "y":
        return True, "manual-confirm"
    if ans == "skip":
        return (
            False,
            "P5: 'skip' nicht erlaubt im Required-xlsx-Pfad (Codex-H2). "
            "Nutze --dry-run oder Smoke-Test korrekt durchführen.",
        )
    return (
        False,
        "P5: User-Confirm n — Smoke-Test ausstehend. Recovery: `03_Tools/xlsx-smoke-test.md`.",
    )


# --------------------------------------------------------------------------- #
# P6 — Two-Commit-Same-Session-Protokoll (Codex-H1, Spec §4 P6)               #
# --------------------------------------------------------------------------- #
#
# Drift-Matrix (Plan-Task-11, Codex-M3 end-to-end Fidelity-Gate):
#   commit_a_sha != HEAD          → session_valid False  ("commit_a_sha ... != HEAD ...")
#   TTL > SESSION_TTL_SECONDS     → session_valid False  ("session TTL exceeded")
#   Marker bereits 'committed'    → _run_verify_b REFUSE ("Marker bereits committed")
#   Marker absent (--verify-b)    → _run_verify_b REFUSE ("kein Session-Marker")
#   Marker JSON corrupt           → read_session_marker None → behandelt wie absent
#   --reset-session (any state)   → silent delete, exit=0
#   Re-Run ohne --verify-b        → main() schreibt neuen Marker (legitim für neuen Commit-A)


def _session_id() -> str:
    """16-Char-sha1-Hash aus host/user/time (Schutz vor cross-machine-Marker-Konflikt)."""
    import hashlib
    import os as _os

    h = hashlib.sha1()
    h.update(_os.environ.get("COMPUTERNAME", "host").encode())
    h.update(_os.environ.get("USERNAME", _os.environ.get("USER", "user")).encode())
    h.update(str(int(time.time())).encode())
    return h.hexdigest()[:16]


def write_session_marker(
    *,
    commit_a_sha: str,
    expected_xlsx: list[str],
    xlsx_tool_stems: list[str] | None = None,
    marker_path: Path | None = None,
) -> dict:
    """Schreibt Session-Marker (JSON) für Two-Commit-Tracking.

    `xlsx_tool_stems` persistiert die Tool-Stems (z.B. ['Rebalancing_Tool', 'Satelliten_Monitor'])
    damit `_run_verify_b()` die xlsx-Files gegen aktuelles SYSTEM.md re-resolven kann
    (Codex-CP-Final-H2 xlsx-set-match drift-guard). `marker_path` für Test-Override.
    """
    path = marker_path if marker_path is not None else SESSION_MARKER
    marker = {
        "session_id": _session_id(),
        "started_at_iso": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
        "started_at_ts": int(time.time()),
        "commit_a_sha": commit_a_sha,
        "expected_xlsx": expected_xlsx,
        "xlsx_tool_stems": list(xlsx_tool_stems or []),
        "status": "pending",
    }
    path.write_text(json.dumps(marker, indent=2), encoding="utf-8")
    return marker


def read_session_marker(marker_path: Path | None = None) -> dict | None:
    """Liest Session-Marker. None bei missing oder corrupt JSON."""
    path = marker_path if marker_path is not None else SESSION_MARKER
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):  # fmt: skip
        return None


def session_valid(marker: dict, *, cwd: Path | None = None) -> tuple[bool, str]:
    """Prüft Drift gegen current HEAD + TTL.

    Returns (True, "ok") oder (False, P6/B-Fail-Reason mit klarem Recovery-Hint).
    """
    if not marker:
        return False, "P6/B: no marker"
    cur_head = get_head_sha(cwd)
    marker_sha = marker.get("commit_a_sha", "")
    if marker_sha != cur_head:
        return False, (
            f"P6/B: commit_a_sha {marker_sha[:8]} != HEAD {cur_head[:8]} "
            f"(anderer Commit zwischendrin). Recovery: --reset-session."
        )
    age = int(time.time()) - int(marker.get("started_at_ts", 0))
    if age > SESSION_TTL_SECONDS:
        return False, (
            f"P6/B: session TTL exceeded ({age}s > {SESSION_TTL_SECONDS}s). "
            f"Recovery: --reset-session."
        )
    return True, "ok"


def _run_verify_b(args: argparse.Namespace) -> int:
    """Two-Commit-Protokoll Re-Invocation für Commit-B xlsx-Bundle.

    Normative Direktive (Codex-M2-Fix): Volle P1+P4+P5-Revalidation für
    xlsx-Subset, keine Phase darf übersprungen werden. Bei jeglichem Sub-Fail
    bleibt der Marker auf 'pending', Re-Run nötig.

    cwd-Disziplin: alle Sub-Phasen nutzen Path.cwd() statt PROJECT_ROOT-
    Konstante, damit verify-b aus jedem Repo-Subdirectory oder Test-tmp_path
    konsistent läuft (Codex-CP3-Sparring-R2 Integration-Coverage).
    """
    cwd = Path.cwd()
    marker = read_session_marker()
    if marker is None:
        sys.stderr.write(
            "FAIL P6 — kein Session-Marker (keine pending Commit-A). "
            "Recovery: ohne --verify-b starten.\n"
        )
        return EXIT_FAIL_P6
    if marker.get("status") == "committed":
        sys.stderr.write(
            "FAIL P6 — Marker bereits committed; xlsx noch dirty? `git status` checken.\n"
        )
        return EXIT_FAIL_P6
    ok, reason = session_valid(marker, cwd=cwd)
    if not ok:
        sys.stderr.write(f"FAIL P6 — {reason}\n")
        return EXIT_FAIL_P6

    expected_xlsx = set(marker.get("expected_xlsx", []))

    # H2 — xlsx-set-match drift-guard (Codex-CP-Final): re-resolve marker.xlsx_tool_stems
    # gegen aktuelles SYSTEM.md/Glob. Mismatch zwischen marker.expected_xlsx und aktuell
    # resolved Set bedeutet: SYSTEM.md wurde zwischen Commit-A und --verify-b geändert
    # (Pin-Update oder Version-Bump) → P6/B drift, --reset-session required.
    marker_stems = marker.get("xlsx_tool_stems", [])
    if marker_stems:
        try:
            current_xlsx, _xlsx_warn, fail = resolve_active_xlsx(marker_stems)
        except Exception as ex:  # noqa: BLE001 — keep verify-b fail-close
            sys.stderr.write(f"FAIL P6 (verify-b) — xlsx-set-resolve error: {ex}\n")
            return EXIT_FAIL_P6
        if fail:
            sys.stderr.write(f"FAIL P6 (verify-b) — xlsx-set-resolve: {fail}\n")
            return EXIT_FAIL_P6
        current_set = set(current_xlsx)
        if current_set != expected_xlsx:
            added = sorted(current_set - expected_xlsx)
            removed = sorted(expected_xlsx - current_set)
            sys.stderr.write(
                "FAIL P6 (verify-b) — xlsx-set-mismatch zwischen Marker und aktuellem "
                f"SYSTEM.md: added={added} removed={removed}. SYSTEM.md-Pin wurde zwischen "
                "Commit-A und --verify-b geändert. Recovery: --reset-session + Two-Commit "
                "neu starten.\n"
            )
            return EXIT_FAIL_P6

    # P1-Revalidation (Working-Tree-Sanity, kein Score-Ordering-Check für Commit-B)
    pf = verify_pre_flight(
        "score-flag-sparraten",
        ticker=None,
        flag_event=False,
        allow_dirty=args.allow_dirty,
        expected=expected_xlsx,
        check_dirty=True,
        cwd=cwd,
    )
    if not pf.ok:
        sys.stderr.write(f"FAIL P1 (verify-b) — {pf.reason}\n")
        return EXIT_FAIL_P1

    # P4-Revalidation: xlsx-Subset MUSS staged sein (kein WARN-Toleranz für
    # unstaged_preexisting im verify-b-Pfad — Codex-CP3-HIGH-2). In Commit-B
    # wäre jede xlsx-Änderung nach Commit-A neu und MUSS via `git add` staged
    # sein bevor `--verify-b` PASS-en darf.
    p4 = verify_staging(expected_xlsx, pf.pre_existing_unstaged, cwd=cwd)
    if not p4.ok:
        sys.stderr.write(f"FAIL P4 (verify-b) — {p4.reason}\n")
        return EXIT_FAIL_P4
    not_staged = expected_xlsx - set(p4.classification.staged)
    if not_staged:
        # H3 (Codex-CP-Final): xlsx-unstaged im verify-b ist ein P6/B drift (Two-Commit-
        # Contract verletzt), kein generischer P4-Staging-Fail. Exit-Code auf 6 gemappt
        # für Konsistenz mit Spec §7 + SKILL.md Exit-Tabelle + failure-recovery.md.
        sys.stderr.write(
            f"FAIL P6 (verify-b) — xlsx-Subset nicht vollständig staged: {sorted(not_staged)}. "
            "Run `git add` für jede xlsx vor --verify-b.\n"
        )
        return EXIT_FAIL_P6

    # P5-Revalidation: xlsx-Smoke-Test
    ok_p5, status = verify_xlsx_smoke(sorted(expected_xlsx))
    if not ok_p5:
        sys.stderr.write(f"FAIL P5 (verify-b) — {status}\n")
        return EXIT_FAIL_P5

    # PASS — Marker-Cleanup nach Commit-B-PASS (Heuristik: Marker hat seinen Zweck erfüllt)
    SESSION_MARKER.unlink(missing_ok=True)
    print(
        json.dumps(
            {
                "verdict": "PASS",
                "phase": "P6/B",
                "xlsx_verified": status,
                "expected_xlsx": sorted(expected_xlsx),
                "session_id": marker.get("session_id", ""),
            },
            indent=2,
        )
    )
    return EXIT_PASS


# --------------------------------------------------------------------------- #
# Closure-Report Emitter (Spec §4 P7 — full JSON-Schema, Codex-M6 retry-flag) #
# --------------------------------------------------------------------------- #


def _build_recovery_hints(
    verdict: str,
    phase: str,
    p4: P4Result,
    pf: PreFlightResult,
    expected_xlsx: list[str],
) -> list[str]:
    """Generiert phase-spezifische Recovery-Hints für den Closure-Report."""
    hints: list[str] = []
    if verdict == "FAIL":
        if phase == "P1":
            hints.append("Sub-Tool zuerst laufen lassen (`!Analysiere` / `archive_flag.py`).")
        if phase == "P4":
            if p4.classification.missing:
                hints.append(
                    "MISSING-Files prüfen + `git add <file>` für die Sync-Pflicht-Bundle-Files."
                )
            if p4.classification.unstaged_new:
                hints.append(
                    "UNSTAGED_NEW (G-01): `git add <file>` für jeden NEW-Eintrag, dann erneut validieren."
                )
        if phase == "P5":
            hints.append(
                "xlsx-Smoke-Test gemäß `03_Tools/xlsx-smoke-test.md` korrekt durchführen, dann --verify-b."
            )
        if phase in ("P6", "P6/B"):
            hints.append(
                "Two-Commit-Drift: `--reset-session` löscht Marker und erlaubt Neustart vom Commit-A."
            )
    if verdict == "PASS" and expected_xlsx and phase == "P7":
        hints.append(
            "Commit-A jetzt absetzen; danach xlsx via openpyxl schreiben + smoke + `--verify-b`."
        )
    if pf.quarterly_rollover_warn:
        hints.append(
            "Quartals-Wechsel (G-03 WARN): log.md sollte zeitnah ins `archive/log/`-Verzeichnis rolliert werden."
        )
    return hints


def _emit_report(
    verdict: str,
    phase: str,
    events: list[str],
    expected: set[str],
    p4: P4Result,
    pf: PreFlightResult,
    xlsx_warnings: list[str],
    args: argparse.Namespace,
    *,
    expected_xlsx: list[str] | None = None,
    cwd: Path | None = None,
    xlsx_verified: str = "not-applicable",
    retry_required_revalidation: bool = False,
) -> None:
    """JSON-Closure-Report (Spec §4 P7, voll-Schema post-Task-12).

    Felder:
      verdict / phase / events / expected_files / staged_files /
      unstaged_modified_files / missing / unstaged_new / pre_existing_unstaged /
      spot_grep_results / xlsx_warnings / expected_xlsx / xlsx_verified /
      retry_required_revalidation / session_marker (nested) /
      quarterly_rollover_warn / ticker / flag_event / dirty_threshold /
      recovery_hints

    Codex-M6 retry-Hint: bei jedem Commit-Failure-Retry MUSS Analyst re-validate
    durch erneuten validator-Lauf. Flag wird im Report exponiert (default False;
    Caller setzt True bei phase-spezifischen FAIL-Verdikten die retry rechtfertigen).
    """
    marker = read_session_marker() or {}
    expected_xlsx_list = expected_xlsx or []
    payload = {
        "verdict": verdict,
        "phase": phase,
        "events": events,
        "expected_files": sorted(expected),
        "staged_files": p4.classification.staged,
        "unstaged_modified_files": get_unstaged_modified_files(cwd),
        "missing": p4.classification.missing,
        "unstaged_new": p4.classification.unstaged_new,
        "pre_existing_unstaged": pf.pre_existing_unstaged,
        "spot_grep_results": p4.spot_greps,
        "xlsx_warnings": xlsx_warnings,
        "expected_xlsx": expected_xlsx_list,
        "xlsx_verified": xlsx_verified,
        "retry_required_revalidation": retry_required_revalidation,
        "session_marker": {
            "session_id": marker.get("session_id", "none"),
            "commit_a_sha": marker.get("commit_a_sha", ""),
            "status": marker.get("status", "none"),
        },
        "quarterly_rollover_warn": pf.quarterly_rollover_warn,
        "ticker": args.ticker,
        "flag_event": args.flag_event,
        "dirty_threshold": args.allow_dirty,
        "recovery_hints": _build_recovery_hints(verdict, phase, p4, pf, expected_xlsx_list),
    }
    print(json.dumps(payload, indent=None if args.json_output else 2))


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
        "--version-bump",
        action="store_true",
        help=(
            "Aktiviert version_bump-Conditional für system-zustand "
            "(+ CORE-MEMORY.md ins Expected-Set; nur bei §6-relevanter Versions-Inkrement)"
        ),
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
        return _run_verify_b(args)

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

    # P1 (Pre-P3) — Ordering + Ticker-Identity + Quartal-Rollover-WARN nur (kein dirty-check).
    # Dirty-Predicate ist expected-abhängig und läuft erst nach P3 (Codex-CP2-HIGH-2 fix:
    # erster Pass mit expected=∅ würde legitime Sync-States als dirty-FAIL maskieren).
    pf = verify_pre_flight(
        args.event_type,
        ticker=args.ticker,
        flag_event=args.flag_event,
        allow_dirty=args.allow_dirty,
        check_dirty=False,
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
        node = (mapping.get("event_types") or {}).get("score-flag-sparraten")
        if not isinstance(node, dict):
            sys.stderr.write(
                "FAIL P3 — yaml-schema-drift: event_types.score-flag-sparraten "
                "fehlt oder ist kein dict.\n"
            )
            return EXIT_FAIL_P3
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
        version_bump=args.version_bump,
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

    # P4 — Staging-Diff (Spec §4). Two-Commit-Protokoll (Codex-H1): xlsx-Subset
    # gehört NICHT in Commit-A; verify_staging prüft daher das md/jsonl/yaml-Set.
    # xlsx-Bundle wird in Commit-B via `--verify-b` revalidiert (Task 11).
    expected_for_a = {f for f in expected if not f.endswith(".xlsx")}
    expected_xlsx = sorted({f for f in expected if f.endswith(".xlsx")})

    p4 = verify_staging(expected_for_a, pf.pre_existing_unstaged, ticker=args.ticker)
    if not p4.ok:
        sys.stderr.write(f"FAIL P4 — {p4.reason}\n")
        _emit_report(
            "FAIL",
            "P4",
            events_dedup,
            expected,
            p4,
            pf,
            xlsx_warnings,
            args,
            expected_xlsx=expected_xlsx,
        )
        return EXIT_FAIL_P4

    # P6 Two-Commit-Setup (Codex-H1): wenn xlsx-Subset erwartet, Marker für Commit-B-
    # Revalidation schreiben. xlsx-Files bleiben unstaged in Commit-A; nach Commit-A
    # + openpyxl-Write + xlsx-Smoke ruft Analyst `validator.py --verify-b` für P5/P6/B.
    if expected_xlsx:
        cur_head = get_head_sha()
        # Tool-Stems für H2 drift-guard persistieren (re-resolve via SYSTEM.md im verify-b-Pfad).
        tool_stems = []
        if "score-flag-sparraten" in events_dedup:
            sf_node = (mapping.get("event_types") or {}).get("score-flag-sparraten") or {}
            tool_stems = list(sf_node.get("required_xlsx_tools", []))
        marker = write_session_marker(
            commit_a_sha=cur_head,
            expected_xlsx=expected_xlsx,
            xlsx_tool_stems=tool_stems,
        )
        sys.stderr.write(
            f"NOTE — Commit-A bereit ({len(p4.classification.staged)} Files staged, "
            f"{len(expected_xlsx)} xlsx pending). Session-Marker: {marker['session_id']}.\n"
            "Nach `git commit` → xlsx via openpyxl + smoke + `validator.py --verify-b`.\n"
        )

    _emit_report(
        "PASS",
        "P7",
        events_dedup,
        expected,
        p4,
        pf,
        xlsx_warnings,
        args,
        expected_xlsx=expected_xlsx,
    )
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
