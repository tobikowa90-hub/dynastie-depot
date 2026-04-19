---
title: "Wissenschaftliche Fundierung DEFCON v3.7"
type: synthesis
tags: [defcon, scoring, wissenschaft, entscheidungsmatrix, faktor-kalibrierung, validation-gate]
sources: "[[arXiv-1711.04837]], [[Gu-Kelly-Xiu-2020]], [[Morningstar-Wide-Moat]], [[Buffetts-Alpha]], [[Wolff-Echterling-2023]], [[Jadhav-Mirza-2025]], [[llms-for-equity-stock-ratings]], [[Piotroski-2000]], [[Novy-Marx-2013]], [[Sloan-1996]], [[Bailey-2015-PBO]], [[Aghassi-2023-Fact-Fiction]], [[Flint-Vermaak-2021-Decay]], [[Palomar-2025-Portfolio-Optimization]]"
concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[Buffett-Faktorlogik]], [[QMJ-Faktor]], [[Chain-of-Thought Prompting]], [[F-Score-Quality-Signal]], [[Gross-Profitability-Premium]], [[Accruals-Anomalie-Sloan]], [[PBO-Backtest-Overfitting]], [[Factor-Investing-Framework]], [[Factor-Information-Decay]], [[Seven-Sins-Backtesting]], [[Palomar-Methods-Reference]]"
related: "[[DEFCON-System]], [[Analyse-Pipeline]], [[CapEx-FLAG]], [[ROIC-vs-WACC]], [[Non-US-Scoring]], [[Backtest-Methodik-Roadmap]]"
entities: "[[ASML]], [[AVGO]], [[MSFT]], [[RMS]], [[VEEV]], [[SU]], [[BRKB]], [[V]], [[APH]], [[COST]], [[TMO]]"
datum: 2026-04-19
status: aktiv
---

# Wissenschaftliche Fundierung DEFCON v3.7

> Dieses Dokument belegt, dass das DEFCON-Scoring-System auf peer-reviewed Forschung basiert.
> 10 Quellen → 14 Befunde → operative Konsequenzen für das Dynasty-Depot.

---

## v3.7-Änderungsprotokoll (17.04.2026)

**3 operative Gap-Closures, wissenschaftlich validiert:**

1. **Quality-Trap-Interaktionsterm (B6)** — Deckel auf Fundamentals-Subscores statt Moat-Malus. Begründung: Applied Learning 17.04. verbietet Double-Counting. Fwd P/E und P/FCF sind bereits in Fundamentals dekomponiert — ein zusätzlicher Moat-Abzug wäre doppelte Strafe auf dieselbe Beobachtung. Lösung: bei Wide Moat + teure Bewertung wird der Fwd-P/E-/P/FCF-Subscore hart auf 0 gedeckelt. Signal-Erhalt ohne Regelverletzung.

2. **Operating Margin TTM (B8)** — neue Fundamentals-Metrik (max. 2 Pt.) operationalisiert Wolff-Echterling-2023 (ROIC + FCF + OpM als Top-Prädiktoren). Vorher war OpM nur implizit in Moat-GM-Trend enthalten, nicht als eigene Quantität.

3. **Analyst-Bias-Kalibrierung (B11)** — Crowd-Consensus >60% Strong Buy erzeugt jetzt Malus (vorher unlimitiert-positiv). Sell-Ratio dreistufig (<3% = Warnsignal, nicht Bestnote). Direkte Umsetzung von Jadhav-Mirza 2025 + llms-for-equity-stock-ratings: News-/Analyst-Daten haben strukturellen Positivity-Bias, den das Scoring aktiv korrigieren muss.

**Nicht übernommen aus v3.6:** F-Score-Bonus, GP/TA-Metrik, Accrual-Bonus — alle drei waren Double-Counting-Kandidaten. Papers B12/B13/B14 bleiben als wissenschaftliche Validation der Sub-Signale (Piotroski → Bilanz/FCF/ROIC, Novy-Marx → GM-Trend, Sloan → Accrual Ratio), aber werden nicht als Aggregat-Scores addiert.

**Fundamentals-Cap bei 50:** Block-Summe hart gedeckelt — verhindert Score-Inflation durch Bonus-Akkumulation bei Top-Namen.

---

## 11-Befunde Entscheidungsmatrix (Stand: 16.04.2026)

| # | Befund | Quelle | Block | Empfehlung | Konsequenz |
|---|--------|--------|-------|------------|------------|
| **B1** | 5J-Fenster > Spot als Rendite-Prädiktor (+2,7% CAGR) | [[arXiv-1711.04837]] | Fundamentals (50 Pt.) | 5J-Perspektive als Pflichtrahmen | 5J-Trend in jeder Analyse prüfen |
| **B2** | FCF + Gross Margin = stabilste Prädiktoren (Top-2 ML-Features) | [[Gu-Kelly-Xiu-2020]] | Fundamentals — FCF/GM | Trailing P/E de-priorisieren; forward P/E valide | P/FCF + Fwd P/E bleiben primär; trailing P/E nur Kontext |
| **B3** | Earnings-Quality > Value (Accrual Ratio top-3 Feature) | [[Gu-Kelly-Xiu-2020]] | Fundamentals — Qualität | FCF-Qualität und GM-Trend aufwerten | Bonus-Metriken Accrual Ratio + GM-Trend bestätigt |
| **B4** | 8 Moat-Quellen operativ identifiziert | [[Morningstar-Wide-Moat]] | Moat (20 Pt.) | 8-Quellen-Checkliste im Moat-Block | Jede Moat-Analyse prüft alle 8 Quellen |
| **B5** | Buffetts Alpha = QMJ + BAB + Value (vollständig erklärt) | [[Buffetts-Alpha]] | Fundamentals + Moat | cheap+safe+quality als operativer Dreiklang | DEFCON-4-Kriterien = cheap+safe+quality |
| **B6** | Moat allein ≠ Excess Return (Quality Trap ohne Bewertung) | [[Morningstar-Wide-Moat]] | Moat + Bewertung | Wide Moat immer mit Bewertungsdisziplin | Kombination Moat + Fundamentals ist Pflicht |
| **B7** | Fundamentals > Sentiment > Technicals (ML-Datenhierarchie) | Kern-Paper (arXiv, Gu, MS, AQR) | Datenhierarchie | Gewichtung 50/10/10 Pt. bestätigt | Datenhierarchie explizit in !Analysiere benennen |
| **B8** | ROIC + FCF/EV + Operating Margin = top-ranked in allen ML-Modellen | [[Wolff-Echterling-2023]] | Fundamentals — ROIC/FCF | ROIC-Malus ist wissenschaftlich zwingend, nicht heuristisch | ROIC-vs-WACC Scoring direkt belegt; Non-US-Übertragbarkeit validiert |
| **B9** | EPS-Growth + Low Leverage = stabile Quality-Prädiktoren | [[Wolff-Echterling-2023]] | Fundamentals — Bilanz | Debt/EBITDA-Scoring wissenschaftlich fundiert | EPS Revision Momentum (+1 Bonus) + Bilanz-Block (9 Pt.) bestätigt |
| **B10** | Chain-of-Thought vor Scoring verbessert Konsistenz + Genauigkeit | [[llms-for-equity-stock-ratings]] | Workflow — !Analysiere | Begründen vor Scoren als Pflichtprinzip | Befunde-Priming in INSTRUKTIONEN.md (Stufe 2) verankert |
| **B11** | News-Daten erzeugen Positivity-Bias — mittelfristig schädlich | [[llms-for-equity-stock-ratings]], [[Jadhav-Mirza-2025]] | Sentiment (10 Pt.) | Sentiment-Gewichtung deckeln; Analyst-Bias (43% Strong Buy) gegensteuern | Sentiment-Cap 10 Pt. gerechtfertigt; Sell-Ratio-Check als Korrektiv |
| **B12** | F-Score ≥7 → +7,5% p.a. Outperformance bei Value-Aktien | [[Piotroski-2000]] | Fundamentals (Quality-Bonus) | Quality als PRÄDIKTOR (nicht nur Malus); 9-Kriterien-Score operationalisieren | v3.6: F-Score ≥7 → +2 Pt. Bonus Fundamentals; ≤3 → -1 Pt. Malus |
| **B13** | GP/TA prognostiziert Returns ~gleich stark wie Book-to-Market | [[Novy-Marx-2013]] | Fundamentals (Profitability-Metrik) | Gross Profitability als eigenständiger Renditefaktor | v3.6: GP/TA als 2-Pt.-Metrik in Fundamentals-Block; GM-Trend im Moat-Block bleibt |
| **B14** | Low-Accrual-Firmen outperformen High-Accrual um +10,4% p.a. | [[Sloan-1996]] | Fundamentals (Accrual Ratio) | Accrual-Schwellen (<5%/>10%) wissenschaftlich validiert | v3.5 Malus bleibt; v3.6-Erweiterung: <3% → +2 Pt. Bonus (Piotroski-Parallele) |
| **B15** | PBO < 0,05 (CSCV) als Overfitting-Gate bei Strategy-Selection | [[Bailey-2015-PBO]] | Validation-Methode | Institutioneller Goldstandard; Pflicht bei Parameter-Tuning | §29.1 Retrospective-Analyse-Gate, Aktivierung 2028-04-01 |
| **B16** | 4 Kanon-Faktoren (Value/Momentum/Quality/Defensive); Size verworfen; t-Stat≥3 Hurdle | [[Aghassi-2023-Fact-Fiction]] | Externer Benchmark + neue Parameter | DEFCON-Faktor-Mapping explizit; aggr. Portfolio-SR im AQR-Band prüfen | §29.2 External-Bench + §29.4 t-Stat-Hurdle |
| **B17** | Faktor-Half-Life: Value 3–4M, Quality 4–5M, Momentum 3M, Investment 1M, LowVol 5–6M | [[Flint-Vermaak-2021-Decay]] | Cadence-Validation | Earnings-Trigger (~3M) wissenschaftlich fundiert; Investment-Klasse Watch | §29.3 Temporal-Konsistenz; keine System-Änderung |
| **B18** | Seven Sins of Quantitative Investing (Overfitting + 6 weitere Biases) | [[Palomar-2025-Portfolio-Optimization]] | Pre-Flight-Validation | Pflicht-Checkliste vor jeder retrospektiven Analyse; Sin #7 n.a. Long-Only | §29.5 Seven-Sins-Gate aktiv auch bei Migration-Events |

---

## PFLICHT-Regeln (wörtlich, session-übergreifend)

### Aus Gu/Kelly/Xiu (2020):
> **"Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide."**
> Gilt in jeder DEFCON-Analyse. Fwd P/E ist Primärmetrik; trailing P/E höchstens als Kontext.

### Aus Buffetts Alpha (AQR 2018):
> **"Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality."**
> Gilt bei jeder BRK.B-Analyse und bei Leverage-Diskussionen.

---

## Quellen-Übersicht (10 Paper — Stand: 17.04.2026)

| Quelle | Jahr | Kernthese | DEFCON-Block | Neue Befunde |
|--------|------|-----------|--------------|-------------|
| [[arXiv-1711.04837]] | 2019 | ML + 5J-Fenster → +2,7% CAGR | Fundamentals 50% | B1, B7 |
| [[Gu-Kelly-Xiu-2020]] | 2020 | FCF+GM primär; trailing P/E schwach | Faktor-Kalibrierung | B2, B3, B7 |
| [[Morningstar-Wide-Moat]] | 2023 | 8 Moat-Quellen; Moat+Fundamentals nötig | Moat 20% | B4, B6 |
| [[Buffetts-Alpha]] | 2018 | QMJ+BAB+Value; Float nicht replizierbar | Fundamentals+Moat+BRK.B | B5 |
| [[Wolff-Echterling-2023]] | 2023 | ROIC+FCF top-ranked; STOXX-robust | Fundamentals ROIC/Bilanz | B8, B9 |
| [[llms-for-equity-stock-ratings]] | 2024 | Fundamentals > News; CoT verbessert Genauigkeit | Workflow + Sentiment | B10, B11 |
| [[Jadhav-Mirza-2025]] | 2025 | 84-Paper-Survey; News-Bias; RL+Memory | Sentiment + Architektur | B11 (Bestätigung) |
| [[Piotroski-2000]] | 2000 | F-Score ≥7 → +7,5% p.a. bei Value-Aktien | Fundamentals (Quality-Bonus) | B12 ← NEU |
| [[Novy-Marx-2013]] | 2013 | Gross Profitability = 2. Seite des Value-Faktors | Fundamentals (GP/TA) | B13 ← NEU |
| [[Sloan-1996]] | 1996 | Accruals-Anomalie: +10,4% p.a. Low-Accrual-Premium | Fundamentals (Accrual Ratio) | B14 ← NEU |
| [[Bailey-2015-PBO]] | 2015 | PBO/CSCV als Overfitting-Gate bei Strategy-Selection | Validation-Methode | B15 ← NEU |
| [[Aghassi-2023-Fact-Fiction]] | 2023 | 4 Kanon-Faktoren validiert; Size verworfen; t-Stat≥3 | Externer Benchmark + neue Parameter | B16 ← NEU |
| [[Flint-Vermaak-2021-Decay]] | 2021 | Faktor-Half-Life → optimale Rebalance-Cadence | Cadence-Validation | B17 ← NEU |
| [[Palomar-2025-Portfolio-Optimization]] | 2025 | Seven Sins of Quantitative Investing | Pre-Flight-Validation | B18 ← NEU |

---

## Betroffene Entitäten

### Aktive Satelliten (v3.5-Zeitstand: 16.04.2026 — dient B1-B11 Mapping)

> ⚠️ **Scores sind v3.5-Zeitstand (16.04.)** — nicht Live-Portfolio-State. Aktuelle v3.7-Scores: siehe `00_Core/STATE.md` (Single Source of Truth). Tabelle dient dem Mapping der wissenschaftlichen Befunde (B1-B11) auf Satelliten-Charakteristika, keine Scoring-Aussage.

| Ticker | DEFCON | Score | FLAG | Relevante Befunde |
|--------|--------|-------|------|------------------|
| [[ASML]] | 🟡 3 | 68 | — | B1 (5J-EUV-Ramp), B4 (EUV-Monopol 100%), B6 (Fwd P/E 38x = Quality Trap ohne Bewertungsmarge), B8 (ROIC clean, Non-US-Übertragbarkeit) |
| [[AVGO]] | 🟢 4 | 85 | ⚠️ Insider-Check | B2 (FCF <15% CapEx = Fabless-Referenz), B4 (Chip+SW-Ökosystem Wide Moat), B5 (cheap+safe+quality erfüllt), B8 (ROIC >WACC +10% — Kalibrierungsanker) |
| [[MSFT]] | 🟠 2 | 60 | 🔴 CapEx >60% | B2 (CapEx/OCF 83,6% destroys FCF-Qualität), B3 (Finance-Lease-Bereinigung = Accrual-Komplexität), B6 (Score 60 bei Wide Moat 19/20 = Quality Trap aktiv), B8 (ROIC 7,5% < WACC 13,35% — wissenschaftlich nicht tragbar) |
| [[RMS]] | 🟢 4 | 69 | ✅ Clean | B4 (Marken-Moat: Hermès = 8/8 Moat-Quellen), B6 (Score 69 trotz ROIC 24% wegen Bewertung), B5 (safe: Netto-Cash +€9,89B) |
| [[VEEV]] | 🟢 4 | 74 | ✅ Clean | B2 (FCF-SaaS-Modell, CapEx-arm), B4 (Switching Costs Life-Sciences-Plattform), B3 (Earnings Quality hoch) |
| [[SU]] | 🟢 4 | 71 | ✅ Clean | B4 (Regulatory Moat Energie-Infrastruktur), B5 (safe-Komponente: ROIC 10,48% > WACC 8,96%), B8 (Profitability-Faktoren konsistent positiv) |
| [[BRKB]] | 🟢 4 | 75 | ✅ Clean | B5 vollständig (Float $686B = nicht replizierbar, aber cheap+safe+quality erfüllt), B9 (Low Leverage: Netto-Cash), B4 (Efficient Scale BNSF, Float-Moat) |
| [[V]] | 🟢 4 | 86 | ✅ Clean | B4 (Network Effects: 4,9 Mrd. Karten, Duopol), B2 (CapEx/OCF ~6% = Fabless-Niveau), B5 (cheap+safe+quality — Kalibrierungsanker #2), B8 (ROIC ~9,9%, Goodwill-Verzerrung durch Visa Europe) |
| [[APH]] | 🟡 3 | 61 | 🔴 Score-basiert | B2 (FCF-Marginen ok, aber Bewertung + CN/MY-Risk), B3 (Accrual-Komplexität Supply-Chain), B9 (Financial Leverage mittel) |
| [[COST]] | 🟢 4 | 69 | ✅ Clean | B4 (Cost Advantage: Membership-Loyalität 8/8 Moat-Quellen), B6 (GM 12,7% ≠ Qualitätsproblem — Geschäftsmodell), B9 (Low Leverage <1x) |
| [[TMO]] | 🟠 2 | 62 | — | B2 (FCF -13,4% YoY — Erosion), B3 (ROIC 2,6% unter WACC = negative Earnings Quality), B4 (Switching Costs Life-Sciences intakt), B8 (Goodwill $49,4B drückt ROIC unter Kapitalkosten) — ⚠️ v3.5: RS -7,82% = 0/3 → Score 62, D3→D2 |

---

## Implikationen für SKILL.md

B7 verlangt explizite Dokumentation der Datenhierarchie in SKILL.md:
```
Datenhierarchie (wissenschaftlich belegt):
1. Fundamentals (FCF, ROIC, GM, Fwd P/E) — stärkste Prädiktoren
2. Earnings Quality (Accrual Ratio, FCF-Trend, GM-Trend)
3. Moat (Wide/Narrow/None — Morningstar)
4. Sentiment (Analyst-Ratings, Price Targets)
5. Technicals (Kurs-Momentum, MA-Lage)
```

---

## Konzept-Karte (aktualisiert)

```
arXiv-1711.04837 ──────► [[5J-Fundamental-Fenster]] ──► alle 11 Ticker
Gu-Kelly-Xiu-2020 ─────► [[FCF-Primacy]] ─────────────► alle 11 Ticker
Morningstar-Wide-Moat ─► [[Moat-Taxonomie-Morningstar]] ► alle 11 Ticker
Buffetts-Alpha ─────────► [[Buffett-Faktorlogik]] ──────► [[BRKB]]
                └──────► [[QMJ-Faktor]] ────────────────► [[BRKB]]
Wolff-Echterling-2023 ──► B8 (ROIC-Dominanz) ──────────► [[ROIC-vs-WACC]]
                └──────► B9 (Quality-Stabilität) ───────► Bilanz-Block
                └──────► STOXX-Robustheit ──────────────► [[Non-US-Scoring]]
llms-for-equity-stock-ratings ► B10 (CoT) ──────────────► [[Analyse-Pipeline]] / INSTRUKTIONEN
                └──────► B11 (News-Bias) ───────────────► Sentiment-Block Cap
Jadhav-Mirza-2025 ─────► B11 (Bestätigung) ────────────► Sentiment-Block Cap
Piotroski-2000 ────────► [[F-Score-Quality-Signal]] ────► Fundamentals Quality-Bonus (B12)
Novy-Marx-2013 ────────► [[Gross-Profitability-Premium]] ► Fundamentals GP/TA-Metrik (B13)
Sloan-1996 ────────────► [[Accruals-Anomalie-Sloan]] ────► Fundamentals Accrual Ratio (B14)
```

## Scoring-System-Audit v3.4 → v3.5 (16.04.2026)

**Auslöser:** PT-Upside-Duplikation entdeckt bei Backtest-Ready-Infrastruktur-Planung.
**Maßstab:** Pragmatisch (nur nachweislich verzerrende Fehler als B).

| # | Frage | Klasse | Fazit |
|---|-------|--------|-------|
| 1 | PT-Upside-Duplikation | **B** | Gleiche Rohdaten in Technicals (>20%, 3P) + Sentiment (>15%, 3P) → Fix: Technicals-Metrik ersetzt durch Relative Stärke vs. S&P500 |
| 2 | Weitere Naming-Kollisionen | A | Keine über PT-Upside hinaus |
| 3 | Redundanzen (Fwd P/E↔P/FCF, CapEx/OCF↔FCF Yield, Bilanz-Triade) | A | Verschiedene Konzepte, pragmatisch akzeptiert |
| 4 | Block-Gewichtung vs. Paper | **C** | Moat=20 strategisch korrekt. Sentiment/Technicals-Rebalancing → Evaluation nach 6 Monaten |
| 5 | Kategorien-Hygiene | A | Korrekt (außer PT-Upside) |
| 6 | Malus-Stacking | A | Floor-Klausel (min 0) hinzugefügt |
| 7 | Anker-Reproduzierbarkeit | A | ±5–7 Punkte systemtypisch |

**Implikation für B7 (Fundamentals > Sentiment > Technicals):** Die Bereinigung stärkt B7 — Technicals enthält jetzt ausschließlich preisbasierte Metriken (ATH-Distanz, Relative Stärke, 200MA), Sentiment ausschließlich Analysten-Meinungen (Konsensus, Sell-Ratio, PT vs Kurs). Konzeptuelle Trennung ist sauberer als in v3.4.

---

## Änderungsprotokoll

| Datum | Änderung |
|-------|---------|
| 2026-04-14 | Erstellt — 4 Paper, 7 Befunde, vollständige Backlink-Vernetzung |
| 2026-04-16 | Erweitert — 3 neue Paper (Wolff/Echterling, Jadhav/Mirza, JPM vollständig eingebunden), 4 neue Befunde B8–B11, alle 11 Satelliten-Scores aktualisiert, Konzept-Karte erweitert |
| 2026-04-16 | v3.4→v3.5 Audit — PT-Upside-Fix, Relative Stärke promoted, Floor-Klausel. 7-Fragen-Audit: 5×A, 1×B, 1×C |
| 2026-04-17 | 3 Foundation-Papers integriert: Piotroski (F-Score, B12), Novy-Marx (GP-Premium, B13), Sloan (Accrual-Anomalie, B14). 7→10 Quellen, 11→14 Befunde. Vorbereitung für v3.6-Release: Quality-Bonus (+2 Pt.) + GP/TA-Metrik (2 Pt.) + Accrual-Bonus <3%. System-Reife-Ceiling: 85% → geplant 92-95%. |
| 2026-04-19 | 4 Backtest-Validation-Papers integriert: Bailey PBO/CSCV (B15), Aghassi AQR Fact/Fiction (B16), Flint/Vermaak Information Decay (B17), Palomar Seven Sins (B18). 10→14 Quellen, 14→18 Befunde. B15-B18 sind **keine Scoring-Änderungen**, sondern Validation-Gate-Framework — §29 (Retrospective-Analyse-Gate, FUTURE-ACTIVATION 2028-04-01). §29.5 Seven-Sins-Gate aktiv auch bei Migration-Events. Applied Learning verletzt NICHT — Paper-Ingest ≠ System-Update, nur Gate-Infrastruktur. |

## Validierung der Befunde (Backtest-Ready-Infrastructure, seit 2026-04-17)

Die 14 Befunde sind heute **nicht formal validiert** — das Scoring-System ist wissenschaftlich fundiert (peer-reviewed Papers) und hart kalibriert (AVGO/MKL/SNPS als Anker), aber statistische Forward-Return-Validation scheitert an Sample-Size (11 Satelliten × ~2 Jahre Historie, sparse FLAG-Events).

**Lösung:** Nicht heute validieren, sondern Infrastruktur bauen, die 2028+ **überhaupt Validierung ermöglicht**. Ab 17.04.2026 wird jeder Score + jedes FLAG-Event unveränderlich in `05_Archiv/*.jsonl` archiviert.

**Entscheidungs-Roadmap 2028-04-01:** Abhängig von Datenlage wird eine von 4 Methoden angewendet — siehe [[Backtest-Methodik-Roadmap]]:
- **Option A** (Return-Prediction): validiert B1-B3 via Forward-Return-Quantile
- **Option B** (Wide-Moat-Prämie): validiert B5, B9-B11 via Alpha vs. S&P500
- **Option C** (Threshold-Kalibrierung): validiert B4 via DEFCON-Cutpoint-Optimum
- **Option D** (FLAG-Event-Study): validiert B2-B3 via Forward-Drift nach Trigger

**Explizit NICHT validiert:** B12-B14 (Piotroski, Novy-Marx, Sloan) — v3.6-Integration wurde 17.04.2026 verworfen (Double-Counting-Falle, Applied Learning). Die Befunde bleiben als Forschungskontext, aber sind **nicht Teil des operativen Scorings**.

Infrastruktur-Details: [[Backtest-Ready-Infrastructure]], [[Score-Archiv]], [[FLAG-Event-Log]].

---

## 4-Dimensionen-Validation-Gate (§29, seit 2026-04-19)

B15-B18 bilden zusammen das **formelle Gate-Framework** für jede zukünftige retrospektive Analyse. Keine Scoring-Änderung — Gate-Infrastruktur oberhalb der Options A–D:

| Dimension | Anker-Befund | Operative §-Komponente |
|---|---|---|
| Methode (Overfitting) | B15 Bailey | §29.1 PBO < 0,05 |
| Raum (External Bench) | B16 Aghassi | §29.2 AQR/Ilmanen-Band-Check + §29.4 t-Stat-Hurdle |
| Zeit (Temporal Decay) | B17 Flint/Vermaak | §29.3 Cadence-Konsistenz |
| Sünden (Pre-Flight) | B18 Palomar | §29.5 Seven-Sins-Gate (Sin #7 n.a.) |
| Portfolio-Metriken | — | §29.6 risk-metrics-calculation (Palomar Ch. 6 Formeln) |

Aktivierungs-Trigger: **Review 2028-04-01** oder erste DEFCON-Parameter-Variation. §29.5 Seven-Sins-Gate greift **bereits jetzt** bei Migration-Events.

**§30 Live-Monitoring (seit 2026-04-19, R1 Paper-Integration Phase 4):** Operative Konsequenz aus Flint-Vermaak 2021 Investment-Faktor-Half-Life ~1M. Monthly-Refresh-Pflicht für **aktive Investment-FLAGs** (Scope: MSFT CapEx/OCF 83.6%). Keine Scoring-Änderung — nur Monitoring-Cadence. TMO fcf_trend_neg bleibt Schema-Watch (nicht-aktiviert). Details: INSTRUKTIONEN §30.

Siehe [[Backtest-Methodik-Roadmap]] v2.0 für Detail-Logik der 4-Dim-Gate-Aktivierung.
