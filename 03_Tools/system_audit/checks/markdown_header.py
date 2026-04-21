"""Check-2: Header-Stand-Drift across STATE.md / CORE-MEMORY.md / Faktortabelle.md.

Spec §5.1 Check-2 (Codex-Patch P6): compare header `**Stand:**` date to the
newest event-date parseable from the markdown content — NOT git commit date
(mass-edit commits would false-positive). Mon-Fri business-day lag threshold:
1-2 days -> WARN, >2 days -> FAIL.
"""
from __future__ import annotations

import datetime
import re
import time
from pathlib import Path
from typing import Callable

from system_audit.types import AuditContext, CheckResult, FailureDetail

STAND_RE = re.compile(r"\*\*Stand:\*\*\s*(\d{2}\.\d{2}\.\d{4})")
STAND_RE_HEADER = re.compile(r"Stand:\s*(\d{2}\.\d{2}\.\d{4})")
DATE_DOT = re.compile(r"(\d{2}\.\d{2}\.\d{4})")
DATE_ISO = re.compile(r"(\d{4}-\d{2}-\d{2})")


def _parse_dot(s: str) -> datetime.date:
    return datetime.datetime.strptime(s, "%d.%m.%Y").date()


def _parse_iso(s: str) -> datetime.date:
    return datetime.date.fromisoformat(s)


def _business_days_lag(newer: datetime.date, older: datetime.date) -> int:
    if newer <= older:
        return 0
    d, days = older + datetime.timedelta(days=1), 0
    while d <= newer:
        if d.weekday() < 5:
            days += 1
        d += datetime.timedelta(days=1)
    return days


def _stand_date(text: str) -> datetime.date | None:
    m = STAND_RE.search(text) or STAND_RE_HEADER.search(text)
    try:
        return _parse_dot(m.group(1)) if m else None
    except (ValueError, AttributeError):
        return None


def _newest_event_date_state(text: str) -> datetime.date | None:
    dates: list[datetime.date] = []
    for m in DATE_DOT.finditer(text):
        try:
            dates.append(_parse_dot(m.group(1)))
        except ValueError:
            pass
    for m in DATE_ISO.finditer(text):
        try:
            dates.append(_parse_iso(m.group(1)))
        except ValueError:
            pass
    return max(dates) if dates else None


def _newest_event_date_core_memory(text: str) -> datetime.date | None:
    dates: list[datetime.date] = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cell = line.strip()[1:].strip()
            m = DATE_DOT.match(cell)
            if m:
                try:
                    dates.append(_parse_dot(m.group(1)))
                except ValueError:
                    pass
    if dates:
        return max(dates)
    return _newest_event_date_state(text)


def _newest_event_date_faktortabelle(text: str) -> datetime.date | None:
    dates: list[datetime.date] = []
    for m in DATE_ISO.finditer(text):
        try:
            dates.append(_parse_iso(m.group(1)))
        except ValueError:
            pass
    return max(dates) if dates else None


PARSERS: dict[str, Callable[[str], datetime.date | None]] = {
    "state": _newest_event_date_state,
    "core_memory": _newest_event_date_core_memory,
    "faktortabelle": _newest_event_date_faktortabelle,
}


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    targets_override: list[tuple[Path, str]] | None = None,
) -> CheckResult:
    start = time.monotonic()

    targets = targets_override or [
        (repo_root / "00_Core" / "STATE.md", "state"),
        (repo_root / "00_Core" / "CORE-MEMORY.md", "core_memory"),
        (repo_root / "00_Core" / "Faktortabelle.md", "faktortabelle"),
    ]

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    for path, kind in targets:
        if not path.exists():
            failures.append(FailureDetail(
                location=str(path), expected="file present", actual="missing",
                severity="warning", hint="Target fehlt — Struktur geaendert?",
            ))
            continue
        text = path.read_text(encoding="utf-8")
        stand = _stand_date(text)
        newest = PARSERS[kind](text)

        n_checked += 1

        if stand is None or newest is None:
            failures.append(FailureDetail(
                location=str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path),
                expected="parseable Stand + event-date",
                actual=f"Stand={stand}, newest_event={newest}",
                severity="error",
                hint="Header-Regex matched nicht — Struktur geaendert?",
            ))
            continue

        lag = _business_days_lag(newest, stand)
        if lag > 2:
            failures.append(FailureDetail(
                location=str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path),
                expected=f"Stand >= {newest.isoformat()} or <= 2 business-day lag",
                actual=f"Stand {stand.isoformat()} vs newest-event {newest.isoformat()} (lag {lag} business days)",
                severity="error",
                hint=f"Header-Zeile auf {newest.strftime('%d.%m.%Y')} aktualisieren",
            ))
        elif lag >= 1:
            failures.append(FailureDetail(
                location=str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path),
                expected=f"Stand = {newest.isoformat()}",
                actual=f"Stand {stand.isoformat()} (lag {lag} business day)",
                severity="warning",
                hint="Header-Sync empfohlen",
            ))
            n_passed += 1
        else:
            n_passed += 1

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="markdown_header",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
