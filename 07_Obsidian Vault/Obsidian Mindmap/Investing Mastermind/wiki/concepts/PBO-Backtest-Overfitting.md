---
title: "PBO — Probability of Backtest Overfitting"
type: concept
tags: [backtest, overfitting, pbo, cscv, validation, method]
created: 2026-04-19
updated: 2026-04-19
sources: [Bailey-2015-PBO]
related: [Backtest-Methodik-Roadmap, Seven-Sins-Backtesting, Palomar-Methods-Reference, Factor-Investing-Framework, Factor-Information-Decay, Score-Archiv, Backtest-Ready-Infrastructure, DEFCON-System]
wissenschaftlicher_anker: "Bailey, Borwein, López de Prado, Zhu (2015) — Journal of Computational Finance"
konfidenzstufe: methoden-standard
---

# PBO — Probability of Backtest Overfitting

> **Formaler Overfitting-Test für Strategy-Selection und Parameter-Tuning. Goldstandard institutioneller Quant-Validierung. Für unser System: Gate-Komponente §29.1 ab Review 2028-04-01 oder erster DEFCON-Parameter-Variation.**

## Kern-Idee

Wenn aus N Strategie-Varianten systematisch die beste gewählt wird, ist selbst bei t-Stat 2,0 einer Einzelstrategie ein False-Positive mit hoher Wahrscheinlichkeit eingebaut (Multiple-Testing-Bias). **PBO** quantifiziert diese Wahrscheinlichkeit als Bayesian Posterior: Wie wahrscheinlich liegt der IS-Sieger OOS unter dem Median aller N Strategien?

- **PBO ≈ 0** → Strategie-Auswahl war informationsreich
- **PBO ≈ 0,5** → Zufall, Backtest wertlos
- **PBO > 0,5** → Overfitting, Strategie schlechter als Zufallsauswahl

## Harte Schwelle (Autoren-Custom)

| PBO | Aktion |
|---|---|
| ≤ 0,05 | Akzeptiert (Neyman-Pearson) |
| 0,05–0,5 | Kritisch — Ursache identifizieren |
| > 0,5 | Reject |

## CSCV-Algorithmus (Estimator)

1. Performance-Matrix M (T × N) bilden — T Zeitperioden, N Strategien
2. In S gleich große Scheiben partitionieren (S=16 Autoren-Default → 12.780 Logits)
3. Alle (S choose S/2) symmetrische Train/Test-Splits bilden
4. Pro Split: Logit λ = ln(ω / (1-ω)), wobei ω = OOS-Rank-Position des IS-Siegers
5. Verteilung f(λ) kumulieren; PBO = φ = ∫₋∞⁰ f(λ) dλ

**Vorteile gegenüber Hold-out / K-Fold:**
- Train/Test-Größe symmetrisch (gleiche Sharpe-Konfidenz)
- Jede Scheibe mehrfach Train UND Test — keine willkürliche Cut-Entscheidung
- Deterministisch (jackknife-ähnlich), keine Randomisierung
- Modellfrei, nicht-parametrisch

## Anwendungskontext — entscheidend

PBO ist definiert für **Strategy-Selection aus N Alternativen**. Drei typische Einsatzszenarien:

1. **Scoring-Gewichte-Tuning:** "Sollte Moat-Block 20 oder 25 Punkte wiegen?" — N Varianten, empirisch beste wählen
2. **Threshold-Optimierung:** "Ist DEFCON-Cutoff 50/65/80 optimal?" — N Cutoff-Kombinationen testen
3. **Scoring-Versions-Vergleich:** "Performt v3.7 besser als v3.5?" — N=2 Versionen, retrospektiv gegen Forward-Returns

**Nicht-Anwendungsfall:** Unser aktueller `backtest-ready-forward-verify` Skill schreibt ScoreRecords append-only aus einer einzigen Scoring-Version. Kein Selection-Kontext → PBO aktuell inaktiv.

## Vier komplementäre Statistiken

Paper liefert nicht nur PBO, sondern Framework mit 4 Dimensionen:

| Statistik | Was es misst | Wann kritisch |
|---|---|---|
| PBO | P[Overfitting] | Immer |
| Performance Degradation | Regression SR_IS vs SR_OOS (β-Vorzeichen) | Bei positiven OOS-Erwartungen |
| Probability of Loss | P[Return < 0 OOS] | Unabhängig von Overfitting |
| Stochastic Dominance | Schlägt IS-Selektion Zufallsauswahl? | Fundamentale Validity-Prüfung |

## Dos & Don'ts

**Do:**
- PBO vor jeder Strategie-Veröffentlichung/Live-Deployment berechnen
- Alle tatsächlich getesteten N Trials offenlegen (File-Drawer-Bias vermeiden)
- Mindestens N >> 10, T ≥ 2× Modellwahl-Fenster, S = 16 als Default

**Don't:**
- PBO als Zielfunktion für Strategie-Suche missbrauchen (Goodhart-Law)
- Verborgene Pre-Screening-Schritte auslassen
- Hoher PBO automatisch als "Strategie ist schlecht" interpretieren (bei N ähnlich-gut kann PBO hoch sein ohne Invalidität)

## Operationalisierung im Dynasty-Depot

- **§29 Retrospective-Analyse-Gate** (`00_Core/INSTRUKTIONEN.md`) — PBO < 0,05 als §29.1 Komponente
- **Aktivierungs-Trigger:** Review 2028-04-01 **oder** erstmaliges Scoring-Parameter-Tuning
- **Implementierungs-Pfad:** `03_Tools/backtest-ready/pbo_cscv.py` bei Aktivierung; CRAN R-Package `pbo` als Referenz; Python-Portierung trivial
- **Brücke zu Palomar Ch. 8.4:** walk-forward und randomized backtests als komplementäre (nicht konkurrierende) Validierungs-Verfahren — siehe [[Palomar-Methods-Reference]]

## Abgrenzung §28.2 Migration-Δ-Gate

Unser §28.2 ist **konzeptioneller Cousin**, aber semantisch anders:
- §28.2 trackt Algebra-vs-Forward-Delta bei **Versions-Migration** (v3.x → v3.y)
- PBO trackt IS-vs-OOS-Rank bei **Selection aus N**
- Beide adressieren gemeinsam: nicht durch Backtest-Shopping täuschen

## Backlinks
- [[Bailey-2015-PBO]] — Source-Zusammenfassung
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Entscheidungsmatrix
- [[Seven-Sins-Backtesting]] — Sin #4 (Overfitting) deckungsgleich mit PBO-Domäne
- [[Palomar-Methods-Reference]] — komplementäre Methoden (walk-forward, CV, synthetic)
- [[Factor-Investing-Framework]] — AQR-Bench als externe Validierungs-Ebene
- [[Factor-Information-Decay]] — Temporal-Dimension der Validation
- [[DEFCON-System]] — Zielsystem, auf das PBO bei Parameter-Variation angewendet wird
