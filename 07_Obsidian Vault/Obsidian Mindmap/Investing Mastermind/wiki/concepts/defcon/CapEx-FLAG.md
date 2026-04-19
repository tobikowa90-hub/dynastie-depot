---
title: "CapEx-FLAG"
type: concept
tags: [konzept, flag, capex, scoring, kern]
created: 2026-04-10
updated: 2026-04-14
version: v3.4
sources: [Gu-Kelly-Xiu-2020, arXiv-1711.04837]
related: [DEFCON-System, Analyse-Pipeline, ROIC-vs-WACC, Update-Klassen-DEFCON, Tariff-Exposure-Regel]
wissenschaftlicher_anker: "B2 (Gu/Kelly/Xiu 2020) — FCF stabilster Prädiktor; hoher CapEx erodiert FCF systematisch | B3 (Gu/Kelly/Xiu) — Earnings Quality über Cash-Konvertierung"
konfidenzstufe: peer-reviewed
---

# CapEx-FLAG — Die heilige Regel

> **FLAG überschreibt jeden Score. Kein Kompromiss, keine Ausnahme.**

## Automatische FLAG-Trigger

| Trigger | Konsequenz |
|---------|------------|
| CapEx/OCF > 60% | 🔴 FLAG — Sparrate 0€, auch bei DEFCON 4 |
| Negativer FCF-Trend + steigendes CapEx | 🔴 FLAG — Sparrate 0€ |
| Insider Net-Selling >$20M / 90d (kein 10b5-1 "M") | 🔴 FLAG — Sparrate 0€ |

## Scoring-Skala CapEx/OCF

| CapEx/OCF | Punkte | Kommentar |
|-----------|--------|-----------|
| < 10% | 9 | Fabless-Ideal (Referenz: AVGO) |
| 10–20% | 7–8 | Asset-Light |
| 20–40% | 4–6 | Normal |
| 40–60% | 1–3 | Beobachten |
| > 60% | 0 + FLAG | Stopp |

## Pre-Processing Regel 2 (Finance Leases)

Wenn Finance Lease Obligations >$5B: **manueller 8-K-Check vor FLAG-Aktivierung.**
Shibui kann Lease-Payments nicht isolieren. Bereinigung nötig.

**Referenz:** MSFT — Finance Leases $19.5B. Bereinigtes CapEx/OCF ~63% statt 83.6%.
FLAG bleibt dennoch aktiv, weil bereinigt >60%.

## Fallbeispiele

- **AVGO:** 2.3% → Kalibrierungsanker. Fabless-Modell.
- **MSFT:** 83.6% (bereinigt 63%) → FLAG aktiv seit 26.03.2026
- **GOOGL:** ~75% FY26 → struktureller Ausschluss (kein Einstieg)
- **ASML:** 12.5% → kein FLAG, Non-US-Kalibrierungsanker

## Verlinkungen

- [[DEFCON-System]] — Scoring-Matrix
- [[Analyse-Pipeline]] — FLAG greift in jeder Stufe
- [[ROIC-vs-WACC]] — Verwandter Malus (ROIC < WACC)
- [[Update-Klassen-DEFCON]] — FLAG-Auslösung = Klasse-C-Event (sofort)
- [[Tariff-Exposure-Regel]] — Verwandter FLAG-Trigger (>35% Exposure)
- [[Non-US-Scoring]] — CapEx-Kalibrierung für IFRS-Ticker
- [[MSFT]] — Aktives FLAG-Beispiel
- [[GOOGL]] — Struktureller Ausschluss
- [[AVGO]] — Fabless-Referenz (2.3%)
- [[FLAG-Event-Log]] — Persistierung aller Trigger/Resolution
- [[Backtest-Ready-Infrastructure]] — Infrastruktur-Dachkonzept

## Persistierung (seit 2026-04-17)

Jeder `capex_ocf`-Trigger wird in `05_Archiv/flag_events.jsonl` als unveränderlicher Record angehängt. Schwelle 60 ist hardcoded in `FLAG_RULES` in `03_Tools/backtest-ready/schemas.py`.

**Deterministische `fcf_trend_neg`-Definition** (Spec §4.2): FCF YoY negativ in ≥3 von 4 letzten Quartalen UND CapEx YoY positiv. Ersetzt frühere heuristische Beschreibung.

**Backfill-Stand 17.04.2026:** 2 capex_ocf-Trigger rekonstruiert (MSFT `83.6%` FY26 Q2, GOOGL FY26 Guidance Wert=null). APH (Score-basierter FLAG) ist nicht in der 4-Typ-Enum abbildbar → dokumentiert in `_parser_errors.log`.

Details: [[FLAG-Event-Log]], [[Score-Archiv]].

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Der CapEx-FLAG triggert Investment-Klasse-Beobachtung. Per Flint-Vermaak 2021 hat der Investment-Faktor die schnellste Half-Life aller AQR-Kanon-Faktoren (~1 Monat):

- **Konsequenz:** Earnings-Trigger-Cadence (~3M) ist zu träge für aktive CapEx-FLAGs
- **Monthly-Refresh-Pflicht** für aktive Investment-FLAGs → INSTRUKTIONEN.md §30 (ab Phase 4)
- **Aktuelle Scope:** MSFT CapEx/OCF 83.6% FLAG aktiv → §30 pflicht
- **Schema-Watch:** TMO fcf_trend_neg schema-getriggert, bewusst nicht aktiviert (WC-Noise) → §30 nicht automatisch

**Rückverweise:** §29.3 (Half-Life-Cadence) liefert die wissenschaftliche Fundierung; §30 (Live-Monitoring) operationalisiert die Monthly-Refresh-Pflicht für aktive Investment-FLAGs.

Quellen: [[Flint-Vermaak-2021-Decay]], [[Factor-Information-Decay]]
