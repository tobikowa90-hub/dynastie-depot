#!/usr/bin/env python3
"""earnings_calendar.py — PIPELINE #24 Stufe 1.

Pulls next earnings dates for the 11 Dynastie satellites via yfinance,
diffs against PORTFOLIO.md "Nächster Trigger" cells, prints stdout report.

Usage:
    python 03_Tools/earnings_calendar.py --check
    python 03_Tools/earnings_calendar.py --check --smoke-test
    python 03_Tools/earnings_calendar.py --check --alert-window 14

Exit codes:
    0 = no drift, smoke-test PASS
    1 = smoke-test FAIL (only with --smoke-test)
    2 = drift detected within alert-window
"""

from __future__ import annotations

import argparse
import contextlib
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

import yaml
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "01_Skills" / "dynastie-depot" / "config.yaml"
PORTFOLIO = ROOT / "00_Core" / "PORTFOLIO.md"

# Yahoo-Suffix-Mapping: Dynastie-Symbol → Yahoo-Symbol
YAHOO_MAP: dict[str, str] = {
    "BRK.B": "BRK-B",
    "ASML": "ASML.AS",
    "RMS": "RMS.PA",
    "SU": "SU.PA",
}

# BRK.B FY26 Q1 = Saturday, 2026-05-02 (handover smoke-test)
SMOKE_TICKER = "BRK.B"
SMOKE_DATE = date(2026, 5, 2)


@dataclass
class EarningsResult:
    ticker: str
    yahoo_symbol: str
    earnings_date: Optional[date]
    source: str  # "earnings_dates" | "calendar" | "no_data" | "error"
    note: str = ""


def load_satellites() -> list[str]:
    if not CONFIG.exists():
        print(f"❌ Config nicht gefunden: {CONFIG}", file=sys.stderr)
        return []
    data = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    return [s["ticker"] for s in data.get("satelliten", [])]


def yahoo_symbol(ticker: str) -> str:
    return YAHOO_MAP.get(ticker, ticker)


def next_earnings(ticker: str, today: date) -> EarningsResult:
    sym = yahoo_symbol(ticker)
    t = yf.Ticker(sym)
    errors: list[str] = []

    # Primär: earnings_dates mit future-Filter
    try:
        df = t.earnings_dates
        if df is not None and not df.empty:
            future_dates = [idx.date() for idx in df.index if idx.date() >= today]
            if future_dates:
                return EarningsResult(ticker, sym, min(future_dates), "earnings_dates")
    except Exception as e:
        errors.append(f"earnings_dates: {e}")

    # Echter Fallback: calendar (Quirk: liefert bei RMS.PA/SU.PA letzten Termin Feb 26 statt next).
    # Wird auch durchlaufen wenn earnings_dates exception warf — fail-soft statt early-return.
    try:
        cal = t.calendar
        if cal:
            ed = cal.get("Earnings Date")
            if ed:
                d = ed[0] if isinstance(ed, list) else ed
                if hasattr(d, "date"):
                    d = d.date()
                if d >= today:
                    return EarningsResult(ticker, sym, d, "calendar")
                return EarningsResult(
                    ticker, sym, d, "calendar_stale",
                    note=f"calendar shows past date {d.isoformat()}",
                )
    except Exception as e:
        errors.append(f"calendar: {e}")

    if errors:
        return EarningsResult(ticker, sym, None, "error", note=" | ".join(errors))
    return EarningsResult(ticker, sym, None, "no_data")


def portfolio_trigger_cell(ticker: str, portfolio_text: str) -> str:
    """Best-effort extraction of 'Nächster Trigger' cell for ticker.

    Matches markdown table row | TICKER | ... | Trigger | (last column).
    """
    pattern = re.compile(
        rf"^\|\s*\*?\*?{re.escape(ticker)}\*?\*?\s*\|"
        r"[^|]+\|[^|]+\|[^|]+\|[^|]+\|([^|]+)\|\s*$",
        re.MULTILINE,
    )
    m = pattern.search(portfolio_text)
    return m.group(1).strip() if m else ""


def trigger_mentions_date(cell: str, d: date) -> bool:
    """Heuristic: does the trigger cell explicitly reference this earnings date?

    Word-boundary-aware: substring `02.05.` would otherwise match `02.05.2027` and
    silently suppress real drift. Pattern requires Jahr-vollständig ODER `dd.mm.`-
    Token mit non-digit-boundary danach (verhindert false positives bei Folge-Jahren).
    """
    yyyy_mm_dd = re.compile(rf"\b{d:%Y-%m-%d}\b")
    dd_mm_yyyy = re.compile(rf"\b{d:%d\.%m\.%Y}\b")
    # `dd.mm.` als kurzes Token: nicht direkt von einem Digit gefolgt (sonst dd.mm.YYYY-False-Match)
    dd_mm_short = re.compile(rf"\b{d:%d\.%m\.}(?!\d)")
    return any(p.search(cell) for p in (yyyy_mm_dd, dd_mm_yyyy, dd_mm_short))


def render_report(results: list[EarningsResult], today: date, alert_window: int,
                  portfolio_text: str) -> tuple[str, list[EarningsResult]]:
    lines = [f"# Earnings-Calendar — Stand {today.isoformat()}", ""]
    lines.append("| Ticker | Yahoo | Next Earnings | Days | Source | PORTFOLIO Trigger (excerpt) | Drift |")
    lines.append("|--------|-------|---------------|------|--------|------------------------------|-------|")
    drifts: list[EarningsResult] = []
    for r in results:
        cell = portfolio_trigger_cell(r.ticker, portfolio_text)
        cell_excerpt = cell[:60].replace("|", "\\|").replace("\n", " ")
        if r.earnings_date is None:
            lines.append(f"| {r.ticker} | {r.yahoo_symbol} | — | — | {r.source} | {cell_excerpt} | ⚠️ {r.note or 'no data'} |")
            continue
        days = (r.earnings_date - today).days
        in_trigger = trigger_mentions_date(cell, r.earnings_date)
        marker = ""
        if r.source == "calendar_stale":
            marker = "⚠️ stale"
        elif days < 0:
            marker = "ℹ️ past"
        elif days <= alert_window and not in_trigger:
            marker = "🔴 DRIFT"
            drifts.append(r)
        elif days <= alert_window:
            marker = "🟢 in trigger"
        elif days <= 30:
            marker = "🟡 soon"
        lines.append(
            f"| {r.ticker} | {r.yahoo_symbol} | {r.earnings_date.isoformat()} | "
            f"{days}d | {r.source} | {cell_excerpt} | {marker} |"
        )
    return "\n".join(lines), drifts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Dynastie-Earnings-Calendar (yfinance)")
    ap.add_argument("--check", action="store_true", help="run check + print report")
    ap.add_argument("--smoke-test", action="store_true",
                    help=f"hard-fail unless {SMOKE_TICKER} = {SMOKE_DATE.isoformat()}")
    ap.add_argument("--alert-window", type=int, default=10,
                    help="days for DRIFT alert (default: 10)")
    args = ap.parse_args(argv)

    if not args.check and not args.smoke_test:
        ap.print_help()
        return 0

    # Windows cp1252 stdout würde Unicode-Marker (✅🔴🟢🟡⚠️) crashen
    with contextlib.suppress(Exception):
        sys.stdout.reconfigure(encoding="utf-8")

    today = date.today()
    tickers = load_satellites()
    portfolio_text = PORTFOLIO.read_text(encoding="utf-8")
    results = [next_earnings(tk, today) for tk in tickers]

    report, drifts = render_report(results, today, args.alert_window, portfolio_text)
    print(report)
    print()

    # Smoke-Test BRK.B (Skip-if-past: nach SMOKE_DATE ist der Anker historisch — kein Hard-Fail).
    smoke = next((r for r in results if r.ticker == SMOKE_TICKER), None)
    if today > SMOKE_DATE:
        actual = smoke.earnings_date if smoke else None
        print(f"ℹ️ Smoke-Test SKIPPED: Anker {SMOKE_TICKER}={SMOKE_DATE.isoformat()} liegt in der Vergangenheit "
              f"(today={today.isoformat()}). Anker manuell auf nächsten BRK.B-Q-Termin updaten "
              f"(aktuell yfinance: {actual}).")
    elif smoke is not None and smoke.earnings_date == SMOKE_DATE:
        print(f"✅ Smoke-Test: {SMOKE_TICKER} = {SMOKE_DATE.isoformat()} PASS")
    else:
        actual = smoke.earnings_date if smoke else None
        print(f"❌ Smoke-Test FAIL: {SMOKE_TICKER} = {actual} (expected {SMOKE_DATE.isoformat()})")
        if args.smoke_test:
            return 1

    if drifts:
        print(f"\n## 🔴 Drifts detektiert ({len(drifts)}, Window {args.alert_window}d)")
        for r in drifts:
            cell = portfolio_trigger_cell(r.ticker, portfolio_text)
            print(f"- **{r.ticker}** {r.earnings_date.isoformat()} "
                  f"({(r.earnings_date - today).days}d) — PORTFOLIO-Trigger: {cell[:120]}")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
