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
import sys
from datetime import date
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="03_Tools/Output")
    args = parser.parse_args()

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
