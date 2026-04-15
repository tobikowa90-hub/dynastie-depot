#!/usr/bin/env python3
"""
Dynastie-Depot Non-US Fundamentals Module v1.1
================================================
Automatisierte Fundamentaldaten fuer ASML, RMS (Hermes) und SU (Schneider Electric)
via Yahoo Finance (yfinance). Kein API-Key noetig. Daten in EUR/IFRS.

EODHD-Hinweis: Free-Tier hat keinen Zugriff auf Fundamentals-Endpoint.
yfinance ist die kostenlose Alternative mit vollstaendiger Coverage.

Routing-Regel (aus SKILL-non-us-fundamentals.md):
  IF US_Ticker  -> Shibui SQL + defeatbeta MCP
  IF Non-US     -> dieses Script (yfinance, EUR-Ticker)

Verwendung:
    python eodhd_intel.py scan              # Alle 3 Non-US-Satelliten
    python eodhd_intel.py scan ASML         # Einzelner Ticker
    python eodhd_intel.py detail ASML       # Vollstaendiger DEFCON-Block
    python eodhd_intel.py prices            # Aktuelle EUR-Kurse + MA-Status
"""

import argparse
import json
import os
import sys
from datetime import datetime

import requests
import yfinance as yf
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

# Non-US Satelliten mit Yahoo Finance EUR-Symbolen
NON_US_SATELLITES = {
    "ASML": {
        "yf_symbol": "ASML.AS",          # Amsterdam Euronext
        "name": "ASML Holding N.V.",
        "currency": "EUR",
        "exchange": "Amsterdam",
        "reporting": "IFRS",
        "reporting_freq": "quarterly",    # ASML berichtet quartalsweise
        "substitute": "SNPS",
    },
    "RMS": {
        "yf_symbol": "RMS.PA",            # Paris Euronext
        "name": "Hermes International SCA",
        "currency": "EUR",
        "exchange": "Paris",
        "reporting": "IFRS",
        "reporting_freq": "semi-annual",  # H1 + H2 Berichte
        "substitute": "RACE",
    },
    "SU": {
        "yf_symbol": "SU.PA",             # Paris Euronext
        "name": "Schneider Electric SE",
        "currency": "EUR",
        "exchange": "Paris",
        "reporting": "IFRS",
        "reporting_freq": "semi-annual",  # H1 + H2 Berichte
        "substitute": "DE",
    },
}

FLAG_CAPEX_THRESHOLD = 60.0   # CapEx/OCF > 60% = FLAG
FLAG_SBC_THRESHOLD    = 15.0   # SBC/OCF  > 15% = FLAG

# API-Keys: config.json hat Vorrang, Env-Var als Fallback
def _load_config() -> dict:
    cfg_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(cfg_path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

_CFG = _load_config()
FRED_API_KEY = _CFG.get("fred_api_key") or os.getenv("FRED_API_KEY", "")


# ---------------------------------------------------------------------------
# FRED / WACC
# ---------------------------------------------------------------------------

def _get_http_session() -> requests.Session:
    """HTTP-Session mit Retry-Logik fuer FRED-Calls."""
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


def fetch_wacc_hurdle() -> dict:
    """Zieht den 10-Year Treasury Yield via FRED und berechnet WACC-Huerden.

    Benötigt env-Variable FRED_API_KEY (kostenlos: fred.stlouisfed.org/docs/api/).
    Fallback: statischer Wert 4.20% risikofreier Zins wenn kein Key oder API-Fehler.
    """
    EQUITY_RISK_PREMIUM = 5.0  # Standard-ERP
    WACC_BUFFER = 5.0          # Eiserne Regel: ROIC > WACC + 5%

    if FRED_API_KEY:
        try:
            url = (
                "https://api.stlouisfed.org/fred/series/observations"
                f"?series_id=DGS10&api_key={FRED_API_KEY}"
                "&file_type=json&sort_order=desc&limit=1"
            )
            resp = _get_http_session().get(url, timeout=5)
            resp.raise_for_status()
            risk_free = float(resp.json()["observations"][0]["value"])
            source = "Live (FRED DGS10)"
        except Exception:
            risk_free = 4.20
            source = "Fallback (FRED-Fehler)"
    else:
        risk_free = 4.20
        source = "Fallback (kein FRED_API_KEY)"

    wacc = round(risk_free + EQUITY_RISK_PREMIUM, 2)
    roic_hurdle = round(wacc + WACC_BUFFER, 2)
    return {
        "risk_free_pct": round(risk_free, 2),
        "wacc_pct": wacc,
        "roic_hurdle_pct": roic_hurdle,
        "source": source,
    }


# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------

def _safe(val, default=0.0):
    """Sichere Konvertierung zu float."""
    try:
        if val is None or str(val) in ("None", "", "nan", "NaT"):
            return default
        return float(val)
    except (ValueError, TypeError):
        return default


def _m(val):
    """Konvertiere zu Millionen (gerundet)."""
    return round(_safe(val) / 1e6, 1)


def _pct(numerator, denominator, decimals=1):
    """Prozentsatz berechnen."""
    n = _safe(numerator)
    d = _safe(denominator)
    if d == 0:
        return None
    return round(n / d * 100, decimals)


def _get_cf_row(cashflow_df, *row_names):
    """Extrahiere Cash-Flow-Zeile (verschiedene Bezeichnungen probieren)."""
    if cashflow_df is None or cashflow_df.empty:
        return None
    for name in row_names:
        if name in cashflow_df.index:
            return cashflow_df.loc[name]
    return None


def _get_bs_row(bs_df, *row_names):
    """Extrahiere Bilanz-Zeile."""
    if bs_df is None or bs_df.empty:
        return None
    for name in row_names:
        if name in bs_df.index:
            return bs_df.loc[name]
    return None


def _get_is_row(is_df, *row_names):
    """Extrahiere Gewinn-und-Verlust-Zeile."""
    if is_df is None or is_df.empty:
        return None
    for name in row_names:
        if name in is_df.index:
            return is_df.loc[name]
    return None


# ---------------------------------------------------------------------------
# Datenabruf und Aufbereitung
# ---------------------------------------------------------------------------

def fetch_metrics(ticker: str) -> dict:
    """Hole und berechne alle DEFCON-relevanten Metriken via yfinance."""
    meta = NON_US_SATELLITES[ticker]
    sym = meta["yf_symbol"]

    print(f"  [{ticker}] Lade Yahoo Finance Daten fuer {sym}...", file=sys.stderr)
    t = yf.Ticker(sym)

    info = t.info or {}
    cf = t.cashflow           # Jaehrlich, neueste zuerst
    bs = t.balance_sheet      # Jaehrlich
    inc = t.income_stmt       # Jaehrlich
    cf_q = t.quarterly_cashflow  # Quartalsweise

    # --- Aktueller Kurs & Marktdaten ---
    price = _safe(info.get("currentPrice") or info.get("regularMarketPrice"))
    market_cap = _safe(info.get("marketCap"))
    currency = info.get("currency", "EUR")

    # --- Cashflow-Historik (letzte 3 Jahre) ---
    ocf_row = _get_cf_row(cf, "Operating Cash Flow", "Cash From Operations",
                           "Total Cash From Operating Activities")
    capex_row = _get_cf_row(cf, "Capital Expenditure", "Capital Expenditures",
                             "Purchase Of Property Plant And Equipment")
    fcf_row = _get_cf_row(cf, "Free Cash Flow")
    sbc_row = _get_cf_row(cf, "Stock Based Compensation")

    # info-level TTM values as fallback for IFRS tickers (yfinance annual bug)
    info_ocf_ttm = _safe(info.get("operatingCashflow"))
    info_fcf_ttm = _safe(info.get("freeCashflow"))
    info_capex_ttm = (info_ocf_ttm - info_fcf_ttm) if (info_ocf_ttm > 0 and info_fcf_ttm > 0) else None

    capex_ocf_history = []
    if cf is not None and not cf.empty:
        cf_cols = list(cf.columns)
        for i, col in enumerate(cf_cols[:4]):  # Max 4 Jahre
            year = str(col.year)
            ocf = _safe(ocf_row[col] if ocf_row is not None else None)
            capex = abs(_safe(capex_row[col] if capex_row is not None else None))
            fcf_val = _safe(fcf_row[col] if fcf_row is not None else None)

            # Detect IFRS yfinance bug: FCF == OCF (CapEx not reported separately)
            # Fix: use info TTM values for the latest year; mark older years as n/a
            if capex == 0 and ocf > 0 and abs(fcf_val - ocf) < ocf * 0.01:
                if i == 0 and info_capex_ttm is not None:
                    capex = info_capex_ttm
                    fcf_val = info_fcf_ttm
                else:
                    fcf_val = None  # Historical CapEx not available via yfinance

            # FCF fallback (normal case: CapEx known but FCF row missing)
            if fcf_val is None or fcf_val == 0 and ocf > 0:
                fcf_val = ocf - capex if capex > 0 else None
            rev = _safe(info.get("totalRevenue")) if year == str(datetime.now().year - 1) else None
            # Versuche Revenue aus IS
            if inc is not None and not inc.empty:
                rev_row = _get_is_row(inc, "Total Revenue", "Revenue")
                if rev_row is not None and col in rev_row.index:
                    rev = _safe(rev_row[col])

            ratio = _pct(capex, ocf) if ocf > 0 and capex > 0 else None
            fcf_margin = _pct(fcf_val, rev) if (fcf_val is not None and rev and rev > 0) else None

            capex_ocf_history.append({
                "year": year,
                "ocf_m": _m(ocf),
                "capex_m": _m(capex) if capex > 0 else None,
                "fcf_m": _m(fcf_val) if fcf_val is not None else None,
                "capex_ocf_pct": ratio,
                "fcf_margin_pct": fcf_margin,
                "revenue_m": _m(rev) if rev else None,
            })

    # Aktuellste Werte fuer Scoring
    latest_ocf = _safe(info.get("operatingCashflow"))
    latest_fcf = _safe(info.get("freeCashflow"))
    latest_capex = latest_ocf - latest_fcf if latest_ocf and latest_fcf else None
    latest_capex_ocf_pct = _pct(latest_capex, latest_ocf) if latest_ocf else None

    # Alternativ aus der Tabelle nehmen
    if capex_ocf_history and capex_ocf_history[0]["capex_ocf_pct"] is not None:
        latest_capex_ocf_pct = capex_ocf_history[0]["capex_ocf_pct"]

    flag_capex = latest_capex_ocf_pct is not None and latest_capex_ocf_pct > FLAG_CAPEX_THRESHOLD

    # FCF-Trend-Flag: negativer FCF-Trend bei gleichzeitig steigendem CapEx (Veto-Regel)
    flag_fcf_trend = False
    if len(capex_ocf_history) >= 2:
        cur = capex_ocf_history[0]
        prv = capex_ocf_history[1]
        if (cur["fcf_m"] is not None and prv["fcf_m"] is not None and
                cur["capex_m"] is not None and prv["capex_m"] is not None):
            flag_fcf_trend = (cur["fcf_m"] < prv["fcf_m"]) and (cur["capex_m"] > prv["capex_m"])

    # SBC-Flag: SBC > 15% OCF
    latest_sbc = _safe(
        sbc_row[list(cf.columns)[0]]
        if sbc_row is not None and cf is not None and not cf.empty else None
    )
    sbc_ocf_pct = _pct(latest_sbc, latest_ocf) if latest_ocf > 0 and latest_sbc > 0 else None
    flag_sbc = sbc_ocf_pct is not None and sbc_ocf_pct > FLAG_SBC_THRESHOLD

    # FCF Yield
    fcf_yield_pct = _pct(latest_fcf, market_cap, 2) if market_cap > 0 else None

    # --- Bilanz ---
    total_assets = _safe(info.get("totalAssets")) or _safe(
        _get_bs_row(bs, "Total Assets")[list(bs.columns)[0]]
        if bs is not None and not bs.empty and _get_bs_row(bs, "Total Assets") is not None else None
    )
    goodwill_row = _get_bs_row(bs, "Goodwill", "Goodwill And Other Intangible Assets")
    goodwill = _safe(
        goodwill_row[list(bs.columns)[0]]
        if goodwill_row is not None and bs is not None and not bs.empty else None
    )
    net_debt = _safe(info.get("netDebt") or info.get("totalDebt"))
    ebitda = _safe(info.get("ebitda"))
    net_debt_ebitda = round(net_debt / ebitda, 2) if ebitda and ebitda > 0 else None
    goodwill_pct = _pct(goodwill, total_assets) if total_assets > 0 else None
    current_ratio = _safe(info.get("currentRatio"))

    # --- Margen ---
    revenue = _safe(info.get("totalRevenue"))
    gross_profit = _safe(info.get("grossProfits"))
    gross_margin_pct = _pct(gross_profit, revenue)
    net_income = _safe(info.get("netIncomeToCommon"))
    net_margin_pct = _pct(net_income, revenue)
    fcf_margin_pct = _pct(latest_fcf, revenue) if revenue > 0 else None

    # GM-Trend 3 Jahre
    gm_trend = []
    if inc is not None and not inc.empty:
        rev_row = _get_is_row(inc, "Total Revenue", "Revenue")
        gp_row = _get_is_row(inc, "Gross Profit")
        for col in list(inc.columns)[:3]:
            rv = _safe(rev_row[col] if rev_row is not None else None)
            gp = _safe(gp_row[col] if gp_row is not None else None)
            gm = _pct(gp, rv) if rv > 0 else None
            gm_trend.append({"year": str(col.year), "gm_pct": gm})

    # --- ROIC Proxy ---
    # Einfacher Proxy via info.returnOnEquity und info.returnOnAssets
    roe = _safe(info.get("returnOnEquity")) * 100 if info.get("returnOnEquity") else None
    roa = _safe(info.get("returnOnAssets")) * 100 if info.get("returnOnAssets") else None
    # ROIC Proxy: EBIT*(1-0.25) / (Total Assets - Current Liabilities)
    ebit = _safe(info.get("ebit"))
    curr_liab = _safe(info.get("currentLiabilities")) or _safe(
        _get_bs_row(bs, "Current Liabilities", "Total Current Liabilities")[list(bs.columns)[0]]
        if bs is not None and not bs.empty and _get_bs_row(bs, "Current Liabilities", "Total Current Liabilities") is not None else None
    )
    invested_capital = total_assets - curr_liab if total_assets and curr_liab else None
    roic_proxy = round(ebit * 0.75 / invested_capital * 100, 1) if ebit and invested_capital and invested_capital > 0 else None

    # --- Technicals ---
    sma200 = _safe(info.get("twoHundredDayAverage"))
    sma50 = _safe(info.get("fiftyDayAverage"))
    week52_high = _safe(info.get("fiftyTwoWeekHigh"))
    week52_low = _safe(info.get("fiftyTwoWeekLow"))
    beta = _safe(info.get("beta"))
    ath_dist_pct = _pct(price - week52_high, week52_high) if week52_high else None  # 52W als ATH-Proxy

    # --- Valuation ---
    fwd_pe = _safe(info.get("forwardPE"))
    trailing_pe = _safe(info.get("trailingPE"))
    p_fcf = round(market_cap / latest_fcf, 1) if market_cap and latest_fcf and latest_fcf > 0 else None
    ev_ebitda = _safe(info.get("enterpriseToEbitda"))
    peg = _safe(info.get("pegRatio"))

    # SBC (latest_sbc bereits oben berechnet)
    sbc = latest_sbc
    sbc_revenue_pct = _pct(sbc, revenue) if revenue > 0 else None

    # --- Analysten ---
    analyst_target = _safe(info.get("targetMeanPrice"))
    target_upside = _pct(analyst_target - price, price) if price and analyst_target else None
    recommendations = info.get("recommendationKey", "n/a")
    n_analysts = int(_safe(info.get("numberOfAnalystOpinions")))

    # Insider Ownership
    pct_insiders = _safe(info.get("heldPercentInsiders")) * 100
    pct_institutions = _safe(info.get("heldPercentInstitutions")) * 100

    return {
        "ticker": ticker,
        "yf_symbol": meta["yf_symbol"],
        "name": meta["name"],
        "exchange": meta["exchange"],
        "currency": currency,
        "reporting_standard": "IFRS",
        "reporting_freq": meta["reporting_freq"],
        "substitute": meta["substitute"],
        "scan_date": datetime.now().strftime("%Y-%m-%d"),

        # Kurs
        "price": price,
        "market_cap_m": _m(market_cap),
        "sma200": sma200,
        "sma50": sma50,
        "week52_high": week52_high,
        "week52_low": week52_low,
        "beta": beta,
        "ath_dist_pct": ath_dist_pct,

        # CapEx/OCF + Flags
        "capex_ocf_pct": latest_capex_ocf_pct,
        "flag_capex": flag_capex,
        "flag_fcf_trend": flag_fcf_trend,
        "flag_sbc": flag_sbc,
        "sbc_ocf_pct": sbc_ocf_pct,
        "capex_ocf_history": capex_ocf_history,

        # Bilanz
        "net_debt_m": _m(net_debt),
        "net_debt_ebitda": net_debt_ebitda,
        "goodwill_pct_assets": goodwill_pct,
        "current_ratio": current_ratio,
        "ebitda_m": _m(ebitda),

        # Margen
        "revenue_m": _m(revenue),
        "gross_margin_pct": gross_margin_pct,
        "fcf_margin_pct": fcf_margin_pct,
        "net_margin_pct": net_margin_pct,
        "gm_trend_3y": gm_trend,
        "sbc_revenue_pct": sbc_revenue_pct,

        # Valuation
        "fwd_pe": fwd_pe,
        "trailing_pe": trailing_pe,
        "p_fcf": p_fcf,
        "ev_ebitda": ev_ebitda,
        "fcf_yield_pct": fcf_yield_pct,
        "peg": peg,

        # ROIC
        "roic_proxy_pct": roic_proxy,
        "roe_pct": roe,
        "roa_pct": roa,

        # Analysten
        "analyst_target": analyst_target,
        "target_upside_pct": target_upside,
        "analyst_consensus": recommendations,
        "n_analysts": n_analysts,

        # Ownership
        "pct_insiders": pct_insiders,
        "pct_institutions": pct_institutions,
    }


# ---------------------------------------------------------------------------
# Output Formatter
# ---------------------------------------------------------------------------

def _flag_icon(condition):
    return "🔴" if condition else "🟢"


def _pct_label(val, good, warn):
    """Ampel-Label fuer Prozentwerte (je nach Richtung)."""
    if val is None:
        return "—"
    if val <= good:
        return f"{val:.1f}% 🟢"
    if val <= warn:
        return f"{val:.1f}% 🟡"
    return f"{val:.1f}% 🔴"


def format_defcon_block(m: dict, wacc: dict | None = None) -> str:
    """Formatiere vollstaendigen DEFCON-Fundamentals-Block."""
    curr = m["currency"]
    flag_icon = _flag_icon(m["flag_capex"])
    flag_text = "FLAG AKTIV" if m["flag_capex"] else "Clean"

    lines = [
        f"## Non-US Fundamentals: {m['ticker']} ({m['name']})",
        f"**Scan:** {m['scan_date']} | **Boerse:** {m['exchange']} ({m['yf_symbol']}) "
        f"| **Standard:** {m['reporting_standard']} ({m['reporting_freq']})",
        f"**Kurs:** {m['price']:.2f} {curr} | **Market Cap:** {m['market_cap_m']:,.0f}M {curr}",
        f"**Ersatz:** {m['substitute']}",
        "",
        "---",
        "",
    ]

    # --- WACC-Kontext ---
    if wacc:
        roic_ok = m.get("roic_proxy_pct") and m["roic_proxy_pct"] > wacc["roic_hurdle_pct"]
        roic_vs = f"{m['roic_proxy_pct']:.1f}% vs. Hürde {wacc['roic_hurdle_pct']:.1f}% — {'✅ übertrifft' if roic_ok else '⚠️ verfehlt'}" if m.get("roic_proxy_pct") else "n/a"
        lines.extend([
            "### WACC-Kontext",
            "",
            f"| Risikofreier Zins (10Y) | WACC (ERP +5%) | ROIC-Hürde (WACC +5%) | ROIC Proxy |",
            f"|------------------------|----------------|----------------------|------------|",
            f"| {wacc['risk_free_pct']:.2f}% ({wacc['source']}) | {wacc['wacc_pct']:.2f}% | {wacc['roic_hurdle_pct']:.2f}% | {roic_vs} |",
            "",
        ])

    # --- CapEx/OCF ---
    # Baue Warn-Suffixe fuer zusaetzliche Flags
    extra_flags = []
    if m.get("flag_fcf_trend"):
        extra_flags.append("⚠️ FCF-Trend negativ bei steigendem CapEx")
    if m.get("flag_sbc"):
        extra_flags.append(f"⚠️ SBC/OCF {m['sbc_ocf_pct']:.1f}% >15%")
    extra_str = " | " + " | ".join(extra_flags) if extra_flags else ""

    lines.extend([
        f"### CapEx/OCF — {flag_icon} {flag_text}{extra_str}",
        "",
        f"| Jahr | OCF ({curr}M) | CapEx ({curr}M) | FCF ({curr}M) | CapEx/OCF | FCF-Marge |",
        "|------|-------------|-------------|------------|-----------|-----------|",
    ])
    for row in m["capex_ocf_history"]:
        flag_marker = " 🔴" if row["capex_ocf_pct"] and row["capex_ocf_pct"] > 60 else ""
        capex_str = f"{row['capex_m']:,.1f}" if row["capex_m"] is not None else "n/a"
        fcf_str = f"{row['fcf_m']:,.1f}" if row["fcf_m"] is not None else "n/a"
        ratio_str = f"{row['capex_ocf_pct']:.1f}%{flag_marker}" if row["capex_ocf_pct"] is not None else "n/a"
        margin_str = f"{row['fcf_margin_pct']:.1f}%" if row["fcf_margin_pct"] is not None else "n/a"
        lines.append(
            f"| {row['year']} | {row['ocf_m']:,.1f} | {capex_str} | {fcf_str} | {ratio_str} | {margin_str} |"
        )
    lines.append("")

    # --- Bilanz ---
    lines.extend([
        "### Bilanz",
        "",
        "| Metrik | Wert | Ampel |",
        "|--------|------|-------|",
    ])
    if m["net_debt_ebitda"] is not None:
        nd_label = "🟢 <2.5x" if m["net_debt_ebitda"] < 2.5 else "🟡 2.5-3.5x" if m["net_debt_ebitda"] < 3.5 else "🔴 >3.5x"
        lines.append(f"| Net Debt/EBITDA | {m['net_debt_ebitda']:.2f}x | {nd_label} |")
    if m["goodwill_pct_assets"] is not None:
        gw_label = "🟢 <30%" if m["goodwill_pct_assets"] < 30 else "🟡 30-50%" if m["goodwill_pct_assets"] < 50 else "🔴 >50%"
        lines.append(f"| Goodwill/Assets | {m['goodwill_pct_assets']:.1f}% | {gw_label} |")
    if m["current_ratio"]:
        cr_label = "🟢 >1.5" if m["current_ratio"] > 1.5 else "🟡 1.0-1.5" if m["current_ratio"] >= 1.0 else "🔴 <1.0"
        lines.append(f"| Current Ratio | {m['current_ratio']:.2f} | {cr_label} |")
    lines.append(f"| Net Debt | {m['net_debt_m']:,.0f}M {curr} | — |")
    lines.append("")

    # --- Valuation ---
    lines.extend([
        "### Valuation",
        "",
        "| Metrik | Wert |",
        "|--------|------|",
        f"| Fwd P/E | {m['fwd_pe']:.1f}x |" if m["fwd_pe"] else "| Fwd P/E | n/a |",
        f"| P/FCF | {m['p_fcf']:.1f}x |" if m["p_fcf"] else "| P/FCF | n/a |",
        f"| EV/EBITDA | {m['ev_ebitda']:.1f}x |" if m["ev_ebitda"] else "| EV/EBITDA | n/a |",
        f"| FCF Yield | {m['fcf_yield_pct']:.2f}% |" if m["fcf_yield_pct"] else "| FCF Yield | n/a |",
        f"| PEG | {m['peg']:.2f} |" if m["peg"] else "| PEG | n/a |",
        "",
    ])

    # --- Margen + GM-Trend ---
    lines.extend([
        "### Margen",
        "",
        "| Metrik | Wert |",
        "|--------|------|",
        f"| Gross Margin | {m['gross_margin_pct']:.1f}% |" if m["gross_margin_pct"] else "| Gross Margin | n/a |",
        f"| FCF-Marge | {m['fcf_margin_pct']:.1f}% |" if m["fcf_margin_pct"] else "| FCF-Marge | n/a |",
        f"| Net Margin | {m['net_margin_pct']:.1f}% |" if m["net_margin_pct"] else "| Net Margin | n/a |",
        f"| SBC/Revenue | {m['sbc_revenue_pct']:.1f}% |" if m["sbc_revenue_pct"] else "| SBC/Revenue | n/a |",
        "",
    ])

    # GM-Trend
    gm_vals = [r["gm_pct"] for r in m["gm_trend_3y"] if r["gm_pct"]]
    if len(gm_vals) >= 2:
        gm_delta = gm_vals[0] - gm_vals[-1]
        trend_label = (
            f"🟢 Steigend +{gm_delta:.1f}pp" if gm_delta > 1
            else f"🔴 Fallend {gm_delta:.1f}pp" if gm_delta < -1
            else "🟡 Stabil"
        )
        gm_str = " → ".join(f"{r['year']}: {r['gm_pct']:.1f}%" for r in reversed(m["gm_trend_3y"]) if r["gm_pct"])
        lines.append(f"**GM-Trend 3J:** {trend_label} | {gm_str}")
        lines.append("")

    # --- ROIC ---
    lines.extend([
        "### Profitabilitaet",
        "",
        f"| ROIC (Proxy) | {'%.1f%%' % m['roic_proxy_pct'] if m['roic_proxy_pct'] else 'n/a'} | _Verifikation via GuruFocus empfohlen_ |",
        f"| ROE | {'%.1f%%' % m['roe_pct'] if m['roe_pct'] else 'n/a'} | |",
        f"| ROA | {'%.1f%%' % m['roa_pct'] if m['roa_pct'] else 'n/a'} | |",
        "",
    ])

    # --- Technicals ---
    if m["sma200"] and m["price"]:
        vs_200 = round((m["price"] / m["sma200"] - 1) * 100, 1)
        ma_label = "🟢 ueber 200MA" if vs_200 > 0 else "🔴 unter 200MA"
        ath_str = f"{m['ath_dist_pct']:.1f}%" if m["ath_dist_pct"] else "—"
        lines.extend([
            "### Technicals (Kurzblock)",
            "",
            f"| Kurs | SMA-200 | vs. 200MA | 52W-Hoch | Dist. 52W | Beta |",
            f"|------|---------|-----------|----------|-----------|------|",
            f"| {m['price']:.2f} | {m['sma200']:.2f} | {vs_200:+.1f}% {ma_label} "
            f"| {m['week52_high']:.2f} | {ath_str} | {m['beta']:.2f} |",
            "",
        ])

    # --- Analysten ---
    if m["n_analysts"] > 0:
        upside_str = f"{m['target_upside_pct']:+.1f}%" if m["target_upside_pct"] else "—"
        lines.extend([
            "### Analysten",
            "",
            f"**Konsensus:** {m['analyst_consensus']} ({m['n_analysts']} Analysten)",
            f"**Ø Kursziel:** {m['analyst_target']:.2f} {curr} ({upside_str} Upside)" if m["analyst_target"] else "",
            "",
        ])

    # --- Ownership ---
    ins_label = "🟢 >1%" if m["pct_insiders"] >= 1 else "🟡 0.1-1%" if m["pct_insiders"] >= 0.1 else "🔴 <0.1%"
    lines.extend([
        "### Ownership",
        "",
        f"- Insider: {m['pct_insiders']:.2f}% {ins_label}",
        f"- Institutionen: {m['pct_institutions']:.1f}%",
        "",
        f"_Non-US Insider-Pflicht: {'AFM' if m['ticker'] == 'ASML' else 'AMF'} manuell pruefen — keine Form-4-Pflicht._",
    ])

    return "\n".join(lines)


def format_summary_table(results: list[dict]) -> str:
    """Kompakte Uebersichtstabelle aller Non-US-Satelliten."""
    lines = [
        f"# Non-US Fundamentals — Uebersicht",
        f"**Datum:** {datetime.now().strftime('%d.%m.%Y')} | Quelle: Yahoo Finance (EUR)",
        "",
        "| Ticker | Kurs EUR | CapEx/OCF | FLAG | Fwd P/E | P/FCF | FCF-Marge | Net Debt/EBITDA |",
        "|--------|----------|-----------|------|---------|-------|-----------|----------------|",
    ]
    for m in results:
        if "error" in m:
            lines.append(f"| {m['ticker']} | FEHLER | — | — | — | — | — | — |")
            continue
        flag = "🔴" if m["flag_capex"] else "🟢"
        lines.append(
            f"| {m['ticker']} | {m['price']:.2f} | "
            f"{'%.1f%%' % m['capex_ocf_pct'] if m['capex_ocf_pct'] else '—'} | {flag} | "
            f"{'%.1f%%' % m['fwd_pe'] + 'x' if m['fwd_pe'] else '—'} | "
            f"{'%.1f' % m['p_fcf'] + 'x' if m['p_fcf'] else '—'} | "
            f"{'%.1f%%' % m['fcf_margin_pct'] if m['fcf_margin_pct'] else '—'} | "
            f"{'%.2f' % m['net_debt_ebitda'] + 'x' if m['net_debt_ebitda'] else '—'} |"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Dynastie-Depot Non-US Fundamentals v1.1 (yfinance)"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_scan = sub.add_parser("scan", help="Scan Non-US Satelliten")
    p_scan.add_argument("tickers", nargs="*", help="Ticker (leer = ASML RMS SU)")
    p_scan.add_argument("--json", action="store_true", help="JSON-Output")
    p_scan.add_argument("--summary", action="store_true", help="Nur Uebersichtstabelle")

    p_det = sub.add_parser("detail", help="Vollstaendiger DEFCON-Block")
    p_det.add_argument("ticker", help="ASML, RMS oder SU")

    sub.add_parser("prices", help="Aktuelle EUR-Kurse + MA-Status")

    args = parser.parse_args()

    if args.command == "scan":
        tickers = [t.upper() for t in args.tickers] if args.tickers else list(NON_US_SATELLITES.keys())
        results = []
        for ticker in tickers:
            if ticker not in NON_US_SATELLITES:
                results.append({"ticker": ticker, "error": f"Nicht in NON_US_SATELLITES. Verfuegbar: {list(NON_US_SATELLITES.keys())}"})
                continue
            try:
                m = fetch_metrics(ticker)
                results.append(m)
            except Exception as e:
                results.append({"ticker": ticker, "error": str(e)})

        if args.json:
            print(json.dumps(results, indent=2, default=str))
        elif args.summary:
            print(format_summary_table([r for r in results if "error" not in r]))
        else:
            for r in results:
                if "error" in r:
                    print(f"### {r['ticker']} — FEHLER: {r['error']}\n")
                else:
                    print(format_defcon_block(r))
                    print("\n---\n")

    elif args.command == "detail":
        ticker = args.ticker.upper()
        if ticker not in NON_US_SATELLITES:
            print(f"FEHLER: {ticker} unbekannt. Verfuegbar: {list(NON_US_SATELLITES.keys())}", file=sys.stderr)
            sys.exit(1)
        try:
            m = fetch_metrics(ticker)
            wacc = fetch_wacc_hurdle()
            print(format_defcon_block(m, wacc=wacc))
        except Exception as e:
            print(f"FEHLER: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "prices":
        print(f"# Non-US Kurse — {datetime.now().strftime('%d.%m.%Y')}\n")
        print("| Ticker | Kurs EUR | SMA-200 | vs. 200MA | 52W-Hoch | Dist. 52W |")
        print("|--------|----------|---------|-----------|----------|-----------|")
        for ticker in NON_US_SATELLITES:
            try:
                m = fetch_metrics(ticker)
                if m["sma200"] and m["price"]:
                    vs = round((m["price"] / m["sma200"] - 1) * 100, 1)
                    ath_dist = f"{m['ath_dist_pct']:.1f}%" if m["ath_dist_pct"] else "—"
                    print(f"| {ticker} | {m['price']:.2f} | {m['sma200']:.2f} | {vs:+.1f}% | {m['week52_high']:.2f} | {ath_dist} |")
                else:
                    print(f"| {ticker} | {m['price']:.2f} | — | — | — | — |")
            except Exception as e:
                print(f"| {ticker} | FEHLER | — | — | — | {e} |")


if __name__ == "__main__":
    main()
