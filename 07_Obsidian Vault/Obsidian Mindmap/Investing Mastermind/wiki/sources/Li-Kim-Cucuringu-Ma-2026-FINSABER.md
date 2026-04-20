---
title: "Can LLM-based Financial Investing Strategies Outperform the Market in Long Run? (FINSABER)"
date: 2026
type: source
subtype: academic-paper
tags: [llm-investing, backtest, bias-mitigation, survivorship, look-ahead, data-snooping, regime, validation-gate]
url: https://arxiv.org/abs/2505.07078
github: https://github.com/waylonli/FINSABER
venue: "ACM SIGKDD '26 Conference on Knowledge Discovery and Data Mining (Jeju Island, Aug 2026)"
authors: "Weixian Waylon Li (Edinburgh AIAI), Hyeonjun Kim (Sungkyunkwan), Mihai Cucuringu (UCLA Math/Stats + Oxford OMI), Tiejun Ma (Edinburgh AIAI)"
status: processed
defcon_relevanz: "Validation-Gate-Verschärfung §29.2 + §29.5. Empirisch belegte Bias-Quellen (Survivorship, Look-Ahead, Data-Snooping) im LLM-Investing-Kontext. Regime-Asymmetrie (Bull-Underperform, Bear-Overshoot) zwingt zur expliziten Audit-Pflicht für jede LLM-/Selection-Strategie. DEFCON ist regelbasiert, NICHT LLM-Inferenz — aber als Composite-Selection-Output bias-anfällig und damit auditierbar mit FINSABER-Pattern. Konsequenz: Phase 2 §33 Skill-Self-Audit-Kandidat (siehe Codex Round 2)."
related: "[[LLM-Investing-Bias-Audit]], [[Regime-Aware-LLM-Failure-Modes]], [[PBO-Backtest-Overfitting]], [[Seven-Sins-Backtesting]], [[Backtest-Methodik-Roadmap]], [[Wissenschaftliche-Fundierung-DEFCON]]"
---

# Li, Kim, Cucuringu, Ma — FINSABER (KDD '26)

## Abstract (eigene Worte)

Die Autoren testen die in der LLM-Trading-Literatur viel-zitierte Behauptung, LLM-Agents (FinMem, FinAgent, FinRobot, TradExpert, FinCon, TradingAgents, MarketSenseAI 2.0) schlügen passive Benchmarks. Sie zeigen empirisch: **alle bisherigen Befunde stützen sich auf eng-gewählte Zeitfenster (3-12 Monate), winzige Symbol-Universe (3-30 Aktien), und ignorieren Survivorship-/Look-Ahead-/Data-Snooping-Bias systematisch.** FINSABER ist das erste umfassende Benchmark-Framework für LLM-Investing-Strategien über 20 Jahre, 100+ Symbole, mit expliziter Bias-Mitigation und Regime-Klassifikation. Schlussfolgerung: Die meisten LLM-Vorteile *verschwinden* unter realistischer langfristiger Evaluation. Regime-Analyse zeigt **systematische Asymmetrie**: LLM-Strategien sind **zu konservativ in Bull-Markets** (underperform passive) und **zu aggressiv in Bear-Markets** (heavy losses). Empfehlung: Trend-Detection + regime-aware Risk-Controls > Framework-Komplexität.

## Drei zentrale Bias-Quellen (Section 4)

| Bias | Mechanismus | Beispiel-Effekt | DEFCON-Risiko |
|---|---|---|---|
| **Survivorship Bias** | Backtest enthält nur heute aktive Aktien — delisted/bankrupt fehlen | Grinblatt/Titman: 0,1-0,9% p.a. Verzerrung; auch "preinclusion bias" via heutiger S&P-500-Membership | 🟡 Quick-Screener-Rejects nicht historisiert; Ersatzbank-Selektion könnte survivor-biased sein |
| **Look-Ahead Bias** | Strategie nutzt Information, die zum Decision-Zeitpunkt nicht bekannt war | Feature-Selection auf Full-Period-Outcomes basiert; Symbol-Auswahl über Zukunfts-Performance | 🟡 Backfill-Records (24 von 27) nutzen v3.7-Regeln auf Pre-v3.7-Daten — bei Forward-Verify ausgeschlossen |
| **Data-Snooping Bias** | Wiederholtes Testen auf gleichem Datensatz produziert Overfitting | Bailey: Multiple-Testing-Inflation der Signifikanz | 🔴 v3.0→v3.7 in 3 Monaten — Iterations-Anzahl nicht offen-gelegt; PBO-Pflicht ab Parameter-Tuning |

## Vier Hauptbeiträge (Section 1)

1. **FINSABER-Framework** — 20-J-Multi-Source-Daten (News + Filings + Prices), unbiased Symbol-Selection, explizite Bias-Mitigation
2. **Empirische Reassessment** — LLM-Vorteile aus Vor-Papers verschwinden in breitem/langem Setup
3. **Regime-Analyse** — Bull/Bear-Asymmetrie aufgedeckt: konservativ-in-Bull (underperform), aggressiv-in-Bear (heavy losses)
4. **Design-Empfehlungen** — Trend-Detection + regime-aware Risk-Controls statt zunehmender Architektur-Komplexität

## Quantitative Befunde

| Vor-Paper | Selbst-Report | FINSABER-Eval-Setup | FINSABER-Befund (komprimiert) |
|---|---|---|---|
| MarketSenseAI | 1J3M / 100 Symbole | 20J / 100+ Symbole | LLM-Vorteil signifikant reduziert |
| FinMem | 6M / 5 Symbole | 20J / 100+ | LLM-Vorteil verschwindet weitgehend |
| FinAgent | 6M / 6 Symbole | 20J / 100+ | LLM-Vorteil verschwindet |
| TradExpert | 1J / 30 Symbole | 20J / 100+ | LLM-Vorteil reduziert |
| FinCon | 8M / 8 Symbole | 20J / 100+ | LLM-Vorteil verschwindet |
| TradingAgents | 3M / 3 Symbole | 20J / 100+ | LLM-Vorteil verschwindet |
| MarketSenseAI 2.0 | 2J / 100 Symbole | 20J / 100+ | LLM-Vorteil signifikant reduziert |

**Generalisierung der Beobachtung:** Je breiter (mehr Symbole, längeres Fenster), desto kleiner der LLM-Edge. Ein Hinweis auf systemische Selection-Bias in Vorpapern.

## Regime-Asymmetrie (Section: Regime Analysis)

- **Bull-Markets:** LLM-Strategien zu **konservativ** → underperform passive Buy-and-Hold-Benchmarks
- **Bear-Markets:** LLM-Strategien zu **aggressiv** → erleiden disproportionale Verluste
- **Implikation:** Klassische "Risk-Off"-Heuristik fehlt LLM-Agents; sie reagieren falsch auf Trend-Wechsel

**Direkte Konsequenz für Risk-Management:** Trend-Detection muss **vor** der LLM-Decision stehen, nicht danach. Macro-Regime-Filter (z.B. unser geplanter Track 5b FRED-Filter) gewinnt damit zusätzliche wissenschaftliche Fundierung.

## DEFCON-Implikation — Abgrenzung und Audit-Bezug

**DEFCON ist NICHT LLM-Inferenz** — es ist regelbasiertes Composite-Scoring (5 Blöcke, deterministische Formel). FINSABER's Befunde sind dennoch übertragbar, weil DEFCON als **Selection-Output** dieselben Bias-Quellen erbt:

| FINSABER-Bias | DEFCON-Self-Audit-Frage |
|---|---|
| Survivorship | Welche Ticker hat der Quick-Screener historisch abgelehnt? Existiert ein Reject-Set? |
| Look-Ahead | Werden Forward-Records aus aktuellem v3.7-Wissen für Pre-v3.7-Ticker geschrieben? |
| Data-Snooping | Wie viele v3.x-Iterationen gab es auf demselben Hold-Out? Hold-Out überhaupt definiert? |
| Regime-Asymmetrie | Underperformt DEFCON-Selektion in 2024-25 Bull-Phase ggü. SPY? |

**Wichtigste Erkenntnis für uns:** Auch ein regelbasiertes System verdient einen Bias-Audit, sobald es als Selection-Strategy fungiert. DEFCON tut das (11 Satelliten-Auswahl + Sparrate-Modulation). Die Audit-Methode ist FINSABER-Pattern, nicht eine "LLM-Sicherheitsdebatte".

## Operationalisierung (Phase 2 von Paper-Ingest 2026-04-20)

- **§29.2 Erweiterung** — bisherige AQR-Bench-Komponente um regime-spezifische Sub-Checks (Bull/Bear-Subsample-SR) ergänzen
- **§29.5 Erweiterung** — Seven-Sins-Pre-Flight-Liste **explizit** um FINSABER-Audit-Fragen erweitern (Reject-Set, Iteration-Count, Hold-Out-Definition)
- **Mögliche neue §33 "Skill-Self-Audit"** — DEFCON als Selection-Strategy formell dokumentieren + Audit-Cadence (z.B. jährlich); siehe Codex Round 2 Empfehlung
- **Track 5b FRED Regime-Filter** — wissenschaftlicher Anker stärken: Bull/Bear-Asymmetrie ist kein heuristischer Add-On, sondern empirisch dokumentiert
- **`backtest-ready-forward-verify` Schema-Erweiterung** — `regime_tag` (Bull/Bear/Neutral) + `bias_flags` (survivorship/lookahead/snooping-checked) in `score_history.jsonl`

## Abgrenzung — Was FINSABER NICHT liefert

- **Keine Empfehlung gegen LLM-Investing** — empfiehlt korrekte Eval-Methodik, nicht LLM-Verzicht
- **Keine spezifische Faktor-Analyse** — orthogonal zu Aghassi 2023 Faktor-Kanon
- **Keine Long-Only-Spezifika** — Tests umfassen Long, Short, Long/Short
- **Keine Gewähr für Buy-and-Hold-Wide-Moat** — passive Benchmarks sind SPY und Buy-and-Hold-Aktien-Baskets, nicht qualitäts-gefiltert

## Backlinks

- [[LLM-Investing-Bias-Audit]] — operative Konzeptseite (Bias-Audit-Pattern)
- [[Regime-Aware-LLM-Failure-Modes]] — operative Konzeptseite (Bull/Bear-Asymmetrie)
- [[PBO-Backtest-Overfitting]] — Bailey-Anker für Sin #4 (Data-Snooping)
- [[Seven-Sins-Backtesting]] — FINSABER konkretisiert Sins #1-#4
- [[Factor-Investing-Framework]] — Aghassi 2023 als komplementäre Validations-Ebene
- [[Backtest-Methodik-Roadmap]] — v2.1 Update durch FINSABER + GT-Score
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B19
- [[Weixian Waylon Li]], [[Hyeonjun Kim]], [[Mihai Cucuringu]], [[Tiejun Ma]] — Author-Entities
