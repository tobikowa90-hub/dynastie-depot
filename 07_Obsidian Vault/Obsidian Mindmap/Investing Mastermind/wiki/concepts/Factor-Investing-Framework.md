---
title: "Factor-Investing-Framework (AQR-Kanon)"
type: concept
tags: [factor-investing, value, momentum, quality, defensive, benchmark, framework]
created: 2026-04-19
updated: 2026-04-19
sources: [Aghassi-2023-Fact-Fiction, Buffetts-Alpha]
related: [PBO-Backtest-Overfitting, Factor-Information-Decay, Seven-Sins-Backtesting, Palomar-Methods-Reference, Backtest-Methodik-Roadmap, QMJ-Faktor, Buffett-Faktorlogik, DEFCON-System]
wissenschaftlicher_anker: "Aghassi, Asness, Fattouche, Moskowitz (2023) + Ilmanen et al. (2021) Century Dataset"
konfidenzstufe: framework-standard
---

# Factor-Investing-Framework (AQR-Kanon)

> **Die 4 peer-reviewed validen Faktoren (Value / Momentum / Carry / Defensive-Quality) als externer Kalibrierungsanker. DEFCON ist ein impliziter Long-Only-Multi-Faktor-Selektor — dieses Framework macht das explizit.**

## Die 4 Kanon-Faktoren

| Faktor | Kern-Metrik | Economic Story |
|---|---|---|
| **Value** | B/M, P/E, P/FCF | Distress-Risk-Kompensation + Behavioral Over-Extrapolation |
| **Momentum** | 12-1M Return | Under-Reaction + Crash-Risk-Kompensation |
| **Carry** | Yield-Spread | Skew-Risk-Prämie (primär FX / Rates / Commodities) |
| **Defensive / Quality** | Low-Beta, hohe Profitabilität, Stable Earnings | Leverage-Aversion + Lottery-Preferences-Kompensation |

Size ist **explizit kein** Kanon-Faktor mehr (Alquist/Israel/Moskowitz 2018, Asness 2020 — schwaches Post-Sample, illiquide, Januar-konzentriert).

## DEFCON-Mapping

| DEFCON-Block (100-Pt.-Matrix) | AQR-Faktor | Evidenz-Stärke |
|---|---|---|
| Fundamentals: Fwd P/E, P/FCF, FCF Yield | **Value** | HML / HMLDEVIL direkte Analoga |
| Fundamentals: ROIC-vs-WACC, Op-Margin, Bilanz-Qualität | **Quality** | QMJ-Komponenten |
| Fundamentals: CapEx/OCF (<10% asset-light) | **Defensive** | Low-CapEx = Low-Risk-Proxy |
| Moat: Pricing Power, Wide-Moat-Rating | **Quality** | Morningstar-Moat korreliert mit QMJ |
| Technicals: Rel. Stärke, Trend-Lage, ATH-Distanz | **Momentum** | UMD-Analogon |
| Sentiment: eps_revision_delta | **Momentum** (fundamental) | Chan et al. 1996 |
| Insider: Net-Buy, Ownership | **nicht im AQR-Kanon** | Dynasty-Depot-Edge |

→ DEFCON ist damit **kein arbitraerer Score-Mix**, sondern aligned mit den peer-reviewed relevanten Faktoren. Insider ergänzt als nicht-akademisches, aber Insider-Trading-Tradition belegtes Signal.

## Kalibrierungs-Zahlen (für Review 2028)

Bei retrospektiver Portfolio-Return-Analyse Erwartungs-Bandbreite:

| Portfolio-Typ | SR-Band | Quelle |
|---|---|---|
| Multi-Faktor US-Stocks (Long-Short) | 1,0–1,2 | Ilmanen 2021 |
| Multi-Faktor all-asset (Long-Short) | 1,3–1,6 | Ilmanen 2021 |
| Long-Only-Faktor-Tilt (Smart Beta) | 0,5–0,8 (Market +100–200bps) | Literatur-Durchschnitt |
| **Dynasty-Depot (Concentrated Long-Only)** | **0,4–0,9 erwartbar** | Projektion — hoher Sample-Error bei n=11 |

**Wichtig:** Dynasty-Depot ≠ Long-Short-Faktor-Portfolio. 11 concentrated Satelliten haben deutlich höheres idiosynkratisches Risiko. AQR-SR-Zahlen sind Orientierung, kein strikter Erwartungswert.

## Harvey-Liu-Zhu t-Stat-Hurdle

Für **neue** DEFCON-Sub-Scores Pflicht: **t-Stat ≥ 3** (nicht 2,0 wie Standard). Begründung:

| t-Stat | Anzahl unabhängiger Trials bis False-Positive |
|---|---|
| 2,0 | 121 |
| **3,0** | **393** |
| 5,0 | 408.234 |
| 8,0 | ~0,5 Billionen |

Academic Finance hat 400+ publizierte Faktoren — die meisten wären bei t ≥ 3 verworfen. Wir wenden diese Hurdle prospektiv auf DEFCON-Erweiterungen an (§29.4).

## Anwendungs-Grenzen

**Was das Framework leistet:**
- Einordnung, welche DEFCON-Komponente welchen akademischen Faktor approximiert
- Externer Benchmark-Anker für aggregierte Portfolio-Analyse (Review 2028)
- t-Stat-Hurdle für prospektive DEFCON-Erweiterungen
- Dämpfer gegen Faktor-Timing-Versuchungen (AQR zeigt: extrem schwer)

**Was es NICHT leistet:**
- Per-Ticker Value-Spread-Signale (AQR-Methode ist Long-Short-Cross-Section)
- Crowding-FLAGs (AQR: Crowding-Narrative meist falsch)
- Timing-Signale (Asness et al. 2017: Value-Timing korreliert r=0,7 mit Static-Value → minimaler Mehrwert)

## Drawdown-Realismus (Paper-Erkenntnis für Psyche)

Ilmanen-Daten über 100 Jahre:
- Jeder Einzel-Faktor hat **mindestens einmal 3J-Drawdown mit negativem SR** erlebt
- Bei SR 0,5 + 10% Vol über 25 Jahre: >30% Max-Drawdown mit >5% WS **normal**, nicht Anomalie
- Value 2018–2020 Drawdown, Momentum-Crash 2009, Quant-Meltdown 2007 August — alle Beispiele "normalen" Faktor-Risikos

→ Drawdown-Kommunikation an sich selbst bei Satelliten-Underperformance: *"Ist das im Band des peer-reviewed erwarteten Drawdown-Risikos?"* — wenn ja, keine Regime-Änderung, sondern normale Faktor-Schwankung.

## Operationalisierung

- **§29 Retrospective-Analyse-Gate** (`00_Core/INSTRUKTIONEN.md`): §29.2 Portfolio-SR-Band-Check, §29.4 t-Stat-Hurdle
- **!Analysiere-Checkliste:** Fwd P/E gegen eigene 5J-Range im Kommentartext anmerken
- **Einzel-Positions-Drawdown-Kontext:** AQR-Faktor-Drawdown-Statistiken als Referenz bei V-/TMO-Unterperformance-Diskussion

## Backlinks
- [[Aghassi-2023-Fact-Fiction]] — Source-Zusammenfassung
- [[QMJ-Faktor]] — Quality-Dimension, AQR-Definition
- [[Buffett-Faktorlogik]] — cheap+safe+quality als Drei-Faktor-Basis
- [[PBO-Backtest-Overfitting]] — methodischer Gate-Komplement
- [[Factor-Information-Decay]] — Temporal-Dimension zu diesem Framework
- [[Seven-Sins-Backtesting]] — Sin-Katalog
- [[Backtest-Methodik-Roadmap]] — 2028-Aktivierungs-Entscheidung
- [[DEFCON-System]] — Zielsystem, Faktor-Mapping-Kontext
