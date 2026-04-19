"""Quarterly portfolio risk tool for Dynasty-Depot (11 Satelliten).

Outputs a Markdown report with three sections: correlation matrix,
component risk contribution, and historical stress-tests. Standalone
script, no workflow integration — run manually every quarter after
rebalancing.

Usage: python portfolio_risk.py [--weights-equal|--weights FILE]

Extracted from _extern/risk-metrics-calculation (PortfolioRisk +
StressTester), trimmed to the three patterns actually useful at a
33-year buy-and-hold horizon.

Wissenschaftlicher Kontext (19.04.2026): Basis für Palomar 2025 Ch 6
Risk-Metrics (Sortino/Calmar/Max-DD/CVaR/IR). Aktivierung Review
2028-04-01 nach 24+ Monaten sauberer Return-Serie (Phase 3 R5).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


SATELLITES = {
    "V": "V",
    "AVGO": "AVGO",
    "BRK.B": "BRK-B",
    "VEEV": "VEEV",
    "COST": "COST",
    "TMO": "TMO",
    "APH": "APH",
    "MSFT": "MSFT",
    "ASML": "ASML.AS",
    "RMS": "RMS.PA",
    "SU": "SU.PA",
}

STRESS_SCENARIOS = {
    "2020_covid_crash": ("2020-02-19", "2020-03-23"),
    "2022_rate_hikes": ("2022-01-01", "2022-10-31"),
}

HISTORY_START = "2019-01-01"
ANN_FACTOR = 252


def load_returns(tickers: dict[str, str]) -> pd.DataFrame:
    data = yf.download(
        list(tickers.values()),
        start=HISTORY_START,
        auto_adjust=True,
        progress=False,
    )["Close"]
    missing = [v for v in tickers.values() if v not in data.columns or data[v].isna().all()]
    for v in missing:
        retry = yf.download(v, start=HISTORY_START, auto_adjust=True, progress=False)
        if "Close" in retry and not retry["Close"].empty:
            data[v] = retry["Close"]
    still_missing = [v for v in tickers.values() if v not in data.columns or data[v].isna().all()]
    if still_missing:
        print(f"[warn] dropping tickers with no data: {still_missing}", file=sys.stderr)
        data = data.drop(columns=still_missing, errors="ignore")
    inv = {v: k for k, v in tickers.items()}
    data = data.rename(columns=inv)
    return data.pct_change().dropna(how="all")


def correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    return returns.corr()


def component_risk(returns: pd.DataFrame, weights: pd.Series) -> pd.DataFrame:
    cov = returns.cov() * ANN_FACTOR
    port_vol = float(np.sqrt(weights @ cov @ weights))
    mrc = (cov @ weights) / port_vol
    contribution = weights * mrc
    return pd.DataFrame({
        "weight": weights,
        "asset_vol_ann": returns.std() * np.sqrt(ANN_FACTOR),
        "risk_contribution": contribution,
        "risk_share_%": 100 * contribution / contribution.sum(),
    }).sort_values("risk_share_%", ascending=False)


def stress_test(returns: pd.DataFrame, weights: pd.Series) -> pd.DataFrame:
    port = returns @ weights
    rows = []
    for name, (start, end) in STRESS_SCENARIOS.items():
        window = port.loc[start:end]
        if window.empty:
            continue
        total = float((1 + window).prod() - 1)
        cum = (1 + window).cumprod()
        dd = float((cum / cum.cummax() - 1).min())
        rows.append({
            "scenario": name,
            "period": f"{start} to {end}",
            "total_return_%": 100 * total,
            "max_drawdown_%": 100 * dd,
            "worst_day_%": 100 * float(window.min()),
            "vol_ann_%": 100 * float(window.std() * np.sqrt(ANN_FACTOR)),
        })
    return pd.DataFrame(rows)


def _df_to_md(df: pd.DataFrame, index: bool = True) -> str:
    frame = df.reset_index() if index else df.copy()
    headers = [str(c) for c in frame.columns]
    rows = ["| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |"]
    for _, row in frame.iterrows():
        cells = []
        for v in row.tolist():
            if isinstance(v, float):
                cells.append(f"{v:.2f}" if abs(v) >= 0.01 or v == 0 else f"{v:.4f}")
            else:
                cells.append(str(v))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def render_markdown(corr: pd.DataFrame, comp: pd.DataFrame, stress: pd.DataFrame) -> str:
    today = date.today().isoformat()
    out = [
        f"# Portfolio-Risk-Report — {today}",
        "",
        "> Quarterly risk-audit (Correlation / Component Risk / Stress-Test).",
        "> Source: yfinance adjusted-close. Weights: equal unless specified.",
        "> Script: `03_Tools/portfolio_risk.py`.",
        "",
        "## 1. Correlation Matrix (daily returns, full history)",
        "",
        _df_to_md(corr.round(2)),
        "",
        "## 2. Component Risk Contribution (annualized)",
        "",
        _df_to_md(comp.round(4)),
        "",
        "**Top-3 Risk-Treiber:** " + ", ".join(comp.head(3).index.tolist()),
        "",
        "## 3. Historical Stress-Test",
        "",
        _df_to_md(stress.round(2), index=False),
        "",
    ]
    return "\n".join(out)


def _fetch_latest_common_closes(
    yahoo_symbols: list[str], lookback_days: int = 14
) -> tuple[date, pd.Series, pd.Series]:
    """Return (trading_date, latest_closes, previous_closes) from yfinance.

    Uses the most recent date on which ALL tickers have valid close prices
    (as-of intersection). Guarantees point-in-time consistency: if any ticker
    is missing data on date D, the record rolls back to D-1.
    """
    end = date.today() + timedelta(days=1)
    start = date.today() - timedelta(days=lookback_days)
    hist = yf.download(
        yahoo_symbols, start=start.isoformat(), end=end.isoformat(),
        auto_adjust=True, progress=False,
    )
    if hist.empty or "Close" not in hist:
        raise RuntimeError("No price data returned from yfinance.")
    closes = hist["Close"]
    if isinstance(closes, pd.Series):
        closes = closes.to_frame()
    missing_cols = [s for s in yahoo_symbols if s not in closes.columns]
    if missing_cols:
        raise RuntimeError(f"yfinance returned no columns for: {missing_cols}")
    common = closes.dropna(how="any")
    if len(common) < 2:
        raise RuntimeError(
            f"Need >=2 common trading dates for all {len(yahoo_symbols)} tickers, "
            f"got {len(common)}."
        )
    latest_ts = common.index[-1]
    trading_date = latest_ts.date() if hasattr(latest_ts, "date") else latest_ts
    return trading_date, common.iloc[-1], common.iloc[-2]


def persist_daily_snapshot(
    tickers: dict[str, str] = SATELLITES,
    cashflow_net: float = 0.0,
    benchmark: str = "SPY",
    archive_path: Path = Path("05_Archiv/portfolio_returns.jsonl"),
    benchmark_path: Path = Path("05_Archiv/benchmark-series.jsonl"),
    initial_notional: float = 10000.0,
) -> dict:
    """Append daily portfolio + benchmark snapshot to JSONL files.

    Portfolio-NAV-Modell: V_new = V_prev * (1 + r) + cashflow_net (post-cashflow NAV).
    Equal-weight basket across all satellites; first record uses initial_notional.

    Point-in-Time-Disziplin (§29.5 Sin #2): das `date`-Feld ist das yfinance-
    Trading-Date der letzten gemeinsam abgeschlossenen Handelssitzung aller
    Ticker (NICHT die Wall-Clock-Systemzeit). Läuft der Job am Wochenende/
    Feiertag, wird die letzte Session-Row getaggt. Duplicate-Date-Guard wirkt
    entsprechend — Mehrfach-Läufe am selben Wochenende schreiben nicht mehrfach.

    WICHTIG — Mixed-Currency-Approximation: Die 11 Satelliten mischen USD-
    (US-Tickers) und EUR-Titel (ASML.AS/RMS.PA/SU.PA). `portfolio_return` ist
    der equal-weighted Mittelwert der Lokalwährungs-Tagesrenditen — KEIN
    währungsbereinigter Multi-Currency-Portfolio-Return. Akzeptabel für Dynasty-
    Depot-Scope (synthetischer Local-Return-Index); für §29.2 AQR-Benchmark-
    Vergleiche muss FX-Conversion nachgerüstet werden (Interim-Gate 2027-10-19).
    """
    all_symbols = list(tickers.values()) + [benchmark]
    trading_date_obj, latest_closes, prev_closes = _fetch_latest_common_closes(all_symbols)
    trading_date = trading_date_obj.isoformat()

    for path in (archive_path, benchmark_path):
        if path.exists():
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    existing = json.loads(line)
                    if existing.get("date") == trading_date:
                        raise ValueError(
                            f"Duplicate date {trading_date} in {path}. "
                            f"Delete/edit manually if intentional."
                        )

    sat_returns = []
    for ticker, yahoo_symbol in tickers.items():
        latest_close = float(latest_closes[yahoo_symbol])
        prev_close = float(prev_closes[yahoo_symbol])
        daily_ret = (latest_close - prev_close) / prev_close
        sat_returns.append((ticker, latest_close, daily_ret))

    n = len(sat_returns)
    weight = 1.0 / n
    portfolio_return = float(np.mean([r for _, _, r in sat_returns]))

    prev_value = initial_notional
    if archive_path.exists() and archive_path.stat().st_size > 0:
        last_line = None
        with archive_path.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    last_line = line
        if last_line:
            prev_value = json.loads(last_line)["portfolio_value_gross"]

    portfolio_value_gross = prev_value * (1 + portfolio_return) + cashflow_net
    per_position_value = portfolio_value_gross / n

    positions = []
    for ticker, latest_close, _ in sat_returns:
        positions.append({
            "ticker": ticker,
            "weight_eod": round(weight, 6),
            "price_eod": round(latest_close, 4),
            "value_eod": round(per_position_value, 2),
        })

    bench_close = float(latest_closes[benchmark])
    bench_prev = float(prev_closes[benchmark])
    benchmark_return = (bench_close - bench_prev) / bench_prev

    record = {
        "schema_version": "1.0",
        "date": trading_date,
        "portfolio_value_gross": round(portfolio_value_gross, 2),
        "cashflow_net": round(cashflow_net, 2),
        "portfolio_return": round(portfolio_return, 5),
        "benchmark_value": round(bench_close, 2),
        "benchmark_return": round(benchmark_return, 5),
        "positions": positions,
    }
    bench_record = {
        "schema_version": "1.0",
        "date": trading_date,
        "benchmark": benchmark,
        "value": round(bench_close, 2),
        "daily_return": round(benchmark_return, 5),
    }

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    benchmark_path.parent.mkdir(parents=True, exist_ok=True)
    with archive_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    with benchmark_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(bench_record, ensure_ascii=False) + "\n")

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    print(
        f"[OK] Snapshot {trading_date} appended -- Portfolio {portfolio_value_gross:.2f} EUR "
        f"(r={portfolio_return:.4%}), Benchmark {benchmark}={bench_close:.2f} "
        f"(r={benchmark_return:.4%})"
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="03_Tools/Output")
    parser.add_argument("--persist", choices=["daily"],
                        help="Persistence mode (daily snapshot to JSONL)")
    parser.add_argument("--cashflow", type=float, default=0.0,
                        help="Net cashflow today in EUR (+ deposit, - withdrawal)")
    parser.add_argument("--benchmark", default="SPY",
                        help="Benchmark ticker (default: SPY)")
    parser.add_argument("--initial-notional", type=float, default=10000.0,
                        help="Initial portfolio notional EUR (first record only)")
    args = parser.parse_args()

    if args.persist == "daily":
        persist_daily_snapshot(
            tickers=SATELLITES,
            cashflow_net=args.cashflow,
            benchmark=args.benchmark,
            initial_notional=args.initial_notional,
        )
        return 0

    returns = load_returns(SATELLITES)
    active = [t for t in SATELLITES if t in returns.columns]
    n = len(active)
    weights = pd.Series(1 / n, index=active)

    returns = returns[active]
    corr = correlation_matrix(returns.dropna())
    comp = component_risk(returns.dropna(), weights)
    stress = stress_test(returns.dropna(how="all").fillna(0), weights)

    report = render_markdown(corr, comp, stress)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"PORTFOLIO-RISK-{date.today().isoformat()}.md"
    out_file.write_text(report, encoding="utf-8")

    sys.stdout.reconfigure(encoding="utf-8")
    print(report)
    print(f"\n[written to {out_file}]", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
