# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 nach V-Rescoring-Revert. **V Rescoring-Revert DONE** (Commit `b8cf4ae`, Pipeline P1-P6 ✅, Δ-Gate accepted Δ=+1, Record #30 `2026-04-28_V_rescoring`, Score 64/🟠D2, Sparrate 19,00€). **Nächster primärer Resume-Trigger: MSFT Q3 FY26 Earnings 29.04. ~22:30 MESZ → !Analysiere MSFT als Second-Live-Run (FLAG-Review CapEx/OCF)**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `b8cf4ae` (V Rescoring-Revert nach Codex-HIGH-1+HIGH-2). Working tree mit Untracked-Anomalie-Files (shell-escape-Artefakte: `15%`, `15%-Niveau`, `FCF-Delta`, `,-`, `1`, `80`, `WACC`, `new\`)`, `"50.000Ô\303\251\302\274"`) — alle empty/garbage, ignorieren oder bei Konsolidierung aufräumen (Plan-Kandidat). Plus `00_Core/RUFLO-PLAN-META-REVIEW.md` untracked (Phase-1.2-Pre-Read) + `02_Analysen/Q2-2026-Earnings-Release_vF.pdf` untracked (V-Source-PDF, optional).

**V-Stand operativ:** 64/🟠D2/19,00€. Original-Record `2026-04-28_V_vollanalyse` bleibt historisch in jsonl (append-only). Alle 8 Sync-Files konsistent: PORTFOLIO/Faktortabelle/CORE-MEMORY/PIPELINE/STATE/config.yaml/log.md/score_history.jsonl. D2-Watch reaktiviert. Q3 FY26 ~Ende Juli mit ROIC-Methodology-Verify (PIPELINE #21).

**STATE.md Critical-Alert:** "28.04. V" entfernt. Verbleibender Alert: **29.04. MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung)**.

---

### 🎯 Nächster Schritt — MSFT Q3 FY26 Vollanalyse (29.04.2026 morgens) **[NEUE SESSION PRIORITÄT 1]**

**Resume-Trigger:** „!Analysiere MSFT" oder „MSFT Q3 FY26 Vollanalyse starten"

**Kontext:** Earnings Release 29.04.2026 ~22:30 MESZ AMC. FLAG aktiv seit Q1 (CapEx/OCF Q2 FY26: 83,6% nominal; bereinigt um Finance Leases ~63%). FLAG-Auflösungs-Pfad: bereinigtes CapEx/OCF <60% = Auflösung; ≥60% = Veto-Verschärfung.

**Pipeline-Disziplin:**
1. **Pre-Brief lesen** (falls vor Ergebnis: Pre-Earnings-Snapshot von Pre-Brief). Nach Earnings-Release: PDF-Source ziehen (analog V Q2-2026-Earnings-Release_vF.pdf).
2. **Schritt 6c Pre-Flight (v3.7.4) MANUELL durchgehen** — alle 5 Blöcke prüfen: Sub-Score!=0 mit Roh-Wert oder `_carryover`-Marker. Insbesondere bei Carryover-Blöcken: kein Up-Score ohne neue Rohdaten (Lesson V-MEDIUM-2 + neuer PIPELINE #23 Insider-Carryover-Disziplin).
3. **SKILL-Wortlaut-Disziplin (Lesson V-HIGH-1):** Bei Methodology-Switches (Skala-Wechsel innerhalb Block, z.B. ROIC absolute vs. WACC-relativ) SKILL-Klausel literal prüfen. WACC-Eintrag im Record gesetzt → kein Switch auf alternative Skala. Carryover + Methodology-Watch + Reviewer-OK statt Switch.
4. **Kurs-Frische (Lesson V-HIGH-2):** `kurs.referenz="close_of_score_datum"` semantisch erfüllen mit echtem Tagesschluss-Close, nicht Carryover-Proxy. defeatbeta-Cutoff prüfen mit `get_latest_data_update_date` → falls Cutoff < score_datum, yfinance-Fallback (analog V: $309,30 yahoo_close_28.04.2026).
5. **Schritt 7 via `backtest-ready-forward-verify`-Skill** — Draft als bare ScoreRecord mit `analyse_typ: "vollanalyse"`. **Kein skill_meta** (kein Migration-Event bei normaler Vollanalyse, nur bei Version-Migration oder Korrektur-Record).
6. **§18-Sync v2.1 (8 Files):** PORTFOLIO + Faktortabelle + CORE-MEMORY §12.5 (MSFT) + PIPELINE (FLAG-Status-Update) + STATE (Critical-Alert "29.04. MSFT" entfernen) + config.yaml + log.md + score_history.jsonl. Bei FLAG-Trigger/Resolve zusätzlich `flag_events.jsonl` via `archive_flag.py resolve|trigger`.
7. **Sparraten-Kaskade je nach Outcome:**
   - **CapEx/OCF bereinigt <60%** → FLAG-Auflösung. MSFT in volle D-Stufe (Score 59 → ggf. höher post-Q3, aber Score Q3 dependent). Sparrate 0€ → Gewicht 1,0 oder 0,5 abhängig von Score-Δ. Nenner verschiebt sich.
   - **CapEx/OCF bereinigt ≥60%** → FLAG bleibt. MSFT-Sparrate weiter 0€. Nenner unverändert. Ggf. zusätzliche Watch oder DEFCON-1-Eskalation (wenn Score < 50).
8. **Codex-Single-Pass-Review nach Schritt 7** — Single-Pass Default; Sparring nur bei HIGH-Count ≥2 oder strukturellen Coverage-Gaps (Memory `feedback_codex_sparring_heuristic.md`).

**Memory-Hooks für MSFT-Lauf:**
- `feedback_skill_methodology_drift_v_q2.md` (NEU) — SKILL-Wortlaut-Disziplin
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
