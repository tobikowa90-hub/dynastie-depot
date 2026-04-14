#!/usr/bin/env python3
"""
Quick-Screener Batch-Script fuer das Dynastie-Depot.
Liest eine CSV mit Finanzkennzahlen und wendet die Screening-Filter an.

Verwendung durch den Skill:
  python scripts/screen.py --csv input.csv [--exceptions BRK.B,MKL,FFH.TO]
  python scripts/screen.py --yaml config.yaml  (extrahiert Ticker-Liste)
  python scripts/screen.py --yaml config.yaml --generate-template output.csv
  python scripts/screen.py --csv input.csv --validate  (Plausibilitaetschecks)

Output: Ampel-Tabelle als Markdown oder JSON.
"""

import argparse
import csv
import json
import sys
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# --- Schwellenwerte (synchron mit thresholds.md) ---

THRESHOLDS = {
    "p_fcf": {"green": 35, "yellow": 45},
    "roic": {"green": 15, "yellow": 12},
    "gross_margin": {"green": 40, "yellow": 35},
    "rev_cagr": {"green": 8, "yellow": 5},
}

# Exception-Metriken fuer Versicherungen/Holdings (BRK.B, MKL, FFH.TO)
# HINWEIS: COST (Discount-Retail) hat ebenfalls Sonderregeln (P/FCF ≤55, GM-Filter
# deaktiviert) — diese sind im Batch-Script NICHT implementiert. COST muss im
# CSV-Modus manuell mit P/FCF-Wert und CAGR eingegeben und das Ergebnis
# manuell interpretiert werden (Standard-Ampel wird P/FCF ROT anzeigen —
# das ist falsch fuer COST). Beim Einzel-Screening per AI-Workflow gilt:
# Exception-Regeln aus thresholds.md Abschnitt "Discount-Retail" anwenden.
EXCEPTION_THRESHOLDS = {
    "price_book": {"green": 1.3, "yellow": 1.5},
    "combined_ratio": {"green": 95, "yellow": 100},
    "float_growth": {"green": 8, "yellow": 5},
}


@dataclass
class ScreenResult:
    ticker: str
    p_fcf: Optional[float] = None
    roic: Optional[float] = None
    gross_margin: Optional[float] = None
    rev_cagr: Optional[float] = None
    morningstar_moat: Optional[str] = None  # "Wide", "Narrow", "None"
    # Exception fields
    price_book: Optional[float] = None
    combined_ratio: Optional[float] = None
    float_growth: Optional[float] = None
    is_exception: bool = False
    # Results
    ampel_p_fcf: str = ""
    ampel_roic: str = ""
    ampel_moat: str = ""
    ampel_gesamt: str = ""
    notes: list = field(default_factory=list)


def rate_value(value, green_threshold, yellow_threshold, higher_is_better=False):
    """Return GRUEN/GELB/ROT based on thresholds."""
    if value is None:
        return "ROT"
    if higher_is_better:
        if value >= green_threshold:
            return "GRUEN"
        elif value >= yellow_threshold:
            return "GELB"
        else:
            return "ROT"
    else:  # lower is better
        if value <= green_threshold:
            return "GRUEN"
        elif value <= yellow_threshold:
            return "GELB"
        else:
            return "ROT"


def screen_ticker(result: ScreenResult) -> ScreenResult:
    """Apply screening filters to a single ticker."""

    # Filter 1: P/FCF (or Price/Book for exceptions)
    if result.is_exception:
        if result.price_book is not None:
            result.ampel_p_fcf = rate_value(
                result.price_book,
                EXCEPTION_THRESHOLDS["price_book"]["green"],
                EXCEPTION_THRESHOLDS["price_book"]["yellow"],
                higher_is_better=False,
            )
            result.notes.append(f"P/B={result.price_book:.2f} (Exception-Modus)")
        else:
            result.ampel_p_fcf = "GELB"
            result.notes.append("P/B nicht verfuegbar — Gelb als Default")
    else:
        if result.p_fcf is not None and result.p_fcf > 0:
            result.ampel_p_fcf = rate_value(
                result.p_fcf,
                THRESHOLDS["p_fcf"]["green"],
                THRESHOLDS["p_fcf"]["yellow"],
            )
        else:
            result.ampel_p_fcf = "ROT"
            if result.p_fcf is not None and result.p_fcf <= 0:
                result.notes.append("Negativer FCF")

    # Filter 2: ROIC (or Combined Ratio / Float Growth for exceptions)
    if result.is_exception:
        cr_ok = result.combined_ratio is not None and result.combined_ratio < 100
        fg_ok = result.float_growth is not None and result.float_growth >= 5
        if cr_ok or fg_ok:
            # Use the better of the two
            if result.combined_ratio is not None:
                result.ampel_roic = rate_value(
                    result.combined_ratio,
                    EXCEPTION_THRESHOLDS["combined_ratio"]["green"],
                    EXCEPTION_THRESHOLDS["combined_ratio"]["yellow"],
                    higher_is_better=False,
                )
            else:
                result.ampel_roic = rate_value(
                    result.float_growth,
                    EXCEPTION_THRESHOLDS["float_growth"]["green"],
                    EXCEPTION_THRESHOLDS["float_growth"]["yellow"],
                    higher_is_better=True,
                )
        elif result.roic is not None:
            # Fallback to standard ROIC if exception metrics unavailable
            result.ampel_roic = rate_value(
                result.roic,
                THRESHOLDS["roic"]["green"],
                THRESHOLDS["roic"]["yellow"],
                higher_is_better=True,
            )
            result.notes.append("ROIC als Fallback (Exception-Metriken fehlen)")
        else:
            result.ampel_roic = "GELB"
            result.notes.append("Keine ROIC/CR/FG-Daten — Gelb als Default")
    else:
        result.ampel_roic = rate_value(
            result.roic,
            THRESHOLDS["roic"]["green"],
            THRESHOLDS["roic"]["yellow"],
            higher_is_better=True,
        )

    # Filter 3: Moat-Proxy
    if result.morningstar_moat:
        moat = result.morningstar_moat.lower().strip()
        if moat == "wide":
            result.ampel_moat = "GRUEN"
        elif moat == "narrow":
            result.ampel_moat = "GELB"
        else:
            result.ampel_moat = "ROT"
    else:
        gm_ampel = rate_value(
            result.gross_margin,
            THRESHOLDS["gross_margin"]["green"],
            THRESHOLDS["gross_margin"]["yellow"],
            higher_is_better=True,
        )
        cagr_ampel = rate_value(
            result.rev_cagr,
            THRESHOLDS["rev_cagr"]["green"],
            THRESHOLDS["rev_cagr"]["yellow"],
            higher_is_better=True,
        )

        if gm_ampel == "GRUEN" and cagr_ampel == "GRUEN":
            result.ampel_moat = "GRUEN"
        elif gm_ampel == "ROT" or cagr_ampel == "ROT":
            result.ampel_moat = "ROT"
        else:
            result.ampel_moat = "GELB"

    # Gesamtampel
    ampeln = [result.ampel_p_fcf, result.ampel_roic, result.ampel_moat]
    if "ROT" in ampeln:
        result.ampel_gesamt = "ROT"
    elif ampeln.count("GELB") >= 2:
        result.ampel_gesamt = "GELB"
    elif ampeln.count("GELB") == 1:
        result.ampel_gesamt = "GRUEN"
    else:
        result.ampel_gesamt = "GRUEN"

    return result


def parse_csv(filepath: str, exceptions: list) -> list:
    """Parse CSV file and return list of ScreenResults."""
    results = []
    # Flexible column name mapping
    col_map = {
        "ticker": ["ticker", "symbol", "stock"],
        "p_fcf": ["p/fcf", "p_fcf", "price_to_fcf", "price-to-free-cash-flow", "pfcf"],
        "roic": ["roic", "return_on_invested_capital", "return on invested capital"],
        "gross_margin": ["gross_margin", "gross margin", "bruttomarge", "gm", "gm%"],
        "rev_cagr": ["rev_cagr", "revenue_cagr", "revenue cagr 5y", "umsatzwachstum", "cagr"],
        "morningstar_moat": ["moat", "morningstar_moat", "morningstar moat", "moat_rating"],
        "price_book": ["p/b", "p_b", "price_book", "price/book", "price to book"],
        "combined_ratio": ["combined_ratio", "combined ratio", "cr"],
        "float_growth": ["float_growth", "float growth", "fg"],
    }

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = {h.lower().strip(): h for h in reader.fieldnames}

        def find_col(field_name):
            for alias in col_map.get(field_name, []):
                for h_lower, h_orig in headers.items():
                    if alias in h_lower:
                        return h_orig
            return None

        ticker_col = find_col("ticker")
        if not ticker_col:
            print("ERROR: Keine Ticker/Symbol-Spalte gefunden.", file=sys.stderr)
            sys.exit(1)

        for row in reader:
            ticker = row[ticker_col].strip().upper()
            if not ticker:
                continue

            r = ScreenResult(ticker=ticker)
            r.is_exception = ticker in [e.upper() for e in exceptions]

            def safe_float(field_name):
                col = find_col(field_name)
                if col and row.get(col):
                    val = row[col].strip().replace("%", "").replace(",", ".")
                    try:
                        return float(val)
                    except ValueError:
                        return None
                return None

            r.p_fcf = safe_float("p_fcf")
            r.roic = safe_float("roic")
            r.gross_margin = safe_float("gross_margin")
            r.rev_cagr = safe_float("rev_cagr")
            r.price_book = safe_float("price_book")
            r.combined_ratio = safe_float("combined_ratio")
            r.float_growth = safe_float("float_growth")

            moat_col = find_col("morningstar_moat")
            if moat_col and row.get(moat_col):
                r.morningstar_moat = row[moat_col].strip()

            results.append(screen_ticker(r))

    return results


def extract_tickers_from_yaml(yaml_path: str) -> list:
    """Extract watchlist + keine_zuteilung + ersatz tickers from config.yaml."""
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)

    tickers = set()

    for item in config.get("watchlist", []):
        tickers.add(item.get("ticker", ""))

    for t in config.get("keine_zuteilung", []):
        # keine_zuteilung entries are dicts {"ticker": ..., "grund": ...}, not plain strings
        if isinstance(t, dict):
            tickers.add(t.get("ticker", ""))
        else:
            tickers.add(str(t))

    for sat in config.get("satelliten", []):
        ersatz = sat.get("ersatz", "")
        if ersatz:
            for e in str(ersatz).replace("/", ",").split(","):
                e = e.strip()
                if e:
                    tickers.add(e)

    tickers.discard("")
    return sorted(tickers)


def generate_template(yaml_path: str, output_path: str, exceptions: list):
    """Generate a CSV template pre-filled with tickers from config.yaml."""
    tickers = extract_tickers_from_yaml(yaml_path)

    headers = [
        "Ticker", "Name", "P/FCF", "ROIC", "Gross Margin", "Revenue CAGR 5Y",
        "Morningstar Moat", "P/B", "Combined Ratio", "Float Growth", "Quelle", "Notizen"
    ]

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for ticker in tickers:
            is_exc = ticker.upper() in [e.upper() for e in exceptions]
            notes = "Exception (Versicherung/Holding)" if is_exc else ""
            writer.writerow([ticker, "", "", "", "", "", "", "", "", "", "", notes])

    print(f"CSV-Template erstellt: {output_path}")
    print(f"  {len(tickers)} Ticker aus config.yaml extrahiert")
    print(f"  Spalten: {', '.join(headers)}")
    print(f"\nBitte fuellen Sie die leeren Spalten aus und fuehren Sie dann aus:")
    print(f"  python scripts/screen.py --csv {output_path}")


def validate_data(results: list) -> list:
    """Check for data quality issues and return warnings."""
    warnings = []
    for r in results:
        # Missing critical data
        missing = []
        if not r.is_exception:
            if r.p_fcf is None:
                missing.append("P/FCF")
            if r.roic is None:
                missing.append("ROIC")
            if r.gross_margin is None and r.morningstar_moat is None:
                missing.append("Gross Margin ODER Morningstar Moat")
        else:
            if r.price_book is None:
                missing.append("P/B (Exception-Modus)")
            if r.combined_ratio is None and r.float_growth is None and r.roic is None:
                missing.append("Combined Ratio ODER Float Growth ODER ROIC")

        if missing:
            warnings.append({
                "ticker": r.ticker,
                "type": "FEHLEND",
                "detail": f"Fehlende Daten: {', '.join(missing)}",
                "severity": "hoch"
            })

        # Implausible values
        if r.p_fcf is not None and r.p_fcf < 0:
            warnings.append({
                "ticker": r.ticker,
                "type": "UNPLAUSIBEL",
                "detail": f"Negativer P/FCF ({r.p_fcf}) — negativer Free Cash Flow?",
                "severity": "hoch"
            })
        if r.roic is not None and r.roic > 100:
            warnings.append({
                "ticker": r.ticker,
                "type": "UNPLAUSIBEL",
                "detail": f"ROIC > 100% ({r.roic}%) — Berechnung pruefen",
                "severity": "mittel"
            })
        if r.gross_margin is not None and r.gross_margin > 95:
            warnings.append({
                "ticker": r.ticker,
                "type": "PRUEFHINWEIS",
                "detail": f"Gross Margin {r.gross_margin}% — ungewoehnlich hoch",
                "severity": "niedrig"
            })

    return warnings


AMPEL_EMOJI = {"GRUEN": "\U0001f7e2", "GELB": "\U0001f7e1", "ROT": "\U0001f534"}


def format_markdown(results: list) -> str:
    """Format results as Markdown table."""
    lines = ["## Batch-Screen Ergebnis\n"]
    lines.append("| Ticker | P/FCF | ROIC | Moat | Gesamt | Notes |")
    lines.append("|--------|-------|------|------|--------|-------|")

    for r in sorted(results, key=lambda x: {"GRUEN": 0, "GELB": 1, "ROT": 2}.get(x.ampel_gesamt, 3)):
        emoji = AMPEL_EMOJI.get(r.ampel_gesamt, "")
        notes = "; ".join(r.notes) if r.notes else "—"
        lines.append(
            f"| {r.ticker} | {AMPEL_EMOJI.get(r.ampel_p_fcf, '')} {r.ampel_p_fcf} "
            f"| {AMPEL_EMOJI.get(r.ampel_roic, '')} {r.ampel_roic} "
            f"| {AMPEL_EMOJI.get(r.ampel_moat, '')} {r.ampel_moat} "
            f"| {emoji} **{r.ampel_gesamt}** "
            f"| {notes} |"
        )

    return "\n".join(lines)


def format_json(results: list) -> str:
    """Format results as JSON."""
    output = []
    for r in results:
        output.append({
            "ticker": r.ticker,
            "ampel_p_fcf": r.ampel_p_fcf,
            "ampel_roic": r.ampel_roic,
            "ampel_moat": r.ampel_moat,
            "ampel_gesamt": r.ampel_gesamt,
            "is_exception": r.is_exception,
            "notes": r.notes,
            "values": {
                "p_fcf": r.p_fcf,
                "roic": r.roic,
                "gross_margin": r.gross_margin,
                "rev_cagr": r.rev_cagr,
                "price_book": r.price_book,
            },
        })
    return json.dumps(output, indent=2, ensure_ascii=False)


def format_warnings_markdown(warnings: list) -> str:
    """Format data quality warnings as Markdown."""
    if not warnings:
        return ""
    lines = ["\n### ⚠ Datenqualitaets-Hinweise\n"]
    lines.append("| Ticker | Typ | Detail | Schwere |")
    lines.append("|--------|-----|--------|---------|")
    for w in warnings:
        sev_emoji = {"hoch": "🔴", "mittel": "🟡", "niedrig": "ℹ️"}.get(w["severity"], "")
        lines.append(f"| {w['ticker']} | {w['type']} | {w['detail']} | {sev_emoji} {w['severity']} |")
    lines.append("\n*Ticker mit hoher Schwere: Ergebnis moeglicherweise unzuverlaessig — manuelle Pruefung empfohlen.*")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Quick-Screener Batch-Tool")
    parser.add_argument("--csv", help="CSV-Datei mit Finanzkennzahlen")
    parser.add_argument("--yaml", help="config.yaml — extrahiert Ticker-Liste")
    parser.add_argument("--generate-template", metavar="OUTPUT",
                        help="CSV-Template mit Tickern aus config.yaml erstellen")
    parser.add_argument("--validate", action="store_true",
                        help="Datenqualitaets-Checks durchfuehren und Warnungen ausgeben")
    parser.add_argument("--exceptions", default="BRK.B,MKL,FFH.TO",
                        help="Komma-separierte Ausnahme-Ticker (Default: BRK.B,MKL,FFH.TO)")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output-Format (Default: markdown)")
    args = parser.parse_args()

    exceptions = [e.strip() for e in args.exceptions.split(",")]

    # Mode 1: Generate CSV template
    if args.generate_template:
        if not args.yaml:
            print("ERROR: --generate-template benoetigt --yaml [config.yaml]", file=sys.stderr)
            sys.exit(1)
        generate_template(args.yaml, args.generate_template, exceptions)
        return

    # Mode 2: Extract tickers from YAML (info only)
    if args.yaml and not args.csv:
        tickers = extract_tickers_from_yaml(args.yaml)
        print("Ticker aus config.yaml extrahiert:")
        for t in tickers:
            exc = " (Exception)" if t.upper() in [e.upper() for e in exceptions] else ""
            print(f"  - {t}{exc}")
        print(f"\nGesamt: {len(tickers)} Ticker")
        print("\nCSV-Template erstellen mit:")
        print(f"  python scripts/screen.py --yaml {args.yaml} --generate-template screener_template.csv")
        return

    # Mode 3: Screen from CSV
    if args.csv:
        results = parse_csv(args.csv, exceptions)
        warnings = validate_data(results) if args.validate else []

        if args.format == "json":
            output = {
                "results": json.loads(format_json(results)),
                "warnings": warnings if warnings else [],
            }
            print(json.dumps(output, indent=2, ensure_ascii=False))
        else:
            print(format_markdown(results))
            if warnings:
                print(format_warnings_markdown(warnings))
            # Summary
            gruen = sum(1 for r in results if r.ampel_gesamt == "GRUEN")
            gelb = sum(1 for r in results if r.ampel_gesamt == "GELB")
            rot = sum(1 for r in results if r.ampel_gesamt == "ROT")
            print(f"\n**Zusammenfassung:** {gruen} Gruen | {gelb} Gelb | {rot} Rot")
            if warnings:
                high = sum(1 for w in warnings if w["severity"] == "hoch")
                if high:
                    print(f"⚠ {high} Ticker mit kritischen Datenhinweisen — manuelle Pruefung empfohlen!")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
