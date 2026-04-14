---
title: "Tariff-Exposure-Regel"
type: concept
tags: [konzept, tariff, scoring, liberation-day]
created: 2026-04-06
updated: 2026-04-14
stand: 2026-04-06
sources: []
related: [DEFCON-System, Analyse-Pipeline, CapEx-FLAG, Non-US-Scoring, Update-Klassen-DEFCON]
---

# Tariff Exposure — Scoring-Regel

> Post Liberation Day (02.04.2026): Pflicht-Check bei jedem !Analysiere.

## Schwellen

| Exposure | Konsequenz |
|----------|------------|
| < 15% | Kein Malus, keine Notiz |
| 15–35% | Risk-Map-Notiz, kein FLAG |
| > 35% | 🔴 FLAG aktiv, -3 Punkte Fundamentals, 0€ Sparrate |

## Risikoländer (Tariff-relevant)

CN (China), TW (Taiwan), MY (Malaysia), TH (Thailand), VN (Vietnam)

## Quellen-Reihenfolge

1. SEC EDGAR 10-K/20-F → "Geographic Revenue" (Primär)
2. defeatbeta `get_quarterly_revenue_by_geography`
3. Earnings Call Transcript (Management-Kommentar)
4. SimplyWallSt (Fallback)

## Aktueller Status (10.04.2026)

| Ticker | Exposure | Status |
|--------|----------|--------|
| AVGO | ~35% (MY/TH) | Risk-Map-Notiz, Grenzwert |
| APH | CN/MY — nicht quantifiziert | Check ausstehend (Priorität 6) |
| COST | US-lastig, Ketteneffekte | Check ausstehend (Priorität 4) |
| RMS, SU, ASML | EUR, EU-Produktion | Geringes Direkt-Risiko |
| VEEV, V, BRK.B | Software/Holding | Kein Direkt-Risiko |

## Verlinkungen

- [[DEFCON-System]] — Scoring-Matrix
- [[Analyse-Pipeline]] — Tariff-Check als Pflicht in jeder !Analysiere-Session
- [[CapEx-FLAG]] — Verwandter FLAG-Trigger (>60% CapEx/OCF)
- [[Non-US-Scoring]] — EUR-Ticker haben geringeres Direkt-Risiko
- [[Update-Klassen-DEFCON]] — Makro-Schock >50 Bps = Klasse-C-Event
