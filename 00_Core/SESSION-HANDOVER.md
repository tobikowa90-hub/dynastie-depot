# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-29 nachmittag. Heute drei Commits: APH Tag-0-Recap + Earnings-Calendar-Drift-Detection (`d314be4`), PIPELINE #24 Earnings-Calendar-Auto-Pull-Tool (`7684afd`), PIPELINE #17 REVISED auf 5-Anker-Mittelweg (`fe8eec9`, Codex-Round-3 84%, deferred bis MSFT-Drift-Audit). **Nächster primärer Resume-Trigger: MSFT Q3 FY26 Earnings 29.04. ~22:30 MESZ Tag-0-Routine (heute Abend, neue Session)**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `fe8eec9` (PIPELINE #17 REVISED 5-Anker-Mittelweg). Working tree clean (alte Shell-Escape-Anomalie-Files vom 28.04. nicht mehr aktuell). Untracked: keine relevanten.

**V-Stand operativ:** unverändert 64/🟠D2/19,00€. Tag-+1-Transcript-Notiz heute morgen in CORE-MEMORY §12.10 + PIPELINE #21 Pre-Q3-Hint persistiert (kein Score-Event). Q3 FY26 ~Ende Juli mit ROIC-Methodology-Verify.

**APH-Stand operativ:** unverändert 63/🟠D2/0€/FLAG-aktiv. Q1 FY26 Earnings heute 29.04. publiziert — Tag-0-Recap done, Pre-Call-Snapshot in CORE-MEMORY §12.APH. **Vollanalyse Tag +1 30.04. morgens** (§19.1) parallel zu MSFT.

**Earnings-Calendar-Drift detektiert (29.04.):** APH Q1-Trigger stand auf „23.07. Q2", Q1 nie eingetragen. Strukturelles Defizit dokumentiert in PIPELINE #24 (Earnings-Calendar-Auto-Pull-Tool, yfinance-Probe 11/11 PASS, Trigger post-MSFT-Window).

**PIPELINE #17 REVISED:** 5-Anker-Mittelweg-Plan (AVGO/ASML/MSFT/TMO/COST-oder-MKL) bei 84% Codex-Confidence < 95%-User-Threshold → DEFERRED. Trigger: „MSFT Tag-+1 fertig **+ driftfrei bestätigt**". Bei MSFT-Drift weiter deferred bis BRK.B Mai oder VEEV 27.05.

**STATE.md Critical-Alerts (3):** **29.04. MSFT Q3 FY26 FLAG-Review** | 29.04. APH Q1 done Tag-0-Recap | **30.04. APH Q1 Vollanalyse Tag +1**.

---

### 🎯 Nächster Schritt — MSFT Q3 FY26 (Tag 0 / Tag +1 Split nach §19.1 Wait-Discipline) **[NEUE SESSION PRIORITÄT 1]**

**Resume-Trigger Tag 0 (29.04. spätabends):** „MSFT Press-Release-Recap + FLAG-Quick-Check"
**Resume-Trigger Tag +1 (30.04. morgens):** „!Analysiere MSFT" oder „MSFT Q3 FY26 Vollanalyse starten"

**Kontext:** Earnings Release 29.04.2026 ~22:30 MESZ AMC. FLAG aktiv seit Q1 (CapEx/OCF Q2 FY26: 83,6% nominal; bereinigt um Finance Leases ~63%). FLAG-Auflösungs-Pfad: bereinigtes CapEx/OCF <60% = Auflösung; ≥60% = Veto-Verschärfung.

**§19.1 Earnings-Call-Wait-Discipline (NEU 28.04. spätabends, post V Q2 Reinfall):** Klasse-B-Vollanalyse läuft strikt **Tag +1 morgens nach Earnings Call**, nicht Tag 0. V Q2 28.04. mittags-Reinfall (~100-130k Token Revert) als Präzedenz; Tag-+1-Slot spart ~50-70%.

#### Tag 0 (29.04. spätabends, ~15-30 Min) — KEIN Score-Move

1. **`_extern/earnings-recap`-Skill aufrufen** (yfinance-basiert) für strukturierten Press-Release-Recap: Beat/Miss-Headlines (EPS estimate vs actual, surprise %), 4-Quartals-Trend-Tabelle, Stock-Reaction
2. **Manueller FLAG-Quick-Check** anhand Press-Release-PDF: CapEx/OCF (bereinigt um Finance Leases ASC 842!), FCF-Trend, Insider-Disclosures, Tariff. **Bei FLAG-Resolution** (CapEx/OCF bereinigt <60%) → `python 03_Tools/backtest-ready/archive_flag.py resolve --flag-id <ID> ...` sofort. **Bei FLAG-Verschärfung** (CapEx/OCF bereinigt ≥60% mit struktureller Eskalation) → bestehender FLAG bleibt aktiv, ggf. flag_events.jsonl-Update
3. **Pre-Call-Snapshot-Notiz** in `00_Core/CORE-MEMORY.md §12.5 MSFT`: 1-2 Sätze (Beat/Miss-Magnitude, CapEx-Status, Guidance grob, FLAG-Outcome)
4. **STOP** — keine Vollanalyse, kein Score-Move, kein D-Stufen-Wechsel, kein 8-File-Sync

**Tag-0-Sync-Set (FLAG-Resolution-Fall):** flag_events.jsonl (via archive_flag.py) + log.md + PORTFOLIO.md (FLAG-Spalte CLEAN + ggf. Sparrate-Note) + Faktortabelle.md (FLAG-Spalte) + config.yaml (MSFT-FLAG-Sub-Block). Score 59 unverändert.

**Tag-0-Sync-Set (kein FLAG-Wechsel):** log.md (Pre-Call-Snapshot) + CORE-MEMORY §12.5 (Headline-Notiz). Sonst nichts.

#### Tag +1 (30.04. morgens, ~30-45 Min) — Vollanalyse

1. **Pre-Brief lesen** (falls vor Ergebnis: Pre-Earnings-Snapshot). Earnings-Release-PDF + Q3-Press-Release als Source ziehen.
2. **Earnings Call Transcript-Read PFLICHT** via `mcp__defeatbeta-api__get_stock_earning_call_transcript` (US): Pricing-Power-Suche („pricing", „price increase", „raised prices"), Forward-Guidance-Detail, CapEx-Outlook, Q&A-Tone. Pricing-Power-Confirmation → Moat +1 Bonus möglich.
3. **Schritt 6c Pre-Flight (v3.7.4) MANUELL durchgehen** — alle 5 Blöcke prüfen: Sub-Score!=0 mit Roh-Wert oder `_carryover`-Marker. Carryover-Blöcke: kein Up-Score ohne neue Rohdaten (Lesson V-MEDIUM-2 + PIPELINE #23).
4. **SKILL-Wortlaut-Disziplin (Lesson V-HIGH-1):** Bei Methodology-Switches SKILL-Klausel literal prüfen. WACC-Eintrag im Record gesetzt → kein Switch auf alternative Skala. Carryover + Methodology-Watch + Reviewer-OK statt Switch.
5. **Kurs-Frische (Lesson V-HIGH-2):** `kurs.referenz="close_of_score_datum"` mit echtem 30.04.-Close (yfinance-Fallback wenn defeatbeta-Cutoff <30.04.).
6. **Schritt 7 via `backtest-ready-forward-verify`-Skill** — Draft als bare ScoreRecord, `analyse_typ: "vollanalyse"`, kein skill_meta.
7. **§18-Sync v2.3 (10 Files Pflicht + 1 conditional):** PORTFOLIO + Faktortabelle + CORE-MEMORY §12.5 + PIPELINE (FLAG-Status-Update) + STATE (Critical-Alert "29.04. MSFT" entfernen) + config.yaml + log.md + score_history.jsonl + **`03_Tools/Rebalancing_Tool_v3.4.xlsx`** (V-Style: Spalte N+O des MSFT-Tickers via openpyxl) + **`03_Tools/Satelliten_Monitor_v2.0.xlsx`** (V-Style: R3-Header + Ticker-Zeile + R24/R25-Footer). Bei FLAG-Resolution am Tag 0: `flag_events.jsonl` schon committed, hier nur referenzieren.
8. **Sparraten-Kaskade je nach Tag-0+Tag+1-Outcome:**
   - **FLAG aufgelöst Tag 0 + Score >65 Tag +1** → MSFT volle D3-Rate (Gewicht 1,0). Nenner 7,5 → 8,5; volle Rate 38,00€ → 33,53€ (alle 7 anderen D3/D4 -4,47€); MSFT-Rate 33,53€; V D2 19,00€ → 16,76€.
   - **FLAG aufgelöst Tag 0 + Score 50-64 Tag +1** → MSFT D2-Halbrate. Nenner 7,5 → 8,0; volle Rate 38,00€ → 35,63€; MSFT 17,81€; V 19,00€ → 17,81€.
   - **FLAG bleibt Tag 0** (CapEx/OCF bereinigt ≥60%) → MSFT-Sparrate weiter 0€, Nenner 7,5 unverändert. Ggf. DEFCON-1-Eskalation wenn Score <50.
9. **Codex-Single-Pass-Review VOR Sync-Commit** (NEU §19.1 Lesson V) — Sparring nur bei HIGH-Count ≥2 oder strukturellen Coverage-Gaps. Codex-Review BEVOR der 8-File-Sync-Commit landet, NICHT danach (sonst Revert-Aufwand wie bei V Q2).

**Memory-Hooks für MSFT-Lauf:**
- `feedback_earnings_call_wait_discipline.md` (NEU) — Tag 0 / Tag +1 Split
- `feedback_skill_methodology_drift_v_q2.md` (NEU) — SKILL-Wortlaut-Disziplin
- `feedback_xlsx_tools_in_sync_set.md` (NEU) — xlsx-Tools-Pflicht-Sync §18 v2.3
- `feedback_review_via_codex_not_advisor.md` — Codex statt Advisor
- `feedback_codex_sparring_heuristic.md` — Single-Pass Default

---

### 🟡 Parallel zu MSFT Tag +1: APH Q1 FY26 Vollanalyse (30.04. morgens)

**Resume-Trigger:** „!Analysiere APH" als Tag-+1-Vollanalyse (Q1 FY26 publiziert 29.04.).

**Kontext:** APH Q1 PR 29.04. Beat-and-Raise (Sales $7,62B +33% organic, Adj. EPS $1,06 +68%, Adj. OpMargin 27,3%, Book-to-Bill 1,24x, FCF $831M +43%, Q2-Guide +43-45% Sales). Schatten: China Tax $290M discrete + CommScope-Leverage-Sprung (+$3,2B Net Debt, Goodwill +66%, Cash 11,1→4,1B). Pre-Call-Snapshot in CORE-MEMORY §12.APH. Score 63/D2/FLAG-aktiv (Score-basiert) heute unverändert. Vollanalyse Tag +1 entscheidet ob FLAG via Score-Lift gelöst wird.

**Workflow analog MSFT:** Transcript-Read PFLICHT via defeatbeta-MCP, Schritt 6c Pre-Flight, SKILL-Wortlaut-Disziplin, Kurs-Frische, Schritt 7, §18-Sync v2.3 (10 Files), Codex-Single-Pass-Review VOR Sync-Commit. Methodology-Watch: China-Tax strukturell (Adj. ETR 27%) vs. Operating-Beat-Cascade-Argumentation; CommScope-Leverage-Sprung in Bilanz-Sub-Score; Pricing-Power-Statement im Transcript suchen; Carryover-Disziplin streng (V-Q2-Lehre).

**Reihenfolge bei zwei Vollanalysen am 30.04.:** APH zuerst (kleineres Risiko, klarer Beat-Cascade-Pfad, FLAG-Score-Move-Test), dann MSFT (höheres Risiko durch Provenance-Gate-Second-Run-Erstanwendung + CapEx-Finance-Lease-Bereinigung). Optional: getrennte Sessions zwischen beiden zur Token-Hygiene.

---

### 🟡 Folge-Resume nach BEIDEN Live-Runs (post-30.04. morgens)

**Resume-Trigger:** „Beispiele.md 5-Anker-Refactor (PIPELINE #17 REVISED) starten — Codex-Round-4-Sparring auf 95%+"

**Vorbedingung:** APH + MSFT Vollanalysen 30.04. morgens DONE **+ Drift-Audit driftfrei bestätigt** (kein Codex-HIGH/MEDIUM-Befund analog V-Q2). Falls Drift-Befund bei MSFT: Item #17 weiter deferred bis BRK.B Mai oder VEEV 27.05.

**Plan-Stand 29.04. (PIPELINE #17 REVISED, Codex-Round-3 84%):** 5-Anker-Mittelweg mit fixen Zwecken — AVGO (Standard-Forward + FLAG-Override mit harter Sektion-Trennung 17.04. | 27.04.), ASML (IFRS/Non-US + Bewertungs-Edge mit harter Trennung Operational | Valuation), MSFT (Provenance-Gate + CapEx-FLAG, post-Drift-Audit), TMO (Goodwill-bereinigte ROIC-Ausnahme), COST oder MKL (Premium-Multiple/Screener-Exception). V explizit OUT der Anker-Sammlung; Float-Modell BRK.B bewusst SKILL.md-only-Restspalt.

**Pflicht-vor-Execution:** (a) Coverage-Matrix vorab schreiben mit „SKILL.md-only"-Markierung; (b) MSFT-Anker-Freigabe an Drift-Audit gebunden; (c) AVGO + ASML Doppelrolle mit harten Sektion-Labels; (d) V außerhalb Beispiele.md halten; (e) Anker-Zweck-Definition fest verdrahten; (f) Codex-Round-4 auf 5-Anker mit Matrix → Ziel ≥95%. **User-Direktive:** kein Rework, klares Fundament — bei <95% weiter deferred.

---

### 🟡 Earnings-Calendar-Auto-Pull-Tool (PIPELINE #24)

**Resume-Trigger:** „Earnings-Calendar-Tool bauen — 03_Tools/earnings_calendar.py" post-MSFT-Window-Schluss.

**Plan:** yfinance-basiert (`Ticker(t).earnings_dates` future-Filter primär, `calendar` Fallback), Watchlist-Lese aus config.yaml, Diff-Report gegen PORTFOLIO/STATE/PIPELINE. Probe 11/11 PASS am 29.04. (alle Satelliten inkl. Non-US ASML.AS/RMS.PA/SU.PA). 3-Stufen-Plan: Stufe 1 manuell, Stufe 2 system_audit.py-Integration, Stufe 3 SessionStart-Hook. Aufwand Stufe 1 ~45-60 Min.
- **D. Live-Disziplin:** SKILL.md Schritt 6c + Schritt 7 SKILL-Wortlaut-Klausel (Lesson V-HIGH-1 als neuer Demo-Block)

**Cross-File-Updates im selben Refactor-Commit:**
- `01_Skills/dynastie-depot/SKILL.md` — AVGO-Score-Erwähnung „85" → „84" + §11→§12/§13 in Zeile :90
- `00_Core/Faktortabelle.md` — §11→§12/§13 in Zeile :74
- `00_Core/PORTFOLIO.md` — §11→§12/§13 in Zeile :30
- `00_Core/STATE.md` — Sync-Kurzregel um config.yaml ergänzen

**Item-Set:**
- **#17** Beispiele.md-Refactor (~45-60 Min Refactor + 15-30 Min Cross-File-Patches)
- **#18** AVGO 27.04. ScoreRecord-Backfill (`analyse_typ: rescoring`, Score 84 unverändert, FLAG-Referenz, ~15 Min) — optional in #17-Session mit-erledigen
- **#19** Schema `anker_relevanz` deferred

**Sync-Set §18.2:** Beispiele.md + SKILL.md + Faktortabelle.md + PORTFOLIO.md + STATE.md + score_history.jsonl (nur bei #18-Mit-Erledigung) + log.md.

**MKL-Pipeline-Test-Status:** UNTERBROCHEN am 28.04. nachmittags (User-Wunsch). Falls weiter gewünscht, in V/MSFT-Refactor-Folgesession nachholen oder als eigener Konsolidierungstag.

---

### 📅 Critical Operational

- **28.04. DONE:** V Q2 FY26 Forward-Vollanalyse (`92c9de1`, mittags Score 63→68 D2→D3) → V Rescoring-Revert nach Codex-HIGH-1+HIGH-2 (`b8cf4ae`, spätabends Score 68→64 D3→D2). Q3 FY26 ~Ende Juli mit ROIC-Methodology-Verify (PIPELINE #21).
- **29.04. ~22:30 MESZ AMC:** MSFT Q3 FY26 Earnings — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung).
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run.
- **01.05.:** Sparplan-Tag (EXUSA 825€ Aufstockung + reguläre Allokation). User-Action. **Nach V-Revert + ggf. MSFT-Resolve:** Sparraten manuell ING/Scalable updaten — V wieder 19,00€ (D2), volle Rate 38,00€ (für 7 D3/D4-Tickers); MSFT hängt von Q3-Outcome ab.

### 🔵 Deferred / Follow-up (PIPELINE.md)

- **#17/#18 Beispiele.md-Refactor + AVGO-ScoreRecord-Backfill:** Trigger post-MSFT-Live-Run 30.04.+ (siehe Folge-Resume oben).
- **#19 Schema `anker_relevanz`:** deferred bis nächster Anker-Promotion ohne Pre-Brief-Hint oder Anker-Tickers >5.
- **#16 INSTRUKTIONEN.md Slim-Refactor:** post-V/MSFT-Live-Runs ODER Konsolidierungstag.
- **#15 Pipeline-Test-Architektur-Hardening:** nach 3-4 realen Live-Runs P3-vor-P3.5-Bypass-Audit. Mitigation aktiv.
- **#11 Atomic-Write-Hardening portfolio_risk.py:** frozen, Re-Activation bei Incident oder Track-4-Auto-Hook.
- **#7 Track 5b FRED Macro-Regime-Filter:** deferred bis Sparrate >1.000€/Monat oder Depotwert >50.000€ oder Regime-Aware-Schmerz.
- **#20 Ruflo-Integration Phase 1.2:** Trigger post-#17/#18 (NICHT direkt nach Earnings). Pre-Read: `00_Core/RUFLO-INTEGRATION-PLAN.md` + `00_Core/RUFLO-PLAN-META-REVIEW.md`.
- **#21 defeatbeta-ROIC-V-Methodology-Verify (NEU 28.04. spätabends):** Trigger V Q3 FY26 Earnings ~Ende Juli.
- **#22 Helper `--porcelain -z`-mode-Robust-Follow-Up (NEU 28.04. spätabends):** Trigger Konsolidierungstag oder nächstes Pipeline-Path-Issue.
- **#23 Insider-Carryover-Discipline-Note (NEU 28.04. spätabends):** Trigger post-MSFT-Live-Run oder Konsolidierungstag — INSTRUKTIONEN-Edit.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€ (FLAG-modifiziert, Nenner 7,5 nach V-Revert), DEFCON v3.7 / Skill-Paket v3.7.4
- AVGO 84/D4 (FLAG Insider seit 27.04., Sparrate 0€), TMO 67/D3, MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`
- **V-Status:** 64/D2/19,00€. ROIC-Methodology-Watch in PIPELINE #21 für Q3 FY26 ~Ende Juli.

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.1 | Slim-Resume — Policy B | Stand: 2026-04-28 spätabends post-V-Rescoring-Revert (Resume-Trigger MSFT Q3 FY26 29.04.)*
