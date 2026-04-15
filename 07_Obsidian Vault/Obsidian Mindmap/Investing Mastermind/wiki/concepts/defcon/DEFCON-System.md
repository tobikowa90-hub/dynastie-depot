---
title: "DEFCON-System"
type: concept
tags: [konzept, defcon, scoring, kern]
created: 2026-04-08
updated: 2026-04-14
version: v3.4
stand: 2026-04-08
sources: [arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha]
related: [CapEx-FLAG, ROIC-vs-WACC, Analyse-Pipeline, Tariff-Exposure-Regel, Non-US-Scoring, Update-Klassen-DEFCON]
---

# DEFCON-System — 100-Punkte-Scoring-Matrix

> Das Herzstück des Dynastie-Depot Analyse-Frameworks.
> Jede Satellitenposition erhält einen Score von 0–100. Der Score bestimmt die Sparrate.

## Scoring-Blöcke

| Block | Gewicht | Inhalt |
|-------|---------|--------|
| 🔢 Fundamentals | 50 Pt. | P/FCF, Fwd P/E, Bilanz, CapEx/OCF, ROIC, FCF Yield |
| 🏰 Economic Moat | 20 Pt. | Wide/Narrow/None — Morningstar als Primärquelle |
| 📉 Technicals | 10 Pt. | ATH-Abstand, MA-Lage, DCF-Anker |
| 🔴 Insider | 10 Pt. | Net Buy/Sell, Ownership, diskretionäres Selling >$20M |
| 📊 Sentiment | 10 Pt. | Analyst-Rating, Ø Price Target, Sell-Ratio |

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

**Beispiel (aktuell: 9× D4/D3 aktiv, 2× 🔴 eingefroren):**
- Nenner = (9 × 1.0) + (0 × 0.5) = 9.0
- D4/D3-Rate = 285 / 9.0 × 1.0 = **31.67€**
- D2-Rate (falls vorhanden) = 285 / Nenner × 0.5
- 🔴/D1-Rate = **0€**
- Check: 9 × 31.67 = 285€ ✓

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
