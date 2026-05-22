# Sub-Tool-Coupling

**paragraph-18-sync = Mid-Session Verify-Orchestrator** (vs. `session-closure` = End-of-Session).

## Reihenfolge (Workflow-Ordering, Z1)

1. **Sub-Tools laufen ZUERST** (Append/Write-Phase):
   - `backtest-ready-forward-verify` (oder dessen Schritt 7) appendet `score_history.jsonl`.
   - `03_Tools/backtest-ready/archive_flag.py` appendet `flag_events.jsonl`.
   - Manuelle Edits an `log.md` / `CORE-MEMORY.md` / `Faktortabelle.md` / `PORTFOLIO.md` / `config.yaml`.
   - Manuelle openpyxl-Writes an xlsx-Tools (`Rebalancing_Tool` / `Satelliten_Monitor` / `Watchlist_Ersatzbank_Monitor`).

2. **`!ParaSync18` läuft DANN** (Verify-Pass vor `git commit`):
   - P1 prüft Sub-Tool-Output-Append-Timestamp = heute + Ticker-Match.
   - P4 prüft Staging-Vollständigkeit gegen Expected-Set.
   - P5 prüft xlsx-Smoke-Test-Bestätigung.

3. **`git commit` läuft DANACH** (Analyst-Verantwortung).
   - Bei Two-Commit-Protokoll (P6, score-flag-sparraten mit xlsx): Commit-A nur md/jsonl, dann `!ParaSync18 --verify-b` vor Commit-B (xlsx).

## Boundary zu session-closure (Z3)

- **`paragraph-18-sync`** = §18-Sync-Pflicht-Bundle-Verify (anytime mid-session, jederzeit re-callable).
- **`session-closure`** (v0.2.0) = End-of-Session-Orchestrator (Briefing-Sync §25, log-Closure, Push-Gate).
- session-closure v0.2.0 hält **eigene** §18-Coupling-Schritte (Memory-Stand 2026-05-23 v0.1.0-Promotion). Ein Refactor-Opportunity ab paragraph-18-sync v0.2.0: session-closure delegiert seinen §18-Check an `validator.py`. **NICHT v0.1-Scope** — beide Skills laufen v0.1 noch unabhängig parallel.

## xlsx-Sub-Skill-Delegation (Z4)

- **v0.1 (jetzt):** P5 = manual-confirm `(y/n)` per xlsx-File. `skip` = Hard-Fail (Codex-H2-Doktrin: kein Bypass-Pfad).
- **v0.2 (post-PIPELINE #73b xlsx-smoke-test-runner):** P5 ruft `!XlsxSmokeTest <file>` automatisch + fail-close-Propagation. Sub-Skill-Exit ≠ 0 → P5 fail-close.

## Out-of-Scope für v0.1

- Auto-Edit/Auto-Append/Auto-Commit/Push (siehe SKILL.md §Out-of-Scope).
- §18.1-Event-Typ-Zeile 5 (KONTEXT §6) → PIPELINE #73c, eigenes Event-Mapping post-v0.1.
- Cross-Skill Trigger-Hooks (z.B. `dynastie-depot` ruft `!ParaSync18` automatisch nach Score-Move) → v0.2-Erweiterung möglich, v0.1 strict-manual.
