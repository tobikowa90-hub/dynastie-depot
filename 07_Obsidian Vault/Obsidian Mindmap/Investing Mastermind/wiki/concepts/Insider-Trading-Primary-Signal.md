---
title: "Insider-Trading als Primary Signal"
type: concept
tags: [defcon, insider-trading, contrarian-signal, form-4, openinsider, b26, b27, active-scoring-validation]
created: 2026-04-26
updated: 2026-04-27
sources: [Lakonishok-Lee-2001, Ke-Huddart-Petroni-2003, 2iQ-Insider-Meta-Review-2021]
related: [Wissenschaftliche-Fundierung-DEFCON, Earnings-Foreknowledge-Window, insider-intelligence, OpenInsider, DEFCON-System, Accruals-Anomalie-Sloan]
wissenschaftlicher_anker: "B26 (Lakonishok & Lee 2001, RFS 14(1)) — Primärquelle Insider-Trading-Anomalie: Buy>Sell-Asymmetrie + Aggregate-Predictability + Small-Cap-Concentration + Contrarian-Timing | B27 (Ke/Huddart/Petroni 2003, JAE 35(3)) — Insider-Sells konzentrieren sich Q-9 bis Q-3 vor Earnings-Break (Legal-Jeopardy-vermeidet); 6M-Window verfehlt strukturell | Sekundär: 2iQ Meta-Review (Hable 2021) bündelt Lorie/Niederhoffer 1968 + Seyhun 1986/88/92 + Jeng/Metrick/Zeckhauser 2003 + Dardas 2011 + Cluster-Studien"
konfidenzstufe: peer-reviewed
defcon_block: "Insider-Block (10 Pt., siehe SKILL.md §Insider)"
operative_regel: "Form-4-X/M-Filter via OpenInsider HEILIG; Buy-Side höher gewichtet als Sell-Side; diskretionäres Selling >$20M/90 Tage = automatisches FLAG."
aliases:
  - "Insider Primary Signal"
  - "Insider-Trading-Heuristik"
---

# Insider-Trading als Primary Signal

> Lakonishok & Lee (2001) etablieren empirisch: Insider-Käufe sind informativer als Insider-Verkäufe; Aggregate-Insider-Aktivität prädiziert Markt-Returns; Insider sind Contrarians; Effekt stärker bei Small-Caps. Ke/Huddart/Petroni (2003) erklären die scheinbare Sell-Schwäche durch Window-Artefakt: Sells finden Q-9 bis Q-3 vor Earnings-Breaks statt, nicht in den letzten 2 Quartalen (Legal-Jeopardy + ITSFEA 1988).

## Definition

**Primary Signal** = die Insider-Block-Heuristiken sind nicht abgeleiteter Sentiment-Indikator, sondern **direkt informativer Cross-Section-Predictor** mit eigenständiger Cross-Validation gegen Earnings-Breaks und Markt-Timing.

## 5 Operative Heuristiken (insider-intelligence-Skill v1)

| # | Heuristik | Primärquelle | Status |
|---|---|---|---|
| 1 | **Form-4-X/M-Filter** (Code S = diskretionär; M = 10b5-1; F = Tax) | B26 + Operative Disziplin | ✅ Implementiert via [[OpenInsider]]-Pflichtcheck |
| 2 | **Buy-Side höher gewichtet** als Sell-Side | B26 (Buy = diskretionär + Eigenkapital; Sell = Liquidität/Vesting/Diversifikation) | ✅ $5M-Cluster-Schwelle für Buys vs $20M-FLAG-Schwelle für Sells |
| 3 | **Diskretionäres Selling >$20M / 90 Tage** = automatisches FLAG | Operative Heuristik | ✅ FLAG überschreibt jeden DEFCON-Score |
| 4 | **Cashless-Exercise-Ausnahme** (M+S am gleichen Tag, Expiry ≤30 Tage) | Operative Disziplin | ✅ Implementiert (Spalte „Option Expiry") |
| 5 | **Small-Cap-Premium** (B26: stärkster Effekt bei Small-Growth) | B26 | ⚠️ NICHT aktiviert — DEFCON-Universum ist Mid-/Large-Cap (>$10B); Effekt schwächer aber nicht null |

## Komplementarität B26 ↔ B27

L&L sagt: „Insider-Käufe sind informativer als -Verkäufe."  
KHP zeigt **warum**: Insider-Verkäufe vor Earnings-Breaks geschehen 9-3 Quartale **VOR** dem Break (legal jeopardy avoidance, Section 10(b) + ITSFEA 1988).

| Window | Capture-Rate (Sell-Pre-Break-Zone) | Status |
|---|---|---|
| **6 Monate** (insider-intelligence v1) | Verfehlt strukturell die Q-9 bis Q-3 Sell-Zone | Aktuell aktiv |
| **24 Monate** (insider-intelligence v2, deferred) | Captured Q-9 bis Q-3 vollständig + Q-2/Q-1 (Compliance-Kontext) | Geplant für 2027+ |
| Quartals-stratifiziert mit Break-Definition | Theoretical Optimum | Nicht im v2-Scope |

→ Wer das L&L-Window auf 9 Quartale erweitert (B27), findet die fehlenden Sell-Signale. **Beide Befunde zusammen → insider-intelligence v2-Roadmap.**

## Beziehung zu anderen DEFCON-Blöcken

- **EPS-Revision-Delta** (Sentiment-Block, B11) ist strukturell **nachlaufend** vs. Insider-Trades. Eigenes Insider-Window erfasst Information ~6-18 Monate früher als Analyst-Revisions (KHP-Kernbefund).
- **fcf_trend_neg / fcf_trend_pos** (Fundamentals-Watch) ist verwandtes nachlaufendes Signal — wenn FCF-Trend bricht, sind Insider oft schon 9-3 Quartale früher dran. Cross-Validation-Möglichkeit für Schema-Watches.
- **Accruals-Anomalie-Sloan** (B14) — Beneish-Bridge: Insider verwenden Earnings-Manipulationsspielraum, um Sell-Timing zu optimieren. Earnings-Quality-Validierung (Accruals-Ratio) komplementär zu Insider-Signalen.

## Was diese Page NICHT umfasst

- **Aggregate-Insider-Indicator** (L&L-Aggregate-Befund, Seyhun 1992: bis zu 60% 1-Jahres-Return-Variation): NICHT im DEFCON enthalten — DEFCON ist Bottom-Up (per Ticker), Top-Down-Markt-Timing absichtlich nicht modelliert.
- **Cluster-Buying-Premium** (Alldredge/Blank 2017, Kang/Kim/Wang 2018): Optional in `insider-intelligence` zu erweitern, deferred (nicht 2026 priorisiert).
- **Small-Cap-Bonus** (B26): nicht aktiviert (Universum-Diskrepanz).

## Limitationen

- **Sekundärquelle für L&L:** Raw-PDF von Lakonishok-Lee 2001 ist image-only (kein Text-Layer extrahierbar). Numerische Magnituden via 2iQ Meta-Review sekundär-zitiert. Inhaltliche Befunde HOCH-konfident (kanonische Primärreferenz weithin repliziert), numerische Werte MITTEL-konfident. Bei Bedarf an Primärzitaten: NBER WP 6656 oder RFS 14(1) konsultieren.
- **Universum-Mismatch:** L&L-Effekt am stärksten bei Small-Growth-Stocks; DEFCON-Universum ist strukturell Mid-/Large-Cap. Effekt-Stärke quantitativ nicht 1:1 übertragbar.
- **Window-Artefakt:** Aktuelles 6M-Window erfasst nur Q-2/Q-1-Zone, in der Insider-Sells legaljuristisch unterdrückt sind. Apparent „Buy>Sell"-Asymmetrie ist teilweise Methoden-Artefakt, nicht reines Informations-Asymmetrie-Argument.

## Backlinks

- [[Lakonishok-Lee-2001]] — Primärquelle (B26, `active-scoring-validation`)
- [[Ke-Huddart-Petroni-2003]] — Primärquelle (B27, `design-context`)
- [[Earnings-Foreknowledge-Window]] — komplementäre Concept-Page (B27-spezifisch, 9-3-Quartale-Sell-Zone)
- [[2iQ-Insider-Meta-Review-2021]] — Sekundärquelle, bündelt L&L mit historischer Insider-Trading-Forschung
- [[insider-intelligence]] — operativer Skill v1, B26-validated; v2 (B27-aktiviert) deferred
- [[OpenInsider]] — Daten-Pflichtquelle (Form-4-Filter X/M)
- [[DEFCON-System]] — Insider-Block 10 Pt.
- [[Accruals-Anomalie-Sloan]] — Earnings-Quality-Komplement (Beneish-Bridge)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befunde B26 + B27
