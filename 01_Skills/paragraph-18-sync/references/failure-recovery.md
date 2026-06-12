# Failure-Recovery — Exit-Codes & Recovery-Hints

Tabelle aller Fail-Klassen mit konkretem Recovery-Pfad. Exit-Codes 0-6 wie in SKILL.md spezifiziert.

| Phase | Exit | Fail-Bedingung | Recovery-Hint |
|-------|------|----------------|---------------|
| P1 | 1 | `score_history.jsonl` HEAD-Append nicht heute | `!Analysiere <ticker>` zuerst — score_history.jsonl wird durch `backtest-ready-forward-verify` Schritt 7 geschrieben |
| P1 | 1 | `score_history.jsonl` HEAD-Ticker ≠ `--ticker` (Codex-H3) | Reihenfolge prüfen (anderer Analyst-Lauf dazwischen?) ODER `--ticker` korrekt setzen |
| P1 | 1 | `score_history.jsonl` leer / nicht vorhanden | `!Analysiere <ticker>` zuerst (Score-Event setzt score_history voraus) |
| P1 | 1 | `flag_events.jsonl` HEAD nicht heute (bei `--flag-event`) | `python 03_Tools/backtest-ready/archive_flag.py …` zuerst |
| P1 | 1 | `flag_events.jsonl` HEAD-Ticker ≠ `--ticker` | wrong-ticker-Drift; FLAG-Event-Reihenfolge prüfen |
| P1 | 1 | Dirty-Tree-Predicate ≥ `--allow-dirty` (Codex-M5) | `git stash` unrelated Files ODER `--allow-dirty <N>` (Hard-Cap 100, WIP-Schutz) |
| P1 | 1 | `--allow-dirty > 100` Hard-Cap-Refused | WIP zu groß; `git stash` / commit zuerst |
| P1 | 1 | Nicht inside-git-work-tree | `cd` ins Repo |
| P1 | – | Quartals-Rollover ausstehend (G-03) | **non-blocking WARN** — `quarterly_rollover_warn=true` im Report. Roll-over manuell durchführen (§18.6 Sync-Set umfasst 5 Files: log.md + archive-log + INSTRUKTIONEN §18.6 + CORE-MEMORY §13 + SYSTEM.md), dann `!ParaSync18 system-zustand --also pipeline-item` für den Sync. WARN verschwindet bei nächstem Lauf. |
| P2 | 2 | Tippfehler / ungültiger event-type | Help-Output: 4 zulässige Werte — `score-flag-sparraten` · `pipeline-item` · `system-zustand` · `critical-alert` |
| P2 | 2 | `--flag-event` ohne `score-flag-sparraten` | Modifier weglassen ODER primary-event korrigieren |
| P2 | 2 | event-type fehlt komplett | event-type als positional argument setzen |
| P3 | 3 | `event_typ_mapping.yaml` parse-fail | YAML-Syntax prüfen (Indent, Quotes) |
| P3 | 3 | `event_typ_mapping.yaml` missing | Skill-Bundle-Integrität prüfen; ggf. von git restore |
| P3 | 3 | SSoT-Drift gegen §18.1 (S7) | yaml updaten ODER §18.1-Bump in INSTRUKTIONEN.md nachvollziehen |
| P3 | 3 | xlsx-Selektion ambiguous (Codex-M4) | `00_Core/SYSTEM.md ## Active xlsx-Filenames`-Block setzen mit aktuellem Filename |
| P3 | 3 | xlsx-Stem ohne Glob-Match | xlsx-File-Existenz prüfen ODER SYSTEM.md-Pin manuell |
| (info) | – | KONTEXT §6-Refactor (Drop/Add/Reassign) | v0.1 hat KEIN Auto-Event. `Watchlist_Ersatzbank_Monitor` muss bei §6-Refactor manuell mit-synced werden (Memory `feedback_watchlist_xlsx_in_sync_set`); Voll-Auto v0.2 via PIPELINE #73c. |
| P4 | 4 | MISSING (File nicht touched + nicht staged) | File touchen + `git add <file>`; Expected-Set in `--dry-run` ansehen |
| P4 | 4 | UNSTAGED_NEW (G-01: modifiziert aber nicht staged) | `git add <file>` — File wurde geändert aber Staging vergessen |
| P5 | 5 | User-Confirm `n` | `03_Tools/xlsx-smoke-test.md`-Checklist durchgehen + xlsx neu schreiben |
| P5 | 5 | User-Confirm `skip` (Codex-H2 Hard-Fail) | **NICHT erlaubt** — Smoke korrekt durchführen ODER `--dry-run` für Trockenlauf |
| P5 | 5 | xlsx-Sub-Skill-Fail (v0.2) | Sub-Skill-Output prüfen; xlsx-Schreib-Fehler reparieren |
| P6/B | 6 | Marker-Mismatch (`marker.commit_a_sha ≠ aktuelles HEAD` vor Commit-B) | `--reset-session` + Two-Commit-Sequenz von vorn |
| P6/B | 6 | Marker-TTL überschritten (>4h; Skill-spezifisch, nicht §18-Doktrin) | `--reset-session` (Session-Abbruch + Restart) |
| P6/B | 6 | xlsx-Set-Mismatch zwischen Marker und aktuellem SYSTEM.md-Pin (Drift-Guard) | SYSTEM.md `## Active xlsx-Filenames`-Block prüfen + `--reset-session` |
| P6/B | 6 | `--verify-b` ohne Marker | Commit-A muss zuerst laufen (Marker wird dort geschrieben) |
| P6/B | 6 | xlsx UNSTAGED bei `--verify-b` (Strict-Stage-Check, H3-Fix: P6/B nicht P4) | `git add <xlsx>` — Commit-B benötigt xlsx als staged |
| P6 | – | Commit-Failure-Retry (Codex-M6) | **Re-Validate-Before-Retry:** `!ParaSync18 <event>` erneut laufen lassen vor `git commit`-Retry; State kann sich zwischen Versuchen geändert haben |

## Recovery-Workflow bei P6/B-Drift

1. `python 03_Tools/para18_sync/validator.py --reset-session` — löscht `.session_marker`.
2. Commit-A regulär neu vorbereiten (md/jsonl staged, xlsx **NICHT** staged).
3. `!ParaSync18 <event>` → PASS → `git commit`.
4. xlsx staged → `!ParaSync18 --verify-b` → PASS → `git commit`.

## Quartals-Rollover-Recovery (G-03)

WARN-only, kein FAIL. Manuelle Aktion (§18.6 v2.4):
1. `mv 07_Obsidian Vault/.../log.md 07_Obsidian Vault/.../archive/log/log-<YYYY>-Q<n>.md`
2. Neue `log.md` mit Quartals-Header.
3. Bei nächstem `!ParaSync18`-Lauf verschwindet die WARN.
