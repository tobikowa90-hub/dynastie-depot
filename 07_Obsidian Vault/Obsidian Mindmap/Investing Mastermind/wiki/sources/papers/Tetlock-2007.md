---
title: "Giving Content to Investor Sentiment: The Role of Media in the Stock Market"
date: 2007
type: source
subtype: academic-paper
tags: [defcon, media-sentiment, investor-sentiment, noise-trader-model, mean-reversion, sentiment-block, b28]
url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2007.01232.x
venue: "Journal of Finance 62(3), 2007, 1139-1168"
authors: "Paul C. Tetlock (Columbia Business School / damals McCombs School of Business, University of Texas at Austin)"
status: processed
defcon_relevanz: "Befund B28 (`active-scoring`, neu seit 26.04.2026). Sentiment-Block (10 Pt.) — Kalibrierungs-Anker. Kern: Hohe Media-Pessimism prädiziert kurzfristig fallende Kurse + nachfolgende Reversion zu Fundamentals; ungewöhnlich hohe ODER niedrige Pessimism prädizieren hohes Trading-Volume. Das ist Noise-Trader/Liquidity-Trader-Modell-konsistent (DeLong/Shleifer/Summers/Waldmann 1990) und INKONSISTENT mit drei alternativen Hypothesen: Media als (a) Fundamental-Information-Proxy, (b) Volatility-Proxy, (c) Sideshow ohne Markt-Bezug. Operative Konsequenz für DEFCON: Sentiment-Block (Analyst-Konsensus + PT-Abstand + Sell-Ratio) wird durch B28 nicht erweitert (DEFCON nutzt strukturierten Analyst-Sentiment, kein Media-Text-Sentiment), aber B28 begründet die EXISTENZ des Sentiment-Blocks als kausal relevant — Sentiment ist nicht nur Rauschen, sondern hat empirisch messbaren Markt-Impact. Wichtig: B28's Mean-Reversion-Befund ist Anker für die DEFCON-Prämisse `Score = Long-Term-Quality-Bewertung, kein Short-Term-Trade-Signal` — kurzfristige Sentiment-Schwankungen sollten KEINEN Score-Drift triggern."
related: "[[Media-Pessimism-Sentiment]], [[Noise-Trader-Model]], [[News Sentiment Analysis]], [[Iacovides-Zhou-Mandic-2025-FinDPO]], [[Jadhav-Mirza-2025]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/Tetlock_Media_Sentiment_JF.pdf"
aliases:
  - "Tetlock 2007"
  - "Giving Content to Investor Sentiment"
  - "Media Pessimism Stock Returns"
---

# Tetlock (2007) — Media Sentiment & Stock Market

## Abstract (eigene Worte)

Tetlock konstruiert einen **Pessimism-Index** aus dem täglichen "Abreast of the Market"-Kolumne im Wall Street Journal (1984-1999, 16 Jahre, ~4.000 Beobachtungen). Methode: Harvard-IV-4 General-Inquirer-Wörterbuch mit 77 Kategorien → Principal-Components-Faktor-Analyse → 1 dominanter Pessimism-Faktor. Ergebnis in vector-autoregressionen (VARs):

1. **Hohe Media-Pessimism prädiziert kurzfristig fallende Kurse, gefolgt von Reversion zu Fundamentals** — konsistent mit Noise-Trader-Modell (DeLong/Shleifer/Summers/Waldmann 1990).
2. **Ungewöhnlich hohe ODER niedrige Pessimism prädizieren hohes Trading-Volume** — konsistent mit Liquidity-Trader-Modell (Campbell/Grossman/Wang 1993).
3. **Niedrige Markt-Returns führen zu hoher Media-Pessimism** — Media reflektiert past sentiment (bidirektional).

Statistische Tests **verwerfen** drei alternative Hypothesen:
- Media als Fundamental-Information-Proxy (würde persistente Returns implizieren, nicht Reversion)
- Media als Volatility-Proxy (Volume-Pattern wäre symmetrisch in Sign, nicht in Absolut-Wert)
- Media als Sideshow ohne Markt-Relevanz (würde keinen Effekt zeigen)

Das Paper ist die **kanonische Erstevidenz** für quantifizierbares Media-Sentiment als Markt-Faktor und ankert die nachfolgende Behavioral-Finance-Literatur (z.B. Tetlock/Saar-Tsechansky/Macskassy 2008, Antweiler/Frank 2004 → Internet-Chat-Sentiment, Da/Engelberg/Gao 2011 → Google Trends als Sentiment-Proxy).

## Drei Quantitativ-Befunde

| VAR-Befund | Magnitude | Horizont |
|---|---|---|
| Pessimism → Returns (negativ) | ~10-15 bps/Tag bei 1-σ-Pessimism-Schock | 1-3 Tage Drawdown |
| Reversion → Fundamentals | Komplette Reversion innerhalb ~5-10 Handelstage | Mittel-frist |
| Pessimism → Volume (Absolut-Wert) | +5-8% Volume bei 1-σ |Pessimism|-Schock | Same-day |

→ **Reversion-Pattern** ist der entscheidende Befund: Media-Pessimism erzeugt **temporären** Kursdruck, NICHT permanente Repricing — also Mispricing, nicht Information.

## DEFCON-Implikation (B28 `active-scoring`)

### Was B28 NICHT ändert

- **Sentiment-Block bleibt strukturell** (10 Pt.: Analyst-Konsensus 3 Pt. + PT-Abstand 3 Pt. + Sell-Ratio-Check 4 Pt.)
- **Kein Media-Text-Sentiment-Element** — DEFCON ist 4-Min-Score-Routine, Tetlock-Pipeline (GI-Wörterbuch + PCA + VAR) ist nicht in 4 Minuten replizierbar
- **Kein Sentiment-Time-Series-Filter** — DEFCON ist Snapshot-basiert, nicht VAR-basiert

### Was B28 begründet

1. **Existenz-Berechtigung des Sentiment-Blocks** — Vor B28 war Sentiment in der akademischen Literatur kontrovers (efficient-markets-Anhänger argumentierten "Sentiment = noise = irrelevant"). Tetlock liefert die erste robuste Empirik gegen die Sideshow-Hypothese. Sentiment-Block ist **wissenschaftlich anchored**, nicht ad-hoc.

2. **Mean-Reversion-Prinzip als DEFCON-Architektur-Anker:** Tetlock's Reversion-Befund (5-10 Tage) ist Mikro-Beweis für die DEFCON-Prämisse `Score = Long-Term-Quality, kein Short-Term-Trade-Signal`. Operative Konsequenz: **Kurzfristige Sentiment-Schwankungen (Tagesnachrichten, Earnings-Day-Volatility) sollen KEINEN Score-Drift triggern.** Score-Updates sind an strukturelle Trigger gebunden (Earnings, FLAG-Events, Watch-Resolves) — exakt das Anti-Tetlock-Pattern: vermeide noise-trader-mimicry.

3. **Crowd-Consensus-Malus-Validation (Block-Element B11):** B11 (Jadhav/Mirza 2025) führte den Crowd-Consensus-Malus für >60% Strong-Buy ein. B28 erweitert die Begründung: **Aggregate-Sentiment ist Mean-Reverting**. Hohe Strong-Buy-Konsentration → wahrscheinliche Mean-Reversion zur Mitte → Risiko-Signal. B11 + B28 kohärent.

### Komplementarität B28 ↔ B11 ↔ B19

| Befund | Quelle | Layer |
|---|---|---|
| **B11** | Jadhav/Mirza 2025 | Crowd-Consensus-Bias-Korrektur |
| **B19** | FINSABER 2026 | Bull/Bear-Asymmetrie + LLM-Investing-Bias-Audit |
| **B28** | Tetlock 2007 | Mean-Reversion-Anker für Score-Stabilität |
| **B24** | FinDPO 2025 | DPO-Pipeline für künftige Sentiment-Block-Architektur (orthogonal zu DEFCON heute) |

→ **Operative Schichtung:** Sentiment-Block hat 4 wissenschaftliche Anker (B11, B19, B24, B28) + 1 strukturelle Architektur-Konstante (Mean-Reversion-Prinzip).

## Methodische Würdigung

- **General Inquirer (GI) Wörterbuch:** 1960er-Methodologie, heute durch Loughran-McDonald (2011) Finance-Specific-Dictionary obsolet (LM eliminiert false-positives bei "liability", "vice", "tax" etc.). Tetlocks Befund replziert mit LM-Wörterbuch; Tetlock 2007 bleibt aber methodologisch erstmals-korrekt.
- **VAR-Approach:** Granger-Causality im engen Sinne — robust gegen einfache Endogeneität, aber nicht gegen Omitted-Variable-Bias (z.B. simultaneous Macro-Shocks). Tetlock kontrolliert für day-of-week + lagged-returns.
- **Sample-Generalisierbarkeit:** 16 Jahre 1984-1999 — pre-Internet-Era für Investor-Information. Online-News + Social-Media (Twitter post-2008) verändern Sentiment-Transmission-Kanäle. Replikationen (Tetlock 2008, García 2013) bestätigen Kern-Befund über Pre/Post-Internet-Periode.

## Operative Schlussfolgerungen

1. **B28 deaktiviert KEINEN bestehenden Score-Pfad** — Sentiment-Block bleibt strukturell.
2. **B28 begründet die Existenz** des Sentiment-Blocks empirisch + ankert die Mean-Reversion-Architektur-Wahl.
3. **Anker für `feedback_score_stability_over_drift.md`-Memory** (geplant, falls Brainstorm Konsolidierungstag): Score soll an strukturelle Trigger gebunden sein, nicht an Tagesnachrichten — Tetlock zeigt empirisch, warum kurzfristiges Sentiment Mean-reverted und kein Score-relevantes Signal sein kann.
4. **Watch-Item für insider-intelligence v3 / Sentiment-Erweiterung 2027+:** Falls künftig Media-Text-Sentiment integriert werden soll, ist Tetlock + Loughran-McDonald die Methoden-Referenz, mit FinDPO (B24) als modernem ML-Backend.

## Backlinks

- [[Media-Pessimism-Sentiment]] — neue Concept-Page (B28-Anker)
- [[Noise-Trader-Model]] — neue Concept-Page (DeLong/Shleifer/Summers/Waldmann 1990)
- [[News Sentiment Analysis]] — bestehendes Konzept, B28 als kanonische Primärquelle
- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — moderner ML-Counterpart
- [[Jadhav-Mirza-2025]] — komplementärer Sentiment-Bias-Befund (B11)
- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — Bias-Audit-Pattern (B19)
- [[DEFCON-System]] — Sentiment-Block 10 Pt.
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B28
- [[Paul Tetlock]] — Author-Entity
