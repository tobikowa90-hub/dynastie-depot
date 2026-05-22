# Build-Time Review-Log

Append-only Versions-Historie. Eintrag pro Skill-Version + Review-Pass.

---

## v0.1.0 — 2026-05-23

**Acceptance-Kriterien für Promotion (alle erfüllt für v0.1.0):**

- **Spec:** `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` v0.3 (28 Befunde adoptiert in 3 Codex-Runden).
- **Plan:** `docs/superpowers/plans/2026-05-22-paragraph-18-sync-implementation.md` v0.2 (Codex-Plan-Review 7 Findings adoptiert).
- **Build-Sessions:** 22.05. (Tasks 1-12 + CP1/CP2/CP3-R1+R2) → 23.05. (Tasks 13-18).
- **Test-Suite:** S1-S20 implementiert + erweiterte H1/H2-Coverage; aktuell **51 collected = 48 PASS + 3 SKIP** (S7+S8a soft-skip by design; S3 conditional skip wenn `score_history.jsonl` kein heute-Append).
- **Reviews (alle 3 Pflicht):**
  - Codex Single-Pass (gpt-5.3-codex via `~/.codex/config.toml`-Pin).
  - Gemini-CLI direct stdin-pipe Cross-Sync (SKILL.md ↔ INSTRUKTIONEN §18).
  - CodeRabbit `coderabbit review -t uncommitted --dir 03_Tools/para18_sync` (WSL Ubuntu).
- **Dogfood:** 4 Test-Cases gegen Live-State (pipeline-item / critical-alert / score-event / multi-event-union).
- **Promotion-Sync-Set (v0.1 verpflichtend, Codex-L2-Fix 2026-05-22):** PIPELINE #73a DONE + log.md Promotion-Entry + SYSTEM.md Skill-Registry + Active-xlsx-Block + CLAUDE.md Routing-Table-Eintrag `!ParaSync18` (v0.1-Pflicht, nicht v0.2-deferred).

---

## Review-Pass — 2026-05-23 (Task 16, v0.1.0 Final-Reviews)

**Codex (gpt-5.3-codex) Single-Pass:** **3 HIGH + 1 MEDIUM + 1 LOW** — alle 5 adoptiert.

- **HIGH-1 §18.2 `version_bump`-Conditional nicht ausgewertet (Spec-Drift):** FIXED — `compute_union_set()` neuer `version_bump`-Parameter; CLI-Flag `--version-bump`; 2 neue Tests (`test_h1_version_bump_conditional_applied`, `test_h1_version_bump_cli_flag_smoke`).
- **HIGH-2 P6/B xlsx-set-match Drift-Guard fehlt:** FIXED — `_run_verify_b()` re-resolved `marker.xlsx_tool_stems` gegen aktuelles SYSTEM.md, vergleicht gegen `marker.expected_xlsx`; Mismatch → `EXIT_FAIL_P6`. Marker-Schema erweitert um `xlsx_tool_stems`. 2 neue Tests (`test_h2_verify_b_xlsx_set_mismatch_after_pin_change`, `test_h2_verify_b_xlsx_set_match_no_drift`).
- **HIGH-3 Exit-Code-Inkonsistenz (xlsx unstaged in verify-b returns 4 statt 6):** FIXED — `_run_verify_b()` Strict-Stage-Check returnt jetzt `EXIT_FAIL_P6`; bestehender Test `test_verify_b_hard_fails_on_unstaged_xlsx_integration` angepasst.
- **MED-1 Doku `commit_a_sha` Wortlaut "HEAD-Vorgänger":** FIXED — SKILL.md + failure-recovery.md auf "marker.commit_a_sha == aktuelles HEAD vor Commit-B" korrigiert.
- **LOW-1 Comment-Typo "n/n":** FIXED — validator.py:12 docstring auf "(y/n)".

**Codex-Sparring-Loop R2 (Diff-Re-Review von f096600):** **PASS-WITH-NITS** (0 HIGH neu, 1 MED test-härte, 1 LOW PROJECT_ROOT-Bindung). R1-Residual-Check: H1+H2+H3 alle korrekt umgesetzt; Marker-Backwards-Compat OK; Doc-Konsistenz OK. R2-Nits adressiert:

- **R2-MED Drift-Guard-Negativtest:** FIXED — `test_h2_verify_b_xlsx_set_match_no_drift` mit aktiver `capsys`-Assertion auf NICHT-Vorkommen von "xlsx-set-mismatch" in stderr.
- **R2-LOW PROJECT_ROOT-Bindung in H2-Tests:** FIXED — beide H2-Tests `monkeypatch.setattr(validator, "PROJECT_ROOT", tmp_path)`; resolve_active_xlsx läuft jetzt sauber gegen tmp-repo statt echtes Repo.

Promotion-ready ohne R3-Loop (Memory `feedback_codex_sparring_heuristic`: PASS-WITH-NITS = ship). Carryover: keine.

**Gemini Cross-Sync (SKILL.md ↔ INSTRUKTIONEN §18):** **3 DRIFT + 5 INKONSISTENZ + 4 NIT.**

- **D1 xlsx-Tools-Count (SKILL+yaml=2 vs §18.7=3 mit Watchlist):** ACCEPTED — v0.1-Default-Set strict §18.1 (2 xlsx); Watchlist als KONTEXT-§6-Refactor-Manual-Carryover in SKILL.md + failure-recovery.md dokumentiert (Memory `feedback_watchlist_xlsx_in_sync_set` referenziert; v0.2 = PIPELINE #73c).
- **D2 yaml-`description` enthält "KONTEXT §6-Reassign" → SKILL out-of-scope:** FIXED — yaml-`description` für `score-flag-sparraten` ohne §6-Phrase + Erklärungs-Kommentar (yaml-Comment).
- **D3 yaml `session_close` Conditional in SKILL.md unsichtbar:** FIXED — SKILL.md pipeline-item-Tabellenzelle ergänzt: "(+ SESSION-HANDOVER.md bei Session-Abschluss; mid-Session optional)".
- **I3 G-03 §18.6-Roll-over 5-File-Sync-Set Hinweis fehlt:** FIXED — failure-recovery.md G-03-Zeile ergänzt.
- **I4 sub-tool-coupling.md Cross-Ref §25.5:** FIXED — Heading-Annotation "(SSoT: INSTRUKTIONEN §25.5)" + Wortlaut-Ergänzung im session-closure-Bullet.
- **I1/I5 + Nits:** I1 = kein echter Drift (CR-Konsistenz); I5 = OK Wortlaut; Nit-Carryover (TTL-Skill-spezifisch + 14-Tage-Karenz-Fenster) angegangen in SKILL.md "(Skill-spezifisch, nicht §18-Doktrin)"-Annotation + failure-recovery.md Karenz-Phrase entfernt.
- **I2 (Begriffs-Drift Bundle vs Set):** PARTIAL — primäre Stellen auf "Expected-Set" / "File-Set" / "§18-File-Set" konsolidiert (SKILL.md description + Trigger-Tabellen-Spalten-Header + P6-Bullet); residuale "Bundle"-Erwähnungen bewusst behalten wo §18-Doktrin-Doppelbedeutung trägt.

**CodeRabbit (WSL Ubuntu, `coderabbit review -t all --base-commit 6f9fd32`):** **2 Findings (1 Major + 1 Minor), beide OUTSIDE para18_sync-Scope** (pre-existing: `02_Analysen/_insider_scans/MSFT_2026-05-14.json` log/JSON-Mix + `03_Tools/briefing-sync-check.ps1:23` hardcoded path). Keine para18_sync-spezifischen Findings — Build clean.

**skill-creator-Gegencheck:** **1 MED + 3 LOW.**

- **MED-1 Description nicht "pushy" genug für Triggering-Accuracy:** FIXED — SKILL.md `description` um Trigger-Phrasen erweitert ("verify §18", "Sync-Pflicht-Bundle", "Pre-Commit-Bundle-Verify", File-Touch-Kontexte).
- **LOW-1 Non-Standard YAML-Felder (`version`, `event_types`):** ACCEPTED (Project-Internal-Metadaten nützlich, backwards-compatible).
- **LOW-2 Imperativ-Form:** ACCEPTED (User-Doku-Stil, nicht blockierend).
- **LOW-3 Trigger-Section nur literal `!ParaSync18`:** RESOLVED via MED-1 Description-Push.

---

## Dogfood-Test — 2026-05-23 (Task 17, gegen Live-State ROOT)

Live-Run (Working-Dir = `C:\Users\tobia\OneDrive\Desktop\Claude Stuff`, branch `main`, post-commit f096600):

- **Test 1** (`pipeline-item --dry-run`): **exit=0**, Verdict=**PASS**. Expected-Set: PIPELINE.md + log.md, `xlsx_warnings=[]`, `quarterly_rollover_warn=false`.
- **Test 2** (`critical-alert` NO-OP-PASS): **exit=0**, Verdict=**PASS**. JSON: `verdict=PASS, phase=P7, no_op_pass=true, expected_files=["00_Core/STATE.md"]`.
- **Test 3** (`score-flag-sparraten --no-flag-event --ticker V --dry-run`): **exit=1**, Verdict=**PASS** (legitime P1-FAIL — `score_history.jsonl` HEAD nicht heute, kein `!Analysiere`-Lauf gelaufen seit 04.05.). Klarer Recovery-Hint im stderr. Kein Traceback.
- **Test 4** (`score-flag-sparraten --also pipeline-item --no-flag-event --ticker V --dry-run`): **exit=1**, Verdict=**PASS** (gleicher legitime P1-FAIL wie Test 3, Multi-Event-Union-Pfad). Kein Traceback.
- **Verdict gesamt:** **4/4 PASS** (≥3/4-Schwelle erreicht; alle Exit-Codes deterministisch, Recovery-Hints aussagekräftig, keine Crashes). v0.1.0 Dogfood-Acceptance ✅ erfüllt.
