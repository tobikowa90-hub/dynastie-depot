"""Check-11: Header-Freshness (Phase 2 Sweep-Driver F6+F9).

Detects:
- FAIL: literal placeholder patterns (<YYYY-MM-DD>, TBD, <DATE>) in header
- WARN: header date stamp > 30 days old vs. today

Audited targets: whitelist of known header-bearing files. Each entry is
a (relative path, header-keyword) tuple. The keyword identifies which line
to scan ('Stand:' / 'Deployed:' / 'Aktualisiert:').
"""
from __future__ import annotations

import datetime as _dt
import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

DEFAULT_TARGETS = (
    ("03_Tools/morning-briefing-prompt-v3.md", "Deployed"),
    ("03_Tools/morning-briefing-prompt-v2.md", "Deployed"),
    ("01_Skills/insider-intelligence/SKILL.md", "Stand"),
    ("01_Skills/non-us-fundamentals/SKILL.md", "Stand"),
    ("01_Skills/dynastie-depot/SKILL.md", "Stand"),
    ("01_Skills/quick-screener/SKILL.md", "Stand"),
    ("01_Skills/backtest-ready-forward-verify/SKILL.md", "Stand"),
)
PLACEHOLDER_PATTERNS = ("<YYYY-MM-DD>", "<DATE>", "TBD", "<TBD>", "TODO")
STALE_THRESHOLD_DAYS = 30

_DATE_RE_DOTTED = re.compile(r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b")
_DATE_RE_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
HEADER_SCAN_LIMIT_LINES = 12  # Header-Zone (Title + Frontmatter + 1-2 Stand/Deployed-Lines)


def _extract_header_date(text: str, keyword: str) -> tuple[_dt.date | None, str | None]:
    """Find first line matching '<keyword>:' within header-zone (first
    HEADER_SCAN_LIMIT_LINES lines) and parse date.

    Header-Scope vermeidet false-matches an spaeteren Body-`Stand:`-Vorkommen
    (z.B. Versionshistorie, Beispiel-Snippets) — Codex-Review P2-06.

    Returns (date, raw_value). raw_value is the substring after ':' for
    placeholder-detection.
    """
    pattern = re.compile(rf"\*?\*?{re.escape(keyword)}\*?\*?\s*:\s*(.+)")
    lines = text.splitlines()[:HEADER_SCAN_LIMIT_LINES]
    for line in lines:
        m = pattern.match(line.strip())
        if not m:
            continue
        raw = m.group(1).strip()
        m_iso = _DATE_RE_ISO.search(raw)
        if m_iso:
            try:
                return _dt.date(int(m_iso.group(1)), int(m_iso.group(2)), int(m_iso.group(3))), raw
            except ValueError:
                return None, raw
        m_dot = _DATE_RE_DOTTED.search(raw)
        if m_dot:
            try:
                return _dt.date(int(m_dot.group(3)), int(m_dot.group(2)), int(m_dot.group(1))), raw
            except ValueError:
                return None, raw
        return None, raw
    return None, None


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    targets_override: list[tuple[Path, str]] | None = None,
    today: _dt.date | None = None,
) -> CheckResult:
    start = time.monotonic()
    today = today or _dt.date.today()
    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    if targets_override is not None:
        targets = targets_override
    else:
        targets = [(repo_root / rel, kw) for rel, kw in DEFAULT_TARGETS]

    present = [(p, kw) for p, kw in targets if p.exists()]
    if not present:
        return CheckResult(
            name="header_freshness", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(repo_root),
                expected="at least one header-bearing target",
                actual="no targets found",
                severity="warning",
                hint="DEFAULT_TARGETS-Liste pruefen — Repo-Layout veraendert?",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    for path, keyword in present:
        n_checked += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path)

        date_val, raw_val = _extract_header_date(text, keyword)

        if raw_val is not None and any(p in raw_val for p in PLACEHOLDER_PATTERNS):
            failures.append(FailureDetail(
                location=f"{rel}: {keyword}",
                expected="resolved date (YYYY-MM-DD or DD.MM.YYYY)",
                actual=raw_val,
                severity="error",
                hint="Header-Placeholder beim Deploy ersetzen (echtes Datum eintragen)",
            ))
            continue

        if raw_val is None:
            failures.append(FailureDetail(
                location=f"{rel}: {keyword}",
                expected=f"line '{keyword}: <date>' present",
                actual="header keyword not found",
                severity="warning",
                hint=f"{keyword}-Header ergaenzen oder Target aus DEFAULT_TARGETS entfernen",
            ))
            continue

        if date_val is None:
            failures.append(FailureDetail(
                location=f"{rel}: {keyword}",
                expected="parsable date",
                actual=raw_val,
                severity="warning",
                hint="Datum nicht im Format YYYY-MM-DD oder DD.MM.YYYY",
            ))
            continue

        age_days = (today - date_val).days
        if age_days > STALE_THRESHOLD_DAYS:
            failures.append(FailureDetail(
                location=f"{rel}: {keyword}",
                expected=f"date within {STALE_THRESHOLD_DAYS}d of today",
                actual=f"date={date_val.isoformat()} (age={age_days}d)",
                severity="warning",
                hint=f"Header-Stempel > {STALE_THRESHOLD_DAYS}d alt — Inhalt seitdem unveraendert?",
            ))
        else:
            n_passed += 1

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="header_freshness",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
