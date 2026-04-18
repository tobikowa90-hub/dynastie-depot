"""FLAG-Event-Study — Dynasty-Depot Backtest-Ready Phase 3 (Task 3.1).

Deskriptive Auswertung rekonstruierter FLAG-Trigger gegen Forward-Horizonte
(+30/+90/+180/+360 Tage). Zweck: Infrastruktur-Validierung, KEINE statistische
Aussage. n<<10 → nur Median/Range, keine Mittelwerte oder Signifikanztests.

Methodik-Referenz:
  docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md §10

Inputs:
  - 05_Archiv/flag_events.jsonl (UTF-8)
  - yfinance (EOD Close) für Ticker + ^GSPC Benchmark

Outputs:
  - 02_Analysen/flag_event_study_<YYYY-MM-DD>.md (Markdown-Report)

CLI:
  python flag_event_study.py [--report-path PATH] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import median
from typing import Optional

# Projekt-lokale Imports
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from schemas import FlagEvent  # noqa: E402

# ---------------------------------------------------------------------------
# Konstanten
# ---------------------------------------------------------------------------

PROJECT_ROOT = SCRIPT_DIR.parent.parent  # C:/Users/tobia/OneDrive/Desktop/Claude Stuff
FLAG_EVENTS_PATH = PROJECT_ROOT / "05_Archiv" / "flag_events.jsonl"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "02_Analysen" / "flag_event_study_2026-04-17.md"

HORIZONS = [30, 90, 180, 360]
BENCHMARK_TICKER = "^GSPC"
TODAY = date(2026, 4, 17)  # Fixiertes Analyse-Datum für Reproduzierbarkeit


# ---------------------------------------------------------------------------
# Datenklassen
# ---------------------------------------------------------------------------


@dataclass
class HorizonResult:
    horizon_days: int
    status: str  # "observed" | "pending" | "n.a."
    pending_days_remaining: int = 0
    kurs_target: Optional[float] = None
    kurs_target_date: Optional[date] = None
    raw_return_pct: Optional[float] = None
    benchmark_return_pct: Optional[float] = None
    alpha_pp: Optional[float] = None


@dataclass
class EventResult:
    flag_id: str
    ticker: str
    flag_typ: str
    event_datum: date
    age_days: int
    kurs_at_trigger: Optional[float]
    kurs_at_trigger_date: Optional[date]
    kurs_benchmark_at_trigger: Optional[float]
    max_drawdown_pct: Optional[float] = None  # im Fenster [trigger, TODAY]
    max_drawdown_window_end: Optional[date] = None
    horizons: dict[int, HorizonResult] = field(default_factory=dict)
    wert_available: bool = True
    data_issue: Optional[str] = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _ensure_utf8_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass


def load_flag_events(path: Path) -> list[FlagEvent]:
    events: list[FlagEvent] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            events.append(FlagEvent.model_validate_json(line))
    return events


def fetch_history_window(ticker: str, start: date, end: date) -> Optional[dict[date, float]]:
    """Fetch daily Close prices for [start, end]. Returns {date: close} or None on failure."""
    try:
        import yfinance as yf
    except ImportError:
        return None
    try:
        t = yf.Ticker(ticker)
        # yfinance 'end' is exclusive; pad by 1 day
        hist = t.history(
            start=start.isoformat(),
            end=(end + timedelta(days=1)).isoformat(),
            auto_adjust=False,
        )
        if hist is None or hist.empty:
            return None
        out: dict[date, float] = {}
        for ts, row in hist.iterrows():
            # ts is pandas Timestamp with tz — convert to date
            d = ts.date() if hasattr(ts, "date") else ts
            out[d] = float(row["Close"])
        return out
    except Exception:
        return None


def closest_close_on_or_after(prices: dict[date, float], target: date, max_days: int = 7) -> Optional[tuple[date, float]]:
    """Find first available close on or after `target`, scanning up to `max_days` forward."""
    for i in range(max_days + 1):
        d = target + timedelta(days=i)
        if d in prices:
            return d, prices[d]
    return None


def closest_close_on_or_before(prices: dict[date, float], target: date, max_days: int = 7) -> Optional[tuple[date, float]]:
    for i in range(max_days + 1):
        d = target - timedelta(days=i)
        if d in prices:
            return d, prices[d]
    return None


# ---------------------------------------------------------------------------
# Kern-Berechnung
# ---------------------------------------------------------------------------


def compute_event_result(event: FlagEvent, today: date) -> EventResult:
    event_date = event.event_datum
    age_days = (today - event_date).days
    wert_available = event.metrik.wert is not None

    er = EventResult(
        flag_id=event.flag_id,
        ticker=event.ticker,
        flag_typ=event.flag_typ,
        event_datum=event_date,
        age_days=age_days,
        kurs_at_trigger=None,
        kurs_at_trigger_date=None,
        kurs_benchmark_at_trigger=None,
        wert_available=wert_available,
    )
    er.horizons = {h: HorizonResult(horizon_days=h, status="pending") for h in HORIZONS}

    # Window to pull: trigger - 3d through min(trigger+360+10, today+3)
    window_start = event_date - timedelta(days=5)
    window_end_candidate = event_date + timedelta(days=max(HORIZONS) + 10)
    window_end = min(window_end_candidate, today + timedelta(days=2))

    prices = fetch_history_window(event.ticker, window_start, window_end)
    bench = fetch_history_window(BENCHMARK_TICKER, window_start, window_end)

    if prices is None:
        er.data_issue = f"yfinance failed for {event.ticker}"
        for h in HORIZONS:
            er.horizons[h].status = "n.a."
        return er
    if bench is None:
        er.data_issue = f"yfinance failed for {BENCHMARK_TICKER}"

    # Trigger-Kurs (closest business day on/after event_datum)
    trigger_hit = closest_close_on_or_after(prices, event_date)
    if trigger_hit is None:
        er.data_issue = f"no price near trigger date for {event.ticker}"
        for h in HORIZONS:
            er.horizons[h].status = "n.a."
        return er
    er.kurs_at_trigger_date, er.kurs_at_trigger = trigger_hit

    if bench is not None:
        bench_hit = closest_close_on_or_after(bench, event_date)
        if bench_hit is not None:
            er.kurs_benchmark_at_trigger = bench_hit[1]

    # Max Drawdown im Fenster [trigger_date, today]
    fenster_prices = [
        p for d, p in prices.items() if er.kurs_at_trigger_date <= d <= today
    ]
    if fenster_prices:
        min_price = min(fenster_prices)
        min_date = min(d for d, p in prices.items() if er.kurs_at_trigger_date <= d <= today and p == min_price)
        er.max_drawdown_pct = (min_price - er.kurs_at_trigger) / er.kurs_at_trigger * 100.0
        er.max_drawdown_window_end = min(today, max(d for d in prices if d <= today))

    # Forward-Horizonte
    for h in HORIZONS:
        target_date = event_date + timedelta(days=h)
        hr = er.horizons[h]
        if target_date > today:
            hr.status = "pending"
            hr.pending_days_remaining = (target_date - today).days
            continue

        # Closest business day on/before target (if target itself missing, walk back)
        t_hit = closest_close_on_or_before(prices, target_date)
        if t_hit is None:
            t_hit = closest_close_on_or_after(prices, target_date)
        if t_hit is None:
            hr.status = "n.a."
            continue

        hr.kurs_target_date, hr.kurs_target = t_hit
        hr.status = "observed"
        hr.raw_return_pct = (hr.kurs_target - er.kurs_at_trigger) / er.kurs_at_trigger * 100.0

        if bench is not None and er.kurs_benchmark_at_trigger is not None:
            b_hit = closest_close_on_or_before(bench, target_date) or closest_close_on_or_after(bench, target_date)
            if b_hit is not None:
                b_date, b_price = b_hit
                hr.benchmark_return_pct = (b_price - er.kurs_benchmark_at_trigger) / er.kurs_benchmark_at_trigger * 100.0
                hr.alpha_pp = hr.raw_return_pct - hr.benchmark_return_pct

    return er


# ---------------------------------------------------------------------------
# Formatierung
# ---------------------------------------------------------------------------


def _fmt_pct(v: Optional[float]) -> str:
    return f"{v:+.2f}%" if v is not None else "–"


def _fmt_pp(v: Optional[float]) -> str:
    return f"{v:+.2f}pp" if v is not None else "–"


def _fmt_horizon_cell(hr: HorizonResult) -> str:
    if hr.status == "pending":
        return f"pending (needs {hr.pending_days_remaining} more days)"
    if hr.status == "n.a.":
        return "n.a. (data source)"
    return _fmt_pct(hr.raw_return_pct)


def _fmt_alpha_cell(hr: HorizonResult) -> str:
    if hr.status == "pending":
        return f"pending ({hr.pending_days_remaining}d)"
    if hr.status == "n.a." or hr.alpha_pp is None:
        return "n.a."
    return _fmt_pp(hr.alpha_pp)


def format_event_narrative_msft(er: EventResult) -> str:
    parts: list[str] = []
    parts.append(
        f"**Hintergrund (CORE-MEMORY §1):** CapEx/OCF Q2 FY26 GAAP 83,6 % (bereinigt um "
        f"Finance Leases ~63 %), damit über der 60 %-Schwelle. Trigger-Datum 2026-01-15 "
        f"ist Proxy (Monatsmitte; Earnings-Call ca. 30.01.)."
    )
    if er.kurs_at_trigger is not None:
        parts.append(
            f"**Kurs@Trigger (yfinance EOD {er.kurs_at_trigger_date}):** {er.kurs_at_trigger:.2f} USD."
        )
    h30 = er.horizons[30]
    h90 = er.horizons[90]
    if h30.status == "observed":
        parts.append(
            f"**+30d:** Raw {_fmt_pct(h30.raw_return_pct)}, Benchmark S&P500 "
            f"{_fmt_pct(h30.benchmark_return_pct)}, Alpha {_fmt_pp(h30.alpha_pp)}."
        )
    if h90.status == "observed":
        parts.append(
            f"**+90d:** Raw {_fmt_pct(h90.raw_return_pct)}, Benchmark "
            f"{_fmt_pct(h90.benchmark_return_pct)}, Alpha {_fmt_pp(h90.alpha_pp)}."
        )
    pending = [h for h in HORIZONS if er.horizons[h].status == "pending"]
    if pending:
        parts.append(
            f"**Noch offen:** Horizonte "
            f"{', '.join(f'+{h}d' for h in pending)} (observierbar ab späterem Review)."
        )
    return " ".join(parts)


def format_event_narrative_googl(er: EventResult) -> str:
    parts: list[str] = []
    parts.append(
        "**Hintergrund (CORE-MEMORY §3/§4):** FY26-Guidance nennt CapEx ~75 % OCF, "
        "FLAG-Record hat `wert=null` (Rohwert nicht eindeutig rekonstruierbar; Direction-"
        "Validator bewusst übersprungen). Trigger-Datum 2026-03-15 Proxy (Monatsmitte; "
        "Score-Datum im CORE-MEMORY ist 26.03. mit Score 72 / roter FLAG / kein Einstieg)."
    )
    if er.kurs_at_trigger is not None:
        parts.append(
            f"**Kurs@Trigger (yfinance EOD {er.kurs_at_trigger_date}):** {er.kurs_at_trigger:.2f} USD."
        )
    h30 = er.horizons[30]
    if h30.status == "observed":
        parts.append(
            f"**+30d:** Raw {_fmt_pct(h30.raw_return_pct)}, Benchmark S&P500 "
            f"{_fmt_pct(h30.benchmark_return_pct)}, Alpha {_fmt_pp(h30.alpha_pp)}."
        )
    pending = [h for h in HORIZONS if er.horizons[h].status == "pending"]
    if pending:
        parts.append(
            f"**Noch offen:** {', '.join(f'+{h}d' for h in pending)}."
        )
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Report-Generator
# ---------------------------------------------------------------------------


def build_report(results: list[EventResult], today: date) -> str:
    n = len(results)
    if n == 0:
        return _build_empty_report(today)

    datum_min = min(r.event_datum for r in results).isoformat()
    datum_max = max(r.event_datum for r in results).isoformat()

    lines: list[str] = []
    lines.append("# FLAG-Event-Study 2026-04-17 — Deskriptive Auswertung")
    lines.append("")
    lines.append(
        f"**Stichprobengröße:** n = {n} Events | **Zeitraum:** {datum_min} bis {datum_max}"
    )
    lines.append(
        "**Disclaimer:** *Nicht statistisch belastbar, rein deskriptiv. "
        "Infrastruktur-Validierung, keine Scoring-Kalibrierung.*"
    )
    lines.append(
        "**Methodik-Referenz:** `docs/superpowers/specs/"
        "2026-04-16-backtest-ready-infrastructure-design.md` §10"
    )
    lines.append("")

    # Section 1: Event-Tabelle
    lines.append("## 1. Event-Tabelle (alle FLAGs)")
    lines.append("")
    header = (
        "| flag_id | Ticker | Typ | Trigger-Datum | Alter (Tage) | Kurs@Trigger | "
        "Raw +30 | Raw +90 | Raw +180 | Raw +360 | MaxDD-Fenster | "
        "Alpha vs S&P500 +30 | Alpha +90 | Resolution? |"
    )
    sep = "|" + "|".join(["---"] * 14) + "|"
    lines.append(header)
    lines.append(sep)
    for r in results:
        kurs_cell = (
            f"{r.kurs_at_trigger:.2f} USD ({r.kurs_at_trigger_date})"
            if r.kurs_at_trigger is not None
            else "n.a. (data source)"
        )
        maxdd_cell = (
            f"{r.max_drawdown_pct:+.2f}% (bis {r.max_drawdown_window_end})"
            if r.max_drawdown_pct is not None
            else "n.a."
        )
        row = (
            f"| `{r.flag_id}` | {r.ticker} | {r.flag_typ} | "
            f"{r.event_datum} | {r.age_days} | {kurs_cell} | "
            f"{_fmt_horizon_cell(r.horizons[30])} | "
            f"{_fmt_horizon_cell(r.horizons[90])} | "
            f"{_fmt_horizon_cell(r.horizons[180])} | "
            f"{_fmt_horizon_cell(r.horizons[360])} | "
            f"{maxdd_cell} | "
            f"{_fmt_alpha_cell(r.horizons[30])} | "
            f"{_fmt_alpha_cell(r.horizons[90])} | "
            f"keine (Backfill-Sample) |"
        )
        lines.append(row)
    lines.append("")
    lines.append(
        "> *Für nicht-observierte Horizonte: \"pending (needs X more days)\". "
        "yfinance-Failures werden als \"n.a. (data source)\" markiert.*"
    )
    lines.append("")

    # Section 2: Aggregation per FLAG-Typ
    lines.append("## 2. Aggregation per FLAG-Typ")
    lines.append("")
    by_typ: dict[str, list[EventResult]] = {}
    for r in results:
        by_typ.setdefault(r.flag_typ, []).append(r)

    lines.append(
        "| FLAG-Typ | Anzahl | Median Raw +30 | Range Raw +30 | Median Raw +90 | Range Raw +90 |"
    )
    lines.append("|---|---|---|---|---|---|")
    for typ, items in sorted(by_typ.items()):
        vals_30 = [r.horizons[30].raw_return_pct for r in items if r.horizons[30].status == "observed" and r.horizons[30].raw_return_pct is not None]
        vals_90 = [r.horizons[90].raw_return_pct for r in items if r.horizons[90].status == "observed" and r.horizons[90].raw_return_pct is not None]

        def _med(xs: list[float]) -> str:
            return _fmt_pct(median(xs)) if xs else "–"

        def _range(xs: list[float]) -> str:
            return f"[{min(xs):+.2f}%, {max(xs):+.2f}%]" if xs else "–"

        lines.append(
            f"| {typ} | {len(items)} | {_med(vals_30)} | {_range(vals_30)} | {_med(vals_90)} | {_range(vals_90)} |"
        )
    lines.append("")
    lines.append(
        "> *n pro FLAG-Typ zu klein für Mittelwerte oder Signifikanztests — "
        "nur Median + Range ausgewiesen. Bei observed=0 steht \"–\".*"
    )
    lines.append("")

    # Section 3: Einzelfall-Narrativ
    lines.append("## 3. Einzelfall-Narrativ")
    lines.append("")
    msft = next((r for r in results if r.ticker == "MSFT"), None)
    googl = next((r for r in results if r.ticker == "GOOGL"), None)
    if msft:
        lines.append("### MSFT capex_ocf (Trigger 2026-01-15)")
        lines.append("")
        lines.append(format_event_narrative_msft(msft))
        lines.append("")
    if googl:
        lines.append("### GOOGL capex_ocf (Trigger 2026-03-15)")
        lines.append("")
        lines.append(format_event_narrative_googl(googl))
        lines.append("")

    # Other cases (catch-all)
    rest = [r for r in results if r.ticker not in ("MSFT", "GOOGL")]
    for r in rest:
        lines.append(f"### {r.ticker} {r.flag_typ} (Trigger {r.event_datum})")
        lines.append("")
        lines.append(f"Generisches Narrativ: age={r.age_days}d, kurs@trigger={r.kurs_at_trigger}.")
        lines.append("")

    # Section 4: Limitationen
    observed_total = sum(
        1 for r in results for h in HORIZONS if r.horizons[h].status == "observed"
    )
    pending_total = sum(
        1 for r in results for h in HORIZONS if r.horizons[h].status == "pending"
    )
    possible_total = n * len(HORIZONS)
    lines.append("## 4. Limitationen & Lehren für 2028-Review")
    lines.append("")
    lines.append(f"- **n = {n}** ist nicht-repräsentativ (Infrastruktur-Sample, keine statistische Power).")
    lines.append(
        f"- **{observed_total} / {possible_total}** Horizont-Messpunkte observierbar, "
        f"**{pending_total} / {possible_total}** pending (brauchen zusätzliche Marktdaten)."
    )
    lines.append(
        "- **GOOGL-FLAG-Record** hat `wert=null` (Backfill-Lücke, CORE-MEMORY §4 hält nur "
        "Score-Level fest, nicht exakten CapEx/OCF-Rohwert zum März-Stichtag)."
    )
    lines.append(
        "- **Backfill-Limit:** FLAGs vor 2026-04 nutzen Trigger-Datum-Proxies (Monatsmitte), "
        "was Event-Study-Präzision bei historischen Records reduziert (±15 Tage Unsicherheit im Stichtag)."
    )
    lines.append(
        "- **Ab 2026-04 live Forward-Pipeline** → zum 2028-Review-Zeitpunkt erwartete Sample-"
        "Size: **~15–25 Events** (annahme: 1–2 FLAGs/Quartal über ~2 Jahre für 10 aktive Symbole)."
    )
    lines.append(
        "- **Nächster Review-Auslöser:** wenn n≥10 UND 2/3 der Events +180d observierbar sind "
        "(frühestens Q4-2027 bei aktueller Trigger-Frequenz)."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        f"*Generiert am {today.isoformat()} via `03_Tools/backtest-ready/flag_event_study.py` "
        f"gegen `05_Archiv/flag_events.jsonl` (n={n}). "
        f"Benchmark: `^GSPC` (S&P 500 Composite, yfinance EOD Close, unadjusted).*"
    )
    return "\n".join(lines) + "\n"


def _build_empty_report(today: date) -> str:
    lines = [
        "# FLAG-Event-Study 2026-04-17 — Deskriptive Auswertung",
        "",
        "**Stichprobengröße:** n = 0 Events",
        "**Disclaimer:** *Nicht statistisch belastbar, rein deskriptiv. "
        "Infrastruktur-Validierung, keine Scoring-Kalibrierung.*",
        "**Methodik-Referenz:** `docs/superpowers/specs/"
        "2026-04-16-backtest-ready-infrastructure-design.md` §10",
        "",
        "## Ergebnis",
        "",
        "Keine rekonstruierbaren Events im Archiv (`05_Archiv/flag_events.jsonl`). "
        "Report ausgegeben als Infrastruktur-Validierung — Pipeline läuft korrekt durch "
        "trotz leerer Input-Menge.",
        "",
        f"*Generiert am {today.isoformat()}*",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def summary_for_stdout(results: list[EventResult]) -> str:
    n = len(results)
    observed = sum(1 for r in results for h in HORIZONS if r.horizons[h].status == "observed")
    pending = sum(1 for r in results for h in HORIZONS if r.horizons[h].status == "pending")
    na = sum(1 for r in results for h in HORIZONS if r.horizons[h].status == "n.a.")
    lines = [
        f"n = {n} Events",
        f"observed horizons: {observed}",
        f"pending horizons: {pending}",
        f"n.a. horizons: {na}",
    ]
    for r in results:
        h_parts = []
        for h in HORIZONS:
            hr = r.horizons[h]
            if hr.status == "observed":
                h_parts.append(f"+{h}d={hr.raw_return_pct:+.2f}%")
            else:
                h_parts.append(f"+{h}d={hr.status}")
        lines.append(f"  {r.flag_id}: kurs@trigger={r.kurs_at_trigger} | " + ", ".join(h_parts))
    return "\n".join(lines)


def main() -> int:
    _ensure_utf8_stdout()
    parser = argparse.ArgumentParser(description="FLAG-Event-Study (deskriptiv, n=2-Sample).")
    parser.add_argument(
        "--report-path",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Target Markdown path (default: 02_Analysen/flag_event_study_2026-04-17.md)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute + print summary, do NOT write report.",
    )
    args = parser.parse_args()

    if not FLAG_EVENTS_PATH.exists():
        print(f"[ERROR] {FLAG_EVENTS_PATH} not found.", file=sys.stderr)
        return 1

    events = load_flag_events(FLAG_EVENTS_PATH)
    # Filter: nur Trigger-Events (Resolutions wären separat behandelt — n=0 aktuell)
    triggers = [e for e in events if e.event_typ == "trigger"]

    results: list[EventResult] = []
    for ev in triggers:
        er = compute_event_result(ev, TODAY)
        results.append(er)

    summary = summary_for_stdout(results)
    print(summary)

    if args.dry_run:
        print("\n[dry-run] report NOT written.")
        return 0

    report_path: Path = args.report_path
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = build_report(results, TODAY)
    report_path.write_text(report, encoding="utf-8")
    print(f"\n[ok] report written: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
