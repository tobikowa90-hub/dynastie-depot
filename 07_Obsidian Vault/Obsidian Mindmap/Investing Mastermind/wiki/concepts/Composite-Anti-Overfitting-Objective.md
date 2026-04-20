---
title: "Composite Anti-Overfitting Objective (GT-Score-Pattern)"
type: concept
tags: [overfitting, objective-function, composite, walk-forward, monte-carlo, downside-risk, validation, method]
created: 2026-04-20
updated: 2026-04-20
sources: [Sheppert-2026-GT-Score]
related: [PBO-Backtest-Overfitting, Palomar-Methods-Reference, Backtest-Methodik-Roadmap, Seven-Sins-Backtesting, DEFCON-System]
wissenschaftlicher_anker: "Sheppert (2026, JRFM) — GT-Score: Performance × Significance × Consistency × Downside-Risk"
konfidenzstufe: methoden-standard
---

# Composite Anti-Overfitting Objective (GT-Score-Pattern)

> **Anti-Overfitting-Architektur, die in den Optimization-Loop integriert wird, statt nur post-hoc via Deflated Sharpe oder PBO. Komplementär zu Bailey/CSCV. Direkt anwendbar auf Track 5b FRED Grid-Search (1620 Combos) und als Audit-Lens für DEFCON's 5-Block-Composite. Kein zwingender Skill-Code-Change — primär strukturierter Audit-Rahmen.**

## Kern-Idee

Die meisten Anti-Overfitting-Verfahren der Literatur (PBO/CSCV nach Bailey, Reality Check nach White, SPA-Test nach Hansen, Deflated Sharpe nach Bailey/López de Prado) operieren **post-hoc** — nach Strategie-Auswahl. Sheppert's GT-Score verschiebt den Filter **in die Optimierung selbst**: Der Optimizer maximiert nicht eine Single-Metric (z.B. Sharpe), sondern ein **Composite aus 4 Komponenten**, das spurious patterns während der Suche herausfiltert.

## Die 4 Komponenten

| Komponente | Was sie misst | Typische Realisierung |
|---|---|---|
| **Performance** | Roher Return | Cumulative, CAGR |
| **Statistical Significance** | Konfidenz unter Multiple-Testing | Adjusted p, Deflated SR |
| **Consistency** | Stabilität über Sub-Perioden | Walk-Forward-Stability, Rolling-SR-Stdev |
| **Downside Risk** | Asymmetrische Loss-Modellierung | Sortino, Max-DD, CVaR |

→ GT-Score = ƒ(Performance, Significance, Consistency, Downside-Risk). Konkrete Aggregations-Formel ist parametrisierbar; Sheppert validiert mit Walk-Forward (9 Splits) + Monte-Carlo (15 Seeds).

## Empirische Validierung (Sheppert 2026)

| Metric | Wert |
|---|---|
| Universe | 50 S&P-500-Aktien |
| Zeitraum | 2010-2024 (15 Jahre) |
| Generalization-Ratio (val/train) | **+98% vs Baseline** |
| Paired t-Test (vs Sortino) | p < 0,01 |
| Paired t-Test (vs Simple) | p < 0,01 |
| Effect Size | klein |

**Lesart:** Statistisch detektierbare Verbesserung mit moderater Effekt-Stärke. Hauptaussage liegt in der **Architektur-Verschiebung** (during-search vs. after-search), nicht im numerischen Edge.

## Komplementarität zu PBO/CSCV (Bailey)

| Aspekt | PBO/CSCV (Bailey) | GT-Score (Sheppert) |
|---|---|---|
| Lebenszyklus | Post-hoc (nach Auswahl) | In-the-Loop (während Suche) |
| Ziel | Wahrscheinlichkeit, dass IS-Sieger OOS unter Median | Composite-Maximierung gegen spurious patterns |
| Multiple-Testing-Korrektur | indirekt via PBO-Verteilung | direkt via Significance-Komponente |
| Anwendung | bei Reviews / Strategy-Selection | bei jeder Optimierungs-Suche |

→ **Beide sind nötig**, nicht alternative. PBO antwortet "ist die ausgewählte Strategie wahrscheinlich überangepasst?"; GT-Score antwortet "haben wir während der Suche schon spurious patterns ausgefiltert?".

## DEFCON-Anwendung — Audit-Lens, kein Code-Change

DEFCON's 5-Block-Composite (Fundamentals 50pt, Moat 20pt, Technicals 10pt, Sentiment 10pt, Insider 10pt) ist **deterministisch**, nicht Optimizer-Output. Es gibt keinen Such-Loop, in dem GT-Score während der Suche maximiert würde. Aber das GT-Score-**Schema** ist als Audit-Lens auf bestehende Block-Gewichte anwendbar:

| GT-Komponente | DEFCON-Audit-Frage |
|---|---|
| **Performance** | Korreliert höher Score signifikant mit Forward-Return? *(2028-Review)* |
| **Significance** | t-Stat ≥ 3 für jede Sub-Komponente? *(B16 Aghassi, §29.4)* |
| **Consistency** | Stabil über v3.x-Versionen? *(§28.2 Δ-Gate)* |
| **Downside Risk** | Identifiziert Top-Bucket (≥80) reliable die Drawdown-Resistenten? |

**Wichtigste Erkenntnis:** GT-Score erfordert **keinen Code-Change in DEFCON-Skills**, sondern liefert ein strukturiertes Audit-Schema. Codex Round 2 (A5) hat das explizit bestätigt: "Echter Code-Change nur nötig, wenn GT-Score als permanente Acceptance-/Monitoring-Schicht in den Skill eingebaut wird."

## Direkter Track-5b-Anwendungsfall

Track 5b FRED Regime-Filter optimiert über **1620 Combos** (hy_oas × curve × ism × persistence × operator × factor) auf historischen FRED-Daten 1997+. Klassisches Multiple-Testing-Setup mit hohem Overfitting-Risiko.

**Aktuelle Plan-Metriken:**
- Primärmetrik: `1 - avg_filtered/avg_unfiltered` (Utility)
- Sekundär-Diagnose (Codex): `forward_6m_hit_rate`
- Tie-Break: 5-Regel-Lexikographie R1-R5

**Empfohlener GT-Score-Patch:**
- **Zusatz: GT-Score-Aggregat als Tie-Break R0 (vor R1-R5)** mit:
  - Performance = Utility (bisherige Primärmetrik)
  - Significance = adjusted-p für 1620-Combo-Multiple-Testing
  - Consistency = Walk-Forward-Stability über Sub-Perioden 1997-2010 / 2011-2026
  - Downside-Risk = Max-DD-Reduction der gefilterten vs ungefilterten Sparrate

→ Robustere Combo-Auswahl gegen Single-Metric-Overfitting.

## Operationalisierung im Dynasty-Depot

- **§29.1 Erweiterung** — GT-Score als komplementäre In-the-Loop-Methode neben Bailey PBO (Post-hoc)
- **§29.6 Erweiterung** — Downside-Risk-Komponente formell aufnehmen (Sortino, Max-DD, CVaR — bereits implizit in Palomar Ch 6)
- **Track 5b Plan-Diff** — GT-Score-Aggregat als Tie-Break R0 in Grid-Search-Acceptance-Layer (Phase 3 Action)
- **Mögliche §33 Skill-Self-Audit** — falls etabliert, GT-Score als Audit-Methode dokumentieren
- **Implementierungs-Pfad:** Python-Implementation trivial (~50 LOC); kein neuer Skill, sondern Tooling in `03_Tools/backtest-ready/`

## Dos & Don'ts

**Do:**
- GT-Score als Audit-Lens für DEFCON-Block-Gewichtungen verwenden
- Bei Track-5b-Grid-Search GT-Score-Aggregat als zusätzliche Tie-Break-Stufe
- GT-Score und PBO/CSCV als **komplementär** kommunizieren (nicht entweder-oder)

**Don't:**
- GT-Score als Universal-Patch für DEFCON adoptieren (DEFCON ist deterministisch, kein Optimizer)
- Single-Metric-Optimization (z.B. nur Utility in Track 5b) trotz GT-Score-Verfügbarkeit beibehalten
- GT-Score als "Anti-PBO" framen — beide haben unterschiedliche Lebenszyklus-Phasen

## Backlinks

- [[Sheppert-2026-GT-Score]] — Source-Zusammenfassung
- [[PBO-Backtest-Overfitting]] — Komplement (post-hoc vs in-the-loop)
- [[Palomar-Methods-Reference]] — Walk-Forward + Monte-Carlo-Methoden
- [[Backtest-Methodik-Roadmap]] — v2.1 Validation-Framework
- [[Seven-Sins-Backtesting]] — Sin #4 (Overfitting) inhaltlich verwandt
- [[DEFCON-System]] — Zielsystem für GT-Score-Audit-Lens
- [[Alexander Pearson Sheppert]] — Author-Entity
