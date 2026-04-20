---
title: "Backtest-Methodik-Roadmap"
type: synthesis
tags: [backtest, methodik, roadmap, zukunft, kern, validation-gate]
created: 2026-04-17
updated: 2026-04-20
version: v2.1
sources: [arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha, Bailey-2015-PBO, Aghassi-2023-Fact-Fiction, Flint-Vermaak-2021-Decay, Palomar-2025-Portfolio-Optimization, Li-Kim-Cucuringu-Ma-2026-FINSABER, Sheppert-2026-GT-Score]
related: [Backtest-Ready-Infrastructure, Score-Archiv, FLAG-Event-Log, Wissenschaftliche-Fundierung-DEFCON, DEFCON-System, PBO-Backtest-Overfitting, Factor-Investing-Framework, Factor-Information-Decay, Seven-Sins-Backtesting, Palomar-Methods-Reference, LLM-Investing-Bias-Audit, Regime-Aware-LLM-Failure-Modes, Composite-Anti-Overfitting-Objective]
wissenschaftlicher_anker: "Entscheidungsmatrix für 2028-Review — wann welcher Fundierungs-Paper als Benchmark anlegbar wird + 4-Dimensionen-Validation-Gate (v2.0 seit 2026-04-19, v2.1 erweitert 2026-04-20 um FINSABER-Bias-Audit + GT-Score In-the-Loop-Komponente)"
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

## 4-Dimensionen-Validation-Gate (v2.0, 2026-04-19)

Nach Triage von 4 weiteren Papern (Bailey/Borwein/López de Prado/Zhu 2015 + Aghassi/Asness/Fattouche/Moskowitz 2023 + Flint/Vermaak 2021 + Palomar 2025) verdichtet sich jede retrospektive Analyse auf **vier unabhängige Validations-Dimensionen**, die Options A–D oben ergänzen, nicht ersetzen.

| Dimension | Was geprüft wird | Anker-Paper | Konzept-Seite |
|---|---|---|---|
| **Methode (Overfitting)** | PBO < 0,05 via CSCV | Bailey et al. 2015 | [[PBO-Backtest-Overfitting]] |
| **Raum (External Bench)** | Portfolio-SR im AQR/Ilmanen-Multifaktor-Band | Aghassi et al. 2023 | [[Factor-Investing-Framework]] |
| **Zeit (Temporal Decay)** | Cadence konsistent mit Faktor-Half-Life | Flint/Vermaak 2021 | [[Factor-Information-Decay]] |
| **Sünden (Pre-Flight)** | 7-Punkt-Catalog vor jeder Analyse (#7 n.a. Long-Only) | Palomar 2025 Ch. 8.2 | [[Seven-Sins-Backtesting]] |

**Aktivierungs-Reihenfolge bei Review 2028:**
1. Sünden-Pre-Flight (Sin #1-#6) → erst wenn alle grün, weitergehen
2. Methoden-Gate (PBO/CSCV, ggf. plus walk-forward nach Palomar Ch 8.4)
3. External-Benchmark-Check (aggr. Portfolio-SR im Band)
4. Temporal-Konsistenz-Check (Cadence vs. Half-Life)

**Gatekeeper für Options A–D:** Eine Option kann erst verfolgt werden, wenn alle 4 Dimensionen geprüft sind. Das ersetzt nicht die n-basierten Gates (n ≥ 50 / n ≥ 10 / +180d), sondern ergänzt sie.

### Harvey-Liu-Zhu Hurdle für neue DEFCON-Parameter (§29.4)

**Unabhängig von Review 2028:** Jede neue Scoring-Sub-Komponente (neuer FLAG, neuer Sub-Score, neue Metrik) erfordert **t-Stat ≥ 3** (nicht 2,0). Begründung: 121 unabhängige Trials genügen für t=2-False-Positive, 393 für t=3 (Aghassi et al. 2023).

### Investment-Faktor-Monthly-Observation offen

Flint/Vermaak zeigen Investment-Faktor-Half-Life = 1 Monat. Aktive FLAGs (MSFT CapEx, TMO fcf_trend_neg) sind Investment-Klasse. **Offene Entscheidung Review 2028:** Monthly-Fundamentals-Refresh formalisieren oder bei Earnings-Trigger-Cadence bleiben? Aktuell keine Änderung — FLAG-Mechanik robust genug.

## v2.1-Erweiterung (2026-04-20) — FINSABER + GT-Score

### Neue Validations-Dimensionen

| Dimension | Anker-Paper | Konzept-Seite | §-Konsequenz |
|---|---|---|---|
| **Bias-Audit (Selection-Strategy)** | Li/Kim/Cucuringu/Ma 2026 (FINSABER) | [[LLM-Investing-Bias-Audit]] | §29.5 erweitert um Reject-Set/Iteration-Count/Hold-Out-Audit; ggf. neue §33 Skill-Self-Audit |
| **Regime-Asymmetrie (Bull/Bear)** | Li et al. 2026 (FINSABER Section: Regime Analysis) | [[Regime-Aware-LLM-Failure-Modes]] | §29.2 erweitert um Bull/Bear-Subsample-SR-Trennung; Track 5b FRED wissenschaftlich verankert |
| **Composite-Optimization (in-the-loop)** | Sheppert 2026 (GT-Score) | [[Composite-Anti-Overfitting-Objective]] | §29.1 erweitert um GT-Score (komplementär zu PBO/CSCV); Track 5b Grid-Search Tie-Break R0 |

### Konsequenzen für 2028-Review-Aktivierung

Die ursprüngliche **4-Dimensionen-Gate** (Methode/Raum/Zeit/Sünden) wird zur **5-Dimensionen-Gate**:

1. **Sünden-Pre-Flight (B18 + B19)** — Palomar Seven Sins **erweitert um FINSABER-Audit-Fragen**
2. **Methoden-Gate (B15 + B20)** — Bailey PBO/CSCV **plus GT-Score In-the-Loop wenn Optimierung beteiligt**
3. **External-Benchmark (B16)** — AQR Faktor-Bench, **mit Bull/Bear-Subsample-SR-Trennung (B19)**
4. **Temporal-Konsistenz (B17)** — Flint/Vermaak Half-Life
5. **Portfolio-Metriken (Palomar Ch 6 + B20 Downside-Risk)** — risk-metrics-calculation Aktivierung

### Track-5b-Spezifischer Anwendungs-Pfad

Track 5b FRED Macro-Regime-Filter (Plan 2026-04-20) nutzt FINSABER+GT-Score doppelt:

| Element | FINSABER-Bezug | GT-Score-Bezug |
|---|---|---|
| Regime-Detection als Pre-Decision-Layer | **direkter Anker** für Bull/Bear-Asymmetrie-Adressierung | — |
| Grid-Search 1620 Combos | Bias-Audit-Pflicht (Multiple-Testing) | **Tie-Break R0** vor R1-R5 |
| Sparraten-Modulation Bull/Bear | Empirische Validierung der Asymmetrie | — |
| `forward_6m_hit_rate` Sekundär-Diagnose | Bull/Bear-Subsample-Validation | Significance-Komponente |

→ Track 5b ist nicht heuristisch, sondern adressiert eine **empirisch dokumentierte Failure-Mode aller untersuchten LLM-Investing-Strategien**. Wissenschaftlicher Anker-Wert hoch.

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
