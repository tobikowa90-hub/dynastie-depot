#!/usr/bin/env python3
"""finnhub_a12_identity_check.py — A12 Acceptance: WSL-subprocess ≡ MCP-path.

Workflow:
1. Run this script standalone → ruft defeatbeta_subprocess.pull_metrics() für 3 Symbole
2. Output ist Tabelle mit WSL-Werten + leere MCP-Spalte
3. User/Claude pulled MCP-Werte separat (mcp__defeatbeta-api__get_stock_quarterly_roe etc.) und füllt MCP-Spalte
4. Identity-Pass = max-Delta <0.01 oder strukturell-äquivalent (None-Mapping)

Spec: docs/superpowers/specs/2026-05-22-finnhub-integration-design.md v0.3 + Build-Plan Task 10.

Usage:
    python 03_Tools/finnhub_a12_identity_check.py [--symbols MSFT,V,TMO]
"""

from __future__ import annotations

import argparse
import json
import sys

import defeatbeta_subprocess

DEFAULT_SYMBOLS = ["MSFT", "V", "TMO"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="A12 Identity-Check WSL vs MCP")
    ap.add_argument("--symbols", default=",".join(DEFAULT_SYMBOLS))
    args = ap.parse_args(argv)

    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    out = {}
    for sym in symbols:
        wsl_data = defeatbeta_subprocess.pull_metrics(sym)
        out[sym] = {"wsl": wsl_data, "mcp": None, "delta_max": None, "status": "PENDING-MCP-FILL"}

    print(json.dumps(out, indent=2))
    print(
        "\n# A12 Identity-Check — Next Steps\n"
        "1. Aus Claude-Session: für jedes Symbol die mcp__defeatbeta-api__get_stock_quarterly_roe,\n"
        "   get_stock_ttm_pe, get_stock_quarterly_roic aufrufen und Werte hier eintragen.\n"
        "   WICHTIG für get_stock_ttm_pe: start_date='<heute-60d>' setzen (z.B. '2026-03-01').\n"
        "   Ohne start_date liefert MCP 1000 Daily-Rows (~170k chars) → token-truncated zu File-Dump.\n"
        "   Nur die letzte Row (max report_date) wird für A12 verglichen; date-range ändert das Ergebnis nicht.\n"
        "2. Pass-Kriterium: max abs(wsl_value - mcp_value) < 0.01 für numerische Felder,\n"
        "   None == None für strukturell-fehlende Werte. MCP roe/roic sind decimal-ratio,\n"
        "   WSL-Werte sind ×100 (Prozent); für direkten Vergleich mcp_value*100 anwenden.\n"
        "3. Bei Pass: A12-Status in 00_Core/SYSTEM.md §Passive Read-Only Data Layer dokumentieren.\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
