---
title: "Palomar-Methods-Reference (Ch 6 + 8.3-8.5 + 7.5 + 11)"
type: concept
tags: [risk-metrics, backtesting-methods, walk-forward, synthetic-data, mvo-critique, risk-parity, reference]
created: 2026-04-19
updated: 2026-04-19
sources: [Palomar-2025-Portfolio-Optimization]
related: [Seven-Sins-Backtesting, PBO-Backtest-Overfitting, Backtest-Methodik-Roadmap, ETF-Core, DEFCON-System]
wissenschaftlicher_anker: "Palomar (2025) — Portfolio Optimization"
konfidenzstufe: methoden-referenz
---

# Palomar-Methods-Reference

> **Konsolidierte Methoden-Referenz aus Palomar-Lehrbuch. Keine operative Konzept-Seite im engeren Sinn — Nachschlagewerk für Review 2028 und für den `risk-metrics-calculation`-Skill.**

## Ch. 6 — Risk-Metric-Formel-Konventionen

Die kanonischen Definitionen für unseren bestehenden `risk-metrics-calculation`-Skill + `03_Tools/portfolio_risk.py`:

| Metrik | Formel (schematisch) | Anwendung |
|---|---|---|
| **Sharpe Ratio** | (E[R] − R_f) / σ(R) | Standard-Vergleich |
| **Sortino Ratio** | (E[R] − R_f) / σ_downside(R) | Downside-spezifisch; σ nur negative Returns |
| **Calmar Ratio** | CAGR / Max-DD | Risk-adjusted mit Drawdown-Fokus |
| **Max-Drawdown** | max_t (peak − trough) / peak | Worst-Case-Kapitalverlust |
| **CVaR (ES) α** | E[R | R ≤ VaR_α] | Erwarteter Verlust im Tail |
| **Information Ratio** | (E[R_portfolio] − E[R_benchmark]) / σ(R_p − R_b) | Alpha pro Tracking-Error |

**Wichtig:** Sortino-Denominator-Konvention variiert zwischen Quellen (Target-Return vs. Null, geometrisch vs. arithmetisch). **Palomar-Konvention** als einheitlicher Referenz-Standard übernehmen bei Skill-Aktivierung 2028.

## Ch. 8.3 — The Dangers of Backtesting

Unterthemen mit DEFCON-Relevanz:
- **p-hacking** — mehrfach-testen bis Signifikanz erreicht; PBO-Anti-Pattern
- **Stop-loss gaming** — Schleier über schlechte Entry-Timing durch schnellen Exit
- **Overfitting Mechanik** — Warum auch "out-of-sample" Overfitting haben kann

Für uns: Awareness-Lektüre, keine konkrete Gate-Regel daraus.

## Ch. 8.4 — Backtesting with Historical Market Data

**Drei Methoden, alle komplementär zu [[PBO-Backtest-Overfitting]] CSCV:**

| Methode | Wann passt sie besser als CSCV? |
|---|---|
| **Walk-forward Analysis** | Bei starkem Regime-Drift; Strategie wird sequenziell re-kalibriert |
| **k-Fold Cross-Validation** | Bei kurzen Zeitreihen; schneller als CSCV |
| **Randomized Backtesting** | Bei geordneten Daten und Regime-Abhängigkeiten |

**Anwendung 2028:** Bei Forward-Score-Retrospektive können wir:
- CSCV als primäres PBO-Estimate (nach Bailey)
- Walk-forward als Sanity-Check (sequenziell)
- Randomized als Stress-Variante

## Ch. 8.5 — Backtesting with Synthetic Data

Monte-Carlo / Bootstrap als Alternative, wenn:
- Historische Samples zu klein sind
- Outlier-Behandlung (Sin #6) separat getestet werden soll
- I.I.D.-Annahmen eingehalten werden können (für unsere Return-Serie: vorsichtig)

**Nicht-Ziel für uns:** Synthetic-Data als Haupt-Backtest (wir haben primär echte Forward-Records). Relevant für Stress-Tests und Outlier-Sensitivity.

## Ch. 7.5 — Drawbacks of MVP (Mean-Variance-Portfolio)

Warum wir **nicht** klassische Markowitz-MVO verwenden:

1. **Estimation Error** — kleine Änderungen in Return-Schätzungen produzieren drastisch unterschiedliche Gewichte
2. **Concentration** — MVO neigt zu 2-3 Position-Konzentration
3. **Leverage** — MVO empfiehlt oft unrealistische Leverage
4. **Sensitivity zu Covarianz-Schätzung** — historische Cov-Matrix instabil

→ **Unser Equal-Weight-Sparplan** auf 11 Satelliten umgeht diese Pathologien. Palomar's Ch 7.5 ist **akademische Validation** dieses Designs, kein Aufruf zu einer Änderung.

## Ch. 11 — Risk Parity Portfolios

**Kern-Idee:** Gewichte so, dass jede Position gleichen Volatilitäts-Beitrag hat (nicht gleichen Dollar-Anteil).

**Abgrenzung zu unserem 65/30/5:**
- 65/30/5 ist **strategische Dollar-Allokation** (ETF 65% / Satelliten 30% / Gold 5%)
- Risk Parity würde Vol-Beiträge ausgleichen — bei unseren Tickern hätte das vermutlich andere Gewichte (Low-Vol wie BRK.B mehr, High-Vol wie ASML/AVGO weniger)
- Risk Parity ist **kein Design-Ziel** für Dynasty-Depot

**Relevanz:** Kontext-Lektüre. Bei Review 2028 ggf. Vergleichs-Portfolio ("Was hätte Risk Parity gezeigt?") als akademischer Sanity-Check.

## Operationalisierung

- **§29.6** (Portfolio-Return-Metrik-Layer): Ch. 6 Formel-Konventionen als Referenz bei Aktivierung `risk-metrics-calculation`-Skill 2028
- **§29.1 komplementär:** Ch. 8.4 walk-forward / randomized als Zusatz-Validation zu CSCV
- **§29.5 bonus:** Ch. 8.5 synthetic data für Outlier-Stress-Test (Sin #6)
- **Validation-Reading (keine Operationalisierung):** Ch. 7.5 + 11 als akademischer Kontext

## Abgrenzung zu [[Seven-Sins-Backtesting]]

- Seven-Sins (Ch 8.2) = **Pflicht-Pre-Flight** (§29.5)
- Diese Seite = **Methoden-Nachschlagewerk** (§29.1 + §29.6 bei Aktivierung)

Unterschiedliche operative Funktion → daher zwei getrennte Konzept-Seiten.

## Backlinks
- [[Palomar-2025-Portfolio-Optimization]] — Source-Zusammenfassung
- [[Seven-Sins-Backtesting]] — Pre-Flight-Sünden-Gate (Ch 8.2)
- [[PBO-Backtest-Overfitting]] — CSCV-Primärmethode, hier erweitert um walk-forward + synthetic
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Entscheidungsmatrix
- [[ETF-Core]] — 65/30/5-Allokation, Ch. 11 Kontext
- [[DEFCON-System]] — Zielsystem, dessen Return-Serie spätere Metrik-Anwendung erhält
