---
title: "Seven Sins of Quantitative Investing"
type: concept
tags: [backtest, sins, validation, pre-flight, retrospective-gate, method]
created: 2026-04-19
updated: 2026-04-19
sources: [Palomar-2025-Portfolio-Optimization]
related: [Palomar-Methods-Reference, PBO-Backtest-Overfitting, Factor-Investing-Framework, Factor-Information-Decay, Backtest-Methodik-Roadmap, Score-Archiv, FLAG-Event-Log, Backtest-Ready-Infrastructure, DEFCON-System]
wissenschaftlicher_anker: "Palomar (2025) — Portfolio Optimization Ch. 8.2"
konfidenzstufe: methoden-standard
---

# Seven Sins of Quantitative Investing

> **Der vollständige Sünden-Katalog bei Backtesting. Pre-Flight-Check vor jeder retrospektiven Analyse (§29.5). Sin #4 (Overfitting) ist deckungsgleich mit [[PBO-Backtest-Overfitting]]. Sin #7 (Shorting) ist n.a. für Long-Only-Dynasty-Depot.**

## Der Katalog

| # | Sin | Kurz-Definition | DEFCON-Mapping / Risiko |
|---|---|---|---|
| **1** | Survivorship Bias | Nur überlebende Strategien/Ticker im Dataset | ⚠️ `score_history.jsonl` enthält nur analysierte Ticker — Early-Rejects via Quick-Screener fehlen |
| **2** | Look-Ahead Bias | Zukunfts-Information in "historischer" Simulation | ⚠️ `source=forward` + `score_datum` adressieren teilweise; Backfill-Records nutzen Ex-Post-Daten |
| **3** | Storytelling Bias | Post-hoc Narrative zur Ergebnis-Rechtfertigung | ⚠️ CORE-MEMORY §5 dokumentiert Scoring-Rationale — post-hoc-Narrativ-Risiko bei Migration-Events |
| **4** | Overfitting / Data Snooping | Strategie zu fit auf Sample, OOS-Decay | ✅ **deckungsgleich mit [[PBO-Backtest-Overfitting]]** |
| **5** | Turnover & Transaction Cost | Ignorieren realer Handelskosten in Simulation | ⚠️ Sparplan hat implizite Kosten; nicht modelliert |
| **6** | Outliers | Extremereignis-Ignoranz oder -Über-Gewichtung | ⚠️ 2020 COVID, 2008 GFC — Review 2028 braucht Policy |
| **7** | Asymmetric Pattern & Shorting Cost | Short-Side ungleich Long-Side behandelt | ❌ **n.a. — Dynasty-Depot ist strikt Long-Only** |

## Warum Seven Sins UND PBO

PBO (Sin #4 formalisiert) ist ein Teil des Overfitting-Schutzes, aber **Sünden #1, #2, #3, #5, #6 sind unabhängig**. PBO allein reicht nicht:
- Ein backtest mit perfekter PBO kann trotzdem Survivorship-Bias haben
- Ein backtest mit Look-Ahead-Bias produziert beliebig gute PBO-Werte (Zukunfts-Info macht jeden IS-Sieger OOS-dominant)
- Ein backtest ohne Outlier-Policy kann Einzel-Ereignisse über-gewichten

→ Seven-Sins-Pre-Flight ist **Pflicht vor** PBO-Berechnung, nicht Alternative.

## Sin-für-Sin: Dynasty-Depot-Spezifika

### Sin #1 Survivorship Bias
**Angriff:** `score_history.jsonl` enthält nur Ticker, die zur Analyse angenommen wurden. Tickers, die der Quick-Screener früh ablehnte, fehlen. Ein retrospektiver Backtest "welche Score-Bucket-Regel predicted Forward-Returns" übersieht die Reject-Population.

**Mitigation bei Review 2028:**
- `03_Tools/quick-screener/` historie checken — wenn vorhanden, Reject-Set rekonstruieren
- Sonst: bias explizit dokumentieren, nicht "wegrechnen"

### Sin #2 Look-Ahead Bias
**Angriff:** Backfill-Records nutzen Scoring-Regeln v3.7 auf Daten vor v3.7-Existenz. Forward-Records schreiben mit aktuellem Wissen für heutigen Ticker-State.

**Mitigation:**
- `source` Feld trennt Forward von Backfill — bei Backtest nur `source=forward` nutzen
- Portfolio-Return-Persistenz **JETZT** starten (nicht 2028 Backfill) → Phase 3 von diesem Plan

### Sin #3 Storytelling Bias
**Angriff:** CORE-MEMORY §5 dokumentiert Scoring-Rationale. Risiko: nach Post-Forward-Verify-Beobachtung Rationale nachträglich "passend gemacht".

**Mitigation:**
- CORE-MEMORY §5 ex-ante vor Forward-Run, nicht ex-post
- Migration-Events mit Algebra-vs-Forward-Δ dokumentiert in §28.2 — das schützt bereits

### Sin #4 Overfitting / Data Snooping
**Angriff:** Siehe [[PBO-Backtest-Overfitting]] — deckungsgleich.

**Mitigation:** §29.1 PBO < 0,05.

### Sin #5 Turnover & Transaction Cost
**Angriff:** Unsere Sparplan-Struktur hat monatliche Transaktionen (ETF + 11 Satelliten + Gold). Broker-Kosten + Spread nicht in Return-Analyse eingerechnet.

**Mitigation bei Review 2028:**
- Realistische TER-Annahmen pro Position
- Sparplan-Gebühr (meist 0,99–1,50€ pro Ausführung)
- Spread auf FR-/NL-Märkte (RMS, SU, ASML) nicht-trivial

### Sin #6 Outliers
**Angriff:** COVID 2020, Liberation Day 2026, 2022-Rate-Hikes sind strukturelle Regime-Shifts. Normale Statistik versagt dort.

**Mitigation:**
- Stress-Test-Fenster bereits in `03_Tools/portfolio_risk.py` definiert (COVID + 2022 Rate Hikes)
- Review 2028: eventuell zusätzliche Liberation-Day-Regime-Period
- Explizit outlier-robuste Metriken: Median statt Mean, MAD statt Std

### Sin #7 Asymmetric Pattern & Shorting Cost
**Angriff:** Long-Short-Strategien haben ungleiche Short-Seite (Borrow-Cost, Gamma-Risk, Squeeze-Risk).

**Status:** **Irrelevant für uns.** Dynasty-Depot ist strikt Long-Only. Keine Mitigation nötig. Explizit dokumentiert im Sünden-Gate als "not applicable".

## Pre-Flight-Checkliste (§29.5)

Vor **jeder** retrospektiven Score-History-Analyse:

- [ ] Sin #1: Reject-Set-Rekonstruktion versucht (auch wenn unvollständig)
- [ ] Sin #2: nur `source=forward` oder explizit deklarierter Backfill
- [ ] Sin #3: Rationale ex-ante dokumentiert (CORE-MEMORY §5 vor Forward-Run)
- [ ] Sin #4: PBO/CSCV berechnet, < 0,05
- [ ] Sin #5: Transaktionskosten modelliert
- [ ] Sin #6: Outlier-Windows explizit behandelt
- [ ] Sin #7: n.a. (Long-Only-Note dokumentieren)

## Operationalisierung

- **§29.5** (Retrospective-Gate): 7-Punkt-Pre-Flight vor Analyse, #7 als "n.a." abgehakt
- **Bei Migration-Events (aktiv, nicht future):** Sin #3 (Storytelling) + Sin #4 (Overfitting via §28.2 Δ-Gate) bereits relevant
- **Sin #2 adressiert jetzt:** Phase-3-Portfolio-Return-Persistenz-Start verhindert 2028-Backfill

## Backlinks
- [[Palomar-2025-Portfolio-Optimization]] — Source (Ch 8.2)
- [[Palomar-Methods-Reference]] — Ch 8.3-8.5 methodische Werkzeugkiste
- [[PBO-Backtest-Overfitting]] — Sin #4 formalisiert
- [[Factor-Investing-Framework]] — Sin #6 Outlier-Kontext (Faktor-Drawdowns normal)
- [[Factor-Information-Decay]] — Temporal-Validation ergänzt Sünden-Pre-Flight
- [[Backtest-Methodik-Roadmap]] — 2028-Review, Sin-Pre-Flight als Gate
- [[Score-Archiv]] — Datenbasis auf der Sünden-Check angewendet wird
- [[FLAG-Event-Log]] — Datenbasis mit eigenen Sünden-Risiken (File-Drawer-Problem)
- [[Backtest-Ready-Infrastructure]] — Design adressiert Sin #2 proaktiv
- [[DEFCON-System]] — Zielsystem, das gegen Sünden geschützt werden muss
