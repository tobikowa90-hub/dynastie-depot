# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 nach V-Rescoring-Revert. **V Rescoring-Revert DONE** (Commit `b8cf4ae`, Pipeline P1-P6 ✅, Δ-Gate accepted Δ=+1, Record #30 `2026-04-28_V_rescoring`, Score 64/🟠D2, Sparrate 19,00€). **Nächster primärer Resume-Trigger: MSFT Q3 FY26 Earnings 29.04. ~22:30 MESZ → !Analysiere MSFT als Second-Live-Run (FLAG-Review CapEx/OCF)**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `b8cf4ae` (V Rescoring-Revert nach Codex-HIGH-1+HIGH-2). Working tree mit Untracked-Anomalie-Files (shell-escape-Artefakte: `15%`, `15%-Niveau`, `FCF-Delta`, `,-`, `1`, `80`, `WACC`, `new\`)`, `"50.000Ô\303\251\302\274"`) — alle empty/garbage, ignorieren oder bei Konsolidierung aufräumen (Plan-Kandidat). Plus `00_Core/RUFLO-PLAN-META-REVIEW.md` untracked (Phase-1.2-Pre-Read) + `02_Analysen/Q2-2026-Earnings-Release_vF.pdf` untracked (V-Source-PDF, optional).

**V-Stand operativ:** 64/🟠D2/19,00€. Original-Record `2026-04-28_V_vollanalyse` bleibt historisch in jsonl (append-only). Alle 8 Sync-Files konsistent: PORTFOLIO/Faktortabelle/CORE-MEMORY/PIPELINE/STATE/config.yaml/log.md/score_history.jsonl. D2-Watch reaktiviert. Q3 FY26 ~Ende Juli mit ROIC-Methodology-Verify (PIPELINE #21).

**STATE.md Critical-Alert:** "28.04. V" entfernt. Verbleibender Alert: **29.04. MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung)**.

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

### 🟡 Folge-Resume nach MSFT-Live-Run (post-30.04. morgens)

**Resume-Trigger:** „Beispiele.md 4-Achsen-Refactor (PIPELINE #17) starten — V/MSFT-Anker einarbeiten + AVGO-FLAG-Patch + Cross-File-§-Refs"

**Vorbedingung:** MSFT-Vollanalyse 30.04. morgens DONE (ScoreRecord mit Anker-Hint appended). Falls FAIL (P3.5 oder anders): Refactor blockiert bis Recovery.

**WICHTIG — V als Anker-Pause:** Nach Codex-Review-Revert ist V als US-Voll-Anker für Beispiele.md #17 erst nach Q3 FY26 belastbar (nicht mehr "primär" wie ursprünglich Codex-96%-geplant). MSFT als Provenance-Gate-Second-Run-Demo bleibt valide. AVGO als sekundär (D4-Range 80-85 + FLAG-Override) bleibt valide. **Architektur-Update für #17:**
- **A. US-Pfad:** ~~V primär~~ → MSFT primär (Provenance-Gate-Second-Run + CapEx-FLAG-Auflösungs-/Veto-Pfad), AVGO sekundär (D4-Range + FLAG-Override), V tertiär mit explizitem "Forward-vs-Rescoring-Revert-Korrektur"-Anker-Hint (Lesson HIGH-1+2), TMO Cross-Reference auf Sub#4
- **B. Non-US-IFRS-Pfad:** ASML unverändert (frisch v3.7 17.04., FY27-Watch)
- **C. Screener-Exception-Katalog:** unverändert 6 Subs (#4 TMO primary, #5 MSFT, #6 ASML)
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
