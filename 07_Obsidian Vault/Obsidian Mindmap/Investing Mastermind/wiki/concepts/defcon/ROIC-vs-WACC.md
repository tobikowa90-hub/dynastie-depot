---
title: "ROIC vs. WACC"
type: concept
tags: [konzept, roic, wacc, scoring, cap, value-creation]
created: 2026-04-10
updated: 2026-04-27
sources: [Gu-Kelly-Xiu-2020, Buffetts-Alpha, Wolff-Echterling-2023, Mauboussin-Callahan-2024-Measuring-Moat]
related: [DEFCON-System, CapEx-FLAG, Analyse-Pipeline, Update-Klassen-DEFCON, Competitive-Advantage-Period, Moat-Taxonomie-Morningstar, Mauboussin-Callahan-2024-Measuring-Moat]
wissenschaftlicher_anker: "B2 (Gu/Kelly/Xiu 2020) — ROIC + FCF stabilste Profitability-Prädiktoren | B5 (Buffetts Alpha AQR) — cheap+safe+quality Dreiklang, ROIC-Spread als Quality-Kern | B8 (Wolff/Echterling 2023) — ROIC top-ranked in allen ML-Modellen, robust auf S&P500 + STOXX Europe 600 | Mauboussin/Callahan 2024 (SOURCE-ONLY) — ROIC-WACC-Spread × CAP (Competitive Advantage Period) als Magnitude × Sustainability-Dekomposition"
konfidenzstufe: peer-reviewed
---

# ROIC vs. WACC — Harter Malus

> Auch bei Wide Moat: Wenn ROIC < WACC, verzinst das Unternehmen Kapital nicht oberhalb der Kapitalkosten. Das ist ein fundamentales Problem.

## Scoring-Regel

| ROIC vs. WACC | Punkte (max 8) |
|--------------|----------------|
| ROIC > WACC + 5% | 8 |
| ROIC > WACC + 3–5% | 6–7 |
| ROIC > WACC + 1–3% | 4–5 |
| ROIC ≈ WACC | 2–3 |
| ROIC < WACC | 0–1 |

## Goodwill-Verzerrung

M&A-Akquisitionen erhöhen den Invested Capital durch Goodwill und drücken ROIC dauerhaft.
- **GAAP-ROIC ist die Scoring-Basis** — kein Non-GAAP-Bypass
- Non-GAAP bereinigter ROIC darf als Zusatzinformation genannt werden

**Referenzen:**
- TMO: ROIC 2.6% (Goodwill $49.4B = 44.8% Assets)
- SNPS: Ansys-Akquisition $26.88B Goodwill → ROIC-Malus -3 Punkte
- SPGI: IHS Markit $44B Goodwill

## Magnitude × Sustainability — CAP-Erweiterung (Mauboussin/Callahan 2024)

ROIC-WACC-Spread quantifiziert *momentane* Wertschöpfung. Mauboussin/Callahan 2024 systematisieren Value-Creation um zwei Dimensionen, von denen Spread nur eine ist:

| Dimension | DEFCON-Element | Operative Anwendung |
|---|---|---|
| **Magnitude** (ROIC-WACC-Spread × Investment-Größe) | **Diese Page** — Fundamentals-Block 8 Pt. | Punktvergabe nach obiger Tabelle |
| **Sustainability (CAP)** | [[Competitive-Advantage-Period]] (Concept-Page) | Sprachregel für DEFCON ≥ 80 + !CAPEX-FCF-ANALYSIS — kein Score-Element |

**Aggregate Value Creation = ROIC-WACC-Spread × Reinvestment-Volume × CAP**

Drei Beispiele der konzeptuellen Trennung:

1. **TMO (ROIC 2,6% < WACC):** Spread-Magnitude negativ → harter Malus per Score-Tabelle. CAP-Frage irrelevant solange Spread negativ.
2. **AVGO (ROIC > WACC + 10pp, Wide Moat, lange CAP):** Spread-Magnitude maximal + CAP >20J → Value-Creation maximal über Lebenszeit. Score 85.
3. **SNPS (ROIC GAAP 3,8% durch Ansys-Goodwill, bereinigt 15-18%):** Spread-Magnitude bereinigt positiv, CAP via Switching-Costs-Moat lang → Score-Malus -3 für GAAP-Bypass-Disziplin, aber Bull-Argument in !CAPEX-FCF-ANALYSIS auf CAP-Argument bauen.

**Wichtig:** CAP wird im DEFCON-Scoring NICHT operationalisiert (Estimation passt nicht in 4-Min-Score-Routine). Aber für DEFCON ≥ 80 + Bull/Bear-DCF-Szenarien (capex-fcf-template.md Sheet 2) ist CAP die theoretische Begründung der Terminal-Value-Annahme.

→ Detailliert: [[Competitive-Advantage-Period]]

## Verlinkungen

- [[DEFCON-System]] — Scoring-Matrix (ROIC = Teil des Fundamentals-Blocks)
- [[CapEx-FLAG]] — Verwandter Malus (CapEx/OCF > 60%)
- [[Analyse-Pipeline]] — ROIC-Check in Stufe 2
- [[Update-Klassen-DEFCON]] — Quartalsupdates bei Klasse A
- [[Moat-Taxonomie-Morningstar]] — Wide Moat ≈ CAP >20J Mapping
- [[Competitive-Advantage-Period]] — CAP-Concept (Mauboussin-Anker)
- [[Mauboussin-Callahan-2024-Measuring-Moat]] — Primärquelle (SOURCE-ONLY)
- [[TMO]] — Hauptbeispiel (ROIC 2.6%, Goodwill $49.4B)
- [[SNPS]] — Goodwill-Referenz (Ansys $26.88B)
- [[SPGI]] — Goodwill-Referenz (IHS Markit $44B)
