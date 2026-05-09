---
title: "Post-Publication Decay"
type: concept
tags: [defcon, validation, anomaly-decay, mispricing, market-efficiency, b25, meta-gate]
created: 2026-04-26
updated: 2026-04-27
sources: [McLean-Pontiff-2016]
related: [Wissenschaftliche-Fundierung-DEFCON, PBO-Backtest-Overfitting, Factor-Investing-Framework, Factor-Information-Decay, Backtest-Methodik-Roadmap, DEFCON-System, Aghassi-2023-Fact-Fiction, Bailey-2015-PBO]
wissenschaftlicher_anker: "B25 (McLean & Pontiff 2016, JF 71(1)) — 97 Cross-Sectional-Predictoren aus 80 Studien: Out-of-Sample-Decay −26% (statistical bias upper bound), Post-Publication-Decay −58% (publication-effect lower bound 32pp). Decay stärker bei höheren in-sample-Returns/t-Stats, bei liquiden Stocks, bei Price-/Trading-only-Predictoren."
konfidenzstufe: peer-reviewed
defcon_block: "Validation-Methode (§29.7 M&P-Discount, angelegt 26.04.2026)"
operative_regel: "Externe in-sample-Performance-Claims werden vor Adoption mit Faktor 0,42 (= 1 − 0,58) diskontiert. Eigenes Score-Archiv (post-publication-Sample) benötigt keinen zusätzlichen Discount."
aliases:
  - "M&P-Discount"
  - "Publication Decay"
  - "Anomaly Decay"
---

# Post-Publication Decay

> McLean & Pontiff (2016) zeigen empirisch: durchschnittliche Long-Short-Predictor-Returns fallen um 26% out-of-sample (statistical bias upper bound) und um 58% post-publication. Akademische Publikation transmittiert Information an sophisticated investors; Mispricing erodiert (mit Reibung) wenn es bekannt wird.

## Operative Definition

**Post-Publication-Decay** bezeichnet den Performance-Verlust einer Faktor-/Anomalie-Strategie nach öffentlicher Publikation des Predictors. McLean & Pontiff (2016) dekomponieren den Total-Decay in zwei Komponenten:

| Komponente | Magnitude | Mechanismus |
|---|---|---|
| Out-of-Sample-Decay (statistical bias) | -26% (upper bound) | Spurious-Findings-Korrektur — In-Sample-Performance enthält Selection/Mining-Bias |
| Publication-Effect (mispricing-Erosion) | -32pp (lower bound) | Sophisticated Investors arbitrieren das Mispricing, sobald die Anomalie bekannt ist |
| **Total Post-Publication-Decay** | **-58%** | Out-of-Sample × Publication-Wirkung |

**M&P-Discount-Faktor:** `1 − 0,58 = 0,42` → realistische Forward-Erwartung = in-sample-Claim × 0,42.

## Decay-Heterogenität (wer überlebt, wer stirbt)

| Predictor-Eigenschaft | Decay-Stärke | Begründung |
|---|---|---|
| Hohe in-sample-Returns | **größer** | Mehr Mispricing → mehr zu arbitrieren |
| Hohe in-sample-t-Statistik | **größer** | Stärkere Evidenz → mehr Aufmerksamkeit |
| Liquide Stocks, Low-IdioVol | **größer** | Niedrigere Arbitragekosten |
| Illiquide Stocks, High-IdioVol | **kleiner** | Limits-of-Arbitrage halten Mispricing oben |
| Price-/Trading-only-Predictoren | **größer** | Weak-form-Verletzungen werden schnell arbitriert |
| Fundamentals-/Accounting-Predictoren | **kleiner** | Höhere Arbitragekosten, langsamere Korrektur |

→ **DEFCON-Implikation:** Fundamentals-basiertes Scoring (50 Pt., ROIC/FCF/OpM/Bilanz) ist strukturell robuster gegen Post-Publication-Decay als rein technisches Scoring (Technicals-Block 10 Pt.). Bestätigt die bestehende Block-Gewichtung 50/20/10/10/10.

## Beziehung zu anderen Validation-Layern

Post-Publication-Decay ist eine **eigene Dimension** im 4-Dimensionen-Validation-Gate (§29; siehe [[RETROSPECTIVE-GATE]]):

- §29.1 PBO/CSCV (Bailey 2015) testet **in-sample-Overfitting** — adressiert NICHT Publication-Decay
- §29.2 External Bench (Aghassi 2023) reduziert in-sample-Bias, NICHT Publication-Decay
- §29.3 Decay/Half-Life (Flint-Vermaak 2021) misst MIKRO-Faktor-Decay (Monatsbasis); §29.7 misst MAKRO-Publikations-Decay (Jahresbasis)
- §29.4 t-Hurdle ≥3 (Harvey/Liu/Zhu 2016) ist notwendig, NICHT hinreichend — höhere t-Stats decayen STÄRKER
- §29.5 Seven-Sins (Palomar 2025) Sin #6 Look-Ahead-Bias verwandt; Publication-Decay ist eigener Layer
- **§29.7 M&P-Discount** (NEU 26.04.2026) operationalisiert das Konzept als Discount-Faktor

## Crowding-Risiko

Post-Publication steigen Trading-Volume und Short-Interest in Predictor-Portfolios, und **Korrelationen zwischen publizierten Predictoren STEIGEN** — direkter Hinweis auf Crowded-Trade-Risiko. DEFCON-Wide-Moat-Strategien können in Stress-Events korrelierter abstürzen als die in-sample-Sharpe-Ratio suggeriert. Faktor 5b FRED-Regime-Filter (geplant) adressiert das partiell.

## Operative Anwendung in DEFCON

1. **Briefing-Sprache:** Keine in-sample-Performance-Claims im Briefing ohne Diskontierungsformel `claim × 0,42`. Jede zitierte Faktor-Outperformance aus Paper/Vendor → realistische Erwartung explizit ausweisen.
2. **§28.1-Migration-Workflow Step 1:** Paper/Evidence-Check prüft, ob Paper-Claim post-publication validiert wurde. Wenn nicht: M&P-Discount auf in-sample-Werte vor §29.4 t-Hurdle-Vergleich.
3. **Score-Archiv-Markierung:** Bei retrospektiven Analysen der `score_history.jsonl` ab 2028 Sample-Periode explizit als post-publication ausweisen (kein zusätzlicher Discount nötig).
4. **Strukturelle Bestätigung:** Block-Gewichtung 50/20/10/10/10 (Fundamentals-dominant) ist wissenschaftlich tragfähige Anti-Decay-Architektur.

## Limitationen

- **Sample-Periode:** McLean/Pontiff verwenden Predictoren bis ~2010-Publikationsdatum. Post-2015-Publikationen (Faktor-Zoo-Ära) sind nicht im Sample — möglicherweise ist Decay-Geschwindigkeit gestiegen (Hanson/Sundareram 2014, Akbas et al. 2014: Sophisticated-Capital-Levels als Decay-Treiber).
- **Heterogenität:** 32pp ist Lower-Bound-Median über 97 Predictoren. Einzelne Predictoren (z.B. Momentum, Jegadeesh/Titman 1993) zeigen NACHpublikations-VerSTÄRKUNG — Ausnahme zur Regel.
- **Faktor-Persistenz:** Fundamentals-Faktoren (B/M, Profitability) decayen langsamer als Technical-Faktoren (Short-Term Reversal, IdioVol).

## Backlinks

- [[McLean-Pontiff-2016]] — Primärquelle (B25, source-page)
- [[Wissenschaftliche-Fundierung-DEFCON]] — §Status-Matrix B25 `meta-gate`
- [[PBO-Backtest-Overfitting]] — komplementärer §29.1-Layer
- [[Factor-Information-Decay]] — Mikro-Half-Life-Konzept (B17, eng verwandt)
- [[Factor-Investing-Framework]] — t≥3-Hurdle (B16) komplementär zu Decay-Discount
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Strategie, §29.7 dort dokumentiert
- [[DEFCON-System]] — Block-Gewichtung 50/20/10/10/10 strukturell robust
