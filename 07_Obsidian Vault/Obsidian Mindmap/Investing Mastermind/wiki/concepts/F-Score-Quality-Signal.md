---
title: "F-Score als Quality-Signal (Piotroski)"
type: concept
tags: [defcon, f-score, quality-bonus, fundamentals, piotroski, earnings-quality]
source: "[[Piotroski-2000]]"
related: "[[Accruals-Anomalie-Sloan]], [[Gross-Profitability-Premium]], [[Buffett-Faktorlogik]], [[QMJ-Faktor]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]], [[FCF-Primacy]]"
defcon_block: "Fundamentals (Quality-Bonus +2 Pt.)"
operative_regel: "F-Score ≥7 → +2 Pt. Fundamentals-Bonus. F-Score 4–6 neutral. F-Score ≤3 → -1 Pt. Malus (niedrige Fundamentalqualität)."
aliases:
  - "Piotroski-F-Score"

---

# F-Score als Quality-Signal

## Definition
Der **Piotroski F-Score** ist ein 9-Punkte-Fundamentaldaten-Score, der in drei Dimensionen (Profitabilität, Leverage/Liquidität, Operative Effizienz) die Qualität einer Bilanz quantifiziert. Jedes Kriterium ist binär (0 oder 1). Die Summe 0–9 signalisiert die operative Verfassung eines Unternehmens zu einem Bilanzstichtag.

## Die 9 Kriterien (Pflichtberechnung)

**Profitabilität (4 Punkte):**
1. Net Income > 0 (aktuelles Jahr)
2. Operating Cash Flow > 0 (aktuelles Jahr)
3. ROA > ROA Vorjahr (Verbesserung)
4. OCF > Net Income (Anti-Accrual-Test, vgl. [[Accruals-Anomalie-Sloan]])

**Leverage / Liquidität / Funding (3 Punkte):**
5. Long-term Debt/Assets < Vorjahr (Entschuldung)
6. Current Ratio > Vorjahr (Liquiditätsverbesserung)
7. Keine Neuemission von Aktien (keine Dilution)

**Operative Effizienz (2 Punkte):**
8. Gross Margin > Vorjahr (Pricing Power, vgl. [[Moat-Taxonomie-Morningstar]])
9. Asset Turnover > Vorjahr (Effizienzsteigerung)

## Scoring-Integration DEFCON

| F-Score | Interpretation | DEFCON-Wirkung |
|---------|---------------|-----------------|
| 8–9 | Exzellente Fundamentalqualität | +2 Pt. Bonus Fundamentals |
| 7 | Hohe Qualität (Piotroski-Schwelle) | +1 Pt. Bonus Fundamentals |
| 4–6 | Durchschnittlich | kein Effekt |
| 0–3 | Schwache Qualität (Junk-Zone) | -1 Pt. Malus Fundamentals |

**Cap:** Bonus zählt gegen Fundamentals-Obergrenze 50 Pt. (keine Überschreitung).

## Verhältnis zu anderen Scoring-Regeln

Der F-Score ist komplementär zu bestehenden Regeln, **nicht redundant**:

| Regel | Was sie misst | Überschneidung |
|-------|--------------|----------------|
| Bilanz-Block (9 Pt.) | Absolute Leverage + Liquidität | Kriterien 5+6 (Veränderung, nicht Level) — getrennt |
| Accrual Ratio Malus | Accrual-Level kontinuierlich | Kriterium 4 (binär) — verwandt, aber granularer |
| GM-Trend Moat-Bonus | GM-Veränderung 3 Jahre | Kriterium 8 (1 Jahr) — kürzere Zeitspanne, getrennt |
| ROIC vs WACC | Return vs. Capital Cost | Kriterium 3 (ROA-Trend) — komplementär, verschiedene Ebenen |

## Datenabruf-Rezept

Alle 9 Kriterien sind in <5 Minuten pro Ticker berechenbar:

```
get_stock_annual_income_statement (2 Jahre) → NI, Revenue, COGS → Kriterien 1, 8
get_stock_annual_cash_flow (2 Jahre)        → OCF → Kriterien 2, 4
get_stock_annual_balance_sheet (2 Jahre)    → Assets, LT Debt, Current Ratio, Shares Outstanding → Kriterien 3, 5, 6, 7, 9
```

## Kalibrierung (Erwartungswerte Satelliten)

| Ticker | Erwarteter F-Score | DEFCON-Bonus |
|--------|-------------------|--------------|
| AVGO | 8–9 | +2 |
| V | 8–9 | +2 |
| VEEV | 7–8 | +1 bis +2 |
| COST | 7–8 | +1 bis +2 |
| BRK.B | 6–7 | 0 bis +1 (Holdings strukturell schwächer im Score) |
| TMO | 3–4 | -1 (fallender FCF, Akquisitionsschulden) |
| MSFT | 5–6 | 0 (CapEx-Probleme drücken #4) |

## Backlinks
- [[Piotroski-2000]] — Primärquelle
- [[Accruals-Anomalie-Sloan]] — Kriterium #4 basiert auf Sloans Anomalie
- [[Gross-Profitability-Premium]] — Kriterium #8 parallel zu Novy-Marx
- [[QMJ-Faktor]] — Quality-Definition (AQR) vs. F-Score (Piotroski)
- [[Buffett-Faktorlogik]] — F-Score operationalisiert den „quality"-Teil
- [[DEFCON-System]] — neuer Quality-Bonus in Fundamentals-Block
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B12

## Aghassi 2023 Context

F-Score (Piotroski 2000) ist frühe Operationalisierung des Quality-Faktors. Aghassi 2023 validiert Quality akademisch, aber:
- Piotroski-spezifische 9-Signale sind NICHT in DEFCON v3.7 integriert (Session 2 verworfen)
- DEFCON-Quality-Logik nutzt eigene Metrik-Kombination (ROIC>WACC + Moat)
- F-Score bleibt Referenz-Konzept, kein Live-Score-Input

→ [[Aghassi-2023-Fact-Fiction]], [[Piotroski-2000]]
