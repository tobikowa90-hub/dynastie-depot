---
title: "Are Insiders' Trades Informative?"
date: 2001
type: source
subtype: academic-paper
tags: [defcon, insider-trading, contrarian-signal, small-cap-effect, primary-evidence, b26, active-scoring-validation]
url: https://www.nber.org/papers/w6656
venue: "Review of Financial Studies 14(1), 2001, 79-111. NBER Working Paper 6656 (1998 Draft)"
authors: "Josef Lakonishok (University of Illinois Urbana-Champaign), Inmoo Lee (Korea University)"
status: processed
defcon_relevanz: "Befund B26 (`active-scoring-validation`, eingeführt 26.04.2026 mit Codex-Re-Klassifikation — Status-Label NEU in Status-Matrix-Legende). Insider-Block (5 Pt.) Primärquelle. Validiert die seit insider-intelligence-Skill-Launch operativen Heuristiken: (1) Insider-Käufe > Insider-Verkäufe in Informationsgehalt — Verkäufe haben Liquiditäts-/Diversifikations-Rauschen. (2) Aggregate Insider-Aktivität prädiziert Markt-Returns. (3) Insider sind Contrarians (Kaufen wenn überverkauft, Verkaufen wenn überbewertet). (4) Effekt ist stärker bei Small-Caps und Small-Growth-Stocks. Operative Konsequenz für DEFCON: Aktuelle Form-4-Auswertung im Insider-Block sollte Buy-Side höher gewichten als Sell-Side; bei Sell-Signalen muss Liquiditäts-/Optionsausübungs-Filter greifen (Spalte M/X-Filter via [[OpenInsider]] bereits implementiert). Validation, kein Architektur-Change."
sources: []
related:
  - "[[Insider-Trading-Primary-Signal]]"
  - "[[Ke-Huddart-Petroni-2003]]"
  - "[[insider-intelligence]]"
  - "[[OpenInsider]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/ARE INSIDERS' TRADES INFORMATIVE.pdf"
aliases:
  - "Lakonishok Lee 2001"
  - "Are Insiders Trades Informative"
  - "Insider Trading Primary Reference"
---

# Lakonishok & Lee (2001) — Are Insiders' Trades Informative?

> ⚠️ **CONFIDENCE-WARNUNG (sekundärer Beleg):** Raw-PDF ist image-only (kein Text-Layer extrahierbar). Diese Source-Page synthesisiert **NICHT aus der Primärquelle**, sondern aus (1) [[2iQ-Insider-Meta-Review]] (industry-meta-review, kein peer review), (2) etablierter Sekundärliteratur und (3) der weithin zitierten Befund-Architektur (Buy>Sell, Aggregate-Predictability, Small-Cap-Concentration, Contrarian-Timing). **Spezifische Magnituden** (z.B. „50-68 bps/Monat" aus 2iQ-Tabelle 33) sind sekundär-zitiert und sollten bei jeder !Analysiere-Insider-Block-Diskussion **NICHT als Primär-Zitat** verwendet werden. **Pflicht bei Bedarf an Primärzitaten:** NBER WP 6656 (1998 Draft) oder RFS 14(1) S. 79-111 konsultieren — Original-Tabellen-Werte verifizieren bevor sie in Briefings/Skill-Roadmap-Dokumente einfließen. Confidence-Level: **Inhaltliche Befunde HOCH** (kanonische Primärreferenz weithin repliziert), **numerische Magnituden MITTEL** (sekundär-zitiert, image-only-Trap).

## Abstract (eigene Worte)

Lakonishok und Lee untersuchen Insider-Transaktionen auf NYSE, AMEX und Nasdaq über 20 Jahre (1975-1995, ~21 Jahre × ~10.000 Firmen × Form-4-Filings). Sie finden, dass Insider auf **Aggregate-Ebene** als Contrarians agieren — sie kaufen, wenn der Markt fällt, und verkaufen, wenn er steigt — und besser als simple Contrarian-Strategien timen können. Auf **Firmen-Level** prädiziert Insider-Aktivität signifikante Stock-Returns: Stocks mit umfangreichen Insider-Käufen outperformen Stocks mit umfangreichen Insider-Verkäufen. Wichtigste Asymmetrie: **Insider-Käufe sind informativer als Insider-Verkäufe** (weil Verkäufe oft Liquiditäts-, Steuer-, oder Portfolio-Rebalancing-Gründe haben). Effekt ist **stärker in Small-Caps**, insbesondere in Small-Growth-Stocks (höhere Mispricing-Gelegenheit + niedrigere institutionelle Coverage). Das Paper ist die kanonische Primär-Referenz für die operative Insider-Trading-Anomaly.

## Vier Kern-Befunde (Faktortabelle-relevant)

1. **Buy-Side > Sell-Side in Information** — Insider-Verkäufe enthalten zu viel Rauschen (Diversifikation, Vesting, Liquidität, Optionsausübung). Käufe sind diskretionär und mit Eigenkapital, also strukturell informativer.

2. **Aggregate-Predictability** — Net-Insider-Buy-Ratio prädiziert künftige Markt-Returns. Seyhun (1992) findet bis zu 60% Erklärung der 1-Jahres-Return-Variation; Lakonishok/Lee bestätigen die Richtung über das längere 1975-1995-Sample.

3. **Small-Cap-Concentration** — Größter Buy-Sell-Spread ist in Small-Growth-Stocks. Insider sind in dem Segment "heavy sellers" — aber WENN sie kaufen, ist das ein starkes Signal.

4. **Contrarian-Timing** — Insider erhöhen Käufe nach Markt-Drawdowns, reduzieren sie nach Rallies. Das passt zur Mispricing-Hypothese: Insider sehen Bewertungsabweichungen vor dem Markt.

## DEFCON-Implikation (B26 `active-scoring-validation`)

| Existierendes Element | L&L-Validation | Anpassungs-Bedarf |
|---|---|---|
| **Form-4-Filter (X/M-Spalte)** via [[OpenInsider]] | Bestätigt — Optionsausübungen + planmäßige Verkäufe filtern raus | Bereits implementiert in `insider-intelligence`-Skill |
| **Buy-Side höher gewichtet als Sell-Side** im Insider-Block (5 Pt.) | Bestätigt | Bereits implementiert (Sell-Signale brauchen >$20M-Schwelle für FLAG, Buy-Signale schon ab $5M-Cluster) |
| **Insider-Cluster-Premium** (mehrere Insider gleichzeitig) | Lakonishok/Lee deutet das an, formell bei Alldredge/Blank 2017 | Optional in `insider-intelligence` zu erweitern |
| **Small-Cap-Bonus** | L&L: Effekt stärker bei Small-Caps | DEFCON-Universum ist **Mid-/Large-Cap** (Satelliten >$10B Mkt-Cap); L&L-Effekt schwächer aber nicht null. Kein Architektur-Change. |

→ **Verdikt:** B26 ist primär-empirische **Validation der bestehenden Insider-Block-Heuristik**, kein neues Scoring-Element.

## Komplementarität zu B27 (Ke/Huddart/Petroni)

L&L sagt: "Insider-Käufe sind informativer als -Verkäufe." Ke/Huddart/Petroni 2003 (B27) zeigt **warum**: Insider-Verkäufe vor Earnings-Breaks geschehen 9-3 Quartale **VOR** dem Break, nicht in den letzten 2 Quartalen (legal jeopardy avoidance). Das heißt: Wer nur die letzten 2 Quartale beobachtet, sieht KEINE Sell-Aktivität — und schließt fälschlich, dass Verkäufe rauschig sind. **Wer das L&L-Window auf 9 Quartale erweitert (B27), findet die fehlenden Sell-Signale.** Beide Befunde zusammen → Insider-Block-Erweiterungs-Pipeline für 2026/2027.

## Operative Konsequenzen

1. **Status quo bleibt:** Insider-Block (5 Pt.) verwendet Buy-Side als primäres Positiv-Signal, Sell-Side nur bei Cluster + diskretionärer Form-4-Klassifikation.
2. **Watch:** B27 (Ke/Huddart/Petroni) öffnet die Möglichkeit, Insider-Sell-Window von aktuell ~6 Monaten auf bis zu ~24 Monate zu erweitern. Aktivierung pendant zu insider-intelligence-Skill v2 (deferred, nicht 2026 priorisiert).
3. **Aggregate-Insider-Indicator** (L&L Aggregate-Befund) ist **nicht** im DEFCON enthalten — DEFCON ist Bottom-Up (per Ticker), Top-Down-Markt-Timing wird absichtlich nicht modelliert. Konzeptuelle Awareness, aber keine Skill-Konsequenz.
4. **Small-Cap-Bonus nicht aktiviert** — Satelliten-Universum ist strukturell Mid-/Large-Cap; L&L-Premium adressiert ein anderes Segment.

## Backlinks

- [[Insider-Trading-Primary-Signal]] — neue Concept-Page (B26-Anker)
- [[Ke-Huddart-Petroni-2003]] — komplementärer Befund (B27): Time-Window-Erweiterung
- [[insider-intelligence]] — operativer Skill, nutzt L&L-Heuristiken
- [[OpenInsider]] — Daten-Pflichtquelle (Form-4-Filter X/M)
- [[2iQ-Insider-Meta-Review]] — Sekundärquelle, bündelt L&L mit Seyhun + Jeng/Metrick/Zeckhauser + Cluster-Buying-Studien
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B26
- [[Josef Lakonishok]], [[Inmoo Lee]] — Author-Entities
