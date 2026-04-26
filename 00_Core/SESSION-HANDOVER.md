# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-26 — Spec-Tranche aus Opus-Parallel-Session done: PR #2 mit drei atomaren Commits (Karpathy §0 + Banner-Migration + Pre-Processing Regel 5) rebase-merged auf main. Phase-2-Branch `feat/system-audit-phase-2` parkt unverändert für Resume in nächster Session.

### 🟢 Resume-Stand (zurück zu `feat/system-audit-phase-2`)

**Branch ist 4 Commits voraus auf `becb190` main:**
- `ec8925a` — Task 1 PyYAML-Preflight (rc=2 + install hint) — fully reviewed ✅
- `6a9051e` — Task 2 score_event_parity (CORE 8→9, +4 Smoke) — Spec+Quality ✅, Codex GO-WITH-FIXES ⚠️
- `e4e250e` — Task 3 skill_frontmatter (CORE 9→10, +5 Smoke) — Spec+Quality ✅, doc-nit
- `ad69501` — Task 4 header_freshness (CORE 10→11, +4 Smoke) — **Reviews offen**

**Plan-File (v1.1):** `docs/superpowers/plans/2026-04-25-system-audit-rework.md` — 8 Tasks, Sequenz: PyYAML-Preflight → §18-Parity → Skill-Frontmatter → Header-Freshness → Top-Level-Governance → Cross-Source-Reverse → Pointer-Completeness → Defer-Doku. Pre-Execution Codex-Review (`a2862e6a730e2ecca`) GO-WITH-FIXES alle 12 Findings (P2-01..12) addressed in v1.1.

**Smoke-Suite-Stand:** 17/17 `[OK]` (von 14 vor Plan), 73 Test-Funktionen.

### ⚠️ Phase-2-Codex-Findings (`adacf0c067b462e5b`, GO-WITH-FIXES) — Vor Task 5 fixen

**TaskID 12 — Task 2 Heuristiken tightenen** (~30 min):
1. `_scan_text_for_basenames` zu naive (`score_event_parity.py:33`) — Whole-file substring scan; line-scope auf list-entry-pattern (Lines mit `,` `'` `"` `` ` `` `|` `@(`).
2. `_scan_text_for_wrong_versions` Changelog-FP (`score_event_parity.py:48`) — INSTRUKTIONEN.md Z315/Z361 `v1.8 → v2.0 ... §18.1 §18.2` ist FP. **Empfehlung Option b: Marker-Check** — nur Lines mit Section-Header-Pattern (`## §18`, `# §18`, `**§18**`) als governing-rule treaten. Plus Smoke-Test `test_score_event_parity_no_fp_on_changelog` als Regression-Anchor.
3. Task 3 Doku-Drift (kein Code-Bug) — wenn `dynastie-depot/SKILL.md` in Task 8 Cleanup landet: `description: >` durch single-line oder korrekte Indent ersetzen.

**Heutige Tranche-Erkenntnis (Final-Review `afe31a2e5397b877d`):** Pre-existing FP-Risk in INSTRUKTIONEN.md Z361 wurde durch heutige Edits nicht eingeführt — gehört zu TaskID 12. Co-Occurrence ist jetzt durch §18.4-Einfügung möglicherweise auf andere Z-Nummer verschoben, Logik aber identisch.

**Showstopper:** keine. Task 4 Reviews + Tasks 5-7 unabhängig von Task 2 Heuristik-Issues, aber Task 5 Top-Level-Governance-Parity berührt CORE-Registry-Count → erst nach TaskID-12-Fix.

### TODO nächste Session — Resume-Sequenz

**Pre-Resume-Checks (manuell, ohne Subagent):**
1. `git checkout feat/system-audit-phase-2`
2. `git rebase main` — heutige 3 Commits sind nun auf main, Phase-2-Branch sollte rebase-clean sein (Task 4 fügt header_freshness in `01_Skills/`/`03_Tools/` ein, Heutige Edits sind in `00_Core/` + `01_Skills/dynastie-depot/SKILL.md` — Konflikt-Potential nur bei SKILL.md, dort heutige Pre-Processing Regel 5 vs. Phase-2-Skill-Frontmatter-Edits)
3. `git status --short` — pre-existing dirty (Rebalancing.xlsx + Vault-Deletes + code-workspace; STATE.md / SESSION-HANDOVER.md heute committet)
4. `python "03_Tools/system_audit/_smoke_test.py"` — 17/17 grün

**Sequenz (priorisiert):**
1. **Task 4 Reviews** (TaskID 11) — Spec-Reviewer + Code-Quality-Reviewer für `ad69501` dispatchen (~5 min)
2. **Codex-Fix Task 2** (TaskID 12) — beide Heuristiken + neuer Regression-Test (~30 min). Commit-Message: `fix(audit): score_event_parity Codex-Review-Heuristik-Tightening`
3. **Task 5** Top-Level-Governance-Parity (Plan §1268-1544) — erst nach TaskID 12
4. **Task 6** Cross-Source-Reverse (Plan §1546-1831)
5. **Task 7** Pointer-Completeness (Plan §1833-2121) — Achtung: heute neue Routing-Table-Zeile in CLAUDE.md könnte Pointer-Section-Anchor-Test beeinflussen, kurz prüfen
6. **Final-Review** (TaskID 10) — Codex + CodeRabbit auf Tasks 4-7 + Task-2-Fix
7. **Task 8** Defer-Doku + optional Live-Drift-Cleanup

**Erwarteter End-Stand:** CORE 11→14, Smoke 73→84, 8-9 Commits auf Branch, rc=0/1, PR-fähig.

### Heute-Tranche-Doku (für Phase-2-Rebase-Awareness)

**3 Commits auf main seit `d129270`:**
- `4e9d4af` — Karpathy §0 in INSTRUKTIONEN.md + CLAUDE.md Pointer + Routing-Hook
- `669a801` — Stand-Banner aus Header in Footer der 8 00_Core-Files (§18.4 Konvention)
- `9c468ec` — Pre-Processing Regel 5 (Tool→Metrik-Triage) in dynastie-depot SKILL.md

**Konflikt-Risiko bei Phase-2-Rebase:**
- `INSTRUKTIONEN.md`: §0 + §18.4 sind neue Sektionen — Phase-2 hat dort keine Edits, aber TaskID 12 wird `score_event_parity.py`-Heuristik betreffen, **die governance-File scannt**. §18.4-Wording neu lesen für Test-Fixture-Aktualisierung.
- `01_Skills/dynastie-depot/SKILL.md`: Pre-Processing Regel 5 angefügt. Phase-2-Task 3 (skill_frontmatter) und potenziell Task 8 (Live-Drift-Cleanup `description: >` Fix) berühren denselben File. Frontmatter (oben) und Pre-Processing-Block (unten Z832ff) sollten konfliktfrei sein.
- 8 × `00_Core/*.md` Stand-Banner-Migration: Phase-2-Code touchiert keine 00_Core-Files direkt; mögliche Test-Fixtures in `_smoke_test.py:505,535` referenzieren `STATE.md:18`/`STATE.md:1` — sind aber Test-Fixture-Strings, keine echten File-Refs (verifiziert).

### Memory-Updates persistiert
- `feedback_pre_commit_diff_inspection.md` (NEU 26.04.) — Bulk-Refactor-Hygiene: vor commit `git diff --cached` prüfen, pre-existing dirty rutscht silent durch
- `feedback_review_via_codex_not_advisor.md` — Reviews via Codex, nie advisor()
- `feedback_onedrive_edit_collision.md` — Edit-Collision-Pattern bei offenem Editor

### Standing-Pre-existing-Dirty
- `03_Tools/Rebalancing_Tool_v3.4.xlsx` — weiterhin ungeklärt
- `07_Obsidian Vault/.../app.json` + 4 Vault-Deletes (`2026-04-23.md`, `Unbenannt*`) — Vault-Cleanup-Backlog
- `Claude-Stuff.code-workspace` — IDE-Setup, gitignore-Kandidat

### Wichtige Calibration-Notiz
F3 (`_forward_verify_helpers.py:25, 257-259`) bleibt **INFO, nicht FIX** — Teil-Gate-Trade-off, Codex-RECONCILED VALID. Nicht als §18-Verletzung oder score_event_parity-Failure re-klassifizieren.

---

## Standing-Focus 30 Tage (unverändert seit Tier-2-Finalize)

- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal-Gate)
- **29.04. MSFT Q3 FY26** — FLAG-Review (CapEx/OCF bereinigt <60%)

---

## 📜 Handover-Policy (seit 2026-04-25 — Tier 2 Follow-up)

Nur **aktiver** RESUME-INPUT-Block in dieser Datei. Historie kanonisch in:
- **`git log`** — jeder Session-Ende-`handover:`-Commit ist die Banner-Chronik
- **`CORE-MEMORY.md` §13** — System-Lifecycle-History
- **`PIPELINE.md`** — Strikethrough-DONE-Items mit Datum + Commit-Hash

Pflege-Pflicht: Bei Session-Ende den aktiven Block durch den neuen ersetzen — nicht anhängen.

---

*🔁 SESSION-HANDOVER.md v2.0 | Dynasty-Depot | Slim-Resume — Policy B*
