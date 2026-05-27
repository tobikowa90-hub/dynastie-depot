"""Check-14: Pointer-Completeness (Phase 2 Sweep-Driver F12, eng scoped).

Parses CLAUDE.md's '## Pointer (Ausgelagertes)'-section ONLY for backtick-
quoted relative paths and asserts each path exists in the repo. FAIL on
missing target.

Heuristik konservativ: nur Backtick-quoted Single-Token-Paths in Tabellen-
Zellen INNERHALB der '## Pointer'-Section, kein freier Prosa-Match (FP-Risk
hoch — '01_Skills' ohne Datei waere keine Behauptung sondern Erwaehnung).
Section-Scoping verhindert Treffer aus Routing-Tabelle, Wiki-Modus-Section
oder Beispiel-Code-Bloecken (Codex-Review P2-09).
"""

from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.audit_types import AuditContext, CheckResult, FailureDetail

# Match a markdown table row '| `path/to/file` | Zweck |'
POINTER_RE = re.compile(r"\|\s*`([^`]+)`\s*\|", re.MULTILINE)
# Section-Anker: '## Pointer'-Heading (mit optionalem Suffix wie '(Ausgelagertes)')
SECTION_HEADER_RE = re.compile(r"^##\s+Pointer\b.*$", re.MULTILINE)
# Naechste gleich-tiefe oder hoehere Section-Boundary
NEXT_SECTION_RE = re.compile(r"^##\s+(?!Pointer\b).+$", re.MULTILINE)


def _extract_pointer_section(text: str) -> str | None:
    """Return only the '## Pointer'-section body, or None if no such section."""
    m_start = SECTION_HEADER_RE.search(text)
    if not m_start:
        return None
    body_start = m_start.end()
    m_next = NEXT_SECTION_RE.search(text, body_start)
    body_end = m_next.start() if m_next else len(text)
    return text[body_start:body_end]


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    claude_md = repo_root / "CLAUDE.md"
    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    if not claude_md.exists():
        return CheckResult(
            name="pointer_completeness",
            status="SKIP",
            n_checked=0,
            n_passed=0,
            failures=[
                FailureDetail(
                    location="CLAUDE.md",
                    expected="CLAUDE.md present",
                    actual="missing",
                    severity="warning",
                    hint="Repo ohne CLAUDE.md? Test-Repo?",
                )
            ],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    full_text = claude_md.read_text(encoding="utf-8", errors="replace")
    section = _extract_pointer_section(full_text)
    if section is None:
        return CheckResult(
            name="pointer_completeness",
            status="SKIP",
            n_checked=0,
            n_passed=0,
            failures=[
                FailureDetail(
                    location="CLAUDE.md: '## Pointer'-section",
                    expected="'## Pointer'-Heading present",
                    actual="section heading not found",
                    severity="warning",
                    hint="CLAUDE.md ohne Pointer-Section — Layout veraendert?",
                )
            ],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    text = section
    seen: set[str] = set()
    for m in POINTER_RE.finditer(text):
        rel = m.group(1).strip()
        if rel in seen:
            continue
        seen.add(rel)
        if "/" not in rel and not rel.endswith(".md"):
            continue  # not a path
        if any(c in rel for c in (" ", "<", ">", "`", "\n")):
            continue  # not a clean path token
        n_checked += 1
        target = repo_root / rel
        if target.exists():
            n_passed += 1
        else:
            failures.append(
                FailureDetail(
                    location=f"CLAUDE.md: pointer `{rel}`",
                    expected=f"path '{rel}' resolvable from repo-root",
                    actual="path does not exist",
                    severity="error",
                    hint=f"Pointer in CLAUDE.md zeigt auf fehlende Datei {rel} — entweder Datei anlegen oder Pointer entfernen",
                )
            )

    if n_checked == 0:
        return CheckResult(
            name="pointer_completeness",
            status="SKIP",
            n_checked=0,
            n_passed=0,
            failures=[
                FailureDetail(
                    location="CLAUDE.md",
                    expected="at least one pointer-table entry",
                    actual="no parsable pointers found",
                    severity="warning",
                    hint="POINTER_RE matched nichts — Tabellen-Format aendern? Section-Header?",
                )
            ],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="pointer_completeness",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
