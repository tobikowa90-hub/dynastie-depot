"""Check-7: Vault log.md must reflect recent git-HEAD commits.

Spec §5.1 Check-7 + INSTRUKTIONEN §18 Sync-Pflicht Position 1.
"""
from __future__ import annotations

import datetime
import re
import subprocess
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

LOG_ENTRY_RE = re.compile(r"^##\s+\[(\d{4}-\d{2}-\d{2})\]", re.MULTILINE)

DEFAULT_LOG_PATHS = [
    Path("log.md"),
    Path("07_Obsidian Vault") / "Obsidian Mindmap" / "Investing Mastermind" / "log.md",
    Path("07_Obsidian Vault") / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "log.md",
]


def _most_recent_log_date(text: str) -> datetime.date | None:
    dates: list[datetime.date] = []
    for m in LOG_ENTRY_RE.finditer(text):
        try:
            dates.append(datetime.date.fromisoformat(m.group(1)))
        except ValueError:
            continue
    return max(dates) if dates else None


def _git_head_date(repo_root: Path) -> datetime.date | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--pretty=%cs"],
            cwd=repo_root, capture_output=True, text=True, check=True, timeout=5,
        )
        return datetime.date.fromisoformat(out.stdout.strip())
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError):
        return None


def _business_days_lag(newer: datetime.date, older: datetime.date) -> int:
    if newer <= older:
        return 0
    d, days = older + datetime.timedelta(days=1), 0
    while d <= newer:
        if d.weekday() < 5:
            days += 1
        d += datetime.timedelta(days=1)
    return days


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()

    log_path = None
    for candidate in DEFAULT_LOG_PATHS:
        p = repo_root / candidate
        if p.exists():
            log_path = p
            break
    if log_path is None:
        return CheckResult(
            name="log_lag", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(DEFAULT_LOG_PATHS[0]),
                expected="log.md present", actual="missing",
                severity="warning", hint="log.md in Projekt-Root oder Vault erwartet",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    text = log_path.read_text(encoding="utf-8", errors="replace")
    log_date = _most_recent_log_date(text)
    head_date = _git_head_date(repo_root)

    if log_date is None or head_date is None:
        return CheckResult(
            name="log_lag", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(log_path.relative_to(repo_root)) if log_path.is_relative_to(repo_root) else str(log_path),
                expected="parseable log + git HEAD",
                actual=f"log={log_date}, head={head_date}",
                severity="warning", hint="log.md-Format oder git-Repo pruefen",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    lag = _business_days_lag(head_date, log_date)
    if lag > 1:
        return CheckResult(
            name="log_lag", status="FAIL", n_checked=1, n_passed=0,
            failures=[FailureDetail(
                location=str(log_path.relative_to(repo_root)) if log_path.is_relative_to(repo_root) else str(log_path),
                expected=f"log.md latest >= {head_date.isoformat()} - 1 business day",
                actual=f"log.md {log_date.isoformat()}, git HEAD {head_date.isoformat()} (lag {lag})",
                severity="error",
                hint="Sync-Pflicht §18 Position 1 verletzt — log.md-Entry nachtragen",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    return CheckResult(
        name="log_lag", status="PASS", n_checked=1, n_passed=1,
        failures=[], duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
