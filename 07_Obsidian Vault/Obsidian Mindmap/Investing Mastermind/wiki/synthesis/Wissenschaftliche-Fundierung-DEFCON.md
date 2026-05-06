---
title: "Wissenschaftliche Fundierung DEFCON v3.7"
type: synthesis
tags: [defcon, scoring, wissenschaft, entscheidungsmatrix, faktor-kalibrierung, validation-gate]
sources:
  - "[[arXiv-1711.04837]]"
  - "[[Gu-Kelly-Xiu-2020]]"
  - "[[Morningstar-Wide-Moat]]"
  - "[[Buffetts-Alpha]]"
  - "[[Wolff-Echterling-2023]]"
  - "[[Jadhav-Mirza-2025]]"
  - "[[llms-for-equity-stock-ratings]]"
  - "[[Piotroski-2000]]"
  - "[[Novy-Marx-2013]]"
  - "[[Sloan-1996]]"
  - "[[Bailey-2015-PBO]]"
  - "[[Aghassi-2023-Fact-Fiction]]"
  - "[[Flint-Vermaak-2021-Decay]]"
  - "[[Palomar-2025-Portfolio-Optimization]]"
  - "[[Li-Kim-Cucuringu-Ma-2026-FINSABER]]"
  - "[[Sheppert-2026-GT-Score]]"
  - "[[Arun-et-al-2025-FinReflectKG]]"
  - "[[Labre-2025-FinReflectKG-Companion]]"
  - "[[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]]"
  - "[[Iacovides-Zhou-Mandic-2025-FinDPO]]"
  - "[[McLean-Pontiff-2016]]"
  - "[[Lakonishok-Lee-2001]]"
  - "[[Ke-Huddart-Petroni-2003]]"
  - "[[Tetlock-2007]]"
  - "[[Asness-Frazzini-Pedersen-2013-QMJ]]"
  - "[[Mauboussin-Callahan-2024-Measuring-Moat]]"
  - "[[Amundi-Quality-2021]]"
  - "[[Fama-French-2015-Five-Factor]]"
  - "[[Harvey-Liu-Zhu-2016]]"
  - "[[Asness-Moskowitz-Pedersen-2013-VME]]"
  - "[[Fama-French-2006-Profitability]]"
  - "[[Hou-Xue-Zhang-2015-q-Factor]]"
  - "[[Yang-Liu-Wang-2023-FinGPT]]"
  - "[[2iQ-Insider-Meta-Review-2021]]"
concepts:
  - "[[5J-Fundamental-Fenster]]"
  - "[[FCF-Primacy]]"
  - "[[Moat-Taxonomie-Morningstar]]"
  - "[[Buffett-Faktorlogik]]"
  - "[[QMJ-Faktor]]"
  - "[[chain-of-thought-prompting|Chain-of-Thought Prompting]]"
  - "[[F-Score-Quality-Signal]]"
  - "[[Gross-Profitability-Premium]]"
  - "[[Accruals-Anomalie-Sloan]]"
  - "[[PBO-Backtest-Overfitting]]"
  - "[[Factor-Investing-Framework]]"
  - "[[Factor-Information-Decay]]"
  - "[[Seven-Sins-Backtesting]]"
  - "[[Palomar-Methods-Reference]]"
  - "[[LLM-Investing-Bias-Audit]]"
  - "[[Regime-Aware-LLM-Failure-Modes]]"
  - "[[Composite-Anti-Overfitting-Objective]]"
  - "[[Knowledge-Graph-Finance-Architecture]]"
  - "[[Agentic-Reflection-Pattern]]"
  - "[[LLM-as-a-Judge-Evaluation]]"
  - "[[RAG-Uncertainty-Quantification]]"
  - "[[LLM-Preference-Optimization-Finance]]"
  - "[[Sentiment-Strength-Logit-Extraction]]"
related:
  - "[[DEFCON-System]]"
  - "[[Analyse-Pipeline]]"
  - "[[CapEx-FLAG]]"
  - "[[ROIC-vs-WACC]]"
  - "[[Non-US-Scoring]]"
  - "[[Backtest-Methodik-Roadmap]]"
entities:
  - "[[ASML]]"
  - "[[AVGO]]"
  - "[[MSFT]]"
  - "[[RMS]]"
  - "[[VEEV]]"
  - "[[SU]]"
  - "[[BRKB]]"
  - "[[V]]"
  - "[[APH]]"
  - "[[COST]]"
  - "[[TMO]]"
datum: 2026-04-27
status: aktiv
---

# Wissenschaftliche Fundierung DEFCON v3.7

> Dieses Dokument belegt, dass das DEFCON-Scoring-System auf peer-reviewed Forschung basiert.
> 34 Quellen → 28 Befunde → operative Konsequenzen für das Dynasty-Depot.
> **Stand 2026-04-20 Abend nach Phase-1b-Ingest:** B21-B24 sind **keine Scoring-Änderungen**, sondern Architektur/Methoden-Befunde für zukünftige Skill-Erweiterungen + Validation-Pflichten.
> **Stand 2026-04-26 nach Paper-Ingest Phase A:** B25-B28 ergänzt. B25 ist `meta-gate` (§29.7 M&P-Discount angelegt 26.04.2026). B26 ist `active-scoring-validation` (Codex-Re-Klassifikation: bestätigt Insider-Block-Heuristik, kein neues Score-Element). B27 + B28 sind `design-context` (Codex-Re-Klassifikation: insider-intelligence-v2-Roadmap-Anker + Sentiment-Mean-Reversion-Architektur-Anker).
> **Stand 2026-04-27 Phase C-1:** Quellen-Übersicht-Tabelle 20 → 34 erweitert. 10 SOURCE-ONLY-Pages aus Phase A (QMJ, Mauboussin/Callahan, Amundi, FF-2015, HLZ-2016, AMP-VME, FF-2006, HXZ-q-Factor, FinGPT, 2iQ-Meta) als **nicht-Befund-Anker** integriert — sie ankern bestehende Befunde (B2, B5, B7, B8, B16, B26) wissenschaftlich, ohne eigenständigen Score-Pfad oder neue B-Befund-ID. Befund-Zähler bleibt bei 28.

---

## v3.7-Änderungsprotokoll (17.04.2026)

**3 operative Gap-Closures, wissenschaftlich validiert:**

1. **Quality-Trap-Interaktionsterm (B6)** — Deckel auf Fundamentals-Subscores statt Moat-Malus. Begründung: Applied Learning 17.04. verbietet Double-Counting. Fwd P/E und P/FCF sind bereits in Fundamentals dekomponiert — ein zusätzlicher Moat-Abzug wäre doppelte Strafe auf dieselbe Beobachtung. Lösung: bei Wide Moat + teure Bewertung wird der Fwd-P/E-/P/FCF-Subscore hart auf 0 gedeckelt. Signal-Erhalt ohne Regelverletzung.

2. **Operating Margin TTM (B8)** — neue Fundamentals-Metrik (max. 2 Pt.) operationalisiert Wolff-Echterling-2023 (ROIC + FCF + OpM als Top-Prädiktoren). Vorher war OpM nur implizit in Moat-GM-Trend enthalten, nicht als eigene Quantität.

3. **Analyst-Bias-Kalibrierung (B11)** — Crowd-Consensus >60% Strong Buy erzeugt jetzt Malus (vorher unlimitiert-positiv). Sell-Ratio dreistufig (<3% = Warnsignal, nicht Bestnote). Direkte Umsetzung von Jadhav-Mirza 2025 + llms-for-equity-stock-ratings: News-/Analyst-Daten haben strukturellen Positivity-Bias, den das Scoring aktiv korrigieren muss.

**Nicht übernommen aus v3.6:** F-Score-Bonus, GP/TA-Metrik, Accrual-Bonus — alle drei waren Double-Counting-Kandidaten. Papers B12/B13/B14 bleiben als wissenschaftliche Validation der Sub-Signale (Piotroski → Bilanz/FCF/ROIC, Novy-Marx → GM-Trend, Sloan → Accrual Ratio), aber werden nicht als Aggregat-Scores addiert.

**Fundamentals-Cap bei 50:** Block-Summe hart gedeckelt — verhindert Score-Inflation durch Bonus-Akkumulation bei Top-Namen.

---

## 28-Befunde Entscheidungsmatrix (Stand: 26.04.2026, post Phase-A-Ingest)

| # | Befund | Quelle | Block | Empfehlung | Konsequenz |
|---|--------|--------|-------|------------|------------|
| **B1** | 5J-Fenster > Spot als Rendite-Prädiktor (+2,7% CAGR) | [[arXiv-1711.04837]] | Fundamentals (50 Pt.) | 5J-Perspektive als Pflichtrahmen | 5J-Trend in jeder Analyse prüfen |
| **B2** | FCF + Gross Margin = stabilste Prädiktoren (Top-2 ML-Features) | [[Gu-Kelly-Xiu-2020]] | Fundamentals — FCF/GM | Trailing P/E de-priorisieren; forward P/E valide | P/FCF + Fwd P/E bleiben primär; trailing P/E nur Kontext |
| **B3** | Earnings-Quality > Value (Accrual Ratio top-3 Feature) | [[Gu-Kelly-Xiu-2020]] | Fundamentals — Qualität | FCF-Qualität und GM-Trend aufwerten | Bonus-Metriken Accrual Ratio + GM-Trend bestätigt |
| **B4** | 8 Moat-Quellen operativ identifiziert | [[Morningstar-Wide-Moat]] | Moat (20 Pt.) | 8-Quellen-Checkliste im Moat-Block | Jede Moat-Analyse prüft alle 8 Quellen |
| **B5** | Buffetts Alpha = QMJ + BAB + Value (vollständig erklärt) | [[Buffetts-Alpha]] | Fundamentals + Moat | cheap+safe+quality als operativer Dreiklang | DEFCON-4-Kriterien = cheap+safe+quality |
| **B6** | Moat allein ≠ Excess Return (Quality Trap ohne Bewertung) | [[Morningstar-Wide-Moat]] | Moat + Bewertung | Wide Moat immer mit Bewertungsdisziplin | Kombination Moat + Fundamentals ist Pflicht |
| **B7** | Fundamentals > Sentiment > Technicals (ML-Datenhierarchie) | Kern-Paper (arXiv, Gu, MS, AQR) | Datenhierarchie | Gewichtung 50/10/10 Pt. bestätigt | Datenhierarchie explizit in !Analysiere benennen |
| **B8** | ROIC + FCF/EV + Operating Margin = top-ranked in allen ML-Modellen | [[Wolff-Echterling-2023]] | Fundamentals — ROIC/FCF | ROIC-Malus ist wissenschaftlich zwingend, nicht heuristisch | ROIC-vs-WACC Scoring direkt belegt; Non-US-Übertragbarkeit validiert |
| **B9** | EPS-Growth + Low Leverage = stabile Quality-Prädiktoren | [[Wolff-Echterling-2023]] | Fundamentals — Bilanz | Debt/EBITDA-Scoring wissenschaftlich fundiert | EPS Revision Momentum (+1 Bonus) + Bilanz-Block (9 Pt.) bestätigt |
| **B10** | Chain-of-Thought vor Scoring verbessert Konsistenz + Genauigkeit | [[llms-for-equity-stock-ratings]] | Workflow — !Analysiere | Begründen vor Scoren als Pflichtprinzip | Befunde-Priming in INSTRUKTIONEN.md (Stufe 2) verankert |
| **B11** | News-Daten erzeugen Positivity-Bias — mittelfristig schädlich | [[llms-for-equity-stock-ratings]], [[Jadhav-Mirza-2025]] | Sentiment (10 Pt.) | Sentiment-Gewichtung deckeln; Analyst-Bias (43% Strong Buy) gegensteuern | Sentiment-Cap 10 Pt. gerechtfertigt; Sell-Ratio-Check als Korrektiv |
| **B12** | F-Score ≥7 → +7,5% p.a. Outperformance bei Value-Aktien | [[Piotroski-2000]] | Fundamentals (Quality-Bonus) | Quality als PRÄDIKTOR (nicht nur Malus); 9-Kriterien-Score operationalisieren | v3.6: F-Score ≥7 → +2 Pt. Bonus Fundamentals; ≤3 → -1 Pt. Malus |
| **B13** | GP/TA prognostiziert Returns ~gleich stark wie Book-to-Market | [[Novy-Marx-2013]] | Fundamentals (Profitability-Metrik) | Gross Profitability als eigenständiger Renditefaktor | v3.6: GP/TA als 2-Pt.-Metrik in Fundamentals-Block; GM-Trend im Moat-Block bleibt |
| **B14** | Low-Accrual-Firmen outperformen High-Accrual um +10,4% p.a. | [[Sloan-1996]] | Fundamentals (Accrual Ratio) | Accrual-Schwellen (<5%/>10%) wissenschaftlich validiert | v3.5 Malus bleibt; v3.6-Erweiterung: <3% → +2 Pt. Bonus (Piotroski-Parallele) |
| **B15** | PBO < 0,05 (CSCV) als Overfitting-Gate bei Strategy-Selection | [[Bailey-2015-PBO]] | Validation-Methode | Institutioneller Goldstandard; Pflicht bei Parameter-Tuning | §29.1 Retrospective-Analyse-Gate, Aktivierung 2028-04-01 |
| **B16** | 4 Kanon-Faktoren (Value/Momentum/Quality/Defensive); Size verworfen; t-Stat≥3 Hurdle | [[Aghassi-2023-Fact-Fiction]] | Externer Benchmark + neue Parameter | DEFCON-Faktor-Mapping explizit; aggr. Portfolio-SR im AQR-Band prüfen | §29.2 External-Bench + §29.4 t-Stat-Hurdle |
| **B17** | Faktor-Half-Life: Value 3–4M, Quality 4–5M, Momentum 3M, Investment 1M, LowVol 5–6M | [[Flint-Vermaak-2021-Decay]] | Cadence-Validation | Earnings-Trigger (~3M) wissenschaftlich fundiert; Investment-Klasse Watch | §29.3 Temporal-Konsistenz; keine System-Änderung |
| **B18** | Seven Sins of Quantitative Investing (Overfitting + 6 weitere Biases) | [[Palomar-2025-Portfolio-Optimization]] | Pre-Flight-Validation | Pflicht-Checkliste vor jeder retrospektiven Analyse; Sin #7 n.a. Long-Only | §29.5 Seven-Sins-Gate aktiv auch bei Migration-Events |
| **B19** | LLM-Investing-Vorteile verschwinden unter 20-J/100+-Symbol-Eval mit Bias-Mitigation; Bull/Bear-Asymmetrie systematisch | [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] | Validation-Audit + Regime-Awareness | Skill-Self-Audit-Pflicht für DEFCON als Selection-Strategy; Bull/Bear-Subsample-SR-Trennung | §29.5 erweitert + ggf. §33 Skill-Self-Audit; Track 5b FRED wissenschaftlich verankert |
| **B20** | Composite Anti-Overfitting Objective (Performance × Significance × Consistency × Downside-Risk) — In-the-Loop statt Post-hoc | [[Sheppert-2026-GT-Score]] | Validation-Methode (komplementär zu B15) | GT-Score-Aggregat als Tie-Break R0 in Track 5b Grid-Search (1620 Combos); Audit-Lens für DEFCON-Block-Gewichtungen | §29.1 erweitert + §29.6 Downside-Risk-Komponente |
| **B21** | Reflection-Driven Agentic KG-Extraction (Critic-Corrector-Loop) erreicht 64,8% All-Rules-Compliance aus SEC 10-K-Filings, +22,5pp vs. Single-Pass; 5-Tuple-Schema mit 10 Entity-Types + 10 Relation-Types | [[Arun-et-al-2025-FinReflectKG]] | Architektur (nicht Scoring) | Anker für Entscheidung `insider-intelligence` KG-Erweiterung: Form-4 bleibt XML, 10-K-KG bleibt FUTURE-Option | Keine §-Änderung; neue Synthesis [[Knowledge-Graph-Architektur-Roadmap]] v0.1 |
| **B22** | Reflection-Entropy-Paradox — Coverage-Gain geht einher mit Diversity-Reduktion (Shannon Rel. -22%); Praktiker-Mitigation via Pre-Correction-Entropy-Monitor | [[Labre-2025-FinReflectKG-Companion]] | Architektur-Caveat | Bei hypothetischer 10-K-KG: Entropy-Monitor als Qualitäts-Gate verpflichtend | Keine §-Änderung; dokumentiert in [[Knowledge-Graph-Architektur-Roadmap]] Gate 2 |
| **B23** | Epistemic-Uncertainty-Quantification via Monte-Carlo-Dropout auf Embeddings; Score $S_i = \mu_i - \lambda \cdot \sigma_i$; -26,8% ECE vs. BM25 bzw. -52% ECE vs. Standard RAG (Paper-Baseline-abhängig), -27,8% Halluzinationen bei 15ms Latency | [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] | Architektur (nicht Scoring) | Wissenschaftliche Fundierung für v3.0.3 Morning-Briefing Korrektheits-Prinzip (n.v.-Markierung + Soft-Alert-Schema); keine operative Änderung heute (Tavily-API erlaubt kein MC-Dropout) | Keine §-Änderung; Alignment-Referenz für `feedback_correctness_over_runtime.md` |
| **B24** | Direct-Preference-Optimization + Logit-to-Score-Konverter enables causal-LLM-Integration in Long-Short-Portfolios; +11% F1 vs. FinGPT v3.3 SOTA, 67% p.a. bei 5bps Transaction Costs | [[Iacovides-Zhou-Mandic-2025-FinDPO]] | Methoden-Kontext (nicht Dynasty-Depot-operativ) | Long-Short orthogonal zu DEFCON Long-Only; FINSABER-Audit-Pflicht (B19) vor Adoption; Future-Option für News-Sentiment-Block | Keine §-Änderung; dokumentiert als Wissenschaftskontext für zukünftige Sentiment-Revisionen |
| **B25** | Cross-Sect Predictoren −26% Out-of-Sample (statistical bias upper bound) + −58% Post-Publication (publication-effect lower bound 32pp); Decay stärker bei höheren in-sample-Returns/t-Stats | [[McLean-Pontiff-2016]] | `meta-gate` — Validation-Methode (§29.7 angelegt 26.04.2026) | M&P-Discount als 7. §29-Layer: in-sample-Result × 0.42 als Plausibility-Test post-publication | §29.7 angelegt (Phase B1-2 — INSTRUKTIONEN.md vollständig dokumentiert); Block-Gewichtung 50/20/10/10/10 strukturell robust gegen M&P-Decay-Pattern bestätigt |
| **B26** | Insider-Käufe > Insider-Verkäufe in Information; Aggregate-Predictability; Small-Cap-Concentration; Contrarian-Timing | [[Lakonishok-Lee-2001]] | `active-scoring-validation` — Insider-Block (5 Pt.) | Bestätigt Status-quo-Heuristik (Buy-Side höher gewichtet, Form-4-X/M-Filter via [[OpenInsider]]) | Keine Score-Änderung; primär-empirische Validation der seit insider-intelligence-v1 operativen Filter |
| **B27** | Insider-Verkäufe Q-9 bis Q-3 vor Earnings-Break (Legal-Jeopardy-vermeidet); Q-2/Q-1 fast Null abnormal; aktuelles 6M-Window verfehlt strukturell | [[Ke-Huddart-Petroni-2003]] | `design-context` — Insider-Block (Window-Erweiterung deferred) | Pipeline-Item: insider-intelligence v2 mit 24-Monats-Lookback gegen Performance-Backtest auf Score-Archiv | Kein Score-Element heute; erklärt scheinbare Buy>Sell-Asymmetrie aus B26 als Window-Artefakt |
| **B28** | Hohe Media-Pessimism prädiziert kurzfrist Drawdown + komplette Reversion zu Fundamentals (5-10 Tage); Volume-Pattern in Absolut-Wert (Liquidity-Trader-Modell) | [[Tetlock-2007]] | `design-context` — Sentiment-Block (10 Pt.) Architektur-Anker | Mean-Reversion-Prinzip ankert Score-Stabilität gegen Tagesnachrichten; validiert B11 Crowd-Consensus-Malus | Keine Score-Änderung; begründet Sentiment-Block-Existenz empirisch (gegen Sideshow-Hypothese) |

---

## Status-Matrix (operative Aktivierungs-Klassifikation)

> **Single Source of Truth für §4-Router (INSTRUKTIONEN.md).** Jeder Befund bekommt ein Status-Label, das mechanisch bestimmt, wann und wo er in Workflow/Scoring/Gate eingreift. Ohne Status-Klassifikation kein Phase-1-Complete bei zukünftigen Paper-Ingests (B25+).

### Legende

- **`active-scoring`** — wirkt per-Ticker im DEFCON-Scoring; Pflicht-Nennung im !Analysiere-Output pro DEFCON-Block (B1-B11 + B14-implicit)
- **`active-scoring-validation`** — primär-empirische Bestätigung eines bestehenden `active-scoring`-Elements; KEIN neuer Score-Pfad. Im !Analysiere-Output kann die Befund-ID **zusätzlich** zum bestehenden Block-Befund genannt werden (z.B. „Insider-Block: B26-validated"). Keine Migration nötig (eingeführt 26.04.2026 — Codex-Re-Klassifikation B26)
- **`design-context`** — Architektur-Anker oder Roadmap-Begründung für deferred Skill-Erweiterung; KEIN per-Ticker-Scoring, KEIN §29-Gate-Trigger, KEIN eigenständiger Score-Pfad. Im !Analysiere-Output zulässig **ausschließlich** als nicht-scorender Architektur-Anker in Klammer-Notation mit `design-context`-Suffix und Erklärtext (vgl. Insider-/Sentiment-Block-Templates in SKILL.md Schritt 3); auch in Pipeline-/Skill-Roadmap-Diskussionen referenzierbar (eingeführt 26.04.2026 — Codex-Re-Klassifikation B27, B28)
- **`meta-gate`** — feuert bei Migration (§28), Retrospective (§29) oder Skill-Self-Audit (§33); **nicht** per-Ticker
- **`design-rejected`** — bewusst NICHT integriert (§27.1 Double-Counting); Wiedereinführung nur mit formaler §27.1-Revision; Rejection-Begründung MUSS erhalten bleiben
- **`future-arch`** — Architektur-Option für zukünftige Skill-Erweiterungen; Bewertung ausschließlich via §33 Skill-Self-Audit-Gate

### Matrix

| Befund | Status | Aktivierungs-Stelle | Anmerkung |
|--------|--------|---------------------|-----------|
| B1 | `active-scoring` | Fundamentals-Block — 5J-Trendperspektive | — |
| B2 | `active-scoring` | Fundamentals-Block — FCF + GM Primärmetriken | Trailing P/E de-priorisiert |
| B3 | `active-scoring` | Fundamentals-Block — Earnings-Quality | — |
| B4 | `active-scoring` | Moat-Block — 8-Quellen-Pflichtcheck | — |
| B5 | `active-scoring` | Gesamt-Urteil — DEFCON-4-Kriterium (cheap+safe+quality) | — |
| B6 | `active-scoring` | Quality-Trap-Interaktionsterm v3.7 (Moat × Fundamentals) | Subscore-Deckel statt additiver Malus |
| B7 | `active-scoring` | Block-Gewichtung 50/20/10/10/10 | Pflicht-Nennung in !Analysiere |
| B8 | `active-scoring` | Fundamentals-Block — ROIC-vs-WACC + OpM TTM | v3.7 OpM als eigene Metrik |
| B9 | `active-scoring` | Fundamentals-Block — Bilanz + EPS Revision | — |
| B10 | `active-scoring` | Workflow — Reasoning vor Score | Implementiert via §4 Router + §2 Befunde-Check |
| B11 | `active-scoring` | Sentiment-Block — Cap 10 Pt. + Analyst-Bias-Kalibrierung | v3.7 Crowd-Consensus-Malus |
| B12 | `design-rejected` | — | F-Score-Komponenten (ROIC/FCF/Leverage) bereits dekomponiert → §27.1 Double-Counting. Rejection-Datum: 17.04.2026 (v3.6→v3.7). |
| B13 | `design-rejected` | — | GM-Trend im Moat-Block + OpM TTM → §27.1 Double-Counting. Rejection-Datum: 17.04.2026 (v3.6→v3.7). |
| B14 | `active-scoring` (implicit) | Fundamentals-Block — Accruals-Ratio Earnings-Quality-Pfad | B14-Bonus (+2 Pt. <3%) rejected § 27.1, aber Accruals-Ratio-Malus bleibt aus v3.5-Erbe aktiv |
| B15 | `meta-gate` | §29.1 Methoden-Gate — PBO/CSCV | Aktivierung 2028-04-01 oder erste Parameter-Variation |
| B16 | `meta-gate` | §29.2 External-Benchmark + §29.4 t-Hurdle | §29.4 SOFORT aktiv (nicht 2028) |
| B17 | `meta-gate` | §29.3 Temporal-Konsistenz — Half-Life × Cadence | — |
| B18 | `meta-gate` | §29.5 Seven-Sins Pre-Flight | SOFORT aktiv bei Migration-Events |
| B19 | `meta-gate` | §29.5 + §33 Skill-Self-Audit | Regime-Awareness, Bull/Bear-Asymmetrie |
| B20 | `meta-gate` | §29.1 + §29.6 — In-the-Loop-Objective + Downside-Risk | — |
| B21 | `future-arch` | [[Knowledge-Graph-Architektur-Roadmap]] Szenario 2 | 10-K-KG frühestens 2027+ |
| B22 | `future-arch` | [[Knowledge-Graph-Architektur-Roadmap]] Gate 2 | Entropy-Monitor bei hypothetischer 10-K-KG |
| B23 | `future-arch` | [[Knowledge-Graph-Architektur-Roadmap]] Szenario 3 | Tavily-API erlaubt kein MC-Dropout; Alignment-Anker für `feedback_correctness_over_runtime.md` |
| B24 | `future-arch` | [[Knowledge-Graph-Architektur-Roadmap]] Szenario 3-Erweiterung | Long-Short orthogonal zu DEFCON Long-Only |
| B25 | `meta-gate` | §29.7 (angelegt 26.04.2026) — M&P-Discount-Layer (in-sample × 0.42) | Phase B1-2: §29.7 in INSTRUKTIONEN.md angelegt (vollständig dokumentiert) |
| B26 | `active-scoring-validation` | Insider-Block (5 Pt.) — bestätigt Buy>Sell + Form-4-X/M-Filter via [[OpenInsider]] | Codex-WARN re-klassifiziert (Page-Body: „kein neues Scoring-Element, primär-empirische Validation") |
| B27 | `design-context` | insider-intelligence v2 Pipeline (24-Monats-Sell-Window für Pre-Earnings-Break-Detection) | Codex-WARN re-klassifiziert (Page-Body: „Kein Live-Score-Change bis insider-intelligence v2 deployed"); deferred bis §29-Backtest-Gate-Kriterien erfüllt |
| B28 | `design-context` | Sentiment-Block (10 Pt.) — Architektur-Anker für Mean-Reversion-Score-Stabilität + B11-Crowd-Consensus-Validation | Codex-WARN re-klassifiziert (Page-Body: „B28 deaktiviert KEINEN bestehenden Score-Pfad"); ankert die Anti-Tagesnachrichten-Architektur |

### Aktivierungs-Regeln (bindend)

1. **`active-scoring`:** Pflicht-Nennung im !Analysiere-Output pro DEFCON-Block (SKILL.md-Output-Template). Neue active-scoring-Befunde nur über §28.1 Migration-Workflow einführbar (inkl. §29.4 t≥3 Hurdle).
2. **`active-scoring-validation`:** Optional-Nennung im !Analysiere-Output als Validation-Suffix zur bestehenden Block-Begründung. Keine Migration, kein Score-Effekt. Wenn die Validation einen impliziten Score-Pfad würdigt, der noch nicht expliziert ist (Beispiel: B26 würdigt Form-4-X/M-Filter), darf die Page-Begründung im Block-Text referenziert werden.
3. **`design-context`:** **Nicht als Score-relevante Befund-ID** und **kein eigenständiger Score-Pfad** — verändert keinen Block-Score, keinen Subscore, kein Gate-Verhalten. Im !Analysiere-Output **zulässig als nicht-scorender Architektur-Anker** in Klammer-Notation mit `design-context`-Suffix + Erklärtext (vgl. Insider-Template `[+ B27 Ke/Huddart/Petroni \`design-context\`: 24-Monats-Window deferred]` und Sentiment-Template `[+ B28 Tetlock \`design-context\`: Mean-Reversion-Architektur-Anker (kein Score-Update durch Tagesnachrichten)]` in SKILL.md Schritt 3). Außerhalb des Outputs auch in Skill-Roadmap-Diskussionen, Konsolidierungstag-Reviews, Phase-B/C-Wiki-Synthesis-Updates, INSTRUKTIONEN-Pipeline-Notes referenzierbar. Wenn ein `design-context`-Befund später in `active-scoring` migriert werden soll: §28.1 Migration-Workflow Pflicht (inkl. §29.4 t≥3 Hurdle + ggf. §29.7 M&P-Discount-Plausibility-Check).
4. **`meta-gate`:** Aktiv nur bei den in "Aktivierungs-Stelle" genannten §§. Kein Zugriff aus per-Ticker-!Analysiere. Wenn Migration ansteht: §28.1 Step 1 (Paper/Evidence-Check) verweist auf diese Matrix.
5. **`design-rejected`:** Wiederaufnahme NUR nach formaler Überarbeitung von §27.1 Double-Counting-Definition. Wenn in !Analysiere die Frage auftaucht "warum fehlt F-Score/GP/TA?" → Antwort aus Rejection-Begründung zitieren, nicht ad-hoc einführen.
6. **`future-arch`:** Bewertung ausschließlich via §33 Skill-Self-Audit-Gate (3 Qualitäts-Gates aus [[Knowledge-Graph-Architektur-Roadmap]]). Keine stille Adoption in bestehende Skills.

### Regel für neue Befunde (B25+)

Jeder zukünftige Befund MUSS bei Ingest in diese Matrix eingetragen werden mit Status-Label + Aktivierungs-Stelle + Begründung. Status-Klassifikation ist Teil von Phase-1-Complete (Codex-Gate 2).

---

## PFLICHT-Regeln (wörtlich, session-übergreifend)

### Aus Gu/Kelly/Xiu (2020):
> **"Trailing P/E verliert Vorhersagekraft — forward P/E bleibt valide."**
> Gilt in jeder DEFCON-Analyse. Fwd P/E ist Primärmetrik; trailing P/E höchstens als Kontext.

### Aus Buffetts Alpha (AQR 2018):
> **"Float-Leverage (~1,6x) nicht replizierbar. Übertragbar: nur cheap + safe + high-quality."**
> Gilt bei jeder BRK.B-Analyse und bei Leverage-Diskussionen.

---

## Quellen-Übersicht (34 Paper — Stand: 27.04.2026 — Phase A + C-1)

| Quelle | Jahr | Kernthese | DEFCON-Block | Neue Befunde |
|--------|------|-----------|--------------|-------------|
| [[arXiv-1711.04837]] | 2019 | ML + 5J-Fenster → +2,7% CAGR | Fundamentals 50% | B1, B7 |
| [[Gu-Kelly-Xiu-2020]] | 2020 | FCF+GM primär; trailing P/E schwach | Faktor-Kalibrierung | B2, B3, B7 |
| [[Morningstar-Wide-Moat]] | 2023 | 8 Moat-Quellen; Moat+Fundamentals nötig | Moat 20% | B4, B6 |
| [[Buffetts-Alpha]] | 2018 | QMJ+BAB+Value; Float nicht replizierbar | Fundamentals+Moat+BRK.B | B5 |
| [[Wolff-Echterling-2023]] | 2023 | ROIC+FCF top-ranked; STOXX-robust | Fundamentals ROIC/Bilanz | B8, B9 |
| [[llms-for-equity-stock-ratings]] | 2024 | Fundamentals > News; CoT verbessert Genauigkeit | Workflow + Sentiment | B10, B11 |
| [[Jadhav-Mirza-2025]] | 2025 | 84-Paper-Survey; News-Bias; RL+Memory | Sentiment + Architektur | B11 (Bestätigung) |
| [[Piotroski-2000]] | 2000 | F-Score ≥7 → +7,5% p.a. bei Value-Aktien | Fundamentals (Quality-Bonus) | B12 ← NEU |
| [[Novy-Marx-2013]] | 2013 | Gross Profitability = 2. Seite des Value-Faktors | Fundamentals (GP/TA) | B13 ← NEU |
| [[Sloan-1996]] | 1996 | Accruals-Anomalie: +10,4% p.a. Low-Accrual-Premium | Fundamentals (Accrual Ratio) | B14 ← NEU |
| [[Bailey-2015-PBO]] | 2015 | PBO/CSCV als Overfitting-Gate bei Strategy-Selection | Validation-Methode | B15 ← NEU |
| [[Aghassi-2023-Fact-Fiction]] | 2023 | 4 Kanon-Faktoren validiert; Size verworfen; t-Stat≥3 | Externer Benchmark + neue Parameter | B16 ← NEU |
| [[Flint-Vermaak-2021-Decay]] | 2021 | Faktor-Half-Life → optimale Rebalance-Cadence | Cadence-Validation | B17 ← NEU |
| [[Palomar-2025-Portfolio-Optimization]] | 2025 | Seven Sins of Quantitative Investing | Pre-Flight-Validation | B18 ← NEU |
| [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] | 2026 | LLM-Investing-Vorteile verschwinden unter realistischer Eval; Bull/Bear-Asymmetrie | Validation-Audit + Regime-Awareness | B19 ← NEU 2026-04-20 |
| [[Sheppert-2026-GT-Score]] | 2026 | Composite Anti-Overfitting Objective (in-the-loop) | Validation-Methode | B20 ← NEU 2026-04-20 |
| [[Arun-et-al-2025-FinReflectKG]] | 2025 | Agentic Reflection-Pattern für Finance-KG-Extraction aus SEC 10-K | Architektur (nicht Scoring) | B21 ← NEU 2026-04-20 Phase 1b |
| [[Labre-2025-FinReflectKG-Companion]] | 2025 | Praktiker-Lens + Entropy-Paradox-Mitigation für Reflection-KG | Architektur-Caveat | B22 ← NEU 2026-04-20 Phase 1b |
| [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] | 2026 | Bayesian RAG mit MC-Dropout-Uncertainty für Finance-QA | Architektur-Referenz | B23 ← NEU 2026-04-20 Phase 1b |
| [[Iacovides-Zhou-Mandic-2025-FinDPO]] | 2025 | DPO-Alignment + Logit-to-Score für Long-Short-Portfolios | Methoden-Kontext (nicht operativ) | B24 ← NEU 2026-04-20 Phase 1b |
| [[McLean-Pontiff-2016]] | 2016 | Cross-Sect Predictoren −26% Out-of-Sample (statistical bias upper bound) + −58% Post-Publication (operativer Total-Decline; davon ≈32pp publication-effect lower bound) | Validation-Methode (§29.7 M&P-Discount) | B25 ← NEU 2026-04-26 Phase A |
| [[Lakonishok-Lee-2001]] | 2001 | Insider-Käufe informativer als -Verkäufe; Aggregate-Predictability + Small-Cap-Concentration + Contrarian-Timing | Insider-Block (5 Pt.) Validation | B26 ← NEU 2026-04-26 Phase A |
| [[Ke-Huddart-Petroni-2003]] | 2003 | Insider-Verkäufe Q-9 bis Q-3 vor Earnings-Break (Legal-Jeopardy-Window); Q-2/Q-1 ≈ Null abnormal | Insider-Block — Architektur-Anker (insider-intelligence v2 deferred) | B27 ← NEU 2026-04-26 Phase A |
| [[Tetlock-2007]] | 2007 | Hohe Media-Pessimism prädiziert kurzfrist Drawdown + komplette Reversion zu Fundamentals (5-10 Tage) | Sentiment-Block — Mean-Reversion-Architektur-Anker | B28 ← NEU 2026-04-26 Phase A |
| [[Asness-Frazzini-Pedersen-2013-QMJ]] | 2013 | QMJ Long-Short, 4-Pillars-Quality-Definition (Profitability/Growth/Safety/Payout); 23/24 Länder positives Alpha | Fundamentals + Moat (Sprachregel + Buffett-Faktorlogik-Anker) | SOURCE-ONLY (anchors B5) ← NEU 2026-04-26 Phase A |
| [[Mauboussin-Callahan-2024-Measuring-Moat]] | 2024 | Competitive Advantage Period (CAP) als zweite Moat-Dimension neben ROIC-WACC-Spread (Magnitude × Sustainability) | Moat-Block (Sprachregel + Tiefen-Analyse) | SOURCE-ONLY (anchors B4, B6) ← NEU 2026-04-26 Phase A |
| [[Amundi-Quality-2021]] | 2021 | Practitioner-Validation 4-Pillars (Profit/Earnings-Quality/Safety/Investment); +2,8% p.a. IR 0,81 post-GFC | Fundamentals (Quality-Faktor-Validation) | SOURCE-ONLY (anchors B5, B8) ← NEU 2026-04-26 Phase A |
| [[Fama-French-2015-Five-Factor]] | 2015 | RMW + CMA Faktoren; HML wird redundant für Cross-Section-Erklärung | Fundamentals (Profitability + Investment-Anker) | SOURCE-ONLY (anchors B2, B8) ← NEU 2026-04-26 Phase A |
| [[Harvey-Liu-Zhu-2016]] | 2016 | t≥3-Hurdle für Faktor-Discovery (Multiple-Testing-Korrektur über 313 Studien) | Validation-Methode (§29.4 t-Stat-Hurdle Anker) | SOURCE-ONLY (anchors B16) ← NEU 2026-04-26 Phase A |
| [[Asness-Moskowitz-Pedersen-2013-VME]] | 2013 | Value + Momentum global, persistent, neg. korreliert über 8 Asset-Klassen | Block-Gewichtung 50/20/10/10/10 Validation | SOURCE-ONLY (anchors B7) ← NEU 2026-04-26 Phase A |
| [[Fama-French-2006-Profitability]] | 2006 | Valuation-Equation: B/M, Profitability, Investment prädizieren Cross-Section-Returns; Sloan-Accruals schrumpft mit Profit/Invest-Kontrollen | Fundamentals (Theorie-Anker FF-5-Vorgänger) | SOURCE-ONLY (anchors B2, B8) ← NEU 2026-04-26 Phase A |
| [[Hou-Xue-Zhang-2015-q-Factor]] | 2015 | q-Theory-Faktor-Modell (Mkt+ME+I/A+ROE) — konvergente Evidenz zu FF-5 aus zweiter, theoretisch unabhängiger Methodologie | Fundamentals (Profitability + Investment-Validation) | SOURCE-ONLY (anchors B2, B8) ← NEU 2026-04-26 Phase A |
| [[Yang-Liu-Wang-2023-FinGPT]] | 2023 | Open-Source 5-Layer-Framework für Finance-LLMs (Data Source / Engineering / LLMs / Tasks / Applications); LoRA-Fine-Tuning | Architektur-Kontext (DEFCON-orthogonal Long-Only) | SOURCE-ONLY (komplementär B19, B24) ← NEU 2026-04-26 Phase A |
| [[2iQ-Insider-Meta-Review-2021]] | 2021 | Industry-Meta-Review Insider-Trading 1968-2018 (Lorie/Niederhoffer/Seyhun/L&L/JMZ/Dardas/Alldredge/Kang) | Insider-Block (insider-intelligence-Skill-Begründung) | SOURCE-ONLY (industry-meta — anchors B26, B27) ← NEU 2026-04-26 Phase A |

---

## Betroffene Entitäten

### Aktive Satelliten (v3.5-Zeitstand: 16.04.2026 — dient B1-B11 Mapping)

> ⚠️ **Scores sind v3.5-Zeitstand (16.04.)** — nicht Live-Portfolio-State. Aktuelle v3.7-Scores: siehe `00_Core/PORTFOLIO.md` (Live-State-SSoT, seit Tier-2-Refactor 25.04.2026; vorher `STATE.md`). Tabelle dient dem Mapping der wissenschaftlichen Befunde (B1-B11) auf Satelliten-Charakteristika, keine Scoring-Aussage.

| Ticker | DEFCON | Score | FLAG | Relevante Befunde |
|--------|--------|-------|------|------------------|
| [[ASML]] | 🟡 3 | 68 | — | B1 (5J-EUV-Ramp), B4 (EUV-Monopol 100%), B6 (Fwd P/E 38x = Quality Trap ohne Bewertungsmarge), B8 (ROIC clean, Non-US-Übertragbarkeit) |
| [[AVGO]] | 🟢 4 | 85 | ⚠️ Insider-Check | B2 (FCF <15% CapEx = Fabless-Referenz), B4 (Chip+SW-Ökosystem Wide Moat), B5 (cheap+safe+quality erfüllt), B8 (ROIC >WACC +10% — Kalibrierungsanker) |
| [[MSFT]] | 🟠 2 | 60 | 🔴 CapEx >60% | B2 (CapEx/OCF 83,6% destroys FCF-Qualität), B3 (Finance-Lease-Bereinigung = Accrual-Komplexität), B6 (Score 60 bei Wide Moat 19/20 = Quality Trap aktiv), B8 (ROIC 7,5% < WACC 13,35% — wissenschaftlich nicht tragbar) |
| [[RMS]] | 🟢 4 | 69 | ✅ Clean | B4 (Marken-Moat: Hermès = 8/8 Moat-Quellen), B6 (Score 69 trotz ROIC 24% wegen Bewertung), B5 (safe: Netto-Cash +€9,89B) |
| [[VEEV]] | 🟢 4 | 74 | ✅ Clean | B2 (FCF-SaaS-Modell, CapEx-arm), B4 (Switching Costs Life-Sciences-Plattform), B3 (Earnings Quality hoch) |
| [[SU]] | 🟢 4 | 71 | ✅ Clean | B4 (Regulatory Moat Energie-Infrastruktur), B5 (safe-Komponente: ROIC 10,48% > WACC 8,96%), B8 (Profitability-Faktoren konsistent positiv) |
| [[BRKB]] | 🟢 4 | 75 | ✅ Clean | B5 vollständig (Float $686B = nicht replizierbar, aber cheap+safe+quality erfüllt), B9 (Low Leverage: Netto-Cash), B4 (Efficient Scale BNSF, Float-Moat) |
| [[V]] | 🟢 4 | 86 | ✅ Clean | B4 (Network Effects: 4,9 Mrd. Karten, Duopol), B2 (CapEx/OCF ~6% = Fabless-Niveau), B5 (cheap+safe+quality — Kalibrierungsanker #2), B8 (ROIC ~9,9%, Goodwill-Verzerrung durch Visa Europe) |
| [[APH]] | 🟡 3 | 61 | 🔴 Score-basiert | B2 (FCF-Marginen ok, aber Bewertung + CN/MY-Risk), B3 (Accrual-Komplexität Supply-Chain), B9 (Financial Leverage mittel) |
| [[COST]] | 🟢 4 | 69 | ✅ Clean | B4 (Cost Advantage: Membership-Loyalität 8/8 Moat-Quellen), B6 (GM 12,7% ≠ Qualitätsproblem — Geschäftsmodell), B9 (Low Leverage <1x) |
| [[TMO]] | 🟠 2 | 62 | — | B2 (FCF -13,4% YoY — Erosion), B3 (ROIC 2,6% unter WACC = negative Earnings Quality), B4 (Switching Costs Life-Sciences intakt), B8 (Goodwill $49,4B drückt ROIC unter Kapitalkosten) — ⚠️ v3.5: RS -7,82% = 0/3 → Score 62, D3→D2 |

---

## Implikationen für SKILL.md

B7 verlangt explizite Dokumentation der Datenhierarchie in SKILL.md:
```
Datenhierarchie (wissenschaftlich belegt):
1. Fundamentals (FCF, ROIC, GM, Fwd P/E) — stärkste Prädiktoren
2. Earnings Quality (Accrual Ratio, FCF-Trend, GM-Trend)
3. Moat (Wide/Narrow/None — Morningstar)
4. Sentiment (Analyst-Ratings, Price Targets)
5. Technicals (Kurs-Momentum, MA-Lage)
```

---

## Konzept-Karte (aktualisiert)

```
arXiv-1711.04837 ──────► [[5J-Fundamental-Fenster]] ──► alle 11 Ticker
Gu-Kelly-Xiu-2020 ─────► [[FCF-Primacy]] ─────────────► alle 11 Ticker
Morningstar-Wide-Moat ─► [[Moat-Taxonomie-Morningstar]] ► alle 11 Ticker
Buffetts-Alpha ─────────► [[Buffett-Faktorlogik]] ──────► [[BRKB]]
                └──────► [[QMJ-Faktor]] ────────────────► [[BRKB]]
Wolff-Echterling-2023 ──► B8 (ROIC-Dominanz) ──────────► [[ROIC-vs-WACC]]
                └──────► B9 (Quality-Stabilität) ───────► Bilanz-Block
                └──────► STOXX-Robustheit ──────────────► [[Non-US-Scoring]]
llms-for-equity-stock-ratings ► B10 (CoT) ──────────────► [[Analyse-Pipeline]] / INSTRUKTIONEN
                └──────► B11 (News-Bias) ───────────────► Sentiment-Block Cap
Jadhav-Mirza-2025 ─────► B11 (Bestätigung) ────────────► Sentiment-Block Cap
Piotroski-2000 ────────► [[F-Score-Quality-Signal]] ────► Fundamentals Quality-Bonus (B12)
Novy-Marx-2013 ────────► [[Gross-Profitability-Premium]] ► Fundamentals GP/TA-Metrik (B13)
Sloan-1996 ────────────► [[Accruals-Anomalie-Sloan]] ────► Fundamentals Accrual Ratio (B14)
```

## Scoring-System-Audit v3.4 → v3.5 (16.04.2026)

**Auslöser:** PT-Upside-Duplikation entdeckt bei Backtest-Ready-Infrastruktur-Planung.
**Maßstab:** Pragmatisch (nur nachweislich verzerrende Fehler als B).

| # | Frage | Klasse | Fazit |
|---|-------|--------|-------|
| 1 | PT-Upside-Duplikation | **B** | Gleiche Rohdaten in Technicals (>20%, 3P) + Sentiment (>15%, 3P) → Fix: Technicals-Metrik ersetzt durch Relative Stärke vs. S&P500 |
| 2 | Weitere Naming-Kollisionen | A | Keine über PT-Upside hinaus |
| 3 | Redundanzen (Fwd P/E↔P/FCF, CapEx/OCF↔FCF Yield, Bilanz-Triade) | A | Verschiedene Konzepte, pragmatisch akzeptiert |
| 4 | Block-Gewichtung vs. Paper | **C** | Moat=20 strategisch korrekt. Sentiment/Technicals-Rebalancing → Evaluation nach 6 Monaten |
| 5 | Kategorien-Hygiene | A | Korrekt (außer PT-Upside) |
| 6 | Malus-Stacking | A | Floor-Klausel (min 0) hinzugefügt |
| 7 | Anker-Reproduzierbarkeit | A | ±5–7 Punkte systemtypisch |

**Implikation für B7 (Fundamentals > Sentiment > Technicals):** Die Bereinigung stärkt B7 — Technicals enthält jetzt ausschließlich preisbasierte Metriken (ATH-Distanz, Relative Stärke, 200MA), Sentiment ausschließlich Analysten-Meinungen (Konsensus, Sell-Ratio, PT vs Kurs). Konzeptuelle Trennung ist sauberer als in v3.4.

---

## Änderungsprotokoll

| Datum | Änderung |
|-------|---------|
| 2026-04-14 | Erstellt — 4 Paper, 7 Befunde, vollständige Backlink-Vernetzung |
| 2026-04-16 | Erweitert — 3 neue Paper (Wolff/Echterling, Jadhav/Mirza, JPM vollständig eingebunden), 4 neue Befunde B8–B11, alle 11 Satelliten-Scores aktualisiert, Konzept-Karte erweitert |
| 2026-04-16 | v3.4→v3.5 Audit — PT-Upside-Fix, Relative Stärke promoted, Floor-Klausel. 7-Fragen-Audit: 5×A, 1×B, 1×C |
| 2026-04-17 | 3 Foundation-Papers integriert: Piotroski (F-Score, B12), Novy-Marx (GP-Premium, B13), Sloan (Accrual-Anomalie, B14). 7→10 Quellen, 11→14 Befunde. Vorbereitung für v3.6-Release: Quality-Bonus (+2 Pt.) + GP/TA-Metrik (2 Pt.) + Accrual-Bonus <3%. System-Reife-Ceiling: 85% → geplant 92-95%. |
| 2026-04-19 | 4 Backtest-Validation-Papers integriert: Bailey PBO/CSCV (B15), Aghassi AQR Fact/Fiction (B16), Flint/Vermaak Information Decay (B17), Palomar Seven Sins (B18). 10→14 Quellen, 14→18 Befunde. B15-B18 sind **keine Scoring-Änderungen**, sondern Validation-Gate-Framework — §29 (Retrospective-Analyse-Gate, FUTURE-ACTIVATION 2028-04-01). §29.5 Seven-Sins-Gate aktiv auch bei Migration-Events. Applied Learning verletzt NICHT — Paper-Ingest ≠ System-Update, nur Gate-Infrastruktur. |
| 2026-04-20 | **Phase 1a** des 6-Paper-Ingest-Projekts (siehe log.md): 2 Severity-🔴-Papers integriert — FINSABER (B19, Li/Kim/Cucuringu/Ma KDD '26) + GT-Score (B20, Sheppert JRFM 2026). 14→16 Quellen, 18→20 Befunde. B19+B20 sind **keine Scoring-Änderungen**, sondern: (1) Audit-Pflicht für DEFCON als Selection-Strategy via FINSABER-Pattern (§29.5 erweitert + ggf. neue §33 Skill-Self-Audit); (2) Composite-Anti-Overfitting-Lens für DEFCON-Block-Gewichtungen + Track 5b Grid-Search (§29.1 + §29.6 erweitert). Codex-Round-2-bestätigt: keine LLM-Sicherheitsdebatte, keine zwingenden Skill-Code-Changes. Phase 1b (4 Severity-🟡-Papers) folgt nächste Session. |
| 2026-04-20 Abend | **Phase 1b** des 6-Paper-Ingest-Projekts: 4 Severity-🟡-Papers integriert — FinReflectKG (B21, Arun et al. Domyn 2025) + Labre-Companion (B22, Towards AI 2025) + Bayesian RAG (B23, Ngartera et al. Frontiers 2026) + FinDPO (B24, Iacovides et al. Imperial 2025). 16→20 Quellen, 20→24 Befunde. B21-B24 sind **keine Scoring-Änderungen**, sondern: (1) Architektur-Referenzen für zukünftige KG/RAG-Skill-Erweiterungen (neue Synthesis [[Knowledge-Graph-Architektur-Roadmap]] v0.1 mit Entscheidungsvorlage Gate 1-3); (2) wissenschaftliche Fundierung des v3.0.3 Morning-Briefing Korrektheits-Prinzips; (3) Methoden-Kontext für Future-News-Sentiment-Integration. **Vault-only-Phase** — DEFCON v3.7 unverändert, 11 Satelliten-Scores unverändert, Sparraten unverändert. Hard-Checkpoint vor Phase 2 (System-Konsequenzen) eingehalten. |
| 2026-04-26 | **Paper-Ingest Phase A** Phase-B1: 4 neue Befunde B25-B28 in Status-Matrix + Entscheidungsmatrix integriert. **Codex-Re-Klassifikation übernommen** (Page-Tags `active-scoring` widersprachen Page-Body): B25 = `meta-gate` (§29.7 M&P-Discount in B1-2 in INSTRUKTIONEN.md angelegt 26.04.2026), B26 = `active-scoring-validation` (NEUES Status-Label — Insider-Block-Heuristik primär-empirisch bestätigt, kein neues Score-Element), B27 = `design-context` (NEUES Status-Label — insider-intelligence-v2-Window-Erweiterung deferred), B28 = `design-context` (Sentiment-Block Mean-Reversion-Architektur-Anker). 20 Quellen → 28 Befunde. **Vault-only-Phase** — DEFCON v3.7 unverändert, Scores unverändert. Quellen-Übersicht-Tabelle (20→34 inkl. 10 SOURCE-ONLY-Pages aus Phase A) erfolgt in Phase C-1. |
| 2026-04-27 | **Paper-Ingest Phase C-1**: Quellen-Übersicht-Tabelle 20 → 34 Zeilen erweitert. 14 neue Zeilen integriert: B25-B28 (McLean-Pontiff, Lakonishok-Lee, Ke-Huddart-Petroni, Tetlock) mit voller B-Befund-ID + DEFCON-Block-Mapping; 10 SOURCE-ONLY (Asness/Frazzini/Pedersen QMJ, Mauboussin/Callahan, Amundi-Quality, Fama/French 2015 Five-Factor, Harvey/Liu/Zhu 2016, Asness/Moskowitz/Pedersen VME, Fama/French 2006, Hou/Xue/Zhang q-Factor, Yang/Liu/Wang FinGPT, 2iQ-Insider-Meta) als nicht-Befund-Anker mit `SOURCE-ONLY (anchors BX)`-Notation in Spalte 5. Header-Counter 20 → 34 Quellen aktualisiert (Befund-Zähler 28 unverändert — SOURCE-ONLY-Pages erzeugen keine neuen B-IDs). Frontmatter-`sources:`-Array um 10 Einträge erweitert. McLean-Pontiff-Eintrag verwendet konsistent **58% operativer Total-Decline** (cde7fa9 / c847dba) statt 32pp publication-effect lower bound (Vermeidung Discount-Verschmelzung — Hauptrisiko Phase C). DEFCON v3.7 unverändert, Scores unverändert. |

## Validierung der Befunde (Backtest-Ready-Infrastructure, seit 2026-04-17)

Die 28 Befunde sind heute **nicht formal validiert** — das Scoring-System ist wissenschaftlich fundiert (peer-reviewed Papers) und hart kalibriert (AVGO/MKL/SNPS als Anker), aber statistische Forward-Return-Validation scheitert an Sample-Size (11 Satelliten × ~2 Jahre Historie, sparse FLAG-Events).

**Lösung:** Nicht heute validieren, sondern Infrastruktur bauen, die 2028+ **überhaupt Validierung ermöglicht**. Ab 17.04.2026 wird jeder Score + jedes FLAG-Event unveränderlich in `05_Archiv/*.jsonl` archiviert.

**Entscheidungs-Roadmap 2028-04-01:** Abhängig von Datenlage wird eine von 4 Methoden angewendet — siehe [[Backtest-Methodik-Roadmap]]:
- **Option A** (Return-Prediction): validiert B1-B3 via Forward-Return-Quantile
- **Option B** (Wide-Moat-Prämie): validiert B5, B9-B11 via Alpha vs. S&P500
- **Option C** (Threshold-Kalibrierung): validiert B4 via DEFCON-Cutpoint-Optimum
- **Option D** (FLAG-Event-Study): validiert B2-B3 via Forward-Drift nach Trigger

**Explizit NICHT validiert:** B12-B14 (Piotroski, Novy-Marx, Sloan) — v3.6-Integration wurde 17.04.2026 verworfen (Double-Counting-Falle, Applied Learning). Die Befunde bleiben als Forschungskontext, aber sind **nicht Teil des operativen Scorings**.

Infrastruktur-Details: [[Backtest-Ready-Infrastructure]], [[Score-Archiv]], [[FLAG-Event-Log]].

---

## 4-Dimensionen-Validation-Gate (§29, seit 2026-04-19, erweitert 2026-04-20 + 2026-04-26)

B15-B20 + B25 bilden zusammen das **formelle Gate-Framework** für jede zukünftige retrospektive Analyse. Keine Scoring-Änderung — Gate-Infrastruktur oberhalb der Options A–D:

| Dimension | Anker-Befund | Operative §-Komponente |
|---|---|---|
| Methode (Overfitting, post-hoc) | B15 Bailey | §29.1 PBO < 0,05 via CSCV |
| Methode (Overfitting, in-the-loop) | **B20 Sheppert** | **§29.1 erweitert um GT-Score-Composite (Tie-Break R0 für Optimization-Loops)** |
| Raum (External Bench) | B16 Aghassi | §29.2 AQR/Ilmanen-Band-Check + §29.4 t-Stat-Hurdle |
| Zeit (Temporal Decay) | B17 Flint/Vermaak | §29.3 Cadence-Konsistenz |
| Sünden (Pre-Flight) | B18 Palomar | §29.5 Seven-Sins-Gate (Sin #7 n.a.) |
| **Sünden (Selection-Strategy-Audit)** | **B19 FINSABER** | **§29.5 erweitert um Bias-Audit (Reject-Set, Iteration-Count, Bull/Bear-Subsample) + ggf. §33 Skill-Self-Audit** |
| Portfolio-Metriken | — + B20 Downside-Comp. | §29.6 risk-metrics-calculation (Palomar Ch. 6 Formeln + GT-Score Downside-Komponente) |
| **Publikation (Post-Publication-Decay)** | **B25 McLean/Pontiff** | **§29.7 M&P-Discount: in-sample-Claim × 0,42 als Plausibility-Test (angelegt 26.04.2026); externe Paper-Outperformance vor Adoption diskontieren; eigenes Score-Archiv post-publication-Sample → kein zusätzlicher Discount** |

Aktivierungs-Trigger: **Review 2028-04-01** oder erste DEFCON-Parameter-Variation. §29.5 Seven-Sins-Gate greift **bereits jetzt** bei Migration-Events. §29.7 M&P-Discount greift **bereits jetzt** bei Briefing-Sprache und §28.1 Migration-Workflow Step 1 (externe Paper-Claim-Validation). **B19/B20-Mapping ist Phase-2-Konsequenz aus 2026-04-20-Ingest**; B25-Mapping ist Phase-A-Konsequenz aus 2026-04-26 — INSTRUKTIONEN §29.7 vollständig dokumentiert.

**§30 Live-Monitoring (seit 2026-04-19, R1 Paper-Integration Phase 4):** Operative Konsequenz aus Flint-Vermaak 2021 Investment-Faktor-Half-Life ~1M. Monthly-Refresh-Pflicht für **aktive Investment-FLAGs** (Scope: MSFT CapEx/OCF 83.6%). Keine Scoring-Änderung — nur Monitoring-Cadence. TMO fcf_trend_neg bleibt Schema-Watch (nicht-aktiviert). Details: INSTRUKTIONEN §30.

Siehe [[Backtest-Methodik-Roadmap]] v2.0 für Detail-Logik der 4-Dim-Gate-Aktivierung.
