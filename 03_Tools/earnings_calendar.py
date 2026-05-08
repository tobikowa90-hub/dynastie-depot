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
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, date
from pathlib import Path

import yaml
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "01_Skills" / "dynastie-depot" / "config.yaml"
PORTFOLIO = ROOT / "00_Core" / "PORTFOLIO.md"
OVERRIDES_PATH = ROOT / "03_Tools" / "earnings_schedule_overrides.yaml"

# Yahoo-Suffix-Mapping: Dynastie-Symbol → Yahoo-Symbol
YAHOO_MAP: dict[str, str] = {
    "BRK.B": "BRK-B",
    "ASML": "ASML.AS",
    "RMS": "RMS.PA",
    "SU": "SU.PA",
}

# BRK.B FY26 Q2 - manuell nachgezogen 2026-05-06 (Stufe 2 deploy)
SMOKE_TICKER = "BRK.B"
SMOKE_DATE = date(2026, 8, 1)


@dataclass
class EarningsResult:
    ticker: str
    yahoo_symbol: str
    earnings_date: date | None
    # source: "earnings_dates" | "calendar" | "override" | "no_data" | "error" | "calendar_stale"
    # ODER alphabetisch sortierte Plus-Concat aller matching sources bei same-date,
    # z.B. "earnings_dates+override" | "calendar+override". Sortier-Order
    # ist deterministisch (sorted set) -> Tests koennen literal asserten.
    # "calendar_stale" tritt nur als alleinige source auf (Degraded-Fallback,
    # nie in min-Aggregation; siehe next_earnings Aggregations-Semantik).
    source: str
    note: str = ""
    event_type: str | None = None


@dataclass
class ScheduleEvent:
    date: date
    type: str
    note: str = ""


def load_satellites() -> list[str]:
    if not CONFIG.exists():
        print(f"❌ Config nicht gefunden: {CONFIG}", file=sys.stderr)
        return []
    data = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    return [s["ticker"] for s in data.get("satelliten", [])]


def yahoo_symbol(ticker: str) -> str:
    return YAHOO_MAP.get(ticker, ticker)


def load_overrides(today: date, path: Path = OVERRIDES_PATH) -> dict[str, list[ScheduleEvent]]:
    """Future-only override events keyed by ticker.

    Fail-soft on missing file, broken YAML, or read errors — returns {} so the
    tool degrades to yfinance-only behaviour rather than crashing the
    SessionStart hook.
    """
    if not path.exists():
        return {}
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (yaml.YAMLError, OSError, UnicodeDecodeError):
        # YAMLError = parse failure; OSError = file IO (permission, lock);
        # UnicodeDecodeError = file not UTF-8 (cp1252 etc.). Alle drei => degrade.
        return {}
    if not isinstance(raw, dict):
        return {}
    schedules = raw.get("schedules", {})
    if not isinstance(schedules, dict):
        return {}
    out: dict[str, list[ScheduleEvent]] = {}
    for ticker, ticker_block in schedules.items():
        if not isinstance(ticker_block, dict):
            continue
        events_raw = ticker_block.get("events", [])
        if not isinstance(events_raw, list):
            continue
        events: list[ScheduleEvent] = []
        for e in events_raw:
            if not isinstance(e, dict):
                continue
            d = e.get("date")
            if not isinstance(d, date) or d < today:
                continue
            events.append(ScheduleEvent(d, str(e.get("type", "")), str(e.get("note", ""))))
        if events:
            out[str(ticker)] = events
    return out


def next_earnings(
    ticker: str,
    today: date,
    data_source: Callable = yf.Ticker,
    overrides_path: Path = OVERRIDES_PATH,
) -> EarningsResult:
    """Earliest-wins Union aus yfinance future-dates + Override-YAML.

    `data_source` und `overrides_path` sind injectable für deterministische Unit-Tests.

    Aggregations-Semantik (HIGH-1-Fix nach Codex-R5):
    - Future candidates only: yfinance future_dates UND override future_dates
      gehen in min()-Auswahl ein.
    - Stale calendar (past date) wird NIE in die min()-Aggregation aufgenommen,
      da sie sonst valid-future-Overrides schlagen wuerde. Stattdessen wird
      sie nur als degraded-Fallback ausgegeben wenn KEINE other future
      candidates existieren — analog zum no_data-Pfad.
    """
    sym = yahoo_symbol(ticker)
    t = data_source(sym)
    yf_dates: list[date] = []
    cal_date_future: date | None = None
    cal_date_stale: date | None = None
    errors: list[str] = []

    # 1) Primaer: earnings_dates mit future-Filter
    try:
        df = t.earnings_dates
        if df is not None and not df.empty:
            yf_dates = sorted({idx.date() for idx in df.index if idx.date() >= today})
    except Exception as e:
        errors.append(f"earnings_dates: {e}")

    # 2) calendar-Fallback NUR wenn yfinance future-leer
    #    (Quirk: RMS.PA/SU.PA calendar zeigt manchmal letzten Termin statt next.)
    if not yf_dates:
        try:
            cal = t.calendar
            if cal:
                ed = cal.get("Earnings Date")
                if ed:
                    d = ed[0] if isinstance(ed, list) else ed
                    if hasattr(d, "date"):
                        d = d.date()
                    if d >= today:
                        cal_date_future = d
                    else:
                        cal_date_stale = d  # NICHT in min-aggregation aufnehmen
        except Exception as e:
            errors.append(f"calendar: {e}")

    # 3) Override-Pull (load_overrides filtert bereits future-only)
    overrides = load_overrides(today, overrides_path).get(ticker, [])

    # 4) Future-Candidate-Aggregation: union(yf_dates, override-dates, cal_future)
    #    earliest-wins. cal_date_stale wird hier bewusst NICHT eingebracht.
    candidates: list[tuple[date, str, str | None]] = []
    for d in yf_dates:
        candidates.append((d, "earnings_dates", None))
    for ev in overrides:
        candidates.append((ev.date, "override", ev.type or None))
    if cal_date_future is not None and not yf_dates:
        candidates.append((cal_date_future, "calendar", None))

    if candidates:
        earliest = min(c[0] for c in candidates)
        matching = [c for c in candidates if c[0] == earliest]
        sources = sorted({m[1] for m in matching})
        types = [m[2] for m in matching if m[2]]
        source_tag = "+".join(sources)
        event_type = types[0] if types else None
        return EarningsResult(
            ticker, sym, earliest, source_tag,
            event_type=event_type,
        )

    # 5) Kein future-candidate. Degraded-Fallbacks in Praeferenz-Reihenfolge:
    #    a) stale calendar date als sichtbares "calendar_stale"-Result
    #    b) errors -> "error"-Result
    #    c) "no_data"-Result
    if cal_date_stale is not None:
        return EarningsResult(
            ticker, sym, cal_date_stale, "calendar_stale",
            note=f"calendar shows past date {cal_date_stale.isoformat()}",
        )
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


TOOL_VERSION = "2.0"


def _classify_drift(r: EarningsResult, today: date, alert_window: int,
                    is_drift: bool = False) -> str:
    """Map render_report markers -> JSON drift_status enum.

    `is_drift` = ticker is in the drifts set produced by render_report.
    We honour that signal directly rather than re-deriving, so that the
    JSON output stays consistent with the markdown report logic.
    """
    if r.earnings_date is None:
        return "NO_DATA"
    if r.source == "calendar_stale":
        return "STALE"
    days = (r.earnings_date - today).days
    if days < 0:
        return "PAST"
    if is_drift:
        return "DRIFT"
    if days <= alert_window:
        return "IN_TRIGGER"
    return "SOON"


def build_json_payload(
    results: list[EarningsResult],
    drifts: set[str],
    today: date,
    alert_window: int,
    portfolio_text: str,
    exit_code: int,
) -> dict:
    """Result-Schema-Shape orientiert an system_audit/types.py::CheckResult (kein Hard-Import)."""
    from datetime import datetime

    items = []
    for r in results:
        cell = portfolio_trigger_cell(r.ticker, portfolio_text)
        cell_excerpt = cell[:120].replace("\n", " ")
        is_drift = r.ticker in drifts
        days_until = (r.earnings_date - today).days if r.earnings_date else None
        items.append({
            "ticker": r.ticker,
            "yahoo_symbol": r.yahoo_symbol,
            "earnings_date": r.earnings_date.isoformat() if r.earnings_date else None,
            "days_until": days_until,
            "source": r.source,
            "event_type": r.event_type,
            "drift_status": _classify_drift(r, today, alert_window, is_drift=is_drift),
            "portfolio_trigger_excerpt": cell_excerpt,
        })

    tickers_with_data = sum(1 for r in results if r.earnings_date is not None)
    return {
        "schema_version": "1.0",
        "tool": "earnings_calendar",
        "tool_version": TOOL_VERSION,
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "summary": {
            "tickers_checked": len(results),
            "tickers_with_data": tickers_with_data,
            "drifts": len(drifts),
            "alert_window_days": alert_window,
        },
        "exit_code": exit_code,
        "items": items,
    }


def evaluate_smoke(
    today: date,
    smoke_result: EarningsResult | None,
    smoke_ticker: str = SMOKE_TICKER,
    smoke_date: date = SMOKE_DATE,
) -> tuple[str, bool]:
    """Smoke-Test-Logic für main() — testbarer Helper (Codex-R10-MED-2-Closure).

    Returns (msg, failed). failed=True propagiert exit 1, wenn --smoke-test gesetzt.
    """
    actual = smoke_result.earnings_date if smoke_result else None
    if today > smoke_date:
        return (
            f"i  Smoke-Test SKIPPED: Anker {smoke_ticker}={smoke_date.isoformat()} "
            f"liegt in der Vergangenheit (today={today.isoformat()}). "
            f"Anker manuell auf naechsten BRK.B-Q-Termin updaten (yfinance: {actual}).",
            False,
        )
    if smoke_result is not None and smoke_result.earnings_date == smoke_date:
        return f"OK Smoke-Test: {smoke_ticker} = {smoke_date.isoformat()} PASS", False
    return (
        f"FAIL Smoke-Test: {smoke_ticker} = {actual} (expected {smoke_date.isoformat()})",
        True,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Dynastie-Earnings-Calendar (yfinance)")
    ap.add_argument("--check", action="store_true", help="run check + print report")
    ap.add_argument("--smoke-test", action="store_true",
                    help=f"hard-fail unless {SMOKE_TICKER} = {SMOKE_DATE.isoformat()}")
    ap.add_argument("--alert-window", type=int, default=10,
                    help="days for DRIFT alert (default: 10)")
    ap.add_argument("--json", action="store_true",
                    help="emit JSON to stdout instead of markdown report")
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
    drift_tickers = {r.ticker for r in drifts}

    # Smoke-Test (gleiche Logik wie v1.0; --smoke-test kann FAIL->exit 1 erzwingen)
    smoke = next((r for r in results if r.ticker == SMOKE_TICKER), None)
    smoke_msg, smoke_failed = evaluate_smoke(today, smoke)

    # MED-1-Fix (Codex-R5): exit_code-Bestimmung MUSS smoke-fail-Propagation
    # bereits beruecksichtigen, BEVOR build_json_payload aufgerufen wird —
    # sonst kann JSON exit_code=0/2 melden waehrend Process tatsaechlich exit 1
    # zurueckgibt. Bei --json --smoke-test waere das ein gefaehrliches Daten-
    # Inkonsistenz-Signal an die ps1-Hook-Konsumtion.
    if smoke_failed and args.smoke_test:
        exit_code = 1
    elif drifts:
        exit_code = 2
    else:
        exit_code = 0

    if args.json:
        import json
        payload = build_json_payload(
            results=results,
            drifts=drift_tickers,
            today=today,
            alert_window=args.alert_window,
            portfolio_text=portfolio_text,
            exit_code=exit_code,
        )
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(report)
        print()
        print(smoke_msg)
        if drifts:
            print(f"\n## Drifts detektiert ({len(drifts)}, Window {args.alert_window}d)")
            for r in drifts:
                cell = portfolio_trigger_cell(r.ticker, portfolio_text)
                print(f"- **{r.ticker}** {r.earnings_date.isoformat()} "
                      f"({(r.earnings_date - today).days}d) - PORTFOLIO-Trigger: {cell[:120]}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
