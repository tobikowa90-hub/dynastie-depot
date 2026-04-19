# portfolio_returns.jsonl — Schema v1.0

**Stand:** 19.04.2026 | **Aktiviert:** Phase 3 R5 Paper-Integration

## Record-Schema (append-only JSONL, ein Record pro Tag)

```json
{
  "schema_version": "1.0",
  "date": "YYYY-MM-DD",
  "portfolio_value_gross": 1234.56,
  "cashflow_net": 0.00,
  "portfolio_return": 0.00234,
  "benchmark_value": 5678.90,
  "benchmark_return": 0.00152,
  "positions": [
    {"ticker": "AVGO", "weight_eod": 0.12, "price_eod": 234.56, "value_eod": 148.27}
  ]
}
```

## Felder

- `schema_version`: "1.0" (Major-Bump bei Breaking-Change)
- `date`: ISO-Date des yfinance-**Trading-Date** (letzte gemeinsame Handelssitzung aller Ticker). NICHT Wall-Clock. Eindeutig pro Record.
- `portfolio_value_gross`: Post-Cashflow-NAV in EUR (= `V_prev × (1 + portfolio_return) + cashflow_net`). Kumulative Portfolio-Zeitreihe für §29.6 Risk-Metrics.
- `cashflow_net`: Netto-Einzahlung/Auszahlung am Tag (+ Spar-Einzahlung, − Entnahme). Kritisch für Return-Rekonstruktion.
- `portfolio_return`: Equal-Weighted Daily Return (Cashflow-bereinigt — reine Marktbewegung)
- `benchmark_value`: Benchmark-NAV (SPY oder Multifactor-Index)
- `benchmark_return`: Daily Benchmark Return
- `positions[]`: Alle Satelliten + ETF + Gold zum EoD

## Mixed-Currency-Hinweis

Satelliten mischen USD (US-Tickers) + EUR (ASML.AS, RMS.PA, SU.PA). Der `portfolio_return` ist der equal-weighted Mittelwert **lokaler** Tagesrenditen — kein währungsbereinigter Multi-Currency-Return. Akzeptabel für Dynasty-Depot-Scope (synthetischer Local-Return-Index). Vor §29.2 AQR-Benchmark-Vergleich (Review 2028) muss FX-Conversion nachgerüstet werden — Notiz für Interim-Gate 2027-10-19.

## Benchmark-Handling

Benchmark wird parallel täglich persistiert in `05_Archiv/benchmark-series.jsonl`. Keine retrospektive Rekonstruktion — Point-in-Time-Disziplin (§29.5 Sin #2).

## Quellen-Fundierung

- Palomar 2025 Ch 6 — Sortino/Calmar/Max-DD/CVaR/IR basieren auf diesem Schema
- §29.5 Sin #2 — Look-Ahead-Prevention via Point-in-Time-Persistenz
- §29.6 Portfolio-Return-Metrik-Layer — Aktivierung Review 2028-04-01 nach 24+ Monaten

## Write-Path

`03_Tools/portfolio_risk.py --persist daily` (ab Phase 3). Append-only, nie Edit. Git-Tracking pflicht.
