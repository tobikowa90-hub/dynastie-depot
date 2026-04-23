---
title: "Factor Information Decay: A Global Study"
date: 2021-12
type: source
subtype: academic-paper
tags: [factor-decay, half-life, rebalancing, cadence, temporal-validation]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3986499
alphaarchitect_summary: https://alphaarchitect.com/information-decay/
quantpedia_summary: https://quantpedia.com/how-often-should-we-rebalance-equity-factor-portfolios/
authors: "Emlyn Flint, Rademeyer Vermaak"
status: processed
defcon_relevanz: "Validiert unsere Earnings-Trigger-Cadence (~3 Monate) als wissenschaftlich fundiert für Value/Quality/Momentum. Keine System-Änderung nötig. §29.3 Temporal-Konsistenz-Check bei Review 2028. Watch: Investment-Faktor-Half-Life = 1 Monat → bei aktiven FLAGs (MSFT CapEx, TMO fcf_trend_neg) Monthly-Fundamentals-Refresh erwägen."
related: "[[Factor-Information-Decay]], [[Factor-Investing-Framework]], [[Update-Klassen-DEFCON]], [[DEFCON-System]], [[Backtest-Methodik-Roadmap]], [[Wissenschaftliche-Fundierung-DEFCON]]"
---

# Flint, Vermaak — Factor Information Decay: A Global Study (2021)

## Abstract (eigene Worte)
Flint und Vermaak untersuchen empirisch, wie schnell Faktor-Exposures von Equity-Faktor-Strategien ihren Informationswert verlieren. Sie führen eine **Half-Life-Metrik** ein und messen sie für 5 Faktoren (Value, Momentum, Quality, Investment, Low Volatility) über 12 Entwickelte + Emerging Markets, 20 Jahre Daten, 36-Monats-Holding-Analyse auf Pure + Quartile Long/Short-Portfolios. Kern-Finding: Faktoren decayen **sehr unterschiedlich schnell** — Value am langsamsten, Investment am schnellsten. Daraus leiten sich **faktor-spezifische optimale Rebalance-Perioden** ab, die unser Earnings-Trigger-Design implizit bestätigen.

## Kern-Ergebnisse — Optimale Rebalance-Periode

| Faktor | Optimale Rebalance-Periode | Decay-Tempo (Ranking) |
|---|---|---|
| **Value** | 3–4 Monate | Langsamster Decay |
| **Low Volatility** | 5–6 Monate | ↓ |
| **Quality** | 4–5 Monate (Pure Half-Life **25,9 Monate**) | ↓ |
| **Momentum** | 3 Monate | ↓ |
| **Investment** | 1 Monat | Schnellster Decay (median-halving <6M) |

**Interpretations-Hinweis:** Quality hat sehr lange Pure-Factor-Half-Life (~26 Monate), aber die *optimale* Rebalance-Periode ist deutlich kürzer, weil Quartile-Portfolio-Zusammensetzung schneller driftet als aggregierte Exposure.

## DEFCON-Implikation — Cadence-Alignment

| DEFCON-Block | Faktor-Analog | Flint/Vermaak optimal | Unsere Cadence | Alignment |
|---|---|---|---|---|
| `fundamentals` (Fwd P/E, P/FCF) | Value | 3–4 Monate | Earnings-Trigger (~3M US-Quartale) | ✅ **passt exakt** |
| `moat` + Quality-Teile | Quality | 4–5 Monate | Earnings-Trigger + jährliche Vollanalyse | ✅ **konservativ ok** |
| `technicals` | Momentum | 3 Monate | Earnings-Trigger + Monitor | ✅ **passt** |
| `fundamentals` (CapEx/OCF, ROIC) | Investment | **1 Monat** | Earnings-Trigger (~3M) | ⚠️ **zu träge** bei aktiven FLAGs |
| — | Low Volatility | 5–6 Monate | nicht explizit getrackt | — |
| `insider` | **Kein AQR-Analog** | täglich via OpenInsider | Real-time Scan | ✅ Edge |

## Offene Frage: Monthly Investment-Refresh?

MSFT-CapEx/OCF-FLAG (83,6%) und TMO-`fcf_trend_neg`-Disclosure sind **Investment-Klasse-Signale**. Paper suggeriert 1-Monat-Half-Life. Aktueller Stand:
- `!Briefing` (daily) fängt Preise + News ab
- Fundamental-Re-Check bei uns quarterly an Earnings gebunden
- **Gap:** zwischen Earnings-Zyklen kein formaler Investment-Signal-Refresh

**Aktivierung offen.** Entscheidung: bei Review 2028 anhand beobachteter FLAG-Event-Trajektorien. Jetzt keine Änderung — FLAG-Mechanik ist robust genug.

## Wissenschaftliche Validierung bestehender Praxis

Paper **bestätigt** unser Cadence-Design, erzwingt keine Änderung:
- Earnings-Trigger-Rebalance ~3 Monate = optimal für 3 der 4 Kanon-Faktoren
- Insider-Real-Time = richtige Wahl für nicht-kanonisches Signal
- Jahres-Vollanalyse bei Quality-Ticker (BRK.B, COST) = konservativ-angemessen bei 26M-Half-Life

Dies ist ein **Applied-Learning-Bullet-Fall**: *"Paper validiert Regel, erzwingt keine neue Regel."*

## Operationalisierung

- **§29.3** (Retrospective-Gate): Score-Cadence-Konsistenz-Check bei Review 2028 — decayen wir synchron mit Faktor-Half-Life?
- **Monitoring:** aktive FLAG-Ticker (Investment-Signal-Klasse) auf Monthly-Observability beobachten
- **Dokumentation:** Earnings-Trigger-Rationale in [[Update-Klassen-DEFCON]] mit Flint/Vermaak-Verweis ergänzen

## Backlinks
- [[Factor-Information-Decay]] — operative Konzeptseite
- [[Factor-Investing-Framework]] — Faktor-Kanon, gleicher AQR-Rahmen
- [[Update-Klassen-DEFCON]] — A/B/C/D Klassen-Definition
- [[DEFCON-System]] — Ziel-Scoring-Matrix
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Temporal-Check
- [[PBO-Backtest-Overfitting]] — komplementäre Methoden-Gate-Ebene
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B17
