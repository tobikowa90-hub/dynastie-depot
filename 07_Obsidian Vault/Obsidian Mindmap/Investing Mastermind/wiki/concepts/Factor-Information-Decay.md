---
title: "Factor Information Decay"
type: concept
tags: [factor-decay, half-life, rebalancing, cadence, temporal, method]
created: 2026-04-19
updated: 2026-04-19
sources: [Flint-Vermaak-2021-Decay]
related: [Factor-Investing-Framework, PBO-Backtest-Overfitting, Seven-Sins-Backtesting, Palomar-Methods-Reference, Backtest-Methodik-Roadmap, Update-Klassen-DEFCON, DEFCON-System]
wissenschaftlicher_anker: "Flint & Vermaak (2021) — SSRN 3986499"
konfidenzstufe: methoden-standard
---

# Factor Information Decay

> **Temporal-Dimension der Faktor-Validation: Wie lange ist ein Faktor-Signal informationsreich, bevor es verblasst? Faktor-Half-Life steuert optimale Rebalance-Cadence. Unser Earnings-Trigger ist wissenschaftlich fundiert für 3 der 4 Kanon-Faktoren.**

## Half-Life-Tabelle (Autoren-Ergebnisse)

| Faktor | Optimale Rebalance | Pure-Factor Median Half-Life |
|---|---|---|
| Value | 3–4 Monate | länger als andere |
| **Quality** | **4–5 Monate** | **25,9 Monate** |
| Momentum | 3 Monate | kürzer |
| Low Volatility | 5–6 Monate | mittel |
| Investment | **1 Monat** | <6 Monate median-halving |

**Reading:** Pure Half-Life ≠ Optimal Rebalance. Pure Half-Life misst, wann aggregierte Exposure halbiert ist; optimaler Rebalance ist kürzer, weil Quartile-Portfolio-Zusammensetzung schneller driftet.

## Warum das zählt für Dynasty-Depot

Wir entscheiden bei **jeder** Score-Re-Evaluierung implizit über Cadence. Ohne Faktor-Decay-Kontext:
- Zu häufiges Re-Scoring → Turnover-Kosten (Sin #5, siehe [[Seven-Sins-Backtesting]])
- Zu seltenes Re-Scoring → Informations-Verlust bei schnell-decayenden Faktoren

Paper liefert die wissenschaftliche Cadence-Rechtfertigung für unsere Earnings-Trigger-Struktur.

## DEFCON-Cadence-Validation

| Faktor-Analog | DEFCON-Block | Cadence-Alignment |
|---|---|---|
| Value | Fundamentals (Fwd P/E, P/FCF) | ✅ Earnings-Trigger ≈ 3 Monate optimal |
| Quality | Moat + Qualität-Subs | ✅ Earnings-Trigger + jährliche Vollanalyse = konservativ |
| Momentum | Technicals | ✅ Earnings-Trigger + !Briefing-Monitor |
| Investment | Fundamentals (CapEx/OCF, Asset-Growth) | ⚠️ Earnings-Trigger zu träge für isolierte Investment-Signals |
| Low Volatility | — | nicht explizit |
| Insider (non-AQR) | Insider-Block | ✅ Real-Time OpenInsider-Scan |

## Investment-Klasse — offene Watch

MSFT-CapEx/OCF-FLAG und TMO-`fcf_trend_neg`-Disclosure sind Investment-Klasse-Signale. Paper impliziert Half-Life ~1 Monat. Aktueller Workflow fängt via Earnings-Trigger + Daily-`!Briefing` ab, aber **keine dedizierte Monthly-Fundamentals-Refresh-Regel**.

**Entscheidung:** derzeit **keine** neue Regel. FLAG-Mechanik ist robust. Review 2028 — anhand realer FLAG-Event-Trajektorien prüfen, ob Monthly-Refresh nötig.

## Drei-Dimensionen-Validation

Faktor-Decay ist die **Temporal-Dimension** einer umfassenden Backtest-Validation. Zusammen mit:

| Dimension | Paper | Was es prüft |
|---|---|---|
| Methode | [[PBO-Backtest-Overfitting]] | Overfitting-Statistik |
| Raum | [[Factor-Investing-Framework]] | Welche Faktoren, welches SR-Band |
| **Zeit** | **Dieses Konzept** | **Wie lange Signale valide sind** |
| Sünden | [[Seven-Sins-Backtesting]] | Pre-Flight-Check vor Analyse |

## Anwendung in §29.3

Retrospective-Gate §29.3 prüft bei Review 2028:
- Ist unsere tatsächliche Cadence (Earnings-Trigger) konsistent mit der Faktor-Half-Life-Dominanz der jeweiligen Ticker?
- Zeigen Quality-lastige Ticker (BRK.B, COST) langsame Score-Drift → bestätigt 4–5M-Cadence ausreichend?
- Zeigen Investment-lastige Signale (MSFT-CapEx, TMO-FCF) schnellere Drift → Monthly-Refresh nötig?

## Operative Regel (bestätigt, nicht neu)

**Applied Learning Bullet:** *Earnings-Trigger-Rebalance-Cadence ist wissenschaftlich aligned für Value/Quality/Momentum; Investment-Signale (CapEx/Asset Growth) decayen schneller (1 Monat) — bei aktiven FLAGs ggf. Monthly-Refresh erwägen (Review 2028).*

## Backlinks
- [[Flint-Vermaak-2021-Decay]] — Source-Zusammenfassung
- [[Factor-Investing-Framework]] — Faktor-Kanon (Raum-Dimension)
- [[PBO-Backtest-Overfitting]] — Methoden-Dimension
- [[Seven-Sins-Backtesting]] — Pflicht-Sünden-Pre-Flight
- [[Palomar-Methods-Reference]] — Methodische Alternativen
- [[Update-Klassen-DEFCON]] — A/B/C/D Klassen, passt Cadence an Faktor-Typ an
- [[Backtest-Methodik-Roadmap]] — 2028-Aktivierungs-Entscheidung
- [[DEFCON-System]] — Ziel-Scoring-Matrix
