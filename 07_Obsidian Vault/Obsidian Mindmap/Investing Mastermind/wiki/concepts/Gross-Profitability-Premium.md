---
title: "Gross Profitability Premium (Novy-Marx)"
type: concept
tags: [defcon, gp-premium, fundamentals, novy-marx, profitability-faktor, gross-margin]
source: "[[Novy-Marx-2013]]"
related: "[[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[F-Score-Quality-Signal]], [[QMJ-Faktor]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]]"
defcon_block: "Fundamentals (GP/TA als 2-Pt.-Metrik) + Moat (GM-Trend-Bonus bleibt)"
operative_regel: "GP/TA > 0,33 = 2 Pt. | 0,20–0,33 = 1 Pt. | <0,20 = 0 Pt. Sonderregel COST: Membership-Yield-Proxy analog zu bestehender Screener-Exception."
---

# Gross Profitability Premium

## Definition
Der **Gross Profitability Premium** beschreibt die empirische Beobachtung, dass Unternehmen mit hoher Gross-Profits-to-Total-Assets-Ratio (GP/TA) systematisch höhere Renditen erzielen als Unternehmen mit niedriger GP/TA — und zwar mit **ähnlicher Vorhersagekraft wie Book-to-Market** (Value-Faktor). Die Arbeit etablierte Gross Profitability als eigenständigen Renditefaktor, der später in Fama/French's Five-Factor-Modell (2015) als Profitability-Faktor aufgenommen wurde.

## Kern-Formel

```
GP/TA = (Revenue − COGS) / Total Assets
```

**Warum nicht Net Income oder EBITDA?**
- **Net Income** wird durch SG&A, R&D, Einmaleffekte, Steueroptimierung verzerrt
- **EBITDA** ignoriert Abschreibungen (= reale CapEx-Kosten)
- **Gross Profit** ist der „ökonomischste" Profitabilitätsindikator — direkt am Kerngeschäft

## Die zentrale Einsicht

Hohes GP/TA + hohe SG&A = Investment in Zukunftswachstum (gut).
Hohes Net Income durch Kürzung von SG&A/R&D = kurzfristig attraktiv, langfristig Moat-Erosion (schlecht).

→ GP/TA unterscheidet **echte Profitabilität** von **buchhalterisch optimierter Profitabilität**.

## Scoring-Integration DEFCON

| GP/TA | Score (max. 2 Pt.) | Interpretation |
|-------|--------------------|----|
| > 0,33 | 2 | Top-Profitability (Software/Zahlungs-Infrastruktur) |
| 0,25 – 0,33 | 1,5 | Hoch (Branchenführer) |
| 0,20 – 0,25 | 1 | Durchschnittlich (gesunde Industrie) |
| 0,10 – 0,20 | 0,5 | Unterdurchschnittlich |
| < 0,10 | 0 | Strukturell niedrig (Retail-Commodity) |

**Integration:** GP/TA wird als eigenständige Fundamentals-Metrik (2 Pt.) in den 50-Punkte-Block aufgenommen. GM-Trend im Moat-Block bleibt unverändert — misst Veränderung, nicht Level.

## Verhältnis zu anderen Metriken

| Regel | Misst | Überschneidung mit GP/TA |
|-------|-------|--------------------------|
| GM-Trend (Moat-Block) | Δ GM über 3 Jahre | Gering: Level vs. Trend |
| ROIC vs. WACC | Return auf investiertes Kapital | Mittel: beide Profitabilität, aber ROIC = nach-SG&A |
| FCF Yield | Cash-Yield auf Marktkapitalisierung | Gering: GP/TA operativ, FCF Yield bewertungsnormalisiert |
| Net Income Margin | Nettomarge | Hoch redundant, aber verzerrt — GP/TA besser |

## COST-Sonderregel

Costco hat GP/TA ~0,06 (strukturell niedrig durch Membership-Geschäftsmodell). Analog zur bestehenden COST-Screener-Exception (ROIC 5,6% GAAP ≠ Membership-Yield 15,2%):

**COST-Proxy:** Membership-Fee-Recovery als ökonomisches GP
- Membership Fees FY25: $5,3B
- Operative Kosten: variieren
- Fee-Recovery-Ratio: Membership-Yield 15,2% > WACC 12,3% → Screener-Exception bleibt aktiv

→ **GP/TA ist für Membership-Modelle kein valider Indikator** — Exception dokumentieren, nicht mechanisch anwenden.

## Kalibrierung Satelliten (Erwartungswerte)

| Ticker | Erwartete GP/TA | Score |
|--------|-----------------|-------|
| V | 0,60–0,70 | 2,0 (Top) |
| AVGO | 0,50–0,60 | 2,0 (Top) |
| VEEV | 0,45–0,55 | 2,0 (Software-Profitabilität) |
| RMS | 0,40–0,50 | 2,0 (Luxury-Margen) |
| ASML | 0,30–0,40 | 1,5 (Hardware-Zyklus) |
| MSFT | 0,30–0,40 | 1,5 (Cloud-CapEx drückt Assets hoch) |
| BRK.B | 0,10–0,15 | 0,5 (Holdings-Verzerrung) |
| COST | 0,05–0,07 | Exception (Membership-Proxy) |

→ Die Reihenfolge validiert unsere intuitive Qualitätsordnung.

## Historische Evidenz
- **Novy-Marx (2013):** +0,31% monatliche Outperformance (Top- vs. Bottom-Dezil)
- **Fama/French (2015):** Profitability als 4. Faktor im Five-Factor-Modell aufgenommen
- **AQR (Buffett's Alpha 2018):** Profitability-Dimension in QMJ direkt abgeleitet aus Novy-Marx

## Backlinks
- [[Novy-Marx-2013]] — Primärquelle
- [[FCF-Primacy]] — komplementäre Fundamentals-Hierarchie
- [[Moat-Taxonomie-Morningstar]] — Gross Margin als Moat-Persistenz-Signal
- [[F-Score-Quality-Signal]] — Piotroski-Kriterium #8 (GM steigend) parallel
- [[QMJ-Faktor]] — Gross Profitability = Profitabilitäts-Dimension in QMJ
- [[DEFCON-System]] — neue Fundamentals-Metrik (2 Pt.)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B13
