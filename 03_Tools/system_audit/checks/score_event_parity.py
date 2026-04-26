"""Check-9: Score-Event-Set §18 v2.1 Parity (Phase 2 Sweep-Driver F1+F2+F4).

Audited Sources (each must reference the canonical 7-File-Set OR have an
explicit subset documented):
- 03_Tools/backtest-ready/README.md           — full 7 + v2.1 string
- 03_Tools/briefing-sync-check.ps1            — full 7 in $briefingFiles array
- 01_Skills/dynastie-depot/SKILL.md           — Schritt-7 sync-block 7
- 00_Core/INSTRUKTIONEN.md                    — §18 v2.1 string presence

Drift-Patterns the check must detect:
- F1: README.md mentions wrong §18 version (e.g. 'v1.7' instead of 'v2.1')
- F2: README.md 7-file-list missing config.yaml
- F4: briefing-sync-check.ps1 $briefingFiles missing config.yaml
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

# Canonical 7-File-Set per CLAUDE.md Z11 + INSTRUKTIONEN.md §18 v2.1
CANONICAL_SCORE_EVENT_BASENAMES = (
    "log.md",
    "CORE-MEMORY.md",
    "Faktortabelle.md",
    "PORTFOLIO.md",
    "score_history.jsonl",
    "config.yaml",
    "flag_events.jsonl",
)
CANONICAL_VERSION = "v2.1"
WRONG_VERSIONS = ("v1.7", "v2.0")  # known prior versions to detect drift


# List-entry markers: commas, quotes, table cells, PowerShell arrays,
# markdown bullets — signals that a basename appears as a declared list item,
# not in narrative prose.
_LIST_MARKER_RE = re.compile(r"[,'\"|`]|@\(|^\s*[-*]\s", re.MULTILINE)

# Sliding-window size for clustering-detection. The §18 7-File-Set is
# always declared as a contiguous list (markdown bullets, PowerShell array,
# inline comma-list). Drift in the canonical block + decoy mention 200+
# lines away (e.g. SKILL.md table-of-files) must NOT cover for the missing
# entry. 25 lines is generous enough to span a numbered list with prose
# between bullets but tight enough to stop spanning unrelated sections.
_CLUSTER_WINDOW_LINES = 25


def _scan_text_for_basenames(text: str) -> set[str]:
    """Return basenames that appear in list-entry contexts (commas, quotes,
    table cells, PowerShell arrays, markdown bullets) — not raw prose.
    Avoids FP where a basename appears in narrative text (e.g., 'die log.md
    Datei wird ...') but is not declared as part of the §18 file set.
    Codex-Review TaskID 12 follow-up.

    NOTE: file-wide scan. Use `_basenames_in_best_window` for §18-parity
    where scattered mentions across unrelated sections must not cover for
    a missing entry in the canonical list block.
    """
    found: set[str] = set()
    for line in text.splitlines():
        if not _LIST_MARKER_RE.search(line):
            continue
        for bn in CANONICAL_SCORE_EVENT_BASENAMES:
            if bn in line:
                found.add(bn)
    return found


def _basenames_in_best_window(
    text: str,
    expected: tuple[str, ...],
    window_lines: int = _CLUSTER_WINDOW_LINES,
) -> set[str]:
    """Sliding-window basename-cluster detection. Returns the set of expected
    basenames found in the best (most-coverage) window of `window_lines`
    consecutive lines, scanning only list-entry contexts.

    Why sliding-window instead of file-wide scan: a basename mention in an
    unrelated table-of-files (e.g., SKILL.md L70 lists `config.yaml` as a
    skill-file) must NOT cover for a missing entry in the canonical §18
    7-File-Set block (e.g., L306). The §18 list is always contiguous; a
    25-line window captures it whether it's a markdown bullet-list with
    prose between bullets, a PowerShell `@(...)` array, or an inline comma
    list. Scattered single-token hits across widely-separated sections do
    not cluster within any window.

    Codex-Review Phase-2-Final Important #1 fix.
    """
    lines = text.splitlines()
    if not lines or not expected:
        return set()

    line_hits: list[set[str]] = []
    for line in lines:
        hits: set[str] = set()
        if _LIST_MARKER_RE.search(line):
            for bn in expected:
                if bn in line:
                    hits.add(bn)
        line_hits.append(hits)

    best: set[str] = set()
    for start in range(len(lines)):
        window: set[str] = set()
        end = min(start + window_lines, len(lines))
        for offset in range(end - start):
            window |= line_hits[start + offset]
        if len(window) > len(best):
            best = window
            if len(best) == len(expected):
                break  # full hit — no larger window possible
    return best


# §18 as governing-rule reference: NOT followed by '.' + digit (subsection)
_GOVERNING_18_RE = re.compile(r"§18(?!\.\d)")

def _scan_text_for_wrong_versions(text: str) -> list[str]:
    """Return list of wrong-version mentions (v1.7, v2.0) co-located with §18.

    Strict heuristic: scan line-by-line, flag only when SAME LINE contains
    BOTH a wrong-version-string AND a §18 reference that is NOT a subsection
    (§18.1, §18.2 are inline subsection refs — exclude). This prevents FP
    on changelog lines like 'v1.8 -> v2.0 ... (§18.1)'.
    Codex-Review TaskID 12 follow-up.
    """
    out: list[str] = []
    for line in text.splitlines():
        if not _GOVERNING_18_RE.search(line):
            continue
        for wv in WRONG_VERSIONS:
            if wv in line and wv not in out:
                out.append(wv)
    return out


def _audit_source(
    label: str,
    path: Path,
    repo_root: Path,
    require_version_string: bool,
    expected_basenames: tuple[str, ...],
) -> tuple[int, int, list[FailureDetail]]:
    """Audit a single source file. Returns (n_checked, n_passed, failures)."""
    failures: list[FailureDetail] = []
    if not path.exists():
        return 0, 0, [FailureDetail(
            location=str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path),
            expected="source file present",
            actual="missing",
            severity="warning",
            hint=f"{label}: erwartete Source-Datei fehlt im Repo",
        )]

    text = path.read_text(encoding="utf-8", errors="replace")
    if expected_basenames:
        found = _basenames_in_best_window(text, expected_basenames)
    else:
        found = set()
    missing = set(expected_basenames) - found
    rel_loc = str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path)

    for bn in sorted(missing):
        failures.append(FailureDetail(
            location=f"{rel_loc} ({label})",
            expected=f"basename '{bn}' in §18 7-File-Set listing",
            actual="not referenced",
            severity="error",
            hint=f"§18 v2.1 Score-Event-Set verlangt {bn}; bitte in {label} ergaenzen",
        ))

    if require_version_string:
        wrongs = _scan_text_for_wrong_versions(text)
        if wrongs:
            failures.append(FailureDetail(
                location=f"{rel_loc} ({label})",
                expected=f"§18 {CANONICAL_VERSION}",
                actual=f"§18 {wrongs[0]}",
                severity="error",
                hint=f"Versions-String-Drift; CLAUDE.md autoritativ ({CANONICAL_VERSION})",
            ))
        elif CANONICAL_VERSION not in text:
            failures.append(FailureDetail(
                location=f"{rel_loc} ({label})",
                expected=f"explicit '{CANONICAL_VERSION}' mention",
                actual="version string not found",
                severity="warning",
                hint=f"{label}-Header sollte §18 {CANONICAL_VERSION} explizit nennen",
            ))

    n_checked = 1
    n_passed = 1 if not failures else 0
    return n_checked, n_passed, failures


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    failures: list[FailureDetail] = []
    n_checked_total = 0
    n_passed_total = 0

    sources = [
        ("README", repo_root / "03_Tools" / "backtest-ready" / "README.md", True,
         CANONICAL_SCORE_EVENT_BASENAMES),
        # briefing-sync tracks Briefing-relevant state files (00_Core/* + config.yaml),
        # not the §18 score-event-set. F4 driver-intent is specifically: config.yaml
        # MUST appear in $briefingFiles (added in §18 v2.1 since 25.04.2026).
        # Auditing the full 7-set here was overly broad and only passed via comment-
        # mention false-positives in the file-wide scan; cluster-scan exposes that
        # the array genuinely doesn't list log.md / score_history.jsonl / flag_events.jsonl
        # (they're score-event JSONLs, not briefing-trigger inputs).
        ("briefing-sync", repo_root / "03_Tools" / "briefing-sync-check.ps1", False,
         ("config.yaml",)),
        ("dynastie-depot SKILL", repo_root / "01_Skills" / "dynastie-depot" / "SKILL.md", False,
         CANONICAL_SCORE_EVENT_BASENAMES),
        ("INSTRUKTIONEN", repo_root / "00_Core" / "INSTRUKTIONEN.md", True,
         ()),  # version-string-only, no basename-scan
    ]

    any_source_present = any(p.exists() for _, p, _, _ in sources)
    if not any_source_present:
        return CheckResult(
            name="score_event_parity", status="SKIP",
            n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(repo_root),
                expected="at least one §18-Parity source",
                actual="no source files found",
                severity="warning",
                hint="Repo-Layout veraendert? Sweep-Spec §28 referenziert 4 Sources",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    for label, path, require_version, expected in sources:
        nc, np_, fs = _audit_source(label, path, repo_root, require_version, expected)
        n_checked_total += nc
        n_passed_total += np_
        failures.extend(fs)

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="score_event_parity",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked_total,
        n_passed=n_passed_total,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
