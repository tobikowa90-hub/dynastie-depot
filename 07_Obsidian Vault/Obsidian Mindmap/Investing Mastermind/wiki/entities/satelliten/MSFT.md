---
tags: [satellit, aktiv, defcon-2, flag-aktiv]
ticker: MSFT
name: Microsoft Corporation
sektor: Cloud / Software
ersatz: GOOGL (FLAG aktiv)
score_aktuell: 59
defcon: 2
flag: "CapEx/OCF Q2 FY26: 83.6% (bereinigt ~63%)"
sparrate: "0€"
letzteAnalyse: 2026-04-17
score_valid_until: 2026-10-14
scoring_notiz_v37: "v3.7 Algebra: 60→59 (-1 Pt. durch Fix-3 Sell-Ratio-Kalibrierung). FLAG überschreibt DEFCON. Q3 FY26 Earnings 29.04. = FLAG-Auflösungs-Pfad."
naechsterTrigger: "2026-04-29 — Q3 FY26 Earnings"
related_concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]]"
---

# MSFT — Microsoft Corporation

> **DEFCON 🟠 2 | Score 59/100 (v3.7) | FLAG 🔴 aktiv**
> Sparrate: 0 € (FLAG überschreibt DEFCON)

## Aktuelle Lage (Stand: 17.04.2026 — v3.7 Algebra)

Score 59 (v3.7: 60→59 durch Fix-3 Sell-Ratio-Kalibrierung). Grund: ROIC strukturell unter WACC (7.5% vs. 13.35%) über 6 Quartale. CapEx FY26 auf Kurs $100–120B. FCF FY25 leicht rückläufig ($71.6B, war $74.1B). FLAG-Auflösungs-Pfad: Q3 FY26 29.04. — bereinigtes CapEx/OCF <60%.

## FLAG-Details

- **Trigger:** CapEx/OCF Q2 FY26 = 83.6% (Finance-Lease-bereinigt ~63%)
- **Regel:** >60% = automatischer FLAG, score-unabhängig
- **Auflösung möglich:** Q3 Earnings 29.04.2026 — bereinigtes CapEx/OCF muss <60% fallen
- **Pre-Processing Regel 2 dauerhaft aktiv:** Finance Lease Obligations $19.5B → immer manueller 8-K-Check

## Scoring-Blöcke (08.04.2026)

| Block | Punkte | Max | Kommentar |
|-------|--------|-----|-----------|
| Fundamentals | ~28 | 50 | CapEx/OCF 0+FLAG, ROIC <WACC (0-1 Pt.) |
| Moat | 19 | 20 | Wide Moat — Azure, M365, Switching Costs |
| Technicals | — | 10 | Unter Druck |
| Insider | — | 10 | — |
| Sentiment | — | 10 | — |

## Entscheidungsbaum nach Q3 Earnings (29.04.2026)

- Bereinigtes CapEx/OCF **<60%** → FLAG aufheben → Score-Update → bei ≥65 DEFCON 3
- Bereinigtes CapEx/OCF **≥60%** → FLAG bleibt → Worst Case prüfen
- Score **<50** → DEFCON 1 → Ersatz-Analyse (GOOGL FLAG aktiv → ZTS/VEEV-Alternative)

## Verlinkungen

- [[DEFCON-System]] — Scoring-Logik
- [[CapEx-FLAG]] — FLAG-Regeln
- [[ROIC-vs-WACC]] — Warum ROIC <WACC ein harter Malus ist
- [[GOOGL]] — Primärer Ersatz (aber ebenfalls FLAG aktiv)

## Analyse-Historie

| Datum | Score | DEFCON | Ereignis |
|-------|-------|--------|---------|
| 26.03.2026 | 77 | 🟡 3 | Erst-Analyse, FLAG gesetzt |
| 08.04.2026 | 60 | 🟠 2 | Re-Analyse v3.4 — ROIC/WACC-Malus verschärft |
| 17.04.2026 | 59 | 🟠 2 | v3.7 Algebra (Fix-3 Sell-Ratio, -1 Pt.) — FLAG bleibt aktiv |

## Wissenschaftliche Basis
- [[5J-Fundamental-Fenster]] — 5J-Perspektive als Pflichtrahmen für alle Fundamentaldaten
- [[FCF-Primacy]] — FCF-Yield und forward P/E als primäre Bewertungsanker; trailing P/E: nur Kontext
- [[Moat-Taxonomie-Morningstar]] — Moat-Prüfung nach 8-Quellen-Schema (Wide/Narrow/None)
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix: wissenschaftliche Validierung des DEFCON-Systems

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch (AI-Capex-Phantasy), Multiple-Expansion
- **Quality:** moderat — ROIC solide, aber CapEx/OCF 83.6% FLAG aktiv ([[CapEx-FLAG]]) reduziert Earnings-Quality temporär
- **Momentum:** moderat — Kurs-Konsolidierung nach Rally, Q3 FY26 am 29.04.
- **Defensive:** moderat — Moat wide (Azure + Office), aber CapEx-Intensität steigt
- **Investment:** **stark (negativ)** — CapEx/OCF 83.6% → aktiver Investment-FLAG ([[CapEx-FLAG]]). Flint-Vermaak Investment-Half-Life ~1M → §30 Monthly-Refresh pflicht

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Factor-Information-Decay]], [[Flint-Vermaak-2021-Decay]]
