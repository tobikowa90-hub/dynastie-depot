---
title: "Media Pessimism Sentiment"
type: concept
tags: [defcon, sentiment, media-text, pessimism-index, mean-reversion, b28, design-context]
created: 2026-04-26
updated: 2026-04-27
sources: [Tetlock-2007]
related: [Wissenschaftliche-Fundierung-DEFCON, Noise-Trader-Model, news-sentiment-analysis, Iacovides-Zhou-Mandic-2025-FinDPO, Jadhav-Mirza-2025, DEFCON-System]
wissenschaftlicher_anker: "B28 (Tetlock 2007, JF 62(3)) — Pessimism-Index aus WSJ 'Abreast of the Market'-Kolumne (1984-1999, 16J): Hohe Media-Pessimism prädiziert kurzfristig fallende Kurse + Reversion zu Fundamentals (5-10 Tage); ungewöhnlich hohe ODER niedrige Pessimism prädizieren hohes Trading-Volume (Liquidity-Trader-Modell). Verwirft drei Alternativen: Information-Proxy / Volatility-Proxy / Sideshow."
konfidenzstufe: peer-reviewed
defcon_block: "Sentiment-Block (10 Pt.) — Architektur-Anker, kein Score-Element"
operative_regel: "Score-Stabilität-Anker: Score-Updates an strukturelle Trigger gebunden (Earnings, FLAG-Events, Watch-Resolves), NICHT an kurzfristige Sentiment-Schwankungen — Tetlock zeigt empirisch warum (5-10-Tage-Reversion zu Fundamentals)."
aliases:
  - "Media Pessimism"
  - "Tetlock Pessimism Index"
---

# Media Pessimism Sentiment

> Tetlock (2007) konstruiert einen Pessimism-Index aus dem WSJ „Abreast of the Market"-Kolumne via Harvard-IV-4 General-Inquirer-Wörterbuch (77 Kategorien, PCA-Faktor). Hohe Media-Pessimism erzeugt temporären Kursdruck, der innerhalb 5-10 Handelstagen zu Fundamentals reverted. Das ist Mispricing, nicht Information.

## Definition

**Media Pessimism Sentiment** = quantifizierbarer textueller Sentiment-Index aus Finanz-Nachrichten, operationalisiert via dictionary-basierte Word-Counts mit Faktor-Analyse. Tetlocks Methode ist die kanonische Erstevidenz für Media-Sentiment als Markt-Faktor und Anker für die nachfolgende Behavioral-Finance-Literatur.

## Drei Quantitativ-Befunde (sekundär-zitierte Magnituden)

⚠️ **Confidence:** Konkrete bps-Werte sind sekundär-zitiert (Replikationen Tetlock 2008 + García 2013); inhaltliches Pattern HOCH-konfident.

| VAR-Befund | Magnitude (sekundär) | Horizont |
|---|---|---|
| Pessimism → Returns (negativ) | ~10-15 bps/Tag bei 1-σ-Pessimism-Schock | 1-3 Tage Drawdown |
| Reversion → Fundamentals | Komplette Reversion innerhalb 5-10 Handelstage | Mittel-frist |
| Pessimism → Volume (Absolut-Wert) | +5-8% Volume bei 1-σ |Pessimism|-Schock | Same-day |
| Niedrige Markt-Returns → hohe Media-Pessimism | bidirektional | Same-week |

## Drei verworfene Alternativen

| Hypothese | Empirische Implikation | Tetlock-Befund |
|---|---|---|
| Media als Fundamental-Information-Proxy | Persistente Returns (kein Reversion) | **Verworfen** — Reversion innerhalb 5-10 Tagen widerspricht |
| Media als Volatility-Proxy | Volume-Pattern symmetrisch in Sign | **Verworfen** — Volume-Pattern in Absolut-Wert (Liquidity-Trader-Modell) |
| Media als Sideshow ohne Markt-Relevanz | Kein Effekt | **Verworfen** — Robust signifikante VAR-Beziehungen |

→ **Mean-Reversion-Pattern** ist der entscheidende Befund: Media-Pessimism erzeugt **temporären** Kursdruck, NICHT permanente Repricing — also Mispricing, nicht Information.

## DEFCON-Implikation: Architektur-Anker, kein Score-Element

### Was B28 NICHT ändert

- Sentiment-Block bleibt strukturell (10 Pt.: Analyst-Konsensus 3 Pt. + PT-Abstand 3 Pt. + Sell-Ratio-Check 4 Pt.)
- KEIN Media-Text-Sentiment-Element — DEFCON ist 4-Min-Score-Routine, Tetlock-Pipeline (GI-Wörterbuch + PCA + VAR) ist nicht in 4 Minuten replizierbar
- KEIN Sentiment-Time-Series-Filter — DEFCON ist Snapshot-basiert, nicht VAR-basiert

### Was B28 begründet

1. **Existenz-Berechtigung des Sentiment-Blocks** — Vor B28 war Sentiment in der akademischen Literatur kontrovers (efficient-markets-Anhänger argumentierten „Sentiment = noise = irrelevant"). Tetlock liefert die erste robuste Empirik gegen die Sideshow-Hypothese. Sentiment-Block ist **wissenschaftlich anchored**, nicht ad-hoc.

2. **Mean-Reversion-Prinzip als DEFCON-Architektur-Anker** — Tetlock's Reversion-Befund (5-10 Tage) ist Mikro-Beweis für die DEFCON-Prämisse `Score = Long-Term-Quality, kein Short-Term-Trade-Signal`. Operative Konsequenz: **Kurzfristige Sentiment-Schwankungen (Tagesnachrichten, Earnings-Day-Volatility) sollen KEINEN Score-Drift triggern.** Score-Updates sind an strukturelle Trigger gebunden (Earnings, FLAG-Events, Watch-Resolves) — exakt das Anti-Tetlock-Pattern: vermeide noise-trader-mimicry.

3. **Crowd-Consensus-Malus-Validation (B11)** — B11 (Jadhav/Mirza 2025) führte den Crowd-Consensus-Malus für >60% Strong-Buy ein. B28 erweitert die Begründung: **Aggregate-Sentiment ist Mean-Reverting**. Hohe Strong-Buy-Konsentration → wahrscheinliche Mean-Reversion zur Mitte → Risiko-Signal. B11 + B28 kohärent.

## Komplementarität B28 ↔ B11 ↔ B19 ↔ B24

| Befund | Quelle | Layer |
|---|---|---|
| **B11** | Jadhav/Mirza 2025 | Crowd-Consensus-Bias-Korrektur |
| **B19** | FINSABER 2026 | Bull/Bear-Asymmetrie + LLM-Investing-Bias-Audit |
| **B28** | Tetlock 2007 | Mean-Reversion-Anker für Score-Stabilität |
| **B24** | FinDPO 2025 | DPO-Pipeline für künftige Sentiment-Block-Architektur (orthogonal) |

→ **Operative Schichtung:** Sentiment-Block hat 4 wissenschaftliche Anker (B11, B19, B24, B28) + 1 strukturelle Architektur-Konstante (Mean-Reversion-Prinzip).

## Methodische Würdigung

- **General Inquirer (GI) Wörterbuch:** 1960er-Methodologie, heute durch Loughran-McDonald (2011) Finance-Specific-Dictionary obsolet (LM eliminiert false-positives bei „liability", „vice", „tax" etc.). Tetlocks Befund repliziert mit LM-Wörterbuch; Tetlock 2007 bleibt aber methodologisch erstmals-korrekt.
- **VAR-Approach:** Granger-Causality im engen Sinne — robust gegen einfache Endogeneität, aber nicht gegen Omitted-Variable-Bias (z.B. simultane Macro-Shocks). Tetlock kontrolliert für day-of-week + lagged-returns.
- **Sample-Generalisierbarkeit:** 16 Jahre 1984-1999 — pre-Internet-Era für Investor-Information. Online-News + Social-Media (Twitter post-2008) verändern Sentiment-Transmission-Kanäle. Replikationen (Tetlock 2008, García 2013) bestätigen Kern-Befund über Pre/Post-Internet-Periode.

## Operative Anwendung

1. **Architektur-Anker** für `feedback_score_stability_over_drift`-Memory (geplant Konsolidierungstag): Score soll an strukturelle Trigger gebunden sein, nicht an Tagesnachrichten.
2. **Briefing-Disziplin:** Tagesnachrichten zu einem Ticker triggern KEINEN automatischen Score-Update, auch wenn die Magnitude stark erscheint. Erst strukturelle Auslöser (Earnings, FLAG-Trigger, Watch-Resolve, Score-Alter >180 Tage) → !Analysiere.
3. **Watch-Item für insider-intelligence v3 / Sentiment-Erweiterung 2027+:** Falls künftig Media-Text-Sentiment integriert werden soll, ist Tetlock + Loughran-McDonald die Methoden-Referenz, mit FinDPO (B24) als modernem ML-Backend.

## Limitationen

- **Tagesnachrichten ≠ Earnings-Day:** Earnings-Day-Volatility ist KEIN Tetlock-Pessimism-Pattern; sie ist strukturelles Information-Event und triggert §6b FLAG-Resolution-Check + ggf. !Analysiere.
- **Magnitude-Bands sind sekundär:** Konkrete bps-Werte aus dieser Page nicht für Briefings/Score-Begründungen verwenden — nur das inhaltliche Reversion-Pattern ist Score-relevant.

## Backlinks

- [[Tetlock-2007]] — Primärquelle (B28, `design-context`)
- [[Noise-Trader-Model]] — DeLong/Shleifer/Summers/Waldmann 1990 als theoretischer Anker
- [[news-sentiment-analysis]] — bestehendes Konzept, B28 als kanonische Primärquelle
- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — moderner ML-Counterpart (B24, `future-arch`)
- [[Jadhav-Mirza-2025]] — komplementärer Sentiment-Bias-Befund (B11, `active-scoring`)
- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — Bias-Audit-Pattern (B19, `meta-gate`)
- [[DEFCON-System]] — Sentiment-Block 10 Pt.
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B28
