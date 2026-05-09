---
title: "RETROSPECTIVE-GATE.md (§29 Retrospective-Analyse-Gate)"
type: concept
aliases:
  - "Retrospective-Analyse-Gate"
  - "RETROSPECTIVE-GATE"
  - "RETROSPECTIVE-GATE.md"
  - "§29"
  - "§29 Retrospective-Analyse-Gate"
tags: [system, single-source-of-truth, backtest-validation-framework, gate]
created: 2026-05-09
updated: 2026-05-09
sources: []
related: [PBO-Backtest-Overfitting, Seven-Sins-Backtesting, Post-Publication-Decay, Factor-Information-Decay, Factor-Investing-Framework, LLM-Investing-Bias-Audit, Composite-Anti-Overfitting-Objective, Palomar-Methods-Reference, Regime-Aware-LLM-Failure-Modes, Earnings-Foreknowledge-Window]
---

# RETROSPECTIVE-GATE.md

> **Vault-externe Datei.** Liegt in `00_Core/RETROSPECTIVE-GATE.md` außerhalb des Obsidian Vaults. Diese Wiki-Page existiert nur als Backlink-Anker.

## Rolle (seit Pointer-Extraction Wave-3 2026-05-09)

**Detail-Spec für §29 Retrospective-Analyse-Gate** — extrahiert aus `INSTRUKTIONEN.md §29` (PIPELINE #16 Variante A Pointer-Refactor; INSTRUKTIONEN 1149→960 LOC -16,4%). INSTRUKTIONEN behält §29-Stub mit 9 H3-Sub-Section-Headings für Cross-Reference-Erhalt; alle Inhalte (4-Dimensionen-Framework + B19/B20/B25-Cross-Refs) leben jetzt verbatim in der externen Detail-Spec.

**4-Dimensionen-Gate-Framework:**
- §29.1 Methoden-Gate — PBO/CSCV nach [[PBO-Backtest-Overfitting|Bailey 2015]]
- §29.2 External-Benchmark-Gate — AQR/Ilmanen-Multifaktor nach [[Factor-Investing-Framework|Aghassi 2023]]
- §29.3 Cadence-Check — Faktor-Decay nach [[Factor-Information-Decay|Flint/Vermaak 2021]]
- §29.4 t-Stat≥3-Hurdle — Multiple-Testing nach Harvey/Liu/Zhu 2016
- §29.5 Pre-Flight Seven-Sins-Gate — [[Seven-Sins-Backtesting|Palomar 2025]] (aktiv-jetzt bei Migration-Events, NICHT FUTURE-ACTIVATION)
- §29.6 Review-Gate — formales 2J-System-Review (Aktivierung 2028-04-01)
- §29.7 M&P-Discount-Layer — [[Post-Publication-Decay|McLean/Pontiff 2016]]; in-sample-Claim × 0,42 als Plausibility-Test

**Aktivierung:** §29.5 läuft bereits jetzt bei jedem Migration-Event (DEFCON-Versions-Sprung). §29.1-4 + §29.6 + §29.7 sind `[FUTURE-ACTIVATION: 2028-04-01]` ODER erste DEFCON-Parameter-Variation. Komplementär zu [[DEFCON-System|§28 Migration-Workflow]] — nicht konkurrierend (§28 schützt Versions-Sprünge, §29 schützt Retrospective-Auswertungen).

## Wann lesen

On-demand bei Backtest-/Strategy-Selection-/Parameter-Tuning-Sessions gegen `score_history.jsonl`; bei System-Audit-Läufen die §29.5-Sektion als Pre-Flight-Checkliste; ab 2028-04-01 zusätzlich §29.6 für formales System-Review.

## Pfad

`C:\Users\tobia\OneDrive\Desktop\Claude Stuff\00_Core\RETROSPECTIVE-GATE.md`
