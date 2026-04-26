---
title: "A Five-Factor Asset Pricing Model"
date: 2015
type: source
subtype: academic-paper
tags: [factor-model, asset-pricing, profitability-factor, investment-factor, hml-redundancy, fama-french, source-only]
url: https://ssrn.com/abstract=2287202
venue: "Journal of Financial Economics 116(1), 2015, 1-22. Original SSRN draft June 2013, this draft September 2014"
authors: "Eugene F. Fama (University of Chicago Booth), Kenneth R. French (Dartmouth Tuck)"
status: processed
defcon_relevanz: "SOURCE-ONLY. Erweitert FF-3-Faktor-Modell (Mkt/SMB/HML) um Profitability (RMW) und Investment (CMA) Faktoren. **Zentraler Befund:** mit RMW + CMA wird HML (Value-Faktor) statistisch redundant für Cross-Section-Erklärung. Operative Konsequenzen: (1) DEFCON's Profitability+Investment-Fokus (ROIC, OpM, CapEx-FLAG) ist methodisch ankerfest — FF zeigen, dass diese Dimensionen das Pricing-Cross-Section dominieren. (2) Trailing-P/E-De-Priorisierung (B2) ist FF-konsistent — Value als isolierter Faktor verliert Erklärungskraft wenn Profitability + Investment kontrolliert werden. (3) **Forward-Looking-Variablen** (Mt-Anteil aus dividend-discount-Equation) ankern unsere Fwd-P/E + ROIC-Forward-Logik. Kein Scoring-Change, aber strukturelle Validation."
related: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Hou-Xue-Zhang-q-Factor]], [[Novy-Marx-2013]], [[Fama-French-2006-Profitability]], [[arXiv-1711.04837]], [[Gu-Kelly-Xiu-2020]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/fama & french.pdf"
aliases:
  - "Fama French 2015 Five Factor"
  - "FF Five Factor Model"
  - "FF-5"
---

# Fama & French (2015) — Five-Factor Asset Pricing Model

## Abstract (eigene Worte)

Fama und French erweitern ihr 3-Faktor-Modell (Market, SMB, HML) um zwei Faktoren, die aus der Dividend-Discount-Valuation-Equation natürlich folgen:

1. **RMW** (Robust-Minus-Weak Profitability) — Operating Profitability nach Novy-Marx (2013)
2. **CMA** (Conservative-Minus-Aggressive Investment) — Asset-Growth-Faktor nach Aharoni/Grundy/Zeng (2013)

Befunde (1963-2013, NYSE/AMEX/NASDAQ):

1. **5-Faktor outperformt 3-Faktor** in Erklärung der Size × B/M × Profitability × Investment 5×5×5×5-Cross-Sections
2. **HML wird redundant** in Anwesenheit von RMW + CMA — alle HML-Erklärungskraft wird durch Profitability + Investment absorbiert
3. **Faktor-Definitionen sind robust** — Modell-Performance ändert sich nicht wesentlich wenn Faktoren anders definiert werden
4. **Achilles-Ferse:** Microcaps mit hoher Investment-Aktivität trotz niedriger Profitability werden vom 5-Faktor-Modell schlecht gepricet — das ist der "Anti-Quality"-Pattern, der durchgehend in Anomalie-Studien auftaucht

Theoretische Verankerung:
```
Mt/Bt = Σ E(Yt+τ − dBt+τ) / (1+r)^τ / Bt
```
→ Bei kontrollierter B/M und kontrolliertem Investment haben Firmen mit höheren expected Earnings höhere expected Returns. Bei kontrollierter B/M und kontrolliertem Profitability haben Firmen mit höherem Investment niedrigere expected Returns.

## DEFCON-Konsequenzen

| FF-2015 Befund | DEFCON-Validation |
|---|---|
| Profitability-Faktor (RMW) | ROIC + OpM bereits Score-Element (Fundamentals-Block) |
| Investment-Faktor (CMA) | CapEx-FLAG (DIE heilige Regel) und ROIC-spread-vs-CapEx-Quality bereits operativ |
| HML-Redundanz | Trailing-P/E-De-Priorisierung in v3.5+ konsistent (Befund B2) |
| Anti-Quality-Trap (high-Inv + low-Prof) | TMO-FLAG-Pattern und MSFT-CapEx-FLAG = exakt dieser Trap-Detector |
| Forward-Looking Variables | Fwd-P/E + Forward-FCF-Yield in DEFCON sind FF-Mt-Decomposition-konform |

## Komplementarität zu Hou/Xue/Zhang q-Factor

Hou/Xue/Zhang (2015, [[Hou-Xue-Zhang-q-Factor]]) propose ein **paralleles 4-Faktor-Modell** (Market, ME, I/A, ROE), motiviert aus q-Theory of Investment statt Dividend-Discount. Die Faktoren überschneiden sich stark mit FF-5 (RMW≈ROE, CMA≈I/A) — **konvergente Evidenz**, dass Profitability + Investment die fundamentalen Cross-Section-Treiber sind, unabhängig vom Theorierahmen.

## Backlinks

- [[5J-Fundamental-Fenster]] — Fundamental-Trendperspektive
- [[FCF-Primacy]] — Fwd-P/E + FCF-Yield-Logik
- [[Hou-Xue-Zhang-q-Factor]] — paralleles 4-Faktor-Modell, konvergente Evidenz
- [[Novy-Marx-2013]] — Profitability-Pillar Primärquelle (RMW-Fundament)
- [[Fama-French-2006-Profitability]] — Working-Paper-Vorgänger (mit gefoldeter F/F 2004 "Profitability, Growth, Average Returns" Draft-Variante)
- [[arXiv-1711.04837]] — Gu/Kelly/Xiu ML-Validation der Dimension-Hierarchie
- [[Gu-Kelly-Xiu-2020]] — RFS 2020 Aktualisierung
- [[DEFCON-System]] — Block-Gewichtung 50 Pt. Fundamentals validated
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle
- [[Eugene F. Fama]], [[Kenneth R. French]] — Author-Entities
