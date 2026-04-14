---
title: "Non-US Scoring"
type: concept
tags: [konzept, non-us, ifrs, asml, rms, su]
created: 2026-04-06
updated: 2026-04-14
stand: 2026-04-06
sources: []
related: [DEFCON-System, CapEx-FLAG, Analyse-Pipeline, Tariff-Exposure-Regel, Update-Klassen-DEFCON]
---

# Non-US Scoring — IFRS-Addendum

> ASML, RMS, SU folgen IFRS — nicht US-GAAP. Abweichungen sind strukturell, kein API-Drift.

## Datenquellen-Routing

| Ticker | Primärquelle | Technicals |
|--------|-------------|-----------|
| ASML | yfinance (ASML.AS) | Shibui (ASML NASDAQ ADR) |
| RMS | yfinance (RMS.PA) | — |
| SU | yfinance (SU.PA) | — |

## IFRS-Besonderheiten

| Block | Besonderheit |
|-------|-------------|
| CapEx/OCF | IFRS 16: ROU-Asset-Zugänge nicht als CapEx zählen — nur Cash-CapEx |
| OCF | Leasingzahlungen → Finanzierungs-CF unter IFRS (nicht Operating) |
| OCF-Toleranz | ±15% zwischen IFRS-EU und US-GAAP-Quellen ist strukturell (kein Fehler) |
| Insider | Kein Form 4 / OpenInsider — AFM (ASML) / AMF (RMS, SU) manuell prüfen |
| Reports | RMS + SU: Halbjährlich (H1/H2) — kein Quarterly-Zyklus |

## Kalibrierungsanker

**ASML (06.04.2026):** Score 68 = Wide-Moat-Monopol zu Premium-Bewertung.
- Moat 19/20 = Referenz "bestes europäisches Unternehmen"
- Fundamentals 28/50 = wie teuer ein Monopol sein darf bevor Score kippt
- CapEx/OCF 12.5% = Non-US-Referenz für Asset-Effizienz

## Verlinkungen

- [[ASML]], [[RMS]], [[SU]] — Die 3 Non-US-Satelliten
- [[SNPS]] — ASML-Ersatz | [[RACE]] — RMS-Ersatz | [[DE]] — SU-Ersatz
- [[DEFCON-System]] — Scoring-Matrix
- [[CapEx-FLAG]] — CapEx-Kalibrierung bei IFRS-Abweichungen
- [[Analyse-Pipeline]] — Non-US-Datenrouting in Stufe 2
- [[Tariff-Exposure-Regel]] — EUR-Ticker: geringeres Direkt-Risiko
- [[Update-Klassen-DEFCON]] — Halbjährliche Reports (RMS/SU) → angepasster Rhythmus
- [[non-us-fundamentals]] — yfinance-Modul für Datenabfrage
