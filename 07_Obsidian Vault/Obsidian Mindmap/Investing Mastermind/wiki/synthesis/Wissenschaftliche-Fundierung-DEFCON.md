---
title: "Wissenschaftliche Fundierung DEFCON v3.4"
type: synthesis
tags: [defcon, scoring, wissenschaft, entscheidungsmatrix, faktor-kalibrierung]
sources: "[[arXiv-1711.04837]], [[Gu-Kelly-Xiu-2020]], [[Morningstar-Wide-Moat]], [[Buffetts-Alpha]]"
concepts: "[[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]], [[Buffett-Faktorlogik]], [[QMJ-Faktor]]"
related: "[[DEFCON-System]], [[Analyse-Pipeline]], [[CapEx-FLAG]], [[ROIC-vs-WACC]]"
entities: "[[ASML]], [[AVGO]], [[MSFT]], [[RMS]], [[VEEV]], [[SU]], [[BRKB]], [[V]], [[APH]], [[COST]], [[TMO]]"
datum: 2026-04-14
status: aktiv
---

# Wissenschaftliche Fundierung DEFCON v3.4

> Dieses Dokument belegt, dass das DEFCON-Scoring-System auf peer-reviewed Forschung basiert.
> 4 Quellen → 7 Befunde → operative Konsequenzen für das Dynasty-Depot.

---

## 7-Befunde Entscheidungsmatrix

| # | Befund | Quelle | Block | Empfehlung | Konsequenz |
|---|--------|--------|-------|------------|------------|
| **B1** | 5J-Fenster > Spot als Rendite-Prädiktor (+2,7% CAGR) | [[arXiv-1711.04837]] | Fundamentals (50 Pt.) | 5J-Perspektive als Pflichtrahmen | 5J-Trend in jeder Analyse prüfen |
| **B2** | FCF + Gross Margin = stabilste Prädiktoren (Top-2 ML-Features) | [[Gu-Kelly-Xiu-2020]] | Fundamentals — FCF/GM | Trailing P/E de-priorisieren; forward P/E valide | P/FCF + Fwd P/E bleiben primär; trailing P/E nur Kontext |
| **B3** | Earnings-Quality > Value (Accrual Ratio top-3 Feature) | [[Gu-Kelly-Xiu-2020]] | Fundamentals — Qualität | FCF-Qualität und GM-Trend aufwerten | Bonus-Metriken Accrual Ratio + GM-Trend bestätigt |
| **B4** | 8 Moat-Quellen operativ identifiziert | [[Morningstar-Wide-Moat]] | Moat (20 Pt.) | 8-Quellen-Checkliste im Moat-Block | Jede Moat-Analyse prüft alle 8 Quellen |
| **B5** | Buffetts Alpha = QMJ + BAB + Value (vollständig erklärt) | [[Buffetts-Alpha]] | Fundamentals + Moat | cheap+safe+quality als operativer Dreiklang | DEFCON-4-Kriterien = cheap+safe+quality |
| **B6** | Moat allein ≠ Excess Return (Quality Trap ohne Bewertung) | [[Morningstar-Wide-Moat]] | Moat + Bewertung | Wide Moat immer mit Bewertungsdisziplin | Kombination Moat + Fundamentals ist Pflicht |
| **B7** | Fundamentals > Sentiment > Technicals (ML-Datenhierarchie) | alle 4 Quellen | Datenhierarchie | Gewichtung 50/10/10 Pt. bestätigt | SKILL-dynastie-depot.md: Datenhierarchie explizit benennen |

---

## PFLICHT-Regeln (wörtlich, session-übergreifend)

### Aus Gu/Kelly/Xiu (2020):
> **"Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide."**
> Gilt in jeder DEFCON-Analyse. Fwd P/E ist Primärmetrik; trailing P/E höchstens als Kontext.

### Aus Buffetts Alpha (AQR 2018):
> **"Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality."**
> Gilt bei jeder BRK.B-Analyse und bei Leverage-Diskussionen.

---

## Quellen-Übersicht

| Quelle | Jahr | Kernthese | DEFCON-Block |
|--------|------|-----------|--------------|
| [[arXiv-1711.04837]] | 2019 | ML + 5J-Fenster → +2,7% CAGR | Fundamentals 50% |
| [[Gu-Kelly-Xiu-2020]] | 2020 | FCF+GM primär; trailing P/E schwach | Faktor-Kalibrierung |
| [[Morningstar-Wide-Moat]] | 2023 | 8 Moat-Quellen; Moat+Fundamentals nötig | Moat 20% |
| [[Buffetts-Alpha]] | 2018 | QMJ+BAB+Value; Float nicht replizierbar | Fundamentals+Moat+BRK.B |

---

## Konzept-Karte

```
arXiv-1711.04837 ──────► [[5J-Fundamental-Fenster]] ──► alle 11 Ticker
Gu-Kelly-Xiu-2020 ─────► [[FCF-Primacy]] ─────────────► alle 11 Ticker
Morningstar-Wide-Moat ─► [[Moat-Taxonomie-Morningstar]] ► alle 11 Ticker
Buffetts-Alpha ─────────► [[Buffett-Faktorlogik]] ──────► [[BRKB]]
                └──────► [[QMJ-Faktor]] ────────────────► [[BRKB]]

Alle 4 Quellen + alle 5 Konzepte → DEFCON v3.4 (wissenschaftlich validiert)
```

---

## Betroffene Entitäten

### Aktive Satelliten (Stand: 14.04.2026)

| Ticker | DEFCON | Score | Relevante Befunde |
|--------|--------|-------|------------------|
| [[ASML]] | 🟡 3 | 68 | B1 (5J-Ramp), B4 (EUV-Monopol), B6 (Premium-Bewertung) |
| [[AVGO]] | 🟢 4 | 86 | B2 (FCF-Qualität), B4 (Chip-Ökosystem), B5 (cheap+safe+quality) |
| [[MSFT]] | 🟠 2 | 60 | B2 (CapEx-Druck auf FCF), B3 (FCF-Qualität), B6 (Premium-Bewertung) |
| [[RMS]] | 🟢 4 | ausstehend | B4 (Marken-Moat), B6 (Bewertungsdisziplin nötig) |
| [[VEEV]] | 🟢 4 | ausstehend | B2 (FCF-SaaS-Modell), B4 (Switching Costs) |
| [[SU]] | 🟢 4 | ausstehend | B4 (Regulatory Moat), B5 (safe-Komponente) |
| [[BRKB]] | 🟢 4 | ausstehend | B5 vollständig — Float nicht replizieren! |
| [[V]] | 🟢 4 | ausstehend | B4 (Network Effects), B2 (FCF-Qualität) |
| [[APH]] | 🟢 4 | ausstehend | B2 (FCF-Marginen), B4 (Switching Costs) |
| [[COST]] | 🟢 4 | ausstehend | B4 (Cost Advantage), B6 (Low GM = Geschäftsmodell, kein Qualitätsproblem) |
| [[TMO]] | 🟡 3 | 67 | B2 (FCF-Rückgang), B4 (Switching Costs), B5 (safe-Komponente unter Druck) |

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

## Änderungsprotokoll

| Datum | Änderung |
|-------|---------|
| 2026-04-14 | Erstellt — 4 Paper, 7 Befunde, vollständige Backlink-Vernetzung |
