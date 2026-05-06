---
title: "What Insiders Know About Future Earnings and How They Use It: Evidence from Insider Trades"
date: 2003
type: source
subtype: academic-paper
tags: [defcon, insider-trading, earnings-prediction, time-window-expansion, legal-jeopardy, b27, design-context]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=234864
venue: "Journal of Accounting and Economics 35(3), 2003, 315-346 (Original Mar 2002 Working Paper)"
authors: "Bin Ke (Penn State University, Smeal College), Steven Huddart (Penn State University, Smeal College), Kathy Petroni (Michigan State University, Eli Broad)"
status: processed
defcon_relevanz: "Befund B27 (`design-context`, eingeführt 26.04.2026 mit Codex-Re-Klassifikation — Status-Label NEU in Status-Matrix-Legende; deferred bis insider-intelligence v2). Insider-Block (5 Pt.) Time-Window-Erweiterung. Kern: Insider-Verkäufe vor einem Earnings-Break (Ende einer Serie konsekutiver Quartals-EPS-Steigerungen) konzentrieren sich 9-3 Quartale VOR dem Break — NICHT in den letzten 2 Quartalen. Grund: Legal jeopardy + ITSFEA 1988 + 10(b)-Antifraud verhindern proximate Sell-Aktivität. Operative Konsequenz für insider-intelligence-Skill: aktuelles Sell-Detection-Window (6-Monats-Lookback) verfehlt strukturell die echten Pre-Break-Sells. Pipeline-Erweiterung auf 24-Monats-Window deferred (insider-intelligence v2). Bridge-Befund zu Fundamentals-Block: Insider haben **Earnings-Foreknowledge** — bestätigt warum EPS-Revision-Delta (Sentiment-Block) nachlaufend ist gegenüber Insider-Trades."
sources: []
related:
  - "[[Insider-Trading-Primary-Signal]]"
  - "[[Earnings-Foreknowledge-Window]]"
  - "[[Lakonishok-Lee-2001]]"
  - "[[insider-intelligence]]"
  - "[[OpenInsider]]"
  - "[[FCF-Primacy]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/Ke, Huddart, Petroni.pdf"
aliases:
  - "Ke Huddart Petroni 2003"
  - "Ke Huddart Petroni 2002"
  - "Insider Earnings Foreknowledge"
---

# Ke, Huddart & Petroni (2003) — Insider Trading & Earnings Foreknowledge

## Abstract (eigene Worte)

Ke, Huddart und Petroni zeigen, dass Insider Wissen über zukünftige **Earnings-Breaks** (Ende einer Serie konsekutiver Quartals-Earnings-Steigerungen) **bis zu 2 Jahre im Voraus** besitzen und entsprechend handeln. Insider-Verkäufe steigen signifikant in den **Quartalen 9 bis 3 vor dem Break** — aber **fast keine Sell-Aktivität in den 2 Quartalen unmittelbar vor dem Break**. Das ist konsistent mit Legal-Jeopardy-Vermeidung: Section 10(b) der Securities Exchange Act 1934 + Insider Trading Sanctions Act 1984 + Insider Trading and Securities Fraud Enforcement Act 1988 (ITSFEA) machen proximate Pre-Earnings-Trades hochriskant. Die Sell-Pattern ist stärker für (1) Growth-Firmen, (2) längere Pre-Break-Strings, (3) größere Earnings-Declines am Break, und (4) längere Decline-Perioden post-Break. Median Buy-and-Hold abnormale Returns für Quartale −8 bis −1 vor dem Break sind negativ — Insider, die früh verkaufen, vermeiden den späteren Drawdown.

## Methodik

- **Sample:** US-Firmen 1989-2000, COMPUSTAT/CRSP, manuell gefilterte Form-4-Filings
- **Definition "String":** Quartal mit YoY-EPS-Steigerung in 4+ konsekutiven Quartalen
- **Definition "Break":** Erstes Quartal nach String mit YoY-EPS-Decline
- **Outcome-Metric:** Net-Insider-Sale-Frequency in Quartalen Q-12 bis Q+4 relativ zum Break
- **Kontrollen:** Legal jeopardy via Liability-Period-Indikatoren (post-1984, post-1988); Growth/Value via B/M-Quintile

## Drei Kernbefunde

| Quartale relativ zum Break | Net-Insider-Sell-Aktivität | Interpretation |
|---|---|---|
| **Q-9 bis Q-3** | **signifikant erhöht** | Insider sehen den Break ~2 Jahre voraus, verkaufen außerhalb der Legal-Jeopardy-Zone |
| **Q-2 und Q-1** | **fast Null abnormal** | Legal-Jeopardy-Vermeidung (10(b), ITSFEA), corporate-policy-Restriktionen post-Earnings-Window |
| **Q-9 bis Q-1 (kombiniert)** | Median Buy-and-Hold AbReturn **negativ** | Insider, die in der erweiterten Pre-Break-Zone verkaufen, vermeiden den späteren Drawdown |

→ **Stärkere Sell-Pattern bei:** (1) Growth-Firmen, (2) längeren Strings (4+ vs 6+ Quartale), (3) größeren Earnings-Declines, (4) längeren post-Break-Declines.

## DEFCON-Implikation (B27 `design-context`)

### Direct-Operative Konsequenz: Insider-Block-Window-Erweiterung

| Status | Window | Capture-Rate (geschätzt) |
|---|---|---|
| **Aktuell (insider-intelligence v1)** | 6-Monate Lookback (~2 Quartale) | Verfehlt strukturell die echte Pre-Break-Sell-Zone (Q-9 bis Q-3) |
| **Geplant (insider-intelligence v2, deferred)** | 24-Monate Lookback (~8 Quartale) | Captured Q-9 bis Q-3 vollständig + Q-2/-1 (für Compliance-Kontext) |
| **Theoretical Optimum** | Quartals-stratifiziert mit Break-Definition | Erfordert EPS-Fortschreibung pro Ticker; Skill-Komplexität >> v2-Scope |

### Bridge-Befund zu Fundamentals-Block

Ke/Huddart/Petroni zeigen: **Insider-Trades führen Earnings-Disclosures** (bis zu 2 Jahre). Das hat zwei Konsequenzen:

1. **EPS-Revision-Delta** (Sentiment-Block, 1 Pt.) ist strukturell **nachlaufend** vs. Insider-Trades. Eigenes Insider-Window erfasst Information ~6-18 Monate früher als Analyst-Revisions.

2. **fcf_trend_neg / fcf_trend_pos** (Fundamentals-Watch, neu in v3.7) ist verwandtes nachlaufendes Signal — wenn FCF-Trend bricht, sind Insider oft schon 9-3 Quartale früher dran. Cross-Validation-Möglichkeit für Schema-Watches.

### Architektur-Implikation

- **Kein Live-Score-Change** bis insider-intelligence v2 deployed ist.
- **Watch-Item für 2027 Konsolidierung:** Window-Erweiterung 6→24 Monate gegen Performance-Backtest auf Score-Archiv (sobald §29-Backtest-Gate-Kriterien erfüllt).
- **Komplementär zu B26:** Lakonishok-Lee sagt "Buys > Sells in Information." Ke/Huddart/Petroni erklärt die scheinbare Sell-Schwäche durch Window-Verkürzung. Ein **24-Monats-Window könnte Sell-Signale aufwerten** auf Höhe der Buy-Signale für Earnings-getriebene Stories.

## Komplementär zu Beneish (1999) + Beneish/Press/Vargus (2001)

Ke/Huddart/Petroni zitiert Beneish (1999): Insider verkaufen nach Earnings-Announcements, die später als überstated revealed werden. Beide Studien zusammen: **Insider verwenden Earnings-Manipulationsspielraum, um Sell-Timing zu optimieren** (Earnings überstaten → Aktie hochhalten → verkaufen → später Korrektur). Das ist ein zusätzliches Argument für **Earnings-Quality-Validierung** (Accruals-Ratio, Sloan 1996, B14) als Komplementär zu Insider-Signalen.

## Operative Schlussfolgerungen

1. **B27 dokumentiert eine strukturelle Lücke** im aktuellen insider-intelligence-Skill (6-Monats-Window verfehlt Q-9 bis Q-3 Sell-Zone).
2. **B27 erklärt die scheinbare Buy>Sell-Asymmetrie aus B26** — sie ist teilweise ein Window-Artefakt, kein fundamentales Signal-Asymmetrie-Argument.
3. **Pipeline-Item (deferred):** insider-intelligence v2 mit 24-Monats-Lookback. Kein Score-Element heute.
4. **Schema-Watches** wie `fcf_trend_neg` (TMO-Beispiel 18.04.-23.04.) sind nachlaufende Signale gegenüber Insider-Trades — Insider-Block bleibt strukturell informativer als Fundamentals-Watches.

## Backlinks

- [[Insider-Trading-Primary-Signal]] — Concept-Page (B26+B27 gemeinsamer Anker)
- [[Earnings-Foreknowledge-Window]] — neue Concept-Page (B27-spezifisch, 9-3-Quartale-Sell-Zone)
- [[Lakonishok-Lee-2001]] — komplementäre Primärquelle (B26)
- [[insider-intelligence]] — operativer Skill, B27 begründet v2-Roadmap
- [[OpenInsider]] — Datenquelle (Form-4 mit Trade-Date)
- [[FCF-Primacy]] — verwandter nachlaufender Indikator
- [[Accruals-Anomalie-Sloan]] — Earnings-Quality-Komplement (Beneish-Bridge)
- [[DEFCON-System]] — Insider-Block (5 Pt.)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B27
- [[bin-ke|Bin Ke]], [[steven-huddart|Steven Huddart]], [[kathy-petroni|Kathy Petroni]] — Author-Entities
