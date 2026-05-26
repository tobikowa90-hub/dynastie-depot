# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Status-Banner (Sliding-Window — letzte 2 Sessions; volle Historie → `05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md` + git log + Vault `log.md`):**
- **Datum:** 2026-05-26 (Mo) ~18:30 Europe/Berlin — **✅ SYSTEM.md Slim-Refactor Welle 1 + Welle 2 (Migration B) DONE (System-Zustand-Event, scoring-neutral, 2 Commits `a4323ef` + `537cf13`).** Welle 1: 6 Strips Hard-Obsolete (Briefing v3.0.6 Phase-3.5-Narrative + Open-Backlog-21.04. 8 Items + 6-Paper-Ingest-Doppel + Plugin-Substrate-Deep-Sweep 13.05. + core-slim-refactor Mega-Bullet → 1-Zeile + Footer-Mega-Changelog), ~7700 Wörter Doku-Bloat raus, alle Lessons in kanonischen SSoT (failure_modes.md / §13 / git log / Memory). Migrate-before-Strip-Disziplin pro Schnitt: 2 stale Memory-Refs aufgedeckt (`feedback_correctness_over_runtime` + `feedback_spec_section_drift`) → OneDrive-Path → Code-Path migriert; Memory-Fork-Issue persistiert als `reference_memory_fork_onedrive_vs_code_path.md`. Welle 2: 1 Migrate (Allokation 65/30/5 → PORTFOLIO.md) + 5 Strips (Live-Verify 5/11 / Backtest-Ready 27-Records / Track-5-Pläne / KG-Roadmap / claude-mem Context-Tuning 17.05.); Block-für-Block-Empirie-Check (Forward-Gates in PIPELINE L102/L105 + #58 + #60 verifiziert, score_history 27→35 empirisch belegt). Bilanz Welle 1+2: SYSTEM.md ~47 KB → ~30 KB (-36%), Bullet-Count System-Zustand ~20 → ~12, alle operativen Gates erhalten. Footer v1.13 → v1.14. **Welle 3 + Memory-Fork pending — siehe Mini-Task unten.**
- **Datum:** 2026-05-26 (Mo) ~14:30 Europe/Berlin — **✅ SESSION-HANDOVER Slim-Refactor DONE + xlsx-smoke-test-runner Description-Optimization-Loop RE-DEFERRED (System-Event + Mini-Task-Re-Defer, scoring-neutral).** (a) Slim-Refactor: 13 Status-Banner → 2 Sliding-Window-Banner, Resume-Anweisung-Frankenstein (Phase-0b 5/16 + #73a Tasks 13-18 5/22, beides DONE) → Cold-Start-Stub, Phase-0a Tasks 0-6 In-Session-Detail → Archiv, ~50 KB Working-Tree-Bloat raus. Snapshot durable in `05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md`. (b) xlsx-smoke-test-runner Description-Optimization: 20 User-validierte Eval-Queries gedraftet (10/10 Split, §C/D/Cell-Format-Boundary covered), `python -m scripts.run_loop` crasht auf Windows-Nativ-Python (run_eval.py:108 `select.select` auf Pipe-Handle → WinError 10038 + cp1252-UnicodeEncodeError). Re-Defer mit 4 klaren Re-Trigger-Schwellen statt WSL2-Setup/Patch (Description ist <24h alt + frisch Codex-validiert, zero Real-World-Empirie). Substrate `01_Skills/xlsx-smoke-test-runner-workspace/desc-opt-iteration-1/eval_set.json` lokal erhalten. Neue Memory `reference_skill_creator_windows_pipe_incompat`. Commits: e2fb3d9 (Re-Defer) + heutiger Slim-Refactor-Commit.

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

## 📌 Mini-Task: SYSTEM.md Slim-Refactor Welle 3 (Slim C) — READY für nächste Session

**Status:** Vorbereitet 2026-05-26 ~18:30 GMT+2 nach Welle 2 Commit `537cf13`. Spec-Substanz unten + Memory-Fork als optionale Stretch.

**Was Welle 3 angeht:** Sub-Section-Bloat in 4 Sektionen unterhalb `## System-Zustand`. Aktueller SYSTEM.md-Stand: 117 Zeilen / ~30 KB. Ziel End-State Welle 3: ~10-12 KB (Welle 1+2 hat schon 47 → 30 KB gemacht).

**Welle-3-Targets (Reihenfolge nach Effort/Reward absteigend):**

1. **§Passive Read-Only Data Layer (L57-86, ~30 Zeilen, größter Single-Block):** FinnHub Build-Phase-DONE-Narrative + Deliverables-Liste (6 Files) + Acceptance-Status (A1-A12 alle PASS) + Step-4a-Decision + v0.2-Roadmap. Substanz lebt in `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` + `03_Tools/finnhub_health.json` + Commit-Trail. Target-Form: 1 Bullet Live-State („FinnHub v0.1 BUILD-DONE 2026-05-22, Shadow-Run aktiv seit 23.05., Reklassifizierungs-Gate-Deadline 2026-07-06, alle 12 Acceptance PASS, Health-Status `03_Tools/finnhub_health.json`") + Pflege-Regel-Bullet bleibt unverändert. **Strip-Estimate:** ~25 Zeilen raus.

2. **§Briefing-Status (L102-117, ~16 Zeilen):** Probe-Trigger + Prod-Trigger + Architektur + Tavily-Connector-Resolved + Allow-List-Regex + Cloud-AIDefence-Decision + v2.1-Rollback + API-Empirie + sec-edgar-Deployment-Touchpoint. Live-Operativ: Prod v3.2.0 LIVE seit 11.05. + Allow-List-Regex normativ + FAIL-OPEN-Pfad. Historisch (>30 Tage Recovery-Window): v2.1-Rollback-Backup-Pfad / Connector-Recreation-Incident 07.05. / Manual-Run-Verify-Detail 11.05. → strip. Target-Form: 3-4 Bullets mit Trigger-IDs + Allow-List-Regex + FAIL-OPEN-Klausel + sec-edgar-Skip-Pointer. Memory `feedback_tavily_connector_uuid_rotation` + `feedback_remote_trigger_shallow_partial_update` halten den Incident-Lesson. **Strip-Estimate:** ~12 Zeilen raus.

3. **§Earnings-Calendar-Status (L88-100, ~13 Zeilen):** Tool-Existenz + Aufruf + Erstlauf 30.04. + Stufenplan + Stufe-2-Coverage + Stufe-2-Trigger-Mechanik + Limits Stufe-1. Live-Operativ: Tool `03_Tools/earnings_calendar.py` + Aufruf + Override-YAML + Hook in `briefing-sync-check.ps1`. Historisch: Erstlauf-Drift 30.04. + Stufenplan-Wave-1/2-Narrative + Spec-Pointer. Target-Form: 2-3 Bullets (Tool + Aufruf + Stufe-2-deployed + Limits-Pointer). **Strip-Estimate:** ~6-8 Zeilen raus.

4. **§Plugin-Layer (L46-55, ~10 Zeilen):** Substrate-Liste + Hybrid-Final-State + obsidian-skills. Hybrid-Final-State-Paragraph (~6 Zeilen) ist normativ (autoMemory = SSoT, claude-mem = additiv, Bun-Invariante, Memory-Guard-Rail) → behalten. Historie (claude-mem doku-drift 13.05. + Phase-0b-Tiefendiagnose-Narrative) → strip-eligibel. obsidian-skills 16.05. Detail → 1-Zeile-Registry. **Strip-Estimate:** ~4-5 Zeilen raus.

**§18-Sync-Impact (system-zustand-Event, scoring-neutral):** SYSTEM.md (Footer v1.14 → v1.15) + Vault log.md. Cross-Ref-Verify pflicht: vor jedem Strip `grep -nE "<keyword>" 00_Core/ 07_Obsidian Vault/.../WIKI-SCHEMA.md` für gebrochene Cross-Refs (Welle-2-Disziplin).

**Empfehlung Reihenfolge:** Block 1 (Passive Read-Only Data Layer) zuerst — größter Strip, sauberste Substanz-Persistenz (Spec-File + health.json + Commit). Dann 2 + 3 + 4. Block-für-Block-Empirie-Check vor jedem Strip wie Welle 2.

**Aufwand:** ~30-45 min für alle 4 Blocks + Footer-Update + 1 Commit + Push.

---

## 📌 Mini-Task: Memory-Fork-Konsolidierung — OPTIONAL Stretch-Goal post-Welle-3

**Status:** Deferred bis post-Welle-3 (Welle-3 ist Voraussetzung, weil Welle-3 möglicherweise weitere stale Memory-Refs aufdecken kann die migriert werden müssen).

**Vollständige Spec:** `~/.claude/projects/C--Users-tobia-Code/memory/reference_memory_fork_onedrive_vs_code_path.md` (4-Schritte-Plan unter "How to apply").

**TL;DR:**
- Diff beider Memory-Ordner: `~/.claude/projects/C--Users-tobia-Code/memory/` (aktiv, 52 Files) vs `~/.claude/projects/C--Users-tobia-OneDrive-Desktop-Claude-Stuff/memory/` (unsichtbar, 43 Files; ~12 unique mit echtem Inhalt).
- Für jeden OneDrive-only-File: Inhalt-Check → kopieren ODER verwerfen (stale).
- MEMORY.md-Index pro migriertem File ergänzen (Marker „migriert YYYY-MM-DD aus OneDrive-Path-Memory-Fork").
- OneDrive-Path-Memory archivieren in `05_Archiv/memory-fork-onedrive-archiv-YYYY-MM-DD/`.
- Optional: claude-mem-Config prüfen warum Working-Dir-Match nicht greift (Memory `feedback_cwd_namespace_discipline` existiert im OneDrive-Path — Selbstreferenz?).

**§18-Sync-Impact:** KEIN — Memory-Files leben außerhalb des git-Repos. Reiner Working-Tree-State-Refactor.

**Aufwand:** ~30-60 min je nach Inhalt-Check-Tiefe. Wenn nach Welle 3 keine Luft mehr: separater Slot.

**Re-Activation-Trigger:** post-Welle-3-Completion ODER User-Direktive „Memory-Fork angehen" ODER nächstes stale-Memory-Ref-Surface-Event in 00_Core/-Audit.

---

## 🔖 Vorgänger-Historie

Vollständige Banner-Historie + Phase-0a/0b-Detail + Phase-D-1-Final-Closure 09.05. + Konsolidierungstag-Wave-1/2/3/4 + Cluster-A-#31/#32/#33/#34 + Wiki-Modus-#54 + AVGO/MSFT/V/BRK.B/APH-Vollanalysen → **`05_Archiv/SESSION-HANDOVER-bis-2026-05-25.md` + git log + STATE.md Critical-Alerts (≤10-Tage-Window) + CORE-MEMORY.md §13 (System-Lifecycle) + Vault `log.md` + `archive/log/` (vollständige History; quartalsweise Roll-over per INSTRUKTIONEN §18.6, Initial-Cut 10.05.2026)**.

**Skill-Versions-Stempel:** dynastie-depot v3.7.6 (SKILL §410 + §27.7-Anti-Buyback-Cross-Reference + Bull-DCF-Source-Pflicht + ATH-Distance-Boundaries; keine Versions-Bump bei Confidence-Upgrade-Pass — nur Begründungs-Härtung). User-Manual-Step bei Skill-Edits: `06_Skills-Pakete/dynastie-depot_v3.7.6.zip` neu deployen + Desktop-App-Install.
