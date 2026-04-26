---
title: "Does Academic Research Destroy Stock Return Predictability?"
date: 2016
type: source
subtype: academic-paper
tags: [defcon, backtest-validation, post-publication-decay, anomaly-decay, mispricing, market-efficiency, meta-gate, b25]
url: https://ssrn.com/abstract=2156623
venue: "Journal of Finance 71(1), 2016, 5-32. SSRN abstract 2156623"
authors: "R. David McLean (University of Alberta), Jeffrey Pontiff (Boston College)"
status: processed
defcon_relevanz: "Befund B25 (`meta-gate`). §29 Backtest-Validation-Framework. Diese Studie ist die strukturelle Grundlage für den 2028-04-01 Backtest-Review-Gate. Kern: Cross-sectional Predictoren verlieren 26% out-of-sample (statistical bias upper bound) und 58% post-publication (mispricing erodiert durch Aufmerksamkeit). Folgen für DEFCON: (1) JEDE in-sample-Outperformance der Faktortabelle muss um geschätzte 32% post-publication-Decay diskontiert werden bevor sie als 'Edge' gilt. (2) §29-Gate-Aktivierung kann nicht 'einfach Backtest-Code laufen lassen' bedeuten — der Gate muss in-sample/post-sample/post-publication trennen. (3) Faktoren mit höherer in-sample-t-Statistik haben STÄRKEREN Decay (kein Schutz vor 'starker' Evidenz). (4) Korrelation zwischen Predictor-Portfolios STEIGT post-publication (Crowding-Effekt, Liquiditätsrisiko bei Stress-Events). Operative Konsequenz: §29.4 t≥3-Hurdle (B16) reicht nicht — Decay-Estimation muss zusätzlicher Layer im 2028-Review werden."
related: "[[Post-Publication-Decay]], [[PBO-Backtest-Overfitting]], [[Factor-Investing-Framework]], [[Factor-Information-Decay]], [[Backtest-Methodik-Roadmap]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]], [[Aghassi-2023-Fact-Fiction]], [[Bailey-2015-PBO]]"
raw_path: "../../../raw/papers/McLean & Pontiff.pdf"
aliases:
  - "McLean Pontiff 2016"
  - "Does Academic Research Destroy Stock Return Predictability"
  - "Post-Publication Decay Paper"
---

# McLean & Pontiff (2016) — Does Academic Research Destroy Stock Return Predictability?

## Abstract (eigene Worte)

McLean und Pontiff testen 97 Cross-Sectional-Predictoren aus 80 publizierten Studien auf Out-of-Sample- und Post-Publication-Performance. Ergebnis: durchschnittliche Long-Short-Predictor-Returns fallen um **26% out-of-sample** (statistical bias upper bound) und um **58% post-publication** (mispricing-Decay durch Aufmerksamkeit). Differenz von 32 Prozentpunkten ist die Lower-Bound-Schätzung des reinen Publikations-Effekts. Decay ist **stärker** für Predictoren mit höheren in-sample Returns/t-Statistiken und für Predictoren, die nur Preis-/Trading-Daten verwenden (weak-form efficiency violations). Post-publication erhöht sich Trading-Volume und Short-Interest in Predictor-Portfolios, und Korrelationen zu anderen publizierten Predictoren STEIGEN — direkter Hinweis auf Crowded-Trade-Risiko. **Befund:** Akademische Publikation transmittiert Information an sophisticated investors; Mispricing erodiert (mit Reibung) wenn es bekannt wird.

## Drei Kernzahlen für die Faktortabelle

| Periode | Avg. Monthly Return | Decay vs. In-Sample |
|---|---|---|
| In-Sample (Original-Studie) | 0.582% | — |
| Out-of-Sample, Pre-Publication | 0.402% | **−31%** (statistical bias upper bound: 26%) |
| Post-Publication | 0.264% | **−55%** (publication effect lower bound: 32%) |

(Werte aus der Studie selbst, Section II.)

## Drei Hypothesen — und wer gewinnt

| Hypothese | Out-of-Sample | Post-Publication | Empirisches Ergebnis |
|---|---|---|---|
| Statistical Bias only (Spurious) | Returns → 0 | Returns → 0 | **Verworfen** (in-sample-Returns überleben teilweise out-of-sample) |
| Rational Risk Pricing (Cochrane 1999) | Returns gleich | Returns gleich | **Verworfen** (signifikanter Post-Publication-Decline) |
| **Mispricing + Investor Learning** | Mild Decay | Starker Decay | **Bestätigt** — Decay-Pattern + Volume + Correlation-Increase passt |

Die Mispricing-Hypothese gewinnt mit Decay-Pattern-Konsistenz: höhere in-sample-Returns → größerer post-publication-Decline (R² der Cross-Sectional-Regression von Decay auf Original-t-Stat: 0.20).

## Decay-Architektur — wer überlebt, wer stirbt

| Predictor-Eigenschaft | Decay-Stärke | Begründung |
|---|---|---|
| Hohe in-sample-Returns | **größer** | Mehr Mispricing → mehr zu arbitrieren |
| Hohe in-sample-t-Statistik | **größer** | Stärkere Evidenz → mehr Aufmerksamkeit |
| Liquide Stocks, Low-IdioVol | **größer** | Niedrigere Arbitragekosten |
| Illiquide Stocks, High-IdioVol | **kleiner** | Limits-of-Arbitrage halten Mispricing oben |
| Price-/Trading-only-Predictoren | **größer** | Weak-form-Verletzungen werden schnell arbitriert |
| Fundamentals-/Accounting-Predictoren | **kleiner** | Höhere Arbitragekosten, langsamere Korrektur |

→ **DEFCON-Implikation:** Fundamentals-basiertes Scoring (50 Pt., ROIC/FCF/OpM/Bilanz) ist **strukturell robuster** gegen Post-Publication-Decay als rein technisches Scoring (Technicals-Block 10 Pt.). Das ist eine Bestätigung der bestehenden Block-Gewichtung 50/20/10/10/10.

## DEFCON-Implikation (operativ — B25 `meta-gate`)

Das Paper ist **kein** Live-Scoring-Trigger, sondern ein **strukturelles Methoden-Gate** für §29 Backtest-Validation-Framework (FUTURE-ACTIVATION 2028-04-01, siehe [[Backtest-Ready-Infrastructure]]).

| §29-Gate | McLean/Pontiff-Konsequenz |
|---|---|
| §29.1 (PBO/CSCV — B15) | Reicht nicht. PBO testet Overfitting im Sample. M&P zeigt: SELBST nach Sample-Wechsel folgt zusätzlicher Publikations-Decay. Layer 1. |
| §29.2 (External Bench — B16) | Reicht nicht. Externe Daten reduzieren in-sample-Bias, aber nicht Post-Publication-Decay. Layer 2. |
| §29.3 (Decay/Half-Life — B17) | Direkter Match. Flint-Vermaak-Half-Life misst sehr ähnliches Phänomen. Layer 3. |
| §29.4 (t-Hurdle ≥3 — B16) | Notwendig, nicht hinreichend. M&P zeigt: HÖHERE t-Stats decayen STÄRKER. Layer 4. |
| §29.5 (Seven-Sins — B18) | Sin #6 "Look-Ahead-Bias" verwandt; aber Publikations-Decay ist kein klassischer Seven-Sins-Punkt. Eigener Layer 5. |
| **NEU §29.7 (geplant)** | **"M&P-Discount":** in-sample-Result × 0.42 (=1 − 0.58) als Plausibilitätsprüfung post-publication. |

## Operative Schlussfolgerungen für die Faktortabelle

1. **Keine in-sample-Performance-Claims im Briefing** ohne Diskontierungsformel `claim × 0.42 ≤ neue_realistische_erwartung`.
2. **2028-Review-Gate-Erweiterung:** §29 muss explizit dokumentieren, ob ein Faktor pre-publication oder post-publication-Daten verwendet. Score-Archiv (seit 17.04.2026) ist post-publication-Sample → keine zusätzliche Diskontierung nötig, aber explizit als post-publication zu markieren.
3. **Crowding-Risiko-Watch:** Post-Publication-Increase in Predictor-Korrelationen (Lee/Shleifer/Thaler-Pattern) bedeutet, dass DEFCON-ähnliche Quality+Moat-Strategien in Stress-Events korrelierter abstürzen können als das in-sample-Sharpe-Ratio suggeriert. Faktor 5b FRED-Regime-Filter (geplant) adressiert das partiell.
4. **B25 deaktiviert kein bestehendes Scoring-Element**, sondern ergänzt das §29-Methodik-Gate um eine 7. Dimension (M&P-Discount).

## Literatur-Anker

- **Vorgänger:** Schwert (2003) — Size+Value-ETFs ohne Alpha post-publication. Anekdotisch, kein systematisches Sample.
- **Verwandt:** Jegadeesh/Titman (2001) — Momentum-Returns STIEGEN nach 1993-Publikation (Gegenbeispiel zur Decay-Hypothese; M&P zeigen aber, dass das eine Ausnahme im 97-Predictor-Sample ist).
- **Komplementär:** Harvey/Liu/Zhu (2016, [[Harvey-Liu-Zhu-2016]]) — t≥3-Hurdle für neue Faktoren. M&P sagt: SELBST mit t≥3 erleidet der Faktor 32%+ Post-Publication-Decay.
- **Forschungsfront:** Hanson/Sundareram (2014), Akbas/Armstrong/Sorescu/Subrahmanyam (2014) — Sophisticated-Capital-Levels als Decay-Treiber (M&P kontrolliert das nicht, ist explizit als Limitation genannt).

## Backlinks

- [[Post-Publication-Decay]] — neue Konzept-Page (B25-Anker)
- [[PBO-Backtest-Overfitting]] — komplementärer §29.1-Layer
- [[Factor-Investing-Framework]] — t≥3-Hurdle (B16) komplementär zu Decay-Discount (B25)
- [[Factor-Information-Decay]] — Half-Life-Konzept (B17), eng verwandt
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Strategie, B25-Erweiterung dort dokumentiert
- [[DEFCON-System]] — Block-Gewichtung 50/20/10/10/10 strukturell robust gegen M&P-Decay-Pattern
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B25
- [[R. David McLean]], [[Jeffrey Pontiff]] — Author-Entities
