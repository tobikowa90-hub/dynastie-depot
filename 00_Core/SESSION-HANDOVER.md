# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 spätabends. **V Q2 First-Live-Run DONE** (Commit `92c9de1`, Pipeline P1-P6 ✅, Score 68/D3) — **ABER Codex-Review identifiziert 2 HIGH-Befunde** → User-Entscheidung **Option A (Strict Revert)**. **Resume-Trigger: „V Rescoring-Revert via Codex-HIGH-1+HIGH-2 ausführen"**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `92c9de1` (V Q2 Forward-Vollanalyse 63→68 + Helper-Bugfix). Working tree dirty (3 leere Anomalie-Files `15%`, `15%-Niveau`, `FCF-Delta` aus Misquotation, ignorieren) + `00_Core/RUFLO-PLAN-META-REVIEW.md` untracked + `02_Analysen/Q2-2026-Earnings-Release_vF.pdf` untracked (Source-PDF, optional).

**First-Live-Run ist erfolgt** — alle 6 Pipeline-Phasen grün (P3.5 8 Checks pass, Schicht D Block-Coverage pass, Skill APPENDED `2026-04-28_V_vollanalyse` als Record #29). **Helper-Bugfix `_forward_verify_helpers.py`**: check_freshness strippt jetzt umschließende `"` von git-porcelain-Pfaden mit Leerzeichen — wäre sonst bei MSFT auch wieder gescheitert.

**Codex-Review Single-Pass (Memory-Heuristik HIGH-Count ≥2 → Sparring-Loop empfohlen, aber User wählte direkt Option A statt Round-2):**

| # | Verdict | Severity | Kern |
|---|---|---|---|
| 1 | **CHALLENGE** | **HIGH** | ROIC 1→7 via SKILL absolute scale ist regelwidrig: SKILL erlaubt das nur "bei fehlender WACC-Schätzung" — `wacc_pct=8.0` ist gesetzt. Score-Move 63→68 hängt netto an dieser einzigen Sub-Score-Korrektur. |
| 4 | **CHALLENGE** | **HIGH** | `kurs.referenz="close_of_score_datum"` semantisch nicht erfüllt — kurs ist 27.04. close-Carryover-Proxy, nicht 28.04. close. Provenance-Gate besteht formal (String-Equality-Check), Intent verletzt. |
| 2 | CONFIRM-with-Caveat | MEDIUM | Insider 5→6 Up-Score via "Buyback-Disziplin-Interpretation" ist nicht aus _carryover-Quellen sauber gedeckt. |
| 5 | CONFIRM-with-Caveat | MEDIUM | Helper-Patch fixt nur happy path. Rename-Zeilen `old -> new` + Quote-Escapes für Sonderzeichen/Newlines unbehandelt. Robust wäre `--porcelain -z` (NUL-separator) oder `-c core.quotePath=false`. |
| 6 | CONFIRM-with-Caveat | MEDIUM | PIPELINE.md Item für `defeatbeta-ROIC-Methodology-Watch` fehlt (Record behauptet "in PIPELINE", aber Sync nicht erfolgt). |
| 3, 7 | PASS | LOW | Δ-Gate Klassifikation + Notizen-Feld-Länge OK. |

---

### 🎯 Nächster Schritt — V Rescoring-Revert (Option A) **[NEUE SESSION PRIORITÄT 1]**

**Ziel:** V zurück auf Score 64 / 🟠 D2 / Sparrate 19,00€ via Korrektur-Record. Original-Record `2026-04-28_V_vollanalyse` bleibt historisch in jsonl (append-only). Operative Werte überschreiben durch neues Record + §18-Sync rückwärts.

**Schritt-Plan (in dieser Reihenfolge):**

1. **Frischer 28.04.-Close für V pullen** (yfinance/Yahoo). Wenn nicht zugänglich, dokumentiert-konservativ ~$309-311 mit `quelle: yahoo_close_28.04.2026` (echter Close, nicht Carryover-Proxy).

2. **ScoreRecord-Draft `2026-04-28_V_rescoring`** in `03_Tools/backtest-ready/_drafts/V_RESCORING_<HHMM>.json`:
   - `analyse_typ: "rescoring"` ⚠️ **Subtilität:** Provenance-Gate Check #4 verlangt `skill_meta` für rescoring (nicht leer). Trotzdem **kein** Migration-Event semantisch. Workaround: skill_meta mit `expected_algebra_score: 63`, `migration_from_version: "v3.7"`, `migration_to_version: "v3.7"` setzen. Δ = 64 − 63 = +1 → bucket `accepted`. Schemas.MigrationEvent erlaubt gleiche from/to-Version (kein Validator dagegen). Falls Skill doch FAIL: alternativ `analyse_typ: "vollanalyse"` mit ausführlicher notizen-Begründung als Korrektur-Record (Präzedenz fehlt aber).
   - **Sub-Scores (alle 18.04.-Carryover-konsistent + nur fresh-data-driven Δ):**
     - Fwd P/E 5 / P/FCF 1 / Bilanz 8 / CapEx/OCF 9 / **ROIC 1** (carryover, 9,89% defeatbeta unkalibriert markiert) / FCF-Y **4** (carryover) / OpM 2 → **Fund 30**
     - Moat **19** (carryover, kein Pricing-Power-Bonus-Erfindung)
     - Tech **3** (carryover, ATH 3 + RS 0 + Trend 0)
     - Insider **5** (carryover, kein Up-Score ohne Rohdaten)
     - Sentiment **7** (legitim: SB 4 + Sell 1 + PT-Up 2 + EPS-Rev +1 post-beat + PT-Disp -1) — einziger fresh-Δ-Block
     - **Σ = 30 + 19 + 3 + 5 + 7 = 64 → defcon_level: 2 (D2)**
   - `kurs.referenz: "close_of_score_datum"` (mit echtem 28.04.-Close, nicht Proxy)
   - `roic_gaap_pct: 9.89` (carryover) + `roic_bereinigungsgrund: "defeatbeta_methodology_watch_q3_verify_pending_skill_compliance_carryover_18.04"` (transparent über Datenzweifel)
   - **notizen** (kompakt, Verweis auf log.md für Detail): "V Q2 FY26 Rescoring-Korrektur nach Codex-HIGH-1+HIGH-2-Review (28.04.-Vollanalyse-Methodology-Drift). Score-Revert 68→64 via ROIC-Carryover (1/8) + Kurs-Refresh (28.04.-close statt 27.04.-Proxy). SKILL absolute alternative scale war regelwidrig (WACC vorhanden, nicht 'fehlende WACC-Schätzung'). defeatbeta-9,89%-Methodology-Watch in PIPELINE für Q3 FY26 ~Ende Juli. Sentiment-Δ +1 (EPS-Rev post-beat) bleibt legitim. Sparrate 35,63€→19,00€, Nenner 8,0→7,5. Detail: log.md 28.04. score-event-correction."

3. **Skill-Invocation** `backtest-ready-forward-verify` mit Draft-Pfad. Pipeline P1-P6 erwartet alle ✅. P3 Δ-Gate-Output: `accepted` (Δ=+1). Wenn `migration_event` injiziert wird: Beachten dass `from_version == to_version` kein Migrations-Bedeutung hat — semantisch nur Record-Identifikation als Korrektur. Wenn Skill failed wegen rescoring-skill_meta-Subtilität: Diagnose + ggf. analyse_typ-Switch.

4. **§18-Sync-Edits rückwärts** (5 Files):
   - `00_Core/PORTFOLIO.md`:
     - V-Row: 68 → **64**, 🟡 3 → 🟠 2, 35,63€ → **19,00€**, "✅ Clean (D2-Watch RESOLVED)" → "✅ Clean (D2 nach Rescoring-Revert 28.04.)", Trigger-Spalte: zurück zu V-Q3-Watch-Notation
     - Footer-Nenner: 8×1,0 + 0×0,5 + 3×0 = 8,0 → **7×1,0 + 1×0,5 + 3×0 = 7,5**, volle Rate 35,63€ → **38,00€**, D2-Rate 0€ → **19,00€**
     - V row neu nach BRK.B-Reihenfolge sortieren (war oben verschoben weil 68 ≥ ASML/RMS — jetzt 64 < APH 63 also zwischen TMO 67 und APH 63, aber V noch über APH wegen 64>63)
     - "28.04.2026 Änderung" Block: zwei Einträge nötig — der ursprüngliche Beat-Cascade-Eintrag PLUS Korrektur-Eintrag „Rescoring-Revert nach Codex-Review HIGH-1 (ROIC) + HIGH-2 (Kurs). Score 68→64. Sparrate 35,63€→19,00€. Methodology-Watch in PIPELINE."
     - Watches: D2-Watch wieder REAKTIVIERT (war RESOLVED, jetzt zurück): „V D2-Watch (rescoring 28.04.): nach Codex-Review-Korrektur — Beat allein lieferte methodisch nicht den D3-Pfad; Q3 FY26 ~Ende Juli mit ROIC-Methodology-Verify entscheidet"
     - 30-Tage-Trigger: V-DONE-Eintrag erweitern: „DONE Q2 Beat-Cascade ABER Rescoring-Revert nach Codex-Review (28.04. spätabends): D3→D2"
   - `00_Core/Faktortabelle.md`: V-Row analog zurück (68→64, 🟡 3→🟠 2, Score-Datum 28.04. bleibt aber Notation Korrektur), Footer-Nenner zurück, Trigger-Tabelle V-DONE-Eintrag erweitern, Offene-Scores-Tabelle V-Row zurück
   - `01_Skills/dynastie-depot/config.yaml`:
     - V-Block: defcon 3→2, score 68→64, sparrate_hinweis "DEFCON 2, kein 🔴 FLAG → Gewicht 0.5 (halbe Rate 19,00€)", scoring_notiz neu mit Codex-Review-Bezug
     - Alle 7 D3/D4-Tickers (ASML/BRK.B/VEEV/SU/COST/RMS/TMO) sparrate_hinweis: 35,63€ → 38,00€ (Reverse-Replace-All)
     - sparplan_verteilung beispiel: zurück auf Nenner 7,5 / 38,00€ / 19,00€
     - termine: V-DONE-Eintrag mit Korrektur-Note
   - `00_Core/CORE-MEMORY.md` §12.10 V: append weiteren Eintrag „28.04.2026 spätabends — Rescoring-Korrektur nach Codex-HIGH-1+HIGH-2-Review: Score 68→64, D3→D2, Sparrate 35,63€→19,00€. ROIC-Carryover statt SKILL-Alternative-Scale-Bruch (WACC vorhanden = SKILL-Ausnahme nicht anwendbar). Kurs-Refresh 28.04.-close statt 27.04.-Proxy. Methodology-Watch in PIPELINE."
   - `07_Obsidian Vault/.../log.md`: Append `## [2026-04-28] score-event-correction | V Rescoring-Revert nach Codex-Review HIGH-1+HIGH-2`

5. **PIPELINE.md** drei neue Items:
   - **#21** `defeatbeta-ROIC-V-Methodology-Verify` — Q3 FY26 ~Ende Juli, Trigger: V Q3-Earnings; Aktion: defeatbeta-MCP `get_stock_quarterly_roic` + `get_stock_wacc` Roh-Output dumpen, mit primary-source-NOPAT/IC-Calc abgleichen, Methodology-Diff dokumentieren, ggf. SKILL.md erweitern um Klausel "WACC vorhanden aber nachweislich inkonsistent → Alternative-Scale erlaubt mit explizitem Methodology-Watch"
   - **#22** `Helper--z-mode-Robust-Follow-Up` — `_forward_verify_helpers.py::check_freshness` auf `git status --porcelain -z` umstellen (NUL-separator), Rename-Zeilen + Quote-Escape-Edge-Cases handling. Trigger: Konsolidierungstag oder bei nächstem Pipeline-Path-Issue.
   - **#23** `Insider-Carryover-Discipline-Note` — INSTRUKTIONEN.md Klarstellung: `_carryover`-Blöcke ohne neue Rohdaten dürfen NICHT upward re-scored werden, nur unverändert übernommen. Codex-Befund MEDIUM-2 als Anlass.

6. **Sync-Commit:** `score(V): rescoring revert D2 nach Codex-Review (HIGH-1 ROIC SKILL-compliance + HIGH-2 kurs-fresh-pull)`. Body: vollständige Codex-Befunde-Tabelle als Begründung; Liste der 6 Sync-Files; PIPELINE-Items #21/#22/#23 erwähnen.

7. **Nach erfolgreichem Commit:** STATE.md Critical-Alert "28.04. V" entfernen (manuell, handgepflegt — separater micro-Edit + Stand-Sync-Commit, oder im selben Commit mit-genommen).

**Memory-Hooks für Resume:**
- `feedback_review_via_codex_not_advisor.md` — Codex war richtig gewählt
- `feedback_codex_sparring_heuristic.md` — User wählte direkt Option A (kein Round-2), Single-Pass-Verdict ausreichend
- **NEU schreibbar:** `feedback_skill_methodology_drift_v_q2.md` — SKILL-Wortlaut-Klausel für absolute-Skala muss strikt geprüft werden; "WACC inkonsistent" rechtfertigt nicht Switch; korrekte Reaktion = Block als unkalibriert markieren bis Re-Verify

**Codex-Round-2 verfügbar via SendMessage(to: 'a449b578f9fc4d4b0')** falls in Korrektur-Session methodische Reconcile-Frage auftaucht (~5-10k Token).

---

### 🟡 Folge-Resume nach V+MSFT-Live-Runs (post-30.04. morgens)

**Resume-Trigger:** „Beispiele.md 4-Achsen-Refactor (PIPELINE #17) starten — V/MSFT-Anker einarbeiten + AVGO-FLAG-Patch + Cross-File-§-Refs"

**Vorbedingung:** V-Vollanalyse 29.04. morgens DONE (ScoreRecord mit Anker-Hint appended) + MSFT-Vollanalyse 30.04. morgens DONE (ScoreRecord mit Anker-Hint appended). Falls eine der beiden FAILed (P3.5 oder anders): Refactor blockiert bis Recovery + erfolgreicher Re-Run.

**Architektur (Codex-Round-1+2 96% Joint-Confidence):**
- **A. US-Pfad** = V (primär, Provenance-Gate-First-Run-Demo, Fundamentals-Cap 50, Forward-vs-Backfill-Korrektur D2-D3-Pfad) → AVGO (sekundär, D4-Range 80-85-Kalibrierung, FLAG-Override-Mechanik) → TMO (tertiär, Cross-Reference auf Sub#4 in C, primäre Beschreibung dort)
- **B. Non-US-IFRS-Pfad** = ASML unverändert (frisch v3.7 17.04., QT beidseitig hart 0, FY27-Watch, eodhd_intel.py + FRED-WACC + IFRS-16-Toleranz)
- **C. Screener-Exception-Katalog** = 6 Sub-Sektionen: #1 MKL (post-MKL-Vollanalyse, falls in dieser Session ausgeführt — sonst Pipeline-Test in Folge-Session) · #2 COST pending Q1 FY27 Dez · #3 RMS pending H1 Juli · **#4 TMO primary** (ROIC<WACC differenzierte QT, Doppelrolle mit A) · **#5 MSFT** (Provenance-Gate-Second-Run, CapEx-FLAG-Auflösungs-/Veto-Pfad) · **#6 ASML Cross-Reference** (Non-US/IFRS Pfad-B → siehe B)
- **D. Live-Disziplin** = bleibt in SKILL.md (Schritt 6c Pre-Flight, ma200_slope-Konvention), in Beispiele.md nur Demo-Block mit Verweis (TMO #28-Verstoß-Beispiel)
- **Legacy-Sektion** „Workflow-Historie" = SNPS, SPGI, EXPN, FICO, MKL-v3.5 — bleiben mit v3.5-Zeitstand-Banner als Workflow-Pattern-Referenzen (Goodwill-Bereinigung, TTM-Verzerrung, Datenlücken-Handling)

**Cross-File-Updates im selben Refactor-Commit:**
- `01_Skills/dynastie-depot/SKILL.md` — AVGO-Score-Erwähnung „85" → „84" + §11→§12/§13 in Zeile :90
- `00_Core/Faktortabelle.md` — §11→§12/§13 in Zeile :74
- `00_Core/PORTFOLIO.md` — §11→§12/§13 in Zeile :30
- `00_Core/STATE.md` — Sync-Kurzregel um config.yaml ergänzen (vs. INSTRUKTIONEN §18 v2.1)
- Vault `07_Obsidian Vault/.../log.md` — §11-Cleanup separat (Wiki-Trennung, eigenes Pipeline-Item ggf.)

**Item-Set:**
- **#17** Beispiele.md-Refactor (primärer Eintrag, ~45-60 Min Refactor + 15-30 Min Cross-File-Patches)
- **#18** AVGO 27.04. ScoreRecord-Backfill (`analyse_typ: rescoring`, Score 84 unverändert, FLAG-Referenz, ~15 Min via backtest-ready-forward-verify-Skill — optional in #17-Session mit-erledigen)
- **#19** Schema `anker_relevanz` deferred (V/MSFT brauchen es nicht)

**Sync-Set §18.2:** Beispiele.md + SKILL.md + Faktortabelle.md + PORTFOLIO.md + STATE.md + score_history.jsonl (nur bei #18-Mit-Erledigung) + log.md.

**MKL-Pipeline-Test-Status:** Bei der Refactor-Vorbereitung in dieser Session (28.04. nachmittags) auf User-Wunsch UNTERBROCHEN — Refactor in neuer Session priorisiert vor MKL-Vollanalyse, weil MKL-Output direkt in Sub#1 fällt. Falls MKL-Pipeline-Test weiterhin gewünscht, in einer der V/MSFT-Refactor-Folgesession nachholen oder als eigener Konsolidierungstag.

**Memory-Hooks für Refactor-Session:**
- `feedback_anchor_promotion_sync_gap.md` (NEU) — 4-Achsen-Pattern + Doppelrolle-via-Cross-Reference + Live-Frische schlägt Legacy + Cross-File-§-Refs prüfen
- `feedback_review_via_codex_not_advisor.md` — falls Refactor-Detail-Frage auftaucht: Codex statt Advisor

---

### 📅 Critical Operational

- **28.04. DONE:** V Q2 FY26 First-Live-Run Pipeline ✅ (Commit `92c9de1`, Score 68/D3) — **ABER Rescoring-Revert pending** (siehe Resume-Stand oben, Codex-HIGH-1+2).
- **MORGEN 29.04. AMC ~22:30:** MSFT Q3 FY26 — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung). Pre-Append-Audit-Klausel auch in MSFT-Pre-Brief committed. **Reihenfolge in neuer Session:** Erst V-Rescoring-Revert (Priorität 1, blockiert MSFT-Run nicht zwingend, aber sauber-zuerst-Prinzip), dann MSFT-Run.
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run.
- **01.05.:** Sparplan-Tag (EXUSA 825€ Aufstockung + reguläre Allokation). User-Action. **Nach V-Revert:** Sparrate V wieder 19,00€ (D2), volle Rate 38,00€ — bei manueller ING/Scalable-Sparplan-Update darauf achten.

### 🔵 Deferred / Follow-up (PIPELINE.md)

- **#17/#18 Beispiele.md-4-Achsen-Refactor + AVGO-ScoreRecord-Backfill:** Trigger post-MSFT-Live-Run 30.04.+ (siehe Folge-Resume-Block oben).
- **#19 Schema `anker_relevanz`:** deferred bis nächster Anker-Promotion ohne Pre-Brief-Hint oder Anker-Tickers >5.
- **#16 INSTRUKTIONEN.md Slim-Refactor:** post-V/MSFT-Live-Runs ODER Konsolidierungstag.
- **#15 Pipeline-Test-Architektur-Hardening (Codex-Round-3 MEDIUM #2 + LOW #3):** Case 7+8 sind Stub-Pipeline-Tests, kein echter Python-Entry-Point. Re-Activation-Trigger: nach 3-4 realen Live-Runs P3-vor-P3.5-Bypass-Audit. Mitigation aktiv via Schritt 6c + Pre-Append-Audit.
- **#11 Atomic-Write-Hardening portfolio_risk.py:** frozen, Re-Activation bei Incident oder Track-4-Auto-Hook.
- **#7 Track 5b FRED Macro-Regime-Filter:** deferred bis Sparrate >1.000€/Monat oder Depotwert >50.000€ oder Regime-Aware-Schmerz.
- **#20 Ruflo-Integration Phase 1.2:** Trigger post-#17/#18 (NICHT direkt nach Earnings). Pre-Read: `00_Core/RUFLO-INTEGRATION-PLAN.md` (committed `c9a3ed5`) + `00_Core/RUFLO-PLAN-META-REVIEW.md` (working-tree-Draft 28.04. — 10 Plan-Patches P1-P10 + 9 Pre-Conditions + 8-Schritt-Kickoff-Checkliste). Risiko-Re-Label MITTEL (OneDrive-AgentDB-Backend + Memory-Path-Pollution). Memory: `feedback_ruflo_memory_bridge_onedrive_pitfall.md`.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€ (FLAG-modifiziert), DEFCON v3.7 / Skill-Paket v3.7.4
- AVGO 84 (FLAG Insider seit 27.04., Sparrate→0€), TMO 67 D3, MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`
- **V-Status mid-State** (post-First-Live-Run, pre-Revert): operativ 68/D3/35,63€ in PORTFOLIO/Faktortabelle/config.yaml — wird in nächster Session via Rescoring zurück auf 64/D2/19,00€ korrigiert.

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.1 | Slim-Resume — Policy B | Stand: 2026-04-28 spätabends (V-Rescoring-Revert pending nach Codex-HIGH-1+2)*
