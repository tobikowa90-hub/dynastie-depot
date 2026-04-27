---
title: "Revisiting Quality Investing"
date: 2021
type: source
subtype: industry-research
tags: [quality-factor, multidimensional, profitability, earnings-quality, safety, investment, k-means, source-only]
url: https://research-center.amundi.com/article/revisiting-quality-investing
venue: "Amundi Working Paper 113-2021, June 2021. Document for professional clients"
authors: "Frédéric Lepetit, Amina Cherief, Yannick Ly, Takaya Sekine (alle Quantitative Research, Amundi)"
status: processed
defcon_relevanz: "SOURCE-ONLY. Practitioner-Validation der QMJ-Quality-Definition über ein anderes 18J-Sample (developed markets, large/mid-caps post-2003). Vier Pillars: **Profitability, Earnings Quality, Safety, Investment** — leicht verschoben gegenüber AFP-QMJ (Growth → Investment, Payout → Earnings Quality). Long-Only-Outperformance +2,8% p.a., Information Ratio 0,81, sehr konsistent post-GFC 2008. Drei Befunde sind operativ relevant: (1) Eurozone-Region zeigt Eurozone-spezifische Sektor-Bias (Sector-Neutral-Konstruktion empfohlen); (2) Safety-Pillar wird in Crisis-Phasen (GFC, Covid) entscheidend; (3) Pillars sind weak-correlated → komplementär. Kein active-scoring — DEFCON nutzt Quality dekomponiert (siehe QMJ + Wolff-Echterling-2023)."
sources: []
related:
  - "[[QMJ-Faktor]]"
  - "[[Asness-Frazzini-Pedersen-2013-QMJ]]"
  - "[[Wolff-Echterling-2023]]"
  - "[[F-Score-Quality-Signal]]"
  - "[[Non-US-Scoring]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/2021.06 - Revisiting Quality Investing - EN.pdf"
aliases:
  - "Amundi Quality 2021"
  - "Lepetit Cherief Ly Sekine 2021"
  - "Revisiting Quality Investing"
---

# Lepetit, Cherief, Ly & Sekine (2021) — Amundi Quality Working Paper

## Abstract (eigene Worte)

Die Amundi-Quantitative-Research-Gruppe testet einen 4-Pillar-Quality-Faktor (Profitability, Earnings Quality, Safety, Investment) über 18 Jahre auf einem globalen Developed-Markets-Universum (Large + Mid-Caps). Long-Short-Framework liefert statistisch signifikante Alpha gegen Carhart-Faktoren (Market/SMB/HML/UMD); Long-Only outperformt Benchmark **+2,8% p.a. mit Information Ratio 0,81**, sehr konsistent post-GFC 2008.

Wichtige praktische Befunde:
- **Pillars sind weak-correlated** → komplementäre Information; Composite ist robuster als Single-Pillar
- **Eurozone braucht Sector-Neutral-Construction** — Region zeigt strukturelle Sektor-Biases die Quality-Signal verzerren
- **Safety wird in Krisen entscheidend** (GFC, Covid-19 Drawdown-Resilienz)
- **Investment-Pillar** (negative Korrelation zu Asset-Growth) ist eigenständig — überlappt nicht vollständig mit Profitability oder Safety
- **K-Means-Clustering** als Portfolio-Construction-Methode (Pillar-aggregiert) verbessert Performance ohne Risk-Drift

Methodisch interessant: Pillar-Definition divergiert zu QMJ (Asness/Frazzini/Pedersen 2013):

| QMJ-Pillar (AFP 2013) | Amundi-Pillar (2021) |
|---|---|
| Profitability | Profitability |
| Growth | Investment (negative) |
| Safety | Safety |
| Payout | Earnings Quality |

→ Ein Practitioner-Befund: Earnings Quality (Accruals-Ratio, ähnlich Sloan 1996) ist robusterer Pillar als Payout (das mit Buyback-Signal-Inflation Issues hat).

## DEFCON-Konsequenzen (ohne Scoring-Change)

- **Validation**, dass Multi-Pillar-Quality nicht-redundant arbeitet — DEFCON's Dekomposition (ROIC/FCF/OpM/Bilanz) repliziert Pillar-Logik in 4 Dimensionen.
- **Sector-Neutral-Hinweis** für Non-US-Satelliten (ASML/SU/RMS): bei Eurozone-Konstruktion strukturelle Sektor-Verzerrung möglich. **Aktuell nicht im Score** — Satelliten-Universum ist klein (3 Non-US), Sector-Neutralität wäre Over-Engineering. Watch-Item.
- **Crisis-Safety-Befund** validiert Bilanz-Block-Pflicht (Net Debt/EBITDA + Current Ratio); APH-FLAG-Begründung post-Liberation-Day passt direkt: in Krisen wird Bilanz-Resilienz bewertungsrelevant.
- **Cluster-Methodik** (K-Means) ist outside-DEFCON-Scope — interessantes Forschungs-Item für 2027+ falls Backtest-Engine voll automatisiert wird.

## Backlinks

- [[QMJ-Faktor]] — komplementäre Primärquelle (4-Pillars-Framing-Anker)
- [[Asness-Frazzini-Pedersen-2013-QMJ]] — kanonische Quality-Definition
- [[Wolff-Echterling-2023]] — STOXX-600-Validation
- [[F-Score-Quality-Signal]] — diskrete Implementierung
- [[Non-US-Scoring]] — Eurozone-Sector-Neutral-Hinweis relevant für ASML/SU/RMS
- [[DEFCON-System]] — Fundamentals-Block validiert
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle
- [[Frédéric Lepetit]], [[Amina Cherief]], [[Yannick Ly]], [[Takaya Sekine]] — Author-Entities
