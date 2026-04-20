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
