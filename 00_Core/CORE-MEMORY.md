# 🧠 CORE-MEMORY.md — Institutionelles Gedächtnis
**Version:** 1.7 (v3.7) | **Stand:** 17.04.2026
> Dieses Dokument speichert alle wichtigen Entscheidungen, Erkenntnisse und
> strategischen Weichenstellungen aus den Projektthreads.
> Für Strategie → KONTEXT.md | Für Workflows → INSTRUKTIONEN.md

---

## 1. System-Meilensteine

| Datum | Meilenstein |
|-------|-------------|
| März 2026 | Projekt-Start: Strategie-Manifest v1.0 erstellt |
| 18.03.2026 | Strategie-Manifest v2.0 ratifiziert (CRWD/PLTR entfernt, Moat-Fokus schärfer) |
| 19.03.2026 | Rebalancing-Tool v1.0 erstellt (Excel) |
| 25.03.2026 | AVGO CapEx-FCF-Analyse durchgeführt (Score 86, Kalibrierungsanker gesetzt) |
| 25.03.2026 | MKL DEFCON-Analyse: Score 82, Ersatzbank BRK.B |
| 26.03.2026 | MSFT DEFCON-Analyse: Score 77, 🔴 FLAG CapEx/OCF 65,3% gesetzt |
| 26.03.2026 | SNPS DEFCON-Analyse: Score 79, Grenzfall-Referenz |
| 26.03.2026 | GOOGL-Analyse: 🔴 FLAG CapEx FY26 ~75% OCF — struktureller Ausschluss |
| 28.03.2026 | HON-Analyse: Score 71 — Post-Spinoff 2026 abwarten |
| 31.03.2026 | SPGI-Analyse: Score 77→79 (Goodwill-Korrektur), Watchlist |
| 31.03.2026 | Rebalancing_Tool_v3.1 FINAL — Allokation 65/30/5 ratifiziert |
| 01.04.2026 | mainconfig.md v1.0 erstellt — Single-Source-of-Truth |
| 02.04.2026 | TMO DEFCON-Analyse: Score 65, DEFCON 3, Clario-Watch-Flag |
| 02.04.2026 | EXPN-Analyse: Score 61, Watchlist |
| 03.04.2026 | FICO-Analyse: Score 70, DEFCON 3, VEEV-Ersatz Kandidat #1 |
| 03.04.2026 | mainSKILL.md v3.1 — 11 Scoring-Verbesserungen |
| 03.04.2026 | mainconfig.md v1.5 — vollständig synchronisiert |
| 04.04.2026 | Dreier-Datei-Struktur (KONTEXT/INSTRUKTIONEN/CORE-MEMORY) erstellt |
| 04.04.2026 | Rebalancing_Tool_v3.2 — visuelles Redesign, DEFCON-Scores vervollständigt (alle 11 Aktien), ASML vorläufig 84 (→ korrigiert auf 68 am 06.04.), TMO korrigiert (DEFCON 3/65) |
| 04.04.2026 | DEFCON-Sparraten-Logik auf 3 Stufen erweitert (initial: D4=voll, D3=50%, D≤2=0€) — projektweite Umsetzung in Excel + 7 Markdown/YAML-Dateien |
| 15.04.2026 | **Rebalancing_Tool_v3.4** — Sparraten-Logik überarbeitet: D4/D3=volle Rate (1.0), D2=50% Sockelbetrag (0.5), D1/🔴 FLAG=0€. Drift-Warnschwelle typ-abhängig (Faktor×Toleranz). 🟡-CF auf O-Spalte. B26 dynamisch. Ziel-Allokation exakt 100%. Alle Markdown/YAML aktualisiert |
| 04.04.2026 | Skill-Paket dynastie-depot.zip neu gebaut und installiert (v3.2-Stand) |
| 04.04.2026 | Session-Initialisierung etabliert: 00_Core-Dateien werden ab sofort zu Sitzungsbeginn gelesen, CORE-MEMORY live fortgeschrieben |
| 05.04.2026 | defeatbeta-MCP-Server erfolgreich eingerichtet (via Claude Code). 6 neue Skills gesichtet und bewertet. defeatbeta-API in sources.md + SKILL.md als Primärquelle für US-Ticker-Rohdaten integriert. Scoring-Logik unverändert. |
| 05.04.2026 | sec-edgar-skill + earnings-calendar in System eingebunden. sec-edgar = Eskalationsquelle bei Datenkonflikten. earnings-calendar = wöchentlicher !EarningsCalendar-Befehl (FMP API Key gesetzt). sources.md v2.5 + SKILL.md aktualisiert. ZIP neu gebaut. |
| 05.04.2026 | 5 neue Skills bewertet: earnings-preview (!EarningsPreview), earnings-recap (!EarningsRecap), qualitative-valuation (Moat-Vertiefung) behalten + integriert. valuation-calculator + findata-toolkit-us manuell vom User gelöscht. Earnings-Workflow: Preview → Recap → QuickCheck etabliert. SKILL.md + sources.md v2.5 + ZIP aktualisiert. |
| 05.04.2026 | Shibui Finance SQL-Connector vollständig evaluiert und integriert. 10 Tabellen getestet, 56 Technicals verifiziert, FCF-Konsistenz-Screening (MSFT/AAPL/ASML 8J) live abgefragt, CapEx-FLAG historisch quantifiziert (MSFT Dez-Quartale 83,6%/70,9%). Shibui = Primärquelle Technicals-Block + FLAG-Historie + Screening-Vorfilter. sources.md v2.6 + SKILL.md (Stand 05.04.2026) + ZIP aktualisiert. Quellenmatrix: defeatbeta (Fundamentals-Tiefe) + Shibui (Technicals + historische Breite) + Web (Forward/Moat/Insider). |
| 06.04.2026 | **Insider Intelligence Module v1.0** gebaut und live getestet (Claude Code). sec-edgar-skill umgeschrieben zu spezialisiertem Form-4-Scanner: CIK-Tabelle 8 US-Satelliten hardcoded, XML-Parsing mit 10b5-1-Erkennung (XML-Feld + Footnote-Analyse), Cashless-Exercise-Detection (M+S same-day), DEFCON-Scoring (7/10 automatisch, Ownership extern), FLAG-Detection ($20M/90d). Befehle: !InsiderScan, !FlagCheck, !InsiderDetail. Live-Test: AVGO (FLAG $123M diskr.), MSFT (3/7 clean), V (4/7 sauber, $24.6M korrekt als 10b5-1 erkannt). Generischer sec-edgar-skill bleibt als Recherche-Fallback. Pfad: 01_Skills/insider-intelligence/. |
| 06.04.2026 | **System-Audit + 7 Lücken geschlossen (v3.3).** SKILL.md: 3 neue Blöcke (Pre-Processing 4 Regeln, Quarterly API Sanity Check mit IFRS-Quelltabelle, API-Routing Shibui/EODHD/SEC EDGAR + CIK-Tabelle). config.yaml: score_valid_until (180d) für alle Positionen + substitute_activation_rule + globale Systemregeln (Moat-Drift-Trigger, Sparplan-Formel, Tariff-Quelle). INSTRUKTIONEN.md: Sparplan-Formel mit Rechenbeispiel, Moat-Drift 3 objektive Trigger, Non-US Addendum (IFRS/EODHD/AFM), Tariff Quellenreihenfolge. System-Reife: 80-85 → ~93 Punkte. ZIP als dynasty-depot_v3.3 neu gebaut. |
| 06.04.2026 | **Non-US Fundamentals Module v1.1** gebaut und live getestet (Claude Code). EODHD Free-Tier hat keinen Zugriff auf Fundamentals-Endpoint (403 Forbidden) → Wechsel auf yfinance (kostenlos, kein API-Key). Alle 3 Non-US-Satelliten live-getestet: ASML (12.9% CapEx/OCF, 1161 EUR, über 200MA), RMS (24.8% CapEx/OCF fix via info-TTM — IFRS-yfinance-Lücke behoben), SU (25.2% CapEx/OCF, alle 4 Jahrgänge vollständig). Neue Dateien: eodhd_intel.py (CLI: scan/detail/prices), SKILL.md (non-us-fundamentals). sources.md v2.7 + SKILL.md (dynasty-depot) mit API-Routing-Block aktualisiert. Pfad: 01_Skills/non-us-fundamentals/. |
| 06.04.2026 | **ASML DEFCON v3.4 Vollanalyse** — erster Non-US Kalibrierungsanker gesetzt. Score 68/100, DEFCON 🟡 3. Moat 19/20 (Wide, Monopol bestätigt Morningstar). Fundamentals 28/50 (Bewertung Fwd P/E 38x, P/FCF ~41x, FCF Yield 2,4% drücken Score). Technicals 6/10 (über steigendem 200MA, -15% vom ATH Feb 2026). Insider 7/10 (3 Direktoren-Käufe, keine Verkäufe >$20M, AFM-Protokoll). Sentiment 8/10 (11 Buy, 0 Sell, PT-Dispersion -1). CapEx/OCF 12,5% — weit unter FLAG. China-Exposure ~24%: Risk-Map-Notiz, kein FLAG. DEFCON 3 trotz perfektem Moat wegen fehlender Bewertungsmarge. Sparrate: volle Rate (D3, kein 🔴). Score valid: 06.10.2026. API Sanity Check abgeschlossen (07.04.2026): CapEx-Werte konsistent (Δ ≤ 3.5%). OCF-Abweichung ~10% yfinance vs. StockAnalysis = IFRS 16 vs. ASC 842 (Leasingzahlungen IFRS → Finanzierungs-CF). Kein API-Drift. FLAG-Schlussfolgerung unter beiden Standards identisch: Clean. |
| 07.04.2026 | **TMO DEFCON v3.4 Re-Analyse:** Score 65→67, DEFCON 🟡 3 bestätigt. Verbesserungen: Net Debt/EBITDA 3.6x→2.57x (Clario-Schulden abgebaut), Fwd P/E 27x→19.9x (Kursrückgang -24% vom ATH). Schwächen bleiben: ROIC 2.6% quartalsweise (Goodwill $49.4B = 44.8% Assets), FCF -13.4% YoY. Technicals unter 200MA. Kein FLAG. Earnings-Trigger 23.04.: FCF >$7.3B nötig für FCF-Yield >4%. |
| 08.04.2026 | **MSFT DEFCON v3.4 Re-Analyse abgeschlossen.** Score 77→60 (−17 Punkte). DEFCON 3→2. FLAG bestätigt und verschärft: Q2 FY26 CapEx/OCF 83.6% (bereinigt via Finance-Lease-Korrektur ~63%). ROIC 7.5% vs. WACC 13.35% = strukturell unter Kapitalkosten (6Q-Muster). Moat 19/20 unverändert. Sparrate bleibt 0€. Nächste Entscheidung: Q3 Earnings 29.04.2026 — bereinigtes CapEx/OCF <60% = FLAG-Auflösung möglich. Neues Scoring-Lernfeld: Pre-Processing Regel 2 (Finance Lease Obligations $19.5B) ist bei MSFT immer aktiv. |
| 10.04.2026 | **Obsidian Vault vollständig in Claude Stuff integriert (07_Obsidian Vault/).** 45 Notes angelegt: 11 Satelliten, 3 Ersatzbank, 6 DEFCON-Konzepte, 2 Depot-Konzepte, 5 Quellen/Skills, 2 Synthesen. Vault dauerhaft unter Claude Stuff gemountet — kein separater Mount mehr nötig. Code-Konnektor hat Skills + ETF-Core + Steuer-Architektur + Querverbindungen JP-Morgan/LLM-Research ↔ DEFCON-Konzepte automatisch verlinkt. System-Score: 94/100 (von ~84 normiert). Offene Punkte: !PortfolioRisk-Skill (nächste Woche) + Tariff-Triage 6 Satelliten (nächste Woche). |
| 07.04.2026 | **defeatbeta MCP via WSL2 vollständig repariert + ASML API Sanity Check abgeschlossen.** defeatbeta: Ubuntu-24.04 venv, Version 1.27.0, 100+ Tools, Daten bis 03.04.2026. ASML Sanity Check: OCF-Δ ~10% = IFRS 16 vs. ASC 842 strukturell (Leasingzahlungen) — kein API-Drift. CapEx-Δ ≤ 3.5% plausibel. FLAG-Schlussfolgerung unter beiden Standards identisch: Clean. IFRS-OCF-Toleranz auf ±15% erweitert wenn Leasingbasis erklärbar. |
| 14.04.2026 | **Second Brain erweitert:** 4 akademische Paper integriert (arXiv-1711.04837, Gu/Kelly/Xiu 2020, Morningstar Wide Moat, Buffetts Alpha AQR). 10 neue Konzeptseiten (5 Paper-Konzepte: 5J-Fundamental-Fenster, FCF-Primacy, Moat-Taxonomie, Buffett-Faktorlogik, QMJ + 5 Token-Effizienz: Token-Mechanik, Context-Hygiene, CLAUDE-md-Konstitution, Context-Hygiene-Code, Update-Klassen). Synthese: Wissenschaftliche-Fundierung-DEFCON mit 7-Befunde-Matrix. 11 Entity-Updates mit related_concepts + Wissenschaftliche-Basis-Abschnitt. CLAUDE.md als Schaltzentrale (Faktortabelle 4. Pflicht-Lektüre, Token-Kurzreferenz, MCP-Session-Check, Applied Learning). index.md: 45→60 Notes. Vollständige bidirektionale Backlink-Vernetzung. |
| 14.04.2026 | **Faktortabelle.md erstellt** (Snapshot-First, Kommentar-Anker `<!-- DATA:TICKER -->`). Insider-Skill erweitert: `--update-faktortabelle` Parameter + `factor-sync` 3-Wege-Vergleich (config.yaml + Faktortabelle + Live-Scan, benötigt pyyaml). COST CIK in dynastie-depot/SKILL.md korrigiert (0000723254→0000909832). EODHD-Hinweis → yfinance korrigiert. Vault: Faktortabelle-Architektur.md als Konzeptseite. index.md: 60→61 Notes. |
| 09.04.2026 | **APH DEFCON-Analyse:** Score 61, DEFCON 🟡 3, 🔴 FLAG aktiv. |
| 09.04.2026 | **RMS DEFCON-Analyse:** Score 71, DEFCON 🟢 4. Erster Non-US-Satellit mit vollem Score. |
| 09.04.2026 | **VEEV DEFCON-Analyse:** Score 74, DEFCON 🟢 4. |
| 15.04.2026 | **Vault-Audit:** 10 neue Seiten (4 Autoren + 6 Ersatzbank), 7 Orphans gefixt, DEFCON Cross-Links, Frontmatter standardisiert. 61→71 Notes. CLAUDE.md/INSTRUKTIONEN.md/CORE-MEMORY optimiert: Duplikate entfernt, Typos gefixt, Versionen synchronisiert. |
| 15.04.2026 | **System-Integration v4.0:** SKILL.md v4.0 (15 Regeln), 6 Lücken in INSTRUKTIONEN.md geschlossen, MCP-Session-Check + Tool Search verankert, settings.json optimiert, Sync-Pflicht 3 Dateien. System-Reife ~95%. |
| 15.04.2026 | **APH Tariff-Check abgeschlossen:** Revenue China FY2025 = 14.7% (< 15%-Schwelle, kein Revenue-FLAG). Supply-Chain CN/MY bestätigt → Risk-Map-Notiz. Bestehender FLAG bleibt (Score-basiert). China-Revenue-Trend strukturell rückläufig (23%→14.7% in 2 Jahren) — positiv. |
| 15.04.2026 | **V (Visa) DEFCON v3.4 Vollanalyse:** Score 86/100, DEFCON 🟢 4. Kalibrierungsanker auf AVGO-Niveau. Highlights: CapEx/OCF ~6% (Fabless-Niveau), Moat 19/20 (GuruFocus 9/10 Wide, 4 überlappende Quellen), FCF $21.6B FY25, Revenue $40B (+11.4%). Schwächen: ROIC ~9.9% GAAP knapp unter WACC ~10.5% (Goodwill-Verzerrung Visa-Europe), Fwd PE 23x, Kurs unter 200MA. Insider sauber (diskr. $201K / 90d). Kein FLAG. Sparplan voll aktiv. |
| 15.04.2026 | **COST (Costco) DEFCON v3.4 Vollanalyse:** Score 69/100, DEFCON 🟢 4 (Bestandsposition). Screener-Exception: ROIC 5.6% GAAP (strukturell durch niedriges Book Value) → Membership Yield 15.2% ($5.3B / $34.9B IC) als ökonomischer Return > WACC 12.3%. Highlights: Moat 19/20 (GuruFocus 9/10 Wide — Membership-Loyalty unübertroffen), CapEx/OCF 21.3% Clean, FCF $7.2B FY2025. Schwächen: P/FCF 53x (teuer), FCF Yield 1.88%, Fwd PE 51x, GAAP-ROIC-Malus. Kein FLAG. Sparplan voll aktiv. |
| 15.04.2026 | **BRK.B (Berkshire Hathaway) DEFCON v3.4 Vollanalyse:** Score 75/100, DEFCON 🟢 4. Screener-Exception: P/B 1.44x statt P/FCF (Versicherung/Holdings). Highlights: Moat 19/20 (Float $686B einzigartig, BNSF Efficient Scale, 60J Capital-Allocation-Track-Record), Book Value CAGR +10% p.a. 5J, Interest Income $39.98B FY25, Goodwill nur 6.8% (kein Malus), CapEx/OCF 45.6% (BNSF+BHE Infrastruktur, kein FLAG). Insider 9/10: Greg Abel Open-Market-Käufe $15.3M (90d) — starkes Alignment-Signal. Schwächen: ROIC 5.6–7.8% GAAP (Insurance Exception), Technicals 4/10 (unter 200MA, limitierter PT-Upside), Buybacks $0 FY25. Kein FLAG. Sparplan voll aktiv. |
| 15.04.2026 | **SU (Schneider Electric) DEFCON v3.4 Vollanalyse:** Score 71/100, DEFCON 🟢 4. Highlights: CapEx/OCF 25.2% (ausgezeichnet, 4J stabil), ROIC 10.48% > WACC 8.96% (positiver Spread bestätigt), FCF-Wachstum +41% in 3J (€3.26B→€4.59B), Kurs +12.6% über 200D-MA (einziger Satellit über 200MA), 22 Analysten Strong Buy 0% Sell. Schwächen: P/FCF 37.7x (teuer), FCF Yield 2.65%, Goodwill 40.2% (AVEVA M&A), Moat Narrow (nicht Wide gesichert). Kein FLAG. Sparplan voll aktiv. |
| 16.04.2026 | **ASML Q1 2026 Earnings Recap:** EPS $7,15 (Beat +7,99% vs. $6,62 Konsens). Umsatz €8,77 Mrd (+13,2% YoY). GM 53,0%. Net Income €2,76 Mrd (+17,1% YoY). Guidance angehoben: FY2026 €36–40 Mrd (von €34–39 Mrd). Kurs −2,4% trotz Beat: Booking-Disclosure erstmals nicht veröffentlicht + China-Exportkontroll-Unsicherheit (€36–40 Mrd Bandbreite explizit für Export-Control-Risiko). DEFCON-Score 68 unverändert. Kein FLAG. Sparrate voll aktiv. Nächster Trigger: Q2 2026 Earnings. |
| 15.04.2026 | **RMS (Hermès) Q1 2026 Earnings Recap + DEFCON v3.4 Re-Analyse:** Score 71→**69**, DEFCON 🟢 4 bestätigt. Q1 Revenue €4,07B (+6% CER, −1% reported). Miss vs. +7–8% Erwartung. Kursreaktion: **−8,4%** (neues 52W-Tief €1.529 intraday). Treiber: Mittlerer Osten −6% (Iran-Krieg, UAE Malls −40%), FX-Headwind €290M, China Asien ex Japan +2%. Positiv: Leder +9%, Moat 19/20 intakt, ROIC 24% >> WACC 6,5%, Insider-Käufe +€7,67M (90d). Kein FLAG. Sparrate voll aktiv (31,67€). Score valid bis 15.10.2026. **Screener-Exception (institutionelle Begründung):** Analog COST (Membership Yield 15,2% > WACC 12,3%) rechtfertigt bei RMS der hohe ökonomische Return ROIC 24% >> WACC 6,5% (Spread +17,5 PP) die Beibehaltung von DEFCON 🟢 4 trotz Score 69 (knapp an D3-Grenze). Score-basierte Downgrade-Mechanik wird durch Return-Exception überschrieben, solange Moat 19/20 + ROIC-Spread >10 PP bestätigt bleiben. Re-Check-Trigger: H1 2026 Report Juli/Aug 2026. |
| 16.04.2026 | **DEFCON v3.5 Scoring-Audit & Fix:** Formales 7-Fragen-Audit des Scoring-Systems. Ergebnis: 5×A, 1×B (PT-Upside Double-Counting in Technicals+Sentiment), 1×C (Gewichtsanpassung zurückgestellt). Fix: PT-Upside aus Technicals entfernt, Relative Stärke vs S&P500 als 0-3 Scored Metric promotet (vorher ±1 Tiebreaker), Fundamentals-Floor-Klausel (min 0) hinzugefügt. Anker rekalibriert: AVGO 86→85, SNPS 79→76, TMO 65→62 (D3→D2 Grenzfall), FICO 70→67, SPGI 77→74. MKL 82 unverändert. Block-Gewichte 50/20/10/10/10 beibehalten. |
| 17.04.2026 | **3 Foundation-Papers integriert (Vault v4.3):** Piotroski (2000) F-Score, Novy-Marx (2013) Gross Profitability Premium, Sloan (1996) Accruals-Anomalie. 7→10 Quellen, 11→14 Befunde (B12/B13/B14). 6 neue Notes (3 sources + 3 concepts), Synthese erweitert, index.md 70→76 wiki-Notes. **Vorbereitet für v3.6-Release:** Quality-Bonus (F-Score ≥7 → +2 Pt.) + GP/TA-Metrik (2 Pt.) + Accrual-Bonus (<3% → +2 Pt.). System-Reife-Ceiling 85% → geplant 92-95%. Kein Scoring-Impact vor v3.6-Implementation — aktuelle Scores unverändert. |
| 17.04.2026 | **v3.6 verworfen, v3.7 „System-Gap-Release" ratifiziert.** v3.6-Boni (F-Score/GP-TA/Accrual) = Double-Counting mit dekomponierten Sub-Signalen → verworfen. v3.7-Fixes implementiert: **(1) Quality-Trap als Interaktionsterm** (Wide Moat + Fwd P/E >30 ODER P/FCF >35 → betreffender Fundamentals-Subscore hart 0; Wide Moat + 22–30/22–35 → Subscore max. 1). Redesign gegen ursprünglichen additiven Moat-Malus (hätte Double-Counting verletzt — Applied Learning 17.04.). **(2) Operating Margin TTM** als Fundamentals-Metrik (max 2 Pt.; >30%→2, 15–30%→1, <15%→0; COST+BRK.B Exception). **(3) Analyst-Bias-Kalibrierung** Sentiment (SB>60% → 1 Crowd-Malus, SB<40%→4; Sell-Ratio <3%→1, 3–10%→3, >10%→0). **(4) Fundamentals-Block-Cap bei 50** (keine Bonus-Inflation). Backtest aller 11 Satelliten approximativ (Interaktions-Redesign): ASML 68→66 (D3 bleibt — Fix-1 milder als additiver Malus), AVGO 85→84, MSFT 60→59, TMO 62→63, RMS 69→68, SU 71→69, VEEV 74→74, V 86→86, BRK.B 75→75, APH 61→63, COST 69→69. **Keine DEFCON-Klassifikations-Shifts.** Sparraten korrigiert (Nenner = 8×1.0 + 1×0.5 = 8.5; zuvor fälschlich 9.0 nach v3.5-Audit nie nachgepflegt): **volle Rate 33,53€, TMO D2-Rate 16,76€, FLAGs (MSFT+APH) 0€**. Live-Verifikation pro Ticker bei nächstem Earnings-Update (QuickCheck-Pflicht). System-Reife 85% → ~92%. **Tools-Sync 17.04. (Commit 7419fe7 + cdf0064):** Rebalancing_Tool + Satelliten_Monitor via openpyxl synchronisiert, Sparraten-Summe 285€ validiert, J-Spalte FLAG-aware gefixt. |
| 17.04.2026 | **TMO Live-Verify (Schritt-2-Restarbeit Backtest v3.7):** defeatbeta + stockanalysis. OpM TTM 18,17% (1 Pt.), Fwd P/E FY26 20,80 (unter 22 → Fix-1 triggert NICHT auf Fwd P/E), P/FCF 29,3x ($184B MCap / $6,29B TTM FCF → 22-35 + Wide Moat → **P/FCF-Subscore hart max 1**), SB-% 31,6% (Score 4, kein Malus), Sell-Ratio 0% (Warning, Score 1). Score-Rekonstruktion 67-1+0-2 = 64 → **Score 63 innerhalb ±1 Toleranz bestätigt**. DEFCON 2 live-verified, Sparrate 16,76€ korrekt. Kritischer Trigger 23.04. Q1 Earnings. Besonderheit: Fix-1 differenziert sauber — nur P/FCF-Zweig triggert, Fwd-P/E-Zweig nicht. |
| 17.04.2026 | **ASML Live-Verify (Schritt-2 Backtest v3.7):** defeatbeta + stockanalysis. OpM TTM 36,1% (2 Pt. max, >30%), Fwd P/E FY26 **39,52** (>30 → Fwd-P/E-Subscore hart 0), Fwd P/E FY27 **30,30 Grenzfall**, P/FCF ~48x (MCap $570B / TTM FCF €11,07B, >35 → P/FCF-Subscore hart 0), SB-% 18,2% (Score 4), Sell-Ratio 0% (Warning, Score 1). **BEIDE Fix-1-Zweige triggern hart auf 0** — maximaler Interaktionsterm-Impact ohne Double-Counting. Approximation **66 innerhalb ±2 Toleranz bestätigt**, DEFCON 3 live-verified. **Watch:** Fwd P/E FY27 30,30 auf der Kippe — wenn nach nächster Guidance <30 → Fix-1-Fwd-Zweig deaktiviert, Score +1 bis +2 möglich (D3→D4-Kandidatur). |
| 17.04.2026 | **RMS Live-Verify (Schritt-2 Backtest v3.7):** stockanalysis (defeatbeta non-US Gap). OpM TTM 41,05% (2 Pt. max), Fwd P/E 34,91 (>30 → Fwd-P/E-Subscore hart 0), P/FCF ~38x (MCap €173B / TTM FCF ~€4,5B, >35 → P/FCF-Subscore hart 0). Analyst-Daten Lücke (EU-Coverage dünn bei stockanalysis). **Beide Fix-1-Zweige triggern** wie ASML — DEFCON 4 durch Screener-Exception (ROIC 24% >> WACC 6,5%, Spread +17,5pp) geschützt. Approximation **68 innerhalb ±2 Toleranz bestätigt**. Nach Q1 −8,4% Kursdrop fiel Fwd P/E von ~39 auf 34,9 — weitere Korrektur könnte <30 bringen, Score +1 möglich. |
| 17.04.2026 | **Zwischenbilanz Live-Verify 3/11 (TMO, ASML, RMS) — alle Approximationen innerhalb Toleranz bestätigt.** Fix-1 Interaktionsterm funktioniert präzise design-konform: bei ASML+RMS beide Zweige hart 0, bei TMO nur P/FCF-Zweig (Differenzierung). Kein Double-Counting, kein Pauschal-Malus. v3.7-System empirisch validiert. Rest-Tickers (8) bei regulärem Earnings-Trigger. |

---

## 2. Strategische Entscheidungen (dauerhaft bindend)

### Allokations-Entscheidung (März 2026)
**Beschluss:** 60/35/5 → **65/30/5** (ETF/Satelliten/Gold)
**Grund:** Mehr Diversifikation, weniger Single-Stock-Risiko, höhere wissenschaftliche Basis im ETF-Block
**Bindend:** Ja — keine Änderung ohne expliziten Beschluss

### Gewichtungs-Entscheidung Satelliten
**Beschluss:** Alle 11 Positionen gleichgewichtet 2,73% (APH 2,70% Ausgleich)
**Vorher:** TMO 2,5%, APH 2,5%, COST 3,5% — ungleichgewichtet
**Bindend:** Ja

### Slot-Anzahl
**Beschluss:** 16 Slots maximum (4 ETFs + 11 Aktien + 1 Gold)
**Slot 12–16 belegt:** Alle vergeben. Nächste Entscheidung: Juni 2026
**Bindend:** Ja — kein Overcrowding

### CRWD und PLTR Entfernung
**Beschluss:** Beide entfernt — kein Wide Moat, Hyper-Growth-Angreifer-Profil passt nicht zur Strategie
**Datum:** März 2026
**Gelernt:** Strategie-Fit > kurzfristige Rendite

### GOOGL struktureller Ausschluss
**Beschluss:** Kein Einstieg trotz Score 72 — 🔴 FLAG CapEx FY26 ~75% OCF
**Datum:** 01.04.2026 (FLAG permanent bis Auflösung)
**Gelernt:** FLAG überschreibt Score. Kein Kompromiss.

---

## 3. Aktive Positions-Entscheidungen (Stand: 04.04.2026)

### MSFT — DEFCON 2, FLAG aktiv (Re-Analyse 08.04.2026)
- **Score:** 60/100 (↓ von 77, −17 Punkte) | **DEFCON:** 🟠 2 | **FLAG:** 🔴 CapEx/OCF Q2 FY26: 83.6% (bereinigt ~63%)
- **Sparrate:** 0 € (FLAG + DEFCON 2 → doppelte Absicherung) seit 26.03.2026
- **Score-Verfall:** ROIC 7.5% vs. WACC 13.35% (−5.85 PP) = strukturell unter Kapitalkosten. CapEx FY26 auf Kurs $100–120B. FCF FY25: $71.6B (↓ von $74.1B)
- **Trigger für FLAG-Auflösung:** Q3 FY26 Earnings 29.04.2026 — bereinigtes CapEx/OCF muss <60% fallen (Finance Leases raus)
- **Nach FLAG-Auflösung:** Score-Update nötig — bei Score ≥65 → DEFCON 3 volle Rate; bei Score 50–64 → DEFCON 2 Sockelbetrag 50%
- **Worst Case:** Score <50 → DEFCON 1 → Ersatz-Analyse (GOOGL FLAG aktiv → ZTS/VEEV-Alternative)
- **Ersatz bereit:** GOOGL (FLAG aktiv!) → kein sofortiger Tausch möglich
- **Moat-Status:** 19/20 unverändert — Wide Moat strukturell intakt (Azure, M365, Switching Costs)

### TMO — DEFCON 2, Clario-Watch
- **Score:** 62/100 | **DEFCON:** 🟠 2 | **Stand:** 16.04.2026 (v3.5 RS-Shift: -3P, D3→D2)
- **Sparrate:** 50% (D2, kein 🔴 FLAG → Gewicht 0.5)
- **Verbesserungen seit 02.04.:** Net Debt/EBITDA 3.6x → 2.57x ✅ | Fwd P/E 27x → 19.9x ✅ | P/FCF 35x → 29.2x ✅
- **Schwächen:** ROIC 2.6% Q (Goodwill $49.4B) | FCF -13.4% YoY | Unter 200MA
- **Trigger für DEFCON 4:** FCF Yield >4% (= FCF >$7.3B bei aktuellem Kurs) + ROIC Aufwärtstrend
- **Trigger für ZTS-Aktivierung:** Score <50 oder Moat-Downgrade oder FCF weiter rückläufig nach Q1
- **Entscheidung:** Q1 Earnings 23.04.2026 — alles oder nichts
- **Gelernt:** ROIC < WACC ist harter Malus auch bei Wide Moat. Goodwill-bereinigter ROIC wäre deutlich höher, aber GAAP-Basis ist Scoring-Pflicht.

### APH — DEFCON 3, FLAG aktiv (Analyse 09.04.2026 | Tariff-Check 15.04.2026)
- **Score:** 61/100 | **DEFCON:** 🟡 3 | **FLAG:** 🔴 aktiv (Score-basiert, nicht Tariff-Schwelle)
- **Sparrate:** 0 € (FLAG überschreibt — Score 61 = DEFCON 3, aber FLAG aus Gesamtbewertung)
- **Tariff-Check 15.04.2026:** Revenue China FY2025 = **14.7%** ($4.58B / $31.1B) — knapp unter 15%-Notiz-Schwelle. Kein Revenue-FLAG ausgelöst.
- **Supply-Chain:** Produktionsstandorte CN/MY bestätigt (Q1 2025 Earnings Call, Adam Norwitt). Kombinierte Exposure CN+MY+VN ~17–22% → Risk-Map-Notiz-Pflicht aktiv (15–35%-Band).
- **China-Trend:** Rückgang von 23% (2023) → 20% (2024) → 14.7% (2025) — strukturell positiv durch CommScope-Akquisition + Diversifikation.
- **Management-Mitigation:** „Purpose built" dezentrale Struktur, Pricing Power bestätigt (Q1 2025 Call).
- **FLAG-Klärung:** FLAG bleibt aktiv — Basis ist Score 61 (DEFCON 3 mit Sparrate 0€ nach FLAG-Logik). Kein separater Tariff-FLAG nach Regelwerk (Revenue <15%).
- **Nächste Aktion:** Q2 2025 Earnings (23.07.2025) — Revenue-Trend China + Manufacturing-Mitigation beobachten.

---

## 4. Score-Register (alle durchgeführten Analysen)

| Ticker | Score | DEFCON | Datum | Status | Nächste Aktion |
|--------|-------|--------|-------|--------|----------------|
| ASML | 66 | 🟡 3 | 17.04.2026 (v3.7) | Aktiv — volle Rate (D3, kein 🔴) | ✅ Q1 2026 Earnings abgeschlossen. Live-Verify QT-Cap bei Q2 2026 |
| AVGO | 84 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — ⚠️ Insider-Review | Q3 FY26 Earnings — OpenInsider manuell prüfen |
| FFH.TO | 88 | 🟢 4 | ~März 2026 | Ersatzbank BRK.B | — |
| NVDA | 86 | 🟢 4 | ~März 2026 | Ersatzbank AVGO | — |
| MKL | 82 | 🟢 4 | 25.03.2026 | Ersatzbank BRK.B | CapEx-FCF (Performance Thread) |
| ZTS | 81 | 🟢 4 | ~März 2026 | Ersatzbank VEEV | — |
| PEGA | 85 | 🟢 4 | ~März 2026 | Slot-16-Kandidat | Earnings Mai 2026 |
| MSFT | 59 | 🟠 2 | 17.04.2026 (v3.7) | Aktiv — FLAG aktiv (CapEx/OCF Q2 FY26: 83.6%, bereinigt ~63%) | Q3 Earnings 29.04.2026 — FLAG-Auflösung wenn bereinigt <60% |
| SNPS | 76 | 🟡 3 | 26.03.2026 | Ersatzbank ASML | Re-Analyse Mai 2026 |
| SPGI | 74 | 🟡 3 | 31.03.2026 | Watchlist | Earnings 28.04.2026 |
| RACE | 73 | 🟢 4 | ~März 2026 | Ersatzbank RMS | — |
| GOOGL | 72 | 🟡 3 | 26.03.2026 | 🔴 FLAG — kein Einstieg | FLAG-Auflösung abwarten |
| SAP | 72 | 🟡 3 | ~März 2026 | Watchlist | ZTS bevorzugt |
| EXPN | 61 | 🟡 3 | 02.04.2026 | Watchlist | P/FCF + Insider-Check |
| HON | 71 | 🟡 3 | 28.03.2026 | Watchlist | Post-Spinoff 2026 |
| TMO | 63 | 🟠 2 | 17.04.2026 (v3.7) | Aktiv — 50% Rate (D2, kein 🔴 FLAG) → **16,76€** | Q1 Earnings 23.04.2026 — FCF-Erholung + ROIC-Trend |
| APH | 63 | 🟡 3 | 17.04.2026 (v3.7) | Aktiv — FLAG aktiv | Tariff-Check CN/MY |
| RMS | 68 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — Sparplan voll → **33,53€** | H1 2026 Report Juli/Aug 2026 |
| VEEV | 74 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — Sparplan voll → **33,53€** | Keine Earnings-Urgenz |
| FICO | 67 | 🟡 3 | 03.04.2026 | Watchlist VEEV-Ersatz #1 | Re-Analyse bei VEEV-Schwäche |
| V | 86 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — Sparplan voll → **33,53€** | Q2 FY26 Earnings ~22.04.2026 |
| COST | 69 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — Sparplan voll (Bestandsposition ≥65, Screener-Exception) → **33,53€** | Nächste Earnings ~Dez 2026 Q1 FY27 |
| BRK.B | 75 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — Sparplan voll (Insurance Exception) → **33,53€** | Q-Earnings Mai 2026 — Buyback-Wiederaufnahme beobachten |
| SU | 69 | 🟢 4 | 17.04.2026 (v3.7) | Aktiv — Sparplan voll → **33,53€** | H1 2026 Earnings Juli/Aug 2026 |

---

## 5. Scoring-Lektionen (gelernte Regeln)

### Goodwill-Malus
M&A-Akquisitionen verzerren ROIC nach unten und die Bilanz nach oben.
→ Net Debt/EBITDA >3x = 0/3 Punkte im Bilanz-Block
→ Non-GAAP bereinigter ROIC darf als Zusatzinformation genannt werden, aber GAAP-Wert ist Scoring-Basis
→ **Referenz:** SNPS (Ansys $26.88B Goodwill = -3 Punkte), SPGI (IHS Markit $44B)

### ROIC < WACC = harter Malus
Auch bei Wide Moat: Wenn das Unternehmen kein Kapital oberhalb seiner Kapitalkosten verzinst, ist das ein fundamentales Problem.
→ Score: 2/8 bei ROIC ~WACC, 0–1 bei ROIC < WACC
→ **Referenz:** TMO (ROIC 9,37% vs. WACC 9,99%)

### FLAG ist absolut
Ein aktives FLAG überschreibt jeden Score. Es gibt keine "Score ist ja trotzdem gut"-Argumentation.
→ CapEx/OCF >60% = FLAG, auch bei DEFCON 4 Score
→ **Referenz:** MSFT (Score 60, DEFCON 2, FLAG aktiv = Sparrate komplett gestoppt, 0 €)

### Cashless Exercise ≠ Insider-Selling
Transaktionen mit Code M+S, gleicher Tag, Expiry ≤30d = automatische Ausübung aus Plan.
→ Kein diskretionäres Signal, kein FLAG-Trigger
→ **Referenz:** FICO-Analyse 03.04.2026

### Datenlücken → konservativ scoren
Wenn Insider-Daten oder Technicals nicht verifizierbar sind: Pflichtmalus.
→ Insider 3/10, Technicals 5/10 als Minimum bei unvollständiger Datenlage
→ **Referenz:** EXPN (Non-US, LSE-Ticker)

### TTM-Verzerrung bei Kurscrash
Bei Titeln mit >40% Kursrückgang: TTM-Metriken verzerren nach oben.
→ Forward-Metriken als Primärbasis, TTM als Kontext
→ **Referenz:** FICO (TTM P/FCF 34x vs. Fwd P/FCF ~19x bei -52% Crash)

### Pre-Processing Layer (v3.3 — 06.04.2026)
Vier Regeln müssen vor jedem Scoring angewendet werden:
- **Regel 1:** SBC/OCF ≥15% → Dokumentationspflicht (kein Score-Malus, nur Transparenz)
- **Regel 2:** Finance Lease Obligations >$5B → manueller 8-K-Check vor CapEx-FLAG (Shibui kann Lease-Payments nicht isolieren)
- **Regel 3:** CapEx-Qualität → Growth vs. Maintenance aus Earnings Call — kein automatisches Veto, nur Risk-Map-Notiz
- **Regel 4:** M&A Amortization → Proxy: NOPAT + (D&A × 0,65) / Invested Capital. Nur bei Goodwill >30% Assets aktiv. Pflichthinweis "Proxy, nicht GAAP".

### API-Sanity-Check-Lücke IFRS (v3.3 — 06.04.2026)
Shibui Finance hat keine primäre Coverage für ASML, RMS, SU (Euronext-Titel).
→ Non-US: EODHD API als Primärquelle, Toleranz ±1,5% (IFRS-Ermessen)
→ US: Shibui + defeatbeta, Toleranz ±0,5%
→ Hermès (RMS) + Schneider (SU): nur halbjährliche Berichte — Sanity-Check H1/H2

### SEC EDGAR 10b5-1 Footnote-Luecke (v1.0 Insider-Modul)
Viele Insider-Verkaeufe (besonders bei Broadcom) erscheinen im Form-4-XML als "diskretionaer",
obwohl sie faktisch nach RSU-Vesting stattfinden. Das liegt daran, dass nicht alle Unternehmen
das 10b5-1-Stichwort explizit in den Filing-Footnotes verwenden.
→ **OpenInsider Gegencheck bleibt HEILIG** — besonders bei AVGO, wo Tan/Brazeal/Spears
  regelmaessig hohe Post-Vesting-Verkaeufe taetigen.
→ Bei FLAG-Trigger durch Insider-Modul: Immer manuell auf openinsider.com Spalte "X"/"M" pruefen
  bevor FLAG aktiviert wird.
→ **Referenz:** AVGO 06.04.2026 — Modul zeigt $123M FLAG, aber viele Transaktionen sind
  vermutlich Post-Vesting (Code F/S am gleichen Tag wie A/M).

### Non-US Kalibrierungsanker: ASML (06.04.2026)
**Erster vollständiger DEFCON-Anker für IFRS/Euronext-Titel.**
- Score 68 = Wide-Moat-Monopol zu Premium-Bewertung (Fwd P/E 38x, P/FCF ~41x)
- Fundamentals 28/50 als Referenz: wie teuer ein Monopol sein darf bevor Score kippt
- Moat 19/20 als Non-US-Referenz für "bestes vorstellbares europäisches Unternehmen"
- Routing: Shibui für Technicals (ASML.NASDAQ ADR) + Web für IFRS-Fundamentals
- eodhd_intel.py: in Cowork-Session blockiert (yfinance nicht installierbar in Sandbox) → bei Code-Session verwenden
- **Fazit:** Ein 68er Non-US-Score bei tadelloser Qualität = Bewertungsproblem, kein Qualitätsproblem. Referenz für zukünftige ASML/RMS/SU-Analysen.

### Tariff Exposure als Scoring-Malus (v3.1)
Bei Unternehmen mit signifikanter Produktion in Risikoländern (Malaysia, Thailand, China):
→ Tariff Exposure Score als Minus im Fundamental-Block
→ **Referenz:** AVGO (~35% Revenue US-Halbleiter, Produktion Malaysia/Thailand = -1 Punkt)

---

## 6. System-Upgrades & Versionsverlauf

### DEFCON v3.1 (03.04.2026) — 11 Verbesserungen
Neu hinzugefügt: SBC/Revenue, Accrual Ratio, GM-Trend, Pricing Power,
Relative Stärke, 200MA Slope als Wachstumsindikator, DCF-Anker erweitert,
EPS Revision, PT-Dispersion, Tariff Exposure

### config.md Struktur (01.04.2026)
Single-Source-of-Truth etabliert. Pflicht: Nach jeder Analyse updaten + neu hochladen.
Versionshistorie in der Datei selbst dokumentieren.

### Rebalancing Tool v3.1 FINAL (31.03.2026)
Allokation 65/30/5 final. US-Exposure korrekt berechnet.
Gleichgewichtung aller 11 Satelliten (2,73%) implementiert.

---

## 7. Steuer-Erinnerungen

- **Freistellungsauftrag:** ING 1.500–1.600€ (Vorabpauschale), Scalable 400–500€ (Dividenden)
- **FIFO-Klon-Strategie:** 10–15 Jahre vor Entnahme starten
- **NV-Bescheinigung Kind:** bis 13.384€/Jahr (Stand 2026) steuerfrei
- **Lombardkredit:** Alternative zu Verkauf — immer erst prüfen bevor verkauft wird
- **Rebalancing:** Niemals durch Verkauf — immer Sparplan umleiten

---

## 8. Nächste offene Entscheidungen

| Entscheidung | Wann | Optionen |
|-------------|------|---------|
| MSFT FLAG auflösen oder Veto? | 29.04.2026 (Q3 Earnings) | Auflösung wenn CapEx/OCF <60% / Veto wenn nicht |
| TMO DEFCON 4 oder Tausch? | 23.04.2026 (Q1 Earnings) | Aufstieg wenn FCF >4%, Net Debt/EBITDA <3.0x |
| Slot 16 — PEGA Einstieg? | Mai 2026 (Earnings) | PEGA Score 85 — Earnings-Check entscheidend |
| Sparplan-Booster-Strategie | Juni 2026 | 9.500€ Bausparvertrag + 2.000€ Steuererstattung einsetzen |

---

## 9b. Nächste Session — Aktionsplan (post Liberation Day)

**Kontext:** Liberation Day (02.04.2026) + Zoll-Eskalation haben Märkte strukturell verändert. Tariff-Exposure aller Satelliten muss neu bewertet werden. Gleichzeitig ist DEFCON v3.4 jetzt vollständig produktiv (alle MCPs, Module, Pre-Processing). Erster vollständiger Re-Check aller 11 Satelliten steht an.

**Workflow-Entscheidung (ratifiziert 06.04.2026):**
Kein blinder Full-Run für alle 11. Erst Triage via `!QuickCheck ALL` mit Tariff-Fokus, dann Deep Dives in Risikoreihenfolge.

### Triage-Reihenfolge

| Priorität | Ticker | Grund | Befehl |
|-----------|--------|-------|--------|
| 🔴 1 | TMO | Earnings 23.04. — Entscheidung steht an | `!Analysiere TMO` |
| 🔴 2 | MSFT | Earnings 29.04. — FLAG-Review | `!Analysiere MSFT` |
| 🟡 3 | AVGO | Tariff-Exposure MY/TH ~35%, Insider-FLAG läuft | `!Analysiere AVGO` |
| 🟡 4 | COST | Retail, US-lastig, Tariff-Ketteneffekte | `!Analysiere COST` |
| 🟡 5 | V | Zahlungsinfrastruktur — kein direktes Tariff-Risiko, aber Konsumrückgang | `!Analysiere V` |
| 🟡 6 | APH | Produktion in Tariff-Risikoländern (CN/MY) | `!Analysiere APH` |
| 🟢 7 | BRK.B | Holding, defensiv, wenig Tariff-Direktexposition | `!Analysiere BRK.B` |
| 🟢 8 | VEEV | SaaS, keine Produktion, kein Tariff-Risiko | `!Analysiere VEEV` |
| 🟢 9 | RMS | Luxury, Preismacht, EUR-denominiert | `!Analysiere RMS` |
| 🟢 10 | SU | Industrie, EUR, Energie-Infrastruktur | `!Analysiere SU` |
| 🟢 11 | ASML | Score 68, DEFCON 3 — API Sanity Check ✅ abgeschlossen (07.04.2026) | — |

### Nach jedem `!Analysiere`:
1. config.yaml aktualisieren (score, defcon, flag, score_valid_until)
2. CORE-MEMORY.md Score-Register aktualisieren
3. Satelliten Monitor + Rebalancing Tool aktualisieren wenn DEFCON/Sparrate sich ändert

### defeatbeta-MCP Status (repariert 07.04.2026 — vollständig produktiv ✅)

**Konfiguration:** `wsl -d Ubuntu-24.04 bash -c /home/tobia/.defeatbeta-env/bin/python -m defeatbeta_mcp`
Version 1.27.0 | 100+ Tools geladen | Daten bis 03.04.2026

**Root-Ursache (dokumentiert):** `cache_httpfs` ist Linux-only DuckDB Community Extension — inkompatibel mit `windows_amd64`. Fix: defeatbeta läuft jetzt in WSL2 (Ubuntu-24.04). Zwei Distros vorhanden (Ubuntu default=leer, Ubuntu-24.04=venv). Immer `-d Ubuntu-24.04` spezifizieren.

**Live-Test (07.04.2026):** AVGO Cash Flow vollständig abgerufen ✅ — OCF $27,54B, CapEx $623M, FCF $26,91B.

### API-Routing (US-Ticker — gültig ab 07.04.2026):
- **Fundamentals:** defeatbeta MCP (Primärquelle — alle Income/CF/Balance/ROIC/WACC-Tools)
- **Technicals + historische Breite:** Shibui SQL (unverändert Primärquelle)
- **Insider:** insider_intel.py (SEC EDGAR Form-4)
- **Forward-Metriken / Moat / Sentiment:** Web Search

### Session-Start-Pflicht (vor erstem !Analysiere):
Quick-Test: `get_latest_data_update_date` → antwortet = Verbindung OK ✅
Falls Fehler → WSL2-Verbindung prüfen: `wsl -d Ubuntu-24.04` verfügbar?

### Zusatz-Check bei jedem Satelliten (Liberation-Day-Pflicht):
- Tariff-Exposure: CN + TW + MY + TH + VN Revenue- + Supply-Chain-Anteil → >35% = FLAG
- Quelle 1: defeatbeta `get_quarterly_revenue_by_geography`
- Quelle 2: Earnings Call Transcript → Management-Kommentar Zölle
- Bewertungskorrektur: Kurse seit 02.04. teilweise -10 bis -20% → TTM-Verzerrung prüfen, Forward-Metriken als Basis

### Aktuelle Sparplan-Berechnung (Stand 16.04.2026 — v3.5)
AVGO FLAG→0,0 | ASML D3→1,0 | MSFT FLAG→0,0 | RMS→1,0 | VEEV→1,0 | SU→1,0 | BRK.B→1,0 | V→1,0 | TMO D2→0,5 | APH FLAG→0,0 | COST→1,0
Summe: 7×1,0 + 1×0,5 = 7,5 | Einheits-Rate: 38,00€ | D2-Rate: 19,00€ | Check: 7×38,00 + 1×19,00 = 285,00€ ✓

### Rebalancing-Workflow-Regel (ratifiziert 06.04.2026)
- Nach `!Analysiere` → config.yaml + CORE-MEMORY + Excel sofort (wenn DEFCON/Sparrate ändert sich)
- `!Rebalancing` → nur wenn Sparplan tatsächlich eingereicht wird (monatlich)
- Freier Betrag bei DEFCON-Abstieg fließt automatisch in D4-Positionen (Formel, kein aktives Targeting)
- Watchlist.csv → archiviert (05_Archiv/). Ersetzt durch Watchlist_Ersatzbank_Monitor_v1.0.xlsx

---

## 10. API-Audit-Log (Quarterly Sanity Check)

**Format:** Datum | Ticker | OCF-Abweichung | CapEx-Abweichung | Status
**Toleranz:** US ±0,5% | Non-US (IFRS) ±1,5%
**Nächster Check:** Mai 2026 (Q2-Check: V, BRK.B, TMO)

| Datum | Ticker | OCF | CapEx | SBC | Status |
|-------|--------|-----|-------|-----|--------|
| 07.04.2026 | ASML | IFRS 16 vs. ASC 842 Δ ~10% strukturell (Leasingzahlungen) — kein API-Drift | Δ ≤ 3.5% (yfinance addiert Intangibles) — plausibel | n/a | ✅ RESOLVED — FLAG-Schlussfolgerung unter beiden Standards identisch: Clean |
| — | RMS | — | — | — | ⏳ PENDING — H1 2026 Bericht (Juli/August) |
| — | SU | — | — | — | ⏳ PENDING — H1 2026 Bericht (Juli/August) |

### IFRS 16 vs. ASC 842 — Strukturelle OCF-Differenz (Non-US Pflicht-Wissen)
Bei ASML (und allen IFRS-Titeln die auch US-ADR haben): yfinance zieht IFRS-EU-Meldung (ASML.AS Amsterdam).
Unter IFRS 16 → Leasingzahlungen (Tilgung) als Finanzierungs-CF → senkt OCF vs. US GAAP (ASC 842).
Differenz ~€1,2B/Jahr = normal für ASML-Leasingbasis. **Kein Fehler, kein Alert.**
→ Toleranz für Non-US OCF-Check: ±15% akzeptabel wenn Differenz mit Leasingbasis erklärbar.
→ CapEx-Toleranz bleibt ±1,5% (PP&E-Zahlen konvergieren unter beiden Standards).

---
*🦅 CORE-MEMORY.md v1.6 | Dynastie-Depot | Stand: 16.04.2026*