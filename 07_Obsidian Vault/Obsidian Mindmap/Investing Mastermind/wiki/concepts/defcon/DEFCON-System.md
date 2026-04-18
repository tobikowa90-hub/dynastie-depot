---
title: "DEFCON-System"
type: concept
tags: [konzept, defcon, scoring, kern]
created: 2026-04-08
updated: 2026-04-19
version: v3.7
stand: 2026-04-19
sources: [arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha, llms-for-equity-stock-ratings, Wolff-Echterling-2023, Jadhav-Mirza-2025, Piotroski-F-Score, Novy-Marx-Gross-Profitability, Sloan-Accruals]
wissenschaftlicher_anker: "B1–B14 (alle 10 Paper) — vollständige wissenschaftliche Fundierung in [[Wissenschaftliche-Fundierung-DEFCON]]"
konfidenzstufe: peer-reviewed
related: [CapEx-FLAG, ROIC-vs-WACC, Analyse-Pipeline, Tariff-Exposure-Regel, Non-US-Scoring, Update-Klassen-DEFCON, Backtest-Ready-Infrastructure, Score-Archiv, FLAG-Event-Log]
---

# DEFCON-System — 100-Punkte-Scoring-Matrix (v3.7)

> Das Herzstück des Dynastie-Depot Analyse-Frameworks.
> Jede Satellitenposition erhält einen Score von 0–100. Der Score bestimmt die Sparrate.
>
> **Aktuelle Version v3.7 (System-Gap-Release, 17.04.2026):** Vier strukturelle Fixes gegenüber v3.5 (Details unten). Skill-Paket-Version v3.7.2 (19.04.2026) delegiert Archiv-Write an Satelliten-Skill, Scoring-Semantik unverändert.

## Scoring-Blöcke (v3.7)

| Block | Gewicht | Inhalt |
|-------|---------|--------|
| 🔢 Fundamentals | 50 Pt. (**hard cap**, v3.7 Fix 4) | P/FCF, Fwd P/E, Bilanz, CapEx/OCF, ROIC, FCF-Yield, **Operating Margin TTM** (v3.7 Fix 2, max 2 Pt.) + Maluse (SBC, Accruals, Tariff) |
| 🏰 Economic Moat | 20 Pt. | Wide/Narrow/None — Morningstar primär; GM-Trend-Delta ±1, Pricing-Power-Bonus +1 |
| 📉 Technicals | 10 Pt. (+DCF-Bonus ±1) | ATH-Distanz 0-4, Rel-Stärke vs S&P500 0-3 (v3.5 Promotion), MA200-Lage 0-3 |
| 🔴 Insider | 10 Pt. | Net Buy 6M 0-4, Ownership 0-3, kein >$20M diskretionäres Selling 0-3 |
| 📊 Sentiment | 10 Pt. (+Delta-Bonus ±2) | **strong_buy_ratio** 0-4 (v3.7 Fix 3, ersetzt konsensus), sell_ratio 0-3 (v3.7 Fix 3 bias-kalibriert), PT-Upside 0-3, EPS-Revision ±1, PT-Dispersion ±1 |

## v3.7 System-Gap-Release — 4 strukturelle Fixes

| Fix | Problem (v3.5) | Lösung (v3.7) |
|-----|----------------|---------------|
| **1. Quality-Trap-Interaktionsterm** | Additiver Moat-Malus verletzte Double-Counting-Verbot | Interaktionsterm: bei Moat=wide + Fwd P/E >30 ODER P/FCF >35 wird der betreffende Fundamentals-Subscore **hart 0**. Bei 22-30/22-35 max 1 Pt. Kein Pauschal-Malus. |
| **2. Operating Margin TTM** | Profitabilitäts-Qualität nicht direkt im Scoring | Neue Fundamentals-Metrik (max 2 Pt.): >30% → 2, 15-30% → 1, <15% → 0. Exception: COST / BRK.B (Membership / Insurance). |
| **3. Analyst-Bias-Kalibrierung** | Rohe Analyst-Counts bias-anfällig (Crowd-Effekt) | `strong_buy_ratio`: SB<40% → 4, 40-50% → 3, 50-60% → 2, >60% → 1 (Crowd-Malus). `sell_ratio`: <3% → 1 (Warning, zu wenig Skepsis), 3-10% → 3, >10% → 0. |
| **4. Fundamentals-Block-Cap 50** | Bonus-Inflation möglich bei vielen Sub-Boni | Harter Deckel 50 Pt. auf Fundamentals — kein Überlauf, keine Score-Inflation. |

**Schema-SKILL-Threshold-Alignment (18.04.2026):** DEFCON-Thresholds auf SKILL.md aligned (≥80/65-79/50-64/<50). Vorher Schema 70/60/50 (Drift gefixt).

## DEFCON-Schwellen & Sparraten

| Score | DEFCON | Sparrate | Bedeutung |
|-------|--------|----------|-----------|
| ≥ 80 | 🟢 4 | Volle Rate (Gewicht 1.0) | Aktiv ausbauen |
| 65–79 | 🟡 3 | Volle Rate (Gewicht 1.0) | These intakt, weiter besparen |
| 50–64 | 🟠 2 | 50% Sockelbetrag (Gewicht 0.5) | Reduziert — Position halten, nicht ausbauen |
| < 50 | 🔴 1 | 0 € — eingefroren | Auswechslung einleiten |

> 🔴 FLAG überschreibt jeden Score → 0 €. Nur 🔴 FLAGs stoppen — 🟡/🚩 lassen Rate unverändert.

## Sparplan-Formel

Aktien-Budget gesamt: **285 €/Monat**

```
Gewichte: D4/D3 (kein 🔴) = 1.0 | D2 (kein 🔴) = 0.5 | D1 / 🔴 FLAG = 0.0
Einzelrate = 285€ / Σ Gewichte × Eigengewicht
```

**Beispiel (Stand 19.04.2026: 7× D4/D3 + 2× D2 (V+TMO) + 2× 🔴 FLAG (MSFT, APH)):**
- Nenner = (7 × 1.0) + (2 × 0.5) = **8.0**
- D4/D3-Rate = 285 / 8.0 × 1.0 = **35,63€**
- D2-Rate (V, TMO) = 285 / 8.0 × 0.5 = **17,81€**
- 🔴/D1-Rate (MSFT, APH) = **0€**
- Check: 7 × 35,63€ + 2 × 17,81€ = 249,41€ + 35,62€ = **285€** ✓

## Verlinkungen

- [[CapEx-FLAG]] — Automatische FLAGs (score-unabhängig)
- [[ROIC-vs-WACC]] — Warum ROIC-Malus so hart ist
- [[Analyse-Pipeline]] — Stufe 0 → 1 → 2 → Entscheidung
- [[Steuer-Architektur]] — Rebalancing ohne Verkauf (Steuer-Bremse)
- [[ETF-Core]] — Parallele 65%-Struktur (separate Logik)
- [[dynastie-depot-skill]] — Skill mit allen Befehlen und Kalibrierungsankern
- [[defeatbeta]] — US-Fundamentals API (Primär für Scoring)
- [[Shibui-SQL]] — Technicals API (Primär für Scoring)
- [[Chain-of-Thought Prompting]] — Methodik hinter dem strukturierten !Analysiere-Workflow (erst begründen, dann scoren)
- [[LLM-Based Stock Rating]] — Forschungsgrundlage: Fundamentals-Block 50 Pt. basiert auf JPM-Evidenz
- [[AI in Investment Analysis]] — Zentrale Synthese: JPM-Forschung → DEFCON-Implementierung
- [[Score-Archiv]] — Append-only Score-Historie (History-Layer)
- [[FLAG-Event-Log]] — Append-only FLAG-Events (History-Layer)
- [[Backtest-Ready-Infrastructure]] — 4-Layer-Architektur (seit 17.04.2026, Skill-Orchestrator seit 19.04.2026)
- [[backtest-ready-forward-verify]] (Skill, 01_Skills/) — orchestriert Schritt-7-Persistence-Pipeline seit v3.7.2

## Datenhaltung — 4-Layer-Architektur (ab 2026-04-17)

Das DEFCON-System hält seinen Zustand in vier getrennten Layern (siehe KONTEXT.md §11):

| Layer | Datei(en) | Mutation |
|-------|-----------|----------|
| State | `Faktortabelle.md` | Überschrieben |
| Narrative | `log.md`, `CORE-MEMORY.md` | Fortgeschrieben |
| History | `05_Archiv/score_history.jsonl`, `05_Archiv/flag_events.jsonl` | Append-only (unveränderlich) |
| Projection | `STATE.md` | Aus State + Narrative synchronisiert |

Jede Score/FLAG-Änderung triggert §18 Sync-Pflicht auf **alle sechs Dateien** im gleichen git-Commit. Details: [[Backtest-Ready-Infrastructure]], [[Score-Archiv]], [[FLAG-Event-Log]].
