"""Check-1.5: Staleness detection for daily-persist stores.

Spec §5.1 Check-1.5. severity="warning" (WARN-Contribution); exit-code stays 0.
Escalation to "error" erst wenn Track 4 Auto-Persist-Cron existiert.
"""
from __future__ import annotations

import datetime
import json
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

LAG_THRESHOLD_BUSINESS_DAYS = 3  # Spec §5.1 Check-1.5: Puffer fuer Karfreitag/Oster


def last_business_day(today: datetime.date) -> datetime.date:
    """Return most recent Mon-Fri (today itself if today is Mon-Fri)."""
    d = today
    while d.weekday() >= 5:
        d -= datetime.timedelta(days=1)
    return d


def business_days_between(start: datetime.date, end: datetime.date) -> int:
    """Count Mon-Fri between start (exclusive) and end (inclusive)."""
    if end <= start:
        return 0
    days = 0
    d = start + datetime.timedelta(days=1)
    while d <= end:
        if d.weekday() < 5:
            days += 1
        d += datetime.timedelta(days=1)
    return days


def _last_record_date(path: Path) -> datetime.date | None:
    last_line = None
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                last_line = line
    if not last_line:
        return None
    rec = json.loads(last_line)
    return datetime.date.fromisoformat(rec["date"])


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    stores_override: dict[str, Path] | None = None,
) -> CheckResult:
    start = time.monotonic()

    stores = stores_override or {
        "portfolio_returns": repo_root / "05_Archiv" / "portfolio_returns.jsonl",
        "benchmark_series": repo_root / "05_Archiv" / "benchmark-series.jsonl",
    }

    today = datetime.date.today()
    lbd = last_business_day(today)

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0
    any_checked = False

    for store_name, path in stores.items():
        if not path.exists() or path.stat().st_size == 0:
            continue
        any_checked = True
        n_checked += 1
        last_date = _last_record_date(path)
        if last_date is None:
            continue
        lag = business_days_between(last_date, lbd)
        if lag > LAG_THRESHOLD_BUSINESS_DAYS:
            failures.append(FailureDetail(
                location=str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path),
                expected=f"last record >= {lbd.isoformat()} (<={LAG_THRESHOLD_BUSINESS_DAYS} business days lag)",
                actual=f"last record {last_date.isoformat()}, lag {lag} business days",
                severity="warning",
                hint="Daily-Append fehlt — Track 4 Auto-Persist-Cron offen",
            ))
        else:
            n_passed += 1

    if not any_checked:
        status: str = "SKIP"
    elif failures:
        status = "WARN"
    else:
        status = "PASS"

    return CheckResult(
        name="store_freshness",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
