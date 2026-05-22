---
name: paragraph-18-sync
description: §18-Sync-Pflicht-Verify-Orchestrator (fail-close). Prüft das §18-File-Set BEVOR `git commit`, mit Multi-Event-Union §18.2 + Two-Commit-Same-Session-Protokoll für xlsx-Tools. Trigger `!ParaSync18 <event-type>`. KEIN Auto-Edit, KEIN --force-Bypass. Nutze diesen Skill IMMER wenn der User §18-Sync, Sync-Pflicht-Bundle, Pre-Commit-Bundle-Verify, score-flag-sparraten/pipeline-item/system-zustand/critical-alert-Events erwähnt — oder wenn ein §18-relevanter File-Touch (PIPELINE/PORTFOLIO/CORE-MEMORY/Faktortabelle/log.md/score_history.jsonl/SYSTEM.md/xlsx-Tools) vor einem `git commit` ansteht. Auch bei "verify §18", "check sync before commit", "pre-commit-Bundle prüfen", "Pflicht-Set verifizieren" oder Versions-Bump-Conditional (`--version-bump`) aktivieren.
version: v0.1.0
event_types:
  - score-flag-sparraten
  - pipeline-item
  - system-zustand
  - critical-alert
---

# paragraph-18-sync v0.1.0

**Zweck:** Fail-close Verify-Orchestrator für §18-Sync-Pflicht. Prüft Bundle-Vollständigkeit + Pre-existing-Dirty-Schutz + Workflow-Ordering + xlsx-Smoke-Test vor `git commit`. Reduziert die manuelle §18-Disziplin auf einen CLI-Pass; bei Drift fail-close mit klarem Recovery-Hint.

**Doktrin-Anker:** `00_Core/INSTRUKTIONEN.md §18` (Sync-Pflicht-SSoT v2.4).
**Validator-CLI:** `03_Tools/para18_sync/validator.py`.
**SSoT-Mirror:** `references/event_typ_mapping.yaml` (Drift-Guard via Test S7).
**Spec-Anker:** `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` v0.3.

## Trigger

```
!ParaSync18 <event-type> [--also <event-type>]* [--flag-event|--no-flag-event]
            [--version-bump] [--ticker <SYMBOL>] [--allow-dirty <N>]
            [--verify-b] [--reset-session] [--dry-run] [--json]
```

**Event-Typen (gemäß §18.1):**

| Event | Trigger-Beispiel | Expected-Set (Auszug) |
|-------|------------------|------------------------|
| `score-flag-sparraten` | Post-`!Analysiere` · `archive_flag.py` · Sparraten-Edit | PORTFOLIO + Faktortabelle + CORE-MEMORY + log + score_history + config.yaml + 2 xlsx (Rebalancing + Satelliten_Monitor) (+ flag_events.jsonl bei `--flag-event` = FLAG-Trigger/Resolve) |
| `pipeline-item` | Plan-Commit · Gate-Passage · Status-Transition | PIPELINE.md + log.md (+ SESSION-HANDOVER.md bei Session-Abschluss; mid-Session optional) |
| `system-zustand` | DEFCON-Bump · MCP-Change · Briefing · Backlog | SYSTEM.md + log.md (+ CORE-MEMORY.md bei `--version-bump` Conditional, §6-relevanter Versions-Inkrement) |
| `critical-alert` | STATE.md Hub-Edit (Alert-Slot only) | STATE.md (NO-OP-PASS — kein Bi-Sync) |

> **xlsx-Tools-Hinweis:** Default-Set v0.1 = 2 xlsx (Rebalancing + Satelliten_Monitor) gemäß §18.1. `Watchlist_Ersatzbank_Monitor_v1.1.xlsx` ist bei KONTEXT §6-Refactor (Drop/Add/Reassign) zusätzlich §18.7-Smoke-relevant (Memory `feedback_watchlist_xlsx_in_sync_set`); v0.1 hat dafür noch keinen automatischen Trigger — manuelle Aufnahme nötig. Voll-Auto in v0.2 (PIPELINE #73c).

**Multi-Event-Union (§18.2):** `--also` mehrfach erlaubt; Pflicht-Sets werden dedupliziert (z.B. log.md erscheint nur 1× im Expected-Set bei Score+Pipeline+System).

## Workflow P1-P7

### P1 — Pre-Flight
- **Working-Tree-Check:** git-Repo verified, kein corrupt-state.
- **Ordering-Guard (Codex-H3):** `score_history.jsonl` HEAD-Append-Datum = heute UND HEAD-Ticker = `--ticker`. Verhindert wrong-ticker-Drift bei sequenziellen Analysen.
- **FLAG-Guard:** `flag_events.jsonl` HEAD-Append heute + Ticker-Match (bei `--flag-event`).
- **Dirty-Tree-Predicate (Codex-M5):** `|unstaged ∪ untracked| \ expected_set ≥ allow_dirty` (Default 10) → FAIL. `--allow-dirty <N>` mit Hard-Cap 100.
- **Quartals-Rollover-WARN (G-03, §18.6):** non-blocking; emittiert `quarterly_rollover_warn=true` im Report.

### P2 — Event-Klassifikation
- Parse `<event-type>` + `--also` (dedupe).
- Validate gegen 4 zulässige Werte (Typo-Refuse).
- Refuse bei `--flag-event` ohne `score-flag-sparraten`.

### P3 — Expected-Set-Resolve
- Load `references/event_typ_mapping.yaml`.
- Compute Union pro Event-Set; `--flag-event`-Conditional appliziert (score-flag-sparraten → +flag_events.jsonl); `--version-bump`-Conditional (system-zustand → +CORE-MEMORY.md).
- **xlsx-Selektion (Codex-M4 deterministisch):** Lookup via `00_Core/SYSTEM.md ## Active xlsx-Filenames`-Pin. Fallback: Glob `<Stem>_v*.xlsx` + Semver-Pick (WARN-only). Ambiguity → FAIL exit=3.

### P4 — Staging-Diff (4-Bucket)
Pro File im Expected-Set:
- **STAGED** → PASS-Beitrag.
- **UNSTAGED_NEW** (G-01) → FAIL exit=4. Hint: `git add <file>`.
- **UNSTAGED_PREEXISTING** → WARN (Pre-existing-Dirty-Schutz, Snapshot-Mode).
- **MISSING** → FAIL exit=4. Hint: File touchen oder Expected-Set prüfen.

### P5 — xlsx-Smoke-Test (v0.1 Manual-Confirm)
- Pro xlsx-File im Expected-Set: User-Prompt "Smoke-Test gemäß `03_Tools/xlsx-smoke-test.md` PASS? (y/n)".
- **`skip` = Hard-FAIL (Codex-H2):** NICHT erlaubt — Smoke korrekt durchführen oder `--dry-run`.
- v0.2 (post-PIPELINE #73b): Sub-Skill-Auto-Call `!XlsxSmokeTest <file>`.

### P6 — Two-Commit-Same-Session-Protokoll
- **Commit-A:** md/jsonl/yaml-Set (xlsx **nicht** staged); validator schreibt `.session_marker` (gitignored, JSON: `{session_id, commit_a_sha, expected_xlsx, xlsx_tool_stems, started_at_*, status}`).
- **Commit-B:** xlsx via `!ParaSync18 --verify-b`. Zweiter Verify-Pass (P1+P4+P5-Subset-Revalidation) gegen Marker.
- **Drift-Detection:** Marker-TTL >4h (Skill-spezifisch, nicht §18-Doktrin) ODER `marker.commit_a_sha ≠ aktuelles HEAD` (= HEAD vor Commit-B) ODER xlsx-Set-Mismatch (Marker vs aktuelles SYSTEM.md re-resolve) → FAIL exit=6. Recovery: `--reset-session`.

### P7 — Closure-Report
JSON-Output mit Feldern: `verdict` · `phase` · `events` · `expected_files` · `staged_files` · `missing` · `unstaged_new` · `unstaged_preexisting` · `xlsx_verified` · `session_marker` · `retry_required_revalidation` · `quarterly_rollover_warn` · `recovery_hints`.

**Exit-Codes (Spec §7):**

| Code | Phase | Bedeutung |
|------|-------|-----------|
| 0 | — | PASS (oder NO-OP für `critical-alert`) |
| 1 | P1 | Pre-Flight (ordering, ticker, dirty, repo) |
| 2 | P2 | Event-Klassifikation (Typo, ungültiger Modifier) |
| 3 | P3 | Expected-Set / yaml-parse / xlsx-Ambiguity |
| 4 | P4 | Staging-Diff (MISSING / UNSTAGED_NEW) |
| 5 | P5 | xlsx-Smoke-Test (Confirm n, skip, sub-skill-fail) |
| 6 | P6/B | Two-Commit-Protokoll-Drift |

## Out-of-Scope

- **Auto-Edit** von Markdown-Files (Verify-First-Foundation).
- **Auto-Append** zu `score_history.jsonl` / `flag_events.jsonl` (Sub-Tool-Domain: `backtest-ready-forward-verify` + `archive_flag.py`).
- **Auto-Commit** (Analyst-Verantwortung; validator gibt nur Verdict).
- **Push** (= `session-closure`-Skill-Verantwortung, §25.5).
- **xlsx-Smoke-Test-Auto-Run** (v0.1 manual-confirm; v0.2 PIPELINE #73b).
- **§18.1-Zeile-5 KONTEXT §6** (= PIPELINE #73c, separates Event-Mapping out-of-scope v0.1).

## Verwandte Tools / Skills

- `00_Core/INSTRUKTIONEN.md §18` — Sync-Pflicht-SSoT (Doktrin-Anker).
- `01_Skills/backtest-ready-forward-verify/` — schreibt `score_history.jsonl` (Sub-Tool, läuft VORHER).
- `03_Tools/backtest-ready/archive_flag.py` — schreibt `flag_events.jsonl` (Sub-Tool, läuft VORHER).
- `03_Tools/xlsx-smoke-test.md` — §18.7 Smoke-Test-SSoT (P5-Referenz).
- `01_Skills/session-closure/` — End-of-Session-Workflow (komplementär; ruft `!ParaSync18` mid-session NICHT auf, eigenes §18-Coupling).

## Boundary

- **paragraph-18-sync** = **Mid-Session-Verify-Orchestrator** vor `git commit`.
- **session-closure** = **End-of-Session-Orchestrator** (Briefing-Sync, log-Closure, Push-Gate).
- Beide Skills sind komplementär; v0.2-Refactor-Opportunity: session-closure delegiert §18-Verify an `paragraph-18-sync`-validator (out-of-scope v0.1).

## Detail-Referenzen (lazy-load)

- `references/event_typ_mapping.yaml` — SSoT-Mirror §18.1 (4 Event-Typen → Pflicht-Files).
- `references/sub-tool-coupling.md` — Z1/Z3/Z4 Workflow-Ordering, session-closure-Boundary, v0.2-Delegation.
- `references/failure-recovery.md` — Exit-Code-Tabelle + Recovery-Hints für alle Fail-Klassen.
- `references/build-time-review-log.md` — Append-only Versions-Historie + Review-Pass-Log.
