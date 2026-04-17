# Wiki Index

> Content catalog. Updated on every ingest, query save, or structural edit.
> Last updated: 2026-04-17 (Foundation-Papers-Integration v4.3 — 82 Notes: 76 wiki + 6 raw)
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

### Datenquellen-APIs
- [[defeatbeta]] — US-Fundamentals (Primär): Income, Cash Flow, ROIC, WACC, Geographic Revenue
- [[Shibui-SQL]] — Technicals + historische Breite + FLAG-Historik (56+ Indikatoren)
- [[OpenInsider]] — Insider-Pflichtquelle; Form-4-Verifikation (Spalte "X"/"M")

### Skills & Module (Operative Tools)
- [[dynastie-depot-skill]] — DEFCON v3.4 Monolith; alle Workflows (!Analysiere, !Rebalancing, !QuickCheck, !CAPEX-FCF-ANALYSIS)
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

### Satelliten (aktive Positionen)
- [[AVGO]] — Broadcom Inc. | DEFCON 🟢 4 | Score 86 | Kalibrierungsanker #1
- [[COST]] — Costco Wholesale | DEFCON 🟢 4 | Score 69
- [[RMS]] — Hermès International | DEFCON 🟢 4 | Score 69 | Non-US | Screener-Exception (ROIC 24% >> WACC)
- [[VEEV]] — Veeva Systems | DEFCON 🟢 4 | Score 74
- [[SU]] — Schneider Electric | DEFCON 🟢 4 | Score 71 | Non-US
- [[BRKB]] — Berkshire Hathaway B | DEFCON 🟢 4 | Score 75
- [[V]] — Visa Inc. | DEFCON 🟢 4 | Score 86
- [[APH]] — Amphenol Corp. | DEFCON 🟡 3 | Score 61 | 🔴 FLAG (Score-basiert)
- [[ASML]] — ASML Holding | DEFCON 🟡 3 | Score 68 | Non-US
- [[TMO]] — Thermo Fisher Scientific | DEFCON 🟡 3 | Score 67 | Q1 Earnings 23.04.
- [[MSFT]] — Microsoft | DEFCON 🟠 2 | Score 60 | 🔴 CapEx-FLAG | Q3 Earnings 29.04.

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
- [[DEFCON-System]] — 100-Punkte-Scoring-Matrix; 5 Blöcke; Sparplan-Formel; v3.4
- [[CapEx-FLAG]] — Die heilige Regel; 3 Trigger; überschreibt jeden Score
- [[ROIC-vs-WACC]] — Harter Malus wenn ROIC < WACC; 8 Punkte Fundamentals
- [[Analyse-Pipeline]] — Stufe 0 → 1 → 2 → Entscheidung; Skill-Hierarchie
- [[Tariff-Exposure-Regel]] — Post Liberation Day; <15% kein FLAG, >35% FLAG
- [[Non-US-Scoring]] — IFRS-Addendum für ASML/RMS/SU; Insider manuell via AFM/AMF

### Wissenschaftliche Fundierung DEFCON
- [[5J-Fundamental-Fenster]] — 5J-Durchschnitt > Spot als Prädiktor; Pflichtperspektive in jeder Analyse
- [[FCF-Primacy]] — FCF-Yield + Fwd P/E primär; trailing P/E nur Kontext (Gu/Kelly/Xiu)
- [[Moat-Taxonomie-Morningstar]] — 8 Moat-Quellen-Checkliste; Wide Moat + Fundamentals = Alpha
- [[Buffett-Faktorlogik]] — cheap+safe+quality Dreiklang; Float-Leverage nicht replizierbar
- [[QMJ-Faktor]] — Quality Minus Junk; erklärt Buffetts Alpha vollständig
- [[F-Score-Quality-Signal]] — Piotroski 9-Kriterien-Score; ≥7 → +2 Pt. Fundamentals-Bonus (B12) ← NEU
- [[Gross-Profitability-Premium]] — Novy-Marx GP/TA; eigenständiger Renditefaktor, +2 Pt. Fundamentals-Metrik (B13) ← NEU
- [[Accruals-Anomalie-Sloan]] — Sloan 1996; Low-Accrual outperformt +10,4% p.a.; validiert v3.5-Schwellen (B14) ← NEU

### Token-Effizienz & System
- [[Token-Mechanik]] — Strukturiertes Token-Management; Snapshot-First, MCP-Minimalset
- [[Context-Hygiene]] — On-demand Loading; Compact-Regeln; MCP-Session-Typen
- [[CLAUDE-md-Konstitution]] — CLAUDE.md als Wahrheitsquelle; 4 Pflicht-Lektüren; Trigger-Liste
- [[Context-Hygiene-Code]] — Claude Code-spezifisch: autoCompact 75%, Tool Search, Deny Rules
- [[Update-Klassen-DEFCON]] — A/B/C/D Klassen; Klasse-C-Priorität (Event-getriggert, sofort)
- [[Faktortabelle-Architektur]] — Snapshot-First; config.yaml → Faktortabelle → API; ~60-70% Token-Einsparung

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

---

## Queries
*Saved responses to notable questions.*

*(none yet)*
