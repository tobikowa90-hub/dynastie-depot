---
title: "Competitive Advantage Period (CAP)"
type: concept
tags: [defcon, moat, value-creation, sustainability, cap, mauboussin, dcf, design-context]
created: 2026-04-26
updated: 2026-06-09
sources: [Mauboussin-Callahan-2024-Measuring-Moat]
related: [Wissenschaftliche-Fundierung-DEFCON, Moat-Taxonomie-Morningstar, ROIC-vs-WACC, DEFCON-System, Buffett-Faktorlogik, Morningstar-Wide-Moat]
wissenschaftlicher_anker: "Mauboussin & Callahan (2024) 'Measuring the Moat' 3. Auflage, Morgan Stanley Counterpoint Global Insights — CAP als zweite Dimension der Value Creation neben ROIC-WACC-Spread; Morningstar-Wide-Moat ≈ CAP >20J, Narrow ≈ 10-20J, None = transient."
konfidenzstufe: industry-research
defcon_block: "Sprachregel für DEFCON ≥ 80 + !CAPEX-FCF-ANALYSIS — KEIN Score-Element (Estimation passt nicht in 4-Min-Routine)"
operative_regel: "CAP-Estimation in Bull/Bear-DCF-Szenarien (capex-fcf-template.md Sheet 2) als theoretische Begründung für Terminal-Value-Annahme; Briefing-Argument für Buy-and-Hold-32J-Rationale."
aliases:
  - "CAP"
  - "Competitive Advantage Period"
  - "Mauboussin CAP"
---

# Competitive Advantage Period (CAP)

> Mauboussin & Callahan (2024, 3. Auflage „Measuring the Moat"): Value Creation hat zwei Dimensionen — *Magnitude* (ROIC-WACC-Spread × Investment-Größe) und *Sustainability* (CAP = Zeitraum, in dem das Unternehmen ROIC > WACC halten kann). Die meisten Moat-Diskussionen vernachlässigen die zeitliche Dimension; CAP ist der Anker für Buy-and-Hold-Argumente.

## Definition

**Competitive Advantage Period (CAP)** = die erwartete Zeit, in der ein Unternehmen ROIC > WACC halten kann, bevor Wettbewerb, Disruption oder Regulierung den Spread auf das Marktniveau drücken. CAP ist die zentrale Variable in DCF-Modellen, weil sie die Terminal-Value-Annahme bestimmt.

```
Aggregate Value Creation = ROIC-WACC-Spread × Reinvestment-Volume × CAP
```

## CAP-Mapping zur Morningstar-Moat-Taxonomie

| Morningstar-Moat | Erwartete CAP | Operative Implikation |
|---|---|---|
| **Wide Moat** | >20 Jahre | Buy-and-Hold-Hauptkandidat; Terminal-Value mit langfristigem Spread |
| **Narrow Moat** | 10-20 Jahre | Watchliste; Terminal-Value mit reduzierendem Spread |
| **No Moat** | <10 Jahre (transient) | Kein Dynastie-Depot-Kandidat; Terminal-Value = Marktdurchschnitt |

**Beobachtungs-Anker:** Morningstar coverage 2024 zeigt ~17% der ~1.600 Coverage-Firmen als Wide Moat — strukturell selten, was Buy-and-Hold-Disziplin im Dynastie-Depot rechtfertigt.

## CAP-Treiber (qualitativ, aus Mauboussin-Framework)

1. **Industriestruktur** (Five Forces) — schwacher Wettbewerb + hohe Eintrittsbarrieren = lange CAP
2. **Disruption-Anfälligkeit** — Christensen-Tradition + Industry Dis-Integration; Software-Plattformen anfällig für Open-Source-Disruption, Pharma anfällig für Patent-Cliffs
3. **Regulatory Stability** — regulierte Sektoren (Energie, Pharma, Finance) haben oft langer CAP, aber Politik-Risiko
4. **Innovation-Investment** — F&E-Reinvestment als CAP-Verlängerung (siehe AVGO Acquihire-Strategie, MSFT Azure-Reinvestment)
5. **Customer-Lock-in** — Switching Costs, Network Effects, Ecosystem-Bindung (siehe VEEV Life-Sciences-Plattform, V Zahlungsnetzwerk)
6. **Brand Power** — Pricing Power × Loyalitäts-Premium (siehe RMS Hermès-Marke, COST Membership-Modell)

## Beziehung zu DEFCON

### Was CAP NICHT ist

- **Kein Score-Element** — Estimation passt nicht in 4-Min-Score-Routine; quantitative CAP-Modelle (z.B. Mauboussin Excess-Return-Period-Tools) brauchen 2-3 Stunden pro Ticker
- **Kein FLAG-Trigger** — CAP-Verkürzung ist langsam und qualitativ; FLAGs reagieren auf scharfe Fundamentals-Veränderungen
- **Kein QuickCheck-Punkt** — siehe oben; QuickCheck ist 3-Min-Ampel-Status

### Was CAP LIEFERT

1. **Sprachregel für !Analysiere-Briefing-Argumentation** — bei Wide Moat + langfristiger Buy-and-Hold-Diskussion ist CAP der theoretische Anker. Beispiel-Briefing-Sprache: „AVGO Wide Moat (Switching Costs Chip-Ökosystem) → CAP geschätzt >25 Jahre durch acquisitive Ecosystem-Erweiterung; Terminal-Value-Annahme im DCF mit 50% Sustainability-Premium gerechtfertigt."

2. **Bull/Bear-DCF-Szenario-Anker** für !CAPEX-FCF-ANALYSIS Sheet 2 (siehe `01_Skills/dynastie-depot/capex-fcf-template.md`):
   - **Bull-Case:** CAP = 25-30J (Moat erweitert, Reinvestment >100% NOPAT)
   - **Base-Case:** CAP = 15-20J (Moat stabil, Reinvestment 60-80% NOPAT)
   - **Bear-Case:** CAP = 8-12J (Moat erodiert durch Disruption/Regulation/Reife)

3. **Konsolidierungstag-Argument für Slot-Allokation:** 16 Slots im Dynastie-Depot bei Zieljahr 2058 → Buy-and-Hold-Horizont 32 Jahre. Nur Wide Moat mit CAP ≥ 25J ist strukturell ausreichend lange — daher die strikte Wide-Moat-Pflicht für Hauptpositionen.

## Konkrete CAP-Schätzungen für die Satelliten (qualitativ, Konsensus-Schätzung)

| Ticker | Moat | CAP (geschätzt) | Begründung |
|---|---|---|---|
| AVGO | Wide | >25J | Chip+SW-Ökosystem + acquisitive Ecosystem-Erweiterung |
| V | Wide | >30J | Network Effects + Efficient Scale Zahlungsnetzwerk; Disruption-resistent (Crypto-Volatilität) |
| MSFT | Wide | >20J | Azure-Plattform + Office-Switching-Costs; CapEx-FLAG drückt aktuell Score, aber CAP unverändert |
| BRK.B | Wide | >30J | Float-Modell + Holding-Diversifikation; CAP = strukturelle Kapital-Allokation |
| RMS | Wide | >25J | Hermès-Marke + Pricing-Power; Luxus-Markt strukturell stabil |
| COST *(Exit 06/2026)* | Wide | >20J | Membership-Modell + Cost Advantage; Disruption durch Online-Retail begrenzt |
| ASML | Wide | 15-20J | EUV-Monopol jetzt; ~2035-2040 Hochskalierung Lithografie-Alternativen möglich |
| VEEV *(Exit 06/2026)* | Wide | >15J | Life-Sciences-SaaS-Switching-Costs; Konkurrenz durch Salesforce.com-Vertical begrenzt |
| TMO | Wide | 15-20J | Switching-Costs Life-Sciences; ROIC<WACC kein CAP-Verkürzungs-Signal, sondern Bilanz-Komplexität |
| SU | Narrow/Wide | 15-20J | Regulatory Moat + Energie-Infrastruktur; Energie-Transition-Risiko mid-term |
| APH | Narrow | 10-15J | Switching-Costs Steckverbinder; Tariff-Exposure CN/MY/TH Disruption-Risiko |

→ **Strukturelle Beobachtung:** CAP <15J = strukturell zu kurz für Dynastie-Buy-and-Hold; APH ist der Edge-Case (FLAG-Score-basiert + niedrige CAP = Auswechselungs-Watch).

> **Umstrukturierung-2027 (06/2026):** COST/VEEV exited (oben markiert). Owner-Adds **AMZN/NOW/KYCCF/ZETA** sind in dieser Tabelle noch ohne CAP-Schätzung — CAP ist SOURCE-ONLY/qualitativ (kein Score-Element, User-Decision 26.04.2026), daher hier **keine erfundenen Werte**; Nachtrag bei Bedarf nach O3-Analyse. Aktueller Roster: 13 Satelliten (siehe [[PORTFOLIO]]).

## Limitationen

- **CAP ist Konsensus-Schätzung, nicht observable** — Standard-Errors sind groß (±5-10 Jahre); CAP-Wert nicht für quantitative Score-Berechnung verwenden.
- **Sample-Bias bei Mauboussin:** Coverage primär US-Large-Cap; Non-US-Übertragbarkeit (RMS, ASML, SU) qualitativ konsistent, aber nicht direkt-empirisch validiert.
- **Disruption-Outlier:** Einzelne Disruption-Events (z.B. iPhone 2007 → Nokia/BlackBerry CAP-Kollaps in 3 Jahren) zeigen, dass CAP-Schätzungen ex-ante systematisch zu lang sind. Konservative Bear-Case-CAP-Annahmen Pflicht.
- **DEFCON-Integrations-Diskussion:** User-Decision 26.04.2026 → CAP bleibt SOURCE-ONLY-Konzept, kein active-scoring B-Element. Wiederaufnahme nur über §28.1 Migration-Workflow + §29.4 t≥3 Hurdle.

## Backlinks

- [[Mauboussin-Callahan-2024-Measuring-Moat]] — Primärquelle (SOURCE-ONLY)
- [[Moat-Taxonomie-Morningstar]] — komplementäre Konzept-Page (Wide/Narrow/None × CAP-Mapping)
- [[ROIC-vs-WACC]] — Magnitude-Dimension; CAP ist Sustainability-Komplement
- [[Morningstar-Wide-Moat]] — Primärquelle für Moat-Taxonomie
- [[Buffett-Faktorlogik]] — Buffett-Stil ist implizite CAP-Maximierung (Hold Forever)
- [[DEFCON-System]] — Block-Gewichtung 50/20/10/10/10 strukturell CAP-konsistent
- [[Wissenschaftliche-Fundierung-DEFCON]] — SOURCE-ONLY-Anchor (kein B-Befund)
