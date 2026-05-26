# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner (Sliding-Window — letzte 2 Sessions; volle Historie → `05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md` + git log + Vault `log.md`):**
- **Datum:** 2026-05-26 (Mo) ~14:30 Europe/Berlin — **✅ SESSION-HANDOVER Slim-Refactor DONE + xlsx-smoke-test-runner Description-Optimization-Loop RE-DEFERRED (System-Event + Mini-Task-Re-Defer, scoring-neutral).** (a) Slim-Refactor: 13 Status-Banner → 2 Sliding-Window-Banner, Resume-Anweisung-Frankenstein (Phase-0b 5/16 + #73a Tasks 13-18 5/22, beides DONE) → Cold-Start-Stub, Phase-0a Tasks 0-6 In-Session-Detail → Archiv, ~50 KB Working-Tree-Bloat raus. Snapshot durable in `05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md`. (b) xlsx-smoke-test-runner Description-Optimization: 20 User-validierte Eval-Queries gedraftet (10/10 Split, §C/D/Cell-Format-Boundary covered), `python -m scripts.run_loop` crasht auf Windows-Nativ-Python (run_eval.py:108 `select.select` auf Pipe-Handle → WinError 10038 + cp1252-UnicodeEncodeError). Re-Defer mit 4 klaren Re-Trigger-Schwellen statt WSL2-Setup/Patch (Description ist <24h alt + frisch Codex-validiert, zero Real-World-Empirie). Substrate `01_Skills/xlsx-smoke-test-runner-workspace/desc-opt-iteration-1/eval_set.json` lokal erhalten. Neue Memory `reference_skill_creator_windows_pipe_incompat`. Commits: e2fb3d9 (Re-Defer) + heutiger Slim-Refactor-Commit.
- **Datum:** 2026-05-24 (So) ~17:00 Europe/Berlin — **✅ PIPELINE #81 v0.2.0 SPEC-LOCKED v0.5 post-Codex-Sparring-4-Runden 96% Confidence (Pipeline-Item-Event, scoring-neutral, Karpathy 2-Phase Spec-Phase DONE).** core-slim-refactor v0.2.0 Spec-Lock erreicht nach 4 Codex-Sparring-Runden (HIGH/MEDIUM-Befunde alle adoptiert), 92 Tests passed + 2 skipped, BUILD-Phase pending in eigener Session. Details + Build-Trail → git log + `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-spec.md` + Vault `log.md`.

## 🎯 Resume-Anweisung für nächste Session

**Cold-Start:** Keine fixed Track-Empfehlung. Live-Forward-Tracks sind ausschließlich `00_Core/PIPELINE.md` offene Items (numbered list, Status-Felder normativ) und die unten stehende `📅 Nächste reguläre Termine`-Tabelle. Falls Resume mit konkretem `!`-Trigger oder Klasse-B-Earnings-Slot: Routing-Table in `CLAUDE.md` ist verbindlich.

**Wichtig — Re-Investigation-Recall-Check (Memory `feedback_pre_investigation_recall_check`):** Vor mehrschrittiger Diagnose immer EIN `mem-search`/PIPELINE-Live-Grep-Pass; veraltete Handover-Banner waren am 2026-05-26 nachweislich Quelle eines #73a-Misroutings, deswegen ist Live-State immer Ground-Truth, nie Handover-Snapshot allein.

### 📅 Nächste reguläre Termine (chronologisch)

| Datum | Item | Aktion |
|-------|------|--------|
| **27.05.** | VEEV Q1 FY27 | Klasse-B Earnings (yfinance-Pull 30.04. confirmed) — Tag 0 earnings-recap + FLAG-Quick-Check, Tag +1 Vollanalyse (§19.1) |
| **28.05.** | COST Q3 FY26 | Klasse-B Earnings (Membership-Yield-Watch) — gleiche §19.1-Discipline |

### 📋 Pending offene Slots (kein fester Termin)

- **PIPELINE #42.3** G3 3-Felder-Konsistenz-Check Tooling — Phase-2a-Slot
- **PIPELINE #48** Codebase-Defect-Pattern-Audit (~7-10h, eigene Session) — taxonomische Pattern-Map über `03_Tools/` + `01_Skills/`-SKILL.md-Logic
- **PIPELINE #52** Quick-Screener-Refresh deferred bis Use-Case-Trigger
- **PIPELINE #53** ✅ Decision-C USER-APPROVED 10.05. — Weiter beobachten + Re-Audit ~09.07.2026 mit Use-Case-Count-Tracking (Memory `project_trigger_landscape_audit_2026-05`)
- **PIPELINE #81** core-slim-refactor v0.2.0 BUILD-Phase (Spec-Lock erreicht 5/24, BUILD pending eigene Session)

### 🔬 Phase-D-Restbestand (deferred per Cluster-Trigger)

- **Phase-D-2 active-deferred-D2 Cluster:** EP-2013 + EKP-2020 → V Q3 FY26 ROIC-Methodology-Verify ~Ende Juli (PIPELINE #21)
- **Phase-D-2 meta-gate-deferred-D2:** BS-2015 → 2028-Review-Gate ODER nächste DEFCON-Block-Re-Gewichtung
- **Phase-D-3 source-only-deferred-D3:** CPZ-2019 → 2028-Review-Gate Backtest-Validation-Wave
- **Phase-D Reject-Inventarisiert:** BPZ-2023 → Latent für 2028-Review-Gate Backtest-Methodology-Roadmap

## 📌 Mini-Task: xlsx-smoke-test-runner Description-Optimization-Loop — RE-DEFERRED 2026-05-26

**Status:** Re-Deferred (User-Entscheidung 2026-05-26 ~13:50 GMT+2). Pain-grounded Trigger statt Polish-Tier-Spec.

**Was passiert ist (2026-05-26 13:40-13:50 GMT+2):**
1. 20 Trigger-Eval-Queries gedraftet (10/10 Split), HTML-Review via `assets/eval_review.html` durchlaufen, User hat 3 Tweaks bestätigt (#9 schärfen, #16 → Cell-Existence-§C/D-Boundary, #20 → Cell-Number-Format-§Out-of-Scope-Boundary).
2. `eval_set.json` exportiert + ins Workspace kopiert (`01_Skills/xlsx-smoke-test-runner-workspace/desc-opt-iteration-1/eval_set.json`, 20 Queries, 10 positive).
3. `python -m scripts.run_loop` gestartet → **sofortiger Crash** mit `WinError 10038` (alle 8 Parallel-Worker-Subprocess-Calls failen) + `UnicodeEncodeError cp1252 ✗`.

**Blocker (durable diagnostiziert):**
- **Root-Cause:** `skill-creator/scripts/run_eval.py:108` benutzt `select.select([process.stdout], ...)` — auf Windows funktioniert `select.select` ausschließlich mit Socket-Handles, nicht mit Pipe-Handles. Fundamentale Plattform-Inkompatibilität (Python-Doku: "On Windows, the underlying select() function is provided by the WinSock library, and does not handle file descriptors that don't originate from WinSock").
- **Sekundär:** `run_loop.py:151/278/317/321` schreibt HTML via `.write_text(generate_html(...))` ohne `encoding='utf-8'` → cp1252-Crash bei UTF-8-Symbolen (✗/✓). Klassische Memory-Anker `feedback_windows_console_ascii_safe_inline_python`.
- **Konsequenz:** Description-Optimization-Loop ist auf Windows-Nativ-Python NICHT lauffähig. Brauchbar nur via WSL2-Ubuntu (~60-90min Setup: Plugin-Cache + OneDrive-Workspace WSL-side mounten) ODER lokalem Plugin-Patch (~30-45min, Risiko: Upstream-Drift bei Plugin-Update).

**Begründung Re-Defer (statt WSL/Patch):**
- Description ist frisch empirie-validiert (Commit `aab66f4` post-Codex 2026-05-26 ~00:47): 0 HIGH/MEDIUM/LOW Findings open; literal-Scope §A/§B/§E/§G in / §C/§D/Cell-Format out korrekt abgebildet.
- Zero Real-World-Empirie bisher (Skill <24h alt, 0 Live-Trigger-Events) — kein konkretes Drift-Signal das WSL/Patch-Aufwand rechtfertigt.
- Polish-Tier per ursprünglicher Pickup-Spec, kein Blocker für offene PIPELINE-Items oder reguläre Termine.
- Memory-Anker `feedback_redefer_over_prespec_dynastie` (24.05.2026): bei <2 Real-Runs + Infrastruktur-Pain → Re-Defer mit pain-grounded Trigger ist nominaler Pfad.

**Re-Trigger-Schwellen (klar verifizierbar):**
1. **Untrigger-Drift:** ≥1 dokumentierter Real-World-Case wo User ein `openpyxl`-Live-Tool-Mutation macht UND Skill silent bleibt (Detection via Pre-Commit-Hook-Block oder downstream-Audit-Fail) → konkretes Pain-Signal.
2. **Overtrigger-Drift:** ≥1 Case wo Skill triggert bei klarem Non-Smoke-Kontext (z.B. Markdown-Edit, `!`-Routing-Trigger) und User-Override braucht.
3. **Description-Mutation-Anlass:** SKILL.md description wird aus anderem Grund substantiell editiert (Scope-Expansion §C/§D inkl., neues 4. Live-Tool, etc.) → Optimization-Loop wird auf neuer Description-Baseline sinnvoll.
4. **Tooling-Fix:** skill-creator-Plugin patched select-Issue upstream ODER WSL2-Dynastie-Bridge wird für anderen Use-Case aufgesetzt (sunk-cost-Argument).

**Durables Substrate (für nächsten Pickup, falls Re-Trigger hits):**
- Eval-Set: `01_Skills/xlsx-smoke-test-runner-workspace/desc-opt-iteration-1/eval_set.json` (20 Queries, 10/10 Split, User-validiert + bewusst editiert; SKILL-Description-Contract-aligned — §C/D/Cell-Format Out-of-Scope-Boundaries explizit covered).
- Draft-JSON: gleiches Verzeichnis `trigger-eval-draft.json` (Vorstufe vor User-Review).
- Workspace-Verzeichnis bleibt erhalten unter `01_Skills/xlsx-smoke-test-runner-workspace/` (gitignored per `.gitignore` Pattern `01_Skills/*-workspace/`, lokal-only — Skill-Creator-Convention, kein §18-Substrate).

**Memory-Anker (neu + reused):**
- NEU: `reference_skill_creator_windows_pipe_incompat` (run_eval.py select.select Pipe-Trap, Line 108, mit Fix-Pfaden).
- Reused: `feedback_skill_name_is_scope_contract` · `feedback_brainstorming_terminal_override_dynastie` · `feedback_codex_default_english_in_dynastie` · `feedback_redefer_over_prespec_dynastie` · `feedback_windows_console_ascii_safe_inline_python` · `feedback_pre_investigation_recall_check`.

**§18-Sync-Impact:** Keiner. SESSION-HANDOVER.md ist working-tree-only, außerhalb §18-Trigger-Set. Reiner doc-Commit ohne Sync-Wave.

**Out-of-Scope (war + bleibt):** Kein Code-Change am Skill, kein Hook-Behavior-Change, kein Version-Bump.

---

## 🔖 Vorgänger-Historie

Vollständige Banner-Historie + Phase-0a/0b-Detail + Phase-D-1-Final-Closure 09.05. + Konsolidierungstag-Wave-1/2/3/4 + Cluster-A-#31/#32/#33/#34 + Wiki-Modus-#54 + AVGO/MSFT/V/BRK.B/APH-Vollanalysen → **`05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md` + git log + STATE.md Critical-Alerts (≤10-Tage-Window) + CORE-MEMORY.md §13 (System-Lifecycle) + Vault `log.md` + `archive/log/` (vollständige History; quartalsweise Roll-over per INSTRUKTIONEN §18.6, Initial-Cut 10.05.2026)**.

**Skill-Versions-Stempel:** dynastie-depot v3.7.6 (SKILL §410 + §27.7-Anti-Buyback-Cross-Reference + Bull-DCF-Source-Pflicht + ATH-Distance-Boundaries; keine Versions-Bump bei Confidence-Upgrade-Pass — nur Begründungs-Härtung). User-Manual-Step bei Skill-Edits: `06_Skills-Pakete/dynastie-depot_v3.7.6.zip` neu deployen + Desktop-App-Install.
