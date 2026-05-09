---
title: "Earnings Foreknowledge Window"
type: concept
tags: [defcon, insider-trading, earnings-prediction, time-window, legal-jeopardy, b27, design-context]
created: 2026-04-26
updated: 2026-04-27
sources: [Ke-Huddart-Petroni-2003]
related: [Wissenschaftliche-Fundierung-DEFCON, Insider-Trading-Primary-Signal, Lakonishok-Lee-2001, insider-intelligence, OpenInsider, DEFCON-System]
wissenschaftlicher_anker: "B27 (Ke/Huddart/Petroni 2003, JAE 35(3)) — Insider-Verkäufe vor einem Earnings-Break (Ende einer Serie konsekutiver Quartals-EPS-Steigerungen) konzentrieren sich Q-9 bis Q-3 vor dem Break — fast Null abnormal in Q-2/Q-1. Legal-Jeopardy + ITSFEA 1988 unterdrücken proximate Pre-Earnings-Trades. Median Buy-and-Hold-AbReturn für Q-8 bis Q-1 negativ — early-Sellers vermeiden Drawdown."
konfidenzstufe: peer-reviewed
defcon_block: "Insider-Block (10 Pt.) — Window-Erweiterung deferred"
operative_regel: "insider-intelligence v1 verwendet 6-Monats-Lookback (~2 Quartale) und verfehlt damit strukturell die echte Pre-Break-Sell-Zone (Q-9 bis Q-3). v2-Roadmap: 24-Monats-Lookback, deferred bis §29-Backtest-Gate-Kriterien erfüllt."
aliases:
  - "Earnings Foreknowledge"
  - "Pre-Break Sell-Zone"
  - "9-3 Quartale Sell Window"
---

# Earnings Foreknowledge Window

> Ke, Huddart & Petroni (2003) zeigen: Insider haben Wissen über zukünftige Earnings-Breaks bis zu 2 Jahre im Voraus und handeln entsprechend. Sell-Aktivität konzentriert sich Q-9 bis Q-3 vor dem Break — fast Null in Q-2/Q-1 (Legal-Jeopardy-vermeidet). Wer nur die letzten 2 Quartale beobachtet, sieht KEINE Sell-Aktivität — und schließt fälschlich, dass Verkäufe rauschig sind.

## Definition

**Earnings Foreknowledge Window** = der Zeitabschnitt, in dem Insider Wissen über bevorstehende Earnings-Breaks (Ende einer konsekutiven YoY-EPS-Steigerungs-Serie) in diskretionäre Sell-Aktivität umsetzen. Empirisch: Q-9 bis Q-3 vor dem Break.

## Window-Decomposition

| Quartale relativ zum Break | Net-Insider-Sell-Aktivität | Mechanismus |
|---|---|---|
| **Q-12 bis Q-10** | Marginal | Foreknowledge noch nicht ausgeprägt; normale Diversifikations-Sells |
| **Q-9 bis Q-3** | **Signifikant erhöht** | Insider sehen den Break ~2 Jahre voraus, verkaufen außerhalb der Legal-Jeopardy-Zone |
| **Q-2 und Q-1** | **Fast Null abnormal** | Legal-Jeopardy-Vermeidung (Section 10(b) Securities Exchange Act 1934 + ITSFEA 1988 + corporate-policy-Restriktionen post-Earnings-Window) |
| **Q+1 bis Q+4** | Mixed | Post-Break-Reaktion; teilweise Buybacks bei Overshoot, teilweise weitere Sells bei strukturellem Decline |

## Stärkere Sell-Pattern bei

1. **Growth-Firmen** (höhere Earnings-Erwartung → größere Drop-Magnitude bei Break)
2. **Längere Pre-Break-Strings** (4+ vs 6+ Quartale) — länger anhaltende Outperformance signalisiert größeren mean-reversion-Druck
3. **Größere Earnings-Declines am Break**
4. **Längere post-Break-Decline-Perioden**

## DEFCON-Implikation: insider-intelligence v2-Roadmap

| Status | Window | Capture-Rate |
|---|---|---|
| **insider-intelligence v1** (aktiv) | 6-Monate Lookback (~2 Quartale) | Verfehlt strukturell die Pre-Break-Sell-Zone — captured nur Q-2/Q-1 (legaljuristisch leer) |
| **insider-intelligence v2** (deferred) | 24-Monate Lookback (~8 Quartale) | Captured Q-9 bis Q-3 vollständig + Q-2/Q-1 (Compliance-Kontext) |
| Theoretical Optimum | Quartals-stratifiziert mit Break-Definition | Erfordert EPS-Fortschreibung pro Ticker; Skill-Komplexität >> v2-Scope |

**Aktivierungs-Trigger:** §29-Backtest-Gate-Kriterien erfüllt (Score-Archiv ausreichend gefüllt + §29.7 M&P-Discount-Plausibility-Check; siehe [[RETROSPECTIVE-GATE]]). Kein Live-Score-Change bis Deploy.

## Bridge-Befund: Insider-Trades führen Earnings-Disclosures

Ke/Huddart/Petroni's Kern-Befund hat zwei DEFCON-Konsequenzen:

1. **EPS-Revision-Delta** (Sentiment-Block, Bonus +1) ist strukturell **nachlaufend** vs. Insider-Trades. Eigenes Insider-Window erfasst Information ~6-18 Monate früher als Analyst-Revisions.
2. **fcf_trend_neg / fcf_trend_pos** (Fundamentals-Watch, neu in v3.7) ist verwandtes nachlaufendes Signal. Wenn FCF-Trend bricht, sind Insider oft schon 9-3 Quartale früher dran. Cross-Validation-Möglichkeit für Schema-Watches.

## Komplementär zu B26 (Lakonishok-Lee)

L&L sagt: „Insider-Käufe sind informativer als -Verkäufe."  
KHP erklärt: Diese apparent Asymmetrie ist teilweise **Window-Artefakt** — wer nur die letzten 6 Monate beobachtet, sieht legaljuristisch unterdrückte Sells, schließt fälschlich auf Sell-Schwäche. Ein 24-Monats-Window könnte Sell-Signale aufwerten auf Höhe der Buy-Signale für earnings-getriebene Stories.

## Komplementär zu Beneish (1999)

KHP zitiert Beneish (1999): Insider verkaufen nach Earnings-Announcements, die später als overstated revealed werden. Beide Studien zusammen: **Insider verwenden Earnings-Manipulationsspielraum, um Sell-Timing zu optimieren** (Earnings overstate → Aktie hochhalten → verkaufen → später Korrektur). Das ist ein zusätzliches Argument für Earnings-Quality-Validierung (Accruals-Ratio, Sloan 1996, B14) als Komplementär zu Insider-Signalen.

## Limitationen

- **Sample-Periode:** 1989-2000 — pre-SOX-Ära (Sarbanes-Oxley 2002 verschärfte Insider-Reporting). Post-SOX-Replikationen zeigen ähnliche Patterns, aber mit kürzerer Pre-Break-Window-Länge (~Q-6 bis Q-3 statt Q-9 bis Q-3).
- **Earnings-Break-Definition:** Manuelle EPS-String-Klassifikation; nicht trivial zu automatisieren in einem Skill ohne EPS-Fortschreibung pro Ticker.
- **Legal-Jeopardy-Veränderung:** Post-2002 SOX und 10b5-1-Plan-Routinisierung haben die Sell-Pattern modifiziert — heutige Sells laufen oft via 10b5-1-Pläne, die im Form-4-X/M-Filter (Spalte „M") herausgefiltert werden müssen.

## Backlinks

- [[Ke-Huddart-Petroni-2003]] — Primärquelle (B27, `design-context`)
- [[Lakonishok-Lee-2001]] — komplementäre Primärquelle (B26)
- [[Insider-Trading-Primary-Signal]] — Concept-Page für B26+B27 gemeinsamer Anker
- [[insider-intelligence]] — operativer Skill v1; v2 (24M-Window) deferred
- [[OpenInsider]] — Datenquelle (Form-4 mit Trade-Date)
- [[Accruals-Anomalie-Sloan]] — Earnings-Quality-Komplement (Beneish-Bridge)
- [[FCF-Primacy]] — verwandter nachlaufender Indikator
- [[DEFCON-System]] — Insider-Block 10 Pt.
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B27
