---
title: "Backtest-Methodik-Roadmap"
type: synthesis
tags: [backtest, methodik, roadmap, zukunft, kern]
created: 2026-04-17
updated: 2026-04-17
version: v1.0
sources: [arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha]
related: [Backtest-Ready-Infrastructure, Score-Archiv, FLAG-Event-Log, Wissenschaftliche-Fundierung-DEFCON, DEFCON-System]
wissenschaftlicher_anker: "Entscheidungsmatrix für 2028-Review — wann welcher der 4 Fundierungs-Papers als Benchmark anlegbar wird"
konfidenzstufe: synthese
---

# Backtest-Methodik-Roadmap

> **Wann validieren wir formal? Welcher Test passt zu welcher Datenlage? Was 2028-04-01 entschieden werden muss.**

## Warum kein formaler Backtest heute

Ehrliche Sample-Size-Diskussion (siehe [[Backtest-Ready-Infrastructure]] → Problem):

- **n klein**: 11 aktive Satelliten, ~2 Jahre Historie, sparse FLAG-Events (n=2 in Backfill). Keine statistische Power für Return-Prediction oder Threshold-Kalibrierung.
- **Point-in-Time-Daten verstreut**: Historische Moat-Ratings, EPS-Revisionen, Analyst-Konsensus nicht maschinenlesbar rekonstruierbar.
- **Regime-Drift**: v3.4 → v3.5 → v3.7 in 3 Monaten — Scoring-System hat sich schneller geändert als die Validierungs-Basis.

Ein heute gebauter Backtest würde Noise als Signal verkaufen und das kalibrierte System an Overfitting gefährden.

## Was 2028+ möglich wird

Erwartete Datenlage am 2028-04-01 (bei Forward-Pipeline ab 17.04.2026):

| Größe | Schätzung |
|-------|-----------|
| Score-Records (Forward) | 250-300 (28 Ticker × 4-6 Analysen/Jahr × 2 Jahre) |
| FLAG-Events (Trigger+Resolution-Paare) | 15-25 |
| Horizont-Vollständigkeit | +30/+90/+180/+360 Tage für Mehrzahl der Events observierbar |
| Backfill-Ergänzung | ~24 Score-Records + 2-4 FLAGs (Präzision limitiert, Trigger-Datum-Proxies) |

## Entscheidungsmatrix 2028-04-01

Welcher der 4 Fundierungs-Papers wird als Benchmark anlegbar? Abhängig von n und beobachtbarem Horizont:

### Option A — Return-Prediction (Ø Forward-Return | Score-Bucket)

**Anker:** [[Gu-Kelly-Xiu-2020]] (Befunde B1-B3) — FCF/ROIC/Valuation als stabilste Prädiktoren.
**Voraussetzung:** n ≥ 200 Score-Records, +360d observierbar.
**Test:** Median Forward-Return je Score-Quantil. Hypothese: Q4 (Score 70+) outperformt Q1 (Score <50) signifikant.
**Falls n < 200:** Auf Option C downgraden.

### Option B — Wide-Moat-Prämie

**Anker:** [[Morningstar-Wide-Moat]] (B5, B9-B11) — Wide-Moat-Universum outperformt Markt.
**Voraussetzung:** n ≥ 50 Wide-Moat-Records mit mind. 3 Jahren Forward-Historie.
**Test:** Alpha vs. S&P500 für Wide-Moat-Bucket. Hypothese: positives Alpha > 2pp p.a.
**Status:** Eher 2030+ feasibel (3-Jahre-Forward-Ketten brauchen Zeit).

### Option C — Threshold-Kalibrierung

**Anker:** [[Buffetts-Alpha]] (B4, B9) — Faktor-Kombination schlägt Einzel-Metriken.
**Voraussetzung:** n ≥ 50 Records ODER 10+ FLAG-Events.
**Test:** Ist DEFCON-Level-Schwelle (50/60/70) optimal, oder zeigen Daten andere Cutpoints?
**Frühestens:** 2028-Q2 (bei n ≥ 50).

### Option D — FLAG-Event-Study (erweitert)

**Anker:** [[arXiv-1711.04837]] (B2-B3) — Earnings Quality + FCF-Konvergenz.
**Voraussetzung:** n ≥ 10 Events, +180d observierbar.
**Test:** Unterperformt Ticker nach FLAG-Trigger signifikant (Raw + Alpha) vs. Benchmark? Median über FLAG-Typen.
**Status:** n=2 Infrastructure-Sample heute (siehe `02_Analysen/flag_event_study_2026-04-17.md`), n ≥ 10 vermutlich Q4-2027.

## Verbindung zu den 14 Befunden

Aus [[Wissenschaftliche-Fundierung-DEFCON]]:

- **B1-B3** (FCF, ROIC, Earnings Quality) → validierbar via Option A + C
- **B4** (Faktor-Kombination) → validierbar via Option C (DEFCON-Threshold-Test)
- **B5, B9-B11** (Moat + Analyst Bias) → validierbar via Option B + A
- **B2-B3** (FLAG-Trigger-Effekt) → validierbar via Option D
- **B6-B8** (v3.7-Interaktion, Cap, OpM) → zu neu für Validation, 2030+ frühestens
- **B12-B14** (Piotroski, Novy-Marx, Sloan — von v3.6 verworfen) → **explizit NICHT validieren**, da v3.6-Integration verworfen wurde

## Entscheidungs-Gate

Am 2028-04-01 Review-Sitzung mit folgender Check-Liste:

1. **n ≥ 50 Score-Records Forward** (minimum für jede statistische Aussage)?
2. **n ≥ 10 FLAG-Events** (minimum für Option D)?
3. **Horizont-Observabilität**: +180d für ≥ 2/3 der Events?
4. **Scoring-Version-Konsistenz**: Haben v3.7.1+ Major-Versions-Sprünge Regime-Shifts produziert?

Falls Gate NICHT bestanden: Review 2029-04-01 wiederholen, keine voreilige Validation.

Falls Gate bestanden: Diese Roadmap entscheidet, welche Option(en) zuerst durchgeführt werden.

## Nicht-Ziele (explizit YAGNI)

- Kein Monte-Carlo, keine Bootstrap-Simulation bei n < 100
- Keine Signifikanztests bei Infrastructure-Sample (n < 10 FLAGs)
- Keine "Optimierung" der DEFCON-Schwellen basierend auf ex-post Overfitting
- Keine Scoring-Anpassung ohne wissenschaftliche Publikation als Motivation (Applied Learning: "Paper-Ingest ≠ System-Update")

## Abhängigkeiten zu anderen Layern

- **History-Layer** (JSONL-Archive): Voraussetzung für jede Option
- **Narrative-Layer** (log.md, CORE-MEMORY.md): Context für Interpretation, nicht Primärdaten
- **State + Projection-Layer**: irrelevant für Backtest (Point-in-Time-fehlend)

## Anti-Pattern

- Narrative-Layer als Primärquelle für Backtest ziteren → **Point-in-Time-Integritätsverlust**
- Ex-post Editing der JSONL-Archive → **Historie-Manipulation**, violates Spec §3.2
- Entscheidungen aus n=2 Event-Study-Report "Alpha -10.56pp" extrapolieren → **Noise-Overfitting**
