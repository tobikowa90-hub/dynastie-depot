# Wiki Index

> Content catalog. Updated on every ingest, query save, or structural edit.
> Last updated: 2026-04-20 Abend (Phase 1b of 6-Paper Ingest — FinReflectKG + Labre + Bayesian RAG + FinDPO: +4 sources, +6 concepts, +12 entities, +1 synthesis = 130 Notes: 124 wiki + 6 raw-ingested; Phase 1a+1b komplett)
> Schema: [[WIKI-SCHEMA]]

---

## Sources
*One page per ingested document or operational tool/skill.*

### Externe Quellen & Forschung
- [[LLMs for Equity Stock Ratings]] — J.P. Morgan AI Research (2024): GPT-4 übertrifft Wall-Street-Analysten bei 3–12-Monats-Aktien-Ratings; Fundamentaldaten sind stärkste Daten-Modalität (1 Quelle)

### Akademische Paper (Wissenschaftliche Fundierung DEFCON)
- [[arXiv-1711.04837]] — Gu, Kelly, Xiu (2019): ML + 5J-Fundamental-Fenster → +2,7% CAGR; Datenhierarchie Fundamentals>Sentiment>Technicals (B1, B7)
- [[Gu-Kelly-Xiu-2020]] — RFS 2020: FCF+GM stabilste Prädiktoren; trailing P/E verliert Vorhersagekraft; forward P/E valide (B2, B3)
- [[Morningstar-Wide-Moat]] — Wide Moat Whitepaper: 8 Moat-Quellen; Moat allein ≠ Excess Return (B4, B6)
- [[Buffetts-Alpha]] — Frazzini/Kabiller/Pedersen AQR 2018: QMJ+BAB+Value; Float-Leverage nicht replizierbar (B5)
- [[Wolff-Echterling-2023]] — Journal of Forecasting 2023: ROIC+FCF top-ranked; Quality-Faktoren stabil; STOXX Europe 600 robust (B8, B9)
- [[Jadhav-Mirza-2025]] — Frontiers in AI 2025: 84-Paper-Survey; News-Positivity-Bias; Multi-Agent-Architektur (B11)
- [[Piotroski-2000]] — Journal of Accounting Research: 9-Punkte-F-Score; High-F-Score Value +7,5% p.a. Outperformance (B12) ← NEU
- [[Novy-Marx-2013]] — Journal of Financial Economics: Gross Profitability Premium ~gleich stark wie B/M (B13) ← NEU
- [[Sloan-1996]] — The Accounting Review: Accruals-Anomalie +10,4% p.a. Low-Accrual-Premium (B14) ← NEU

### Akademische Paper (Backtest-Validation-Framework — §29 Gate)
- [[Bailey-2015-PBO]] — Journal of Computational Finance: PBO/CSCV als Overfitting-Gate (B15) ← NEU 2026-04-19
- [[Aghassi-2023-Fact-Fiction]] — J. Portfolio Management (AQR): 4 Kanon-Faktoren, t-Stat≥3-Hurdle, externer Benchmark (B16) ← NEU 2026-04-19
- [[Flint-Vermaak-2021-Decay]] — SSRN 3986499: Faktor-Half-Life, optimale Rebalance-Cadence (B17) ← NEU 2026-04-19
- [[Palomar-2025-Portfolio-Optimization]] — Cambridge UP: Seven Sins + Methoden-Werkzeugkasten (B18) ← NEU 2026-04-19
- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — KDD '26: LLM-Investing-Vorteile verschwinden unter realistischer Eval; Bull/Bear-Asymmetrie (B19) ← NEU 2026-04-20
- [[Sheppert-2026-GT-Score]] — JRFM 2026: Composite Anti-Overfitting Objective (in-the-loop, komplementär zu PBO) (B20) ← NEU 2026-04-20
- [[Arun-et-al-2025-FinReflectKG]] — arXiv 2508.17906 (Domyn, 2025): Agentic-Reflection-Pattern für Finance-KG aus SEC 10-K; 64,8% All-Rules-Compliance (B21) ← NEU 2026-04-20 Phase 1b
- [[Labre-2025-FinReflectKG-Companion]] — Towards AI (2025-09-29): Praktiker-Lens + Entropy-Paradox-Mitigation für Reflection-KG (B22) ← NEU 2026-04-20 Phase 1b
- [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] — Frontiers AI (Jan 2026): MC-Dropout-Uncertainty für Finance-QA; -27,8% Halluzinationen (B23) ← NEU 2026-04-20 Phase 1b
- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — arXiv 2507.18417 (Imperial, 2025): DPO + Logit-to-Score für Long-Short-Portfolios; 67% p.a. bei 5bps (B24) ← NEU 2026-04-20 Phase 1b

### Datenquellen-APIs
- [[defeatbeta]] — US-Fundamentals (Primär): Income, Cash Flow, ROIC, WACC, Geographic Revenue
- [[Shibui-SQL]] — Technicals + historische Breite + FLAG-Historik (56+ Indikatoren)
- [[OpenInsider]] — Insider-Pflichtquelle; Form-4-Verifikation (Spalte "X"/"M")

### Skills & Module (Operative Tools)
- [[dynastie-depot-skill]] — DEFCON v3.7 Haupt-Skill (Skill-Paket v3.7.2); alle Workflows (!Analysiere, !Rebalancing, !QuickCheck, !CAPEX-FCF-ANALYSIS). Schritt 7 delegiert an `backtest-ready-forward-verify` (seit 19.04.2026)
- [[backtest-ready-forward-verify]] — Satellit für Forward-Run Persistence-Pipeline; kein eigenes Trigger-Word, aktiviert programmatisch aus dynastie-depot Schritt 7. Orchestriert Freshness + STATE.md-Tripwire + §28.2 Δ-Gate + Dry-Run + Append + git add (neu 19.04.2026)
- [[quick-screener]] — Stufe-0 Vorfilter; 3 Filter (P/FCF, ROIC, Moat-Proxy); Ampel-Ergebnis
- [[insider-intelligence]] — Form-4-Automatisierung; 8 US-Satelliten; FLAG-Detection (>$20M diskretionär)
- [[non-us-fundamentals]] — yfinance für ASML/RMS/SU; EUR, IFRS, kein API-Key

---

## Entities
*People, organizations, places, products, projects.*

### Forschung & KI
- [[J.P. Morgan AI Research]] — KI-Forschungsgruppe von JPMorgan Chase; Autoren: Papasotiriou, Sood, Reynolds
- [[GPT-4]] — OpenAI Large Language Model; in Finanzforschung eingesetzt für Ratings, Sentiment, Zusammenfassungen
- [[S&P 500]] — US-Leitindex (500 Unternehmen); Standarduniversum für quantitative Aktienanalyse

### Autoren (akademische Quellen)
- [[Dominik Wolff]] — Co-Autor "Stock picking with machine learning" (Wiley)
- [[Fabian Echterling]] — Co-Autor "Stock picking with machine learning" (Wiley)
- [[Aakanksha Jadhav]] — Co-Autorin "Large Language Models in equity markets" (PMC Survey, 84 Studien)
- [[Vishal Mirza]] — Co-Autor "Large Language Models in equity markets" (PMC Survey, 84 Studien)
- [[Weixian Waylon Li]] — Erstautor FINSABER (Edinburgh AIAI) ← NEU 2026-04-20
- [[Hyeonjun Kim]] — Co-Autor FINSABER (Sungkyunkwan) ← NEU 2026-04-20
- [[Mihai Cucuringu]] — Co-Autor FINSABER (UCLA Math/Stats + Oxford OMI) ← NEU 2026-04-20
- [[Tiejun Ma]] — Co-Autor FINSABER (Edinburgh AIAI, vermutlich Supervisor) ← NEU 2026-04-20
- [[Alexander Pearson Sheppert]] — Alleinautor GT-Score (Capitol Tech U) ← NEU 2026-04-20
- [[Abhinav Arun]] — Erstautor FinReflectKG (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[Fabrizio Dimino]] — Co-Autor FinReflectKG + Präsentator Quant x AI NY 2025 (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[Tejas Prakash Agarwal]] — Co-Autor FinReflectKG (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[Bhaskarjit Sarmah]] — Co-Autor FinReflectKG (Domyn Gurgaon India) ← NEU 2026-04-20 Phase 1b
- [[Stefano Pasquali]] — Senior Co-Autor FinReflectKG (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[Marcelo Labre]] — Praktiker/Blogger Towards AI, Quant x AI Event NY 2025 ← NEU 2026-04-20 Phase 1b
- [[Lebede Ngartera]] — Erstautor Bayesian RAG (TeraSystemsAI Philadelphia) ← NEU 2026-04-20 Phase 1b
- [[Saralees Nadarajah]] — Co-Autor Bayesian RAG (U Manchester Mathematics) ← NEU 2026-04-20 Phase 1b
- [[Rodoumta Koina]] — Co-Autor Bayesian RAG (U N'Djamena Chad) ← NEU 2026-04-20 Phase 1b
- [[Giorgos Iacovides]] — Erstautor FinDPO + FinLlama (Imperial College London) ← NEU 2026-04-20 Phase 1b
- [[Wuyang Zhou]] — Co-Autor FinDPO (Imperial College London) ← NEU 2026-04-20 Phase 1b
- [[Danilo Mandic]] — Senior-Author FinDPO, Professor Imperial College London ← NEU 2026-04-20 Phase 1b

### Satelliten (aktive Positionen)
- [[AVGO]] — Broadcom Inc. | DEFCON 🟢 4 | Score 84 | Kalibrierungsanker #1 (v3.7)
- [[COST]] — Costco Wholesale | DEFCON 🟢 4 | Score 69
- [[RMS]] — Hermès International | DEFCON 🟢 4 | Score 68 | Non-US | Screener-Exception (ROIC 24% >> WACC)
- [[VEEV]] — Veeva Systems | DEFCON 🟢 4 | Score 74
- [[SU]] — Schneider Electric | DEFCON 🟢 4 | Score 69 | Non-US
- [[BRKB]] — Berkshire Hathaway B | DEFCON 🟢 4 | Score 75
- [[V]] — Visa Inc. | DEFCON 🟢 4 | Score 86
- [[APH]] — Amphenol Corp. | DEFCON 🟡 3 | Score 63 | 🔴 FLAG (Score-basiert)
- [[ASML]] — ASML Holding | DEFCON 🟡 3 | Score 68 | Non-US
- [[TMO]] — Thermo Fisher Scientific | DEFCON 🟠 2 | Score 63 | Q1 Earnings 23.04. (D3→D2 v3.7)
- [[MSFT]] — Microsoft | DEFCON 🟠 2 | Score 59 | 🔴 CapEx-FLAG | Q3 Earnings 29.04.

### Ersatzbank
- [[GOOGL]] — MSFT-Ersatz | Score 72, DEFCON 3 | 🔴 FLAG: CapEx ~75% OCF — kein Einstieg
- [[ZTS]] — VEEV/TMO-Ersatz | DEFCON 4 | bereit
- [[PEGA]] — Slot-16-Kandidat | Earnings Mai 2026
- [[MKL]] — BRK.B-Ersatz | Specialty-Versicherung + Holding
- [[NVDA]] — AVGO-Ersatz | GPU-Marktführer, KI-Infrastruktur
- [[SNPS]] — ASML-Ersatz | EDA-Marktführer, Ansys-Goodwill-Risiko
- [[RACE]] — RMS-Ersatz | Luxus-Auto, Wide Moat, Non-US
- [[DE]] — SU-Ersatz | Landmaschinen, Precision-Ag
- [[SPGI]] — Watchlist | Finanzinfrastruktur, Q1 Earnings 28.04.

---

## Concepts
*Ideas, topics, themes, frameworks, methods.*

### KI & Finanzforschung
- [[LLM-Based Stock Rating]] — Automatisierte Aktien-Ratings via LLM; schlägt Analysten bei 3–6 Monaten (1 Quelle)
- [[Financial Fundamentals Analysis]] — Bilanz, GuV, Cashflow-Analyse aus SEC-Filings; stärkste Daten-Modalität für KI-Ratings (1 Quelle)
- [[Chain-of-Thought Prompting]] — Prompting-Technik: LLM denkt Schritt für Schritt; erhöht Qualität und Interpretierbarkeit (1 Quelle)
- [[News Sentiment Analysis]] — Sentiment-Scoring von Finanznachrichten; kurzfristig nützlich, mittelfristig Positivitäts-Bias (1 Quelle)
- [[Forward Returns Evaluation]] — Quintil-basierte Methode zur Bewertung von Rating-Genauigkeit über verschiedene Zeithorizonte (1 Quelle)
- [[Analyst Stock Ratings]] — Traditionelle Wall-Street-Ratings; struktureller 43%-Strong-Buy-Bias; langfristig besser als LLMs (1 Quelle)

### DEFCON-System (Kern-Framework)
- [[DEFCON-System]] — 100-Punkte-Scoring-Matrix; 5 Blöcke; Sparplan-Formel; v3.7 (System-Gap-Release; Skill-Paket v3.7.2 seit 19.04.2026)
- [[CapEx-FLAG]] — Die heilige Regel; 3 Trigger; überschreibt jeden Score
- [[ROIC-vs-WACC]] — Harter Malus wenn ROIC < WACC; 8 Punkte Fundamentals
- [[Analyse-Pipeline]] — Stufe 0 → 1 → 2 → Entscheidung; Skill-Hierarchie
- [[Tariff-Exposure-Regel]] — Post Liberation Day; <15% kein FLAG, >35% FLAG
- [[Non-US-Scoring]] — IFRS-Addendum für ASML/RMS/SU; Insider manuell via AFM/AMF
- [[Score-Archiv]] — Append-only JSONL-Historie aller Score-Records; Basis für 2028+ Backtest (neu 17.04.2026)
- [[FLAG-Event-Log]] — Trigger + Resolution für 4 FLAG-Typen; Quelle für deskriptive Event-Study (neu 17.04.2026)
- [[Backtest-Ready-Infrastructure]] — 4-Layer-Architektur (State/Narrative/History/Projection); §18 6-Dateien-Sync (neu 17.04.2026)

### Wissenschaftliche Fundierung DEFCON
- [[5J-Fundamental-Fenster]] — 5J-Durchschnitt > Spot als Prädiktor; Pflichtperspektive in jeder Analyse
- [[FCF-Primacy]] — FCF-Yield + Fwd P/E primär; trailing P/E nur Kontext (Gu/Kelly/Xiu)
- [[Moat-Taxonomie-Morningstar]] — 8 Moat-Quellen-Checkliste; Wide Moat + Fundamentals = Alpha
- [[Buffett-Faktorlogik]] — cheap+safe+quality Dreiklang; Float-Leverage nicht replizierbar
- [[QMJ-Faktor]] — Quality Minus Junk; erklärt Buffetts Alpha vollständig
- [[F-Score-Quality-Signal]] — Piotroski 9-Kriterien-Score; ≥7 → +2 Pt. Fundamentals-Bonus (B12) ← NEU
- [[Gross-Profitability-Premium]] — Novy-Marx GP/TA; eigenständiger Renditefaktor, +2 Pt. Fundamentals-Metrik (B13) ← NEU
- [[Accruals-Anomalie-Sloan]] — Sloan 1996; Low-Accrual outperformt +10,4% p.a.; validiert v3.5-Schwellen (B14) ← NEU

### Backtest-Validation-Framework (§29 Gate — FUTURE-ACTIVATION 2028-04-01)
- [[PBO-Backtest-Overfitting]] — Bailey PBO/CSCV-Methode; §29.1 Methoden-Gate (B15) ← NEU 2026-04-19
- [[Factor-Investing-Framework]] — AQR 4-Faktor-Kanon + DEFCON-Mapping; §29.2 External-Bench + §29.4 t-Stat≥3 (B16) ← NEU 2026-04-19
- [[Factor-Information-Decay]] — Flint/Vermaak Half-Life pro Faktor; §29.3 Cadence-Check (B17) ← NEU 2026-04-19
- [[Seven-Sins-Backtesting]] — Palomar Sünden-Katalog; §29.5 Pre-Flight-Gate (Sin #7 n.a. Long-Only) (B18) ← NEU 2026-04-19
- [[Palomar-Methods-Reference]] — Palomar Ch 6 + 8.3-8.5 + 7.5 + 11 konsolidierte Methoden-Referenz ← NEU 2026-04-19
- [[LLM-Investing-Bias-Audit]] — FINSABER-Pattern (Survivorship/Look-Ahead/Data-Snooping) für DEFCON-Self-Audit (B19) ← NEU 2026-04-20
- [[Regime-Aware-LLM-Failure-Modes]] — FINSABER Bull/Bear-Asymmetrie; Anker für Track 5b FRED Regime-Filter (B19) ← NEU 2026-04-20
- [[Composite-Anti-Overfitting-Objective]] — GT-Score-Pattern (in-the-loop); Tie-Break R0 für Track 5b Grid-Search (B20) ← NEU 2026-04-20

### KG-/RAG-/LLM-Architektur (Phase 1b 6-Paper-Ingest — 2026-04-20)
- [[Knowledge-Graph-Finance-Architecture]] — Schema-guided KG-Primitive für SEC-Filings; 5-Tuple + 10 Entity-Types + 10 Relation-Types (B21) ← NEU 2026-04-20 Phase 1b
- [[Agentic-Reflection-Pattern]] — Critic-Corrector-Loop, +22,5pp All-Rules-Compliance; generisches Multi-Agent-Muster (B21) ← NEU 2026-04-20 Phase 1b
- [[LLM-as-a-Judge-Evaluation]] — Ground-truth-agnostic Evaluation; 4 Dimensionen + 3-Vote-Consensus (B21) ← NEU 2026-04-20 Phase 1b
- [[RAG-Uncertainty-Quantification]] — Bayesian-RAG-Pattern via MC-Dropout; epistemische Unsicherheit $S_i = \mu_i - \lambda \sigma_i$ (B23) ← NEU 2026-04-20 Phase 1b
- [[LLM-Preference-Optimization-Finance]] — DPO statt SFT für Finance-LLMs; +11% F1 vs. FinGPT v3.3 (B24) ← NEU 2026-04-20 Phase 1b
- [[Sentiment-Strength-Logit-Extraction]] — Kontinuierliche Sentiment-Scores aus causal-LLM-Logits; Long-Short-Enabler (B24) ← NEU 2026-04-20 Phase 1b

### Token-Effizienz & System
- [[Token-Mechanik]] — Strukturiertes Token-Management; Snapshot-First, MCP-Minimalset
- [[Context-Hygiene]] — On-demand Loading; Compact-Regeln; MCP-Session-Typen
- [[CLAUDE-md-Konstitution]] — CLAUDE.md als Wahrheitsquelle; 4 Pflicht-Lektüren; Trigger-Liste
- [[Context-Hygiene-Code]] — Claude Code-spezifisch: autoCompact 75%, Tool Search, Deny Rules
- [[Update-Klassen-DEFCON]] — A/B/C/D Klassen; Klasse-C-Priorität (Event-getriggert, sofort)
- [[Faktortabelle-Architektur]] — Snapshot-First; config.yaml → Faktortabelle → API; ~60-70% Token-Einsparung
- [[Session-Start-Protokoll]] — STATE.md als Single-Entry-Point; ersetzt 4-Datei-Auto-Read (~80% Token-Einsparung, seit 17.04.2026)
- [[INSTRUKTIONEN-SKILL-Trennung]] — Post-Dedup Arbeitsteilung: User-Workflow (INSTRUKTIONEN) vs. Scoring-Technik (SKILL); 587→452 Zeilen, 10 Cross-Refs, seit 17.04.2026

### Depot-Struktur & Planung
- [[ETF-Core]] — 65% des Sparplans (617,50€/Monat); IWDA, EIMI, EXUSA, AVGC, EWG2
- [[Steuer-Architektur]] — Lombardkredit, FIFO-Klon, 10-Jahres-Kaskade, PKV-Wäsche; Zeithorizont 2058

---

## Synthesis
*Cross-source analyses and evolving theses.*

- [[AI in Investment Analysis]] — Zentrale Synthese: KI in Aktienanalyse, Depot-Strategie, Trading; wächst mit jeder neuen Quelle
- [[Investing-Mastermind-Index]] — Zentraler Navigationsindex: Depot-State, Satelliten, Konzepte, Skills
- [[Depot-State-April-2026]] — Monatlicher Snapshot; Sparplan-Verteilung; offene Entscheidungen
- [[Wissenschaftliche-Fundierung-DEFCON]] — 14-Befunde-Matrix: 10 Paper → operative Konsequenzen für DEFCON v3.5 (Stand 17.04.2026)
- [[Backtest-Methodik-Roadmap]] — Entscheidungsmatrix für 2028-Review; Options A–D je nach Datenlage; welcher Paper als Benchmark wann anlegbar (neu 17.04.2026)
- [[Knowledge-Graph-Architektur-Roadmap]] — v0.1 Entscheidungsvorlage KG/RAG vs. XML-Direkt-Parsing für insider-intelligence + zukünftige Skills; 3 Qualitäts-Gates + 3 konkrete Szenarien ← NEU 2026-04-20 Phase 1b

---

## Queries
*Saved responses to notable questions.*

*(none yet)*
