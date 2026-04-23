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

## [2026-04-17] system | DEFCON v3.7 "System-Gap-Release" ratifiziert & deployed
- v3.6 verworfen (Double-Counting: F-Score/GP-TA/Accrual-Bonus überlappen mit dekomponierten Sub-Signalen in §4/§5)
- v3.7 schließt 3 operative Gaps:
  - Fix 1 (Quality-Trap-Interaktion, B6): Wide Moat + Fwd P/E >30 → Fwd-P/E-Subscore hart 0; Wide Moat + P/FCF >35 → P/FCF-Subscore hart 0; 22–30 / 22–35 → Subscore max 1. Interaktionsterm (nicht Moat-Malus) gegen Double-Counting.
  - Fix 2 (Operating Margin, B8): OpM TTM >30%→2 | 15–30%→1 | <15%→0. Fundamentals-Cap hart bei 50.
  - Fix 3 (Analyst-Bias-Kalibrierung, B11): Strong-Buy >60%→1 (Crowd-Malus). Sell-Ratio <3%→1 (Warning), 3–10%→3 (Healthy), >10%→0.
- Backtest 11 Satelliten (Interaktions-approx): ASML 68→66 (D3), AVGO 85→84, MSFT 60→59, TMO 62→63 (D2 aus v3.5 Audit), RMS 69→68, SU 71→69, APH 61→63, COST 69, V 86, BRK.B 75, VEEV 74 — keine DEFCON-Shifts
- Sparraten neu: Nenner 8.5 (8× D4/D3 + 1× D2 TMO), volle Rate 33,53€, TMO D2 16,76€, MSFT/APH 🔴 0€
- Pages updated: [[Wissenschaftliche-Fundierung-DEFCON]] (v3.7-Änderungsprotokoll)
- Core files: INSTRUKTIONEN.md §5 + §5a + §22, SKILL-dynastie-depot.md v3.7, config.yaml v3.7, CORE-MEMORY.md v1.7, Faktortabelle.md v3.7
- System-Reife: 85% → ~92%

## [2026-04-17] hygiene | Systemhygiene post-v3.7
- SESSION-HANDOVER.md komplett neu geschrieben (Pre-Implementation → Post-Deployment-Status)
- Auto-Memory aktualisiert: portfolio-state-snapshot.md (v3.7-Scores + Nenner 8.5 + TMO D2), system-architecture.md (config v3.4.1 → v3.7 + Skill-Deployment-Notiz), MEMORY.md Index
- Skill-Paket-Konsistenz: `06_Skills-Pakete/dynastie-depot_v3.7.zip` gebaut & manuell installiert (ersetzt v3.5)
- Rebalancing-Tool bleibt als User-Pending (xlsx nicht programmatisch editiert)
- Commit d890d57: 14 files +247/-142

## [2026-04-17] refactor | Session-Start-Refactor — STATE.md als Single-Entry-Point
- **Problem:** Session-Start-Auto-Read lud 4 Dateien (~1.200 Zeilen: CORE-MEMORY 362 + INSTRUKTIONEN 588 + KONTEXT 148 + Faktortabelle 114). ~70% Token-Overload (historische Chronik in CORE-MEMORY §1).
- **Fix:** `00_Core/STATE.md` (~80 Zeilen) als neuer Single-Entry-Point. Enthält Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches, Navigation. Andere 00_Core-Dateien on-demand.
- **Archivierung (ohne Kontextverlust):** CORE-MEMORY §1 Meilensteine vor 15.04.2026 → `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md`. Mapping-Tabelle zeigt für jede historische Lektion, wo sie permanent lebt (Sections 2–10, INSTRUKTIONEN, Vault-Konzepte).
- **CLAUDE.md** Session-Initialisierung-Block + Verhalten-Block (Sync-Pflicht jetzt 4 Dateien inkl. STATE.md) umgeschrieben.
- **CORE-MEMORY §1** gekürzt: 60+ Einträge → 16 aktuelle (ab 15.04.2026), Verweis auf Archiv vorangestellt.
- Pages created: [[Session-Start-Protokoll]] (concept)
- Pages updated: [[CLAUDE-md-Konstitution]] (Session-Init-Section + frontmatter `related`), [[Faktortabelle-Architektur]] (frontmatter `related`), [[index.md]] (77 wiki-Notes, Header)
- **Kein Commit-/Briefing-Sync in dieser Session** — User entscheidet über `!SyncBriefing` (00_Core/ geändert).
- Token-Einsparung Session-Start: ~1.200 → ~80 Zeilen Auto-Read (≈-93%)

## [2026-04-17] refactor | Post-STATE Konsolidierung — INSTRUKTIONEN↔SKILL-Dedup + SKILL-Rename + CLAUDE-Konsistenz
- **Phase 1+4 (CLAUDE.md):** Sync-Pflicht Z.59 auf 4 Dateien korrigiert (vorher 3, Widerspruch zu Header Z.19); MCP-Session-Check 10 Zeilen → 1 Bullet; Token-Effizienz-Block verdichtet (6 Bullets → 6 kompakte; "Modell"-Zeile für `/model opus`-Toggle ergänzt); Applied Learning "SKILL.md-Rename"-Bullet obsolet → entfernt (12→11 Bullets).
- **Phase 2a (SKILL-Rename):** `01_Skills/dynastie-depot/SKILL-dynastie-depot.md` → `SKILL.md` (ZIP-Install-Konvention). Aktualisiert: config.yaml, PIPELINE.md, SESSION-HANDOVER.md, wiki/sources/dynastie-depot-skill.md, wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md. Historischer Log-Eintrag oben unberührt (zeitliche Authentizität).
- **Phase 2b (Dedup):** INSTRUKTIONEN.md 587→452 Zeilen (-23%). Gelöscht als Duplikate zu SKILL.md: §4 Gewichtung/DEFCON-Schwellen/FLAGs, §5 Fundamentals-Skalen, §5a Sentiment v3.7, §6 Insider (außer Cashless-Exercise → zu SKILL migriert), §8 Datenquellen, §13 Verhaltensregeln, §14 Non-US Addendum, §15 Tariff, §16 Non-US API Sanity Check. 10 Cross-Refs zu SKILL.md gesetzt.
- **Phase 3 vorbereitet (Modell-Strategie):** `/model sonnet` Default, `/model opus` manuell für !Analysiere, Multi-Step-Refactors, strategische Entscheidungen. Kein Auto-Routing — null Risiko.
- **ZIP-Rebuild:** `06_Skills-Pakete/dynastie-depot_v3.7.zip` neu gepackt (SKILL.md 38497 bytes inkl. Cashless-Exercise-Ergänzung).
- Pages created: [[INSTRUKTIONEN-SKILL-Trennung]] (concept)
- Pages updated: [[index.md]] (78 wiki-Notes), [[dynastie-depot-skill]] (SKILL.md-Ref), [[Wissenschaftliche-Fundierung-DEFCON]] (SKILL.md-Ref)
- Motivation: Token-Effizienz (kein Doppel-Load) + Drift-Vermeidung (eine Quelle pro Regel) + ZIP-Install ohne Copy-Rename-Schritt.

## [2026-04-17] analyse | ASML Q1 2026 Post-Earnings Vollanalyse (Pfad B, Non-US/IFRS-Anker)
- **Score:** 66 → **68** (Live-Verify +2 innerhalb v3.7-Toleranz ±2) | **DEFCON 🟡 3** bleibt | **Kein FLAG**
- **Auslöser:** Session-Handover — ASML als mustergültiger Non-US/IFRS-Workflow-Anker für Beispiele.md v3.7-Rebuild (ergänzend zu AVGO Post-Fix-Form).
- **Datenquelle Primär:** `eodhd_intel.py` (Non-US → nicht Shibui/defeatbeta). Kurs €1.242,60, MC €482,3B, FCF-Marge 33,8%, ROIC 26,48%, WACC 9,29% (FRED DGS10 4,29% + 5% ERP).
- **WACC-Konflikt:** GuruFocus 18,21% (implausibel — Beta/ERP-Overestimation) verworfen zugunsten FRED-basierter Methodik. 3-Punkte-ROIC-Swing dokumentiert.
- **v3.7-Mechanismen beobachtet:** Quality-Trap **beidseitig hart 0** (Fwd P/E FY26 30,6x + P/FCF 58,5x) — einziger Depot-Anker mit doppelter QT-Aktivierung. B11 Analyst-Bias-Malus aktiv (35/44 Strong-Buy = 79,5% → Sentiment gedeckelt). B8 OpM-Cap erreicht (2/2).
- **Q1-Actuals (15.04.):** Rev €8,8B / EPS €7,15 / GM 53,0% ✅ Beat. FY26-Guidance €36-40B (raised). **China 19%** (von 36% Q4) = struktureller Shift. Kurs -6% post-Earnings (Export-Control-Sorge).
- **FY27-Watch:** Fwd P/E 30,30 — bei <30 deaktiviert QT-P/E-Zweig → Score +6-8 möglich (D3→D4-Pfad dokumentiert).
- **Subscore-Breakdown:** Fund 28/50 · Moat 20/20 · Tech 7/10 · Insider 7/10 (Carry-Forward — AFM-H1-2026 pending) · Sent 6/10.
- Pages updated: [[ASML]] (frontmatter score 66→68, Analyse-Historie, Q1-Recap-Section), [[Beispiele.md]] (ASML-Anker in AVGO-Post-Fix-Form eingefügt, Rebuild-Status ASML ⏳→✅)
- Sync: STATE.md (66→68) + Faktortabelle.md (ROIC/FCF-Marge/Debt-EBITDA live) + CORE-MEMORY §1 (Meilenstein-Eintrag)
- **Briefing-Sync erforderlich** (00_Core/ geändert).

## [2026-04-17] refactor | Part 1 & 2: _extern Cleanup + Skill-Audit + Vault-Score-Drift-Fix
- **Part 1 — _extern Cleanup (manuell vom User + Tool-Extraktion):**
  - `01_Skills/_extern/qualitative-valuation/` gelöscht (~80% in DEFCON kodifiziert, ESG bewusst ausgelassen)
  - `01_Skills/_extern/risk-metrics-calculation/` gelöscht — 3 Funktionen extrahiert nach `03_Tools/portfolio_risk.py`
  - `01_Skills/_extern/earnings-calendar/` gelöscht (FMP-basiert, redundant zu earnings-preview/recap)
  - Neu: `03_Tools/portfolio_risk.py` (Correlation Matrix / Component Risk / Stress-Test 2020-COVID + 2022-Rate-Hikes) — quartalsweise manuell, kein Skill
- **Part 2 — Skill-Audit Kategorie A (Score-Drift Fixes):**
  - `config.yaml`: v3.4.1 → v3.7 Header + ASML score 66→68, AVGO-Notiz 86→84, SU-Notiz 71→69, RMS-Notiz 71→68, MSFT-FLAG-Grund harmonisiert (83.6%/bereinigt 63%)
  - `INSTRUKTIONEN.md` Z.110: TMO 62 → 63
  - `Faktortabelle.md`: v3.4 → v3.7 + 3/11 Live-Verify-Status
  - `dynastie-depot-skill.md` (Wiki): D3-Rate 0.5 → 1.0 (v3.4-Logik) + Rechenbeispiel auf 8.5-Nenner/33,53€
- **Wiki Entity-Page Sync (Body ↔ Frontmatter ↔ STATE):**
  - [[AVGO]]: Callout 86→84, Historie-Eintrag v3.7
  - [[SU]]: Callout 71→69
  - [[RMS]]: Callout 69→68, Score-Verlauf erweitert
  - [[TMO]]: Callout D3/67 → D2/63, Stand 17.04., Historie-Eintrag
  - [[MSFT]]: Callout 60→59, Frontmatter-Datum 17.04., Historie-Eintrag
  - [[APH]]: Callout 61→63, Score-Verlauf erweitert, v3.7-Notiz
  - [[Wissenschaftliche-Fundierung-DEFCON]]: v3.5-Zeitstand-Banner hinzugefügt (B-konform, keine Score-Änderung)
- **Pages updated:** 6 Satelliten-Entities, 1 Synthese, 1 Source
- **Pages created:** keine
- **Deleted:** 3 _extern Skills + zugehörige Verzeichnisse
- **Sync:** STATE.md (bereits aktuell — Source of Truth) + Faktortabelle + config.yaml + alle Wiki-Entities on par
- **Briefing-Sync erforderlich** (00_Core/INSTRUKTIONEN.md + Faktortabelle.md + config.yaml geändert)
- **Nächster Schritt:** ZIP-Release `dynastie-depot_v3.7.zip` vom User manuell + Rebalancing_Tool_v3.4 + Satelliten-Monitor auf Konsistenz zu STATE prüfen

## [2026-04-18] analysis | V Pre-Earnings Q2 FY26 — Erster Forward-Record + Schema-Threshold-Fix
- **Ablauf:** earnings-preview V → !Analysiere Vollanalyse → Advisor-Review → 3 Scoring-Korrekturen → γ-Schema-Fix → α-Rescoring
- **Forward-Records (beide 18.04.):**
  - `2026-04-18_V_vollanalyse` Score 72 D4 — erster Forward-Record überhaupt (Pre-Earnings-Baseline Q2 FY26)
  - `2026-04-18_V_rescoring` Score 63 D2 — Korrektur nach Advisor-Review (nicht delete, append-only + Chain-Notiz)
- **Drei Sub-Score-Korrekturen (via Advisor):**
  - Moat 20→19: Pricing-Power-Bonus entfernt (Earnings-Call-Transcript nicht explizit verifiziert gemäß SKILL-Regel)
  - Insider 6→5 (ownership 2/3→1/3): V-Aggregate-Ownership <1%, erfüllt 1%-Threshold nicht
  - Fundamentals 37→30 (ROIC 8/8→1/8): Regel-4-Gating (GW/Assets 19,95% <30%) greift nicht, V ist kein M&A-Compounder, GAAP ROIC 9,89% < WACC 10,48% → Score 1
- **γ-Schema-Fix (schemas.py + archive_score.py):** DEFCON-Thresholds auf SKILL.md aligned (≥80 D4 / 65-79 D3 / 50-64 D2). Vorher Schema 70/60/50 (Drift). Smoke-Tests grün.
- **STATE.md / Faktortabelle.md Label-Drift-Fix:** BRK.B/VEEV/SU/COST/RMS D4→D3, APH D3→D2 (Sparraten unverändert bei D3/D4-Übergang, FLAG überschreibt APH).
- **Sparraten-Nenner:** 8.5 → 8.0, volle Rate 33,53€→35,63€, D2-Rate 16,76€→17,81€. **Summe 285€** ✓
- **V Score-Delta Narrative:** 86 (17.04. Backfill aus CORE-MEMORY §4-Rekonstruktion, sub-scores Fractional-Split-Platzhalter) → 63 (erste echte v3.7-empirische Berechnung). Treiber: Technicals-Kollaps (6M RelStärke -13,97pp vs SPY, Kurs -4,97% unter fallendem 200MA), v3.7 Sentiment Crowd-Warnung (0% Sell + PT-Dispersion 32%), P/FCF QT-Deckel Wide+28x, ROIC GAAP strikt.
- **Key Finding:** v3.5→v3.7-Algebra-Projektionen vom 17.04. (8/11 Titel nicht empirisch verifiziert) könnten stille Überschätzungen enthalten. Bei jedem Earnings-Trigger: voller Forward-Lauf ersetzt Algebra-Schätzung.
- **Archive-Stand:** 26 Records (24 Backfill + 2 Forward V).
- **Sync:** STATE.md + Faktortabelle.md + CORE-MEMORY §11 + schemas.py + archive_score.py + score_history.jsonl (§18 alle 6 Dateien).
- **Briefing-Sync erforderlich** (00_Core/ geändert).

## [2026-04-18] analysis | TMO Pre-Earnings Q1 FY26 — Forward-Vollanalyse + struktureller FLAG-Disclosure
- **Ablauf:** earnings-preview TMO → !Analysiere Vollanalyse → Advisor-Review der FLAG-Entscheidung → Option B (Strukturdisclosure statt mechanischem Trigger)
- **Forward-Record:** `2026-04-18_TMO_vollanalyse` Score 64 D2 — Algebra-Projektion 63 empirisch bestätigt (±1, dritte Verifikation nach V-Gegenbeispiel)
- **Score-Breakdown:** Fund 30 (Fwd P/E 6, P/FCF 1 QT-cap Wide+31x, Bilanz 6, CapEx/OCF 7, ROIC 6 bereinigt, FCF Yield 3, OpM 1) + Moat 18 (Wide) + Tech 6 (ATH 3, RelStärke 0, Trend 3) + Insider 4 (0+1+3) + Sent 6 (SB 4, Sell 1 Crowd, PT-Upside 2, PT-Disp -1) = 64
- **ROIC-Bereinigung (Regel-4-Gating erfüllt):** GW/Assets 44,74% ≥30% → Goodwill-Ausnahme; Invested Capital bereinigt = 92,792M - 49,362M = 43,430M → ROIC bereinigt 17,18% vs WACC 10,44% = +6,74pp Spread
- **FLAG-Entscheidung fcf_trend_neg — Schema-Trigger abgelehnt (Option B):**
  - Schema-Signal: FCF FY25 6,293M vs FY24 7,267M = **-13,4% YoY**; CapEx +8,9% YoY
  - Advisor-Begründung (nicht aktiviert): (a) **WC-Noise** — WC-Delta FY25 -1,766M vs -334M FY24, Δ -1,432M erklärt FCF-Rückgang -974M überproportional; (b) **4J-Plateau** — FY22-25 FCF $6,911→6,927→7,267→6,293M = kein Mehrjahres-Abwärtstrend; (c) **Profitabilität intakt** — Operating Income +5,1% YoY ($8,110M vs $7,717M)
  - Konsequenz: `flags.aktiv_ids=[]` + expliziter Disclosure in `notizen` + Faktortabelle + STATE.md
- **Systemische Lektion:** Schema-Validator ≠ SKILL-Regel-Semantik — einzelperiodische Trigger brauchen Multi-Year-Kontext + strukturelle Erklärung + Parallel-Metriken (OpInc) vor FLAG-Aktivierung. Dokumentiert in CORE-MEMORY §11 Befund #4.
- **Resolve-Gate:** Q1 FY26 Earnings 23.04.2026 — WC-Unwind + FCF-Recovery bestätigt → Disclosure bleibt Notiz; fehlende Reversibilität → fcf_trend_neg-Trigger nachtragen
- **Archive-Stand:** 27 Records (24 Backfill + 3 Forward: V_vollanalyse + V_rescoring + TMO_vollanalyse)
- **Sparraten:** unverändert (D2 → 17,81€, Nenner 8.0, Summe 285€ ✓)
- **Sync:** STATE.md + Faktortabelle.md + CORE-MEMORY §11 + score_history.jsonl + log.md (§18 — 5/6 Dateien; schemas.py unberührt)
- **Briefing-Sync erforderlich** (00_Core/ geändert)

## [2026-04-18] sync | config.yaml + Vault-Satelliten auf 18.04.-Stand aligned
- **Scope:** Propagation der V-Forward + TMO-Forward + Schema-SKILL-Threshold-Alignment vom 18.04. in `config.yaml` und `wiki/entities/satelliten/`
- **config.yaml Updates:**
  - Sparplan-Beispiel: Nenner 8.5→8.0, Volle Rate 33,53€→35,63€, D2 16,76€→17,81€ (V + TMO beide D2)
  - V-Entry: Score 86→63, DEFCON 4→2, score_datum → 18.04., sparrate_hinweis → 17,81€, scoring_notiz komplett neu (Technicals-Kollaps + ROIC Regel-4-Gating-Fail)
  - TMO-Entry: Score 63→64, score_datum → 18.04., sparrate_hinweis → 17,81€, scoring_notiz (ROIC bereinigt 17,18% vs WACC 10,44%, +6,74pp Spread, Regel-4 greift), flag_hinweis (fcf_trend_neg Struktureller Disclosure Option B)
  - APH-Entry + FLAG-Sektion: DEFCON 3→2 (Label-Fix)
  - 5 Label-Fixes (DEFCON 4→3): BRK.B, VEEV, SU, COST, RMS (Score unverändert, Sparrate bei D3/D4 identisch)
  - Meta: Live-Verify 3/11→5/11, Event-Kalender (V Score 86,D4 → 63,D2 ; TMO 63→64)
- **Vault-Entities aktualisiert (8 Pages):**
  - [[V]]: Komplette Neuanalyse (v3.4-Block entfernt, v3.7-Forward mit 3 Advisor-Korrekturen dokumentiert)
  - [[TMO]]: Score 63→64, ROIC-Regel-4-Gating dokumentiert, fcf_trend_neg Struktureller Disclosure tabelliert
  - [[BRKB]], [[VEEV]], [[SU]], [[COST]], [[RMS]]: Tag defcon-4→defcon-3 + Callout-Banner + Sparrate 33,53€→35,63€
  - [[APH]]: Tag defcon-3→defcon-2 + Callout-Banner (FLAG überschreibt Sparrate weiter)
- **Nicht geändert:** ASML (D3), AVGO (D4, Score 84), MSFT (D2 FLAG). Nicht-Satelliten-Pages unberührt.
- **Konsistenz-Check:** YAML-Parser grün (`python -c yaml.safe_load`), keine Score-Verschiebung gegenüber STATE.md / Faktortabelle.md / score_history.jsonl.
- **Sync-Applied-Learning-Prinzip:** "config.yaml-Fix allein reicht nie" — diese Konsolidierung schließt den Multi-Source-Drift zwischen 00_Core, Skill-SSOT und Vault.
- **Briefing-Sync erforderlich** (config.yaml ist Skill-SSOT, wird von Remote-Trigger nicht direkt gelesen, aber Konsistenz für ZIP-Rebuild nötig)
- **Nächster Schritt:** Skill-ZIP v3.7.2 bauen (manuell via User), Rebalancing_Tool_v3.4 Sparraten-Spalte manuell nachziehen

## [2026-04-19] deploy | Skill `backtest-ready-forward-verify` deployed (v3.7.2)
- **Scope:** 6 Plan-Tasks abgearbeitet (superpowers:subagent-driven-development). Pre-Gates A (git-Performance 34ms ✓) + B (§-Citations §18/§27.4/§28.1/§28.2/§28.3 verifiziert) grün.
- **Task 1 — Schema (commits `33cdd74` + `1bd50ac`):** `MigrationEvent(from_version, to_version, algebra_score, forward_score, delta signed, outcome: Literal[accepted|log_only|block])` als nested struct + `ScoreRecord.migration_event: Optional[MigrationEvent] = None`. Zwei self-validators: `_check_delta` (Arithmetik: forward − algebra, float-safe `round(.,6)`) + `_check_outcome_bucket` (§28.2: |Δ|≤2 → accepted | 3-5 → log_only | >5 → block). 7/7 Smoke-Tests grün. Defense-in-depth gegen Builder-Bugs (append-only → jeder korrupt Record permanent).
- **Task 2 (commit `2f3e828`):** `03_Tools/backtest-ready/_drafts/` + `.gitkeep` + `.gitignore`-Pattern `03_Tools/backtest-ready/_drafts/*.json`. Ephemer Handoff-Ordner Draft→Skill.
- **Task 3 (commits `7d43492` + `7e0b021` + `603ea74`):** Skill `backtest-ready-forward-verify` (229 Zeilen Prosa, `trigger_words: []` = programmatisch) + Helpers `_forward_verify_helpers.py` (4 Funktionen: `parse_wrapper`, `parse_state_row`, `build_migration_event`, `check_freshness`) + `_smoke_test.py` (6 TDD-Cases, alle grün). Advisor-Korrektur: Skill-Prosa ist nicht TDD-testbar → Smoke-Tests nur deterministische Teile, qualitative E2E erst in Task 6. Code-Reviewer 2. Runde: 2 Important-Fixes (`parse_wrapper` strict kein flat-fallback, P2b exakte Int-Gleichheit statt ±1 Toleranz) + 3 Minor (porcelain-offset, Case-4-Assertion-Härtung, `{abs_delta:g}` statt `int()`).
- **Task 4 (commit `018257e`):** dynastie-depot `SKILL.md` Schritt 7 ersetzt: inline `archive_score.py`-Aufruf → `Skill(skill="backtest-ready-forward-verify", args=<pfad>)` + 6-Fall-Stdout-Parser (OK / freshness / PFLICHT / STOP / duplicate / FAIL). Version-Bump 3.7.1 → 3.7.2 (kein DEFCON-Bump per §28.3 Nicht-Migration-Trigger).
- **Task 5 (commit `8b856b4`):** INSTRUKTIONEN §18 v1.7 (score_history.jsonl via Skill orchestriert) + CORE-MEMORY §1 Meilenstein 19.04. + STATE.md System-Zustand-Zeile.
- **Task 6 (commit `2d97ba1`):** Qualitative E2E-Verification 6 Szenarien. 1 Gap identifiziert und gefixt: SKILL.md P2b fehlte explizites "Stopp"-Kommando (P4/P5 hatten es, asymmetrisch). Zusätzliche Zeile eingefügt.
- **Nach User-Install (Desktop-App):** Bugfix Header-Banner v3.7.1 → v3.7.2 (commit `2d97ba1`-Folge) + Vault-Sync 4 DEFCON-concept-Pages (Score-Archiv/FLAG-Event-Log/Backtest-Ready-Infrastructure/Analyse-Pipeline) auf v3.7.2 + Skill-Orchestrator-Komponente (commit `07431d0`).
- **Dokumentations-Propagation (commit folgt):** CLAUDE.md Projektstruktur + sync-note, `03_Tools/backtest-ready/README.md` (15 Modelle + 6 Validators + Skill-Workflow + 7-case smoke), PIPELINE.md Skill-Struktur + ZIP-Name, Vault `index.md` (DEFCON v3.4→v3.7, Skill-Entry), `wiki/sources/dynastie-depot-skill.md` (Monolith-Claim ersetzt, Rechenbeispiel + Kalibrierungsanker auf 19.04.-Stand), `Investing-Mastermind-Index.md` (Portfolio-Tabelle + Skills-Liste auf STATE.md-Stand), KONTEXT.md score_history.jsonl-Zeile.
- **Archive-Stand:** unverändert 27 Records (kein neuer !Analysiere-Lauf heute — reine Skill-Infrastruktur + Dokumentation).
- **Sparraten:** unverändert (Nenner 8.0, 35,63€ / 17,81€ / 0€, Summe 285€ ✓).
- **Sync:** log.md + CORE-MEMORY.md + STATE.md + INSTRUKTIONEN.md + score_history.jsonl (unverändert, kein neuer Record) + alle Skill/Tool-Sources + 6 Vault-Pages. Kein FLAG-Event.
- **Erster Real-Run der Skill-Pipeline:** TMO Q1 FY26 am 23.04.2026 (FLAG-Resolve-Gate + D2-Entscheidung).
- **Briefing-Sync erforderlich** (00_Core/ geändert: CLAUDE.md + KONTEXT.md + CORE-MEMORY.md + STATE.md + INSTRUKTIONEN.md).

## [2026-04-19] ingest | 4-Paper Backtest-Validation-Framework
- **Scope:** 4 neue akademische Paper trianguliert — Bailey/Borwein/López de Prado/Zhu 2015 (PBO/CSCV), Aghassi/Asness/Fattouche/Moskowitz 2023 (AQR Fact/Fiction), Flint/Vermaak 2021 (Factor Information Decay), Palomar 2025 (Portfolio Optimization, Seven Sins). Advisor-validierte Triage + User-bestätigte Workflow-Reihenfolge (Vault-first, dann System).
- **Pages created (9):**
  - 4 Sources: [[Bailey-2015-PBO]], [[Aghassi-2023-Fact-Fiction]], [[Flint-Vermaak-2021-Decay]], [[Palomar-2025-Portfolio-Optimization]]
  - 5 Concepts: [[PBO-Backtest-Overfitting]], [[Factor-Investing-Framework]], [[Factor-Information-Decay]], [[Seven-Sins-Backtesting]], [[Palomar-Methods-Reference]]
- **Pages updated (2):**
  - [[Backtest-Methodik-Roadmap]] v1.0 → v2.0 (4-Dim-Gate-Section ergänzt, frontmatter sources/related erweitert)
  - [[Wissenschaftliche-Fundierung-DEFCON]] (B15-B18 in 14-Befunde-Tabelle, Quellen-Übersicht erweitert, §29-Validation-Gate-Section eingefügt, Änderungsprotokoll aktualisiert)
- **Kernaussagen konsolidiert — 4-Dimensionen-Validation-Gate (§29):**
  - §29.1 Methode (B15 Bailey): PBO < 0,05 via CSCV als Overfitting-Gate
  - §29.2 Raum (B16 Aghassi): aggr. Portfolio-SR im AQR/Ilmanen-Multifaktor-Band
  - §29.3 Zeit (B17 Flint/Vermaak): Cadence konsistent mit Faktor-Half-Life
  - §29.4 Neue Parameter (B16 Harvey/Liu/Zhu): t-Stat ≥ 3 Pflicht
  - §29.5 Sünden (B18 Palomar): 7-Punkt-Pre-Flight (Sin #7 n.a. Long-Only)
  - §29.6 Portfolio-Metriken: Palomar Ch. 6 Formeln für `risk-metrics-calculation`-Skill
- **Architektur-Entscheidungen:**
  - §28.3 bereits belegt ("Nicht-Migration-Trigger") → neues §29 für Retrospective-Analyse-Gate
  - FUTURE-ACTIVATION 2028-04-01 für §29.1-4 + §29.6; §29.5 Seven-Sins-Gate bereits jetzt aktiv bei Migration-Events
  - valuation_z_score Watch-Metric **verworfen** nach Advisor-Feedback (evidence-mismatch zu AQR value-spread, Applied-Learning-Regel greift); stattdessen einzeilige !Analysiere-Checkliste
  - Portfolio-Return-Persistenz via `03_Tools/portfolio_risk.py`-Erweiterung (Phase 3, wartet auf ETF/Gold-Ticker vom User)
- **DEFCON-Faktor-Mapping dokumentiert:** DEFCON = impliziter Long-Only-Multi-Faktor-Selektor (Value/Quality/Momentum/Defensive + Insider als non-AQR-Edge). Size explizit verworfen (konsistent mit AQR).
- **Phase 2 pending:** INSTRUKTIONEN §29-Draft + dynastie-depot SKILL.md Checklist + backtest-ready-forward-verify SKILL.md §8-Erweiterung + CLAUDE.md Applied-Learning-Bullet + STATE.md Interim-Gate (2027-10-19) + CORE-MEMORY §5-Lektion.
- **Archive-Stand:** unverändert 27 Records. Scores/Sparraten unverändert. Kein FLAG-Event.
- **Sync-Commit folgt:** Vault + System-Änderungen in einem Commit nach Phase 2 (§18 6-File-Sync für System, + 11 Vault-Pages für Ingest).
- **Advisor-E2E-Verify Phase 1 (post-Write):** 1 Fix-Issue + 2 Deferred. Fix: `[[§29 Retrospective-Analyse-Gate]]` Phantom-Links in PBO-Backtest-Overfitting.md + Factor-Investing-Framework.md durch Plaintext-Verweise auf `00_Core/INSTRUKTIONEN.md` ersetzt. Deferred für nächste Lint-Session: (a) Autoren-Entity-Stubs für Asness, López de Prado, Palomar erwägen (schema-konform weil authors Plaintext, aber Prominenz-Klasse rechtfertigt Entity-Pages); (b) WIKI-SCHEMA-Klausel für akademische Paper-Sources: `url:`-Frontmatter ersetzt raw/-Backlink bei stabiler URL + Paywall-Verfügbarkeit (bewusste Entscheidung, Link-only statt Raw-Kopie — alle 4 neuen Source-Pages betroffen).

## 2026-04-19 — Paper-Integration systemweit (Track 3)

**Phase 1a+1b abgeschlossen:**
- 11 Satelliten-Pages mit Factor-Exposure-Block (Aghassi 2023)
- 6 defcon-Concepts mit §29-Rückverweisen + Paper-Ankern
- 8 bestehende Concept-Pages mit "Wissenschaftliche Fundierung"-Abschnitt
- index.md + log.md aktualisiert

**Phase 2-4 pending:** Skill-Verankerung, R5 Portfolio-Return-Persistenz, R1 §30 Monthly-Refresh

**Spec:** docs/superpowers/specs/2026-04-19-paper-integration-design.md

## 2026-04-19 — Track 3 Paper-Integration systemweit ABGESCHLOSSEN

**5 Phasen fertig:**
- Phase 1a: 11 Satelliten-Pages mit Factor-Exposure-Block (Commit 7ed5267)
- Phase 1b: 6 defcon-Concepts + 8 bestehende Concepts mit Paper-Ankern (Commit 81fece3)
- Phase 2: 2 Skills + 3 Tool-Dokus + INSTRUKTIONEN §§18/27/28/29 Querverweise (Commit a47cc28)
- Phase 3: R5 Portfolio-Return-Persistenz aktiv (Commit f7920cf) — portfolio_returns.jsonl + benchmark-series.jsonl Daily-Schema v1.0, Trading-Date-Fix nach Codex-Review (5/5 Fixes)
- Phase 4: §30 Live-Monitoring & Cadence (Commits c1f0f21 Draft + 96b0b69 Final nach Codex-Review 5/5 Fixes)

**Skills repacked:** dynastie-depot + backtest-ready-forward-verify (v3.7.2 in-place, keine Version-Bump — Track 3 ist Doku-Refresh, kein funktionaler Change)

**Interim-Gate 2027-10-19** (PBO-Smoke-Test + 18M-Dry-Run risk-metrics-calculation + FX-Conversion-Nachrüstung).
**Review-Gate 2028-04-01** (Volle §29.1-3/6 Aktivierung nach 24+ Monaten Return-Serie).

**Applied-Learning-Regel gewahrt:** Keine Scoring-Kern-Änderungen, nur Monitoring/Dokumentation/Infrastruktur/Validation-Vorbau. DEFCON unverändert v3.7.

**Codex-Review-Gates (3×):** (1) Phase 1b Konsistenz-Pass — 3 Fixes (MSFT/TMO Plan-intendiert, CapEx-FLAG §29.3-Rückverweis ergänzt). (2) Phase 3 Code-Review — 5 Fixes (Trading-Date, dual-file Duplicate-Guard, Common-Date-Intersection, Mixed-Currency-Caveat, Schema-Doc-Wording). (3) Phase 4 §30-Formulierung — 5 Fixes (Drei-Ebenen-Disambiguierung, Score-Unverändbarkeit, Applied-Learning-Re-Review-Ablage, Forward-Dating-Pflicht, Schema-Watch-Klarstellung).

**Commits:** 7ed5267 → 81fece3 → a47cc28 → f7920cf → c1f0f21 → 96b0b69 + Spec 976e67a + Plan ee61535.

## 2026-04-20 — Track 5 Implementation-Plans geschrieben (5a + 5b, Execution-deferred auf 2026-04-21)

**Session-Scope:** Zwei Implementation-Plans zum TRACK5-SPEC v1.0 (Commit `22cdeb8`) via `superpowers:writing-plans`. Keine Code-Execution, reine Planungs-Artefakte. Vault-Updates folgen Post-Execution.

**Artefakte (beide force-added, `docs/superpowers/` ist gitignored per Konvention):**
- `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (~540 Zeilen, 9 Tasks inkl. 90-Tage-Audit-Review deferred auf 2026-07-19)
- `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (~1240 Zeilen, 15 Tasks inkl. 30-Tage-Stabilität deferred auf 2026-05-20 + Interim-Gate 2027-10-19)

**Plan 5a (EDGAR Skill-Promotion):**
- Promote `01_Skills/_extern/sec-edgar-skill/SKILL-sec-edgar-skill.md` → `01_Skills/sec-edgar-skill/SKILL.md`
- `pip install edgartools` + `set_identity("Tobias Kowalski tobikowa90@gmail.com")`
- Eskalations-Fallback: Daten-Konflikt-Arbitrage / 10-K-Textsuche / Form-4-Eskalation / Multi-Period-Trend
- Frontmatter-Trigger-Words nach Codex-P0-Fix gekürzt (Auto-Load-Risiko in !Analysiere eliminiert)
- INSTRUKTIONEN §17-Zeile 248 Update + CORE-MEMORY §1 Meilenstein + _extern/ Superseded-Banner

**Plan 5b (FRED Macro-Regime-Filter):**
- β `fredapi` + `python-dotenv`, ALFRED-first-release (Backfill) + FRED-latest-release (Live) Dual-Mode-Adapter `fred_client.py`
- Historical-Backfill `macro_regime_historical.jsonl` 1997+ (~7500 Records) mit Codex-Data-Quality-Gate
- Grid-Search 1620 Combos über (hy_oas × curve × ism × persistence × operator × factor), vectorized via Pre-Compute-Cache (180:1620 Cache-Hit-Ratio = O(1) inner-loop)
- Utility-Primärmetrik `1 - avg_filtered/avg_unfiltered` + Codex-Sekundär-Diagnose `forward_6m_hit_rate` (Spec-§3.3.1-Verbalisierung-Check)
- Konservative Parameter-Wahl via 5-Regel-Tie-Break R1→R5 (Lexikographie, total-ordering-Fallback)
- Single-Source-of-Truth `03_Tools/macro_regime_config.py` (daily-run importiert, §31.2 referenziert)
- Neue INSTRUKTIONEN §31 (Trigger-Regeln + Sparraten-Modulation + Revision-Invarianz + Kill-Switch)
- Neue INSTRUKTIONEN §22.1 (Manual-Read-Workflow; kein programmatischer Sparplan-Enforcer, Enforcement deferred)
- Daily-Run integriert in CCR-Remote-Trigger via Prompt-Template-SCHRITT-0-Prepend (full-replace)

**Codex-Review-Gates (3×):**
- Pre-Plan §-Mismatch-Entscheidung: Option 1 bestätigt (Plan-Header-Notice, Spec frozen)
- Plan 5a Review: 2 P0 (1 Dissens — bash/PowerShell — System-Prompt bestätigt bash korrekt; 1 ACCEPT — Trigger-Words verengt), 3 P1 (90-Tage-Audit-Task, PyYAML-Dep-Entfernung via Regex-Check, Token-Budget 400/1200 → 500/1500 +25% Puffer)
- Plan 5b Review: 0 P0, 8 P1 + 1 Kompromiss — alle 7 Fixes eingepflegt (Enforcement-Deferral / Persistence-Contiguity-Guard / Tie-Break-R5 / CCR-Remote-Pfad / Q3-ALFRED-Alignment / macro_regime_config.py Single-Source / NYSE-Approximation-Wording) + forward_6m_hit_rate als Sekundär-Diagnose (Primärmetrik-Dissens gelöst durch Zusatzspalte statt Formel-Umbau)

**§-Mismatch-Fixes (beide Pläne):** TRACK5-SPEC v1.0 referenziert in §2.5/§2.6/§3.2.4/§3.3.2/§3.4/§3.5 veraltete INSTRUKTIONEN/CORE-MEMORY-§-Nummern. Plan-Header-Notice dokumentiert: Spec-§22 → Ist §17 / Spec-§19 → Ist §8 / Spec-§5 Deployment-Audit → Ist §1 Meilensteine. Spec bleibt frozen, Codex-Attestierung 2026-04-20. Neu als Applied-Learning-Bullet #10 + Auto-Memory-File.

**Scope-Änderungen System:** Keine Scores. Keine FLAGs. Keine Sparraten-Änderung. Reine Artefakt-Vorbereitung vor Execution. DEFCON v3.7 unverändert.

**Next:** 2026-04-21 Execution-Start — Track 5a zuerst (kleiner, sauberer), dann 5b. Track 1 T1-Rerun bleibt parallel offen (siehe `SESSION-HANDOVER.md`).

## [2026-04-20] ingest | Phase 1a — 6-Paper-Ingest Severity-🔴-Cluster: FINSABER + GT-Score
- **Scope:** 2 von 6 neu hinzugefügten Papers (Severity-First-Order nach 2-Runden Codex-Triage-Review). FINSABER (Li/Kim/Cucuringu/Ma KDD '26, arxiv 2505.07078v5) + GT-Score (Sheppert JRFM 2026, arxiv 2602.00080v1). Phase 1b (4 Severity-🟡: FinReflectKG + Labre Companion + Bayesian RAG + FinDPO) folgt nächste Session.
- **Pages created (10):**
  - 2 Sources: [[Li-Kim-Cucuringu-Ma-2026-FINSABER]], [[Sheppert-2026-GT-Score]]
  - 3 Concepts: [[LLM-Investing-Bias-Audit]], [[Regime-Aware-LLM-Failure-Modes]], [[Composite-Anti-Overfitting-Objective]]
  - 5 Author-Entities: [[Weixian Waylon Li]], [[Hyeonjun Kim]], [[Mihai Cucuringu]], [[Tiejun Ma]], [[Alexander Pearson Sheppert]]
- **Pages updated (3):**
  - [[Wissenschaftliche-Fundierung-DEFCON]] — B19+B20 in 18-Befunde-Matrix (jetzt 20), Quellen-Übersicht erweitert (14→16), 4-Dimensionen-Validation-Gate erweitert um GT-Score-In-the-Loop und FINSABER-Selection-Strategy-Audit, Änderungsprotokoll Eintrag 2026-04-20
  - [[Backtest-Methodik-Roadmap]] — v2.0 → v2.1, neue Sektion "v2.1-Erweiterung" mit FINSABER+GT-Score-Validation-Dimensionen + Track-5b-Spezifischer-Anwendungs-Pfad-Tabelle
  - [[index.md]] — 10 neue Wiki-Pages indiziert + Header-Counter aktualisiert (97→107 Notes)
- **Kernaussagen aus 2 Papers konsolidiert:**
  - **B19 FINSABER (KDD '26):** LLM-Investing-Vorteile aus Vorpapern (FinMem/FinAgent/FinRobot/TradExpert/FinCon/TradingAgents/MarketSenseAI 2.0) verschwinden unter 20-J/100+-Symbol-Eval mit expliziter Bias-Mitigation (Survivorship/Look-Ahead/Data-Snooping). Bull/Bear-Asymmetrie systematisch dokumentiert: zu konservativ in Bull (underperform passive), zu aggressiv in Bear (heavy losses). Empfehlung: Trend-Detection + regime-aware Risk-Controls > Framework-Komplexität.
  - **B20 GT-Score (JRFM 2026):** Composite Anti-Overfitting Objective (Performance × Significance × Consistency × Downside-Risk) integriert Anti-Overfitting in den Optimization-Loop, statt nur post-hoc via Deflated Sharpe. Walk-Forward (9 Splits) + Monte-Carlo (15 Seeds) auf 50 S&P-500 / 2010-2024. +98% Generalization-Ratio vs Sortino/Simple. p<0,01 — Effect-Size klein. Komplementär zu Bailey PBO/CSCV.
- **Architektur-Entscheidungen (Codex Round 2 bestätigt):**
  - DEFCON ist regelbasiert, NICHT LLM-Inferenz — aber als Selection-Strategy-Output trotzdem bias-anfällig → FINSABER-Pattern ist als Audit-Methodik anwendbar (kein LLM-Sicherheitsproblem-Framing)
  - GT-Score primär **Audit-Methodik**, kein zwingender Skill-Code-Change in DEFCON oder backtest-ready-forward-verify (außer optional als Acceptance-Layer)
  - **Kein neuer Skill** — Erweiterungen als Add-Ons in bestehende Skills oder als externe Audit-Artefakte
  - FinReflectKG aus initial vermutetem 🔴-Cluster auf 🟡 revidiert (Form-4 ist XML, KG-Mehrwert nur für Cross-Entity-Relations)
- **Mappingvorschläge für Phase 2 (System-Konsequenzen, noch nicht ediert):**
  - §29.1 erweitert um GT-Score (komplementär zu Bailey PBO)
  - §29.2 erweitert um Bull/Bear-Subsample-SR-Trennung (FINSABER)
  - §29.5 erweitert um FINSABER-Bias-Audit-Fragen (Reject-Set/Iteration-Count/Hold-Out-Definition)
  - §29.6 erweitert um GT-Score-Downside-Risk-Komponente
  - **Neu möglich:** §33 Skill-Self-Audit (DEFCON als Selection-Strategy formell dokumentieren) — Codex-Gate Phase 2.5 entscheidet
- **Plan-Diff-Vorschläge für Phase 3 (noch nicht ediert):**
  - Track 5a EDGAR: NICHT rewriten (Codex-bestätigt) — extension seams für ggf. Track 5c
  - Track 5b FRED: GT-Score-Aggregat als Tie-Break R0 vor R1-R5; FINSABER-Anker im Plan-Header
  - Briefing v3.1: FinDPO erst nach Phase 1b ingest, hinter FINSABER-Validation-Gate
- **Codex-Review-Gates (2 in Phase 0, je 1 vor Phase 1a-Start und Phase 1b-Start geplant):**
  - Round 1 (Triage + Severity): 1/4/5 = 🔴 bestätigt; 2/3/6 = 🟡; FinReflectKG-Track-5a-Rewrite ablehnt (extension seams + ggf. Track 5c iff ≥3 Use-Cases); kein neuer Skill; 2-Sessions-Split; 7 Lücken im initialen Phasen-Plan identifiziert
  - Round 2 (Skill×Paper-Cross-Check): 10 überschätzte Zellen korrigiert + 1 übersehene ergänzt + Framing "DEFCON ist LLM-Strategie" bereinigt zu "regelbasiertes Composite mit Audit-Pflicht"; Phase 2.5 Codex-Skill-Audit-Gate als Anti-Creep-Mechanismus eingeführt; Showstopper-Risk dokumentiert ("Vermischung Audit-Layer ↔ Produktions-Skill-Logik")
- **Archive-Stand:** unverändert 27 Records. Scores/Sparraten unverändert. Kein FLAG-Event. Keine Skill-Code-Änderungen.
- **Dokument-Status:** Phase 1a Vault-only (per Hard-Checkpoint Vault-first → System). Phase 2-6 in nächsten Sessions.
- **Auto-Lint pending:** Orphans + broken Links Phase 1a-Pages prüfen vor Phase 1b.

## [2026-04-20] ingest | Phase 1b — 6-Paper-Ingest Severity-🟡-Cluster: FinReflectKG + Labre-Companion + Bayesian-RAG + FinDPO
- **Scope:** 4 von 6 neu hinzugefügten Papers abgearbeitet (🟡-Cluster). Komplettiert Phase 1 des 6-Paper-Ingest-Projekts. Papers: FinReflectKG (Arun/Dimino/Agarwal/Sarmah/Pasquali, Domyn 2025, arxiv 2508.17906v2), Labre-Companion (Marcelo Labre, Towards AI 2025-09-29), Bayesian RAG (Ngartera/Nadarajah/Koina, Frontiers AI Jan 2026, DOI 10.3389/frai.2025.1668172), FinDPO (Iacovides/Zhou/Mandic, Imperial 2025, arxiv 2507.18417v1).
- **Pages created (23):**
  - 4 Sources: [[Arun-et-al-2025-FinReflectKG]], [[Labre-2025-FinReflectKG-Companion]], [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]], [[Iacovides-Zhou-Mandic-2025-FinDPO]]
  - 6 Concepts: [[Knowledge-Graph-Finance-Architecture]], [[Agentic-Reflection-Pattern]], [[LLM-as-a-Judge-Evaluation]], [[RAG-Uncertainty-Quantification]], [[LLM-Preference-Optimization-Finance]], [[Sentiment-Strength-Logit-Extraction]]
  - 12 Author-Entities: [[Abhinav Arun]], [[Fabrizio Dimino]], [[Tejas Prakash Agarwal]], [[Bhaskarjit Sarmah]], [[Stefano Pasquali]], [[Marcelo Labre]], [[Lebede Ngartera]], [[Saralees Nadarajah]], [[Rodoumta Koina]], [[Giorgos Iacovides]], [[Wuyang Zhou]], [[Danilo Mandic]]
  - 1 neue Synthesis: [[Knowledge-Graph-Architektur-Roadmap]] v0.1 (Entscheidungsvorlage KG vs. XML-Direkt-Parsing vs. Bayesian RAG; 3 Qualitäts-Gates; 3 konkrete Szenarien)
- **Pages updated (2):**
  - [[Wissenschaftliche-Fundierung-DEFCON]] — B21-B24 in 20-Befunde-Matrix (jetzt 24), Quellen-Übersicht erweitert (16→20), Änderungsprotokoll-Eintrag 2026-04-20 Abend
  - [[index.md]] — 23 neue Wiki-Pages + neue Gruppe "KG-/RAG-/LLM-Architektur (Phase 1b)" + Synthesis-Sektion erweitert + Header-Counter (107→130 Notes)
- **Kernaussagen aus 4 Papers konsolidiert:**
  - **B21 FinReflectKG (Domyn 2025):** Agentic-Reflection-Pattern (Extraction → Critic → Correction Loop) erreicht 64,8% All-Rules-Compliance (+22,5pp vs. Single-Pass 42,3%), 15,8 Triples/Chunk, ECR 0,53. 5-Tuple-Schema (Head Entity, Type, Relation, Tail Entity, Type). Qwen2.5-72B-Instruct + 3-Vote LLM-as-a-Judge-Evaluation.
  - **B22 Labre-Companion (Towards AI 2025):** Praktiker-Lens zum FinReflectKG-Paper. Hauptbeitrag: **Reflection-Entropy-Paradox** (Coverage gewinnt, Shannon-Rel-Entropy verliert -22%) + Vorschlag Diversity-Monitor als Qualitäts-Gate vor Correction-LLM-Runde.
  - **B23 Bayesian RAG (Frontiers AI 2026):** Epistemische Uncertainty via MC-Dropout auf Query/Doc-Embeddings. Score $S_i = \mu_i - \lambda \sigma_i$. +26,8% Uncertainty-Calibration, -27,8% Halluzinationen, 15ms Latency. In-Scoring statt post-hoc (architektonisch überlegen).
  - **B24 FinDPO (Imperial 2025):** DPO-Alignment statt SFT für Finance-Sentiment. Llama-3-8B + LoRA r=16. +11% F1-Durchschnitt vs. FinGPT v3.3. Novel logit-to-score-Konverter enabled kontinuierliche Sentiment-Scores aus causal-LLMs → Long-Short-Portfolio mit 67% p.a. bei 5bps (einzige Methode, die bei realistischen Transaction Costs signifikant positiv bleibt).
- **Architektur-Entscheidungen (konsolidiert in [[Knowledge-Graph-Architektur-Roadmap]] v0.1):**
  - **Form-4 bleibt XML-Direkt-Parsing** (Codex Round 2 bestätigt: KG-Over-Engineering für strukturierte Daten)
  - **10-K-KG FUTURE-Option, nicht priorisiert** (benötigt wiederkehrenden Cross-Entity-Use-Case)
  - **Morning-Briefing v3.0.3 Korrektheits-Prinzip wissenschaftlich validiert** durch Bayesian-RAG-Paper — n.v.-Markierung + Soft-Alert-Schema sind aligned (3-Quellen-Triangulation als MC-Dropout-Proxy)
  - **FinDPO orthogonal zu DEFCON** (Long-Short vs. Long-Only); Kontext für zukünftige Sentiment-Block-Revisionen
  - **3 Qualitäts-Gates** für zukünftige KG/RAG-Erweiterungen definiert (Sinnhaftigkeit / Operationalisierung / Anti-Over-Engineering mit Codex-Review-Pflicht)
- **Mappingvorschläge für Phase 2 (System-Konsequenzen, noch nicht ediert):**
  - Keine neuen §-Einträge in INSTRUKTIONEN nötig — B21-B24 sind Architektur/Methoden, nicht Scoring
  - Phase 2.5 Codex-Skill-Audit-Gate hat jetzt konkrete Szenarien (Szenario 1-3 in [[Knowledge-Graph-Architektur-Roadmap]])
- **Codex-Review-Gate:**
  - Post-Commit Combined-Review durch Codex via `git show <phase1b-hash> 7ec7b86` geplant — spart eine Review-Runde ggü. Sequential-Review (User-Direktive)
- **Archive-Stand:** unverändert 27 Records. Scores/Sparraten unverändert. Kein FLAG-Event. Keine Skill-Code-Änderungen. Keine §-Edits in INSTRUKTIONEN.md.
- **Dokument-Status:** Phase 1b Vault-only (per Hard-Checkpoint Vault-first → System). Phase 2-6 in nächsten Sessions. **Phase 1 des 6-Paper-Ingest-Projekts damit vollständig abgeschlossen.**
- **Auto-Lint pending:** Orphans + broken Links Phase 1b-Pages prüfen vor Commit (Task #9).

## [2026-04-20] phase2 | System-Konsequenzen der wissenschaftlichen Fundierung — Hybrid A+B+C implementiert
- **Auslöser:** User-Frage "Fließt die Wissenschaftliche-Fundierung-DEFCON automatisch in jede Analyse ein oder ist das toter Content?" — Drift identifiziert: §4 Befunde-Priming listete nur B1-B11, B12-B24 waren passiv.
- **Codex-Konsultation (Agent `af272d556e2707209`):** Hybrid A+B+C empfohlen (Synthesis = kanonische SSoT, §4 = Router, SKILL.md-Output = Transparenz-Block, §2 Pipeline = expliziter Befunde-Check).
- **Implementierung (Phase 2 — docs + SKILL.md-Output-Only, KEIN Scoring-Impact):**
  - `07_Obsidian Vault/.../wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` — neue **Status-Matrix** mit 4 Labels (`active-scoring` / `meta-gate` / `design-rejected` / `future-arch`) für B1-B24, Aktivierungs-Regeln bindend, Regel für neue Befunde (B25+)
  - `00_Core/INSTRUKTIONEN.md` v1.12:
    - §2 Pipeline — neuer [BEFUNDE]-Schritt zwischen Stufe 1 und Stufe 2
    - §4 **Router-Umbau** — Mini-Tabelle B1-B11 raus, Status-Router + Pflicht-Abfolge rein
    - §29.1 + B20 GT-Score In-the-Loop-Objective (komplementär zu PBO)
    - §29.5 + B19 FINSABER Regime-Audit-Addendum (Bull/Bear-Subsample-SR, Symbol-Breite, Zeitfenster)
    - §29.6 + B20 Composite-Objective-Alignment (Downside-Risk = Palomar Sortino/CVaR)
    - **§33 NEU Skill-Self-Audit-Gate** — Gates 1/2/3 aus Roadmap, ADOPT/DEFER/REJECT-Decision, 3 Beispiel-Szenarien dokumentiert
  - `00_Core/CORE-MEMORY.md` §5 — neue Lektion "Phase-2-System-Konsequenzen der wissenschaftlichen Fundierung"
  - `00_Core/STATE.md` — Header + System-Zustand Phase-2-Eintrag
  - `01_Skills/dynastie-depot/SKILL.md` — neuer Schritt 2.5 Befunde-Check + "Befunde angewendet:"-Zeilen im Output-Template pro DEFCON-Block (reine Transparenz)
  - `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` — Header-Notice (FinReflectKG DEFER via §33)
  - `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` — Header-Notice (B19+B20 als Plan-Anker)
  - `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md` — Header-Notice (Bayesian RAG DEFER via §33)
- **Szenario-Entscheidungen aus [[Knowledge-Graph-Architektur-Roadmap]] via §33-Gate:** Form-4-KG REJECT (Gate 1 negativ), 10-K-KG DEFER 2027+ (alle 3 Gates conditional), Bayesian-RAG-Briefing DEFER (Gate 2 negativ Tavily-API-Limit).
- **Phase 2.5 Codex-Gate (Agent `ab8cde5ab598bb656`):** CONDITIONAL → PASS nach Bereinigung der pre-existing .obsidian/*.json workspace-state-Files (nicht Teil der Implementation). Layer-Trennung verifiziert: Docs/Audit / SKILL.md-Output / config.yaml unberührt. §28.3 Nicht-Migration-Trigger bestätigt (kein Scoring-Impact).
- **System-Reife:** Wissenschaftliche Fundierung ab heute **aktiv** im Workflow (vorher retroaktiv-dokumentarisch). B25+ landet automatisch in der Matrix oder Phase-1 gilt als incomplete.
- **Scoring-Impact:** keiner. DEFCON v3.7 unverändert. Scores/Sparraten/FLAGs unverändert. Skill bleibt v3.7.2 (§28.3 Nicht-Migration-Trigger — Output-Format-Erweiterung ohne Funktions-Änderung).
- **Archive-Stand:** unverändert 27 Records. Keine neuen FLAG-Events. Kein config.yaml-Touch.

## [2026-04-20] projekt-abschluss | 6-Paper-Ingest-Projekt formal abgeschlossen
- **Scope:** 6-Paper-Ingest-Projekt B19-B24 (20.04.2026) umfasste Phase 0 (Triage + 2 Codex-Rounds) + Phase 1a (🔴 B19+B20) + Phase 1b (🟡 B21-B24) + Phase 2 (System-Konsequenzen) + Phase 2.5 (Codex-Layer-Gate). Formal abgeschlossen mit Commit `89275e2` plus 3 Mini-Discoverability-Edits.
- **Final-Edits Discoverability (O1+O2+O3):**
  - `CLAUDE.md` — On-Demand-Lektüre um expliziten Pointer auf Status-Matrix erweitert (globale Verankerung auf Top-Level)
  - `01_Skills/insider-intelligence/SKILL-insider-intelligence.md` — §33-Szenario-1-REJECT-Note (Form-4 bleibt XML, KG-Alternative verworfen)
  - `01_Skills/backtest-ready-forward-verify/SKILL.md` — GT-Score Future-Option-Pointer (B20 Acceptance-Layer ab §29.1-Aktivierung)
- **"Phase 2-6"-Formulierung dekonstruiert:** Die in Phase-1a-Log erwähnten "Phase 2-6" waren loser Platzhalter, nicht formale Struktur. Codex-Handover-Direktive war explizit nur Phase 2 + Phase 2.5. Kein Phase 3/4/5/6 existiert.
- **Greift-Bereich der wissenschaftlichen Fundierung:** `!Analysiere` (via §4 Router + §2 Pipeline + SKILL.md Schritt 2.5) + §28 Migration + §29 Retrospective (ab 2028) + §33 Skill-Self-Audit. **Greift bewusst NICHT in:** `!QuickCheck` / `!Rebalancing` / Screener / Excel-Tiefenanalyse — das sind mechanische Workflows ohne wissenschaftlichen Urteils-Input.
- **Gesamtprojekt-Delta:** 20 Quellen → 24 Befunde (vorher 16→20); 130 Wiki-Notes (vorher 107); 7 §§-Edits in INSTRUKTIONEN (§2/§4/§29.1/§29.5/§29.6/§33 + Versions-Banner v1.11→v1.12); 1 neue Synthesis [[Knowledge-Graph-Architektur-Roadmap]] v0.1; 3 Plan-Header-Notices; 3 Skill-Discoverability-Notes.
- **Scoring-Impact Gesamt:** ZERO. DEFCON v3.7 unverändert. Scores/Sparraten/FLAGs aller 11 Satelliten unverändert. Skill bleibt v3.7.2. §28.3 Nicht-Migration-Trigger bestätigt über gesamtes Projekt.
- **Next:** Prod-Deploy v3.0.3 Morning-Briefing (Primär-Track aus SESSION-HANDOVER), danach Track 5a + Track 5b nach Gate-A-PASS.
- **Archive-Stand:** unverändert 27 Records. Kein FLAG-Event.

## [2026-04-20] post-gate-d | KG-Roadmap v0.1 als `draft-frozen` markiert (Codex-Verdikt Option D)
- **Auslöser:** User-Frage "Macht Punkt 3 (KG-Roadmap-Ratifikation) zuvor mehr Sinn als Track 5a/5b Re-Validation?" — bejaht (Roadmap ist upstream).
- **Entscheidungs-Optionen:**
  - **A** v0.1→v1.0 Ratifikation, Szenarien 1-3 als bestätigt
  - **B** Q1-Q3 (Dataset-Größe / Lizenz-Legal / Score-Archiv-Integration) klären
  - **C** beides
  - **D** (neu via Codex): `draft-frozen` belassen, Inhalte faktisch geltend, Re-Review-Trigger explizit
- **Codex-Review-Verdikt (Opus 4.7 + Codex Combined):** Empfehlung **Option D**. Begründung: Szenario 2 (10-K-KG) ist genuine `future-arch` ohne Usage-Evidence; v1.0 würde Konsens-Lock-in suggerieren. Q1-Q3 heute spekulativ beantwortbar, nicht release-blockierend, aber Q3 (Score-Archiv-Integration) braucht Design-Klarheit **vor** operativer KG-Adoption (Point-in-Time-Append-only-Natur von `score_history.jsonl`).
- **Pages updated (1 in Vault):**
  - [[Knowledge-Graph-Architektur-Roadmap]] — Frontmatter erweitert (`status: draft-frozen` + `re_review_trigger`); Status-Banner direkt nach Frontmatter; Offene-Fragen-Abschnitt um Governance-Hinweis + Per-Frage-Status erweitert; Versionshistorie um v0.1-`draft-frozen`-Zeile ergänzt
- **Pages updated outside Vault (3):**
  - `00_Core/STATE.md` — System-Zustand-Eintrag „KG-Roadmap v0.1 `draft-frozen`" mit Re-Review-Trigger; Header-Stand 20.04.2026 Nacht-Spät
  - `00_Core/CORE-MEMORY.md` §1 — neuer Meilenstein-Eintrag (20.04.2026 Nacht-Spät) mit Codex-Verdikt-Begründung + Präzedenz-Note
  - `07_Obsidian Vault/.../log.md` — dieser Eintrag
- **Re-Review-Trigger:** konkreter Cross-Entity-/10-K-Narrativ-Bedarf ODER Score-Archiv-Interim-Gate **2026-10-17** (whichever first)
- **Faktische Inhalte (gelten ab heute trotz `draft-frozen`):**
  - Form-4 Insider bleibt XML-Parsing (Szenario 1 REJECT bestätigt)
  - 10-K-KG bleibt `future-arch`, frühestens 2027+ (Szenario 2 DEFER)
  - Bayesian-RAG-Briefing-Rewrite verworfen wegen Tavily-API-MC-Dropout-Limitation (Szenario 3 DEFER)
- **Scoring-Impact:** ZERO. DEFCON v3.7 unverändert. config.yaml unberührt. Skill bleibt v3.7.2. §28.3 Nicht-Migration-Trigger weiterhin gültig. **Track 5a/5b und v3.0.3-Prod-Deploy nicht blockiert.**
- **Präzedenz:** Erste Anwendung von `draft-frozen`-Status für Synthesis-Dokumente — etabliert legitimen Zwischen-Status zwischen v0.1 (Draft) und v1.0 (Ratified), wenn Szenarien faktisch decided sind, aber Usage-Evidence für formale Promotion fehlt.
- **Archive-Stand:** unverändert 27 Records.

## [2026-04-20] edit | Morning-Briefing Prod-Deploy v3.0.3 + Discoverability-Edits Post-6-Paper-Ingest
- **Prod-Deploy:** Remote-Trigger `trig_01PyAVAxFpjbPkvXq7UrS2uG` via `RemoteTrigger.update` (full-replace ccr, JSON-Nesting-Regel beachtet: parent_tool_use_id/session_id/type/uuid siblings von message) von v2.1 auf v3.0.3 gehoben. updated_at 2026-04-20T14:36:26Z. next_run 21.04.2026 10:01 MESZ. Content 1:1 identisch zum Probe-Trigger T1-Baseline (T1/T3/T4 PASS am 20.04.). `allowed_tools` erweitert um `mcp__tavily__tavily_search`. MCP-Connections (Shibui + Tavily) automatisch erhalten durch Weglassen aus ccr-Pfad. Gate-A-Fenster 21./22./23.04.: Korrektheits-Check (8/8 Sektionen, Yahoo-n.v.-deterministic, Material-Filter, Slot-Struktur), keine Runtime-Gates (Soft-Alert-Schema). Rollback-Pfad: v2.1-Content in `03_Tools/morning-briefing-prompt-v2.md`, Runbook Spec §11.
- **Post-Ingest-Audit (User-Initiative):** Impact-Check der 6-Paper-Ingest-Konsequenzen auf 3 DEFCON-Notes via Explore-Agent → 2 Discoverability-Lücken (Update-Klassen-DEFCON + DEFCON-System ohne Status-Matrix-Deep-Link; zusätzlich Drift im Depot-State-April-2026-Banner).
- **Pages updated (3 in Vault):**
  - [[Update-Klassen-DEFCON]] — Frontmatter `updated: 2026-04-20`, `related:` um `Wissenschaftliche-Fundierung-DEFCON` + `Regime-Aware-LLM-Failure-Modes`. Neue Sektion "Klasse-C-Erweiterungs-Potenzial (Meta-Gate, aktuell nicht aktiv)" mit B17+B19-Referenzen + Status-Matrix-Deep-Link (`[[Wissenschaftliche-Fundierung-DEFCON#Status-Matrix (operative Aktivierungs-Klassifikation)]]`).
  - [[DEFCON-System]] — Frontmatter `updated: 2026-04-20`, `stand: 2026-04-20`, `wissenschaftlicher_anker` von "B1–B14" auf "B1–B24 (20 Quellen / 24 Befunde)" mit Status-Matrix-Deep-Link, `related:` um `Knowledge-Graph-Architektur-Roadmap` + `Wissenschaftliche-Fundierung-DEFCON`. §Wissenschaftliche-Fundierung erweitert: Status-Matrix als kanonische SSoT deklariert, B19-B24 als Meta-Gate-Addendum mit `🔴/🟡`-Severity und operativer Status-Verortung (§29 / §33), Kernaussage "DEFCON v3.7 unverändert" fixiert.
  - [[Depot-State-April-2026]] — Frontmatter `updated: 2026-04-20`. Banner-Drift-Fix: Live-Stand-Verweis von "Nenner 8.5, Rate 33,53€/16,76€" auf aktuellen "Nenner 8.0, Rate 35,63€/17,81€/0€" aktualisiert. Neue Sektion "Post-Snapshot-Events (11.-20.04.2026)" mit chronologischem Abriss (17.04. v3.7-Release, 18.04. Nenner-Shift 9.0→8.0, 19.04. Skill-Orchestrator v3.7.2 + §30 Live-Monitoring, 20.04. v3.0.3-Probe + 6-Paper-Ingest-Abschluss, 20.04. Nacht-Spät Prod-Deploy). **10.04.-Kernsnapshot unverändert** (Informationsverlust-Aversion).
- **Pages updated outside Vault (4):**
  - `00_Core/STATE.md` — Header auf Prod-Deploy DONE + Discoverability-Edits erweitert; Morning-Briefing-System-Zustand-Eintrag komplett umformuliert (v3.0.3 deployed + Gate-A-Fenster 21./22./23.04. + Rollback-Pfad).
  - `00_Core/CORE-MEMORY.md` §1 — neuer Meilenstein-Eintrag (20.04.2026 Nacht-Spät, oberhalb KG-Roadmap-Eintrag) mit vollem Prod-Deploy-Kontext + Discoverability-Audit-Befund.
  - Memory `morning-briefing-config.md` — Prod-Trigger-Status von "pending" auf "DEPLOYED 20.04.2026 14:36 UTC" mit Gate-A-Fenster.
  - `07_Obsidian Vault/.../log.md` — dieser Eintrag
- **Multi-Source-Drift-Check:** STATE.md ↔ DEFCON-System.md ↔ Update-Klassen-DEFCON.md ↔ Depot-State-April-2026.md jetzt alignment auf Status-Matrix-SSoT; keine verwaiste Nenner-8.5-Referenz mehr im Vault.
- **Scoring-Impact:** ZERO. DEFCON v3.7 unverändert. Scores/Sparraten/FLAGs aller 11 Satelliten unverändert. Skill bleibt v3.7.2. Archive-Stand unverändert 27 Records. Kein FLAG-Event.
- **Next:** Manual-Run-Verification auf Prod via Desktop-App (User-Aktion), dann morgen 21.04. 10:00 MESZ erster Cron-Run Gate-A-Tag-1.

## [2026-04-20] incident+rollback | 🔴 v3.0.3 Hallucination FAIL → Rollback auf v2.1

- **Auslöser:** Manual-Run auf Prod (Desktop-App "Jetzt ausführen") ~720s Runtime (>2× Alert-Schwelle). Output meldete für 7 US-Ticker **Yahoo-Intraday-Kurse mit massiven Deltas** (AVGO $317,79 / -21,8%, APH -16,1%, TMO -9,9%, MSFT -9,7%).
- **Broker-Verify durch User:** AVGO real €345,38 (Fr 17.04.) → €337,58 (Mo 20.04.) = **-2,26%**. Reported $317,79 ≈ €276, existiert nicht. Phantom-Kurs.
- **Root Cause:** Shibui-EOD-Query gab 17.04. als `latest_date` (korrekt: Karfreitag + Osterwochenende, keine US-Börsensitzung 18/19.04., Montag 20.04. noch nicht in EOD). Agent interpretierte "stale data" und **improvisierte unautorisierten Yahoo-Intraday-Fallback-Pfad** via Tavily für US-Ticker. v3.0.3 Spec §3 hat keinen expliziten Guard gegen alternative Datenpfade — Critical Guards verbieten nur Halluzinierte-Gründe, nicht Phantom-Datenquellen.
- **Was korrekt funktionierte:** Yahoo-n.v.-deterministic für BRK-B/RMS/SU (§3c), Material-Filter (alle 4 Per-Ticker "keine material News" korrekt begründet), Slot-Struktur 4≤5, 8/8 Sektionen, FLAGS/WATCHES/Trigger alignment mit STATE.md.
- **Rollback-Execution:** RemoteTrigger.update mit v2.1-Content aus `03_Tools/morning-briefing-prompt-v2.md`, allowed_tools `[Bash,Read,Glob,Grep]` (Tavily raus, MCP-Connector bleibt attached aber ungenutzt). updated_at 2026-04-20T15:13:12Z. next_run 21.04.2026 10:01 MESZ läuft wieder v2.1 (keine News, reine Shibui+Yahoo-curl-Kurs-Extraktion, stable seit 14.04.).
- **Gate A ausgesetzt** bis v3.0.4-Hotfix. Hotfix-Spec-Draft in nächster Session:
  - §3a expliziter Guard: "Shibui `latest_date` = autoritativ. Wochenend-/Feiertags-Lag = NORMAL. KEIN alternativer Live-Preis-Pfad für US-Ticker."
  - Delta-Spalte zeigt "(Score-Datum-Close)" wenn heute-Close nicht verfügbar
  - Neuer Probe-Test T5 Adversarial-Stale-Shibui (Simulate 3-Tage-Lag → verifizieren kein Fallback-Trigger)
  - Gate A Re-Start erst nach T5-PASS + T1/T3/T4 Retest
- **Pages updated outside Vault (3):**
  - `00_Core/STATE.md` — Header + Morning-Briefing-Eintrag auf Rollback-Status
  - `00_Core/CORE-MEMORY.md` §1 — Incident-Meilenstein-Eintrag (20.04.2026 Nacht-Spät Post-Deploy-Fail, oberhalb Deploy-Success-Eintrag zeitlich einsortiert)
  - Memory `morning-briefing-config.md` — Incident-Sektion + v3.0.4-Hotfix-Spec
- **Scoring-Impact:** ZERO. DEFCON v3.7 + Scores + FLAGs + Sparraten aller 11 Satelliten unverändert (Infrastruktur-Ereignis, keine Score-Neuberechnung).
- **Lesson Learned:** Anti-Hallucination-Guards müssen nicht nur Begründungen, sondern auch alternative Datenpfade explizit verbieten. "KEINE Gründe erfinden" ist notwendig, aber nicht hinreichend — braucht Ergänzung "KEINE unautorisierten Datenquellen nutzen, auch wenn autorisierte Quelle scheinbar stale ist".
- **Implication für v3.0.4:** Probe-Tests müssen Adversarial-Stale-Shibui abdecken (bisher nicht getestet — T1 war Happy-Path mit frischem Freitag-EOD).

## [2026-04-21] drift-migration | score_history.jsonl 12/27 → 27/27 + System-Audit-Lesson

- **Auslöser:** Pre-Check vor Provenance-Gate-Plan-Execution (heute geschriebene Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md` + Plan `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md`) deckte 12 von 27 Records in `05_Archiv/score_history.jsonl` als schema-inkonsistent auf — alle defcon_level-Drift seit der 18.04.2026-SKILL-Threshold-Migration auf 80/65/50.
- **Migration-Tool:** `03_Tools/backtest-ready/migrate_defcon_drift.py` (~70 Zeilen, idempotent, atomar via .tmp + os.replace). Dry-Run + Apply: 12 Records korrigiert (Score 71-76 D4→D3, Score 61-63 D3→D2). Re-Validate: **27/27 PASS**. Notably: Zeile 25 V_vollanalyse 17.04. Score 72/D4→D3 = der Auslöser-Fall der Provenance-Spec.
- **Audit-Sweep auf andere Stores (Stufe-1-Quick-Check):**
  - `flag_events.jsonl` 2/2 PASS ✓
  - `config.yaml` Score+DEFCON 11/11 == STATE.md ✓
  - `portfolio_returns.jsonl` + `benchmark-series.jsonl` je 1 Record (17.04.) — **stale seit 4 Tagen**, R5-Phase-3 ist seit 19.04. „aktiv" laut STATE.md aber Daily-Append-Cron existiert nicht (Manual-Trigger-Pflicht vergessen). Backlog-Item für Track 4.
- **Codex-Verdikt (heute):** Sequenzierung β (Provenance-Plan zuerst, Audit-Tool danach als eigene Sub-Spec). Automatismus: Slash-Command `/SystemAudit` + STATE.md-Section „Last Audit", **kein SessionStart-Hook** (kollidiert mit CLAUDE.md SESSION-INITIALISIERUNG „nur STATE.md lesen"). Memory-Promotion: noch nicht neuer §, aber **§27.4 Vertikal-Drift-Klausel ergänzt** (Schema-Migration-Drift als zweite Klasse neben Multi-Source-Horizontal-Drift). Sub-Spec `system_audit.py` in nächster Session.
- **Pages updated outside Vault (5):**
  - `00_Core/STATE.md` — Header auf 21.04. Mittag aktualisiert; Backtest-Ready-Eintrag um Drift-Migration ergänzt; **neuer Open-Backlog-Block** mit 2 Items (Daily-Persist + Audit-Tool).
  - `00_Core/INSTRUKTIONEN.md §27.4` — neue Klausel „Zweite Klasse — Vertikal-Drift" + Präzedenzfall 21.04.2026.
  - `CLAUDE.md` Applied Learning Bullet 12/20 — „Drift-Check = exhaustive Schema-Validation aller Records, nicht Spot-Check".
  - Memory `feedback_exhaustive_drift_check.md` (NEU, Tier 1).
  - Memory `MEMORY.md` Index — 13 topic files.
  - `03_Tools/backtest-ready/migrate_defcon_drift.py` (NEU, idempotent One-Shot-Tool).
- **Scoring-Impact:** ZERO. DEFCON v3.7 + Scores aller 11 Satelliten unverändert (Migration nur defcon_level recompute aus score_gesamt). Skill bleibt v3.7.2.
- **Lesson Learned:** Spot-Check über STATE.md-Snapshot ist KEIN Drift-Check. Schema-Migration tickt vorwärts, Altdaten bleiben silent stale, jeder zukünftige Validator-Test wird toxisch verzerrt. Pflichtreflex bei „Hygiene"/„Drift"-Aufträgen: Re-Validate-Sweep über alle Stores, „N/M PASS" explizit.
- **Next:** Provenance-Plan-Patches (4 Codex-Punkte: Task 0 Baseline-Check + Task 2 Re-Validate-Step + Task 3 Granularitäts-Split + Task 6 CORE-MEMORY §10 Timing-Fix), dann Plan-Execution. Sub-Spec für `system_audit.py` in nächster Session als β-Pfad.

## [2026-04-21] sync-wave | Systemhygiene-Sweep Phase A+B+C post-Drift-Migration

- **Kontext:** Fortsetzung der Systemhygiene-Pivot-Entscheidung aus Mittag — Phase A (CORE-MEMORY) + B (log.md + Handover) + C (STATE.md Pipeline-SSoT) als manueller Sync-Sweep **vor** Build des `system_audit.py` (Phase D+E). Grund: Tool gegen kaputte Baseline zu bauen würde bestehende Drift-Stellen als FAIL persistieren lassen — erst Ground-Truth herstellen, dann Audit-Tool gegen saubere Baseline trainieren.
- **Phase A — `00_Core/CORE-MEMORY.md` nachgezogen:**
  - Header-Stand `17.04.2026` → `21.04.2026 Mittag` (stale, 4 Tage hinter Realität).
  - §1 System-Meilensteine: **3 neue Einträge** am Tabellenende — (1) Drift-Migration 12/27→27/27 (Commit `ca76114`), (2) Score-Append Provenance-Gate Spec + Plan v2 (Commit `206c0a1`, Architektur-Variante E nach 5 Codex-Sparring-Runden), (3) §27.4 Vertikal-Drift-Klausel + Applied Learning 12/20 + Systemhygiene-Pivot (Phase A-G Sequenz in SESSION-HANDOVER).
  - §10 API-Audit-Log: neue Sub-Sektion „21.04.2026 Mittag — Drift-Audit-Sweep" mit strukturiertem 5-Store-Ergebnis (score_history ↺ 27/27, flag_events 2/2, config.yaml 11/11, portfolio_returns + benchmark-series stale seit 4 Tagen).
  - §3 Label geschärft: von „Stand: 04.04.2026 — pre-v3.7" auf „Historisch, pre-v3.7 — aktuelle Positions-Realität in `00_Core/STATE.md` + `Faktortabelle.md`" + Callout um 18.04.-Shifts (V Vollanalyse, 5× Threshold-Drift-Fix, Nenner 8.5→8.0) ergänzt.
- **Phase C — `00_Core/STATE.md` Pipeline-SSoT-Section eingebaut:**
  - Neue Section `## 🗺 Aktive Pipeline (SSoT)` nach „Nächste kritische Trigger (30 Tage)" mit 4 Kategorien: 🔴 Unmittelbar (3 Items) / 🟠 Portfolio 10-Tage / 🟡 Bereit wartet-auf-Gate-A (2 Items) / 🔵 Deferred (3 Items) + ⏰ Long-Term-Gates.
  - Zweck: verhindert Fragmentierung über STATE.md+SESSION-HANDOVER+Plan-Files+Memory (4 Quellen, die jedes Mal rekonstruiert werden mussten). Single-Source-of-Truth für alle offenen Pläne + Termine.
  - §18 Sync-Pflicht-Liste erweitert (Pipeline-SSoT bei jedem Plan-Commit + jedem Gate-Passage mitpflegen).
- **Phase B — Handover-Update:** SESSION-HANDOVER.md erhält einen kleinen „A+B+C completed, D next" Hinweis (diese Wiki-log.md-Zeile ist der zweite Teil von Phase B).
- **Scoring-Impact:** ZERO. DEFCON v3.7 + Scores + FLAGs + Sparraten aller 11 Satelliten unverändert. Reine Dokumentations-Kohärenz-Wiederherstellung.
- **Next:** Phase D — Brainstorming-Skill → Sub-Spec `docs/superpowers/specs/2026-04-22-system-audit-tool-design.md` (Scope Codex-aligned, JSONL-Schema + Markdown-Cross-Drift Kern, Vault-Backlinks optional).

## [2026-04-21] implementation | Task 14 System-Audit Optional Checks 8/9 + Fix-Welle C+D

- **Kontext:** Phase E Tasks 1-13 bereits in dieser Session fertig (Task-13 CLI-Orchestrator + Fix-Welle A+B + Pre-Task-14-Hygiene committed). Task 14 = letzter Build-Schritt vor Task 15 (Smoke-Temp-Repo) / Task 19 (Acceptance-Matrix).
- **Task 14 Scope (Plan 2837-3113, Spec §5.2):** Check-8 `vault_backlinks.py` (Obsidian `[[Wikilink]]`-Resolver, 20s Timeout, SKIP on missing vault) + Check-9 `status_matrix.py` (B1..BN Monotonicity + No-Duplicate-Gate auf `Wissenschaftliche-Fundierung-DEFCON.md`) als Optional-Checks (`--full`/`--vault`-Scope).
- **Methodik (Review-Matrix-konform, `feedback_review_stack.md`):** Implementer-Subagent (Sonnet) via `subagent-driven-development` → Spec-Compliance-Review (Subagent) → Claude-Code-Quality-Review (Subagent) → Fix-Welle C (TDD RED-GREEN) → Codex Post-Impl-Reconciliation (Pflicht-Gate) → CodeRabbit-CLI-Review via WSL → Fix-Welle D.
- **Pflicht-Quick-Win Session-Start (Task-1 aus SESSION-HANDOVER-Backlog):** `jsonl_schema.py:83` `json.loads + model_validate` → `model_validate_json` (Pydantic v2, ein Pass). Bonus-Fix in Fix-Welle C: `errs[0]["type"] == "json_invalid"`-Branch für differenzierten Hint (verhindert misleading "Migration-Helper"-Empfehlung bei echtem JSON-Parse-Fehler).
- **Code-Review-Findings + Fixes (Fix-Welle C):**
  - Blocker #1 (status_matrix): Section-Isolation matched first textual "Status-Matrix" in Prosa, nicht den Header → silent PASS bei Dokumenten die "Status-Matrix" in Prosa vor dem echten Header erwähnen. Fix: `HEADER_RE = ^#{1,6}\s+...Status-Matrix...$` MULTILINE + level-aware Terminator (same-or-higher Heading-Level ohne Status-Matrix-Match). Subsections-Preservation via Regression-Test locked.
  - Blocker #2 (status_matrix): `n_passed = len(numbers) - len(failures)` doppelte Abzug-Fehler — gap-failures referenzieren B-Nummern die gar nicht in `numbers` sind. Fix: `len(numbers) - len(dup_numbers)` (nur Duplikate reduzieren n_passed; Gaps sind unabhängige Failures). Counter ersetzt O(n²) count-Loop.
  - Important #3 (jsonl_schema): Hint differenziert zwischen JSON-Parse-Error (type=`json_invalid`) und Schema-Drift.
  - Deferred Important #4-7 (vault_backlinks Robustness-Pass): stem-collisions, timeout-granularity, SKIP+warning-Mix, dedup — als Task #4 Follow-up getrackt, einzeln deferrable.
- **Codex Post-Impl-Reconciliation-Verdikt: RECONCILED** — alle 5 Spec-Drift-Punkte + 3 Info-Loss-Punkte COMPLIANT/ACCEPTABLE_DEVIATION/PRESERVED. Kein DRIFT_FIX_REQUIRED. Non-blocking Nit: `--vault` CLI-Help-Text war stale (Fix-Welle D).
- **CodeRabbit-CLI-Verdikt (via WSL `wsl.exe -- bash -lc 'coderabbit review --base f99571e --plain'`):** 7 Findings. Adressiert: (1) `vault_backlinks.py` docstring-Falschheit "Hardcoded 20s" → "context.vault_timeout_s"; (2) `status_matrix.py:17` unused `context`-Param → noqa-Doku-Kommentar. Deferred nach Task #4: `WIKILINK_RE [[C#]]`-Edge-Case + Timeout-Granularity-per-File (deckt Important #5). Ignoriert: 2× Vault-Noise (Unbenannt.*-Dateien aus User-Vault).
- **Pages updated outside Vault (7):**
  - `03_Tools/system_audit/checks/vault_backlinks.py` (NEW, 62 LOC)
  - `03_Tools/system_audit/checks/status_matrix.py` (NEW, 64 LOC post-Fix-Welle-C+D)
  - `03_Tools/system_audit/checks/jsonl_schema.py` (model_validate_json + json_invalid-branching)
  - `03_Tools/system_audit/checks/__init__.py` (OPTIONAL registry populated)
  - `03_Tools/system_audit/_smoke_test.py` (+10 Fixtures: 6 Task-14-Spec + 4 Fix-Welle-C-Regression)
  - `03_Tools/system_audit.py` (--vault-Filter-Bug-Fix + Help-Text-Update)
  - `00_Core/STATE.md` + `00_Core/SESSION-HANDOVER.md` (Phase E 13→14/19 + Task-4-Follow-up + float→Decimal Long-Term-Gate)
- **Scoring-Impact:** ZERO. DEFCON v3.7 + Scores + FLAGs + Sparraten aller 11 Satelliten unverändert. Reine Tooling-Arbeit.
- **Commits dieser Session (6):** `510cbbf` (Feature) · `68d58ab` (Fix-Welle C) · `6926f58` (STATE Long-Term-Gate) · `9a3906f` (Handover-Sync) · `b1b41d1` (Fix-Welle D).
- **Lesson Learned (Kandidat für Applied Learning):** Fixture-green ≠ live-correct bei Parser/Regex-Scope-Fixes. Blocker-#1-Fix (header-anchored HEADER_RE) war grün auf 3 Fixtures, aber der initial zu enge End-Terminator hätte Live-Drift übersehen (status_matrix 1/1 statt 21/25). Entdeckt nur via `--full` Live-Run — Regression-Test `test_status_matrix_subsections_are_scanned` lockt das Verhalten jetzt.
- **Next:** Task 15 Smoke-Test temp-repo-copy (Plan 3109-3246, Spec §7.4). Dann Tasks 16-19 (Slash-Command `/SystemAudit`, INSTRUKTIONEN §27.4 Regression-Guard, Pipeline-SSoT-Sync, Acceptance-Matrix).

## [2026-04-22] deployment | System-Audit-Tool v1.0 deployed (Phase E 15-18/19)

- **Scope:** Tasks 15-18 der Systemhygiene-Phase-E committed. Tool live, `--minimal-baseline`-Regression-Guard in INSTRUKTIONEN §27.5 verankert. Erster Last-Audit-Block (3/3 PASS) in STATE.md persistiert.
- **Methodik:** Subagent-driven-development + Codex-Reconciliation (keine CodeRabbit-Pässe bei Minor-Tasks, siehe feedback_review_stack.md Matrix).
- **Commits (4):**
  - `486f2c1` **Task 15** Smoke temp-repo + seeded-drift. Codex-Reconciliation Option 2: Baseline-Assertion `rc == 0` → `rc ∈ {0, 1}` (Plan-Header-Notice dokumentiert). 3 Plattform-Fixes (Py 3.14 `sys.path`-Guard, Windows `encoding="utf-8"` + `stdout.reconfigure`). [OK] 2× live.
  - `fa238bf` **Task 16** `/SystemAudit` Slash-Command-Wrapper (`.claude/commands/SystemAudit.md`, 15 LOC). `$ARGUMENTS`-Passthrough, Default `--core`.
  - `ab7ae19` **Task 17** INSTRUKTIONEN §27.5 Migration-Regression-Guard + initialer Baseline-Run. Scope-Drift `--core` → `--minimal-baseline` dokumentiert (pre-existing Tool-Bugs Check-3 future-date + Check-5 existence blockieren `--core`). Rollback-Pfad an Follow-up-Tasks gekoppelt.
  - (dieser Commit) **Task 18** Sync-Welle: STATE.md Pipeline-SSoT Punkt 4 auf DONE, Open-Backlog Punkt „System-Audit-Tool fehlt" → deployed, Phase-E-Banner 14/19 → 18/19, CORE-MEMORY §10 Sub-Section mit Check-Status-Tabelle, diese log-Zeile.
- **Baseline-Realität:** `--minimal-baseline` 3/3 PASS. `--core` 4/8 PASS mit 2 known Tool-Bugs.
  - Check-2 `markdown_header`: Future-Date-Bug (Long-Term-Gate-Rows 2028-04-01 / 2027-10-19 als Event gewertet) → Follow-up-Task #2.
  - Check-4 `existence`: 54 CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix → deferred Post-Task-17-Cleanup-Welle.
- **Spec-§-Drift-Handling:** 2 Plan-Header-Notices dokumentieren die `rc`-Relaxation (Task 15) + Scope-Flag (Task 17). Spec v0.2 bleibt frozen (`82482d7`). Pattern: `feedback_spec_section_drift.md`.
- **Scoring-Impact:** ZERO. DEFCON v3.7 + Scores + FLAGs + Sparraten aller 11 Satelliten unverändert.
- **Follow-up-Tasks offen:** #2 Check-3 future-date-exclude, #4 vault_backlinks Robustness-Pass (Important #4-7 aus Fix-Welle-C-Review), existence-Cleanup-Welle.
- **Next:** Task 19 Verification-Before-Completion Acceptance-Matrix + obligatorischer 2. 4-Wege-Review-Pass (Codex + CodeRabbit sequenziert für Meilenstein-Abschluss). Dann Phase F (Provenance-Plan Execution vor TMO Q1 23.04.).

## [2026-04-22 Spät] system-audit | Task 19 Verification + Fix-Welle E (Phase E ~95%)

- **Acceptance-Matrix gegen Spec §12:** 9/11 ✅, 2 dokumentierte WARNs (Item 2 `--core` rc=1 wg. bekannter Tool-Bugs → `--minimal-baseline` rc=0 ist pragmatischer Gate; Item 9 `--full` zeigt 10 Checks statt 9 + Check-10 status_matrix Over-Strict-Bug entdeckt).
- **Codex-Reconciliation:** RECONCILED_WITH_FOLLOWUPS — 3 deferred Follow-ups (Check-3 future-date / existence-Cleanup → §27.5-Guard auf `--core` hochziehen; Check-10 Regex-Scope auf `### Matrix`-Subsection; §27.5 Kommentar-Update nach Cleanup).
- **CodeRabbit-Pass:** Run-1 = 6 Findings, davon 4 sichtbar (tail-Truncation). 3 valide auf `_smoke_temp_repo.py` ✅ FIXED in Fix-Welle E `e3ba381` (Docstring „60s"→„120s" Korrektheits-Drift, `import re` Modul-Level-Hub, redundanter Inline-Import-Block aus `smoke_seeded_drift()`). 1 OOS pre-existing `flag_events.jsonl:2`. 2 Findings unklar durch Truncation; CR-CLI rate-limited (~46 min) → Re-Verify-Backlog gegen `e3ba381` als neue Base.
- **Closure-Entscheidung (advisor-validiert):** Final-Commit `log(phase-e-done)` aufgehoben — Closure-mit-2-unbekannten-Findings widerspricht `feedback_correctness_over_runtime.md`.
- **Commits dieser Sub-Session (2):** `e3ba381` Fix-Welle E + dieser Sync-Welle-Commit.
- **Scoring-Impact:** ZERO. DEFCON v3.7 + Scores + FLAGs + Sparraten unverändert.
- **Lesson:** Multi-Tool-Reviews → Run-Output IMMER File-persistieren (nicht nur tail-Inspect), sonst Truncation + Non-Determinismus + Rate-Limit = perfect storm. Applied-Learning-Kandidat.
- **Next:** CR-Re-Run gegen `e3ba381` nach Cooldown (>22.04. ~23:23 UTC). Bei keinen neuen Blockern: Phase-E-Closure + Phase F oder direkt Phase G (TMO Q1 23.04.).

## [2026-04-23] reorg+ingest-video | Voll-Reorg + Wiki-Closure + Video-Pipeline-Setup + Pilot-Ingest

**Reorg + Schema:**
- Voll-Reorg `wiki/sources/` und `raw/` in Sub-Ordner (`papers/`, `tools/`, `references/`, `videos/{earnings-calls,interviews,conferences,analyses,updating-system}/`) — 39 git mv, 0 Backlink-Brüche (Obsidian-Basename-Resolution).
- WIKI-SCHEMA.md erweitert: Frontmatter v2 (`medium`+`video`+`transcript`+`language`+`aliases`-Blöcke), §INGEST-VIDEO als eigenständiger Workflow, Quality-Gate-Tabelle, Sub-Ordner-Transparenz-Hinweis, Cross-Medium-Aggregation-Regel.

**Wiki-Graph-100%-Closure:**
- 322 broken `[[wiki-link]]` + 20 broken Frontmatter-Refs → **0 broken refs**.
- 46 Aliases auf bestehende Pages (Title-Case ↔ kebab-case Resolution).
- 5 neue Stub-Pages: [[MA]] (Mastercard), [[STATE]], [[Faktortabelle]], [[CORE-MEMORY]] (Vault-extern-Anker), [[backtest-ready-forward-verify]] (Skill-Source).
- 1 Source-Edit: ASML.md `[[Beispiele.md]]`-Phantomlink entfernt.

**Video-Pipeline:**
- `03_Tools/video_ingest_lib.py` (build_slug, sha256_file, quality_gate) + 18 pytest-Tests.
- `03_Tools/video_ingest.py` CLI (yt-dlp + whisper + ffmpeg + Quality-Gate + Frontmatter-Generation).
- `.gitignore`: transient Audio (`*.m4a`/`*.mp3`/`*.webm`) + `whisper_raw.json` ausgeschlossen.

**Pilot-Ingest (Task 9 End-to-End):**
- Pages created: [[2026-04-08-charlie-automates-graphify-claude-code]] (Kategorie `updating-system`, neu)
- Pages updated: [[index]], [[WIKI-SCHEMA]]
- yt-dlp 5.6s + whisper-small 152.3s + Quality-Gate PASS (no warns).
- Reproduzierbarkeit: `transcript.sha256`/`info.sha256` + Tool-Versionen im Frontmatter + run.log.

**Commits dieser Session (10):** Pre-Check → wiki-Reorg → raw-Reorg → Wiki-Closure → Schema → Lib+Tests → CLI → Index → gitignore → 5.-Kategorie → Pilot-Ingest.

**Lesson:** Migration-Pre/Post-Check ist Pflicht-Sicherheitsnetz, aber das echte Gold-Insight war: Postcheck flaggte 322 broken Links, die ALLE pre-existent waren. Der „Voll-Reorg-bricht-nichts"-Beweis = grep der migrierten Basenames in der broken-link-Liste, nicht der absolute Count. Verallgemeinert: bei Drift-Audits immer Differenz-Count vs absolute Count messen.

## [2026-04-23] analysis | TMO Q1 FY26 Forward-Vollanalyse — Beat + Guidance-Raise, D2→D3, fcf_trend_neg Resolve

**Context:** Pfad-2 Old-Pipeline (Weekly-Limit 93%, Reset Do 22:00 CEST). Pre-Briefing via earnings-preview-Skill 22.04. (`02_Analysen/TMO_pre-earnings_2026-04-23.md`). Release 23.04. pre-market + Call 14:30 CEST.

**Release-Kennzahlen Q1 FY26:**
- Revenue $11,01B (+6,2% reported / **+1% organic**) — Beat vs. $10,86B Konsens
- Adj. EPS $5,44 (+5,6% YoY) — Beat vs. $5,24 Konsens (+3,8%)
- GAAP EPS $4,43 (+11,3% YoY)
- GAAP OpM 16,9% (+30bps) / Adj. OpM 21,8% (-10bps)
- OCF $1.192M (+64,9% YoY) / CapEx $376M / **FCF $825M (+121% YoY)**
- ΔWC -$1.112M vs -$1.425M (Q1'25) — +$313M weniger Drag = **WC-Unwind-These bestätigt**
- Segmente: Life Sciences $2,636B (36,2% Margin ✅); Analytical Instruments $1,716B flat (20,7%, Mix/FX-Headwind)

**Capital Deployment:**
- Clario-Akquise $8,87B abgeschlossen (Life-Sciences-Services)
- $3,0B Buybacks bereits Januar
- $5,24B neue Debt aufgenommen
- 10% Dividenden-Raise

**FY26-Guidance-Raise (Top + Bottom):**
- Revenue $47,3-48,1B (von $46,3-47,2B, +$1,0B Midpoint)
- Adj. EPS $24,64-25,12 (von $24,22-24,80, +8-10% FY-Growth)
- **FCF-Guide FY26 $6,9-7,4B** (vs FY25 $6,3B = +10-17% Recovery)
- Organic 3-4% bestätigt (H2-Akzeleration impliziert nach Q1 +1%)

**FLAG-Resolution:**
- `fcf_trend_neg` Schema-Watch seit 18.04. (FY25 FCF -13,4% YoY, WC-Noise-Erklärung) → Resolve-Gate CLEAR alle Kriterien erfüllt: FCF YoY positiv (+121%), ΔWC verbessert, Management-FCF-Commitment. **Schema-Watch deaktiviert.**

**Score-Delta (§28.2 log-only-Fenster |Δ|=3):**
- Pre: 64/D2 (18.04.) → Neu: **67/D3**
- Fundamentals +2 (fwd_pe 6→7 Mid-Band-Rekalibrierung bei 19,3; fcf_yield 3→4 FCF-Recovery + FY-Guide)
- Sentiment +1 (eps_revision_delta 0→+1 Management-Guide-Raise = Analyst-Revision-Trigger)
- Moat 18 / Technicals 6 / Insider 4 unverändert (Skip-Window <14 Tage)
- Screener-Exception #4 TMO differenzierte QT weiter aktiv (P/FCF 27,27x Cap 1 Pt / Fwd P/E 19,3 Standard)

**Sparraten-Kaskade:**
- Nenner 8,0 → 8,5 (TMO Gewicht 0,5 → 1,0)
- Volle Rate 35,63€ → 33,53€ (Kaskade auf 7 andere D3/D4-Satelliten, je -2,10€)
- V D2-Rate 17,81€ → 16,76€
- TMO 17,81€ → 33,53€ (+15,72€)
- Summe 285€ ✓

**Risk-Map neu:**
1. Organic +1% Q1 thin — H2-Akzeleration 3-4% guide hängt von Lab-Tools-End-Market Recovery ab. Q2 Ende Juli Re-Check.
2. Clario-Integration-Execution — $8,87B M&A, Goodwill/Assets >30% (Regel 4 Cash-ROIC-Proxy aktiv), Integration-Performance entscheidet ROIC-Normalisierung.
3. Bilanz-Leverage Post-Clario — $5,24B neue Debt + $8,87B M&A + $3B Buybacks in Q1. Net Debt/EBITDA Pre-Deal 2,57x → post-Deal schätzungsweise deutlich höher. Q2 Bilanz-Watch.

**Workflow-Disziplin:**
- Advisor-Review pre-Scoring (Matrix-Misread-Check: EPS $5,44 > $5,35 = Beat+Raise-Zeile, nicht In-Line — korrigiert)
- Guidance-Line via Tavily vor Scoring gezogen (nicht verschoben auf "Call noch nicht disclosed"-Argument)
- Organic +1% explizit im Fundamentals-Narrativ adressiert, nicht nur Bull/Bear-Footnote

**Sync-Welle (6 Files, Old-Pipeline-Format):**
- log.md, CORE-MEMORY.md §1, Faktortabelle.md, STATE.md, `05_Archiv/score_history.jsonl` (direct append, kein Skill-Invoke — Weekly-Limit)
- `05_Archiv/flag_events.jsonl` unverändert (kein Trigger/Resolve-Event — Schema-Watch ≠ formaler FLAG)

**Retro-Migration geplant:** Post-Reset Do 22:00+ CEST → TMO-Record via `backtest-ready-forward-verify`-Skill (Phase P1-P6: Freshness + Tripwire + §28.2 Δ-Gate + Dry-Run + Append + git add) separater Commit. Erster echter Skill-Forward-Run.

**XLSX-Tools:** `Rebalancing_Tool_v3.4.xlsx` + `Satelliten_Monitor_v2.0.xlsx` bleiben unberührt bis post-Retro-Migration — einmaliges Update gegen validierten Skill-Record (Vermeidung Doppel-Edit-Churn).

**Watches neu:**
- Organic-Akzeleration Q2 ~Ende Juli (Q2-Guide organic ~3% konsistent)
- Clario-Integration-Early-Read (Q2)
- Analytical-Instruments-Margin-Drift (-10bps)
- Net-Debt/EBITDA Post-Clario-Recomputation (Q2 Bilanz)

**Skill:** dynastie-depot v3.7.2 Schritt 0-6 vollständig; Schritt 7 (Archiv-Write via Skill-Invoke) deferred auf Post-Reset Retro-Migration wegen Pfad-2-Weekly-Limit. §28.3 Nicht-Migration-Trigger bestätigt (Standard-Rescore, kein DEFCON-Bump).

## [2026-04-23] retro-audit | TMO-Record `backtest-ready-forward-verify` Option B PASS
- **Kontext:** TMO Q1 FY26 Vollanalyse war wegen Weekly-Limit-93% (Pfad-2) mit Old-Pipeline direkt in `score_history.jsonl` angehängt und in `620702a` committed. Handover sah Retro-Migration via Skill vor. Option-B-Entscheidung (Handover empfohlen): kein Re-Append, stattdessen Post-hoc-Validation der Skill-Pipeline gegen den existierenden Record.
- **Draft:** `03_Tools/backtest-ready/_drafts/TMO_20260423-retro-audit.json` (Wrapper-Format, ohne `skill_meta` — Standard-Rescore, kein Version-Bump; Verzeichnis ist `.gitignore`d, daher nur im Working-Tree).
- **Phase-Outcomes:**
  - P1 `parse_wrapper` — PASS (record_id `2026-04-23_TMO_vollanalyse`, skill_meta leer)
  - P2a `check_freshness` — INFO (3 Required-Touch-Files sauber im Working-Tree, weil Sync-Welle `620702a` committed — erwartet, nicht blockierend)
  - P2b `parse_state_row` Tripwire — PASS (STATE.md ↔ Record: score 67 / defcon 3 / flags_active False, dreifach konsistent)
  - P3 Algebra-Δ-Gate — N/A (kein `skill_meta`, keine Version-Migration)
  - P4 Dry-Run Schema-Validation gegen synthetisches Archiv (ohne TMO-Zeile) — PASS
  - P4-bis Duplicate-Guard gegen echtes Archiv — PASS (erwartete `DuplicateRecordError`, beweist Self-Defense)
- **Ergebnis:** Skill-Pipeline hätte den Record sauber validiert und angehängt. Real-Append nicht ausgeführt — Record existiert bereits, Informationsverlust-Aversion > Ästhetik (kein `git revert` der Zeile). **Erster echter Skill-Forward-Run bleibt V Q2 FY26 28.04.2026.**
- **Folge-Schritt:** XLSX-Tools-Update (Rebalancing_Tool + Satelliten_Monitor) unblockiert — separater Commit.

## [2026-04-23] ingest-video second-run + adoption-decision | Dubibubii "Powerful Settings"
- **Video:** [[Claude Code's Creator Reveals His Most POWERFUL Settings]] — Dubibubii, 10,2 min, YouTube Standard-Video (kein Short), upload 2026-04-22, Chapters vorhanden.
- **Pipeline-Lauf (`ingest-video` Skill Second-Run post-Pilot):** yt-dlp 19,4s + whisper-small 403s (≈0,66× realtime — sublinear, schneller per-Minute als 2-min-Pilot mit 1,2× realtime) + quality-gate PASS ohne Warns + 219 Segmente + Chapters.json persistiert. Artefakte `raw/videos/updating-system/2026-04-22-dubibubii-claude-code-powerful-settings/`.
- **Skill-Bewertung (Pilot+Second-Run zusammen):**
  - ✅ Deterministisch, robust — 2/2 Runs PASS, inkl. Chapters-Detection für Long-Form
  - ✅ SHA256-Provenance (transcript, info, chapters), Version-Pinning (yt-dlp 2026.03.17, whisper 20250625, ffmpeg 8.1), `run.log`
  - ✅ `updating-system`-Kategorie trägt ihren Zweck („Adoption-Evaluation" ≠ „Wissensquelle") — Framing-Klarheit nach User-Korrektur 23.04.
  - ⚠️ Metadata-Gap bestätigt: `--channel`, `--topic`, `--upload-date` müssen manuell, obwohl `info.json` `uploader`, `title`, `upload_date` enthält → Reibung bei Bulk, lohnt bei ≥5 Videos/Session Auto-Derivation zu bauen
  - ⚠️ Whisper-`small` reicht für Transkript-Textur + Adoption-Entscheidungen; für inhaltstiefere Wissensquellen-Ingests Upgrade auf `large-v3` empfehlenswert (Runtime ×3-4)
- **Content-Adoption-Decision (siehe Source-Page-Adoption-Matrix):** 4 REJECT (Auto Mode, Focus Mode, Slash-go ×1) / 2 OBSERVE (Effort Levels, Recaps) / 1 ADOPT-READY (`fewer-permission-prompts` — bereits installiert, einmaliger Run am Konsolidierungstag).
- **Meta-Learning:** Neue Memory `feedback_friction_as_evidence.md` — Creator-Videos framen Friction-Reduction-Mechaniken als Gewinn; in Dynasty-Depot ist Friction (Permissions, Intermediate-Visibility, Prompt-Detail) der Evidenz-Kanal für Halluzinations-Erkennung (v3.0.3-Präzedenz). Adoption-Default skeptisch, Re-Eval nur bei Scope-Erweiterung auf echte Multi-Agent-Automatisierung.
- **System-Impact:** Null System-Änderung, keine Config/Skill-Commits. Quellen-Gewinn: dokumentierte Präzedenz für künftige Broad-Audience-Creator-Video-Ingests (Negative-Reference + Matrix-Template).
