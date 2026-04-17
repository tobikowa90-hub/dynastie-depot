---
title: "Accruals-Anomalie (Sloan 1996)"
type: concept
tags: [defcon, accruals, earnings-quality, sloan, anomaly, fundamentals, cash-flow]
source: "[[Sloan-1996]]"
related: "[[F-Score-Quality-Signal]], [[Gross-Profitability-Premium]], [[FCF-Primacy]], [[QMJ-Faktor]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]]"
defcon_block: "Fundamentals (Accrual Ratio Malus — unverändert, wissenschaftlich fundiert)"
operative_regel: "Accrual Ratio < 5% kein Effekt | 5–10% -1 Pt. | >10% -2 Pt. Malus. v3.6-Erweiterung: <3% → +2 Pt. Bonus (Piotroski-Parallelität)."
---

# Accruals-Anomalie (Sloan)

## Definition
Die **Accruals-Anomalie** ist die empirische Beobachtung, dass Aktienmärkte die Persistenz-Unterschiede zwischen Cash-Earnings und Accrual-Earnings unterschätzen. Firmen mit hohen Accruals (Gewinn > Cash Flow) liefern systematisch schwächere zukünftige Earnings als erwartet → ihre Kurse fallen. Firmen mit niedrigen Accruals (Cash Flow ≥ Gewinn) überraschen positiv → ihre Kurse steigen. Der Markt preist diese Asymmetrie nicht korrekt ein, trotz Bekanntheit seit 1996.

## Kern-Formel

```
Accruals = Net Income − Operating Cash Flow
Accrual Ratio = Accruals / Total Assets (TTM oder 5-Jahres-Durchschnitt)
```

**Interpretation:**

| Vorzeichen | Bedeutung | Prognose |
|-----------|-----------|----------|
| Accruals > 0 (NI > OCF) | Gewinn durch nicht-cash-wirksame Buchungen gestützt (Forderungen, Inventar, Abschreibungs-Timing) | Schwache künftige Earnings |
| Accruals ≈ 0 | Gewinn = Cash | Neutral |
| Accruals < 0 (OCF > NI) | Cash-Generation stärker als Gewinnausweis (konservative Rechnungslegung) | Starke künftige Earnings |

## Scoring-Integration DEFCON (Status quo)

Die bestehende Accrual Ratio in der DEFCON-Matrix ist **wissenschaftlich korrekt kalibriert**:

| Accrual Ratio | Sloan-Dezil | DEFCON-Wirkung |
|---------------|-------------|----------------|
| < 5% | Bottom 30% (Low-Accrual, gut) | kein Abzug |
| 5 – 10% | Middle | -1 Punkt |
| > 10% | Top 20% (High-Accrual, schlecht) | -2 Punkte |

**Sloan-Validation:** Bottom-Dezil outperformt Top-Dezil um +10,4% p.a. → unsere Schwelle <5% fängt genau diese Outperformer.

## v3.6-Erweiterung: Bonus für Low-Accrual

Piotroski (2000) operationalisiert Sloan's Anomalie als binäres F-Score-Kriterium #4 (OCF > NI = 1 Punkt). In unserem System wäre eine Erweiterung logisch:

| Accrual Ratio | v3.5 (aktuell) | v3.6 (vorgeschlagen) |
|---------------|----------------|----------------------|
| < 3% | 0 | **+2 Pt. Bonus** (Low-Accrual-Champion) |
| 3 – 5% | 0 | +1 Pt. Bonus |
| 5 – 10% | -1 | -1 Pt. Malus (unverändert) |
| > 10% | -2 | -2 Pt. Malus (unverändert) |

**Begründung:** Quality ist nicht nur Risiko-Korrektiv, sondern eigenständiger Renditefaktor. Aktuelle Malus-only-Struktur nutzt nur die halbe wissenschaftliche Evidenz.

## Verhältnis zu Piotroski F-Score

| Konzept | Granularität | DEFCON-Integration |
|---------|--------------|--------------------|
| Sloan Accrual Ratio | Kontinuierlich (Prozentwert) | Fundamentals-Malus/Bonus direkt |
| Piotroski F-Score #4 | Binär (OCF > NI: 0/1) | Teil des F-Score-Bonus (+2 Pt. bei F-Score ≥7) |

→ **Beide gleichzeitig anwenden ist keine Doppelzählung:** Sloan misst Intensität, Piotroski aggregiert mit anderen Qualitätsfaktoren. Ein Ticker kann niedrige Accruals haben UND F-Score 9 erreichen — beide Punkte sind verdient.

## Kalibrierung (Erwartungswerte Satelliten)

| Ticker | Accrual Ratio TTM | Sloan-Dezil | v3.5-Effekt | v3.6-Effekt |
|--------|-------------------|-------------|-------------|-------------|
| AVGO | ~2% | Bottom (top 10%) | 0 | +2 Bonus |
| V | ~1% | Bottom (top 10%) | 0 | +2 Bonus |
| VEEV | ~2% | Bottom | 0 | +2 Bonus |
| COST | ~3% | Bottom | 0 | +1 Bonus |
| BRK.B | ~4% | Lower-middle | 0 | +1 Bonus |
| MSFT | ~6% | Middle | -1 | -1 |
| TMO | ~9% | Upper-middle | -1 | -1 |
| APH | ~8% | Middle | -1 | -1 |

## Historische Evidenz

- **Sloan (1996):** +10,4% p.a. Long-Short-Spread (Bottom vs. Top Accrual-Dezil)
- **Replikationen (Richardson et al. 2005, Hirshleifer et al. 2004):** Anomalie persistiert, robust über 30+ Jahre
- **Dechow & Dichev (2002):** Accrual-Qualität als eigenständiger Risikofaktor bestätigt

## Backlinks
- [[Sloan-1996]] — Primärquelle
- [[F-Score-Quality-Signal]] — Piotroski #4 als binäres Sloan-Derivat
- [[Gross-Profitability-Premium]] — parallele Fundamentals-Anomalie
- [[FCF-Primacy]] — OCF > NI als Cash-Primacy
- [[QMJ-Faktor]] — Accrual-Qualität = Quality-Dimension in AQR-QMJ
- [[DEFCON-System]] — Accrual Ratio wissenschaftlich fundiert, v3.6-Bonus-Erweiterung
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B14
