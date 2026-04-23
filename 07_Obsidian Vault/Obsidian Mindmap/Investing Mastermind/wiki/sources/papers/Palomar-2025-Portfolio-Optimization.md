---
title: "Portfolio Optimization: Theory and Application"
date: 2025
type: source
subtype: textbook
tags: [textbook, portfolio-optimization, backtesting, risk-metrics, mvo-critique, risk-parity]
url: https://portfoliooptimizationbook.com/
publisher: "Cambridge University Press"
isbn: "9781009428088"
authors: "Daniel P. Palomar (HKUST — Hong Kong University of Science and Technology)"
status: processed
defcon_relevanz: "Institutionelles Lehrbuch, selektiv wertvoll. Kap. 8.2 Seven Sins of Quantitative Investing = Pre-Flight-Gate §29.5. Kap. 8.3-8.5 walk-forward/CV/synthetic als methodische Erg\u00e4nzung zu Bailey PBO. Kap. 6 Risk-Metric-Formeln als Referenz f\u00fcr bestehenden risk-metrics-calculation-Skill. Kap. 7.5 + 11 als Validation-Reading f\u00fcr Equal-Weight/65-30-5-Allokation."
related: "[[Seven-Sins-Backtesting]], [[Palomar-Methods-Reference]], [[PBO-Backtest-Overfitting]], [[Factor-Investing-Framework]], [[Backtest-Methodik-Roadmap]], [[Wissenschaftliche-Fundierung-DEFCON]], [[DEFCON-System]]"
---

# Palomar — Portfolio Optimization: Theory and Application (2025)

## Abstract (eigene Worte)
Daniel Palomar (HKUST) liefert ein frei zugängliches, peer-reviewed Doktoranden-Lehrbuch über mathematische Optimierungstheorie mit Finanzanwendung. 16 Kapitel + 2 Anhänge, Cambridge University Press 2025. Frei verfügbar als HTML + PDF unter portfoliooptimizationbook.com. **Für Dynasty-Depot selektiv wertvoll** — etwa 60% ist tiefe Mathematik (Konvexoptimierung, GARCH, Graphentheorie) ohne operative Relevanz für ein fundamental-getriebenes Wide-Moat-Depot; die relevanten 40% sind institutioneller Goldstandard.

## Relevante Kapitel für Dynasty-Depot

| Kapitel | Titel | Relevanz | Warum |
|---|---|---|---|
| **Ch 6** | Portfolio Basics | 🔴 Hoch | Formale Definitionen Sortino/CVaR/Calmar/Max-DD/IR — direkt einsetzbar für `risk-metrics-calculation`-Skill + `03_Tools/portfolio_risk.py` |
| Ch 7.5 | Drawbacks of MVP | 🟡 Mittel | Akademische Grundlage warum Mean-Variance-Optimization versagt → bestätigt Equal-Weight-Sparplan |
| **Ch 8.1** | A Typical Backtest | 🟢 Referenz | Backtest-Struktur-Terminologie |
| **Ch 8.2** | The Seven Sins of Quantitative Investing | 🔴 **Kernstück** | Sünden-Katalog → [[Seven-Sins-Backtesting]] §29.5 Gate |
| **Ch 8.3** | The Dangers of Backtesting | 🔴 Hoch | p-hacking, stop-loss-gaming, Overfitting-Mechanik |
| **Ch 8.4** | Backtesting with Historical Market Data | 🔴 Hoch | Walk-forward, Cross-Validation, Randomized — **komplementär zu Bailey CSCV** |
| **Ch 8.5** | Backtesting with Synthetic Data | 🔴 Hoch | Monte Carlo, Bootstrap, I.I.D.-Stress-Testing — **alternative zu CSCV** |
| Ch 11 | Risk Parity Portfolios | 🟡 Mittel | Vol-Contribution-Theorie → Kontext für 65/30/5 (nicht Validation) |

## Nicht-relevant (überspringen)

| Kapitel | Grund für Skip |
|---|---|
| Ch 2–5 | Statistical Modeling, I.I.D., Time Series, Graphs — reine Mathematik |
| Ch 9 | High-Order Portfolios (Skew/Kurt) — overkill für Buy-and-Hold |
| Ch 10 | Alternative Risk Measures — CVaR/Max-DD abgedeckt in Ch 6 |
| Ch 12 | Graph-Based Portfolios — Netzwerk-Optimierung, nicht unser Ansatz |
| Ch 13 | Index Tracking — ETF-Core macht das passiv |
| Ch 14 | Robust Portfolios — relevant bei Unsicherheit in Input-Parametern |
| Ch 15 | Pairs Trading — Long/Short, nicht unser Stil |
| Ch 16 | Deep Learning Portfolios — black-box, widerspricht Moat-Thesen-Stil |
| App A/B | Convex Optimization Theory / Algorithms — pure Mathematik |

→ ~70% des Lese-Aufwands eingespart, ohne institutionellen Wert zu verlieren.

## Die Seven Sins (Ch 8.2) — verbatim

1. **Survivorship Bias** — nur überlebende Strategien/Ticker im Dataset
2. **Look-Ahead Bias** — Information aus der Zukunft in "historischer" Simulation
3. **Storytelling Bias** — post-hoc Narrative, die Ergebnisse rechtfertigen
4. **Overfitting and Data Snooping Bias** — deckungsgleich mit [[PBO-Backtest-Overfitting]]
5. **Turnover and Transaction Cost** — Cost-Realismus in Simulation
6. **Outliers** — Extremereignis-Behandlung (COVID 2020, GFC 2008)
7. **Asymmetric Pattern and Shorting Cost** — **n.a. für uns (Long-Only)**

## Operationalisierung

- **[[Seven-Sins-Backtesting]]** — operative Konzeptseite mit DEFCON-Mapping und Long-Only-Ausnahme
- **[[Palomar-Methods-Reference]]** — konsolidierte Referenz für Ch 6 Formel-Definitionen + Ch 8.3–8.5 Methoden
- **§29.5** (Retrospective-Gate): Seven-Sins-Pre-Flight vor jeder retrospektiven Analyse — Sin #4 deckt [[PBO-Backtest-Overfitting]] ab, #7 n.a.
- **§29.6** (Portfolio-Return-Metrik-Layer): Palomar Ch. 6 Formel-Konventionen bei Aktivierung 2028

## Abgrenzung

**Was Palomar bietet, was andere Paper nicht bieten:**
- Vollständiger Sünden-Katalog (Bailey nur Sin #4 = Overfitting)
- Kanonische Formel-Definitionen für Risk-Metrics (kein anderes Paper)
- Methodische Werkzeugkiste walk-forward / CV / synthetic (ergänzt Bailey CSCV)

**Was Palomar NICHT bietet:**
- Konkrete Faktor-Zahlen (→ Aghassi 2023 / Ilmanen 2021)
- Faktor-Half-Life (→ Flint/Vermaak 2021)
- PBO-spezifische Statistik (→ Bailey 2015)

## Backlinks
- [[Seven-Sins-Backtesting]] — operative Konzeptseite zu Ch 8.2
- [[Palomar-Methods-Reference]] — konsolidierte Referenz Ch 6 + 8.3-8.5 + 7.5 + 11
- [[PBO-Backtest-Overfitting]] — Sin #4 Deckungsgleichheit
- [[Factor-Investing-Framework]] — externe Faktor-Benchmark-Ebene
- [[Factor-Information-Decay]] — Temporal-Validations-Ebene
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Entscheidungsmatrix
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B18
