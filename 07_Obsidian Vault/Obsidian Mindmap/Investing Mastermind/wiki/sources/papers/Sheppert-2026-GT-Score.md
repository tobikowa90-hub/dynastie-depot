---
title: "The GT-Score: A Robust Objective Function for Reducing Overfitting in Data-Driven Trading Strategies"
date: 2026
type: source
subtype: academic-paper
tags: [overfitting, objective-function, walk-forward, monte-carlo, downside-risk, composite-score, validation-gate]
url: https://arxiv.org/abs/2602.00080
venue: "Journal of Risk and Financial Management (MDPI), 2026, 1, 0 — Open Access (CC BY)"
authors: "Alexander Pearson Sheppert (Capitol Technology University, Department of Computer and Data Science)"
status: processed
defcon_relevanz: "Methoden-Anker §29.1 (Komplement zu Bailey PBO: in-the-loop statt post-hoc) und §29.6 Portfolio-Metriken (Downside-Risk-Komponente). DEFCON ist Composite-Score (5 Blöcke); GT-Score-Pattern (Performance × Significance × Consistency × Downside-Risk) ist ein Validation-Lens für unsere Block-Gewichtungen — kein zwingender Code-Change im Skill, sondern Audit-Methodik (Codex Round 2 A5). Direkte Anwendung in Track 5b FRED Grid-Search (1620 Combos) als robusteres Acceptance-Criterion."
related: "[[Composite-Anti-Overfitting-Objective]], [[PBO-Backtest-Overfitting]], [[Palomar-Methods-Reference]], [[Backtest-Methodik-Roadmap]], [[Seven-Sins-Backtesting]], [[Wissenschaftliche-Fundierung-DEFCON]]"
---

# Sheppert — The GT-Score (JRFM 2026)

## Abstract (eigene Worte)

Sheppert führt das **GT-Score (Golden Ticket Score)** ein — eine zusammengesetzte Zielfunktion, die Anti-Overfitting-Prinzipien direkt in den Optimierungsprozess integriert, statt Overfitting nur ex-post via Deflated Sharpe (Bailey/López de Prado) zu messen. Empirische Validierung mit 50 S&P-500-Aktien über 2010-2024, mit Walk-Forward-Validation (9 sequentielle Splits) und Monte-Carlo-Studie (15 Random-Seeds × 3 Trading-Strategien). Hauptbefund: **+98% Generalization-Ratio** (val_return/train_return) ggü. Baseline-Objectives (Sortino, Simple). Paired Statistical Tests p<0,01 vs. Sortino/Simple — kleine Effect-Sizes. Komplementär zu PBO/CSCV: Bailey filtert nach Auswahl, GT-Score steuert *während* der Auswahl.

## Die GT-Score-Komposition (Sheppert 2025 + 2026 Validation)

GT-Score = ƒ(**Performance**, **Statistical Significance**, **Consistency**, **Downside Risk**)

| Komponente | Was sie misst | Typische Realisierung |
|---|---|---|
| **Performance** | Cumulative / annualized return | Total Return, CAGR |
| **Statistical Significance** | p-Wert oder Sharpe-Konfidenz unter Multiple-Testing | Adjusted p, Deflated SR (Bailey 2014) |
| **Consistency** | Stabilität über Sub-Perioden | Walk-Forward-Stability, Rolling-SR-Stdev |
| **Downside Risk** | Asymmetric Loss-Modellierung | Sortino, Max-Drawdown, CVaR |

→ Composite-Score wird **vom Optimizer maximiert**. Das Ziel: Spurious Patterns werden während der Suche herausgefiltert, nicht erst nach der Strategie-Wahl verworfen.

## Empirisches Setup (Section 4-5)

| Element | Wert |
|---|---|
| Universe | 50 S&P-500-Aktien |
| Zeitraum | 2010-2024 (15 Jahre) |
| Walk-Forward | 9 sequentielle Time-Splits |
| Monte-Carlo | 15 Random-Seeds × 3 Trading-Strategien |
| Baseline-Objektive | Sortino, Simple |
| Generalization-Ratio | val_return / train_return |
| Reproduzierbarkeit | Code + Result-Files als Supplementary Material |

## Quantitative Befunde

| Metric | Baseline (Sortino, Simple) | GT-Score | Δ |
|---|---|---|---|
| Generalization Ratio | Baseline | +98% | hochsignifikant |
| Paired t-Test p-Wert (vs Sortino) | — | < 0,01 | statistisch detektierbar |
| Paired t-Test p-Wert (vs Simple) | — | < 0,01 | statistisch detektierbar |
| Effect Size | — | klein | praktische Vorsicht |

**Lesart:** GT-Score liefert **statistisch detektierbare**, aber praktisch *moderate* Verbesserung. Die größere Aussage liegt in der Architektur (during-search vs. after-search), nicht im numerischen Edge.

## Theoretische Einordnung (Section 2 — Related Work)

- **Bailey/López de Prado (2014):** Deflated Sharpe Ratio als selection-bias-aware Performance-Metrik. **Post-hoc.**
- **Bailey et al. (2016):** PBO via CSCV (siehe [[Bailey-2015-PBO]]). **Post-hoc, retrospektiv.**
- **Sullivan/White (1999), White (2000), Hansen (2005):** Reality Check, SPA-Test — Multiple-Testing-Korrekturen. **Post-hoc.**
- **Romano/Wolf (2005):** Stepwise Multiple Testing Procedures. **Post-hoc.**
- **GT-Score (2025/2026):** Anti-Overfitting **in der Optimization-Loop selbst**.

→ GT-Score und PBO/CSCV sind **komplementär, nicht konkurrierend**. Beide adressieren verschiedene Lebenszyklus-Phasen einer Strategie.

## DEFCON-Implikation — Audit-Lens, kein Code-Change

DEFCON-Scoring ist ein **deterministisches Composite** (5 Blöcke: Fundamentals 50pt-Cap, Moat 20pt, Technicals 10pt, Sentiment 10pt, Insider 10pt). GT-Score-Pattern (Performance × Significance × Consistency × Downside-Risk) ist als **Validation-Lens** auf diese Block-Gewichtungen anwendbar:

| GT-Komponente | DEFCON-Lens-Frage |
|---|---|
| Performance | Korreliert höher Score tatsächlich mit Forward-Return? *(Antwort: 2028-Review)* |
| Significance | t-Stat ≥ 3 Hurdle für jeden Sub-Score (B16 Aghassi)? *(bereits in §29.4)* |
| Consistency | Stabil über v3.x-Versionen? §28.2 Δ-Gate adressiert das Migration-Δ-Problem |
| Downside Risk | Identifiziert DEFCON-Top-Bucket (≥80) reliable die Drawdown-Resistenten? |

**Wichtigste Erkenntnis für uns:** GT-Score ist nicht zwingend ein Skill-Code-Feature, sondern ein **strukturierter Audit-Rahmen**. Codex Round 2 A5 hat das explizit bestätigt: "Echter Code-Change nur nötig, wenn GT-Score als permanente Acceptance-/Monitoring-Schicht in den Skill eingebaut wird."

## Direkter Track-5b-Bezug — FRED Regime-Filter Grid-Search

Der geplante Track-5b-Plan optimiert über **1620 Combos** (hy_oas × curve × ism × persistence × operator × factor) auf historischen FRED-Daten 1997+. Klassischer Multiple-Testing-Kontext mit hohem Overfitting-Risiko.

**Empfohlener GT-Score-Patch:**
- Aktuelle Primärmetrik: `1 - avg_filtered/avg_unfiltered` (Utility)
- Sekundär-Diagnose (Codex): `forward_6m_hit_rate`
- **Zusatz:** GT-Score-Aggregat aus (Utility, t-Stat ≥ 3, Sub-Period-Stability, Max-Drawdown-Reduction) als Tie-Break R0 (vor R1-R5)

Damit wird die 1620-Combo-Suche robuster gegen Single-Metric-Overfitting.

## Operationalisierung (Phase 2 von Paper-Ingest 2026-04-20)

- **§29.1 Erweiterung** — GT-Score als komplementäre In-the-Loop-Methode neben Bailey PBO (Post-hoc); beide bei Parameter-Tuning anwenden
- **§29.6 Erweiterung** — Downside-Risk-Komponente (Sortino, CVaR, Max-DD) für `risk-metrics-calculation` formell aufnehmen (war bereits implizit in Palomar Ch 6)
- **Track 5b** — GT-Score-Aggregat als Tie-Break R0 in Grid-Search-Acceptance-Layer (Plan-Diff-Task)
- **Mögliche §33** — falls Skill-Self-Audit etabliert wird, GT-Score als Audit-Methode dokumentieren
- **Implementierungs-Pfad:** Python-Implementation trivial (~50 LOC); kein eigenständiger Skill, sondern Tooling in `03_Tools/backtest-ready/`

## Abgrenzung — Was GT-Score NICHT ist

- **Keine neue Performance-Metrik** — sondern Aggregations-Architektur über bekannte Metriken
- **Kein Ersatz für PBO/CSCV** — komplementär (in-the-loop vs post-hoc)
- **Kein Universal-Patch für DEFCON** — DEFCON ist deterministisch, kein Optimizer-Output
- **Keine Aussage zu LLM-Inferenz** — GT-Score ist objektiv-funktional, agnostisch zu Strategie-Klasse

## Backlinks

- [[Composite-Anti-Overfitting-Objective]] — operative Konzeptseite (GT-Score-Pattern)
- [[PBO-Backtest-Overfitting]] — Komplement (post-hoc vs in-the-loop)
- [[Palomar-Methods-Reference]] — Walk-Forward + Monte-Carlo-Methoden (Ch 8.4-8.5)
- [[Seven-Sins-Backtesting]] — Sin #4 (Overfitting) inhaltlich verwandt
- [[Backtest-Methodik-Roadmap]] — v2.1 Update durch FINSABER + GT-Score
- [[Bailey-2015-PBO]] — methodischer Vorläufer
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B20
- [[Alexander Pearson Sheppert]] — Author-Entity
