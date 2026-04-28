# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 Abend (Update #2 nach Pre-MKL-Pipeline-Test-Session + Codex-Sparring 4-Achsen-Architektur). **Provenance-Gate Plan v3.1 KOMPLETT ABGESCHLOSSEN** (Tasks 0-6.5 + Mini-Patches A/B + V/MSFT-Pre-Append-Audit-Notices + Codex-Round-3-Reconcile). Joint-Confidence ~95%. **Beispiele.md 4-Achsen-Architektur entschieden (Codex Round-1+2 96%)** — Execution post-MSFT (PIPELINE #17/#18/#19). Pipeline ready für **V Q2 First-Live-Run** (heute 28.04. AMC ~22:00, Auswertung 29.04. morgens). **Resume-Trigger nach Pause: „!Analysiere V Q2 FY26 — First-Live-Run mit Provenance-Gate + Anker-Promotion (notizen-Hint)"**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `267a216` (Codex-Round-3 sec_edgar Multi-Word + Schritt-7 P3.5). Working tree clean. **9 Commits ahead** seit Handover `889becb`.

**Smoke-Test-Status:** schemas 14/14 ✓ + archive_score 5/5 ✓ + provenance_gate 9/9 ✓ (jetzt 8a-8o inkl. Multi-Word) + skill 8/8 ✓ = **36/36**. Re-Validate-Sweep jsonl 28/28 PASS.

**Provenance-Gate Plan v3.1 — Commits (chronologisch):**
| Commit | Task | Was |
|---|---|---|
| `5d97ddc` | 0.5 | TMO #28 Block-Coverage-Backfill (Migration-Helper, byte-level Line-Endings, idempotent) |
| `ef6979c` | 1 | versions.py SSoT + schemas Refactor |
| `5f4a6c5` | 2 | Schicht D Block-Coverage-Validator + Tests D1-D4 + archive_score-Fixture-Patch |
| `06ff82c` | A+B | Mini-Patches: Doc-Typo + Plan-File D1-D4 IDs |
| `cacf2a0` | 3 | provenance_gate.py Schicht B — 8 Checks fail-close, Carryover-Whitelist, 9/9 Smoke-Tests |
| `d039a5b` | 4 | forward-verify SKILL.md Phase P3.5 + Authoritative-Sources + FAIL-Phase-Enum |
| `e3547e9` | 5 | _smoke_test.py Case 7 (Integration fail-close) + Case 8 (Pipeline-Sequence-Order) |
| `507eb64` | 6 | SYSTEM.md + INSTRUKTIONEN §18.5 + CORE-MEMORY §10 + log.md Union-Scope |
| `bd83631` | 6.5 | dynastie-depot Schritt 6c Pre-Flight-Klausel + ma200_slope-Threshold |
| `4ca4654` | V/MSFT | Pre-Append-Audit-Klausel in Pre-Earnings-Briefs |
| `267a216` | R3 | Codex-Round-3 Sofort-Fixes (sec_edgar Multi-Word + Schritt-7-Summary) |

---

### 🎯 Nächster Schritt — V Q2 First-Live-Run

**Heute 28.04. AMC ~22:00 MESZ:** V Q2 FY26 Earnings (Quarter ending 31.03.2026). Daten morgen früh verfügbar.

**Pipeline-Erwartung im Erfolgsfall:**
1. Pre-Brief in `02_Analysen/V_pre-earnings_2026-04-28.md` enthält Pre-Append-Audit-Klausel (committed `4ca4654`, Zeile 9).
2. `!Analysiere V` 29.04. morgens via dynastie-depot Skill.
3. dynastie-depot Schritt 6c Pre-Flight-Klausel pro Block durchgehen (Sub-Score!=0 ↔ Rohwert/Carryover-Konsistenz).
4. **NEU — Anker-Promotion-Hint im ScoreRecord setzen** (Beispiele.md-4-Achsen-Architektur, PIPELINE #17): `notizen` enthält `anker_promotion_kandidat=us_voll_anker, mechanismen=[fundamentals_cap_50, forward_vs_backfill_korrektur, provenance_gate_first_run]`. Existierendes Pipeline-Feld, kein Schema-Change. Beim MSFT-Run analog mit `anker_promotion_kandidat=screener_exception_sub5, mechanismen=[capex_flag_bereinigter_pfad, finance_lease_decomposition, provenance_gate_second_run]`.
5. Schritt 7 Archive-Write via backtest-ready-forward-verify Skill — Pipeline-Sequenz: P1 → P2a (alle 3 Pflicht-Files modified) → P2b (V in PORTFOLIO.md) → **P3.5 (NEU, 8 Checks pass)** → P3 (skill_meta=ja → Δ-Gate) → P4/P5/P6 grün.
6. Joint-Confidence 92% → 95%+ erwartet.

**Falls P3.5 FAIL:** Recovery-Pfad via Workflow-Korrektur (Pflicht-Touch-Files berühren / `analyse_typ` umklassifizieren / `quellen` mit echten Quellen oder legitimen `*_carryover`-Suffixen befüllen / Versions-Drift via Migration-Pipeline lösen). Kein `--force`-Bypass.

**Eigener CORE-MEMORY §10-Eintrag** nach erfolgreicher Pipeline-Sequenz: konkrete P3.5-Output + tatsächlicher Δ-Gate-Outcome + Pre-Flight-Audit-Result + Anker-Promotion-Status (notizen-Feld gesetzt ja/nein).

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

- **HEUTE 28.04. AMC ~22:00:** V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?).
- **MORGEN 29.04. AMC ~22:30:** MSFT Q3 FY26 — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung). Pre-Append-Audit-Klausel auch in MSFT-Pre-Brief committed.
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run.
- **01.05.:** Sparplan-Tag (EXUSA 825€ Aufstockung + reguläre Allokation). User-Action.

### 🔵 Deferred / Follow-up (PIPELINE.md)

- **#17/#18 Beispiele.md-4-Achsen-Refactor + AVGO-ScoreRecord-Backfill:** Trigger post-MSFT-Live-Run 30.04.+ (siehe Folge-Resume-Block oben).
- **#19 Schema `anker_relevanz`:** deferred bis nächster Anker-Promotion ohne Pre-Brief-Hint oder Anker-Tickers >5.
- **#16 INSTRUKTIONEN.md Slim-Refactor:** post-V/MSFT-Live-Runs ODER Konsolidierungstag.
- **#15 Pipeline-Test-Architektur-Hardening (Codex-Round-3 MEDIUM #2 + LOW #3):** Case 7+8 sind Stub-Pipeline-Tests, kein echter Python-Entry-Point. Re-Activation-Trigger: nach 3-4 realen Live-Runs P3-vor-P3.5-Bypass-Audit. Mitigation aktiv via Schritt 6c + Pre-Append-Audit.
- **#11 Atomic-Write-Hardening portfolio_risk.py:** frozen, Re-Activation bei Incident oder Track-4-Auto-Hook.
- **#7 Track 5b FRED Macro-Regime-Filter:** deferred bis Sparrate >1.000€/Monat oder Depotwert >50.000€ oder Regime-Aware-Schmerz.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€ (FLAG-modifiziert), DEFCON v3.7 / Skill-Paket v3.7.4
- AVGO 84 (FLAG Insider seit 27.04., Sparrate→0€), TMO 67 D3, MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`

### 📊 Codex-Sparring-Bilanz (Session 28.04.)

- **Round 1** (Single-Pass auf Tasks 0-2): 0 HIGHs, 1 MEDIUM (Plan-File-Drift), 2 LOWs, 4 PASSes.
- **Round 2** (Reconcile + 95%-Frage): 1 NEUER HIGH (Pre-Flight-Klausel war Frame-blind in R1), 1 MEDIUM (Plan-Inline), 1 LOW (ma200_slope), 1 NEUER 4. Punkt (V/MSFT Audit).
- **Round 3** (Single-Pass auf Tasks 3-6.5 + Mini-Patches + Audit-Notices): 0 HIGHs, 2 MEDIUMs (sec_edgar toter Whitelist-Eintrag + Case 7 tautologisch), 2 LOWs (Case 8 Stub + Schritt-7-Summary fehlt P3.5). Variante 1 sofort committed (`267a216`), Variante 2 deferred via PIPELINE #15.
- **Bilanz:** Reconcile-Round-2 fand HIGH dass R1 nicht hatte. Round-3 fand realen Whitelist-Bug (sec_edgar Multi-Word) + Doku-Drift (Schritt-7-Summary). Memory `feedback_codex_sparring_heuristic.md` validiert.

### Memory-Hooks aktiv

- feedback_review_via_codex_not_advisor.md — 3 Codex-Rounds Provenance-Gate-Cluster + 2 Codex-Rounds Beispiele.md-4-Achsen-Cluster in Session 28.04.
- feedback_codex_sparring_heuristic.md — VALIDIERT Provenance-Round-3 + Beispiele-Round-2 (Reconcile brachte AVGO-D4-Argument + AVGO-ScoreRecord-Bug).
- feedback_anchor_promotion_sync_gap.md (NEU 28.04.) — 4-Achsen-Pattern, Doppelrolle-via-Cross-Reference, Live-Frische schlägt Legacy-Subscores. Aktiviert für Refactor-Session post-MSFT.
- feedback_windows_python_crlf_text_mode.md — byte-level Line-Ending-Preservation (0 ungewollte Konvertierungen).
- feedback_pre_commit_diff_inspection.md — alle 11 Commits via `git diff --cached --stat` vor commit verifiziert.
- feedback_onedrive_edit_collision.md — keine Kollisionen.

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B | Stand: 2026-04-28*
