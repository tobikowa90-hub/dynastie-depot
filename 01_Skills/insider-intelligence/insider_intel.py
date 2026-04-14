#!/usr/bin/env python3
"""
Dynastie-Depot Insider Intelligence Module v1.0
================================================
Spezialisiertes Form-4-Abfrage-Tool fuer die 8 US-Satelliten des Dynastie-Depots.
Ersetzt den generischen sec-edgar-skill fuer den DEFCON-Insider-Scoring-Block.

Verwendung:
    python insider_intel.py scan                    # Alle 8 US-Satelliten scannen
    python insider_intel.py scan AVGO MSFT          # Nur bestimmte Ticker
    python insider_intel.py detail AVGO             # Detail-Report eines Tickers
    python insider_intel.py flag-check              # Nur FLAG-relevante Transaktionen
    python insider_intel.py factor-sync             # 3-Wege-Vergleich config/Tabelle/Live

SEC EDGAR API: Kein API-Key noetig. Nur User-Agent-Header (SEC Fair Access Policy).
Rate Limit: max 10 req/s — Script haelt 0.12s Pause pro Request (~8 req/s).
"""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

import requests

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

DATA_URL = "https://data.sec.gov"
SEC_WWW = "https://www.sec.gov"

# SEC-Pflicht: User-Agent mit Name + Email
USER_AGENT = "Tobias tobikowa90@gmail.com"

# CIK-Tabelle: Alle US-Satelliten des Dynastie-Depots
# Einmalig hinterlegt — bei Slot-Tausch aktualisieren
SATELLITES_CIK = {
    "AVGO":  "0001730168",  # Broadcom Inc.
    "MSFT":  "0000789019",  # Microsoft Corporation
    "V":     "0001403161",  # Visa Inc.
    "BRK.B": "0001067983",  # Berkshire Hathaway Inc.
    "TMO":   "0000097745",  # Thermo Fisher Scientific
    "VEEV":  "0001393052",  # Veeva Systems Inc.
    "APH":   "0000820313",  # Amphenol Corporation
    "COST":  "0000909832",  # Costco Wholesale Corporation
}

# Pfade (relativ zum Script-Verzeichnis)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # 01_Skills/insider-intelligence → Claude Stuff
FAKTORTABELLE_PATH = PROJECT_ROOT / "00_Core" / "Faktortabelle.md"
CONFIG_YAML_PATH = PROJECT_ROOT / "01_Skills" / "dynastie-depot" / "config.yaml"

# BRK.B Exception: Entity-Level-Verkäufe durch "BERKSHIRE HATHAWAY INC" als
# 10% Owner sind strukturell bedingt (Aktienrueckkauf-Reporting, Portfolio-
# Rebalancing) und kein klassisches Insider-Selling. Nur Named Executives
# (Buffett, Abel, Jain etc.) werden fuer FLAG-Detection gezaehlt.
BRK_ENTITY_NAMES = {
    "BERKSHIRE HATHAWAY INC",
    "BERKSHIRE HATHAWAY",
    "BERKSHIRE HATHAWAY INC.",
}

# DEFCON Schwellen
FLAG_THRESHOLD_USD = 20_000_000  # $20M diskretionaer in 90 Tagen = FLAG
FLAG_WINDOW_DAYS = 90
SCORING_WINDOW_DAYS = 180  # 6 Monate fuer Net Buy/Sell

# Transaction Code Referenz (SEC Form 4)
TX_CODES = {
    "P": "Purchase (Open Market)",
    "S": "Sale (Open Market)",
    "M": "Exercise/Conversion",
    "A": "Grant/Award",
    "D": "Disposal to Issuer",
    "F": "Tax Withholding",
    "G": "Gift",
    "J": "Other Acquisition",
    "C": "Conversion of Derivative",
    "W": "Expiration/Cancellation",
}


# ---------------------------------------------------------------------------
# HTTP Layer
# ---------------------------------------------------------------------------

def _headers() -> dict:
    return {"User-Agent": USER_AGENT, "Accept": "application/json"}


def _get(url: str, params: dict = None) -> requests.Response:
    """Rate-limited GET (SEC Policy: max 10 req/s)."""
    time.sleep(0.12)  # ~8 req/s — sicher unter Limit
    resp = requests.get(url, headers=_headers(), params=params, timeout=30)
    resp.raise_for_status()
    return resp


# ---------------------------------------------------------------------------
# Form 4 Fetching
# ---------------------------------------------------------------------------

def fetch_form4_filings(cik: str, days: int = 180) -> list[dict]:
    """Hole Form-4-Filing-Metadaten von SEC EDGAR."""
    url = f"{DATA_URL}/submissions/CIK{cik}.json"
    resp = _get(url)
    data = resp.json()

    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    recent = data.get("filings", {}).get("recent", {})

    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])

    filings = []
    for i, form_type in enumerate(forms):
        if form_type not in ("4", "4/A"):
            continue
        filing_date = dates[i] if i < len(dates) else ""
        if filing_date < cutoff:
            continue

        filings.append({
            "filing_date": filing_date,
            "accession_number": accessions[i] if i < len(accessions) else "",
            "document": primary_docs[i] if i < len(primary_docs) else "",
        })

    return filings


# ---------------------------------------------------------------------------
# Form 4 XML Parsing
# ---------------------------------------------------------------------------

def _find(element, tag: str, ns: str = ""):
    """Finde Child-Element mit optionalem Namespace."""
    el = element.find(f"{ns}{tag}")
    if el is None and ns:
        el = element.find(tag)
    return el


def _safe_float(text, default: float = 0.0) -> float:
    """Sichere Float-Konvertierung."""
    try:
        return float(str(text).replace(",", ""))
    except (ValueError, TypeError, AttributeError):
        return default


def _get_text(element, tag: str, ns: str = "") -> str:
    """Extrahiere Text aus verschachteltem Element mit value-Child."""
    parent = _find(element, tag, ns)
    if parent is None:
        return ""
    # Manche Form-4-Felder haben ein <value> Child
    val = _find(parent, "value", ns)
    if val is not None and val.text:
        return val.text.strip()
    # Oder direkter Text
    if parent.text:
        return parent.text.strip()
    return ""


def parse_form4_xml(xml_text: str, filing_date: str) -> list[dict]:
    """Parse Form 4 XML — erweitert um 10b5-1-Erkennung und DEFCON-Klassifikation."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []

    # Namespace-Erkennung
    ns = ""
    for prefix in ["{http://www.sec.gov/cgi-bin/viewer?action=view&cik=}", ""]:
        if root.find(f"{prefix}reportingOwner") is not None:
            ns = prefix
            break

    # --- Insider-Informationen ---
    insider_name = ""
    insider_title = ""
    is_director = False
    is_officer = False
    is_ten_pct = False

    reporting = _find(root, "reportingOwner", ns)
    if reporting is not None:
        rid = _find(reporting, "reportingOwnerId", ns)
        if rid is not None:
            name_el = _find(rid, "rptOwnerName", ns)
            insider_name = name_el.text.strip() if name_el is not None and name_el.text else ""

        rel = _find(reporting, "reportingOwnerRelationship", ns)
        if rel is not None:
            title_el = _find(rel, "officerTitle", ns)
            if title_el is not None and title_el.text:
                insider_title = title_el.text.strip()

            dir_el = _find(rel, "isDirector", ns)
            is_director = dir_el is not None and dir_el.text in ("1", "true")
            off_el = _find(rel, "isOfficer", ns)
            is_officer = off_el is not None and off_el.text in ("1", "true")
            ten_el = _find(rel, "isTenPercentOwner", ns)
            is_ten_pct = ten_el is not None and ten_el.text in ("1", "true")

            if not insider_title:
                if is_officer:
                    insider_title = "Officer"
                elif is_director:
                    insider_title = "Director"
                elif is_ten_pct:
                    insider_title = "10% Owner"

    # --- Globale 10b5-1 Footnote-Pruefung ---
    has_10b51_footnote = False
    footnotes_el = _find(root, "footnotes", ns)
    if footnotes_el is not None:
        for fn in footnotes_el:
            fn_text = "".join(fn.itertext()).lower()
            if any(kw in fn_text for kw in ["10b5-1", "rule 10b5", "trading plan",
                                             "10b-5", "pre-arranged"]):
                has_10b51_footnote = True
                break

    # --- Transaktionen parsen ---
    trades = []

    for table_tag in ["nonDerivativeTable", "derivativeTable"]:
        tx_table = _find(root, table_tag, ns)
        if tx_table is None:
            continue

        is_derivative = "derivative" in table_tag.lower()

        for tx in tx_table:
            tag = tx.tag.replace(ns, "") if ns else tx.tag
            if "Transaction" not in tag:
                continue

            # Transaction Coding
            coding = _find(tx, "transactionCoding", ns)
            tx_code = ""
            is_10b51 = False

            if coding is not None:
                code_el = _find(coding, "transactionCode", ns)
                tx_code = code_el.text.strip() if code_el is not None and code_el.text else ""

                # 10b5-1 Indikator (SEC Amendment April 2023+)
                for child in coding:
                    child_tag = (child.tag.replace(ns, "") if ns else child.tag).lower()
                    if "10b5" in child_tag or "rule10b" in child_tag:
                        if child.text and child.text.strip() in ("1", "true", "yes"):
                            is_10b51 = True

            # Footnote-basierte 10b5-1 Erkennung (Fallback fuer Pre-2023 Filings)
            if not is_10b51 and has_10b51_footnote and tx_code in ("S", "D"):
                is_10b51 = True

            # Transaction Amounts
            amounts = _find(tx, "transactionAmounts", ns)
            shares = 0.0
            price = 0.0
            acq_disp = ""

            if amounts is not None:
                shares_el = _find(amounts, "transactionShares", ns)
                if shares_el is not None:
                    val = _find(shares_el, "value", ns)
                    if val is not None:
                        shares = _safe_float(val.text)

                price_el = _find(amounts, "transactionPricePerShare", ns)
                if price_el is not None:
                    val = _find(price_el, "value", ns)
                    if val is not None:
                        price = _safe_float(val.text)

                ad_el = _find(amounts, "transactionAcquiredDisposedCode", ns)
                if ad_el is not None:
                    val = _find(ad_el, "value", ns)
                    acq_disp = val.text.strip() if val is not None and val.text else ""

            # Transaction Date
            tx_date = _get_text(tx, "transactionDate", ns)

            # Security Title
            sec_title = _get_text(tx, "securityTitle", ns)

            # Post-Transaction Holdings
            post_holdings = 0.0
            post_el = _find(tx, "postTransactionAmounts", ns)
            if post_el is not None:
                shares_owned = _find(post_el, "sharesOwnedFollowingTransaction", ns)
                if shares_owned is not None:
                    val = _find(shares_owned, "value", ns)
                    if val is not None:
                        post_holdings = _safe_float(val.text)

            # Ownership Type (Direct/Indirect)
            ownership = "D"
            own_el = _find(tx, "ownershipNature", ns)
            if own_el is not None:
                doi = _find(own_el, "directOrIndirectOwnership", ns)
                if doi is not None:
                    val = _find(doi, "value", ns)
                    ownership = val.text.strip() if val is not None and val.text else "D"

            tx_value = round(shares * price, 2) if shares and price else 0.0

            # DEFCON-Klassifikation
            defcon_type = _classify_transaction(tx_code, is_10b51, price)

            trades.append({
                "filing_date": filing_date,
                "transaction_date": tx_date or filing_date,
                "insider_name": insider_name,
                "insider_title": insider_title,
                "is_director": is_director,
                "is_officer": is_officer,
                "is_ten_pct_owner": is_ten_pct,
                "transaction_code": tx_code,
                "transaction_type": TX_CODES.get(tx_code, f"Unknown ({tx_code})"),
                "is_10b51_plan": is_10b51,
                "is_derivative": is_derivative,
                "security": sec_title,
                "shares": shares,
                "price_per_share": price,
                "transaction_value": tx_value,
                "acquired_disposed": acq_disp,
                "post_holdings": post_holdings,
                "ownership_type": ownership,
                "defcon_classification": defcon_type,
            })

    return trades


def _classify_transaction(tx_code: str, is_10b51: bool, price: float) -> str:
    """Klassifiziere Transaktion fuer DEFCON-Relevanz.

    Mapping (aus sources.md / SKILL.md):
    - P = Open-Market-Kauf → positiv
    - S + 10b5-1 = Plan-Verkauf → neutral (kein FLAG)
    - S ohne 10b5-1 = Diskretionaerer Verkauf → potenziell FLAG
    - M + Preis $0 = RSU Vesting → neutral
    - M + S gleicher Tag = Cashless Exercise → neutral (wird spaeter gepaired)
    - A = Grant/Award → neutral
    - F = Tax Withholding → neutral
    """
    if tx_code == "P":
        return "OPEN_MARKET_BUY"

    if tx_code == "S":
        if is_10b51:
            return "PLAN_SALE_10B51"
        return "DISCRETIONARY_SALE"

    if tx_code == "M":
        if price == 0.0:
            return "RSU_VESTING"
        return "OPTION_EXERCISE"

    if tx_code == "D":
        if is_10b51:
            return "PLAN_DISPOSAL_10B51"
        return "DISCRETIONARY_DISPOSAL"

    if tx_code == "A":
        return "GRANT_AWARD"

    if tx_code == "F":
        return "TAX_WITHHOLDING"

    if tx_code == "G":
        return "GIFT"

    return f"OTHER_{tx_code}"


# ---------------------------------------------------------------------------
# Cashless Exercise Detection
# ---------------------------------------------------------------------------

def detect_cashless_exercises(trades: list[dict]) -> list[dict]:
    """Erkenne M+S same-day Cashless Exercises — KEIN FLAG-Signal.

    Regel (aus INSTRUKTIONEN.md):
    Code M + Code S am gleichen Tag + gleicher Insider = erzwungener Verkauf.
    Transaktionsvolumen trotzdem pruefen — bei >$20M und kein 10b5-1-Plan → FLAG.
    """
    exercises = [t for t in trades if t["transaction_code"] == "M"]
    sales = [t for t in trades if t["transaction_code"] == "S"
             and t["defcon_classification"] == "DISCRETIONARY_SALE"]

    for ex in exercises:
        for sale in sales:
            if (ex["transaction_date"] == sale["transaction_date"]
                    and ex["insider_name"] == sale["insider_name"]):
                sale["defcon_classification"] = "CASHLESS_EXERCISE_SALE"

    return trades


# ---------------------------------------------------------------------------
# DEFCON Metrics Computation
# ---------------------------------------------------------------------------

def compute_defcon_metrics(ticker: str, trades: list[dict]) -> dict:
    """Berechne DEFCON-Insider-Block-Metriken aus geparsten Transaktionen."""
    now = datetime.now()
    cutoff_90d = (now - timedelta(days=90)).strftime("%Y-%m-%d")
    cutoff_180d = (now - timedelta(days=180)).strftime("%Y-%m-%d")
    cutoff_365d = (now - timedelta(days=365)).strftime("%Y-%m-%d")

    trades_90d = [t for t in trades if t["transaction_date"] >= cutoff_90d]
    trades_180d = [t for t in trades if t["transaction_date"] >= cutoff_180d]
    trades_365d = [t for t in trades if t["transaction_date"] >= cutoff_365d]

    # Klassifikations-Sets
    buy_classes = {"OPEN_MARKET_BUY"}
    sell_discretionary = {"DISCRETIONARY_SALE", "DISCRETIONARY_DISPOSAL"}
    sell_plan = {"PLAN_SALE_10B51", "PLAN_DISPOSAL_10B51", "CASHLESS_EXERCISE_SALE"}
    sell_all = sell_discretionary | sell_plan

    # BRK.B Exception: Entity-Level-Verkaeufe herausfiltern
    is_brk = ticker.upper() in ("BRK.B", "BRK")
    if is_brk:
        def _is_entity_sale(t):
            return t["insider_name"].upper().strip() in BRK_ENTITY_NAMES
        trades_90d_flag = [t for t in trades_90d if not _is_entity_sale(t)]
        trades_180d_flag = [t for t in trades_180d if not _is_entity_sale(t)]
    else:
        trades_90d_flag = trades_90d
        trades_180d_flag = trades_180d

    def sum_value(txs, classifications):
        return sum(t["transaction_value"] for t in txs
                   if t["defcon_classification"] in classifications)

    def count_tx(txs, classifications):
        return len([t for t in txs if t["defcon_classification"] in classifications])

    # 90-Tage-Fenster (FLAG-Check) — BRK.B: nur Named Executives
    disc_sell_90d = sum_value(trades_90d_flag, sell_discretionary)
    plan_sell_90d = sum_value(trades_90d, sell_plan)
    buy_90d = sum_value(trades_90d, buy_classes)

    # 180-Tage-Fenster (Scoring) — BRK.B: nur Named Executives fuer Sells
    disc_sell_180d = sum_value(trades_180d_flag, sell_discretionary)
    plan_sell_180d = sum_value(trades_180d_flag, sell_plan)
    buy_180d = sum_value(trades_180d, buy_classes)  # Kaeufe: alle zaehlen
    net_180d = buy_180d - disc_sell_180d - plan_sell_180d

    # 12-Monate (Kontext)
    buy_12m = sum_value(trades_365d, buy_classes)
    sell_12m = sum_value(trades_365d, sell_all)

    # FLAG Detection — BRK.B: nur Named Executives
    flag_active = disc_sell_90d > FLAG_THRESHOLD_USD
    flag_transactions = [
        t for t in trades_90d_flag
        if t["defcon_classification"] in sell_discretionary
        and t["transaction_value"] > 1_000_000
    ]

    # Unique Insiders
    buyers_180d = sorted(set(
        t["insider_name"] for t in trades_180d
        if t["defcon_classification"] in buy_classes
    ))
    sellers_disc_180d = sorted(set(
        t["insider_name"] for t in trades_180d_flag
        if t["defcon_classification"] in sell_discretionary
    ))

    # Top Insider Holdings (aus letzter Transaktion)
    latest_holdings = {}
    for t in sorted(trades, key=lambda x: x["transaction_date"]):
        if t["ownership_type"] == "D" and t["post_holdings"] > 0:
            latest_holdings[t["insider_name"]] = {
                "shares": t["post_holdings"],
                "title": t["insider_title"],
                "as_of": t["transaction_date"],
            }

    # DEFCON Scoring (max 10 Punkte)
    score_net_buy = _score_net_buy(net_180d, buy_180d)       # max 4
    score_no_flag = _score_no_flag(disc_sell_90d)             # max 3
    # score_ownership = max 3 — benoetigt Market Cap, extern ergaenzen

    return {
        "ticker": ticker,
        "scan_date": now.strftime("%Y-%m-%d"),
        "cik": SATELLITES_CIK.get(ticker, ""),

        "flag_active": flag_active,
        "flag_reason": (
            f"Diskretionaere Verkaeufe ${disc_sell_90d:,.0f} "
            f"> ${FLAG_THRESHOLD_USD:,.0f} in 90 Tagen"
            if flag_active
            else "Kein FLAG"
        ),
        "flag_transactions": flag_transactions,

        "window_90d": {
            "discretionary_sell_value": disc_sell_90d,
            "plan_sell_value": plan_sell_90d,
            "buy_value": buy_90d,
            "net": buy_90d - disc_sell_90d,
        },
        "window_180d": {
            "discretionary_sell_value": disc_sell_180d,
            "plan_sell_value": plan_sell_180d,
            "buy_value": buy_180d,
            "net": net_180d,
            "unique_buyers": buyers_180d,
            "unique_discretionary_sellers": sellers_disc_180d,
        },
        "window_12m": {
            "total_buy_value": buy_12m,
            "total_sell_value": sell_12m,
            "net": buy_12m - sell_12m,
        },

        "transaction_counts": {
            "total_parsed": len(trades),
            "open_market_buys": count_tx(trades, buy_classes),
            "discretionary_sales": count_tx(trades, sell_discretionary),
            "plan_sales_10b51": count_tx(trades, sell_plan),
            "exercises_vestings": count_tx(trades, {"RSU_VESTING", "OPTION_EXERCISE"}),
            "grants_awards": count_tx(trades, {"GRANT_AWARD"}),
            "tax_withholding": count_tx(trades, {"TAX_WITHHOLDING"}),
            "gifts": count_tx(trades, {"GIFT"}),
        },

        "defcon_scoring": {
            "net_buy_score": score_net_buy,
            "ownership_score": "—",
            "no_flag_score": score_no_flag,
            "subtotal": score_net_buy + score_no_flag,
            "max_without_ownership": 7,
            "note": "Ownership-Score (max 3) benoetigt Market Cap + percent_insiders"
        },

        "top_insider_holdings": dict(
            sorted(latest_holdings.items(),
                   key=lambda x: x[1]["shares"], reverse=True)[:5]
        ),

        "all_transactions": trades,
    }


def _score_net_buy(net_value: float, buy_value: float) -> int:
    """Net Buy letzte 6 Monate (max 4 Punkte).

    Skala (aus SKILL.md Insider-Block):
    4 = starke Net Buys (>$5M)
    3 = moderate Net Buys (>$1M)
    2 = leichte Net Buys (>$0)
    1 = neutral (keine Aktivitaet) oder leichte Netto-Verkaeufe
    0 = massive Netto-Verkaeufe (>$50M)
    """
    if buy_value > 0 and net_value > 5_000_000:
        return 4
    if buy_value > 0 and net_value > 1_000_000:
        return 3
    if buy_value > 0 and net_value > 0:
        return 2
    if net_value == 0 and buy_value == 0:
        return 1
    if net_value < -50_000_000:
        return 0
    return 1


def _score_no_flag(disc_sell_90d: float) -> int:
    """Kein diskretionaeres Selling >$20M (max 3 Punkte).

    Skala:
    3 = clean (diskr. Verkaeufe <$5M)
    2 = moderate Aktivitaet ($5M-$10M)
    1 = erhoehtes Volumen ($10M-$20M)
    0 = FLAG aktiv (>$20M)
    """
    if disc_sell_90d > FLAG_THRESHOLD_USD:
        return 0
    if disc_sell_90d > 10_000_000:
        return 1
    if disc_sell_90d > 5_000_000:
        return 2
    return 3


# ---------------------------------------------------------------------------
# Scan & Output
# ---------------------------------------------------------------------------

def scan_satellite(ticker: str, days: int = 180) -> dict:
    """Vollstaendiger Scan eines US-Satelliten."""
    cik = SATELLITES_CIK.get(ticker.upper())
    if not cik:
        return {"ticker": ticker, "error": f"Kein CIK hinterlegt fuer {ticker}"}

    print(f"  [{ticker}] Lade Form-4-Filings (CIK: {cik})...", file=sys.stderr)

    try:
        filings = fetch_form4_filings(cik, days=days)
    except Exception as e:
        return {"ticker": ticker, "error": f"EDGAR API Fehler: {e}"}

    print(f"  [{ticker}] {len(filings)} Form-4-Filings gefunden, parse XML...",
          file=sys.stderr)

    all_trades = []
    errors = 0
    for filing in filings[:40]:  # Max 40 Filings
        accession = filing["accession_number"].replace("-", "")
        doc = filing["document"]
        # Strip XSL prefix (z.B. xslF345X05/ownership.xml → ownership.xml)
        if "/" in doc:
            doc = doc.split("/", 1)[1]

        xml_url = (
            f"{SEC_WWW}/Archives/edgar/data/"
            f"{cik.lstrip('0')}/{accession}/{doc}"
        )

        try:
            resp = _get(xml_url)
            trades = parse_form4_xml(resp.text, filing["filing_date"])
            all_trades.extend(trades)
        except Exception:
            errors += 1
            continue

    if errors:
        print(f"  [{ticker}] {errors} Filings konnten nicht geparst werden",
              file=sys.stderr)

    # Cashless Exercises erkennen
    all_trades = detect_cashless_exercises(all_trades)

    # DEFCON Metriken berechnen
    return compute_defcon_metrics(ticker, all_trades)


def format_defcon_output(result: dict) -> str:
    """Formatiere als DEFCON-ready Insider-Block (Markdown)."""
    if "error" in result:
        return f"### {result['ticker']} — FEHLER\n{result['error']}\n"

    ticker = result["ticker"]
    flag = "FLAG AKTIV" if result["flag_active"] else "Kein FLAG"
    flag_icon = "🔴" if result["flag_active"] else "🟢"
    scoring = result["defcon_scoring"]
    w90 = result["window_90d"]
    w180 = result["window_180d"]
    w12m = result["window_12m"]
    counts = result["transaction_counts"]

    lines = [
        f"### 🔴 Insider: {scoring['subtotal']}/7* | {ticker}",
        f"**Scan:** {result['scan_date']} | **CIK:** {result['cik']}",
        f"**FLAG:** {flag_icon} {flag}",
        "",
    ]

    if result["flag_active"]:
        lines.append(f"> **{result['flag_reason']}**")
        lines.append("> Sparrate komplett gestoppt (0 EUR) bis FLAG aufgehoben.")
        lines.append("")

    # Zeitfenster-Tabelle
    lines.extend([
        "| Metrik | 90 Tage | 180 Tage | 12 Monate |",
        "|--------|---------|----------|-----------|",
        f"| Diskr. Verkaeufe | ${w90['discretionary_sell_value']:,.0f} "
        f"| ${w180['discretionary_sell_value']:,.0f} | — |",
        f"| 10b5-1 Plan-Verkaeufe | ${w90['plan_sell_value']:,.0f} "
        f"| ${w180['plan_sell_value']:,.0f} | — |",
        f"| Open-Market-Kaeufe | ${w90['buy_value']:,.0f} "
        f"| ${w180['buy_value']:,.0f} | — |",
        f"| **Netto** | **${w90['net']:+,.0f}** "
        f"| **${w180['net']:+,.0f}** | **${w12m['net']:+,.0f}** |",
        "",
    ])

    # Transaktions-Zusammenfassung
    lines.extend([
        f"**Transaktionen gesamt:** {counts['total_parsed']} | "
        f"Kaeufe: {counts['open_market_buys']} | "
        f"Diskr. Verkaeufe: {counts['discretionary_sales']} | "
        f"Plan-Verkaeufe: {counts['plan_sales_10b51']} | "
        f"Exercises: {counts['exercises_vestings']}",
        "",
    ])

    # Unique Insiders
    if w180["unique_buyers"]:
        lines.append(f"**Kaeufer (180d):** {', '.join(w180['unique_buyers'])}")
    if w180["unique_discretionary_sellers"]:
        lines.append(
            f"**Diskr. Verkaeufer (180d):** "
            f"{', '.join(w180['unique_discretionary_sellers'])}"
        )
    lines.append("")

    # Scoring-Tabelle
    lines.extend([
        "| Scoring-Komponente | Punkte | Basis |",
        "|-------------------|--------|-------|",
        f"| Net Buy (6M) | {scoring['net_buy_score']}/4 "
        f"| Netto ${w180['net']:+,.0f} |",
        f"| Ownership (>1%) | {scoring['ownership_score']}/3 "
        f"| _(extern ergaenzen)_ |",
        f"| Kein diskr. Selling >$20M | {scoring['no_flag_score']}/3 "
        f"| Diskr. 90d: ${w90['discretionary_sell_value']:,.0f} |",
        f"| **Subtotal** | **{scoring['subtotal']}/7*** | |",
        "",
        "*Ownership-Score via Shibui `share_stats.percent_insiders` "
        "oder GuruFocus ergaenzen.*",
    ])

    # FLAG-Transaktionen Detail
    if result["flag_transactions"]:
        lines.extend([
            "",
            "**FLAG-relevante Transaktionen (>$1M diskretionaer, 90d):**",
            "",
            "| Datum | Insider | Titel | Wert | 10b5-1? |",
            "|-------|---------|-------|------|---------|",
        ])
        for t in sorted(result["flag_transactions"],
                        key=lambda x: x["transaction_value"], reverse=True):
            plan = "Ja" if t["is_10b51_plan"] else "**NEIN**"
            lines.append(
                f"| {t['transaction_date']} | {t['insider_name']} | "
                f"{t['insider_title']} | ${t['transaction_value']:,.0f} | {plan} |"
            )

    # Top Holdings
    if result["top_insider_holdings"]:
        lines.extend(["", "**Top Insider Holdings (Direct):**", ""])
        for name, info in list(result["top_insider_holdings"].items())[:5]:
            lines.append(
                f"- {name} ({info['title']}): "
                f"{info['shares']:,.0f} Aktien (Stand: {info['as_of']})"
            )

    return "\n".join(lines)


def format_flag_summary(results: list[dict]) -> str:
    """Kompakte FLAG-Uebersicht aller Satelliten."""
    now_str = datetime.now().strftime("%d.%m.%Y")
    lines = [
        "# FLAG-Check — Dynastie-Depot US-Satelliten",
        "",
        f"**Datum:** {now_str} | **Fenster:** 90 Tage",
        "",
        "| Ticker | FLAG | Diskr. Verkaeufe (90d) | Detail |",
        "|--------|------|------------------------|--------|",
    ]

    for r in results:
        if "error" in r:
            lines.append(f"| {r['ticker']} | -- | FEHLER | {r['error']} |")
            continue

        flag = "🔴" if r["flag_active"] else "🟢"
        disc = r["window_90d"]["discretionary_sell_value"]
        reason = r["flag_reason"]
        lines.append(f"| {r['ticker']} | {flag} | ${disc:,.0f} | {reason} |")

    # Zusammenfassung
    flags = [r for r in results if r.get("flag_active")]
    clean = [r for r in results if not r.get("flag_active") and "error" not in r]
    errors = [r for r in results if "error" in r]

    lines.extend([
        "",
        f"**Ergebnis:** {len(clean)} clean, {len(flags)} FLAG(s), {len(errors)} Fehler",
    ])

    if flags:
        lines.append("")
        lines.append("**Aktive FLAGs:**")
        for r in flags:
            lines.append(f"- **{r['ticker']}**: {r['flag_reason']}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Faktortabelle Integration
# ---------------------------------------------------------------------------

def update_faktortabelle(results: list[dict], path: Path = None) -> None:
    """Aktualisiert FLAG-Status in Faktortabelle.md via Kommentar-Anker.

    Sucht <!-- DATA:TICKER --> Anker und aktualisiert die FLAG-Spalte
    in der nachfolgenden Tabellenzeile. Schreibt NIE config.yaml.
    """
    fpath = path or FAKTORTABELLE_PATH
    if not fpath.exists():
        print(f"  WARNUNG: {fpath} nicht gefunden — uebersprungen.", file=sys.stderr)
        return

    content = fpath.read_text(encoding="utf-8")
    now_str = datetime.now().strftime("%Y-%m-%d")
    changes = []

    for r in results:
        if "error" in r:
            continue
        ticker = r["ticker"]
        anchor = f"<!-- DATA:{ticker} -->"
        if anchor not in content:
            continue

        # Finde die Tabellenzeile nach dem Anker
        anchor_pos = content.index(anchor)
        rest = content[anchor_pos + len(anchor):]
        # Naechste Zeile ist die Tabellenzeile
        line_start = rest.index("\n") + 1
        line_end = rest.index("\n", line_start)
        old_line = rest[line_start:line_end]

        # Parse die bestehende Zeile in Spalten
        cols = [c.strip() for c in old_line.split("|")]
        # cols[0]="" (vor erstem |), cols[1]=Position, ..., cols[9]=FLAG, ...
        # Tabelle: Position|FCF|ROIC|GM|Debt|Moat|Score|DEFCON|FLAG|Score-Datum|Update
        if len(cols) >= 10:
            flag_idx = 9  # FLAG ist Spalte 9 (0-indexed)
            if r["flag_active"]:
                flag_text = f"🔴 {r['flag_reason'][:40]}"
            else:
                flag_text = "—"
            cols[flag_idx] = f" {flag_text} "

            new_line = "|".join(cols)
            content = content.replace(old_line, new_line)

            old_flag = "FLAG" if r["flag_active"] else "clean"
            changes.append(f"  {ticker}: {old_flag}")
            print(
                f"  ⚠️ config.yaml sync: {ticker} FLAG "
                f"{'true' if r['flag_active'] else 'false'}",
                file=sys.stderr,
            )

    # Aktualisiere Stand-Datum
    content = re.sub(
        r"\*\*Stand:\*\* \d{2}\.\d{2}\.\d{4}",
        f"**Stand:** {datetime.now().strftime('%d.%m.%Y')}",
        content,
    )

    # Fuege Insider-Check Timestamp ein (nach END_TABLE)
    check_line = f"\n**Insider-Check:** {now_str}\n"
    if "**Insider-Check:**" in content:
        content = re.sub(r"\*\*Insider-Check:\*\* \S+", f"**Insider-Check:** {now_str}", content)
    elif "<!-- END_TABLE -->" in content:
        content = content.replace("<!-- END_TABLE -->", f"<!-- END_TABLE -->{check_line}")

    fpath.write_text(content, encoding="utf-8")

    if changes:
        print(f"\n  Faktortabelle.md aktualisiert ({len(changes)} Ticker):", file=sys.stderr)
        for c in changes:
            print(c, file=sys.stderr)
    else:
        print("  Faktortabelle.md: keine Aenderungen.", file=sys.stderr)


def _parse_faktortabelle_flags(path: Path = None) -> dict[str, bool]:
    """Extrahiert FLAG-Status pro Ticker aus Faktortabelle.md."""
    fpath = path or FAKTORTABELLE_PATH
    if not fpath.exists():
        return {}

    content = fpath.read_text(encoding="utf-8")
    flags = {}
    for ticker in SATELLITES_CIK:
        anchor = f"<!-- DATA:{ticker} -->"
        if anchor not in content:
            continue
        anchor_pos = content.index(anchor)
        rest = content[anchor_pos:]
        lines = rest.split("\n", 3)
        if len(lines) >= 2:
            line = lines[1]  # Tabellenzeile nach Anker
            # FLAG-Spalte enthaelt "🔴" wenn aktiv
            flags[ticker] = "🔴" in line
    return flags


def _parse_config_yaml_flags(path: Path = None) -> dict[str, dict]:
    """Extrahiert FLAG-Status + FLAG-Typ pro Ticker aus config.yaml.

    Returns dict[ticker] = {"active": bool, "type": "insider"|"capex"|"other"|None, "grund": str}
    """
    cpath = path or CONFIG_YAML_PATH
    if not cpath.exists():
        print(f"  WARNUNG: {cpath} nicht gefunden.", file=sys.stderr)
        return {}

    if not HAS_YAML:
        print(
            "  FEHLER: pyyaml nicht installiert. Bitte: pip install pyyaml",
            file=sys.stderr,
        )
        return {}

    with open(cpath, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    flags = {}
    for sat in config.get("satelliten", []):
        ticker = sat.get("ticker", "")
        if ticker not in SATELLITES_CIK:
            continue
        is_flag = bool(sat.get("flag", False))
        grund = str(sat.get("flag_grund", "") or "")

        # FLAG-Typ erkennen aus flag_grund
        flag_type = None
        if is_flag:
            grund_lower = grund.lower()
            if any(kw in grund_lower for kw in ["insider", "selling", "10b5", "diskretion"]):
                flag_type = "insider"
            elif any(kw in grund_lower for kw in ["capex", "ocf", "investition"]):
                flag_type = "capex"
            else:
                flag_type = "other"

        flags[ticker] = {"active": is_flag, "type": flag_type, "grund": grund}
    return flags


def factor_sync() -> str:
    """3-Wege-Vergleich: config.yaml vs. Faktortabelle vs. Live-Scan."""
    now_str = datetime.now().strftime("%d.%m.%Y")

    # 1. config.yaml
    config_flags = _parse_config_yaml_flags()

    # 2. Faktortabelle.md
    tabelle_flags = _parse_faktortabelle_flags()

    # 3. Live-Scan (flag-check)
    print("  Live-Scan laeuft...", file=sys.stderr)
    live_flags = {}
    for ticker in SATELLITES_CIK:
        result = scan_satellite(ticker, days=90)
        if "error" not in result:
            live_flags[ticker] = result["flag_active"]

    # Vergleich
    lines = [
        f"# 3-Wege FLAG-Vergleich ({now_str})",
        "",
        "| Ticker | config.yaml | Faktortabelle | Live-Scan | Status |",
        "|--------|------------|---------------|-----------|--------|",
    ]

    drift_count = 0
    for ticker in SATELLITES_CIK:
        cfg_data = config_flags.get(ticker, {})
        tab = tabelle_flags.get(ticker)
        live = live_flags.get(ticker)

        # config.yaml: FLAG-Typ anzeigen
        cfg_active = cfg_data.get("active", False) if cfg_data else False
        cfg_type = cfg_data.get("type") if cfg_data else None

        def fmt_cfg():
            if not cfg_data:
                return "—"
            if not cfg_active:
                return "clean"
            if cfg_type == "capex":
                return "FLAG (CapEx)"
            if cfg_type == "insider":
                return "FLAG (Insider)"
            return "FLAG"

        def fmt(v):
            if v is None:
                return "—"
            return "FLAG" if v else "clean"

        # Insider-Vergleich: CapEx-FLAGs werden NICHT als Drift gewertet
        # Nur Insider-FLAGs in config.yaml werden mit Live-Scan verglichen
        # Wenn config sagt CapEx-FLAG → Faktortabelle-FLAG ist auch CapEx-origin
        cfg_insider_flag = cfg_active and cfg_type == "insider"
        tab_insider = tab if not (cfg_active and cfg_type == "capex") else False

        insider_values = [v for v in [cfg_insider_flag, tab_insider, live] if v is not None]
        if not insider_values:
            status = "⚠️ KEINE DATEN"
            drift_count += 1
        elif len(set(insider_values)) == 1:
            status = "✅ Sync"
        else:
            status = "⚠️ DRIFT"
            drift_count += 1

        lines.append(
            f"| {ticker} | {fmt_cfg()} | {fmt(tab)} | {fmt(live)} | {status} |"
        )

    lines.extend([
        "",
        f"**Ergebnis:** {len(SATELLITES_CIK) - drift_count} sync, {drift_count} drift",
    ])

    if drift_count > 0:
        lines.append("")
        lines.append("⚠️ Bei Drift: config.yaml manuell aktualisieren.")

    if not HAS_YAML:
        lines.extend([
            "",
            "⚠️ pyyaml nicht installiert — config.yaml-Spalte leer.",
            "   Install: pip install pyyaml",
        ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Dynastie-Depot Insider Intelligence Module v1.0"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # scan
    p_scan = sub.add_parser(
        "scan",
        help="Scanne US-Satelliten (alle oder bestimmte Ticker)"
    )
    p_scan.add_argument(
        "tickers", nargs="*",
        help="Ticker-Liste (leer = alle 8 US-Satelliten)"
    )
    p_scan.add_argument(
        "--days", type=int, default=180,
        help="Lookback-Zeitraum in Tagen (default: 180)"
    )
    p_scan.add_argument(
        "--json", action="store_true",
        help="JSON-Output statt Markdown"
    )
    p_scan.add_argument(
        "--update-faktortabelle", action="store_true",
        help="Aktualisiert Faktortabelle.md nach Scan"
    )

    # flag-check
    p_flag = sub.add_parser(
        "flag-check",
        help="Schneller FLAG-Status aller 8 US-Satelliten"
    )
    p_flag.add_argument(
        "--days", type=int, default=90,
        help="Lookback-Zeitraum in Tagen (default: 90)"
    )
    p_flag.add_argument(
        "--update-faktortabelle", action="store_true",
        help="Aktualisiert Faktortabelle.md nach FLAG-Check"
    )

    # factor-sync
    sub.add_parser(
        "factor-sync",
        help="3-Wege-Vergleich: config.yaml vs. Faktortabelle vs. Live-Scan"
    )

    # detail
    p_det = sub.add_parser(
        "detail",
        help="Vollstaendiger Detail-Report eines Tickers mit allen Transaktionen"
    )
    p_det.add_argument("ticker", help="Ticker (z.B. AVGO)")
    p_det.add_argument(
        "--days", type=int, default=365,
        help="Lookback-Zeitraum in Tagen (default: 365)"
    )

    args = parser.parse_args()

    if args.command == "scan":
        tickers = [t.upper() for t in args.tickers] if args.tickers else list(SATELLITES_CIK.keys())

        results = []
        for ticker in tickers:
            result = scan_satellite(ticker, days=args.days)
            results.append(result)

        if args.json:
            output = []
            for r in results:
                r_copy = {k: v for k, v in r.items() if k != "all_transactions"}
                output.append(r_copy)
            print(json.dumps(output, indent=2, default=str))
        else:
            for result in results:
                print(format_defcon_output(result))
                print("\n---\n")

        if getattr(args, "update_faktortabelle", False):
            update_faktortabelle(results)

    elif args.command == "flag-check":
        results = []
        for ticker in SATELLITES_CIK:
            result = scan_satellite(ticker, days=args.days)
            results.append(result)

        print(format_flag_summary(results))

        if getattr(args, "update_faktortabelle", False):
            update_faktortabelle(results)

    elif args.command == "factor-sync":
        print(factor_sync())

    elif args.command == "detail":
        ticker = args.ticker.upper()
        result = scan_satellite(ticker, days=args.days)

        if "error" in result:
            print(f"FEHLER: {result['error']}", file=sys.stderr)
            sys.exit(1)

        print(format_defcon_output(result))
        print("\n---\n")
        print("## Alle Transaktionen\n")
        print("| Datum | Insider | Code | Shares | Preis | Wert | 10b5-1 | Klasse |")
        print("|-------|---------|------|--------|-------|------|--------|--------|")

        for t in sorted(result["all_transactions"],
                        key=lambda x: x["transaction_date"], reverse=True):
            plan = "Ja" if t["is_10b51_plan"] else "—"
            name = t["insider_name"][:25]
            print(
                f"| {t['transaction_date']} | {name} | "
                f"{t['transaction_code']} | {t['shares']:,.0f} | "
                f"${t['price_per_share']:.2f} | ${t['transaction_value']:,.0f} | "
                f"{plan} | {t['defcon_classification']} |"
            )


if __name__ == "__main__":
    # Windows-Konsole: UTF-8 Output erzwingen (fuer Emojis)
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    main()
