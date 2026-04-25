# 🔁 Session-Übergabeprompt — Dynastie-Depot

## Verweise
- [STATE.md](STATE.md) — Hub
- [PORTFOLIO.md](PORTFOLIO.md) — aktueller Portfolio-State
- [PIPELINE.md](PIPELINE.md) — offene Pläne bei Session-Abschluss
- [SYSTEM.md](SYSTEM.md) — Infra-Kontext
- [CORE-MEMORY.md §12](CORE-MEMORY.md#12-per-ticker-chronik) — Per-Ticker-Historie bei Ticker-Sessions

**Aktualisiert:** 2026-04-25 Session-6-Ende — **00_Core Perfect-Organization Tier 2: Tasks 7+8 CLOSED (inkl. Narrative-Drift-Fix).** Feature-Branch `refactor/00core-perfect-organization`, 3 neue atomare Commits seit Task-6-`9cce107`:
- `f66b622` Task-7 Skill-Paket-Build — ZIPs physisch gebaut (`dynastie-depot_v3.7.3.zip` 57,6 KB + `backtest-ready-forward-verify.zip` 10,8 KB v1.0.1-Frontmatter verifiziert via SHA256+Entries), `v3.7.2.zip` → `05_Archiv/skills-legacy/` archiviert. **User-Pause-Punkt 7.5 erfolgt**, manuelle Desktop-Installation durch User bestätigt, Post-Install-Smoke 6/6 PASS. Commit-Scope: nur `skills-legacy/README.md` force-added (ZIPs bleiben gitignored Build-Artefakte, User löschte Trail-Kopie manuell). AC #7 ✓ + AC #8 ✓.
- `0e45989` Task-8-Narratives-Drift-Fix — Codex-Review entdeckte 2 🔴 Blocker (F1 CORE-MEMORY §3/§4/§5/§9: 5 Stellen, F2 KONTEXT §11 Projection-Layer: 5 Stellen). 9 Drift-Pointer STATE.md → PORTFOLIO.md / 4-file-arch nachgezogen. KONTEXT v1.1→v1.2. Allowed: L405 CORE-MEMORY historisch (18.04. pre-Hub-Split korrekt at write-time); morning-briefing-prompt-v2.md Changelog.
- `7ee1b61` Task-8 Smoke-Sweep + Artefakt-Gate — minimal-baseline 3/3 PASS (AC #9), --core 5/8→6/8 PASS (AC #10, Check-3 FAIL→PASS via Task-4 Fixture-Fix, keine PASS→FAIL-Transitions), Skill-Smoke 6/6 PASS (AC #11), Scoring-Neutralität (AC #18) verifiziert (jsonl+config.yaml unverändert, DEFCON v3.7 persistent; 2 v3.8-Treffer beide False-Positive). PIPELINE.md #13 Vault-Sanierung als Deferred-Follow-up eingehängt (AC #17 ✓). Last-Audit-Block aktualisiert (AC #16c ✓). 4 Artefakte force-added in `docs/superpowers/specs/_artifacts/`.

Codex-Verdikt Task-8 Step 8.6: `RECONCILED_WITH_FOLLOWUPS` → F1+F2 durch `0e45989` closed. AC-Matrix Stand Session-6-Ende: **#1-#6 PASS** (Tasks 2/3), **#7-#8 PASS** (Task 7), **#9-#11 PASS** (Task 4 + Smoke), **#12-#13 PASS** (Task 6), **#14-#15 PASS** (Task 8 Reconcile+Lint), **#16c PASS** (Last-Audit), **#17 PASS** (Vault-FU), **#18 PASS** (Scoring-Neutralität). **OPEN (Task 9 Scope): #16a (Codex formal), #16b (CodeRabbit), #16-User-Sign-off, #16d Merge-Dokumentation.**

**Portfolio-State unverändert** seit 23.04. TMO Q1 (Score 67/D3/33,53€/Nenner 8,5). System: DEFCON v3.7 (unverändert).

**Working-Tree (uncommitted, runtime/autosave):** `03_Tools/Rebalancing_Tool_v3.4.xlsx` (Excel-Autosave), `.claude/scheduled_tasks.lock`, `.claude/worktrees/`. Kein Task-Scope.

## 🔄 RESUME-INPUT (Session 7 — Task 9 Review-Gates + Merge, 2026-04-25 Session-6-Ende)

**Auftrag:** Plan `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md` ab **Task 9 Step 9.1** via `superpowers:executing-plans` fortsetzen. Branch `refactor/00core-perfect-organization` bleibt checked out. Tasks 0-8 sind committed; nur noch Task 9 (Review-Gates) + Merge laut Spec.

**Task 9 Steps Session 7 (~45-75 Min, harter User-Pause-Punkt 9.7):**
1. **Step 9.1:** Claude Self-Review Checklist — AC #1-#18 durchgehen, bereits dokumentierte PASS aus Handover-Banner übernehmen, noch OPEN prüfen (#16a/b/Sign-off/Merge-Doku).
2. **Step 9.2:** Codex-Reconciliation formal via `codex:codex-rescue`-Subagent gegen vollen `main..HEAD`-Diff (9 Commits seit baseline `db50ff0`). Prompt per Plan-Template.
3. **Step 9.3:** Codex-Output speichern als `docs/superpowers/specs/_artifacts/codex-reconciliation-report.md` (force-add).
4. **Step 9.4:** Codex-Findings adressieren. 🔴 Blocker sofort fixen als einzelne Commits `fix(refactor): Codex-F<N>…`. 🟡 Should inline oder Deferred. ℹ️ Nice dokumentieren.
5. **Step 9.5:** CodeRabbit-Pass via WSL, `--base-commit` statt `--base` (Auto-Memory `coderabbit_cli_via_wsl.md` kanonisch). Base = letzter main-Commit vor 2026-04-24 (wahrscheinlich `db50ff0`).
6. **Step 9.6:** CodeRabbit-Findings triagieren → `coderabbit-findings.md` (Fix/Decline + Rationale). Fixes als separate Commits.
7. **🛑 Step 9.7 USER-PAUSE:** User-Sign-off einholen (Plan-Zitat: „STOP until user approval or decline is received"). Sign-off-Artefakt `user-signoff.md` anlegen.
8. **Step 9.8-9.10 (nach User-OK):** Merge nach `main` via `--no-ff`, Tag-Commit optional, `!SyncBriefing` nach Merge.

**AC-Bezug:** AC #16a (Claude Self) · #16b (Codex/CR via Artefakte) · #16c bereits ✓ · #16d Merge-Dokumentation.

**Sequenz Session 7:**
1. `Session starten` → STATE.md (Hub, default-load) + PORTFOLIO.md (Live-State, default-load)
2. SESSION-HANDOVER.md (diese Datei) — Resume-Input Session 7
3. Step 9.1 Claude Self-Review (AC-Matrix aus Handover-Banner als Ausgangspunkt)
4. Step 9.2 Codex-Subagent dispatch (codex:codex-rescue)
5. Codex-Findings adressieren (9.3+9.4)
6. Step 9.5 CodeRabbit-Pass (WSL, base-commit=merge-base-main-HEAD)
7. Step 9.6 CR-Triage
8. 🛑 USER-PAUSE 9.7 → Sign-off
9. Post-Sign-off: Merge + !SyncBriefing

**Codex-Preview (Task 8 Step 8.6):** Bereits `RECONCILED_WITH_FOLLOWUPS` für Tasks 0-7 + Drift-Fix. Task 9 Step 9.2 Full-Pass wird vermutlich `RECONCILED` zurückgeben (F1+F2 gefixt), eventuell neue kleinere Findings.

**Bekannte offene Codex-Followups (pre-Task-9, kein Blocker):**
- `03_Tools/backtest-ready/README.md:130` v3.7.2-Skill-Orchestrierung → v3.7.3 (Doku-Drift, harmlos)
- `03_Tools/system_audit/_smoke_test.py:450-471,505-507` Test-/Fixture-Naming `state_*` → `portfolio/pipeline` (kosmetische Hygiene, Codex F3 Task 4)
- briefing-sync-check.ps1 — Codex-False-Positive (STATE.md intentional als Hub für Critical-Alert-Sync)

**Known Pre-Existing FAIL in --core (Task-8-Diff, nicht Task-9-Scope):**
- Check-4 `cross_source` FAIL 20/22: `PORTFOLIO.md: TMO score=64` vs `config.yaml=67` — config.yaml nicht synchronisiert nach TMO Q1 23.04. (Task-6-Scope laut Handover, aber im Commit nicht addressiert → weiter Backlog).
- Check-5 `existence` FAIL 203/455: stale path-refs in CLAUDE.md/SESSION-HANDOVER/Plan-Files. Task-6-"existence-Cleanup-Welle" nicht ausgeführt. Pre-existing, durch Task-4 Scan-Erweiterung nur sichtbarer geworden.

**Spec-Anker:** `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` v0.4 ratified.

**Push-Status:** 9 Commits LOKAL auf Feature-Branch seit baseline `db50ff0` (7 Task-Commits + Task-8 Artefakt-Commit + Narrative-Drift-Fix). Kein `git push`. `!SyncBriefing` deferred bis Branch-Merge in main (Task 9.8-9.10).

**Branch-Status nach Session 6:**
```
7ee1b61 verify(refactor): Task-8 Smoke-Sweep + Artefakt-Gate
0e45989 refactor(narratives): post-migration drift-fix CORE-MEMORY §3 + KONTEXT §Layer
f66b622 build(skills): Task-7 Skill-Paket-Build — Legacy-Archive README-Entry
9cce107 refactor(governance): Task-6 CLAUDE.md + INSTRUKTIONEN §18/§25/§27.3/§27.4
a404012 refactor(skills+peers): Task-5 Content-Patches + Peer-Verweise-Header
469f5af refactor(scripts): Task-4 Tool-Patches für 00_Core-Split
60b2882 handover: Session-3-Ende — Task-3 CORE-MEMORY closed, Task-4 Resume-Input
326fa42 refactor(00core): Task-3 CORE-MEMORY §1→§12/§13 Topic-Auflösung
db50ff0 (main, baseline merge-base)
```

---

## 🗃 Vorherige Resume-Inputs (archiviert)

### Session 6 (Task 7 Skill-Paket-Build + Task 8 Verification — ARCHIVIERT 2026-04-25)

**Auftrag war:** Plan ab Task 7 Step 7.1 fortsetzen. Ergebnis: Task 7 (`f66b622`), Narrative-Drift-Fix (`0e45989` per Codex F1+F2), Task 8 (`7ee1b61`). 1 Codex-Review durchgeführt während Step 8.6 Allow/Deny-Lint = RECONCILED_WITH_FOLLOWUPS → F1+F2 fixed. AC #7/#8/#9/#10/#11/#14/#15/#16c/#17/#18 PASS. Task-7 Commit-Scope nur README force-added (ZIPs blieben gitignored Build-Artefakte per User-Entscheidung Option 2). User löschte Trail-Kopie `_1.0.1.zip` manuell.

### Session 5 (Tasks 4+5+6 Atomare Commits — ARCHIVIERT 2026-04-25)

**Auftrag:** Plan `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md` ab **Task 7 Step 7.1** via `superpowers:executing-plans` fortsetzen. Branch `refactor/00core-perfect-organization` bleibt checked out. Tasks 4+5+6 sind committed; nur noch Task 7 (Build) + Task 8+ (Governance/Audit/Merge laut Spec).

**Task 7 Steps Session 6 (~30-45 Min, harter User-Pause-Punkt 7.5):**
1. **Step 7.1:** `06_Skills-Pakete/dynastie-depot_v3.7.3.zip` bauen via `cd 01_Skills/dynastie-depot && zip -r ../../06_Skills-Pakete/dynastie-depot_v3.7.3.zip . -x "__pycache__/*" -x "*.pyc" -x ".*"`
2. **Step 7.2:** `backtest-ready-forward-verify` ZIP rebuilden (bare-name + versionierte Kopie `_1.0.1.zip` für Trail; bare-name-Konvention laut Backlog)
3. **Step 7.3:** `06_Skills-Pakete/dynastie-depot_v3.7.2.zip` → `05_Archiv/skills-legacy/` movem
4. **Step 7.4:** `05_Archiv/skills-legacy/README.md` Eintrag mit Rationale (00_Core-Refactor-Bezug, DEFCON v3.7 unverändert)
5. **🛑 Step 7.5 USER-PAUSE:** Manuelle Desktop-Installation der ZIPs durch User (`dynastie-depot_v3.7.3.zip` + `backtest-ready-forward-verify.zip`). Claude pausiert; User-Confirmation einholen
6. **Step 7.6:** Post-Install-Smoke `python 01_Skills/backtest-ready-forward-verify/_smoke_test.py` PASS
7. **Step 7.7:** Atomarer Commit ZIPs + Archive (`build(skills): Task-7 v3.7.3 + 1.0.1 ZIP-Pakete + Legacy-Archive`)

**AC-Bezug:** AC #7 (ZIP existiert, alter ZIP archiviert) · AC #8 (version 1.0.1 im Frontmatter im ZIP).

**Sequenz Session 6:**
1. `Session starten` → STATE.md (Hub, default-load) + PORTFOLIO.md (Live-State, default-load nach §6.1 CLAUDE.md v2)
2. SESSION-HANDOVER.md (diese Datei) — Resume-Input Session 6
3. Step 7.1 → 7.2 → 7.3 → 7.4 → 🛑 USER-PAUSE 7.5 → User confirmiert → 7.6 → Codex-Review (kurz, ZIPs sind Build-Artefakte) → 7.7 (Commit)
4. Optional Codex-Review pre-7.7 (oder skip wenn nur ZIP-Inhalt = bereits reviewter Source)
5. Post-Task-7 → Task 8+ je Spec: Post-Migration-Audit + Vault-Sync (`!SyncBriefing`) + Branch-Merge.

**Codex-Followups offen** (post-Task-6, post-commit, in Task 7+ oder Hygiene-Welle):
- `03_Tools/backtest-ready/README.md:130` v3.7.2-Skill-Orchestrierung → v3.7.3 (Doku-Drift, harmlos)
- `03_Tools/system_audit/_smoke_test.py:450-471,505-507` Test-/Fixture-Naming `state_*` → `portfolio/pipeline` (kosmetische Hygiene, kein Funktional-Impact, Codex F3 Task 4)
- briefing-sync-check.ps1 — Codex falsch-positiv-flagged (STATE.md ist intentional drin als Hub für Critical-Alert-Sync)

**Spec-Anker:** `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` v0.4 ratified.

**Push-Status:** 3 Commits LOKAL auf Feature-Branch. Kein `git push`. `!SyncBriefing` deferred bis Branch-Merge in main (Task 8+).

**Branch-Status nach Session 5:**
```
9cce107 refactor(governance): Task-6 CLAUDE.md + INSTRUKTIONEN §18/§25/§27.3/§27.4
a404012 refactor(skills+peers): Task-5 Content-Patches + Peer-Verweise-Header
469f5af refactor(scripts): Task-4 Tool-Patches für 00_Core-Split
60b2882 handover: Session-3-Ende — Task-3 CORE-MEMORY closed, Task-4 Resume-Input
326fa42 (baseline) refactor(00core): Task-3 CORE-MEMORY §1→§12/§13 Topic-Auflösung
```

---

## 🗃 Vorherige Resume-Inputs (archiviert)

### Session 5 (Tasks 4+5+6 Atomare Commits — ARCHIVIERT 2026-04-25)

Auftrag war: Plan ab Task 4 Step 4.12 fortsetzen. Ergebnis: Task 4 (`469f5af`) + Task 5 (`a404012`) + Task 6 (`9cce107`). 3 Codex-Reviews durchgeführt (RECONCILED_WITH_FOLLOWUPS / RECONCILED_WITH_FOLLOWUPS / CRITICAL_DRIFT→behoben). Alle 11 AC erfüllt.

### Session 4 (Task 4 Script-Patches TDD-Order — ARCHIVIERT 2026-04-25 in Session 5 Commit `469f5af`)

**Restliche Steps Session 5:**
1. **Step 4.12:** `03_Tools/briefing-sync-check.ps1` — `$CheckedFiles`-Liste um `00_Core/PORTFOLIO.md`, `00_Core/PIPELINE.md`, `00_Core/SYSTEM.md` erweitern (neben dem bereits gelisteten STATE.md). Optional Smoke via `pwsh.exe -File ... -WhatIf`.
2. **Step 4.13:** `03_Tools/backtest-ready/backfill_flags.py` — Docstring + Prose-Refs „CORE-MEMORY §1" auf §12 (Ticker-Bezug) bzw. §13 (ohne Ticker-Bezug) umleiten. §3/§4 bleiben.
3. **Step 4.14:** `03_Tools/backtest-ready/flag_event_study.py` — Output-Template „**Hintergrund (CORE-MEMORY §1):**" → „**Hintergrund (CORE-MEMORY §12):**". §3/§4 bleiben.
4. **Step 4.15:** `03_Tools/backtest-ready/backfill_scores.py` — `grep -n "CORE-MEMORY §"` prüfen; §4-Ref bleibt, §1 → §12/§13. Wahrscheinlich kein Change, nur Verification.
5. **Step 4.16:** Final Smoke-Sweep — `python 03_Tools/system_audit/_smoke_test.py`, `python 01_Skills/backtest-ready-forward-verify/_smoke_test.py`, `python 03_Tools/system_audit.py --minimal-baseline` alle rc=0.
6. **Step 4.16b (NEU, User-Request Session 4):** **Codex-Review** via `codex:rescue` / `codex:gpt-5-4-prompting`-Pattern auf den vollen Task-4-Diff (`git diff` gegen `326fa42`). Ziel: Spec-Drift-Check + Info-Loss-Check (Review-Stack v2, Memory `feedback_review_stack.md`). Codex-Findings adressieren vor Commit (Option 1: Plan-Header-Notice falls §-Referenz-Drift auftritt, Memory `feedback_spec_section_drift.md`).
7. **Step 4.17:** Atomarer Commit via Plan-Template (erweitert um Task-2-Carry-Over **Stand:**-Nachtrag):
   ```
   refactor(scripts): Task-4 Tool-Patches für 00_Core-Split
   …
   + Task-2-Carry-Over: **Stand:** 25.04.2026 in STATE/PORTFOLIO/PIPELINE/SYSTEM (Hub-Split hatte Header verloren → Check-3 FAIL)
   ```

**AC-Bezug Restdauer:** AC #9 muss nach 4.12-4.17 weiter 3/3 PASS halten · AC #11 ebenso.

**Sequenz Session 5:**
1. `Session starten` → STATE.md lesen
2. SESSION-HANDOVER.md (diese Datei) — Resume-Input Session 5
3. `git status` + `git diff --stat 326fa42..HEAD` — Session-4-Diff inspizieren
4. Step 4.12 → 4.13 → 4.14 → 4.15 → 4.16 (Smoke-Sweep) → 4.16b (Codex) → 4.17 (Commit)

**Known Pre-Existing Carry-Over (nicht Task-4-Scope, nicht in Commit):**
- `Check-4 cross_source` FAIL: `PORTFOLIO.md: TMO score=64` vs `config.yaml=67` — config.yaml nicht synchronisiert nach TMO Q1 23.04. **Task 6 Governance-Scope.**
- `Check-5 existence` FAIL: 244 stale path-refs in SESSION-HANDOVER/CLAUDE.md + `PIPELINE.md`-extrahierten Plan-Files. **Task 6 `existence-Cleanup-Welle`** löst das. Task 4 hat den FAIL durch Scan-Erweiterung nur *sichtbar* gemacht; die Drift war schon da.
- `portfolio_risk.py`, `benchmark-series.jsonl`, `03_Tools/repair_daily_persist.py` in SYSTEM.md/PIPELINE.md ohne Pfad-Prefix — Task 6 Housekeeping.

**Post-Task-4:** Task 5 Skill-Patches + Peer-Verweise (`dynastie-depot` v3.7.3, `backtest-ready-forward-verify` v1.0.1, Verweise-Köpfe in 4 Files). Task 6 CLAUDE.md + INSTRUKTIONEN §18-Rename. Task 7+ Governance, ZIP-Build, Post-Migration-Audit, Merge.

**Spec-Anker:** `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` v0.4 ratified.

**Durchgeführte Verifikationen Session 4:**
- backtest-ready-forward-verify `_smoke_test.py` 6/6 PASS (inkl. RED-Zustand 5/6 als Teil TDD-Protokoll dokumentiert)
- system_audit `_smoke_test.py` 14 Suites PASS
- `--minimal-baseline` 3/3 PASS rc=0 (mehrfach während Session)
- Check-3 markdown_header: 2/3 FAIL vor Task 4 → 6/6 PASS nach Task-2-Carry-Over-Fix

---

## 🗃 Vorherige Resume-Inputs (archiviert)

### Session 4 (Task 4 Script-Patches TDD-Order — ARCHIVIERT 2026-04-25)

**Auftrag:** Plan `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md` ab **Task 4** via `superpowers:executing-plans` fortsetzen. Branch `refactor/00core-perfect-organization` bleibt checked out.

**Task 4 Kern (TDD-Order kritisch — Tripwire-RED vor GREEN):**
1. Step 4.1-4.3: `_forward_verify_helpers.py` Tripwire STATE.md → PORTFOLIO.md — erst `_smoke_test.py`-Fixture auf PORTFOLIO-Snippet umstellen (RED), dann Helper-Code anpassen (GREEN). Beide Smoke-Runs explizit zeigen.
2. Step 4.4-4.7: `system_audit/checks/*` Pfad-Listen erweitern (pipeline_ssot → PIPELINE.md, markdown_header + existence + cross_source um PORTFOLIO/PIPELINE/SYSTEM).
3. Step 4.8: Fixtures `state_hub_ok.md` + `portfolio_ok.md` + `pipeline_ok.md` + `system_ok.md` neu anlegen (minimale Section-Anchors).
4. Step 4.9-4.11: `_smoke_test.py` + `_smoke_temp_repo.py` Content-Assertions auf Hub-Schema; `report.py` prüfen; kompletter Smoke-Sweep muss PASS.
5. Step 4.12: `briefing-sync-check.ps1` CheckedFiles-Liste um PORTFOLIO/PIPELINE/SYSTEM erweitern.
6. Step 4.13-4.15: `backfill_flags.py` + `backfill_scores.py` + `flag_event_study.py` — CORE-MEMORY §1-Refs auf §12/§13 umleiten (Ticker-Bezug → §12, kein Ticker-Bezug → §13, §3/§4 bleiben).
7. Step 4.16-4.17: Smoke-Sweep + atomarer Commit.

**AC-Bezug:** AC #9 `--minimal-baseline` 3/3 PASS muss auch nach Task 4 halten; AC #11 Skill-Smoke PASS.

**Sequenz für Session 4:**
1. `Session starten` → STATE.md (Default) lesen
2. SESSION-HANDOVER.md (diese Datei) — dieser Resume-Block
3. Plan re-lesen ab Task 4 (Zeilen 621+)
4. Step 4.1 grep auf `_forward_verify_helpers.py` STATE.md-Stellen → notieren
5. Step 4.2 RED-State fabrizieren → PASS → Step 4.3 GREEN
6. Weiter Step 4.4+ exakt Plan-Steps
7. Commit-Message pattern `refactor(scripts): Task-4 Tool-Patches für 00_Core-Split` (Plan Step 4.17 Template)

**Post-Task-4:** Task 5 Skill-Patches + 6 Peer-Verweise (dynastie-depot v3.7.3, backtest-ready-forward-verify 1.0.1, SKILL.md + Prompts + SESSION-HANDOVER/TOKEN-RULES/KONTEXT/Faktortabelle Verweise-Kopf). Task 6 CLAUDE.md + INSTRUKTIONEN §18-Rename. Task 7+ Governance, ZIP-Build, Post-Migration-Audit, Merge.

**Spec-Anker:** `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` v0.4 ratified.

**Durchgeführte Verifikationen dieser Session (Task 3):** AC #6 `grep ^## 1\.`=0, `grep ^## 9b\.`=0, `grep ^## 12\. Per-Ticker-Chronik`=1, `grep ^### 12\.`=11, `grep ^## 13\. System-Lifecycle`=1, `awk '/^## 6\./,/^## 7\./' | wc -l`=24 (≤50 PASS). `system_audit --minimal-baseline` rc=0 vor + nach Commit.

---

## 🗃 Vorherige Aktualisierungen

**2026-04-24 Session-2-Ende — CLAUDE.md Routing-Refactor Tier 1 VOLLSTÄNDIG CLOSED.**

## 🏛 STATE-Banner-Chronik (migriert aus STATE.md Header 2026-04-24)

**Single Entry Point für Session-Start** | Stand: 24.04.2026 Session-2-Ende (**CLAUDE.md Routing-Refactor Tier 1 VOLLSTÄNDIG CLOSED** — Session 1 (16 Commits) + Session 2 Vault-Update `f9d65d1` + CodeRabbit-Pass `4cf0ea9` (3 Fixes + 5 begründete Declines). CR-CLI-Command-Bug im Handover-Block als Zusatz-Fix behoben. **Session 3 offen:** Brainstorm 00_Core Perfect-Organization (STATE-Split Variante B + CORE-MEMORY Restrukturierung + Global-Linking). **Portfolio-State unverändert** seit 23.04. · vorher: 23.04.2026 Nachmittag (**Phase G TMO Q1 FY26 Vollanalyse DONE** — BEAT + Guidance-Raise. Adj EPS $5,44 / Rev $11,01B / GAAP EPS $4,43 (+11%) / FCF $825M (+121% YoY) / OCF $1.192M (+65%) / ΔWC $-1.112M vs $-1.425M. Guidance hochgesetzt: Rev $47,3-48,1B, Adj EPS $24,64-25,12, FCF $6,9-7,4B, Organic 3-4% bestätigt. Clario $8,87B closed. **`fcf_trend_neg` Resolve-Gate CLEAR** (Schema-Watch deaktiviert). Score **64→67**, **D2→D3**, Sparrate **17,81€→33,53€**, Nenner **8,0→8,5** (volle Rate 35,63€→33,53€, V D2-Rate 17,81€→16,76€). Sync-Welle 6 Files Old-Pipeline-Format committed (`620702a`) · **Retro-Audit Option B PASS (23.04. spät)** — `backtest-ready-forward-verify` P1-P4 Post-hoc-Validation sauber, kein Re-Append · XLSX-Tools (Rebalancing_Tool + Satelliten_Monitor) unberührt bis post-Retro-Migration (Vermeidung Doppel-Edit-Churn). **Fr 24.04. Konsolidierungstag-Agenda erweitert um Block 0 Teil 2: Track 5a/5b-Entscheidungspunkt**) · vorher: Phase G Pre-TMO-Briefing bereit via `02_Analysen/TMO_pre-earnings_2026-04-23.md` (earnings-preview-Skill 22.04.) · vorher: **Phase E 19/19 DONE ✅** — Tasks 15-19 committed + Fix-Welle E + CR-Re-Run gegen `e3ba381` = **1 OOS-Nitpick** (`PORTFOLIO-RISK-2026-04-17.md:39` DE/EN-Mix „Risk-Treiber", Auto-Output nicht Phase-E-Scope, dokumentiert + closed). Codex-Pass = **RECONCILED_WITH_FOLLOWUPS** (3 Codex-Follow-ups deferred: Check-3+existence-Cleanup → §27.5-Guard auf `--core` hochziehen, Check-10 Regex-Scope). Acceptance-Matrix 9/11 ✅ + 2 dokumentierte WARNs (Item 2 `--core` rc=1 Tool-Bugs, Item 9 Notation-Drift). **Phase F (Provenance-Plan) deferred per Pfad-2-Entscheidung** — TMO Q1 23.04. 14:30 CEST läuft mit Old-Pipeline im Minimal-Modus (Weekly-Limit 93%, Reset Do 22:00 CEST), Retro-Migration TMO-Record post-Reset. Phase G (TMO Q1) next. Konsolidierungstag Fr 24.04. geplant (Check-3-Fix + existence-Cleanup + v3.0.4-Briefing-Hotfix + Tavily-Key-Rotation). v3.0.4 Briefing-Hotfix weiter pending) | System: DEFCON v3.7 (unverändert)

---

**Summary:**
- Session 1: 16 Commits (Tier-1-Execution + AL v2.5 + Sync-Welle + Codex-Reconciliation + Option-B-Compression 97→71 Zeilen)
- Session 2 (heute): Vault-Update `f9d65d1` (Konstitution-Note auf 7-Section-Struktur) + CodeRabbit-Pass `4cf0ea9` (8 Findings → 3 Fixes / 5 Declines) + STATE/Handover-Close-Commits

**Acceptance:** 11/11 AC PASS (2 dokumentierte Abweichungen). Codex `RECONCILED_WITH_FOLLOWUPS` (alle 3 adressiert). CodeRabbit triage-drift-free.

**CR-Command-Bug als Zusatz-Fix:** Session-1-Handover dokumentierte `--base d025c7f`, das interpretiert `d025c7f` als Branch → CR crashte mit „339 Files > 150". Korrektur: `--base-commit d025c7f --type committed`. Auto-Memory `coderabbit_cli_via_wsl.md` war bereits korrekt — Drift nur im Handover-Block.

**Pending:**
- Session 3 (Brainstorm-Kandidat): 00_Core Perfect-Organization — Tier-2 STATE-Split Variante-B-Hub + Tier-2b CORE-MEMORY Restrukturierung + Global-Linking-Strategie. Siehe STATE.md Pipeline-Deferred #12.

**Vorherige Aktualisierungen:** 2026-04-24 Session-1-Ende — 16 Commits Tier 1 · 2026-04-24 Mobile — Brainstorm+Spec+Plan (5 Commits) · 2026-04-23 Nachmittag — Phase G (TMO Q1 DONE) · 2026-04-22 Spät — Task 19 + Fix-Welle E · 2026-04-22 Mittag — Tasks 15-18 · 2026-04-21 Nacht — Task 14 + Fix-Welle C+D.

> **Progress-Banner Tier 1:** ✅ Brainstorm (Desktop 24.04.) · ✅ Spec v0.2 (Mobile) · ✅ Plan v0.2.1 3-fach-reviewed (Mobile) · ✅ Execution (Session 1) · ✅ Sync-Welle (STATE + CORE-MEMORY) · ✅ Codex-Reconciliation · ✅ Option-B-Compression (86→71 Zeilen) · ✅ **Vault-Update-Sweep** (Session 2) · ✅ **CodeRabbit-Pass** (Session 2, 3/8 Fixes, 5 begründete Declines).

> **🔄 RESUME-INPUT (Session 3 — 00_Core Perfect-Organization Brainstorm, 2026-04-24 Session-2-Ende):**
>
> **Auftrag:** Brainstorm-Session (nicht Execution) zur Vision „perfekt organisierter + global verknüpfter `00_Core/`-Ordner". Kandidaten-Scope siehe STATE.md Pipeline-Deferred #12:
> - (a) Tier-2b CORE-MEMORY Restrukturierung (~45 §1-Einträge → Subkategorien + Verknüpfung zu adressierten System-Elementen)
> - (b) Tier-2 STATE-Split Variante-B-Hub (STATE.md ~10-Z-Hub + PORTFOLIO.md / PIPELINE.md / SYSTEM.md)
> - (c) Global-Linking-Strategie (Back-Refs zwischen 00_Core-Files)
> - (d) Vault-Integration (Wiki-Concepts strukturell auf neue 00_Core-Struktur beziehen?)
> - (e) insider-intelligence SKILL §215 Snapshot-First-Block-Review (aus 24.04. Session 1 Cross-Ref-Pass): einzigartig vs. Duplikat von TOKEN-RULES.md Snapshot-First?
>
> **Arbeits-Modus:** Section-by-Section + Approval-Gate (`superpowers:brainstorming`-Skill Pflicht). Kein Spec, kein Plan bis Approval aller Sections. **HARD-GATE:** keine Write/Edit an 00_Core-Files oder Vault bis Spec-Approval.
>
> **Sequenz für Session 3:**
> 1. `Session starten` → STATE.md (Default) lesen, kompakte Zusammenfassung
> 2. SESSION-HANDOVER.md (diese Datei) — dieser Resume-Block
> 3. Brainstorming-Skill aktivieren, Scope-Kandidaten (a)-(e) als Start-Punkte nehmen
> 4. Sections 1+2+3... durcharbeiten bis Spec-Ready
>
> **Nicht-Scope Session 3:** Execution. Nach Brainstorm-Approval → Spec (separate Session) → Plan (separate Session) → Execution (separate Session), analog Tier-1-Sequenz.
>
> ---
>
> **🗃 RESUME-INPUT (Session 2 — CodeRabbit + Vault, ARCHIVIERT, DONE 2026-04-24):**
>
> **Auftrag war:** Externe System-Integration des abgeschlossenen Refactors: (1) CodeRabbit-Pass via WSL, (2) Vault-Update-Sweep.
>
> **Ergebnis:**
> - Vault `f9d65d1`: `CLAUDE-md-Konstitution.md` auf 7-Section-Struktur + Tier-1-Refactor-Subsection + Änderungsprotokoll-Zeile 24.04.
> - CR-Pass `4cf0ea9`: 8 Findings triaggiert → 3 FIX (CLAUDE.md Edge-Cases Case-Drift/Sprach-Varianten, APPLIED-LEARNING Historie-Tabelle, Handover CR-Command-Bug) / 5 begründete Declines (Session-1-SHA-Stable, Quote-Empirisch-OK, Bullet-Count-CR-self-confirmed, Handover-Dense-wird-rebuilt, STATE-Numbering-Konvention, CORE-MEMORY-Dense-Konvention).
>
> **Sequenz war:**
> 1. `Session starten` → STATE.md (Default) lesen, kompakte Zusammenfassung ziehen
> 2. SESSION-HANDOVER.md (diese Datei) — dieser Resume-Block
> 3. **CodeRabbit-Pass** via WSL (Memory `coderabbit_cli_via_wsl.md` kanonisch):
>    ```bash
>    wsl.exe -- bash -lc "cd '/mnt/c/Users/tobia/OneDrive/Desktop/Claude Stuff' && coderabbit review --plain --type committed --base-commit d025c7f --config /dev/null"
>    ```
>    (Bug-Fix 24.04. Session 2: `--base` interpretiert `d025c7f` als Branch-Name → 339 Files > 150-Limit-Crash; `--base-commit` + `--type committed` scopt korrekt auf Diff-Commits. Quelle: Auto-Memory `coderabbit_cli_via_wsl.md` Z. 12.)
>    Commit-Range: `d025c7f..HEAD` (12 Commits). Erwartete niedrige Finding-Rate bei Markdown-Refactor; potenzielle Findings: Typos, interne Link-Breaks, Tabellen-Konsistenz. **Sequenz Codex→CodeRabbit** bereits korrekt gelaufen (Codex war Session 1).
> 4. **Vault-Update-Sweep** — Prüfe zuerst ob `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/CLAUDE-md-Konstitution.md` existiert; falls ja: strukturell aktualisieren auf neue 7-Section-Struktur (SESSION-INIT / Verhalten / KontLernen / Projektstruktur / Routing-Table / Wiki-Modus / Pointer). Falls nein: neue Konzept-Note anlegen wenn sinnvoll, oder als Backlog-Punkt notieren.
> 5. Nach Session 2 Abschluss: **Session 3 Brainstorm-Kandidat** = 00_Core Perfect-Organization (siehe STATE.md #12)
>
> **Spec/Plan-Anker (historisch):**
> - Spec v0.2: `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md`
> - Plan v0.2.1: `docs/superpowers/plans/2026-04-24-claude-md-routing-refactor.md`
>
> **Resultate Tier 1 (für CR-Context):**
> - CLAUDE.md 97→71 Zeilen (Spec-Ziel ~70 erreicht)
> - 2 neue SSoT-Files: `00_Core/APPLIED-LEARNING.md` (14/20 Bullets, v2.5) + `00_Core/TOKEN-RULES.md` (Accessibility-Modell)
> - Neue `## Routing-Table` (9 Trigger + 3 Edge-Cases + Hybrid-Match) ersetzt On-Demand-Lektüre
> - `## Pointer (Ausgelagertes)` 4 Zeilen (AL/Token/Instruktionen/Meilensteine-Archiv — User-Entscheidung gegen Info-Verlust, AC #8 dokumentiert abweichend)
> - Sync-Welle: STATE.md Pipeline-SSoT (Tier-1 als DONE #5 + Renumber-Kaskade) + CORE-MEMORY §1-Eintrag
> - Codex-Reconciliation: RECONCILED_WITH_FOLLOWUPS, alle 3 Findings abgearbeitet
>
> **Commits-Übersicht Session 1 (Baseline `d025c7f`):**
> `9ae0dcc`(AL) → `81829b5`(Token) → `e586d27`(remove) → `3e81a14`(KontLernen) → `ca66785`(Routing) → `2a67221`(Pointer-4Z) → `b99cf3b`(AC-Marker) → `1bd7492`(AL v2.5) → `3f76917`(STATE) → `0964d85`(CORE-MEMORY) → `1e79386`(Codex-Fix#3) → `3bd8632`(Option-B-Compression 86→71) → `a555a1b`(Handover+Deferred#12) → `d069b85`(TOKEN-RULES-CrossRef zu SKILL.md)
>
> **Execution-Mode für Session 2:** Direkt-Editieren (Markdown), kein Subagent-Mode (CLAUDE.md Applied-Learning Bullet #1). CodeRabbit ist externer Subprocess (keine Subagent-Problematik).
>
> **Untracked Working-Tree-Items (unverändert, informativ):**
> - `03_Tools/Rebalancing_Tool_v3.4.xlsx` — Excel-Autosave
> - `.claude/scheduled_tasks.lock` + `.claude/worktrees/` — Runtime-Files
>
> **Push-Status:** Alle 16 Commits LOKAL auf `main`. Kein `git push`. Briefing-Sync per `!SyncBriefing` falls User das will (00_Core/-Edits in STATE+CORE-MEMORY+APPLIED-LEARNING+TOKEN-RULES+SESSION-HANDOVER vorhanden).

---

## 📦 ABGESCHLOSSENE ARBEIT (2026-04-24 — Brainstorm/Spec/Plan CLAUDE.md-Routing)

### Original-Brainstorm-Input (für historische Referenz)

> Brainstorm **mitten in der Arbeit pausiert**, nicht frisch starten. Desktop-Session war Opus 4.7 + `superpowers:brainstorming`-Skill aktiv. Sections 1+2 approved, nächste Schritte glasklar.
>
> **Auftrag für Mobile-Session:** Direkt Section 3 (Routing-Table-Entwurf) präsentieren + User-Approval einholen. Sections 1+2 **nicht wiederholen** — bestätigt. Skill `superpowers:brainstorming` aktiv halten (Section-by-Section + Approval-Gate + HARD-GATE keine Implementation bis Spec-Approval).
>
> **Scope Tier 1 (diese Session):**
> - CLAUDE.md von ~150 auf ~70 Zeilen
> - Zwei neue Files: `00_Core/APPLIED-LEARNING.md` + `00_Core/TOKEN-RULES.md`
> - Projekt-lokal (nicht User-Level)
> - **Kein struktureller Reorg** außer den 2 neuen Files, keine Umbenennungen
>
> **Ziel-Gliederung CLAUDE.md (5 Top-Level, ~70 Z., User-revidiert):**
> ```
> # SESSION-INITIALISIERUNG
>   ## Pflicht-Read
>   ## Verhalten                (Sync-Pflicht, CORE-MEMORY live, briefing-sync §25, remote-Control)
>   ## Kontinuierliches Lernen  (3-Tier knapp, Details in APPLIED-LEARNING.md)
> ## Projektstruktur           (UNVERÄNDERT)
> ## Routing-Table (Read/Skip/Skill)  (NEU — Jakes #3, ERSETZT On-Demand-Lektüre)
> ## Wiki-Modus                (Trigger + Pointer zu WIKI-SCHEMA.md)
> ## Pointer (Ausgelagertes)   (NEU — → APPLIED-LEARNING, TOKEN-RULES, INSTRUKTIONEN)
> ```
> Begründung der Revision: Verhalten + Kontinuierliches Lernen sind Wenn-Dann-Regeln die bei Session-Start triggern — gehören unter Session-Init, nicht Top-Level. Pointer ans Fuß-Ende (Inhaltsverzeichnis-Logik).
>
> **Entscheidungen (verbindlich, Desktop):**
> - **A = ja:** Routing-Table **ERSETZT** die existierende On-Demand-Lektüre-Liste (keine Duplizierung, vermeidet Drift)
> - **B = c:** TOKEN-RULES **Accessibility statt Enforcement** — Regeln liegen vor, via Pointer nachlesbar, **kein Enforcement-Mechanismus**. Spec muss das explizit sagen.
> - **Variante B Hub** für STATE.md (Tier 2, DEFERRED — nicht diese Session)
> - **Projekt-lokal** beide neuen Files
> - **Kein Codex jetzt** (erst nach Spec-Draft, Memory `feedback_review_stack.md`)
>
> **Deferred (Spec unter „Future Work" notieren):**
> - **Tier 2** STATE.md 3-Split Variante B (Hub): STATE.md bleibt als ~10-Z-Hub + Banner + Pointer; darunter `00_Core/PORTFOLIO.md` (Portfolio-State + Watches + 30d-Trigger, konsolidiert mit 🟠 Portfolio-Triggers-Block) / `00_Core/PIPELINE.md` (Pipeline-SSoT 🔴/🟡/🔵 + Long-Term-Gates ⏰) / `00_Core/SYSTEM.md` (System-Zustand + Audit + Backlog). Erwartet ~70% Session-Start-Cost-Reduktion. Separate Session.
> - **Tier 2b** CORE-MEMORY.md Subkategorisierung (kalendarische Riesen-Liste → Subkategorien + Verknüpfung mit adressierten System-Elementen). User beiläufig geparkt.
> - **Tier 3** `vault_backlinks`-Check-Erweiterung auf Root-Ordner. Bereits Backlog-Punkt STATE.md Z. 120.
>
> **Advisor-Blind-Spots (alle addressieren im Spec):**
> 1. **Pain #1 nur halb adressiert.** Spec ehrlich: Tier 1 löst Kategorie **B** (projekt-eigen, ~308 Z.). Kategorie **A** (Harness: Skill-Listings + Tool-Deferred + MCP-Instructions + System-Reminders) bleibt **out-of-scope** dieser Runde.
> 2. **TOKEN-RULES = (c) Accessibility**, nicht Enforcement — explizit schreiben.
> 3. **Routing-Table ersetzt** On-Demand-Lektüre — nicht paralleles Dasein.
>
> **Pre-Spec-Checklist (vor Spec-Finalisierung abarbeiten):**
> 1. Governance-Text mitmigrieren nach APPLIED-LEARNING.md: 12/20 Bullets + Historie v1.0-v2.4 + Proaktive-Pflege-Regel (Monats-Übergang 5-Min-Scan) + Kurator-Regel-bei-Überlauf (15/20-Ziel).
> 2. Pre-Move-Grep: `grep -rn "Applied Learning\|Token-Effizienz" 00_Core/ 01_Skills/ 03_Tools/ docs/` — externe Referenzen finden, die beim Move brechen könnten.
> 3. Tier 2b CORE-MEMORY im Spec unter „Deferred / Future Work" mit 2-Zeiler (Problem + Lösung).
> 4. Revision History im Spec: Handover-verworfene STATE-Split-Entscheidung heute 2026-04-24 mit feinerer 3-Teilung + Variante-B-Hub revidiert. Bezug Memory `feedback_multi_source_drift_check.md`.
>
> **Trigger-Words-Kandidaten für Section 3 Routing-Table:**
> - `Session starten` → Default, Pflicht-Read STATE.md
> - `!Analysiere <Ticker>` → INSTRUKTIONEN + Faktortabelle + Wissenschaftliche-Fundierung-DEFCON + Skill `dynastie-depot` + Skill `backtest-ready-forward-verify`
> - `!Rebalancing` → INSTRUKTIONEN + KONTEXT
> - `!QuickCheck <Ticker>` → Faktortabelle + Skill `quick-screener`
> - `!SyncBriefing` → §25
> - Wiki-Ops (`ingest`/`lint`/`query`/Obsidian/Vault/Faktortabelle-Edit/Score-Update/Insider-Scan) → WIKI-SCHEMA.md
> - `remote-Control`/mobile weiter → Memory `remote-trigger-api.md` (User-Präferenz: **nur manuell**, keine auto-Routine — /remote-control Slash erzeugt Link/QR-Code)
> - Konsolidierungstag/System-Audit/Backlog → SYSTEM/PIPELINE-relevant (Tier 2 aktuell STATE.md §Pipeline+§System)
>
> Format-Vorschlag: `| Trigger | Lies zusätzlich (über Pflicht-Read hinaus) | Skippe | Skill-Call |`. Robuste Trigger-Klassifikation: bei Miss besser konservativ mehr laden.
>
> **Content-Migration-Templates (Section 4):**
>
> `00_Core/APPLIED-LEARNING.md`:
> - Frontmatter: `type: learning-log`, `updated: 2026-04-24`
> - Sections: Kuratierte Bullets (12/20) · Proaktive-Pflege-Regel · Kurator-Regel-bei-Überlauf · Historie v1.0-v2.4
> - Inhalt **unverändert** aus heutiger CLAUDE.md-§ „Applied Learning" übernehmen
>
> `00_Core/TOKEN-RULES.md`:
> - Frontmatter: `type: ruleset`, `scope: projekt-weit referenzierbar (Accessibility-Modell, kein Enforcement)`
> - Sections: Accessibility-Hinweis (explizit „kein Enforcement, Verfügbarkeit") · Regeln (Snapshot-First, Sync-Pflicht alle sechs, Pause-Regel, DEFCON 1 Stopp, MCP lazy-load, Modell-Default)
> - Inhalt aus heutiger CLAUDE.md-§ „Token-Effizienz (operativ)" übernehmen
>
> **Arbeits-Modus für Mobile-Session:**
> - Section-by-Section + User-Approval (kein Sprung)
> - Approval nach Section 3 (Routing-Table) einholen
> - Approval nach Section 4 (Content-Migration) einholen
> - Dann Spec schreiben: `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md`
> - Self-Review (Placeholder/Consistency/Scope/Ambiguity) → User-Review
> - **HARD-GATE:** keine Write/Edit an CLAUDE.md oder neuen Files ohne Spec-Approval
> - Dann `superpowers:writing-plans` für Implementation-Plan
> - Codex erst nach Spec-Draft (Reviewer-Matrix, Memory `feedback_review_stack.md`)
>
> **Git-Stand (bereits auf `main` gepusht):**
> - `2f6e8ba` docs(handover): Brainstorm-Input CLAUDE.md-Routing
> - `7baa543` ingest-video(third-run): Jake Van Clief Folder-System
> - Uncommitted am Desktop (informativ): `03_Tools/Rebalancing_Tool_v3.4.xlsx` (Excel-Autosave, vermutlich Revert), `.claude/scheduled_tasks.lock` + `.claude/worktrees/` (Runtime, .gitignore-Kandidaten)
>
> **Quellen-Referenzen** (bei Bedarf nachlesen, nicht automatisch):
> - Jake-Wiki-Source (7 Mechaniken + Adoption-Matrix): `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/sources/videos/updating-system/2026-03-10-jake-van-clief-folder-system-ai-agents.md`
> - Dubibubii-Präzedenz: `…/2026-04-22-dubibubii-claude-code-powerful-settings.md`
> - Memory: `feedback_friction_as_evidence.md`, `feedback_multi_source_drift_check.md`, `feedback_review_stack.md`, `feedback_information_loss_aversion.md`
>
> **Startpunkt Mobile-Session:** Kurze State-Confirmation (1-2 Sätze: „Brainstorm-State übernommen, setze mit Section 3 fort"), dann direkt Section 3 (Routing-Table-Entwurf) präsentieren + Approval-Gate. **Nicht** Section 1 oder 2 wiederholen — bestätigt.

---

## 🚀 NÄCHSTE SESSION — Post-Reset-Aufgaben Do Abend + Konsolidierungstag Fr

### Kontext-Konstanten

- **Weekly-Reset:** Donnerstag 23.04.2026 **22:00 CEST** → Full-Budget-Window öffnet (heute Abend)
- **Phase G DONE:** TMO Q1 FY26 Forward-Vollanalyse 23.04. Nachmittag (Pfad-2 Old-Pipeline). Beat + Guidance-Raise, Score 64→67, D2→D3, `fcf_trend_neg` Resolve-Gate CLEAR. Sync-Welle committed `620702a`. Siehe CORE-MEMORY §1 Eintrag 23.04.2026 Nachmittag für Details.
- **Portfolio-State aktuell:** 11 Satelliten, Nenner 8,5 (8×1,0 + 1×0,5 + 2×0), volle Rate **33,53€**, V D2-Rate **16,76€**, FLAG-Raten **0€** (MSFT + APH). Summe 285€.
- **Nächste Trigger:** V Q2 FY26 28.04. (D2-Entscheidung), MSFT Q3 FY26 29.04. (FLAG-Review).

### ~~Direkter Einstieg Post-Reset: TMO-Retro-Migration~~ **DONE 23.04. spät (Option B)**

**Sequenz:**

1. ~~**TMO-Record Retro-Migration**~~ **Retro-Audit Option B DONE 23.04. spät.** Draft `03_Tools/backtest-ready/_drafts/TMO_20260423-retro-audit.json` angelegt (gitignored), Post-hoc-Validation der Skill-Pipeline gegen den `620702a`-Record gefahren. Phase-Outcomes: P1 parse PASS · P2a freshness INFO (erwartet, Working-Tree clean) · P2b STATE-Tripwire PASS (67/3/False dreifach konsistent) · P3 N/A · P4 Dry-Run PASS (synth. Archiv ohne TMO) · P4-bis Duplicate-Guard PASS (real). Kein Re-Append — Informationsverlust-Aversion > Ästhetik. **Erster echter Skill-Forward-Run bleibt V Q2 FY26 28.04.** Siehe `log.md` §[2026-04-23] retro-audit für volles Phase-by-Phase-Protokoll.
2. **XLSX-Tools einmaliger Update** via openpyxl:
   - `03_Tools/Rebalancing_Tool_v3.4.xlsx` — TMO-Row Score 64→67, DEFCON D2→D3, Sparrate 17,81€→33,53€; volle Rate anderer 7 Satelliten 35,63€→33,53€; V 17,81€→16,76€; Nenner-Zelle 8,0→8,5
   - `03_Tools/Satelliten_Monitor_v2.0.xlsx` — TMO-Row Score/DEFCON/Rate/Delta-Spalten; Legende-Datum 17.04.→23.04.
   - Sparraten-Summe 285€ in beiden Tools verifizieren
3. **Commit:** `chore(tools): TMO D2→D3 in Rebalancing + Satelliten-Monitor nach Retro-Migration`

### Alternative: Phase F Provenance-Plan-Execution (Do Abend Post-Reset, falls Zeit + Energie)

**Nur wenn User sagt „jetzt Phase F":** Plan `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks, 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. TMO-Retro-Migration oben läuft dann gegen v2-Schema (Provenance-Gate aktiv).

### Konsolidierungstag Fr 24.04. — Backlog-Cleanup + Dashboard v2

**Zeitbudget-Warnung (Opus-Advisory 22.04.):** Block 1 harter Cutoff 50 Min → Block 2 startet 11:00 Uhr fest. Falls existence-Cleanup >50 Min → auf nächste Session verschieben (Housekeeping, kein Blocker).

**Block 0 — Pre-Check (Session-Start, 25 Min):**
0. **Tavily-Key Smoke-Test** (5 Min) — prüfen ob Key `tvly-dev-4PYXp...` noch valid oder bereits abgelaufen. Falls abgelaufen → sofort rotieren, BEVOR Block 2 startet.
0b. **Provenance-Gate Pfad-2 Smoke-Test** (5 Min) — TMO Old-Pipeline-Draft gegen v2-Schema validieren: `python 03_Tools/backtest-ready/archive_score.py --dry-run <draft>`. Falls fail → Phase-F-Entscheidung überprüfen.
0c. **Track 5a/5b Entscheidungspunkt** (NEU 23.04., 15 Min, ausgeführt NACH Block 2 v3.0.4-PASS):
    - **5a SEC EDGAR Skill-Promotion** ja/nein — Re-Validation nach 6-Paper-Ingest B21-B24 prüfen, Dashboard-Feed-Scope bedenken.
    - **5b FRED Macro-Regime-Filter** ja/nein — User-Pre-Aktion: FRED-API-Key registrieren (https://fred.stlouisfed.org/docs/api/api_key.html). B19 stärkt wissenschaftliche Begründung.
    - **Output:** Entscheidung protokollieren in STATE.md §Pipeline 🟡 (Pläne aktivieren ODER weiter 🔵 deferred). Dashboard v2 Block 3 übernimmt Feed-Scope entsprechend.
    - **Grund der Position vor Block 3:** Dashboard-Scope hängt von Feed-Entscheidung ab — EDGAR/FRED nachträglich wäre Re-Integration.

**Block 1 — System-Hygiene (Morgen, max. 50 Min):**
1. **Check-3 `markdown_header` future-date-exclude** — `03_Tools/system_audit/checks/markdown_header.py:51-63` — Long-Term-Gates (2028-04-01, 2027-10-19, 2026-10-17) aus Event-Kandidaten ausschließen. Prüfen ob `##`- und `###`-Header beide korrekt gefiltert werden.
2. **existence-Cleanup-Welle** — ~54 CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix. Grep-Pattern bereitstellen vor manuellem Edit (spart Zeit). **Falls >50 Min Gesamt-Block → hier abbrechen, Rest nächste Session.**
3. **Nach (1)+(2):** §27.5-Guard von `--minimal-baseline` auf `--core` hochziehen + INSTRUKTIONEN-§-Kommentar-Update
4. **Check-5 Batch-Output** (Opus-Empfehlung 22.04.) — gruppiert nach Sektion mit Patch-Suggestion. `system_audit/checks/existence.py` anpassen.
5. **Check-4 WARN-Semantik** (Opus-Empfehlung 22.04.) — `⚠️ Informativ` vs. `🔴 Funktional` trennen. `system_audit/types.py` oder `report.py`.
6. **Check-6 Naming-Convention-Fix** — ZIPs existieren alle (`06_Skills-Pakete/backtest-ready-forward-verify.zip` etc.), aber Check-6 sucht nach `_v1.0.0.zip`-Pattern → False Positive WARN. Fix: Check-6-Logik in `system_audit/checks/skill_version.py` auf Basename-Match ohne Versionsnummer erweitern (~5 Min).

**Block 2 — Morning Briefing + Key (ab 11:00, ~90 Min):**
7. **Morning-Briefing v3.0.4-Hotfix** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, ~90 Min). **Gate A für Track 5a/5b.**
8. **Tavily Dev-Key Rotation** — Key im Dashboard rotieren (falls nicht schon Block 0 erledigt). **Gate für Tavily-Integration Dashboard v2.**

**Block 3 — Dashboard v2 (Nachmittag, ~60 Min) — Gate: Block 2 DONE + Block 0c Entscheidung:**
9. **Dashboard v2 bauen** (`dynasty-depot-dashboard` Artifact updaten):
   - Faktortabelle.md-Parser mit `<!-- DATA:TICKER -->`-Ankern (ersetzt hartkodierte Scores)
   - Freshness-Guard: >7d 🟡 Banner / >90d 🔴 Banner
   - Preisquellen: Shibui primär → defeatbeta Fallback → yfinance Non-US
   - Tavily-Integration (scoped: Earnings ≤3d + aktive FLAGs + 1 Macro-Headline)
   - FLAG-Lösungs-Pfad inline (was löst jedes FLAG auf?)
   - Scheduled Task `dynasty-dashboard-refresh` auf File-Read-Architektur umstellen
   > **Architektur-Entscheidung (22.04. Opus+Sonnet, FINAL):** Artifact ≠ Briefing-Ersatz. Hybrid: Artifact = Snapshot/Feed (30s), Briefing = Narrativ+Reassurance (3 Min). Excel-Tools (Rebalancing/Satelliten/Watchlist) NICHT integriert. Scope = 11 Satelliten.

**Block 4 — Optional (falls Zeit bleibt):**
10. TMO-Retro-Migration falls Do Abend 22:00+ nicht erledigt
11. **Daily-Persist manueller Append** (Opus-Empfehlung 22.04.) — `python 03_Tools/portfolio_risk.py --persist daily --cashflow <eur>` für fehlende Tage 20.-24.04. ausführen. R5 ist deklarativ aktiv aber faktisch seit 17.04. stale — Interim-Gate 2027-10-19 braucht kontinuierliche Daten.

> **R5-Status-Klarstellung:** `portfolio_returns.jsonl` + `benchmark-series.jsonl` haben je nur 1 Record (17.04.). R5 Phase 3 ist deklarativ aktiv, faktisch stale. Auflösung via manuellen Append (Block 4) oder Auto-Hook (Track 4 nach ETF/Gold-Ticker-Entscheidung).

---

## 🔍 Lageprüfung Session-Start

```bash
cd "C:\Users\tobia\OneDrive\Desktop\Claude Stuff"
python 03_Tools/system_audit.py --minimal-baseline   # 3/3 PASS, rc=0
git log --oneline 57bee6b..HEAD                       # Zeigt neue Commits seit Phase-E-Closure
```

STATE.md Banner sagt: „Phase E 19/19 DONE" + „Pfad-2" + „Phase G next".

---

## 📊 Commit-Graph (seit Baseline `ab6b3f5` bis Phase-E-Closure)

```
57bee6b log(phase-e-done): Phase E 19/19 RECONCILED + CR Re-Run + Pfad-2  ← CLOSURE
09e629f chore(vault): gitignore .obsidian/graph.json + cleanup stub files
d7ecf71 log(phase-e-95): Task 19 Acceptance + Codex RECONCILED + Fix-Welle E
e3ba381 fix(system-audit): Fix-Welle E — CodeRabbit Smoke-Cleanup
51f5719 handover(phase-e-18-done): Tasks 15-18 committed, Task 19 offen
ca35f62 handover(system-audit): Task 18 Sync-Welle — Pipeline-SSoT + §10-Audit
ab7ae19 chore(docs): Task 17 INSTRUKTIONEN §27.5 Migration-Regression-Guard
fa238bf feat(system-audit): Task 16 /SystemAudit slash-command wrapper
486f2c1 test(system-audit): Task 15 temp-repo smoke + seeded-drift integration
ab6b3f5 (baseline) log(task-14): Task 14 System-Audit Optional Checks + Fix-Welle C+D
```

**9 Phase-E-Commits** seit Baseline.

---

## 🎯 Deferred-Skill-Frage (Kontext bewahrt)

**Status-Matrix-Housekeeping-Skill `system-state-guardian`** — Opus-Vorschlag 2026-04-21 Abend. Entscheidung weiterhin auf **nach Phase G / Konsolidierungstag aufgehoben**. Parallel dazu: **System-Audit-Skill-Migration abgelehnt** per Projekt-Memory `project_system_audit_skill_decision.md` (Re-Eval-Trigger = ≥3 Audit-FAIL-Triage-Patterns, dann ggf. separater `system-audit-triage`-Skill — nicht Ersatz der Slash-Command).

---

## 🌐 Session-Übergabe-Protokoll

**Vor Session-Clear (diese Session):**
1. **`!SyncBriefing` empfohlen** (CLAUDE.md §25) — pushed `00_Core/` ins GitHub-Repo. Review-Gate Pflicht.
2. Unpushed-Commits seit letztem Push: `486f2c1`, `fa238bf`, `ab7ae19`, `ca35f62`, `51f5719`, `e3ba381`, `d7ecf71`, `09e629f`, `57bee6b` + Handover-Sync-Commit. **10 Commits gesamt** — größere Charge als üblich, Review-Aufmerksamkeit angemessen.

**Nach Session-Clear — Phase-G-Einstieg (Do Nachmittag ~14:30 CEST):**
1. `Session starten` → STATE.md (Banner „Phase E 19/19 DONE, Pfad-2, Phase G next")
2. Handover (diese Datei) — Phase G TMO-Details + Pfad-2-Kontext
3. TMO Q1 Earnings lesen (MarketBeat/IR-Portal/10-Q)
4. `!Analysiere TMO` — Old-Pipeline, Minimal-Modus
5. Sync-Welle (log + CORE-MEMORY §4 + Faktortabelle + STATE + JSONL)
6. Post-Reset (Do 22:00+ oder Fr): Phase F / Konsolidierungstag je nach User-Präferenz
