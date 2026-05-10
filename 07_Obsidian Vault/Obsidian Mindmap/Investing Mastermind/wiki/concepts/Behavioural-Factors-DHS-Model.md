---
title: "Behavioural Factors — DHS Model"
type: concept
tags: [defcon, behavioural-finance, peed-factor, fin-factor, sentiment-block, insider-block, b30, active-scoring-validation]
created: 2026-05-09
updated: 2026-05-09
sources: [Daniel-Hirshleifer-Sun-2020-Behavioural-Factors]
related: [Wissenschaftliche-Fundierung-DEFCON, Insider-Trading-Primary-Signal, Media-Pessimism-Sentiment, Noise-Trader-Model, Earnings-Foreknowledge-Window, Lakonishok-Lee-2001, Ke-Huddart-Petroni-2003, Tetlock-2007, Jadhav-Mirza-2025, DEFCON-System]
wissenschaftlicher_anker: "B30 (Daniel, Hirshleifer & Sun 2020, RFS 33(4)) — Drei-Faktor-Behavioural-Modell (MKT + PEAD + FIN), das eine breite Anomalie-Menge besser erklärt als Fama-French-3/5. Theoretische Klammer für die DEFCON-Ankerquellen B11 (Crowd-Bias), B26 (Insider-Buy>Sell), B27 (Insider-Sell-Window), B28 (Mean-Reversion). Wichtig: Buyback-Aktivität gehört NICHT in den Sentiment-Block, sondern konzeptuell zu FIN (Long-Horizon-Behavioural). Anti-Methodology-Drift-Anker für V-Q2-28.04. + BRK.B-04.05.-Reinfälle."
konfidenzstufe: peer-reviewed
defcon_block: "Sentiment-Block (10 Pt.) + Insider-Block (5 Pt.) — Klammer-Anker, KEIN neues Score-Element"
operative_regel: "(1) Buyback-Aktivität ist KEIN Sentiment-Bonus — gehört konzeptuell zu FIN-Long-Horizon-Behavioural-Faktor (deferred). (2) Earnings-Day-Reaktionen (Tag 0) sind Noise-Trading-Phase; PEAD-Drift entfaltet sich über 1-3 Monate — Tag-+1-Discipline §19.1 ist wissenschaftlich verankert. (3) DHS-Faktoren sind Long-Short, DEFCON ist Long-Only — Adoption als Sub-Score wäre §28.1-Migration."
aliases:
  - "DHS Model"
  - "DHS-Modell"
  - "PEAD-FIN-Modell"
  - "Behavioural Two-Factor"
  - "Daniel Hirshleifer Sun"
---

# Behavioural Factors — DHS Model

> Daniel, Hirshleifer & Sun (2020) konstruieren ein Drei-Faktor-Behavioural-Modell (MKT + PEAD + FIN), das eine breite Anomalie-Menge besser erklärt als Fama-French-Multi-Faktor-Modelle. Zwei Behavioural-Drift-Phänomene reichen empirisch aus: kurzfristige Underreaction auf Earnings-Surprises (PEAD-Drift signifikant 1-2 Quartale post-Formation; statistische Insignifikanz nach 6-9 Monaten, Tabelle 5 Panel A) + langfristige Mispricing-Korrektur via Manager-Timing-Indikatoren (FIN, 1-3 Jahre Half-Life). Das Modell liefert die theoretische Klammer für viele heute lose nebeneinanderstehende DEFCON-Anker-Befunde.

## Operative Definition

**DHS-Modell** bezeichnet das von Daniel/Hirshleifer/Sun (2020) vorgeschlagene Drei-Faktor-Asset-Pricing-Modell mit:

1. **MKT** (Markt-Excess-Return) — Standard.
2. **PEAD-Faktor** (Post-Earnings-Announcement Drift) — Long Top-CAR-Quintile / Short Bottom-CAR-Quintile. CAR = 4-Tage-Cumulative-Abnormal-Return um Earnings-Announcement, Window (t−2, t+1) um RDQ. Footnote 13 des Papers wählt CAR-basierten PEAD über SUE-basierten (stärkere Erklärungskraft, Chan/Jegadeesh/Lakonishok 1996). Drift signifikant 1-2 Quartale post-Formation; statistische Insignifikanz nach 6-9 Monaten (Tabelle 5 Panel A). Theoretischer Mechanismus: Limited-Attention/Anchoring (Hirshleifer/Teoh 2003).
3. **FIN-Faktor** (Financing) — Long Buyback-Heavy-Firmen / Short Issuance-Heavy-Firmen, definiert über Net Stock Issuance. Half-Life 1-3 Jahre. Theoretischer Mechanismus: Manager-Timing-gegen-Mispricing (Loughran/Ritter 1995).

**CAR (4-Day Cumulative Abnormal Return um Earnings-Announcement)** = Σ_{d=t−2}^{t+1} (R_i,d − R_m,d) — primäre PEAD-Sortier-Variable im DHS-Modell.

**SUE** = Standardized Unexpected Earnings = (actual EPS − consensus EPS) / σ(consensus). Standard-Maß für Earnings-Surprise; im DHS-Modell **nur als Robustness-Komparator** (siehe Footnote 13 zur stärkeren CAR-Erklärungskraft), nicht primäre Faktor-Konstruktions-Variable.

**Net Stock Issuance** = (Shares Outstanding_t − Shares Outstanding_{t-1}) × Price / Market-Cap_{t-1}. Buybacks zählen negativ, Equity-Emissionen positiv.

## Empirie-Position des DHS-Modells

| Test | DHS-3-Faktor (MKT+PEAD+FIN) | FF-5-Faktor (MKT+SMB+HML+RMW+CMA) |
|---|---|---|
| Unerklärte Anomalien (sig. α 5%, 34 untersucht) | **3/34** BF3 | **18/34** FF5 |
| GRS-F-Test über alle 34 Anomalien (Table 7 Panel C) | F=**1,61** (kleinster) | F=**2,60** |
| Quality-/Profitabilitäts-Anomalien | weitgehend absorbiert via FIN | partiell absorbiert via RMW |
| Issuance-related Anomalien | direkt absorbiert via FIN | nicht spezifisch adressiert |
| Earnings-Drift-Anomalien (PEAD-related) | direkt absorbiert via PEAD | nicht spezifisch adressiert |
| Theoretische Begründung | Behavioural (Limited-Attention + Manager-Timing) | Risk-Based (Profit/Investment-Risiken) |

→ DHS hat **nicht universell überlegene** Performance, sondern ist auf Quality-/Issuance-Cluster und Earnings-Drift-Subset stärker. Beide Modelle sind komplementär; der Theorie-Streit (behavioural vs. risk) ist für DEFCON-Operationalisierung irrelevant.

## DEFCON-Implikation (B30 `active-scoring-validation`)

### Was B30 NICHT ändert

- **Sentiment-Block (10 Pt.)** bleibt strukturell: Analyst-Konsensus 3 Pt. + PT-Abstand 3 Pt. + Sell-Ratio-Check 4 Pt.
- **Insider-Block (5 Pt.)** bleibt strukturell: Form-4-X/M-Filter via [[OpenInsider]] + Buy>Sell-Asymmetrie + $20M-FLAG-Schwelle.
- **Kein PEAD-Sub-Score.** EPS-Revision-Bonus +1 ist bereits PEAD-adjacent in Sentiment-Block; weitere PEAD-Operationalisierung wäre §27.1 Double-Counting.
- **Kein FIN-Sub-Score.** Net Issuance ist nicht in DEFCON v3.7. Adoption wäre §28.1-Migration mit §29.4 t-Hurdle + §29.7 M&P-Discount.

### Was B30 begründet — drei Operative Konsequenzen

#### (1) Anti-Methodology-Drift-Disziplin: Buyback ≠ Sentiment-Bonus

Zwei dokumentierte Reinfälle 2026:

- **V Q2 FY26 28.04.2026 (mittags-Variante, später durch Codex-HIGH-1+2-Review reverted):** $20B Buyback-Authorization wurde als Sentiment-Δ +1 ad-hoc-eingebucht, weil „erweiterter EPS-Revision-Anker". Das war doppelt falsch: (a) ROIC-Methodology-Drift war Hauptproblem (Codex-HIGH-1); (b) Buyback ist kein Sentiment-Signal, sondern strukturell Long-Horizon-Behavioural. Memory `feedback_skill_methodology_drift_v_q2.md` dokumentiert die Lehre.
- **BRK.B Q1 FY26 04.05.2026 Tag-+1-Vollanalyse:** Annual-Meeting-Color +2 wurde als Sentiment-Drift entfernt nach Codex-R1-REJECT-Korrektur (Score 75→71 Δ-4). Kein direkter Buyback-Bezug, aber gleiches Klassifikations-Problem: nicht-Sentiment-Information wurde im Sentiment-Block als +1/+2 verbucht.

**Anti-Pattern-Anker via B30:**
- Sentiment-Block = Tagesnachrichten-Mittel-Reversion-Signal (B28 Tetlock theoretisch verankert).
- Buyback = Long-Horizon-FIN-Behavioural-Signal (B30 theoretisch verankert) — gehört konzeptuell NICHT in den Sentiment-Block.
- Earnings-Surprise-Reaktion = Short-Horizon-PEAD-Behavioural (B30 theoretisch verankert), bereits via EPS-Revision-Bonus +1 partiell abgebildet — kein zusätzlicher Bonus auf Earnings-Day-Reaktion.

→ **Operative Regel:** Buyback-Aktivität, Annual-Meeting-Tone, Capital-Allocation-Statements werden NICHT als Sentiment-Block-Bonus verbucht. Falls sie scorerelevant erscheinen, gehört das in eine eigene Methodology-Watch-PIPELINE-Item (FIN-Score-Migration §28.1) — niemals ad-hoc-Lift.

#### (2) Earnings-Wait-Discipline §19.1 wissenschaftlich verankert

PEAD-Drift entfaltet sich über 1-3 Monate; Tag-0-Reaktion auf Earnings-Surprise ist Noise-Trading-Phase. Memory `feedback_earnings_call_wait_discipline.md` dokumentiert die operative Begründung (Token-Effizienz + Methodology-Cleanliness); B30 liefert die ökonomische Begründung dazu:

- **Tag 0** = Earnings-Call-Recap (`_extern/earnings-recap`) + FLAG-Quick-Check + Pre-Call-Snapshot. Kein Score-Move, weil PEAD-Drift in dem Window dominiert noise.
- **Tag +1** = Vollanalyse mit Transcript-Read + Score-Move + 8-File-Sync. Information ist nun cleansed; Drift-Phase informativ statt panic-driven.

#### (3) Wissenschaftliche Klammer für B11/B26/B27/B28

| Befund | Bisheriger Anker | DHS-Klammer |
|---|---|---|
| **B11 Crowd-Consensus-Bias** (Jadhav/Mirza 2025) | Empirie-Befund Sentiment-Bias | Special-Case PEAD-Komponente — Crowd-Underreaction auf negative Information |
| **B26 Insider-Buy>Sell** (Lakonishok/Lee 2001) | Empirie-Befund Insider-Asymmetrie | Mikro-Manifestation FIN-Manager-Timing — Insider als individueller Manager-Mispricing-Detektor |
| **B27 Insider-Sell-Window 9-3-Quartale** (Ke/Huddart/Petroni 2003) | Legal-Jeopardy-Window | FIN-Mikro-Mechanismus — Sells finden vor materieller Information statt, nicht danach |
| **B28 Tetlock Mean-Reversion** (2007) | Mean-Reversion-Sentiment | Limits-of-Arbitrage-Annahme der DHS-Theorie |

→ **Vorher:** vier nebeneinanderstehende Empirie-Befunde mit jeweils eigenem Anker. **Nachher:** ein theoretisches Klammer-Modell, das die operative Sinnhaftigkeit der Sentiment-/Insider-Architektur explizit macht.

## Beziehung zu anderen DEFCON-Layern

- **B14 Sloan Accruals** — Earnings-Quality-Manipulation kann als Manager-Timing-Vorbereitung interpretiert werden (FIN-adjacent), aber Sloan ist `active-scoring (implicit)` über Accruals-Ratio-Malus; B30 erzeugt keinen Konflikt.
- **B19 FINSABER (Li/Kim/Cucuringu/Ma 2026)** — Bull/Bear-Asymmetrie + LLM-Investing-Bias-Audit. B30 liefert ökonomisches Mikro-Modell, B19 das Audit-Framework darüber.
- **B24 FinDPO (Iacovides/Zhou/Mandic 2025)** — orthogonal zu DEFCON Long-Only (analog DHS Long-Short-Caveat). Beide sind Future-Reference für Sentiment-Block-Architektur.
- **§19.1 Earnings-Wait-Discipline** (INSTRUKTIONEN.md, eingeführt 28.04.2026 spätabends post V-Q2) — wissenschaftlich verankert via B30 PEAD-Komponente.

## Was diese Page NICHT umfasst

- **Vollständige PEAD-/FIN-Sub-Score-Operationalisierung** — wäre §28.1-Migration. Deferred.
- **DHS vs. q-Faktor-Modell-Vergleich (Hou/Xue/Zhang 2015)** — q-Faktor-Modell adressiert ähnliches Anomalie-Set risk-based; Theorie-Debatte für DEFCON irrelevant.
- **Long-Only-Konversion der DHS-Faktoren** — non-trivial, ~50-60% Faktor-Return aus Long-Side allein. Adoption nur via §28.1-Migration mit Long-Only-Validation.
- **Daniel/Hirshleifer/Subrahmanyam 1998 (DHS-Theorie-Vorläufer Overconfidence-Modell)** — könnte als SOURCE-ONLY-Anker später ergänzt werden; nicht in dieser Phase.

## Limitationen

- **Long-Short-Konstruktion:** Faktoren sind Long-Short. DEFCON-Long-Only-Mapping ist nicht 1:1; das ist der zentrale Grund warum kein direkter FIN-/PEAD-Sub-Score adoptiert wird.
- **Post-Publication-Decay (DEFCON-Konvention):** [[McLean-Pontiff-2016]] (B25) liefert die DEFCON-Konvention M&P-Discount-Faktor 0,42 auf zitierte FIN-/PEAD-Outperformance — das ist DEFCON-eigene Vorsichtsmarge, **nicht** eigenständige DHS-Paper-Implikation. Bei Briefing-Sprache und §28.1-Migration zwingend zu berücksichtigen.
- **Sample-Periode:** 1972:07–2014:12 (510 Monate, US-Compustat). Non-US-Übertragbarkeit (Faktor-Konstruktion bei Non-US) nicht im Originalpapier. Für DEFCON 8 US-Satelliten + 3 Non-US-Satelliten relevant: B30-Klammer-Logik gilt theoretisch international, aber Faktor-Konstruktion müsste pro Markt re-validiert werden — irrelevant solange B30 nur als Klammer, nicht als Sub-Score.
- **Behavioural vs. Risk-Theorie:** Daniel/Hirshleifer argumentieren rein behavioural; Risk-Based-Alternative (Cochrane 2017) nicht ausgeschlossen. Für DEFCON irrelevant — Cross-Section-Predikabilität ist beides Mal vorhanden.
- **Methodology-Drift-Anti-Pattern ist KEIN automatischer Schutz:** B30 sagt „Buyback gehört nicht in Sentiment", aber operative Schutzmaßnahme bleibt SKILL-Output-Template-Klammer-Notation + Codex-Review-Disziplin. Theorie-Anker reduziert das Risiko, eliminiert es nicht.

## Operative Anwendung in DEFCON

1. **SKILL-Output-Template Sentiment-Block** soll B30-Klammer-Notation tragen analog B26/B27/B28-Pattern — Edit ist dokumentiert, aber bis zum SKILL.md-Schritt-3-Edit-Slot deferred (Phase D-1 Closure-Disposition: kleiner Folge-Edit, keine Pflicht für Phase-1-Sync-Set).
2. **SKILL-Output-Template Insider-Block** soll B30-Klammer-Notation tragen als FIN-Mikro-Manifestations-Anker — gleicher deferred Status. Im Skill ist die Anti-Buyback-Disziplin via §27.7-Cross-Reference (B30 NICHT in Sentiment-Block, NICHT in Insider-Block; FIN-Komplex deferred) bereits aktiv (Phase D-1 2026-05-09 Final-Closure).
3. **Anti-Buyback-Sentiment-Drift-Schutz:** Bei Buyback-Authorization, Capital-Allocation-Statements, Annual-Meeting-Color-Aussagen explizit prüfen, ob diese als Sentiment-Bonus verbucht werden sollen. Default-Antwort = NEIN, weil B30 zeigt: das gehört konzeptuell zu FIN-Long-Horizon, nicht zu Sentiment-Mean-Reversion.
4. **Earnings-Wait-Discipline §19.1** ist wissenschaftlich verankert; Tag-+1-Pattern bleibt Pflicht.
5. **FIN-Score-Pfad-Vorschlag deferred** bis BRK.B Q2 FY26 ~02./03.08. Buyback-Cashflow-Reconciliation (PIPELINE #40); falls dort Buyback-Methodology-Saubermachung systematisch wird, eigene Migration-Session.

## Backlinks

- [[Daniel-Hirshleifer-Sun-2020-Behavioural-Factors]] — Primärquelle (B30, source-page)
- [[Wissenschaftliche-Fundierung-DEFCON]] — §Status-Matrix B30 `active-scoring-validation`
- [[Insider-Trading-Primary-Signal]] — komplementäre Concept-Page (B26 + B27, FIN-Mikro-Manifestation)
- [[Media-Pessimism-Sentiment]] — komplementäre Concept-Page (B28, Limits-of-Arbitrage-Annahme)
- [[Noise-Trader-Model]] — DeLong/Shleifer/Summers/Waldmann 1990 (B30-Theorie-Vorläufer)
- [[Earnings-Foreknowledge-Window]] — KHP-2003 (B27, FIN-Mikro-Mechanismus)
- [[Lakonishok-Lee-2001]] — Primärquelle B26
- [[Ke-Huddart-Petroni-2003]] — Primärquelle B27
- [[Tetlock-2007]] — Primärquelle B28
- [[Jadhav-Mirza-2025]] — Sentiment-Bias-Befund (B11)
- [[DEFCON-System]] — Sentiment-Block 10 Pt. + Insider-Block 5 Pt.
