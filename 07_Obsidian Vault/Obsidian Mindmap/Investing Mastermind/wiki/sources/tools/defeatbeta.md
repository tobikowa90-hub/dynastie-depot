---
tags: [quelle, api, us-ticker, fundamentals]
status: aktiv
version: 1.27.0
stand: 2026-04-07
---

# defeatbeta MCP — Primärquelle US-Fundamentals

## Was es liefert

- Income Statement, Cash Flow, Balance Sheet (quarterly + annual)
- ROIC, WACC, Enterprise Value
- Geographic Revenue Breakdown
- EPS, Margins, Growth Rates
- Earnings Transcripts

## Konfiguration (WSL2)

```
wsl -d Ubuntu-24.04 bash -c /home/tobia/.defeatbeta-env/bin/python -m defeatbeta_mcp
```

Version: 1.27.0 | 100+ Tools | Daten bis 03.04.2026

**Achtung:** Immer `-d Ubuntu-24.04` spezifizieren (Ubuntu default = leer).

## Routing-Regel

| Datentyp | Tool |
|----------|------|
| Fundamentals (US) | defeatbeta (Primär) |
| Technicals | Shibui SQL |
| Insider | insider_intel.py / OpenInsider |
| Forward-Metriken / Moat | Web Search |
| Non-US | yfinance (via eodhd_intel.py) |

## Session-Start-Check

`get_latest_data_update_date` → antwortet = Verbindung OK ✅

## Live-Test-Referenz (07.04.2026)

AVGO: OCF $27.54B | CapEx $623M | FCF $26.91B ✅

## Crosswalk mit FinnHub (seit 2026-05-22)

Read-Only Crosswalk-Pipeline gegen [[finnhub]] (Real-Time-Layer) für **Stale-Detection** (defeatbeta 2-Wochen-Lag-Problem) und zukünftige v0.2-Reklassifizierung. Primary-Pull via WSL-Subprocess `03_Tools/defeatbeta_subprocess.py` gegen `/home/tobia/.defeatbeta-env/bin/python` — bit-perfect Identity zu MCP-Path verifiziert (A12 Δ=0.00 für [MSFT,V,TMO]×[roe,peTTM,roic]). Aktuelle 3/8-Coverage (peTTM/roe/roic Live + 5/8 systematisch N/A); 5/8-Folge-Recherche als PIPELINE #76 (v0.2-Methoden-Discovery).

## Verlinkungen

- [[finnhub]] — Crosswalk-Real-Time-Quelle (Stale-Detection + v0.2-Reklassifizierungs-Gate 2026-07-06)
- [[DEFCON-System]]
- [[Shibui-SQL]]
