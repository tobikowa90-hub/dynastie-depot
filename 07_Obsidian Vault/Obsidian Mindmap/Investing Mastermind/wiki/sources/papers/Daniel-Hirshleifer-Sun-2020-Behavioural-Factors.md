---
title: "Short- and Long-Horizon Behavioral Factors"
date: 2020
type: source
subtype: academic-paper
tags: [defcon, behavioural-finance, peed-factor, fin-factor, sentiment-block, insider-block, b30, active-scoring-validation]
url: https://academic.oup.com/rfs/article-abstract/33/4/1673/5544316
venue: "Review of Financial Studies 33(4), 2020, 1673-1736 (NBER WP 24163, 2018)"
authors: "Kent D. Daniel (Columbia GSB), David Hirshleifer (UC Irvine / USC Marshall), Lin Sun (Florida International University)"
status: primary-belegt
medium: paper
created: 2026-05-09
updated: 2026-05-10
defcon_relevanz: "Befund B30 (`active-scoring-validation`, eingeführt 2026-05-09 Phase D-1). Sentiment-Block (10 Pt.) + Insider-Block (5 Pt., konzeptuell-erweitert) — wissenschaftlicher Klammer-Anker für die heute lose nebeneinander stehenden behavioural-empirischen Ankerquellen B11 (Crowd-Consensus-Bias, Jadhav/Mirza), B26 (Insider-Buy>Sell, Lakonishok/Lee), B27 (Insider-Sell-Window, Ke/Huddart/Petroni) und B28 (Media-Pessimism Mean-Reversion, Tetlock). Kern-These: Zwei Behavioural-Faktoren reichen empirisch aus, um eine breite Anomalie-Menge zu erklären — (1) PEAD = Post-Earnings-Announcement Drift (Short-Horizon Underreaction auf Earnings-Surprises) + (2) FIN = Financing-Faktor (Long-Horizon Mispricing via Issuance-vs-Buyback-Asymmetrie). Operative Konsequenz für DEFCON: KEIN neues Score-Element. B30 liefert das Modell-Klammer-Argument, warum die DEFCON-Blöcke Sentiment + Insider + Buyback-relevante-Indikatoren empirisch funktionieren — sie sind Manifestationen derselben zwei Behavioural-Drift-Phänomene. Wichtige praktische Implikation aus der Long-Horizon-Komponente FIN: Buyback-Aktivität ist KEIN Sentiment-Signal (Methodology-Drift V-Q2-28.04. + BRK.B-04.05.-Annual-Meeting-Lehre), sondern ein eigenständiger Long-Horizon-Behavioural-Indikator — das Mapping `Buybacks → Sentiment-Bonus` ist falsch; korrektes Mapping wäre `Buybacks → strukturelles FIN-Signal mit langem Half-Life`."
sources: []
related:
  - "[[Behavioural-Factors-DHS-Model]]"
  - "[[Insider-Trading-Primary-Signal]]"
  - "[[Media-Pessimism-Sentiment]]"
  - "[[Noise-Trader-Model]]"
  - "[[Earnings-Foreknowledge-Window]]"
  - "[[Lakonishok-Lee-2001]]"
  - "[[Ke-Huddart-Petroni-2003]]"
  - "[[Tetlock-2007]]"
  - "[[Jadhav-Mirza-2025]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
  - "[[DEFCON-System]]"
raw_path: "raw/papers/Daniel, Hirshleifer, Sun (2020).pdf"
aliases:
  - "Daniel Hirshleifer Sun 2020"
  - "DHS 2020"
  - "Short and Long Horizon Behavioral Factors"
  - "PEAD-FIN-Modell"
  - "Behavioural Two-Factor Model"
---

# Daniel, Hirshleifer & Sun (2020) — Short- and Long-Horizon Behavioral Factors

> ✅ **PRIMÄRBELEG (Voll-PDF gelesen 2026-05-09 sehr-spät / 2026-05-10 früh, Phase-D-1 Confidence-Upgrade-Pass):** Daniel/Hirshleifer/Sun (2020) RFS 33(4) S. 1673-1736 vollständig ingested. Alle quantitativen Magnituden (Faktor-Konstruktionen, Spanning-Statistiken, GRS-F-Werte, Sample-Periode, Long-/Short-Leg-Asymmetrie) sind aus Original-Tabellen verifiziert (Tables 1-10 + Sections 2-5 + Footnote 13 zur CAR-vs-SUE-Wahl). **Confidence-Level: HOCH** für Befunde + Magnituden + Methodik-Beschreibung. **Verbleibende Restvorbehalte (markiert):** (a) Eine exakte Long-Only-Konversionsquote ist im Paper nicht beziffert — die in Tabelle 10 dokumentierte Long-/Short-Leg-Asymmetrie (avg βF IN +0,03 long vs −0,27 short; avg βPEAD +0,31 long vs −0,51 short) erlaubt nur qualitative Einordnung; eine quantitative Long-Only-Implementierung erfordert §28.1-Backtest-Validierung. (b) Der M&P-Discount-Faktor 0,42 ist **DEFCON-Konvention** über [[McLean-Pontiff-2016]] (B25), **nicht** eigenständige DHS-Paper-Implikation.

## Abstract (eigene Worte)

Daniel, Hirshleifer und Sun konstruieren ein **Drei-Faktor-Behavioural-Modell** als Alternative zu Fama-French-3-/4-/5-Faktoren-Modellen. Das Modell besteht aus:

1. **Markt-Faktor (MKT)** — Standard-Markt-Excess-Return über Risk-Free-Rate.
2. **PEAD-Faktor (Post-Earnings-Announcement Drift)** — Short-Horizon-Faktor, der die systematische Underreaction auf Earnings-Surprises operationalisiert: Long-Position in Stocks mit höchster 4-Tage-Cumulative-Abnormal-Return (CAR) um die jüngste Earnings-Announcement, Short-Position in niedrigsten. CAR berechnet als R_i,d − R_m,d über das Window (t−2, t+1) um RDQ. **Footnote 13 des Papers:** CAR-basierter PEAD-Faktor hat stärkere Erklärungskraft als SUE-basierter (Chan/Jegadeesh/Lakonishok 1996); SUE bleibt empirische Robustness-Komparator. Drift signifikant 1-2 Quartale post-Formation; statistische Insignifikanz nach 6-9 Monaten (Tabelle 5 Panel A).
3. **FIN-Faktor (Financing)** — Long-Horizon-Faktor aus Net Stock Issuance: Long-Position in Buyback-Heavy-Firmen (negative Net Stock Issuance), Short-Position in Issuance-Heavy-Firmen; konstruiert über Index aus 1-Jahres-Net-Share-Issuance (Pontiff/Woodgate 2008) UND 5-Jahres-Composite-Share-Issuance (Daniel/Titman 2006); 2x3 Sort auf Size × Financing-Index. Mispricing-Erosion über 1-3 Jahre. **Kritisch:** FIN benötigt MULTI-YEAR-Issuance-Pattern, nicht single-quarter Buyback-Authorization — methodischer Anker für die §27.7 Anti-Sentiment-Drift-Disziplin (V-Q2 28.04. + BRK.B 04.05. Reinfälle waren multi-faceted: Klassifikations- + Zeit-Horizont-Fehler).

**Theoretische Begründung:** PEAD ist klassische Underreaction durch Limited-Attention/Anchoring (Hirshleifer/Teoh 2003). FIN reflektiert Manager-Timing-Ability gegen Mispricing — Manager kaufen Aktien zurück, wenn sie ihre eigenen Aktien für unterbewertet halten, und emittieren neue Aktien bei Überbewertung (Loughran/Ritter 1995). Beide sind Behavioural-Theorie-konsistent, NICHT risk-based.

**Anti-Sentiment-Drift-Anker (DHS S. 5, literal):** „FIN is designed to capture longer-term mispricing and correction, as opposed to short-term mispricing... such corporate events [issuance and repurchase] tend to occur only occasionally, rather than as immediate responses to even transient mispricing." Direkter theoretischer Anker für die DEFCON-Disziplin: Buyback ist KEIN Sentiment-Signal — die zugrundeliegende Capital-Allocation-Entscheidung adressiert mittel- bis langfristige Mispricing, nicht den Tagesnachrichten-Pulse, der den Sentiment-Block treibt.

**Empirie-Ergebnis:** Das DHS-3-Faktor-Modell **erklärt eine breitere Anomalie-Menge als Fama-French-5-Faktor** — insbesondere viele Quality-/Profitabilitäts-Anomalien werden durch FIN absorbiert (Buyback-Heavy-Firmen sind oft Quality-Firmen). PEAD absorbiert Momentum-related Drift bei Earnings-Events. Zusammen reduzieren die zwei Behavioural-Faktoren die Anzahl unerklärter Anomalien substanziell gegenüber dem klassischen Multi-Faktor-Kanon.

## Drei Kern-Befunde (für DEFCON-Anker relevant)

1. **Behavioural-Asymmetrie ist quantifizierbar als zwei orthogonale Drift-Phänomene.** Underreaction (kurz, ~3M) + Manager-Timing (lang, 1-3J). Beide sind in den Anomalie-Daten mess-stark, beide sind Theorie-konsistent gegen Limits-of-Arbitrage.

2. **FIN-Faktor wird primär durch Net Stock Issuance konstruiert, nicht direkt durch Buyback-Volume.** Issuance ist die saubere ökonomische Variable, weil sie Buybacks (negative Issuance) und Equity-Emissionen (positive Issuance) symmetrisch behandelt. Das ist wichtig für DEFCON: Buybacks alleine (ohne Issuance-Kontext) sind nicht das saubere Signal — Net Issuance ist es.

3. **PEAD-Faktor liefert wissenschaftliche Fundierung für die Earnings-Window-Architektur.** Das DEFCON-Earnings-Wait-Discipline-Pattern (§19.1, V-Q2-Reinfall 28.04.2026) sagt: Tag-+1 Vollanalyse, nicht Tag-0 — operative Begründung war Token-Effizienz + Methodology-Cleanliness. B30 liefert die ökonomische Begründung dazu: PEAD-Drift ist real, aber findet auf 3-Monats-Horizont statt; Tag-0-Reaktion auf Earnings-Surprise ist Noise-Trading mit hoher Mean-Reversion-Wahrscheinlichkeit (siehe auch B28 Tetlock).

## DEFCON-Implikation (B30 `active-scoring-validation`)

### Was B30 NICHT ändert

- **Sentiment-Block (10 Pt.) bleibt strukturell** (Analyst-Konsensus + PT-Abstand + Sell-Ratio).
- **Kein PEAD-Faktor-Score-Element.** PEAD ist Long-Short-Faktor; DEFCON ist Long-Only-Stock-Picking. Mapping wäre nicht-trivial und §27.1-Double-Counting-gefährdet (EPS-Revision-Bonus +1 ist bereits PEAD-adjacent).
- **Kein FIN-Faktor-Score-Element.** Net Issuance ist nicht in DEFCON v3.7 enthalten. Migration wäre §28.1-Workflow mit §29.4 t-Hurdle + §29.7 M&P-Discount.

### Was B30 begründet

1. **Anti-Methodology-Drift-Disziplin: Buyback ≠ Sentiment-Bonus.** V-Q2-Reinfall 28.04.2026 (Buyback $20B Authorization → Sentiment-Δ +1 als „erweiterter EPS-Revision-Anker") und BRK.B-04.05.-Annual-Meeting-Lehre (Annual-Meeting-Color +2 als Sentiment-Drift entfernt) sind beide Manifestationen desselben Klassifikations-Fehlers: Buyback ist KEIN Sentiment, sondern strukturell Long-Horizon-Behavioural (FIN-Faktor). B30 liefert den theoretischen Block-Schnitt: Sentiment-Block = Tagesnachrichten-Mittel-Reversion (B28 Tetlock); Behavioural-Buyback-Signal = Long-Horizon-FIN (B30); Earnings-Revision = Short-Horizon-PEAD-adjacent (B30 erste Komponente). **Operative Schlussfolgerung:** Buyback-Aktivität gehört NICHT in den Sentiment-Block (10 Pt.) sondern konzeptuell in einen ggf. zukünftigen FIN-Sub-Score (deferred). Solange dieser nicht existiert, ist Buyback-Aktivität explizit KEIN scorbares Element — weder im Sentiment-Block noch ad-hoc als +1-Bonus.

2. **Wissenschaftliche Klammer für B11/B26/B28.** Bisher standen diese drei Befunde lose nebeneinander. B30 liefert die theoretische Aggregation:
   - **B11 (Crowd-Consensus-Bias)** ist ein Special-Case der DHS-Overconfidence/Limited-Attention-Linie — Analysten als Crowd zeigen Underreaction-Pattern auf negative Information.
   - **B26 (Insider-Buy>Sell-Asymmetrie)** ist ein Special-Case des FIN-Manager-Timing-Mechanismus — Insider-Käufe sind Mikro-Manifestation der gleichen Mispricing-Information, die FIN aggregiert.
   - **B28 (Tetlock Mean-Reversion)** ist die Mikro-Beweis-Linie für die Limits-of-Arbitrage-Annahme, ohne die Behavioural-Faktoren nicht überleben würden.

3. **Earnings-Wait-Discipline §19.1 wissenschaftlich verankert.** Tag-+1-Pattern (V-Q2-Lehre) wird durch PEAD-Theorie gestützt: Earnings-Day-Sentiment ist Noise-Trading-Phase, der reale Drift entfaltet sich über die nachfolgenden 1-3 Monate. Tag-+1-Read mit Transcript ist ökonomisch legitime Information-Cleansing-Stelle.

### Komplementarität B30 ↔ Bestehendem

| Befund | Quelle | Layer | Beziehung zu B30 |
|---|---|---|---|
| **B11** | Jadhav/Mirza 2025 | Crowd-Consensus-Bias-Korrektur | B30 PEAD-Komponente theoretisch tragend |
| **B26** | Lakonishok/Lee 2001 | Insider-Buy>Sell-Asymmetrie | B30 FIN-Komponente Mikro-Manifestation |
| **B27** | Ke/Huddart/Petroni 2003 | Insider-Sell-Window 9-3-Quartale | B30 FIN-Mikro-Mechanismus + Legal-Jeopardy-Komplement |
| **B28** | Tetlock 2007 | Media-Pessimism Mean-Reversion | B30-Theorie-Annahme: Limits-of-Arbitrage |
| **B14** | Sloan 1996 | Accruals-Anomalie | B30 FIN-adjacent (Earnings-Quality-Manipulation) — Sloan ist `active-scoring (implicit)`, kein FIN-Konflikt |

## Methodische Würdigung

- **Faktor-Konstruktion:** PEAD via 2x3 Sort auf CAR × Size; FIN via 2x3 Sort auf Financing-Index × Size (Index aus 1-Jahres-Net-Issuance + 5-Jahres-Composite-Issuance). Standard-Fama-French-Methode, robust gegen Construction-Variations (Hou/Xue/Zhang 2020 q-Factor-Critique).
- **Spanning-Tests (Table 7 Panel C):** DHS-BF3-Modell hat **3 von 34** untersuchten Anomalien mit signifikantem α auf 5%-Niveau (also 31/34 gespannt); FF-5 hat **18/34** signifikante αs (16/34 gespannt). HXZ4 (q-Factor) hat 6 sig. αs, SY4 (Stambaugh/Yuan-Mispricing) hat 7 sig. αs. GRS-F-Test über alle 34 Anomalien: BF3 F=**1,61** (kleinster), FF5 F=**2,60**, HXZ4 F=**2,42** — BF3 dominiert in Aggregation. Carhart-4 ist nicht zentraler Vergleichsbenchmark im Paper; Spanning-Vorteil von BF3 ist primär bei Quality-/Issuance-Cluster und Earnings-Drift-Subset.
- **Sample / Out-of-Sample:** Sample 1972:07–2014:12 (510 Monate), US-Compustat/CRSP. **M&P-Discount-Faktor 0,42** ist **DEFCON-Konvention** via [[McLean-Pontiff-2016]] (B25), **nicht** eigenständige DHS-Paper-Implikation; bei Anwendung in DEFCON-Briefings auf zitierte FIN-/PEAD-Outperformance zu setzen.
- **Long-Short vs. Long-Only-Übertragbarkeit:** Faktoren sind Long-Short konstruiert. **Tabelle 10** zeigt Asymmetrie zwischen Long- und Short-Leg: avg βF IN = **+0,03** (long-leg) vs **−0,27** (short-leg) bei 22 long-horizon Anomalien; avg βPEAD = **+0,31** (long-leg) vs **−0,51** (short-leg) bei 12 short-horizon Anomalien. Short-Side trägt strukturell 70-80% der Faktor-Loadings — Long-Only-Implementierung des FIN-/PEAD-Faktors verliert systematisch Faktor-Return-Anteil; eine exakte Long-Only-Quote ist im Paper nicht beziffert. Das ist der zentrale Grund, warum DEFCON keinen direkten FIN-/PEAD-Sub-Score adoptiert: das Modell-Mapping ist nicht 1:1, und Migration via §28.1 erfordert Long-Only-Backtest-Validierung.
- **Behavioural vs Risk:** Daniel/Hirshleifer argumentieren rein behavioural; Risk-Based-Alternative-Erklärungen (Cochrane 2017) sind nicht ausgeschlossen. Diese Theoriedebatte ist für DEFCON irrelevant — beide Klassen liefern dieselbe operative Schlussfolgerung (Net-Issuance + Earnings-Surprise sind cross-section-prädiktiv).

## Operative Schlussfolgerungen

1. **B30 deaktiviert KEINEN bestehenden Score-Pfad** — Sentiment + Insider bleiben strukturell.
2. **B30 liefert die theoretische Klammer** über B11/B26/B27/B28: zwei Behavioural-Drift-Phänomene erklären die empirische Wirksamkeit der DEFCON-Sentiment- und Insider-Blöcke.
3. **Anti-Buyback-Sentiment-Drift-Anker:** SKILL-Output-Template Sentiment-Block-Klammer-Notation um B30-Hinweis erweitern (analog B26/B27/B28-Pattern). Prävention der wiederholten V-Q2- + BRK.B-04.05.-Methodology-Drifts.
4. **Earnings-Wait-Discipline §19.1 ist wissenschaftlich fundiert** — PEAD-Theorie ist die ökonomische Begründung für Tag-+1-Pattern, ergänzt die operative Token-/Methodology-Cleanliness-Begründung aus Memory `feedback_earnings_call_wait_discipline.md`.
5. **Phase D-2 deferred:** FIN-Sub-Score-Erweiterung (Net Issuance als eigene Fundamentals-Metrik) wäre §28.1-Migration-Workflow mit §29.4 t-Hurdle + §29.7 M&P-Discount. Trigger-Fenster: BRK.B Q2 FY26 ~02./03.08. Buyback-Cashflow-Reconciliation (PIPELINE #40) — falls dort die Buyback-Methodology-Saubermachung systematisch wird, könnte ein FIN-Score-Pfad-Vorschlag eigene Session bekommen.
6. **Long-Short-Caveat dokumentiert (analog B24 FinDPO):** DHS-Faktoren sind Long-Short, DEFCON ist Long-Only. Mapping ist nicht-trivial; Adoption nur via formale §28.1-Migration mit Long-Only-Konversions-Validierung.

## Backlinks

- [[Behavioural-Factors-DHS-Model]] — neue Concept-Page (B30-Anker)
- [[Insider-Trading-Primary-Signal]] — komplementäre Concept-Page (B26 + B27, FIN-Mikro-Manifestation)
- [[Media-Pessimism-Sentiment]] — komplementäre Concept-Page (B28, Limits-of-Arbitrage)
- [[Noise-Trader-Model]] — DeLong/Shleifer/Summers/Waldmann 1990 (B30-Theorie-Vorläufer)
- [[Earnings-Foreknowledge-Window]] — KHP-2003 (B27, FIN-Mikro-Mechanismus)
- [[Lakonishok-Lee-2001]] — Primärquelle B26
- [[Ke-Huddart-Petroni-2003]] — Primärquelle B27
- [[Tetlock-2007]] — Primärquelle B28
- [[Jadhav-Mirza-2025]] — Sentiment-Bias-Befund (B11)
- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — moderner ML-Counterpart (B24, Long-Short-orthogonal)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B30
- [[DEFCON-System]] — Sentiment-Block 10 Pt. + Insider-Block 5 Pt.
- [[kent-d-daniel|Kent D. Daniel]], [[david-hirshleifer|David Hirshleifer]], [[lin-sun|Lin Sun]] — Author-Entities
