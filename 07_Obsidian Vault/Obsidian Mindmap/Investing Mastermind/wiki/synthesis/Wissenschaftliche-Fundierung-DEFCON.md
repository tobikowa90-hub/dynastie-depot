---
title: "Wissenschaftliche Fundierung DEFCON v3.4"
type: synthesis
tags: [defcon, scoring, wissenschaft, entscheidungsmatrix, faktor-kalibrierung]
sources: "[[arXiv-1711.04837]], [[Gu-Kelly-Xiu-2020]], [[Morningstar-Wide-Moat]], [[Buffetts-Alpha]], [[Wolff-Echterling-2023]], [[Jadhav-Mirza-2025]], [[llms-for-equity-stock-ratings]]"
concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[Buffett-Faktorlogik]], [[QMJ-Faktor]], [[Chain-of-Thought Prompting]]"
related: "[[DEFCON-System]], [[Analyse-Pipeline]], [[CapEx-FLAG]], [[ROIC-vs-WACC]], [[Non-US-Scoring]]"
entities: "[[ASML]], [[AVGO]], [[MSFT]], [[RMS]], [[VEEV]], [[SU]], [[BRKB]], [[V]], [[APH]], [[COST]], [[TMO]]"
datum: 2026-04-16
status: aktiv
---

# Wissenschaftliche Fundierung DEFCON v3.4

> Dieses Dokument belegt, dass das DEFCON-Scoring-System auf peer-reviewed Forschung basiert.
> 7 Quellen → 11 Befunde → operative Konsequenzen für das Dynasty-Depot.

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
| **B7** | Fundamentals > Sentiment > Technicals (ML-Datenhierarchie) | alle 4 Kern-Paper | Datenhierarchie | Gewichtung 50/10/10 Pt. bestätigt | Datenhierarchie explizit in !Analysiere benennen |
| **B8** | ROIC + FCF/EV + Operating Margin = top-ranked in allen ML-Modellen | [[Wolff-Echterling-2023]] | Fundamentals — ROIC/FCF | ROIC-Malus ist wissenschaftlich zwingend, nicht heuristisch | ROIC-vs-WACC Scoring direkt belegt; Non-US-Übertragbarkeit validiert |
| **B9** | EPS-Growth + Low Leverage = stabile Quality-Prädiktoren | [[Wolff-Echterling-2023]] | Fundamentals — Bilanz | Debt/EBITDA-Scoring wissenschaftlich fundiert | EPS Revision Momentum (+1 Bonus) + Bilanz-Block (9 Pt.) bestätigt |
| **B10** | Chain-of-Thought vor Scoring verbessert Konsistenz + Genauigkeit | [[llms-for-equity-stock-ratings]] | Workflow — !Analysiere | Begründen vor Scoren als Pflichtprinzip | Befunde-Priming in INSTRUKTIONEN.md (Stufe 2) verankert |
| **B11** | News-Daten erzeugen Positivity-Bias — mittelfristig schädlich | [[llms-for-equity-stock-ratings]], [[Jadhav-Mirza-2025]] | Sentiment (10 Pt.) | Sentiment-Gewichtung deckeln; Analyst-Bias (43% Strong Buy) gegensteuern | Sentiment-Cap 10 Pt. gerechtfertigt; Sell-Ratio-Check als Korrektiv |

---

## PFLICHT-Regeln (wörtlich, session-übergreifend)

### Aus Gu/Kelly/Xiu (2020):
> **"Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide."**
> Gilt in jeder DEFCON-Analyse. Fwd P/E ist Primärmetrik; trailing P/E höchstens als Kontext.

### Aus Buffetts Alpha (AQR 2018):
> **"Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality."**
> Gilt bei jeder BRK.B-Analyse und bei Leverage-Diskussionen.

---

## Quellen-Übersicht (7 Paper — Stand: 16.04.2026)

| Quelle | Jahr | Kernthese | DEFCON-Block | Neue Befunde |
|--------|------|-----------|--------------|-------------|
| [[arXiv-1711.04837]] | 2019 | ML + 5J-Fenster → +2,7% CAGR | Fundamentals 50% | B1, B7 |
| [[Gu-Kelly-Xiu-2020]] | 2020 | FCF+GM primär; trailing P/E schwach | Faktor-Kalibrierung | B2, B3, B7 |
| [[Morningstar-Wide-Moat]] | 2023 | 8 Moat-Quellen; Moat+Fundamentals nötig | Moat 20% | B4, B6 |
| [[Buffetts-Alpha]] | 2018 | QMJ+BAB+Value; Float nicht replizierbar | Fundamentals+Moat+BRK.B | B5 |
| [[Wolff-Echterling-2023]] | 2023 | ROIC+FCF top-ranked; STOXX-robust | Fundamentals ROIC/Bilanz | B8, B9 |
| [[llms-for-equity-stock-ratings]] | 2024 | Fundamentals > News; CoT verbessert Genauigkeit | Workflow + Sentiment | B10, B11 |
| [[Jadhav-Mirza-2025]] | 2025 | 84-Paper-Survey; News-Bias; RL+Memory | Sentiment + Architektur | B11 (Bestätigung) |

---

## Betroffene Entitäten

### Aktive Satelliten (Stand: 16.04.2026 — alle 11 vollständig gescort)

| Ticker | DEFCON | Score | FLAG | Relevante Befunde |
|--------|--------|-------|------|------------------|
| [[ASML]] | 🟡 3 | 68 | — | B1 (5J-EUV-Ramp), B4 (EUV-Monopol 100%), B6 (Fwd P/E 38x = Quality Trap ohne Bewertungsmarge), B8 (ROIC clean, Non-US-Übertragbarkeit) |
| [[AVGO]] | 🟢 4 | 86 | ⚠️ Insider-Check | B2 (FCF <15% CapEx = Fabless-Referenz), B4 (Chip+SW-Ökosystem Wide Moat), B5 (cheap+safe+quality erfüllt), B8 (ROIC >WACC +10% — Kalibrierungsanker) |
| [[MSFT]] | 🟠 2 | 60 | 🔴 CapEx >60% | B2 (CapEx/OCF 83,6% destroys FCF-Qualität), B3 (Finance-Lease-Bereinigung = Accrual-Komplexität), B6 (Score 60 bei Wide Moat 19/20 = Quality Trap aktiv), B8 (ROIC 7,5% < WACC 13,35% — wissenschaftlich nicht tragbar) |
| [[RMS]] | 🟢 4 | 69 | ✅ Clean | B4 (Marken-Moat: Hermès = 8/8 Moat-Quellen), B6 (Score 69 trotz ROIC 24% wegen Bewertung), B5 (safe: Netto-Cash +€9,89B) |
| [[VEEV]] | 🟢 4 | 74 | ✅ Clean | B2 (FCF-SaaS-Modell, CapEx-arm), B4 (Switching Costs Life-Sciences-Plattform), B3 (Earnings Quality hoch) |
| [[SU]] | 🟢 4 | 71 | ✅ Clean | B4 (Regulatory Moat Energie-Infrastruktur), B5 (safe-Komponente: ROIC 10,48% > WACC 8,96%), B8 (Profitability-Faktoren konsistent positiv) |
| [[BRKB]] | 🟢 4 | 75 | ✅ Clean | B5 vollständig (Float $686B = nicht replizierbar, aber cheap+safe+quality erfüllt), B9 (Low Leverage: Netto-Cash), B4 (Efficient Scale BNSF, Float-Moat) |
| [[V]] | 🟢 4 | 86 | ✅ Clean | B4 (Network Effects: 4,9 Mrd. Karten, Duopol), B2 (CapEx/OCF ~6% = Fabless-Niveau), B5 (cheap+safe+quality — Kalibrierungsanker #2), B8 (ROIC ~9,9%, Goodwill-Verzerrung durch Visa Europe) |
| [[APH]] | 🟡 3 | 61 | 🔴 Score-basiert | B2 (FCF-Marginen ok, aber Bewertung + CN/MY-Risk), B3 (Accrual-Komplexität Supply-Chain), B9 (Financial Leverage mittel) |
| [[COST]] | 🟢 4 | 69 | ✅ Clean | B4 (Cost Advantage: Membership-Loyalität 8/8 Moat-Quellen), B6 (GM 12,7% ≠ Qualitätsproblem — Geschäftsmodell), B9 (Low Leverage <1x) |
| [[TMO]] | 🟡 3 | 67 | — | B2 (FCF -13,4% YoY — Erosion), B3 (ROIC 2,6% unter WACC = negative Earnings Quality), B4 (Switching Costs Life-Sciences intakt), B8 (Goodwill $49,4B drückt ROIC unter Kapitalkosten) |

---

## Implikationen für SKILL-dynastie-depot.md

B7 verlangt explizite Dokumentation der Datenhierarchie in SKILL-dynastie-depot.md:
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
