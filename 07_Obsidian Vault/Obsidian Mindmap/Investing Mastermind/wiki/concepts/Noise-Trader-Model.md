---
title: "Noise-Trader-Modell (DeLong/Shleifer/Summers/Waldmann 1990)"
type: concept
tags: [defcon, behavioral-finance, noise-trader, mean-reversion, mispricing, theoretical-anchor, design-context]
created: 2026-04-26
updated: 2026-04-27
sources: [Tetlock-2007]
related: [Wissenschaftliche-Fundierung-DEFCON, Media-Pessimism-Sentiment, news-sentiment-analysis, DEFCON-System]
wissenschaftlicher_anker: "DeLong, Shleifer, Summers & Waldmann (1990, JPE 98(4) 'Noise Trader Risk in Financial Markets') — theoretisches Modell, in dem irrationale Noise-Traders neben rationalen Arbitrageuren agieren. Noise-Trader-Sentiment-Schwankungen erzeugen kurzfristige Mispricings, die langsam zu Fundamentals revertieren — exakt das Pattern, das Tetlock (2007, B28) empirisch für Media-Pessimism dokumentiert."
konfidenzstufe: theoretical-foundation
defcon_block: "Theoretischer Anker für Sentiment-Block-Mean-Reversion-Architektur (B28); kein direkter Score-Pfad"
operative_regel: "Mean-Reversion ist erwartetes Equilibrium-Verhalten in Märkten mit Noise-Traders; kurzfristige Sentiment-Drifts triggern KEINEN Score-Update."
aliases:
  - "DSSW 1990"
  - "Noise Trader Risk"
  - "DeLong Shleifer Summers Waldmann"
---

# Noise-Trader-Modell (DeLong, Shleifer, Summers & Waldmann 1990)

> Klassisches Behavioral-Finance-Modell: In Märkten mit zwei Akteurs-Klassen (rationale Arbitrageure + irrationale Noise-Traders mit zufälligem Sentiment) erzeugen Noise-Trader-Sentiment-Schwankungen kurzfristige Preis-Abweichungen vom Fundamentalwert. Diese Mispricings revertieren langsam, weil rationale Arbitrageure begrenzte Time-Horizons haben und Noise-Trader-Risk nicht vollständig wegarbitrieren können.

## Definition

**Noise-Trader-Modell** = theoretisches Equilibrium-Modell mit zwei Akteurs-Klassen:
1. **Rationale Arbitrageure** — handeln nach Bayes-Updates über Fundamentalwerte; haben begrenzte Time-Horizons (Marktbewertung, Career-Risk).
2. **Noise-Traders** — handeln nach zufälligem Sentiment, das nicht mit Fundamentals korreliert; ihre Erwartungen sind systematisch verzerrt.

**Kernergebnis:** Noise-Trader-Sentiment-Schwankungen sind ein eigenständiger Risikofaktor — ihr Sentiment kann persistente Preis-Abweichungen vom Fundamentalwert erzeugen, weil rationale Arbitrageure NICHT vollständig arbitrieren können (Risk-Aversion + begrenzte Time-Horizons + Limits-of-Arbitrage).

## Vier Modell-Implikationen

| Implikation | Mechanismus | Empirische Validierung |
|---|---|---|
| **Mean-Reversion** | Mispricings revertieren langsam zu Fundamentals (über Tage bis Wochen) | [[Tetlock-2007]] B28: 5-10-Tage-Reversion nach Pessimism-Schock |
| **Excess Volatility** | Preis-Schwankungen übersteigen Fundamentalwert-Schwankungen | Shiller (1981) Excess Volatility-Tests |
| **Closed-End-Fund-Discount** | NAV-Discount-Schwankungen reflektieren Noise-Trader-Sentiment | Lee/Shleifer/Thaler (1991) — gleichzeitige Discount-Schwankungen verschiedener Funds = aggregate-Sentiment-Faktor |
| **Crowded-Trade-Risiko** | Korrelationen zwischen ähnlichen Strategies steigen in Stress-Events | McLean/Pontiff (2016) B25: Post-Publication-Correlation-Increase |

## Beziehung zu DEFCON

### Theoretischer Anker für B28 Mean-Reversion-Architektur

Tetlock (2007) operationalisiert das DSSW-Modell empirisch: Media-Pessimism = Proxy für Noise-Trader-Sentiment, Reversion innerhalb 5-10 Tagen = empirische Bestätigung des Mean-Reversion-Pattern. Diese Verbindung Theorie-Empirie ist der wissenschaftliche Grund, warum DEFCON-Score-Updates an strukturelle Trigger gebunden sind, NICHT an kurzfristige Sentiment-Schwankungen.

### Theoretischer Anker für Block-Gewichtung

DSSW liefert auch theoretische Begründung für die Fundamentals-Dominanz im DEFCON-Scoring (50/20/10/10/10):
- **Noise-Trader-Sentiment** wirkt primär auf Technicals + Sentiment (Tagesnachrichten, Crowd-Trades)
- **Fundamentals + Moat** sind langsamer arbitrierbar (Limits-of-Arbitrage höher) → strukturell robusterer Cross-Section-Predictor
- McLean/Pontiff (2016) B25 bestätigt: Fundamentals-/Accounting-Predictoren decayen langsamer als Price-/Trading-only-Predictoren post-publication

### Theoretischer Anker für FLAG-Architektur

FLAGs (CapEx/OCF, FCF-Trend, Insider-Selling, Tariff-Exposure) sind strukturelle Trigger — sie reagieren auf Fundamental-Veränderungen, nicht auf Sentiment-Schwankungen. Das ist DSSW-konsistent: Score-Stabilität gegen Noise-Trader-Druck ist Architektur-Disziplin, nicht Reaktivität.

## Komplementarität zu anderen Behavioral-Finance-Ankern

- **Limits-of-Arbitrage** (Shleifer/Vishny 1997, Behavioral-Finance-Klassiker): Liefert die operative Begründung warum Noise-Trader-Mispricing nicht sofort arbitriert wird (Margin-Calls, Capital-Flow-Pressure).
- **Investor-Sentiment** (Baker/Wurgler 2006, 2007): Operationalisiert Aggregate-Sentiment via Closed-End-Fund-Discount, IPO-Volume, IPO-First-Day-Returns, Equity-Issuance — komplementär zu Tetlock-Media-Sentiment.
- **Behavioral Asset Pricing** (Daniel/Hirshleifer/Subrahmanyam 1998): Overconfidence + Self-Attribution-Bias als Microfoundation für Noise-Trader-Sentiment.

## Limitationen

- **Theoretisches Modell:** DSSW ist Equilibrium-Modell mit starken Annahmen (zwei Akteurs-Klassen, OLG-Struktur, exogenes Sentiment). Reale Marktstrukturen sind komplexer (HFT, Quants, Retail-Robinhood-Welle 2020+).
- **Empirische Operationalisierung:** Noise-Trader-Sentiment ist nicht direkt beobachtbar; Proxies (Media-Sentiment, Closed-End-Fund-Discount, IPO-Volume) sind sekundär. Tetlock 2007 ist eine der robustesten empirischen Operationalisierungen.
- **Post-Internet-Ära:** Social-Media + Algorithmic-Trading verändern Sentiment-Transmission-Kanäle. Modern Noise-Trader = Retail-Robinhood + Twitter-Sentiment + Reddit-Subreddits — andere Kanäle als 1990er-WSJ-Pessimism, aber Modell-Mechanismus überträgt.

## Backlinks

- [[Tetlock-2007]] — empirische Operationalisierung des DSSW-Pattern (B28, `design-context`)
- [[Media-Pessimism-Sentiment]] — Concept-Page für die operative Tetlock-Pessimism-Methode
- [[news-sentiment-analysis]] — bestehende Konzept-Page für Sentiment-Methoden
- [[McLean-Pontiff-2016]] — Crowded-Trade-Risiko-Ergänzung (B25, `meta-gate`)
- [[DEFCON-System]] — Block-Gewichtung 50/20/10/10/10 strukturell DSSW-konsistent
- [[Wissenschaftliche-Fundierung-DEFCON]] — Theoretischer Anker (zitiert in B28-Begründung)
