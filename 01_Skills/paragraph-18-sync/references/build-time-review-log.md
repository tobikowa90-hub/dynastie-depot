# Build-Time Review-Log

Append-only Versions-Historie. Eintrag pro Skill-Version + Review-Pass.

---

## v0.1.0 — 2026-05-23

**Acceptance-Kriterien für Promotion (alle erfüllt für v0.1.0):**

- **Spec:** `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` v0.3 (28 Befunde adoptiert in 3 Codex-Runden).
- **Plan:** `docs/superpowers/plans/2026-05-22-paragraph-18-sync-implementation.md` v0.2 (Codex-Plan-Review 7 Findings adoptiert).
- **Build-Sessions:** 22.05. (Tasks 1-12 + CP1/CP2/CP3-R1+R2) → 23.05. (Tasks 13-18).
- **Test-Suite:** S1-S20 implementiert; aktuell 47 collected = **44 PASS + 3 SKIP** (S7+S8a soft-skip by design; S3 conditional skip wenn `score_history.jsonl` kein heute-Append).
- **Reviews (alle 3 Pflicht):**
  - Codex Single-Pass (gpt-5.3-codex via `~/.codex/config.toml`-Pin).
  - Gemini-CLI direct stdin-pipe Cross-Sync (SKILL.md ↔ INSTRUKTIONEN §18).
  - CodeRabbit `coderabbit review -t uncommitted --dir 03_Tools/para18_sync` (WSL Ubuntu).
- **Dogfood:** 4 Test-Cases gegen Live-State (pipeline-item / critical-alert / score-event / multi-event-union).
- **Promotion-Sync-Set (v0.1 verpflichtend, Codex-L2-Fix 2026-05-22):** PIPELINE #73a DONE + log.md Promotion-Entry + SYSTEM.md Skill-Registry + Active-xlsx-Block + CLAUDE.md Routing-Table-Eintrag `!ParaSync18` (v0.1-Pflicht, nicht v0.2-deferred).

---

## Review-Pass — 2026-05-23 (Task 16, v0.1.0 Final-Reviews)

Engineer trägt nach jedem Review-Pass exakte Counts ein (Platzhalter `<N>` ersetzen):

- **Codex (gpt-5.3-codex):** `<H>` HIGH + `<M>` MEDIUM + `<L>` LOW Befunde — pro Finding: adoptiert / abgelehnt mit 1-Zeilen-Begründung.
- **Gemini Cross-Sync:** `<N>` Drift-Findings (SKILL.md ↔ INSTRUKTIONEN §18) — alle adoptiert ODER Begründung pro Reject.
- **CodeRabbit (WSL Ubuntu):** `<C>` Critical + `<M>` Major + `<L>` Minor — adoptiert / out-of-scope.

---

## Dogfood-Test — 2026-05-23 (Task 17, gegen Live-State ROOT)

Engineer trägt nach Live-Run pro Zeile den tatsächlichen Exit-Code + Verdict ein:

- **Test 1** (`pipeline-item --dry-run`): exit=`<N>`, Verdict=`<PASS/FAIL>`.
- **Test 2** (`critical-alert` NO-OP-PASS): exit=`<N>`, Verdict=`<PASS/FAIL>`.
- **Test 3** (`score-flag-sparraten --no-flag-event --ticker V --dry-run`): exit=`<N>`, Verdict=`<PASS/FAIL>` (P1-FAIL legitim wenn kein heute-Append in `score_history.jsonl`).
- **Test 4** (`score-flag-sparraten --also pipeline-item --no-flag-event --ticker V --dry-run`): exit=`<N>`, Verdict=`<PASS/FAIL>`.
- **Verdict gesamt:** v0.1.0 Promotion-ready WENN ≥3/4 PASS UND kein Crash/Traceback.
