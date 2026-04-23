---
title: "Value Investing: The Use of Historical Financial Statement Information"
date: 2000
type: source
subtype: academic-paper
tags: [defcon, f-score, quality-signal, earnings-quality, value-investing, fundamentals]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=249455
authors: "Joseph D. Piotroski (University of Chicago, Journal of Accounting Research 38, Supplement)"
status: processed
defcon_relevanz: "Fundamentals — Quality-Bonus: F-Score ≥7 → +2 Pt. Fundamentals-Bonus (Befund B12). Belegt Quality als PRÄDIKTOR, nicht nur Risiko-Signal."
related: "[[F-Score-Quality-Signal]], [[Buffett-Faktorlogik]], [[QMJ-Faktor]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]], [[FCF-Primacy]]"
---

# Piotroski F-Score (2000)

## Abstract (eigene Worte)
Joseph Piotroski zeigt, dass ein simpler 9-Punkte-Fundamentaldaten-Score (F-Score) die Rendite von Value-Aktien (High B/M) signifikant verbessert: Ein Portfolio aus Value-Aktien mit hohem F-Score (≥7) erzielt eine **+7,5% jährliche Überrendite** gegenüber dem Value-Durchschnitt. Der F-Score aggregiert 9 binäre Signale aus drei Bereichen: Profitabilität (4), Leverage/Liquidität (3), Operative Effizienz (2). Die Arbeit ist die empirische Grundlage für Quality-Screening und ein direkter Nachweis, dass Earnings Quality ein **eigenständiger Renditefaktor** ist — nicht nur ein Risiko-Korrektiv.

## Die 9 F-Score-Kriterien

**Profitabilität (4 Signale):**
1. Net Income positiv (1 Punkt)
2. Operating Cash Flow positiv (1 Punkt)
3. ROA gestiegen vs. Vorjahr (1 Punkt)
4. OCF > Net Income (= echte Cash-Earnings, kein Accrual-Trick) (1 Punkt)

**Leverage / Liquidität / Funding (3 Signale):**
5. Long-term Debt-to-Assets gefallen vs. Vorjahr (1 Punkt)
6. Current Ratio gestiegen vs. Vorjahr (1 Punkt)
7. Keine neuen Aktien emittiert (kein Dilutive Issuance) (1 Punkt)

**Operative Effizienz (2 Signale):**
8. Gross Margin gestiegen vs. Vorjahr (1 Punkt)
9. Asset Turnover gestiegen vs. Vorjahr (1 Punkt)

→ **Summe:** 0–9 Punkte. Piotroski definiert F-Score ≥ 7 als „hohe Qualität".

## Key Findings (DEFCON-gemappt)

- **High-F-Score Value (≥7) outperformen Low-F-Score (≤3) um +23% p.a.** — robust über 20-Jahres-Sample
- **F-Score separiert „echte Value" von „Value Traps"** — genau das, was unsere Moat+Fundamentals-Kombination heute leistet
- **Kriterium #4 (OCF > Net Income)** ist faktisch ein Anti-Accrual-Signal → komplementär zu [[Accruals-Anomalie-Sloan]]
- **Kriterium #8 (GM steigend)** validiert unsere GM-Trend-Regel (Moat-Block, aktuell ±1 Bonus)
- **Kriterium #9 (Asset Turnover)** = Operating Efficiency = fehlt in unserer Matrix vollständig

## DEFCON-Implikation

| Block | Auswirkung |
|-------|-----------|
| Fundamentals (50 Pt.) | Quality-Bonus operationalisierbar: F-Score ≥7 → +2 Pt. Bonus |
| Bilanz-Block (9 Pt.) | Kriterien 5+6 = bereits implementiert (Net Debt/EBITDA + Current Ratio) |
| Earnings Quality | Kriterium 4 (OCF > NI) ergänzt unsere Accrual Ratio |
| Moat-Block (20 Pt.) | Kriterium 8 (GM steigend) bestätigt unsere GM-Trend-Regel |

> **Operative Schlussfolgerung:** F-Score lässt sich in unter 5 Minuten pro Ticker aus defeatbeta-Daten berechnen. Die 9 Kriterien sind vollständig aus `get_stock_annual_income_statement` + `get_stock_annual_cash_flow` + `get_stock_annual_balance_sheet` ableitbar.

## Kalibrierung (Live-Test)

Geschätzte F-Scores der Satelliten (vor vollständiger Berechnung):

| Ticker | Erwarteter F-Score | Begründung |
|--------|-------------------|------------|
| AVGO | 8-9 | Alle Profitabilität + stabile Leverage + OCF>>NI |
| V | 8-9 | Klassischer High-Quality Compounder |
| MSFT | 5-6 | CapEx/OCF-Problem drückt #4 (OCF steigt nicht proportional) |
| TMO | 3-4 | Fallender ROA, fallender FCF, Akquisitionsschulden |

→ F-Score bestätigt intuitiv unsere bestehenden DEFCON-Scores — das ist Validation, nicht Neuerung.

## Backlinks
- [[F-Score-Quality-Signal]] — operative Konzeptseite
- [[Buffett-Faktorlogik]] — cheap+safe+quality; F-Score ist quality-Operationalisierung
- [[QMJ-Faktor]] — komplementäre Quality-Definition (AQR vs. Piotroski)
- [[Accruals-Anomalie-Sloan]] — F-Score-Kriterium #4 = Anti-Accrual-Signal
- [[DEFCON-System]] — Quality-Bonus erweitert Fundamentals-Block
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B12
