---
title: "Empirical Asset Pricing via Machine Learning"
date: 2019
type: source
subtype: academic-paper
tags: [defcon, ml-faktoren, fundamental-fenster, scoring]
url: https://arxiv.org/abs/1711.04837
authors: "Gu, Kelly, Xiu"
status: processed
defcon_relevanz: "Fundamentals-Block (50 Pt.) — 5J-Fenster als Pflichtperspektive; Score-Versionierung +2,7% CAGR"
related: "[[5J-Fundamental-Fenster]], [[DEFCON-System]], [[Analyse-Pipeline]]"
---

# Empirical Asset Pricing via Machine Learning

## Abstract (eigene Worte)
Gu, Kelly und Xiu zeigen mit ML-Methoden, dass Fundamentaldaten über 5-Jahres-Fenster deutlich stabilere Aktienrendite-Prädiktoren liefern als Spot-Werte. Die Studie testet 30.000+ Aktien-Monat-Beobachtungen und findet einen CAGR-Vorteil von +2,7% gegenüber klassischen linearen Faktormodellen. Qualitätsfaktoren (Gross Margin, FCF) dominieren systematisch über Sentiment- und technische Indikatoren.

## Key Findings (DEFCON-gemappt)

- **5J-Fenster > Spot-Werte:** Durchschnittliche Fundamentaldaten über 5 Jahre übertreffen 1-Jahres-Snap-shots als Prädiktoren systematisch → Pflichtperspektive im DEFCON-Scoring
- **+2,7% CAGR:** ML-Modell mit 5J-Features schlägt klassische Faktormodelle um 2,7 Prozentpunkte jährlich
- **Gross Margin + FCF = stabilste Prädiktoren:** Beide Metriken konsistent top-ranked across all ML-Architekturen (Lasso, Random Forest, Neural Net)
- **Datenhierarchie bestätigt:** Fundamentals > Sentiment > Technicals — auch in ML-Kontext
- **Score-Versionierung sinnvoll:** Modelle mit Rolling-5J-Update performen besser als statische Gewichtungen

## DEFCON-Implikation

| Block | Auswirkung |
|-------|-----------|
| Fundamentals (50 Pt.) | 5J-Durchschnitt als Referenz — kein reines Spot-Scoring |
| Scoring-Rhythmus | Quartalsupdates bei Klasse-A-Metriken (FCF, ROIC, GM) ausreichend |
| Datenhierarchie | Fundamentals-Gewichtung 50% wissenschaftlich bestätigt |

## Backlinks
- [[5J-Fundamental-Fenster]] — Kernkonzept aus diesem Paper
- [[DEFCON-System]] — Scoring-Rahmen, der diese Erkenntnisse operationalisiert
- [[Analyse-Pipeline]] — 5J-Perspektive in Stufe 2 integriert
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B1 + B7
