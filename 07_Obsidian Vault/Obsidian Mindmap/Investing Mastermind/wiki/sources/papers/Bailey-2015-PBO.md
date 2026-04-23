---
title: "The Probability of Backtest Overfitting"
date: 2015
type: source
subtype: academic-paper
tags: [backtest, overfitting, pbo, cscv, validation, retrospective-gate]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
pdf_alt: https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
authors: "David H. Bailey (LBL/UC Davis), Jonathan M. Borwein (Newcastle), Marcos López de Prado (Guggenheim/LBL), Qiji Jim Zhu (Western Michigan) — Journal of Computational Finance"
status: processed
defcon_relevanz: "Retrospective-Analyse-Gate §29.1 — PBO/CSCV als formaler Overfitting-Test bei Strategy-Selection + Parameter-Tuning. Aktivierung 2028-04-01 oder erste DEFCON-Parameter-Variation. Nicht anwendbar auf aktuelles Forward-Score-Append (kein Selection-Kontext)."
related: "[[PBO-Backtest-Overfitting]], [[Backtest-Methodik-Roadmap]], [[Score-Archiv]], [[Backtest-Ready-Infrastructure]], [[Wissenschaftliche-Fundierung-DEFCON]]"
---

# Bailey, Borwein, López de Prado, Zhu — The Probability of Backtest Overfitting (2015)

## Abstract (eigene Worte)
Die Autoren zeigen, dass Standard-Techniken zur Vermeidung von Regression-Overfitting (insbesondere Hold-out-Validation) im Backtest-Kontext unzuverlässig sind, weil aus N Strategie-Varianten systematisch die beste gewählt wird — ein Multiple-Testing-Problem, das Hold-out ignoriert. Vorgeschlagen wird **PBO** (Probability of Backtest Overfitting) als Bayesian Posterior-Wahrscheinlichkeit, dass die In-Sample-Siegerstrategie Out-of-Sample unter Median fällt. Die konkrete Schätzmethode **CSCV** (Combinatorially Symmetric Cross-Validation) partitioniert die Performance-Matrix in S Zeitscheiben und bildet alle (S choose S/2) symmetrische Train/Test-Splits — ergibt deterministische, nicht-parametrische Logit-Verteilung. Paper ist der institutionelle Goldstandard für Backtest-Validierung in der Quant-Industrie.

## Kern-Formeln & Thresholds

| Element | Wert / Formel |
|---|---|
| PBO-Definition (Gl. 2.2) | φ = ∫₋∞⁰ f(λ) dλ — Anteil Logits λ<0 |
| CSCV-Partitionen | S = 16 (Autoren-Empfehlung) → (16 choose 8) = 12.780 Logits |
| Standard-Reject-Schwelle | **PBO > 0,05** (Neyman-Pearson-Custom, S. 13) |
| Minimum-N (Trials) | N >> 10, sonst zu wenige Logit-Werte |
| Minimum-T (Zeitreihe) | ≥ 2 × Modellwahl-Fenster; bei tägl. Daten ~4 J für S=16 |
| Minimum-Observations | ≥ 1.000 (Weiss/Kulikowski-Regel für Hold-out-Äquivalenz) |

## Vier komplementäre Statistiken (S. 13–18)

1. **PBO** — P[IS-Sieger < Median OOS]
2. **Performance Degradation** — Regression SR_IS vs. SR_OOS; β negativ bei Overfitting
3. **Probability of Loss** — P[R_n* < 0 OOS], unabhängig von Overfitting
4. **Stochastic Dominance** (1./2. Ordnung) — Schlägt IS-Optimierung Zufalls-Auswahl?

## Limitationen (Autoren-Eigendiagnose, S. 23-25)

- **Strukturbrüche außerhalb T** werden nicht erfasst (Paper ist blind für Regime-Shifts nach dem Sample)
- **Hoher PBO ≠ keine Skill:** Bei N ähnlich guten Strategien ist PBO hoch, obwohl jede valide ist
- **File-Drawer-Problem:** Verborgene Trials verzerren PBO nach unten
- **Goodhart-Warnung:** *"when a measure becomes a target, it ceases to be a good measure"* — CSCV darf NIEMALS als Selektions-Zielfunktion verwendet werden, nur als Evaluation

## DEFCON-Implikation — Abgrenzung zum aktuellen System

| Aspekt | Bailey-Framework | Unser `backtest-ready-forward-verify` |
|---|---|---|
| Kontext | Strategy-Selection aus N Varianten | Append-only Forward-Score-Log |
| Anwendbarkeit jetzt | ❌ Nein (wir haben 1 System, nicht N) | ✅ Forward-Persistenz |
| Anwendbarkeit ab 2028 | ✅ Bei Parameter-Tuning oder Scoring-Version-Comparison | ✅ Vorgelagertes Daten-Sammeln für §29.1 |
| §28.2 Migration-Δ-Gate | Konzeptioneller Cousin (Version-Drift) | Gestufte Δ≤2/3-5/>5-Toleranz |

**Wichtigste Erkenntnis für uns:** Paper gilt **nicht universell**. Unser aktuelles Score-Logging ist kein "Backtest" im Paper-Sinn und daher kein Kandidat für PBO-Gate. PBO wird erst relevant, wenn wir jemals:
1. Zwischen DEFCON-Versionen retrospektiv vergleichen
2. Scoring-Gewichte oder Thresholds gegen gemessene Forward-Returns tunen
3. Review 2028-04-01 mit Strategy-Selection-Charakter durchführen

## Operationalisierung

- **§29.1** (Retrospective-Analyse-Gate): PBO < 0,05 als harte Grenze vor jeder Scoring-Parameter-Variation
- **`03_Tools/backtest-ready/pbo_cscv.py`** — Python-Implementierung bei Aktivierung (nicht jetzt); CRAN `pbo`-Package als Referenz
- **Brücke zu Paper 4 Palomar Ch. 8.4:** Walk-forward / randomized backtests als komplementäre Validation-Methoden

## Backlinks
- [[PBO-Backtest-Overfitting]] — operative Konzeptseite
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Entscheidungsmatrix (extended)
- [[Seven-Sins-Backtesting]] — Sin #4 (Overfitting) deckungsgleich
- [[Score-Archiv]] — Datenbasis für spätere PBO-Anwendung
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B15
