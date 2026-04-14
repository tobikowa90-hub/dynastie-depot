---
title: "Empirical Asset Pricing via Machine Learning (Review of Financial Studies)"
date: 2020
type: source
subtype: academic-paper
tags: [defcon, fcf-primacy, forward-pe, earnings-quality, faktor-kalibrierung]
url: https://onlinelibrary.wiley.com/doi/full/10.1002/for.3021
authors: "Gu, Kelly, Xiu"
status: processed
defcon_relevanz: "Faktor-Kalibrierung — PFLICHT: trailing P/E verliert Vorhersagekraft; forward P/E bleibt valide"
related: "[[FCF-Primacy]], [[DEFCON-System]], [[CapEx-FLAG]], [[Analyse-Pipeline]]"
---

# Empirical Asset Pricing via Machine Learning (RFS 2020)

## Abstract (eigene Worte)
Die publizierte RFS-Version von Gu/Kelly/Xiu (2020) validiert, dass FCF-basierte Metriken und Gross Margin die stabilsten Rendite-Prädiktoren sind — trailing P/E hingegen verliert nach 12-monatigem Horizont signifikant an Vorhersagekraft. Forward P/E bleibt valide, weil es zukunftsgerichtete Earnings-Erwartungen abbildet. Earnings-Quality-Faktoren übertreffen Value-Multiples in Prädiktionsgenauigkeit.

## Key Findings (DEFCON-gemappt)

- **PFLICHT: Trailing P/E verliert Vorhersagekraft** — konsistent schwach nach 12 Monaten in allen getesteten ML-Architekturen; nicht als primärer Bewertungsanker verwenden
- **Forward P/E bleibt valide** — zukunftsgerichtete Earnings-Schätzungen haben weiterhin Prädiktionskraft; weiterhin als DEFCON-Metrik einsetzen
- **FCF + Gross Margin = stabilste Prädiktoren** — beide top-2 Features in Random Forest und Neural Network
- **Earnings-Quality > Value** — Accrual Ratio, FCF-Qualität, GM-Trend übertreffen klassische Value-Multiples (P/B, P/E)
- **Feature Importance:** Reihenfolge: FCF-Yield → GM → Accrual Ratio → Forward P/E → P/FCF (trailing P/E nicht in Top 10)

## DEFCON-Implikation

| Block | Auswirkung |
|-------|-----------|
| Fundamentals — Fwd P/E (8 Pt.) | Weiterhin einsetzen — valider Prädiktor ✅ |
| Fundamentals — P/FCF (8 Pt.) | Primäranker bestätigt ✅ |
| Fundamentals — trailing P/E | **De-priorisieren** — Vorhersagekraft verloren ⚠️ |
| Bonus-Metriken | Accrual Ratio, GM-Trend aufgewertet |

> **PFLICHT-Dokumentation (wörtlich):** *"Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide."*
> Diese Regel gilt in jeder DEFCON-Analyse. Fwd P/E ist Primärmetrik; trailing P/E höchstens als Kontext.

## Backlinks
- [[FCF-Primacy]] — Kernkonzept aus diesem Paper
- [[DEFCON-System]] — Faktor-Gewichtungen angepasst
- [[CapEx-FLAG]] — FCF-Qualität zentral für FLAG-Logik
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B2 + B3
