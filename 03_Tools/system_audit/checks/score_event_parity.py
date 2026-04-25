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


def _scan_text_for_basenames(text: str) -> set[str]:
    """Return basenames from CANONICAL set that appear at least once in text."""
    return {bn for bn in CANONICAL_SCORE_EVENT_BASENAMES if bn in text}


def _scan_text_for_wrong_versions(text: str) -> list[str]:
    """Return list of wrong-version mentions (v1.7, v2.0) co-located with §18.

    Strict heuristic: scan line-by-line, flag only when SAME LINE contains
    both a wrong-version-string AND a §18-marker (`§18` literal).
    Vermeidet false-positives bei Skill-Versionen (`version: 1.0.1`),
    System-Version (`v3.7`), und Cross-Section-Drift wo §18 in Z10 und
    `v1.7` in Z200 unbezogen sind (Codex-Review P2-07).
    """
    out: list[str] = []
    for line in text.splitlines():
        if "§18" not in line:
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
    found = _scan_text_for_basenames(text)
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
        ("briefing-sync", repo_root / "03_Tools" / "briefing-sync-check.ps1", False,
         CANONICAL_SCORE_EVENT_BASENAMES),
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
