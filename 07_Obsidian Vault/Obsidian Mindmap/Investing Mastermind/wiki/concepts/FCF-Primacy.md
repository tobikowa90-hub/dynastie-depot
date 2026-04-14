---
title: "FCF-Primacy"
type: concept
tags: [defcon, fcf, bewertung, forward-pe, trailing-pe, earnings-quality]
source: "[[Gu-Kelly-Xiu-2020]]"
related: "[[DEFCON-System]], [[CapEx-FLAG]], [[5J-Fundamental-Fenster]], [[Wissenschaftliche-Fundierung-DEFCON]], [[ASML]], [[AVGO]], [[MSFT]], [[RMS]], [[VEEV]], [[SU]], [[BRKB]], [[V]], [[APH]], [[COST]], [[TMO]]"
defcon_block: "Fundamentals (50 Pt.) — P/FCF + Fwd P/E"
operative_regel: "PFLICHT: Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide. FCF-Yield und P/FCF sind primäre Bewertungsanker."
---

# FCF-Primacy

## Definition
FCF-Primacy bezeichnet den wissenschaftlich belegten Vorrang von Free-Cash-Flow-Metriken und Forward P/E gegenüber Trailing P/E als Rendite-Prädiktoren. Gu, Kelly und Xiu (2020, RFS) zeigen, dass FCF-Yield und Gross Margin konsistent zu den top-2 Features in allen getesteten ML-Architekturen zählen. Trailing P/E erscheint nicht in den Top-10-Features und verliert nach 12-monatigem Horizont signifikant an Vorhersagekraft.

## Wissenschaftliche Basis
Quelle: [[Gu-Kelly-Xiu-2020]] — Review of Financial Studies 2020

Feature-Importance-Reihenfolge (ML-Konsens über Random Forest, Neural Net, Lasso):
1. FCF-Yield ← primär
2. Gross Margin ← primär
3. Accrual Ratio
4. Forward P/E ← valide
5. P/FCF (trailing) ← valide
n/a. **Trailing P/E** ← nicht in Top 10, Vorhersagekraft verloren

## PFLICHT-Regel (wörtlich, in jeder Datei dokumentiert)

> **"Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide."**
>
> — Gu, Kelly, Xiu (2020)

Diese Regel gilt verbindlich in jeder DEFCON-Analyse:
- Fwd P/E (8 Pt.) → weiterhin als Primärmetrik einsetzen ✅
- P/FCF (8 Pt.) → weiterhin als Primärmetrik einsetzen ✅
- Trailing P/E → höchstens als Kontext, nicht als Scoring-Basis ⚠️

## Operative DEFCON-Anwendung

| Scoring-Block | Metrik | Status nach FCF-Primacy |
|--------------|--------|------------------------|
| Fundamentals | Fwd P/E (8 Pt.) | Primäranker — unverändert ✅ |
| Fundamentals | P/FCF (8 Pt.) | Primäranker — bestätigt ✅ |
| Fundamentals | FCF Yield (8 Pt.) | Top-1-Feature — aufgewertet ✅ |
| Bonus-Metriken | Accrual Ratio | Top-3-Feature — relevant |
| Bonus-Metriken | GM-Trend | Top-2-Proxy — relevant |
| Kontext-only | Trailing P/E | Nicht im Scoring |

## DEFCON-Relevanz nach Ticker

Alle 11 Satelliten sind betroffen — FCF-Primacy gilt universal:

| Ticker | FCF-Besonderheit |
|--------|-----------------|
| [[AVGO]] | Fabless-Modell: CapEx/OCF <15% → FCF-Qualität Top-Score |
| [[MSFT]] | CapEx-FLAG durch hohe Investitionen → FCF-Druck temporär |
| [[ASML]] | FCF Yield ~2,4% (Bewertungsproblem, kein Qualitätsproblem) |
| [[TMO]] | FCF -13,4% YoY (Clario-Integration) → Klasse-B-Trigger |
| [[COST]] | Low GM strukturell (Geschäftsmodell) → Screener-Exception |
| [[BRKB]], [[V]], [[RMS]], [[SU]], [[VEEV]], [[APH]] | FCF-Analyse ausstehend |

## Backlinks
- [[Gu-Kelly-Xiu-2020]] — Primärquelle
- [[CapEx-FLAG]] — FCF-Qualität zentral für FLAG-Auslösung
- [[DEFCON-System]] — Scoring-Gewichtung
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B2 + B3
