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

## Verlinkungen

- [[DEFCON-System]]
- [[Shibui-SQL]]
