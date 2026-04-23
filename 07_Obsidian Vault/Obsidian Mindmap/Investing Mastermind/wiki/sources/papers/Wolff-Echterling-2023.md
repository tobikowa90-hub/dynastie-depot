---
title: "Stock Picking with Machine Learning"
date: 2023
type: source
subtype: academic-paper
tags: [defcon, ml-faktoren, profitability, quality, stoxx-europe, s&p500]
url: https://onlinelibrary.wiley.com/doi/full/10.1002/for.3021
authors: "[[Dominik Wolff]], [[Fabian Echterling]]"
journal: "Journal of Forecasting (Wiley)"
status: processed
defcon_relevanz: "Fundamentals-Block (50 Pt.) — ROIC + FCF + Operating Margin als top-ranked Profitability-Faktoren | Bilanz-Block — EPS-Growth + Leverage als Quality-Faktoren | Non-US validiert: Ergebnisse robust auf STOXX Europe 600"
related: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[ROIC-vs-WACC]], [[Non-US-Scoring]], [[DEFCON-System]], [[Analyse-Pipeline]]"
---

# Stock Picking with Machine Learning

**Originaltitel:** Stock picking with machine learning  
**Autoren:** [[Dominik Wolff]] · [[Fabian Echterling]]  
**Journal:** Journal of Forecasting (Wiley) | DOI: 10.1002/for.3021  
**Datenzeitraum:** Januar 1999 – März 2021 | S&P 500 (1164 historische Konstituenten) + STOXX Europe 600 (Robustheitscheck)  
**Originaldokument:** [[Stock picking with machine learning]] (raw/)

---

## Kernthese

ML-Modelle für Aktienauswahl übertreffen einen gleichgewichteten Benchmark signifikant. Einfache regularisierte Regressionsmodelle performen ähnlich wie komplexe Deep-Learning-Modelle. Die Ergebnisse sind auf den STOXX Europe 600 übertragbar.

---

## Methodik

- **Universum:** 1164 historische S&P500-Konstituenten · 1,3 Mio. Aktien-Wochen-Beobachtungen
- **Aufgabe:** Binäre Klassifikation — outperformt eine Aktie den Median-Return der Folgewoche?
- **Training:** Rolling 3-Jahres-Fenster, jährlich re-trainiert · Out-of-Sample: 2002–2021 (19 Jahre)
- **Modelle:** Ridge / LASSO / ENet / PCA / Random Forest / Boosting / DNN / LSTM / Ensemble

### Features (Panel A — Fundamental)

| Faktorgruppe | Metriken |
|---|---|
| **Profitability** | ROIC · FCF/EV · FCF-to-Equity · OCF/Market Cap · Operating Margin · Net Margin · Dividend Yield |
| **Quality** | EPS Growth · EPS Variability · Financial Leverage |
| **Value** | Book-to-Market |
| **Growth** | Asset Growth · Sales Growth · Employee Growth |
| **Size** | Market Cap |

### Features (Panel B — Technical)

Momentum (12M/6M/1M), Moving Averages (200D/100D/50D), Beta, Volatility, RSI, Bollinger Bands

---

## Kernergebnisse

### Performance (Portfolio Size 50, Out-of-Sample 2002–2021)

| Modell | Return p.a. | Sharpe | FF-6 Alpha p.a. |
|--------|------------|--------|----------------|
| S&P500 Market | 6.6% | 0.40 | — |
| Benchmark (1/N) | 11.1% | 0.57 | 5% |
| Ridge (bestes lineares) | 19.4% | 0.77 | 14%*** |
| **Ensemble (bestes gesamt)** | **20.8%** | **0.84** | **15%*** |

### Schlüsselbefunde

**B8 — Profitability-Faktor-Dominanz:**
ROIC, FCF/EV, Operating Margin und OCF/Market Cap sind konsistent top-ranked über alle ML-Architekturen. Profitability schlägt Value (Book-to-Market) in jedem Modell.

**B9 — Quality-Faktor-Stabilität:**
EPS Growth + Financial Leverage (Debt-Proxy) liefern stabile Outperformance-Signale. Je geringer die Financial Leverage, desto robuster das Signal.

**Einfachheit schlägt Komplexität:**
Regularisiertes Ridge (linear) ≈ Ensemble aus DNN/LSTM/RF. Kein statistisch signifikanter Unterschied. → Systematische Einfachheit ist produktiv.

**Non-US Robustheit:**
Ergebnisse auf STOXX Europe 600 übertragbar — Faktor-Hierarchie bleibt identisch. Europäische Aktien folgen denselben Profitability-Mustern.

---

## DEFCON-Implikation

| Befund | Block | Konsequenz |
|--------|-------|-----------|
| B8: ROIC top-ranked | Fundamentals — ROIC-vs-WACC | ROIC-Malus bei <WACC wissenschaftlich zwingend, nicht heuristisch |
| B8: FCF/EV primär | Fundamentals — FCF Yield | P/FCF als primäre Bewertungsmetrik bestätigt |
| B9: Low Leverage = Signal | Fundamentals — Bilanz | Debt/EBITDA-Scoring (0–3 Punkte) wissenschaftlich fundiert |
| B9: EPS Growth = Quality | Fundamentals — Bonus-Metriken | EPS Revision Momentum (+1 Bonus-Punkt) bestätigt |
| Non-US robust | Non-US-Scoring | DEFCON-Gewichtung auf ASML/RMS/SU übertragbar |

---

## Backlinks

- [[ROIC-vs-WACC]] — B8 validiert harten ROIC-Malus direkt
- [[FCF-Primacy]] — B8 bestätigt FCF als stärksten Einzel-Prädiktor
- [[5J-Fundamental-Fenster]] — Rolling-Window-Ansatz (3J Training) unterstützt Zeitfenster-Prinzip
- [[Non-US-Scoring]] — STOXX-Robustheit validiert Übertragbarkeit
- [[DEFCON-System]] — B8+B9 ergänzen wissenschaftliche Fundierung
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befunde B8 + B9
