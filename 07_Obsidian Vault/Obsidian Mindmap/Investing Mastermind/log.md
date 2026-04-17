# Wiki Log

> Append-only activity log. Most recent entries at the bottom.
> Format: `## [YYYY-MM-DD] operation | Description`

---

## [2026-04-09] setup | Wiki initialized
- Created directory structure: raw/, pages/entities/, pages/concepts/, pages/sources/, pages/synthesis/, pages/queries/
- Created CLAUDE.md (schema), index.md (catalog), log.md (this file)
- Pages created: none (fresh wiki)
- Pages updated: none

## [2026-04-10] setup | Claude Stuff Integration — Skills, Konzepte, Verlinkungen
- Integrationsquelle: `C:\Users\tobia\OneDrive\Desktop\Claude Stuff\` (00_Core, 01_Skills)
- Neue Source-Seiten: [[quick-screener]], [[insider-intelligence]], [[non-us-fundamentals]], [[dynastie-depot-skill]]
- Neue Concept-Seiten: [[ETF-Core]], [[Steuer-Architektur]]
- Aktualisierte Seiten: [[Analyse-Pipeline]], [[DEFCON-System]], [[AI in Investment Analysis]], [[Investing-Mastermind-Index]], [[index.md]]
- Gesamt: 6 neue Seiten, 5 aktualisierte Seiten — alle Skill/Tool-Seiten mit DEFCON-Konzepten verknüpft

## [2026-04-10] ingest | LLMs for Equity Stock Ratings (J.P. Morgan, ICAIF 2024)
- Quelle: arXiv 2411.00856 — PDF in raw/ abgelegt
- Kernthese: GPT-4 ohne Fine-Tuning schlägt Wall-Street-Analysten bei 3–12-Monats-Aktien-Ratings; Fundamentaldaten sind stärkste Daten-Modalität (MAE 1.417 mit Fundamentals+Sentiment vs. 1.570 Analysten)
- Pages created: [[LLMs for Equity Stock Ratings]], [[J.P. Morgan AI Research]], [[GPT-4]], [[S&P 500]], [[LLM-Based Stock Rating]], [[Financial Fundamentals Analysis]], [[Chain-of-Thought Prompting]], [[News Sentiment Analysis]], [[Forward Returns Evaluation]], [[Analyst Stock Ratings]], [[AI in Investment Analysis]]
- Pages updated: [[index.md]], [[log.md]]
- Gesamt: 11 neue Seiten

## [2026-04-10] earnings-preview | ASML Q1 2026
- Berichtstag: 15.04.2026
- EPS-Konsensus: $6,64 (+10,6% YoY) | Revenue: $8,65B (+11,8% YoY)
- Sentiment: 84% bullish (44 Analysten) | PT-Median $1.593
- Key Watch: High-NA Ramp + China-Exposure (aktuell 24%, FLAG-Schwelle 35%)
- Pages updated: [[ASML]] — Earnings Preview Block + Analyse-Historie-Eintrag 10.04.2026

## [2026-04-10] link | Querverbindungen JPM-Research ↔ DEFCON-Konzepte gezogen
- Lücke geschlossen: [[Chain-of-Thought Prompting]] und [[LLM-Based Stock Rating]] waren nicht mit [[DEFCON-System]] / [[Analyse-Pipeline]] / [[dynastie-depot-skill]] verbunden
- Pages updated (Frontmatter `related:` + neue Body-Sections):
  - [[Chain-of-Thought Prompting]] — Abschnitt "Umsetzung im Dynastie-Depot" + Links zu DEFCON-System, Analyse-Pipeline, dynasty-depot-skill
  - [[LLM-Based Stock Rating]] — Abschnitt "Umsetzung im Dynastie-Depot" mit Mapping-Tabelle + selbe Links
  - [[DEFCON-System]] — Verlinkungen ergänzt: CoT, LLM-Stock-Rating, AI in Investment Analysis
  - [[Analyse-Pipeline]] — Verlinkungen ergänzt: CoT, LLM-Stock-Rating
  - [[AI in Investment Analysis]] — Frontmatter `related:` um DEFCON-System, Analyse-Pipeline, dynasty-depot-skill erweitert
- Gesamt: 0 neue Seiten, 5 aktualisierte Seiten

## [2026-04-14] ingest | Wissenschaftliche Fundierung + Token-Effizienz

### Neue Dateien erstellt (15)

**wiki/sources/ (4):**
- [[arXiv-1711.04837]] — ML + 5J-Fundamental-Fenster (Gu/Kelly/Xiu)
- [[Gu-Kelly-Xiu-2020]] — FCF-Primacy, trailing P/E, forward P/E (RFS 2020)
- [[Morningstar-Wide-Moat]] — 8 Moat-Quellen, Wide Moat Whitepaper
- [[Buffetts-Alpha]] — QMJ+BAB+Value, Float-Leverage, cheap+safe+quality (AQR 2018)

**wiki/concepts/ — Paper-Konzepte (5):**
- [[5J-Fundamental-Fenster]], [[FCF-Primacy]], [[Moat-Taxonomie-Morningstar]]
- [[Buffett-Faktorlogik]], [[QMJ-Faktor]]

**wiki/concepts/ — Token-Effizienz (5):**
- [[Token-Mechanik]], [[Context-Hygiene]], [[CLAUDE-md-Konstitution]]
- [[Context-Hygiene-Code]], [[Update-Klassen-DEFCON]]

**wiki/synthesis/ (1):**
- [[Wissenschaftliche-Fundierung-DEFCON]] — 7-Befunde-Matrix, vollständig vernetzt

### Aktualisierte Dateien (16)

**wiki/entities/satelliten/ (11):** Alle 11 Satelliten-Seiten mit `related_concepts` + `## Wissenschaftliche Basis`
- ASML, AVGO, MSFT, RMS, VEEV, SU, BRKB (+ Buffett-Quellen), V, APH, COST, TMO

**System-Dateien (5):**
- CLAUDE.md — Faktortabelle als 4. Pflicht-Lektüre; Wiki-Trigger erweitert; Token-Kurzreferenz; MCP-Check; Applied Learning
- index.md — 45 → 60 Notes; alle neuen Seiten katalogisiert
- log.md — dieser Eintrag
- 00_Core/CORE-MEMORY.md — Milestone-Eintrag

### Backlink-Vernetzung
Vollständig bidirektional:
- 4 Paper → 5 Konzepte → 1 Synthese → 11 Entities
- Alle Pflicht-Regeln (trailing P/E, Float-Leverage) in betroffenen Dateien dokumentiert

## [2026-04-14] setup | Faktortabelle + Insider-Schnittstelle (Prompt 2)
- Neu: `00_Core/Faktortabelle.md` — Snapshot-First mit `<!-- DATA:TICKER -->` Kommentar-Ankern
- Neu: `wiki/concepts/Faktortabelle-Architektur.md` — Konzeptseite mit Datenhierarchie + 3 Arbeitsbereiche
- Update: `insider_intel.py` — `--update-faktortabelle` Parameter + `factor-sync` 3-Wege-Vergleich
- Update: `insider-intelligence/SKILL.md` — Snapshot-First Workflow + Vault-Integration
- Fix: COST CIK `0000723254` → `0000909832` in `dynastie-depot/SKILL.md`
- Fix: EODHD-Hinweis → yfinance-Hinweis in `dynastie-depot/SKILL.md`
- Update: `index.md` — 60 → 61 Notes

## [2026-04-14] lint | Vault-Audit — Orphans, Broken Links, Cross-Links, Frontmatter

### Runde 1: Orphan-Fix
- **Problem:** 7 isolierte Knoten im Obsidian-Graph (3 Raw-Dateien, 4 Autoren-Namen, WIKI-SCHEMA)
- Pages created: [[Dominik Wolff]], [[Fabian Echterling]], [[Aakanksha Jadhav]], [[Vishal Mirza]]
- Pages updated: [[LLMs for Equity Stock Ratings]], [[AI in Investment Analysis]], [[index.md]]

### Runde 2: Vollständiges Audit
- **Backslash-Typos gefixt:** `[[BRKB\|BRK.B]]` → `[[BRKB|BRK.B]]` in [[Investing-Mastermind-Index]], [[Depot-State-April-2026]]
- **Fehlende Ersatzbank-Seiten erstellt (6):** [[MKL]], [[NVDA]], [[SNPS]], [[RACE]], [[DE]], [[SPGI]]
- **DEFCON Cross-Links ergänzt:** Alle 6 Konzeptseiten (CapEx-FLAG, ROIC-vs-WACC, Tariff-Exposure, Non-US-Scoring, Analyse-Pipeline, Update-Klassen) jetzt bidirektional vernetzt
- **Frontmatter standardisiert:** title, type, created, updated, sources, related für alle DEFCON-Konzeptseiten
- Pages created: 10 neue Seiten (4 Autoren + 6 Ersatzbank)
- Pages updated: 11 Seiten (2 Typo-Fix + 3 Orphan-Links + 6 DEFCON Cross-Links/Frontmatter)
- Gesamt: 61 → 71 Notes

## [2026-04-15] edit | System-Integration v4.0 (Cowork-Session)
- Update: SKILL.md v4.0 (15 Regeln, 4 Blöcke: Datenabruf, Early-Exit, Output-Hygiene, Session-Management + Snapshot-First Schritt 0)
- Update: INSTRUKTIONEN.md v1.4 (6 neue Blöcke: Sync-Pflicht, Update-Klassen, Ersatzbank-Aktivierung, Non-US Kurzreferenz, Sparplan-Formel, Tariff Scoring)
- Update: CLAUDE.md (MCP-Session-Check, Token-Effizienz 6 Bullets, Applied Learning, Wiki-Trigger erweitert)
- Update: CORE-MEMORY.md v1.5 (Scores sync: APH 61/FLAG, RMS 71, VEEV 74; Meilensteine; Sparplan-Formel)
- Update: settings.json (BASH 150k, Deny Rules für .obsidian/node_modules/dist/.git)
- Update: [[Context-Hygiene-Code]] (settings.json Wirkungsbereiche korrigiert — autoCompact existiert nicht im Schema)
- Quelle: Chat 09./10./13./15.04.2026

## [2026-04-15] analysis | V (Visa) DEFCON v3.4 Vollanalyse

- **Score:** 86/100 | **DEFCON:** 🟢 4 | **FLAG:** ✅ Kein FLAG
- **Kurs:** ~$309 | **Market Cap:** ~$593B | **FY:** Sep 2025
- **Datenquellen:** defeatbeta (Cash Flow, Balance Sheet, Income Statement, ROIC, WACC, Gross Margin), insider_intel.py (Form 4 SEC EDGAR), StockAnalysis (Quarterly CapEx/OCF, P/FCF, FCF Yield), WebSearch (Kurs, Analyst-Konsensus, Q1 FY26 Earnings, EPS-Revisionen)
- **Fundamentals 44/50:** CapEx/OCF ~6% (Fabless-Niveau, 9/9), FCF $21.6B FY25, GM ~80% stabil, Net Debt/EBITDA 0.31x exzellent. Schwäche: ROIC ~9.9% GAAP knapp unter WACC ~10.5% (Goodwill-Verzerrung Visa-Europe $19.9B), Fwd PE 23.35x / P/FCF 25.88x im mittleren Bewertungsbereich.
- **Moat 19/20:** GuruFocus Moat Score 9/10 Wide. 4 überlappende Quellen: Netzwerkeffekte (dominant), Intangible Assets, Switching Costs, Efficient Scale. +1 Pricing Power (VAS +28% Q1 FY26 bestätigt).
- **Technicals 7/10:** -17.6% vom ATH $375 (Jun 2025). PT-Upside +28–29%. Kurs unter fallendem 200MA ($330) → 1/3 Trend-Score.
- **Insider 6/10:** Diskr. 90d nur $201K (kein FLAG). Plan-Verkäufe $24.6M (10b5-1 plankonform, Lloyd Carney). Ownership strukturell trivial (<0.1% MC) bei Mega-Cap → 0/3.
- **Sentiment 10/10:** 37 Buy / 3 Hold / 0 Sell. Zacks: 1 Aufwärtsrevision / 0 Abwärts. -1 PT-Dispersion ($323–450, 32% Spread).
- **Sparplan:** Voll aktiv (DEFCON 4 × $35.63/Monat).
- **Nächste Aktion:** Q2 FY26 Earnings ~22.04.2026 → QuickCheck.
- **Sync:** CORE-MEMORY.md (Meilenstein + Score-Register) + Faktortabelle.md (V-Zeile aktualisiert, Offene Scores 6→5/11) + log.md (dieser Eintrag)

## [2026-04-15] analysis | COST (Costco) DEFCON v3.4 Vollanalyse

- **Score:** 69/100 | **DEFCON:** 🟢 4 (Bestandsposition) | **FLAG:** ✅ Kein FLAG
- **Kurs:** ~$940 | **Market Cap:** ~$416B | **FY:** Aug 2025
- **Datenquellen:** defeatbeta (Cash Flow, Balance Sheet, Income Statement, ROIC, WACC), insider_intel.py (Form 4 SEC EDGAR), WebSearch (Kurs, Moat-Score, Analyst-Konsensus)
- **Screener-Exception:** GAAP-ROIC 5.6% (strukturell niedrig durch niedriges Book Value). Membership Yield $5.3B / IC $34.9B = **15.2%** > WACC 12.3% — echter ökonomischer Return-Motor. Kein ROIC-FLAG; dokumentiert als Ausnahme.
- **Fundamentals 29/50:** P/FCF ~53x (teuer), FCF Yield 1.88%, Fwd PE ~51x (Bewertungs-Malus). CapEx/OCF 21.3% ausgezeichnet. Bilanz solide (Net Debt/EBITDA <1x). FCF $7.2B FY2025.
- **Moat 19/20:** GuruFocus 9/10 Wide. Membership-Loyalty unübertroffen — Renewal Rate 93%. Pricing Power durch Low-Cost-Operator-Position strukturell gesichert.
- **Technicals 5/10:** Moderate Distanz vom ATH. 22 Analysten PT Upside ~+15%.
- **Insider 8/10:** CEO/Insider-Käufe bekannt. Kein FLAG-Selling.
- **Sentiment 8/10:** Strong Buy-Konsens, 0% Sell.
- **Sparplan:** Voll aktiv (DEFCON 4 × $35.63/Monat).
- **Nächste Aktion:** Q1 FY27 Earnings ~Dez 2026.
- **Sync:** CORE-MEMORY.md + Faktortabelle.md + log.md

## [2026-04-15] analysis | BRK.B (Berkshire Hathaway) DEFCON v3.4 Vollanalyse

- **Score:** 75/100 | **DEFCON:** 🟢 4 | **FLAG:** ✅ Kein FLAG
- **Kurs:** ~$480 | **ATH:** $539.80 (Mai 2025) | **Market Cap:** ~$1.04T
- **Datenquellen:** defeatbeta (Cash Flow, Balance Sheet, Annual CF), insider_intel.py (SEC EDGAR Form 4, CIK 0001067983), WebSearch (Kurs, ATH, Book Value, Float, Analyst PT)
- **Screener-Exception:** P/B 1.44x statt P/FCF (Versicherung/Holdings). Float $686B als zinsloses Fremdkapital → ROIC-Verzerrung strukturell.
- **Fundamentals 35/50:** P/B 1.44x (historische Buyback-Zone <1.5x). Book Value CAGR +10% p.a. 5J ($443B→$717B). Interest Income $39.98B FY25 (T-Bill Float-Ertrag). Netto-Cash-Position ~$344B. CapEx/OCF 45.6% (BNSF Railroad + BHE Utilities, kein FLAG). Goodwill 6.8% = kein Malus.
- **Moat 19/20:** Float-Leverage einzigartig, BNSF Efficient Scale (Railroad-Duopol), 60J Capital-Allocation-Track-Record. –1 Nachfolge-Risiko Greg Abel.
- **Technicals 4/10:** -11.1% vom ATH, unter 200D-MA, limitierter PT-Upside ~+13.5%.
- **Insider 9/10:** Greg Abel Open-Market-Käufe $15.3M (90d) — starkes Alignment-Signal (Net Buy 4/4). Kein diskretionäres Selling $0 (3/3). Buffett ~15% Ownership strukturell.
- **Sentiment 8/10:** Strong Buy-Konsens, 0% Sell, 22 Analysten.
- **Score-Korrektur:** 73→75 nach korrektem insider_intel.py-Aufruf (`BRK.B` statt `BRK-B`).
- **Sparplan:** Voll aktiv (DEFCON 4 × Sparrate).
- **Nächste Aktion:** Q-Earnings Mai 2026 — Buyback-Wiederaufnahme bei Kurs <$480 (P/B <1.5x).
- **Sync:** CORE-MEMORY.md + Faktortabelle.md + log.md

## [2026-04-15] analysis | SU (Schneider Electric) DEFCON v3.4 Vollanalyse

- **Score:** 71/100 | **DEFCON:** 🟢 4 | **FLAG:** ✅ Kein FLAG
- **Kurs:** €267.55 | **Market Cap:** €150.4B | **Börse:** Paris (SU.PA)
- **Datenquellen:** eodhd_intel.py / yfinance (Non-US Fundamentals Module), WebSearch (ROIC GuruFocus, Analyst-Konsensus)
- **Fundamentals 31/50:** ROIC 10.48% > WACC 8.96% (positiver Spread ~+1.5-2%). CapEx/OCF 25.2% (4J stabil 23–25%, ausgezeichnet). FCF-Wachstum +41% in 3J (€3.26B→€4.59B). P/FCF 37.7x (teuer), FCF Yield 2.65% (niedrig). Goodwill 40.2% (AVEVA M&A 2023, –Malus). Net Debt/EBITDA 2.51x (akzeptabel). GM-Trend stabil ~42%.
- **Moat 16/20:** Narrow/Wide (Morningstar Narrow). EcoStruxure IoT-Plattform Switching Costs, Intangible Assets (Marke #1 Energiemanagement), Efficient Scale (Rechenzentrum-Boom). Kein GuruFocus Wide Moat direkt verifiziert.
- **Technicals 8/10:** +12.6% über 200D-MA (einziger Satellit über 200MA ✅). -4.5% vom 52W-Hoch. PT Ø €294.45 (+10.1%).
- **Insider 7/10:** 3.39% Ownership (über 1%-Schwelle). AMF manuell unverified — konservativ.
- **Sentiment 9/10:** 22 Analysten Strong Buy, 0% Sell.
- **Sparplan:** Voll aktiv (DEFCON 4 × Sparrate).
- **Nächste Aktion:** H1 2026 Earnings Juli/Aug 2026.
- **Meilenstein:** Alle 11 Satelliten vollständig gescort — offene Scores: 0/11 ✅
- **Sync:** CORE-MEMORY.md + Faktortabelle.md + log.md

## [2026-04-15] edit | Vault-Sync — Satelliten-Scores nach Vollanalysen aktualisiert
- **Anlass:** V, COST, BRK.B, SU hatten noch Platzhalter-Scores (~80) und altes Analyse-Datum (2026-03-01) trotz abgeschlossener DEFCON v3.4 Vollanalysen
- Pages updated: [[V]] (80→86), [[COST]] (80→69), [[BRKB]] (80→75), [[SU]] (80→71)
- Alle 4 Seiten: Frontmatter (score, datum, trigger) + neuer Analyse-Ergebnis-Block mit Score-Tabelle
- [[index.md]] — Score-Angaben bei allen 4 Satelliten korrigiert
- Gesamt: 0 neue Seiten, 5 aktualisierte Seiten

## [2026-04-15] earnings-recap | RMS (Hermès) Q1 2026

- **Trigger:** Q1 2026 Revenue-Veröffentlichung 15.04.2026 — enttäuschende Zahlen
- **Resultat:** €4,07B (+6% CER, −1% reported). Konsens-Erwartung: +7–8% CER. Minimal-Beat auf absolute Zahl (+0,5%) aber Wachstumsmiss.
- **Kursreaktion:** **−8,4%** (€1.783 → €1.632,50). Intraday 52W-Tief: €1.529. Gesamtmarkt-Selloff Luxury-Sektor (LVMH, Kering ebenfalls schwach).
- **Treiber:** Mittlerer Osten −6% (Iran-Krieg, UAE Mall Traffic −40% März), FX-Headwind €290M, China Asien ex Japan +2%.
- **Positiv:** Leder & Sattlerwaren +9% (Kernmoat intakt), Americas/Japan/Europa ex FR zweistellig.
- **FY 2025 Kontext:** Revenue €16,0B (+5,5%), Net Income €4,52B (leicht rückläufig vs. €4,60B FY2024, EPS −1,6%).
- **Insider:** Co-Chairman Henri-Louis Bauer kaufte €4,99M (12.03.2026), Gesamt-Insider-Net-Buy 90d: +€7,67M.

## [2026-04-15] analysis | RMS (Hermès) DEFCON v3.4 Re-Analyse

- **Score:** 71 → **69** (−2 Punkte) | **DEFCON:** 🟢 4 (Bestandsposition) | **FLAG:** ✅ Kein FLAG
- **Kurs:** €1.632,50 | **Market Cap:** €171,1B | **Börse:** Euronext Paris (RMS.PA)
- **Datenquellen:** yfinance / earnings-recap-skill (Revenue, FCF, Margins), WebSearch (Analyst-Konsensus, Insider AMF, AlphaSpread DCF, Q1 Details)
- **Fundamentals 29/50:** Fwd P/E 30,7x (2/8), P/FCF ~37x (1/8), Bilanz 8/9 (Netto-Cash €9,89B, Goodwill minimal), CapEx/OCF ~25% 7/9 (kein FLAG), ROIC 24,2% >> WACC 6,52% (8/8 Maximal), FCF Yield ~2,7% (3/8). SBC 0,83% — kein Abzug. Accruals negativ (gut).
- **Moat 19/20:** Wide Moat strukturell unberührt. 4 Quellen: Brand/Intangibles, künstliche Verknappung, vertikale Integration, Familienkontrolle. GM >71% (Best-in-class). Leder +9% = Moat-Bestätigung.
- **Technicals 6/10:** ATH-Abstand −37,4% (3/4), Ø PT ~€2.448 = +50% Upside (3/3), Kurs unter fallendem 200MA — neues 52W-Tief (0/3). AlphaSpread DCF Base €1.197 — Kurs drüber, kein Bonus.
- **Insider 8/10:** Net Buy €7,67M (90d, AMF), Co-Chairman Bauer €4,99M. Familienkontrolle 67% (3/3). AMF nicht vollständig verifiziert → konservativ (2/3).
- **Sentiment 7/10:** 14 Buy/3 SB/7 Hold/1 SS. PT-Dispersion 34% (−1 Punkt).
- **Score-Änderung:** −2 Punkte vs. 09.04.2026 (Technicals schwächer, PT-Dispersion höher nach Kursrückgang).
- **Sparplan:** Voll aktiv — keine Änderung. DEFCON 4 Bestandsposition ≥65.
- **Nächste Aktion:** H1 2026 Earnings Juli/Aug 2026 — Mittlerer Osten Recovery + China-Trend.
- **Sync:** CORE-MEMORY.md (Meilenstein + Score-Register) + Faktortabelle.md (Score 71→69, Datum aktualisiert) + log.md (dieser Eintrag)

## [2026-04-15] analysis | APH Tariff-Check abgeschlossen
- Trigger: Offener APH-FLAG-Posten aus Analyse 09.04.2026 (Tariff-Exposure CN/MY)
- Datenquellen: defeatbeta (Geography — kein API-Output), Earnings Release FY2025, Q1 FY2025 Transcript (23.04.2025)
- Befund Revenue: China FY2025 = 14.7% ($4.58B / $31.1B) — unter 15%-Notiz-Schwelle. Trend: 23% (2023) → 14.7% (2025) strukturell rückläufig.
- Befund Supply-Chain: Produktionsstandorte CN/MY durch CEO Adam Norwitt bestätigt (Q1 2025 Call). Kombinierte Exposure ~17–22% → Risk-Map-Notiz-Pflicht aktiv.
- FLAG-Entscheidung: Kein neuer Tariff-FLAG nach Regelwerk (Revenue <15%). Bestehender FLAG bleibt (Score-basiert: Score 61, DEFCON 3).
- Sync: CORE-MEMORY.md + Faktortabelle.md + log.md (diese Einträge)

## [2026-04-16] maintenance | Systempflege — config.yaml + Vault-Backlinks + Briefing-Infrastruktur

### config.yaml v3.4.1 (12 Fixes)
- **Stand:** 06.04 → 16.04.2026
- **Sparplan-Formel:** D3=0.5 → D3=1.0 (v3.4-Logik: D4/D3 volle Rate)
- **7 fehlende Scores eingetragen:** RMS 69, VEEV 74, SU 71, BRK.B 75, V 86, COST 69, APH 61
- **APH:** DEFCON 4→3, flag false→true (Score-basiert)
- **AVGO:** flag true→false + flag_review:true (Unter Review, nicht bestätigt)
- **FLAGs-Sektion:** Getrennt in flags_aktiv (MSFT+APH), flags_review (AVGO), flags_watchlist (GOOGL)
- **Termine:** Aktualisiert (V ~22.04, TMO 23.04, RMS/SU Jul/Aug, APH 23.07)

### Vault-Backlinks (6 Satellite-Pages)
- **RMS.md:** Q1 2026 Recap + Screener-Exception (ROIC 24% >> WACC 6.5%), Backlinks zu [[COST]], [[DEFCON-System]]
- **BRKB.md:** Frontmatter-Update, Backlinks zu [[Faktortabelle-Architektur]]
- **COST.md:** Screener-Exception-Tag, Backlinks zu [[RMS]]
- **V.md:** Top-Score 86 Backlink zu [[AVGO]]
- **SU.md:** Frontmatter-Update, Backlinks zu [[Analyse-Pipeline]]
- **APH.md:** DEFCON 3, FLAG aktiv, Score 80→61, Backlinks zu [[MSFT]], [[CapEx-FLAG]]

### Briefing-Infrastruktur (Session 15-16.04.)
- Morning-Briefing Remote Trigger v2.1 deployed (JSON-Nesting-Bug gefixt)
- SessionEnd/SessionStart Hooks installiert (03_Tools/briefing-sync-check.ps1)
- !SyncBriefing / !BriefingCheck Shortcuts in INSTRUKTIONEN.md §25
- Known Limitation: Yahoo 403 (BRK.B/RMS/SU-Kurse nicht aus Cloud verfügbar)

### Offene Punkte
- SKILL.md DEFCON-Schwellen-Mismatch: ≥73 (SKILL) vs. ≥80 (INSTRUKTIONEN) — separater Fix-Task
- ASML Q1 2026 Earnings QuickCheck — ausstehend seit 15.04.

## [2026-04-16] ingest | Wissenschaftliche Integration v4.2 — B8–B11 + Befunde-Priming

**Anlass:** Operativ totes Wissen — 7-Befunde-Matrix existierte, wurde aber nie während Analysen konsultiert. Lösung: Pflicht-Priming + fehlende Source-Pages + Frontmatter-Verankerung.

### Neue Source-Seiten erstellt (2)
- [[Wolff-Echterling-2023]] — "Stock Picking with Machine Learning" (Wiley, Journal of Forecasting 2023): B8 (ROIC+FCF/EV+Operating Margin top-ranked in allen ML-Modellen), B9 (EPS Growth + Low Leverage stabile Quality-Prädiktoren), STOXX-Robustheit validiert Non-US-Scoring
- [[Jadhav-Mirza-2025]] — "Large Language Models in Equity Markets" (Frontiers in AI, PMC 2025): 84-Paper-Survey, B11 (News-Positivity-Bias Meta-Bestätigung), Risk-Management-Forschungslücke identifiziert

### Aktualisierte DEFCON-Konzeptseiten (6) — neues Frontmatter
Alle 6 Seiten erhielten `wissenschaftlicher_anker:` + `konfidenzstufe:` + `sources:` Felder:
- [[DEFCON-System]] — B1–B11 vollständig, 6 Paper, konfidenzstufe: peer-reviewed
- [[CapEx-FLAG]] — B2+B3 (Gu/Kelly/Xiu FCF-Primacy + Earnings Quality)
- [[ROIC-vs-WACC]] — B2+B5+B8 (Gu/Xiu + Buffett + Wolff/Echterling)
- [[Analyse-Pipeline]] — B7+B10 (Datenhierarchie + Chain-of-Thought)
- [[Non-US-Scoring]] — B8 (STOXX-Robustheit validiert Übertragbarkeit)
- [[Tariff-Exposure-Regel]] — konfidenzstufe: erfahrungsbasiert (kein Paper-Anker)

### Synthese-Update [[Wissenschaftliche-Fundierung-DEFCON]]
- 7-Befunde → **11-Befunde** Entscheidungsmatrix (B8: ROIC-Dominanz, B9: Quality-Stabilität, B10: CoT-Konsistenz, B11: News-Positivity-Bias)
- Quellen-Übersicht: 4 → 7 Paper
- Satelliten-Tabelle: alle 11 Ticker mit aktuellen Scores + FLAG-Status + relevanten Befunden (vorher 7 "ausstehend")
- Konzept-Karte erweitert

### 00_Core/INSTRUKTIONEN.md — Befunde-Priming (Pflichtschritt)
- Neuer Block vor Gewichtungs-Tabelle in Stufe 2: "### Befunde-Priming (Pflicht vor jedem Scoring-Start)"
- Vorschrift: Wissenschaftliche-Fundierung-DEFCON.md lesen + relevante Befunde im Output benennen
- B1–B7 Referenztabelle direkt im Instruktionen-Dokument verankert

### index.md aktualisiert
- 74 → **76 Notes** (70 wiki + 6 raw)
- Akademische Paper Sektion: Wolff-Echterling-2023 (B8, B9) + Jadhav-Mirza-2025 (B11) ergänzt

### Gesamt
- Pages created: 2 ([[Wolff-Echterling-2023]], [[Jadhav-Mirza-2025]])
- Pages updated: 9 ([[DEFCON-System]], [[CapEx-FLAG]], [[ROIC-vs-WACC]], [[Analyse-Pipeline]], [[Non-US-Scoring]], [[Tariff-Exposure-Regel]], [[Wissenschaftliche-Fundierung-DEFCON]], [[index.md]], 00_Core/INSTRUKTIONEN.md)
- Neue Befunde: B8, B9, B10, B11 operationalisiert

## [2026-04-17] ingest | 3 Foundation-Papers: Piotroski, Novy-Marx, Sloan
- Quellen: Piotroski (2000) F-Score, Novy-Marx (2013) Gross Profitability, Sloan (1996) Accruals-Anomalie
- Kernthese: Drei Gründungstexte für Quality-Faktor-Investing. Piotroski = 9-Kriterien-Score; Novy-Marx = GP/TA als 2. Value-Seite; Sloan = Accruals-Anomalie +10,4% p.a.
- Pages created: [[Piotroski-2000]], [[Novy-Marx-2013]], [[Sloan-1996]] (sources); [[F-Score-Quality-Signal]], [[Gross-Profitability-Premium]], [[Accruals-Anomalie-Sloan]] (concepts)
- Pages updated: [[Wissenschaftliche-Fundierung-DEFCON]] (B12/B13/B14 + Quellen 7→10 + Konzept-Karte + Änderungsprotokoll), [[index.md]] (Notes 70→76, 3 neue Sources + 3 neue Konzepte)
- Befunde: B12 (F-Score Quality-Signal), B13 (Gross Profitability Premium), B14 (Accruals-Anomalie)
- Vorbereitung: v3.6-Release — Quality-Bonus (+2 Pt.) + GP/TA-Metrik (2 Pt.) + Accrual-Bonus <3%. System-Reife-Ceiling 85% → 92-95%.
- Gesamt: 6 neue Seiten, 2 aktualisierte Seiten, 1 Synthese erweitert
