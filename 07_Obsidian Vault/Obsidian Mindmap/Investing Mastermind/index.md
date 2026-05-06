# Wiki Index

> Content catalog. Updated on every ingest, query save, or structural edit.
> Last updated: 2026-05-06 (Satelliten-State-Drift-Cleanup: 8 von 11 Zeilen auf aktuellen DEFCON/Score/Sparraten/FLAG-State gebracht — AVGO 84→53/D4→D2/FLAG, COST/RMS/VEEV/SU 🟢4→🟡3 Schema-Fix, V 86→64/D4→D2 Rescoring 28.04., APH 63→61/D3→D2 Q1 30.04., TMO 63/D2→67/D3 Resolve 23.04., MSFT 59→50 Q3 30.04. Sparraten als Tertiär-Info ergänzt.)
> Last updated (zuvor): 2026-04-27 (Paper-Ingest Phase A+B+C: 14 source-pages B25-B28 + 10 SOURCE-ONLY, 6 neue concept-pages, 30 entity-pages. Phase-B-Errata gefixt: 3 entity-files mit halluzinierten Vornamen umbenannt + broken sources-link `Amundi-2024-Quality-Pillars` → `Amundi-Quality-2021` korrigiert in 4 entity-pages.)
> Last updated (zuvor): 2026-04-26 (Hub-Split-Lückenschluss: 3 neue Vault-Stubs PORTFOLIO/PIPELINE/SYSTEM als Backlink-Anker + DEFCON-System 4-Layer→5-Layer Inkonsistenz gefixt; Lint-Follow-up zur Vault-Sanitation 25.04.)
> Last updated (zuvor): 2026-04-25 (Vault-Concept-Seiten-Sanierung Tier-2-00_Core-Refactor — 14 Files: Hub-Split STATE→Hub+PORTFOLIO/PIPELINE/SYSTEM, CORE-MEMORY §1→§12/§13, §18 v2.1 Trigger-Mapping, Tripwire-Migration STATE→PORTFOLIO. Keine neuen Pages, nur Drift-Sanierung)
> Schema: [[WIKI-SCHEMA]]

---

## Sources
*One page per ingested document or operational tool/skill.*
*Sub-Ordner-Layout (seit 2026-04-23): `wiki/sources/{papers,tools,references,videos}/`*

### Externe Quellen & Forschung (`wiki/sources/papers/`)
- [[llms-for-equity-stock-ratings|LLMs for Equity Stock Ratings]] — J.P. Morgan AI Research (2024): GPT-4 übertrifft Wall-Street-Analysten bei 3–12-Monats-Aktien-Ratings; Fundamentaldaten sind stärkste Daten-Modalität (1 Quelle)

### Akademische Paper (Wissenschaftliche Fundierung DEFCON) — `wiki/sources/papers/`
- [[arXiv-1711.04837]] — Gu, Kelly, Xiu (2019): ML + 5J-Fundamental-Fenster → +2,7% CAGR; Datenhierarchie Fundamentals>Sentiment>Technicals (B1, B7)
- [[Gu-Kelly-Xiu-2020]] — RFS 2020: FCF+GM stabilste Prädiktoren; trailing P/E verliert Vorhersagekraft; forward P/E valide (B2, B3)
- [[Morningstar-Wide-Moat]] — Wide Moat Whitepaper: 8 Moat-Quellen; Moat allein ≠ Excess Return (B4, B6)
- [[Buffetts-Alpha]] — Frazzini/Kabiller/Pedersen AQR 2018: QMJ+BAB+Value; Float-Leverage nicht replizierbar (B5)
- [[Wolff-Echterling-2023]] — Journal of Forecasting 2023: ROIC+FCF top-ranked; Quality-Faktoren stabil; STOXX Europe 600 robust (B8, B9)
- [[Jadhav-Mirza-2025]] — Frontiers in AI 2025: 84-Paper-Survey; News-Positivity-Bias; Multi-Agent-Architektur (B11)
- [[Piotroski-2000]] — Journal of Accounting Research: 9-Punkte-F-Score; High-F-Score Value +7,5% p.a. Outperformance (B12) ← NEU
- [[Novy-Marx-2013]] — Journal of Financial Economics: Gross Profitability Premium ~gleich stark wie B/M (B13) ← NEU
- [[Sloan-1996]] — The Accounting Review: Accruals-Anomalie +10,4% p.a. Low-Accrual-Premium (B14) ← NEU

### Akademische Paper (Backtest-Validation-Framework — §29 Gate) — `wiki/sources/papers/`
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

### Akademische Paper (Paper-Ingest Phase A — B25-B28 + 10 SOURCE-ONLY) — `wiki/sources/papers/`
- [[McLean-Pontiff-2016]] — Journal of Finance 2016: Cross-Sect Predictoren −26% Out-of-Sample + −58% Post-Publication-Decay (operativer Total-Decline; davon ≈32pp publication-effect lower bound) (B25 `meta-gate` § 29.7) ← NEU 2026-04-26 Phase A
- [[Lakonishok-Lee-2001]] — Review of Financial Studies 2001: Insider-Käufe informativer als -Verkäufe; Aggregate-Predictability + Small-Cap-Concentration (B26 `active-scoring-validation`) ← NEU 2026-04-26 Phase A
- [[Ke-Huddart-Petroni-2003]] — JAE 2003: Insider-Verkäufe Q-9 bis Q-3 vor Earnings-Break (Legal-Jeopardy-Window); Q-2/Q-1 ≈ Null abnormal (B27 `design-context`) ← NEU 2026-04-26 Phase A
- [[Tetlock-2007]] — Journal of Finance 2007: Hohe Media-Pessimism prädiziert kurzfrist Drawdown + komplette Reversion zu Fundamentals (5-10 Tage) (B28 `design-context`) ← NEU 2026-04-26 Phase A
- [[Asness-Frazzini-Pedersen-2013-QMJ]] — AQR/Review of Accounting Studies 2013/2019: QMJ Long-Short, 4-Pillars-Quality (Profit/Growth/Safety/Payout) (SOURCE-ONLY anchors B5) ← NEU 2026-04-26 Phase A
- [[Mauboussin-Callahan-2024-Measuring-Moat]] — Morgan Stanley Counterpoint Global 2024: Competitive Advantage Period (CAP) als zweite Moat-Dimension (Magnitude × Sustainability) (SOURCE-ONLY anchors B4, B6) ← NEU 2026-04-26 Phase A
- [[Amundi-Quality-2021]] — Amundi WP 113-2021: Practitioner-Validation 4-Pillars (Profit/Earnings-Quality/Safety/Investment); +2,8% p.a. IR 0,81 post-GFC (SOURCE-ONLY anchors B5, B8) ← NEU 2026-04-26 Phase A
- [[Fama-French-2015-Five-Factor]] — JFE 2015: RMW + CMA Faktoren; HML wird redundant für Cross-Section-Erklärung (SOURCE-ONLY anchors B2, B8) ← NEU 2026-04-26 Phase A
- [[Harvey-Liu-Zhu-2016]] — Review of Financial Studies 2016: t≥3-Hurdle für Faktor-Discovery (Multiple-Testing über 313 Studien) (SOURCE-ONLY anchors B16) ← NEU 2026-04-26 Phase A
- [[Asness-Moskowitz-Pedersen-2013-VME]] — Journal of Finance 2013: Value + Momentum global, persistent, neg. korreliert über 8 Asset-Klassen (SOURCE-ONLY anchors B7) ← NEU 2026-04-26 Phase A
- [[Fama-French-2006-Profitability]] — JFE 2006: Valuation-Equation; B/M, Profitability, Investment prädizieren Cross-Section-Returns (SOURCE-ONLY anchors B2, B8; gefoldete Sibling-Note F/F 2004 Draft) ← NEU 2026-04-26 Phase A
- [[Hou-Xue-Zhang-2015-q-Factor]] — Review of Financial Studies 2015: q-Theory-Faktor (Mkt+ME+I/A+ROE) — konvergente Evidenz zu FF-5 (SOURCE-ONLY anchors B2, B8) ← NEU 2026-04-26 Phase A
- [[Yang-Liu-Wang-2023-FinGPT]] — FinLLM 2023 @ IJCAI: Open-Source 5-Layer-Framework für Finance-LLMs; LoRA-Fine-Tuning (SOURCE-ONLY komplementär B19, B24) ← NEU 2026-04-26 Phase A
- [[2iQ-Insider-Meta-Review-2021]] — 2iQ Research Blog 2021 (industry-meta): Konsolidiertes Review Insider-Trading-Akademie 1968-2018 (SOURCE-ONLY anchors B26, B27) ← NEU 2026-04-26 Phase A

### Datenquellen-APIs (`wiki/sources/tools/`)
- [[defeatbeta]] — US-Fundamentals (Primär): Income, Cash Flow, ROIC, WACC, Geographic Revenue
- [[Shibui-SQL]] — Technicals + historische Breite + FLAG-Historik (56+ Indikatoren)
- [[OpenInsider]] — Insider-Pflichtquelle; Form-4-Verifikation (Spalte "X"/"M")

### Methodik & Standards (`wiki/sources/references/`)
- [[Morningstar-Wide-Moat]] — Wide-Moat Whitepaper: 8 Moat-Quellen-Taxonomie; Methodik-Referenz für Moat-Scoring

### Skills & Module (Operative Tools) — `wiki/sources/tools/`
- [[dynastie-depot-skill]] — DEFCON v3.7 Haupt-Skill (Skill-Paket v3.7.2); alle Workflows (!Analysiere, !Rebalancing, !QuickCheck, !CAPEX-FCF-ANALYSIS). Schritt 7 delegiert an `backtest-ready-forward-verify` (seit 19.04.2026)
- [[backtest-ready-forward-verify]] — Satellit für Forward-Run Persistence-Pipeline; kein eigenes Trigger-Word, aktiviert programmatisch aus dynastie-depot Schritt 7. Orchestriert Freshness + PORTFOLIO.md-Tripwire + §28.2 Δ-Gate + Dry-Run + Append + git add (neu 19.04.2026; Tripwire seit Tier-2-Refactor 25.04.2026 auf PORTFOLIO.md, v1.0.1)
- [[quick-screener]] — Stufe-0 Vorfilter; 3 Filter (P/FCF, ROIC, Moat-Proxy); Ampel-Ergebnis
- [[insider-intelligence]] — Form-4-Automatisierung; 8 US-Satelliten; FLAG-Detection (>$20M diskretionär)
- [[non-us-fundamentals]] — yfinance für ASML/RMS/SU; EUR, IFRS, kein API-Key
- [[backtest-ready-forward-verify]] — Persistence-Pipeline-Satellit; programmatisch aus dynastie-depot Schritt 7 aktiviert

### Videos (`wiki/sources/videos/`)
*Eingepflegt via INGEST-VIDEO-Workflow (siehe WIKI-SCHEMA §INGEST-VIDEO). Aktuell leer — wird nach erstem Pilot-Ingest gefüllt.*

#### Earnings Calls (`wiki/sources/videos/earnings-calls/`)
_(noch leer)_

#### Interviews (`wiki/sources/videos/interviews/`)
_(noch leer)_

#### Conferences (`wiki/sources/videos/conferences/`)
_(noch leer)_

#### Analyses (`wiki/sources/videos/analyses/`)
_(noch leer)_

#### Updating System (`wiki/sources/videos/updating-system/`)
*Videos zu Tool-/System-Upgrades, Claude-Skills, neuen Workflows.*
- [[2026-04-08-charlie-automates-graphify-claude-code]] — Pilot-Ingest, Charlie Automates
- [[2026-04-22-dubibubii-claude-code-powerful-settings]] — Dubibubii Powerful Settings, Adoption 1A/2O/4R
- [[2026-03-10-jake-van-clief-folder-system-ai-agents]] — Jake Van Clief Folder-System, Adoption `pending-brainstorm`

---

## Entities
*People, organizations, places, products, projects.*

### Forschung & KI
- [[jp-morgan-ai-research|J.P. Morgan AI Research]] — KI-Forschungsgruppe von JPMorgan Chase; Autoren: Papasotiriou, Sood, Reynolds
- [[gpt-4|GPT-4]] — OpenAI Large Language Model; in Finanzforschung eingesetzt für Ratings, Sentiment, Zusammenfassungen
- [[sp-500|S&P 500]] — US-Leitindex (500 Unternehmen); Standarduniversum für quantitative Aktienanalyse

### Autoren (akademische Quellen)
- [[dominik-wolff|Dominik Wolff]] — Co-Autor "Stock picking with machine learning" (Wiley)
- [[fabian-echterling|Fabian Echterling]] — Co-Autor "Stock picking with machine learning" (Wiley)
- [[aakanksha-jadhav|Aakanksha Jadhav]] — Co-Autorin "Large Language Models in equity markets" (PMC Survey, 84 Studien)
- [[vishal-mirza|Vishal Mirza]] — Co-Autor "Large Language Models in equity markets" (PMC Survey, 84 Studien)
- [[waylon-li|Weixian Waylon Li]] — Erstautor FINSABER (Edinburgh AIAI) ← NEU 2026-04-20
- [[hyeonjun-kim|Hyeonjun Kim]] — Co-Autor FINSABER (Sungkyunkwan) ← NEU 2026-04-20
- [[mihai-cucuringu|Mihai Cucuringu]] — Co-Autor FINSABER (UCLA Math/Stats + Oxford OMI) ← NEU 2026-04-20
- [[tiejun-ma|Tiejun Ma]] — Co-Autor FINSABER (Edinburgh AIAI, vermutlich Supervisor) ← NEU 2026-04-20
- [[alexander-pearson-sheppert|Alexander Pearson Sheppert]] — Alleinautor GT-Score (Capitol Tech U) ← NEU 2026-04-20
- [[abhinav-arun|Abhinav Arun]] — Erstautor FinReflectKG (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[fabrizio-dimino|Fabrizio Dimino]] — Co-Autor FinReflectKG + Präsentator Quant x AI NY 2025 (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[tejas-prakash-agarwal|Tejas Prakash Agarwal]] — Co-Autor FinReflectKG (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[bhaskarjit-sarmah|Bhaskarjit Sarmah]] — Co-Autor FinReflectKG (Domyn Gurgaon India) ← NEU 2026-04-20 Phase 1b
- [[stefano-pasquali|Stefano Pasquali]] — Senior Co-Autor FinReflectKG (Domyn NY) ← NEU 2026-04-20 Phase 1b
- [[marcelo-labre|Marcelo Labre]] — Praktiker/Blogger Towards AI, Quant x AI Event NY 2025 ← NEU 2026-04-20 Phase 1b
- [[lebede-ngartera|Lebede Ngartera]] — Erstautor Bayesian RAG (TeraSystemsAI Philadelphia) ← NEU 2026-04-20 Phase 1b
- [[saralees-nadarajah|Saralees Nadarajah]] — Co-Autor Bayesian RAG (U Manchester Mathematics) ← NEU 2026-04-20 Phase 1b
- [[rodoumta-koina|Rodoumta Koina]] — Co-Autor Bayesian RAG (U N'Djamena Chad) ← NEU 2026-04-20 Phase 1b
- [[giorgos-iacovides|Giorgos Iacovides]] — Erstautor FinDPO + FinLlama (Imperial College London) ← NEU 2026-04-20 Phase 1b
- [[wuyang-zhou|Wuyang Zhou]] — Co-Autor FinDPO (Imperial College London) ← NEU 2026-04-20 Phase 1b
- [[danilo-mandic|Danilo Mandic]] — Senior-Author FinDPO, Professor Imperial College London ← NEU 2026-04-20 Phase 1b
- [[r-david-mclean]] — Erstautor McLean/Pontiff (B25) — Georgetown McDonough; Cross-Section-Predictability + Post-Publication-Decay ← NEU 2026-04-26 Phase A
- [[jeffrey-pontiff]] — Co-Autor McLean/Pontiff (B25) — Boston College Carroll ← NEU 2026-04-26 Phase A
- [[josef-lakonishok]] — Erstautor Lakonishok/Lee (B26) — UIUC; Insider-Trading-Akademiker ← NEU 2026-04-26 Phase A
- [[inmoo-lee]] — Co-Autor Lakonishok/Lee (B26) — Korea University ← NEU 2026-04-26 Phase A
- [[bin-ke]] — Erstautor Ke/Huddart/Petroni (B27) — Penn State; Earnings-Quality + Insider-Trading ← NEU 2026-04-26 Phase A
- [[steven-huddart]] — Co-Autor Ke/Huddart/Petroni (B27) — Penn State Smeal ← NEU 2026-04-26 Phase A
- [[kathy-petroni]] — Co-Autorin Ke/Huddart/Petroni (B27) — Michigan State Eli Broad ← NEU 2026-04-26 Phase A
- [[paul-tetlock]] — Alleinautor Tetlock 2007 (B28) — Columbia Business School; Sentiment-Mean-Reversion ← NEU 2026-04-26 Phase A
- [[michael-mauboussin]] — Erstautor Mauboussin/Callahan 2024 (SOURCE-ONLY) — Morgan Stanley Counterpoint Global; CAP-Konzept ← NEU 2026-04-26 Phase A
- [[dan-callahan]] — Co-Autor Mauboussin/Callahan 2024 — Morgan Stanley Counterpoint Global ← NEU 2026-04-26 Phase A
- [[clifford-asness]] — Co-Autor QMJ 2013 + VME 2013 (SOURCE-ONLY) — AQR Capital Management Founder ← NEU 2026-04-26 Phase A
- [[andrea-frazzini]] — Co-Autor QMJ 2013 (SOURCE-ONLY) — AQR Capital Management ← NEU 2026-04-26 Phase A
- [[lasse-pedersen]] — Co-Autor QMJ 2013 + VME 2013 (SOURCE-ONLY) — NYU Stern + Copenhagen Business School + AQR ← NEU 2026-04-26 Phase A
- [[tobias-moskowitz]] — Co-Autor VME 2013 (SOURCE-ONLY) — University of Chicago Booth + NBER ← NEU 2026-04-26 Phase A
- [[frederic-lepetit]] — Co-Autor Amundi-Quality-2021 (SOURCE-ONLY) — Amundi Asset Management Quantitative Research ← NEU 2026-04-26 Phase A (Errata 27.04.: Vorname von "Jean-Baptiste" zu "Frédéric" korrigiert)
- [[amina-cherief]] — Co-Autorin Amundi-Quality-2021 (SOURCE-ONLY) — Amundi AM ← NEU 2026-04-26 Phase A (Errata 27.04.: Vorname von "Nazim" zu "Amina" korrigiert)
- [[yannick-ly]] — Co-Autor Amundi-Quality-2021 (SOURCE-ONLY) — Amundi AM ← NEU 2026-04-26 Phase A (Errata 27.04.: Vorname von "Thy" zu "Yannick" korrigiert)
- [[takaya-sekine]] — Co-Autor Amundi-Quality-2021 (SOURCE-ONLY) — Amundi AM ← NEU 2026-04-26 Phase A
- [[eugene-fama]] — Co-Autor Fama-French 2006 + 2015 (SOURCE-ONLY) — University of Chicago Booth, Nobel-Preisträger 2013 ← NEU 2026-04-26 Phase A
- [[kenneth-french]] — Co-Autor Fama-French 2006 + 2015 (SOURCE-ONLY) — Dartmouth Tuck ← NEU 2026-04-26 Phase A
- [[campbell-harvey]] — Erstautor Harvey/Liu/Zhu 2016 (SOURCE-ONLY) — Duke Fuqua + NBER; t≥3-Hurdle ← NEU 2026-04-26 Phase A
- [[yan-liu]] — Co-Autor Harvey/Liu/Zhu 2016 (SOURCE-ONLY) — Texas A&M ← NEU 2026-04-26 Phase A
- [[heqing-zhu]] — Co-Autor Harvey/Liu/Zhu 2016 (SOURCE-ONLY) — University of Oklahoma ← NEU 2026-04-26 Phase A
- [[kewei-hou]] — Erstautor Hou/Xue/Zhang 2015 q-Factor (SOURCE-ONLY) — Ohio State Fisher ← NEU 2026-04-26 Phase A
- [[chen-xue]] — Co-Autor Hou/Xue/Zhang 2015 q-Factor (SOURCE-ONLY) — University of Cincinnati Lindner ← NEU 2026-04-26 Phase A
- [[lu-zhang]] — Co-Autor Hou/Xue/Zhang 2015 q-Factor (SOURCE-ONLY) — Ohio State Fisher + NBER ← NEU 2026-04-26 Phase A
- [[hongyang-yang]] — Erstautor FinGPT 2023 (SOURCE-ONLY) — AI4Finance Foundation ← NEU 2026-04-26 Phase A
- [[xiao-yang-liu]] — Co-Autor FinGPT 2023 (SOURCE-ONLY) — Columbia University ← NEU 2026-04-26 Phase A
- [[christina-dan-wang]] — Co-Autorin FinGPT 2023 (SOURCE-ONLY) — NYU Shanghai ← NEU 2026-04-26 Phase A
- [[robert-hable]] — Alleinautor 2iQ-Insider-Meta-Review 2021 (SOURCE-ONLY industry-meta) — 2iQ Research ← NEU 2026-04-26 Phase A

### Satelliten (aktive Positionen)
- [[AVGO]] — Broadcom Inc. | DEFCON 🟠 2 | Score 53 | 🔴 FLAG (insider_selling_20m, $106M+ diskretionär 90d) | Sparrate 0€ | Q1 FY26 Forward-Vollanalyse 30.04. (84→53, Δ-31, Codex R1+R2 74% Confidence)
- [[COST]] — Costco Wholesale | DEFCON 🟡 3 | Score 69 | Sparrate 38€ | Screener-Exception
- [[RMS]] — Hermès International | DEFCON 🟡 3 | Score 68 | Sparrate 38€ | Non-US | Screener-Exception (ROIC 24% >> WACC)
- [[VEEV]] — Veeva Systems | DEFCON 🟡 3 | Score 74 | Sparrate 38€
- [[SU]] — Schneider Electric | DEFCON 🟡 3 | Score 69 | Sparrate 38€ | Non-US
- [[BRKB]] — Berkshire Hathaway B | DEFCON 🟡 3 | Score 71 | Sparrate 38€ | FLAG ✅ Clean (Insurance Exception) | Q1 FY26 Tag-+1 04.05. (75→71 Codex-R1-Korrektur)
- [[V]] — Visa Inc. | DEFCON 🟠 2 | Score 64 | Sparrate 19€ | FLAG ✅ Clean | Q2 FY26 Beat 28.04. + Codex-Rescoring-Revert (68→64, ROIC-Methodology-Watch Q3)
- [[APH]] — Amphenol Corp. | DEFCON 🟠 2 | Score 61 | 🔴 FLAG (Score-basiert <65) | Sparrate 0€ | Q1 FY26 Tag-+1 30.04. (63→61)
- [[ASML]] — ASML Holding | DEFCON 🟡 3 | Score 68 | Sparrate 38€ | Non-US
- [[TMO]] — Thermo Fisher Scientific | DEFCON 🟡 3 | Score 67 | Sparrate 38€ | Q1 FY26 Forward-Vollanalyse 23.04. (D2→D3, fcf_trend_neg Resolve-Gate CLEAR)
- [[MSFT]] — Microsoft | DEFCON 🟠 2 | Score 50 | 🔴 CapEx/OCF-FLAG aktiv | Sparrate 0€ | Q3 FY26 Tag-+1 30.04. (59→50, Bull-Case Trigger A✅/B❌/C✅✅ — UND nicht erfüllt)

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
- [[llm-stock-rating|LLM-Based Stock Rating]] — Automatisierte Aktien-Ratings via LLM; schlägt Analysten bei 3–6 Monaten (1 Quelle)
- [[financial-fundamentals-analysis|Financial Fundamentals Analysis]] — Bilanz, GuV, Cashflow-Analyse aus SEC-Filings; stärkste Daten-Modalität für KI-Ratings (1 Quelle)
- [[chain-of-thought-prompting|Chain-of-Thought Prompting]] — Prompting-Technik: LLM denkt Schritt für Schritt; erhöht Qualität und Interpretierbarkeit (1 Quelle)
- [[news-sentiment-analysis|News Sentiment Analysis]] — Sentiment-Scoring von Finanznachrichten; kurzfristig nützlich, mittelfristig Positivitäts-Bias (1 Quelle)
- [[forward-returns-evaluation|Forward Returns Evaluation]] — Quintil-basierte Methode zur Bewertung von Rating-Genauigkeit über verschiedene Zeithorizonte (1 Quelle)
- [[analyst-stock-ratings|Analyst Stock Ratings]] — Traditionelle Wall-Street-Ratings; struktureller 43%-Strong-Buy-Bias; langfristig besser als LLMs (1 Quelle)

### DEFCON-System (Kern-Framework)
- [[DEFCON-System]] — 100-Punkte-Scoring-Matrix; 5 Blöcke; Sparplan-Formel; v3.7 (System-Gap-Release; Skill-Paket v3.7.2 seit 19.04.2026)
- [[CapEx-FLAG]] — Die heilige Regel; 3 Trigger; überschreibt jeden Score
- [[ROIC-vs-WACC]] — Harter Malus wenn ROIC < WACC; 8 Punkte Fundamentals
- [[Analyse-Pipeline]] — Stufe 0 → 1 → 2 → Entscheidung; Skill-Hierarchie
- [[Tariff-Exposure-Regel]] — Post Liberation Day; <15% kein FLAG, >35% FLAG
- [[Non-US-Scoring]] — IFRS-Addendum für ASML/RMS/SU; Insider manuell via AFM/AMF
- [[Score-Archiv]] — Append-only JSONL-Historie aller Score-Records; Basis für 2028+ Backtest (neu 17.04.2026)
- [[FLAG-Event-Log]] — Trigger + Resolution für 4 FLAG-Typen; Quelle für deskriptive Event-Study (neu 17.04.2026)
- [[Backtest-Ready-Infrastructure]] — 5-Layer-Architektur (State/Narrative/History/Projection-Live/Hub) seit Tier-2-Refactor 25.04.2026; §18 v2.1 Trigger-basiertes Sync-Mapping (neu 17.04.2026)

### Wissenschaftliche Fundierung DEFCON
- [[5J-Fundamental-Fenster]] — 5J-Durchschnitt > Spot als Prädiktor; Pflichtperspektive in jeder Analyse
- [[FCF-Primacy]] — FCF-Yield + Fwd P/E primär; trailing P/E nur Kontext (Gu/Kelly/Xiu)
- [[Moat-Taxonomie-Morningstar]] — 8 Moat-Quellen-Checkliste; Wide Moat + Fundamentals = Alpha
- [[Buffett-Faktorlogik]] — cheap+safe+quality Dreiklang; Float-Leverage nicht replizierbar
- [[QMJ-Faktor]] — Quality Minus Junk; erklärt Buffetts Alpha vollständig
- [[F-Score-Quality-Signal]] — Piotroski 9-Kriterien-Score; ≥7 → +2 Pt. Fundamentals-Bonus (B12) ← NEU
- [[Gross-Profitability-Premium]] — Novy-Marx GP/TA; eigenständiger Renditefaktor, +2 Pt. Fundamentals-Metrik (B13) ← NEU
- [[Accruals-Anomalie-Sloan]] — Sloan 1996; Low-Accrual outperformt +10,4% p.a.; validiert v3.5-Schwellen (B14) ← NEU
- [[Insider-Trading-Primary-Signal]] — Insider-Block-Konzept-Anker; Buy>Sell-Asymmetrie + Form-4-X/M-Filter via OpenInsider; primär aus Lakonishok/Lee 2001 (B26) ← NEU 2026-04-26 Phase B
- [[Earnings-Foreknowledge-Window]] — Insider-Verkaufs-Window Q-9 bis Q-3 vor Earnings-Break (Legal-Jeopardy-Avoidance); Architektur-Anker für insider-intelligence v2 (B27 design-context) ← NEU 2026-04-26 Phase B
- [[Media-Pessimism-Sentiment]] — Tetlock 2007 Mean-Reversion-Anker; hohe Media-Pessimism → kurzfrist Drawdown + komplette Reversion zu Fundamentals 5-10 Tage; ankert Sentiment-Block-Architektur (B28 design-context) ← NEU 2026-04-26 Phase B
- [[Noise-Trader-Model]] — Liquidity-Trader-Modell zu Tetlock 2007 Volume-Pattern (Absolut-Wert); ergänzt B28-Architektur ← NEU 2026-04-26 Phase B
- [[Competitive-Advantage-Period]] — Mauboussin/Callahan 2024 CAP-Konzept; zweite Moat-Dimension neben ROIC-WACC-Spread (Magnitude × Sustainability) ← NEU 2026-04-26 Phase B

### Backtest-Validation-Framework (§29 Gate — FUTURE-ACTIVATION 2028-04-01)
- [[PBO-Backtest-Overfitting]] — Bailey PBO/CSCV-Methode; §29.1 Methoden-Gate (B15) ← NEU 2026-04-19
- [[Factor-Investing-Framework]] — AQR 4-Faktor-Kanon + DEFCON-Mapping; §29.2 External-Bench + §29.4 t-Stat≥3 (B16) ← NEU 2026-04-19
- [[Factor-Information-Decay]] — Flint/Vermaak Half-Life pro Faktor; §29.3 Cadence-Check (B17) ← NEU 2026-04-19
- [[Seven-Sins-Backtesting]] — Palomar Sünden-Katalog; §29.5 Pre-Flight-Gate (Sin #7 n.a. Long-Only) (B18) ← NEU 2026-04-19
- [[Palomar-Methods-Reference]] — Palomar Ch 6 + 8.3-8.5 + 7.5 + 11 konsolidierte Methoden-Referenz ← NEU 2026-04-19
- [[LLM-Investing-Bias-Audit]] — FINSABER-Pattern (Survivorship/Look-Ahead/Data-Snooping) für DEFCON-Self-Audit (B19) ← NEU 2026-04-20
- [[Regime-Aware-LLM-Failure-Modes]] — FINSABER Bull/Bear-Asymmetrie; Anker für Track 5b FRED Regime-Filter (B19) ← NEU 2026-04-20
- [[Composite-Anti-Overfitting-Objective]] — GT-Score-Pattern (in-the-loop); Tie-Break R0 für Track 5b Grid-Search (B20) ← NEU 2026-04-20
- [[Post-Publication-Decay]] — McLean/Pontiff 2016 §29.7 M&P-Discount; in-sample-Claim × 0,42 als Plausibility-Test post-publication (B25 meta-gate) ← NEU 2026-04-26 Phase B

### KG-/RAG-/LLM-Architektur (Phase 1b 6-Paper-Ingest — 2026-04-20)
- [[Knowledge-Graph-Finance-Architecture]] — Schema-guided KG-Primitive für SEC-Filings; 5-Tuple + 10 Entity-Types + 10 Relation-Types (B21) ← NEU 2026-04-20 Phase 1b
- [[Agentic-Reflection-Pattern]] — Critic-Corrector-Loop, +22,5pp All-Rules-Compliance; generisches Multi-Agent-Muster (B21) ← NEU 2026-04-20 Phase 1b
- [[LLM-as-a-Judge-Evaluation]] — Ground-truth-agnostic Evaluation; 4 Dimensionen + 3-Vote-Consensus (B21) ← NEU 2026-04-20 Phase 1b
- [[RAG-Uncertainty-Quantification]] — Bayesian-RAG-Pattern via MC-Dropout; epistemische Unsicherheit $S_i = \mu_i - \lambda \sigma_i$ (B23) ← NEU 2026-04-20 Phase 1b
- [[LLM-Preference-Optimization-Finance]] — DPO statt SFT für Finance-LLMs; +11% F1 vs. FinGPT v3.3 (B24) ← NEU 2026-04-20 Phase 1b
- [[Sentiment-Strength-Logit-Extraction]] — Kontinuierliche Sentiment-Scores aus causal-LLM-Logits; Long-Short-Enabler (B24) ← NEU 2026-04-20 Phase 1b

### Token-Effizienz & System
- [[STATE]] — Hub: Verweise + Critical-Alerts + Last-Audit (~40 Z, Vault-Stub für `00_Core/STATE.md`, seit Tier-2-Hub-Split 25.04.2026)
- [[PORTFOLIO]] — Live-State: 11 Satelliten Scores/DEFCON/FLAGs/Sparraten + 30-Tage-Trigger (Vault-Stub für `00_Core/PORTFOLIO.md`, default-load bei Session-Start)
- [[PIPELINE]] — Pipeline-SSoT + Long-Term-Gates (Vault-Stub für `00_Core/PIPELINE.md`)
- [[SYSTEM]] — System-Zustand + Infrastruktur: DEFCON-Version, MCP, Briefing, Backtest, R5, §30, Backlog (Vault-Stub für `00_Core/SYSTEM.md`)
- [[CORE-MEMORY]] — Live-Gedächtnis: Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13) (Vault-Stub für `00_Core/CORE-MEMORY.md`)
- [[Faktortabelle]] — Score-Detail pro Ticker (Vault-Stub für `00_Core/Faktortabelle.md`)
- [[Token-Mechanik]] — Strukturiertes Token-Management; Snapshot-First, MCP-Minimalset
- [[Context-Hygiene]] — On-demand Loading; Compact-Regeln; MCP-Session-Typen
- [[CLAUDE-md-Konstitution]] — CLAUDE.md als Wahrheitsquelle; Hub+PORTFOLIO Default-Load; Routing-Table-Trigger (Tier-1 24.04. + Tier-2 25.04.2026)
- [[Context-Hygiene-Code]] — Claude Code-spezifisch: autoCompact 75%, Tool Search, Deny Rules
- [[Update-Klassen-DEFCON]] — A/B/C/D Klassen; Klasse-C-Priorität (Event-getriggert, sofort)
- [[Faktortabelle-Architektur]] — Snapshot-First; config.yaml → Faktortabelle → API; ~60-70% Token-Einsparung
- [[Session-Start-Protokoll]] — Hub (STATE.md) + PORTFOLIO.md Default-Load; ersetzt 4-Datei-Auto-Read (~80% Token-Einsparung, seit 17.04.2026 STATE-First; Tier-2-Hub-Split 25.04.2026)
- [[INSTRUKTIONEN-SKILL-Trennung]] — Post-Dedup Arbeitsteilung: User-Workflow (INSTRUKTIONEN) vs. Scoring-Technik (SKILL); 587→452 Zeilen, 10 Cross-Refs, seit 17.04.2026

### Depot-Struktur & Planung
- [[etf-core|ETF-Core]] — 65% des Sparplans (617,50€/Monat); IWDA, EIMI, EXUSA, AVGC, EWG2
- [[steuer-architektur|Steuer-Architektur]] — Lombardkredit, FIFO-Klon, 10-Jahres-Kaskade, PKV-Wäsche; Zeithorizont 2058

---

## Synthesis
*Cross-source analyses and evolving theses.*

- [[ai-in-investment-analysis|AI in Investment Analysis]] — Zentrale Synthese: KI in Aktienanalyse, Depot-Strategie, Trading; wächst mit jeder neuen Quelle
- [[Investing-Mastermind-Index]] — Zentraler Navigationsindex: Depot-State, Satelliten, Konzepte, Skills
- [[Depot-State-April-2026]] — Monatlicher Snapshot; Sparplan-Verteilung; offene Entscheidungen
- [[Wissenschaftliche-Fundierung-DEFCON]] — 28-Befunde-Matrix: 34 Paper → operative Konsequenzen für DEFCON v3.7; Status-Matrix mit 6 Labels (active-scoring, active-scoring-validation, design-context, meta-gate, design-rejected, future-arch); §29-Validation-Gate-Framework inkl. §29.7 M&P-Discount (Phase A+B+C 26-27.04.2026)
- [[Backtest-Methodik-Roadmap]] — Entscheidungsmatrix für 2028-Review; Options A–D je nach Datenlage; welcher Paper als Benchmark wann anlegbar (neu 17.04.2026)
- [[Knowledge-Graph-Architektur-Roadmap]] — v0.1 `draft-frozen` (Codex-Verdikt Option D, 20.04.2026 Nacht-Spät): Entscheidungsvorlage KG/RAG vs. XML-Direkt-Parsing für insider-intelligence + zukünftige Skills; 3 Qualitäts-Gates + 3 Szenarien (Form-4-XML bleibt / 10-K-KG DEFER 2027+ / Bayesian-RAG-Briefing verworfen). Re-Review-Trigger: Cross-Entity-Bedarf ODER 2026-10-17 Score-Archiv-Interim-Gate.

---

## Queries
*Saved responses to notable questions.*

*(none yet)*
