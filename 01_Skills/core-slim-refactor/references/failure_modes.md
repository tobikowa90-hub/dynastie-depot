# Failure Modes — core-slim-refactor v0.1

Vollständige Spec siehe `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` Sektion 4. Dieser Doc liefert Quick-Reference für Recovery + Liste der bekannten v0.1-Limitierungen aus dem Codex-R1 Build-Review.

---

## Exit-Codes

| Code | Klasse | Trigger | Recovery |
|---|---|---|---|
| 0 | OK | P0-P7 successful | Proceed to P8 (manual post-audit) |
| 2 | Config-Schema-Error (P1) | YAML invalid, unknown key, mutex-violation, executed-partial, append-only-misuse, date-cut-section-nonnull | Read stderr `ConfigError`; fix YAML + retry |
| 3 | Audit-Drift (P0) | system_audit.py --core fails AND `fail_close_on_drift: true` | Read audit stdout; fix drift OR set `pre_run: false` + retry |
| 4 | Classification-Empty (P2) | classify returned 0 archive + 0 slim_targets | Adjust `keywords`/`cut_before`/`fat_threshold_bytes`; oder Skill ist nicht der richtige Tool für aktuelles File-State |
| 5 | Migrate-before-Strip-Violation (P2, v0.2) | Reserved | v0.1 hat keine explicit-check; siehe `pattern_specs.md` Known-Pitfall 1 |
| 6 | Backlink-Hit (P3) | hits gefunden AND `on_match: fail_close` AND `skip_override_allowed: false` | Read stderr Hit-Summary; entweder Refs vorher aktualisieren ODER YAML auf `warn_continue`/`skip_override_allowed: true` setzen mit Begründung |
| 7 | File-Write-Error (P4/P5/P6) | OSError beim Schreiben (permission, disk full, locked) | Read traceback; fix IO-Bedingung |
| 8 | §18-Skill-Gate-Fail (P7) | `paragraph-18-sync system-zustand --dry-run --json` returned non-PASS | Read stdout für §18-Status; fix Sync-State manuell + retry. Skill macht Atomic-Rollback (backup restore + archive cleanup). |
| 10 | Reference-Archive-Mismatch (Gate-3 only) | test_reference_archive_match SHA-256 + Row-Set beide mismatch | Investigate via `failure_modes.md` Whitespace-Drift section unten |
| 99 | Approach-Reset (Karpathy 2-Fail-Stop) | 2× identischer phase+exception-class-fail | Stop. User-Konsultation oder Plan-Wechsel. |

---

## Rollback Policy

| Phase Fail | Backup Restore | Archive Cleanup | Bemerkung |
|---|---|---|---|
| P0 | N/A | N/A | Backup wird erst NACH P0 erstellt (außer dry-run) |
| P1 (executed-guard) | N/A | N/A | Kein File-Write erfolgt |
| P2 | N/A | N/A | Kein File-Write erfolgt |
| P3 | N/A | N/A | Kein File-Write erfolgt |
| P4 | N/A | N/A | Archive teilweise geschrieben — wird beim nächsten Phase-Fail aufgeräumt |
| P5 | ✅ | ✅ | Backup → target restoren; partial archive löschen |
| P6 | ✅ | — | Backup → target restoren (archive bleibt; ist konsistent) |
| P7 (Codex-R1 HIGH-1 fix) | ✅ | ✅ | Gate-Fail rollt target UND archive zurück (Atomicity-Garantie) |

Backup-Filename: `<target>.pre-refactor.bak` (gitignored via `*.pre-refactor.bak`). Nach erfolgreichem P7 wird Backup gelöscht.

---

## Approach-Reset-Schwelle (Karpathy)

Bei 2× identischem phase+exception-class-fail emittiert `_emit_sparring_hint(...)` einen Recovery-Vorschlag auf stderr:

```
=== APPROACH-RESET HINT (Karpathy §0) ===
Phase failed: <phase>
Exception: <type>: <msg>
Last failures: [(phase, exc_class), ...]
Workspace snapshot: <target>@<sha>
Backup available: <backup_path>
Config: <config_path>

Suggested next steps:
  1. Inspect failure: read traceback above + check target file
  2. Codex diagnostic: git diff > /tmp/slim-fail.diff && /codex:codex-rescue
  3. Config adjustment: edit <config_path>
  4. Plan-pivot: /superpowers:brainstorming
=== END HINT ===
```

Exit-Code in diesem Fall: `99` (EXIT_APPROACH_RESET).

---

## Whitespace-Drift Investigation (Gate-3 Fallback)

Wenn `test_reference_archive_match` SHA-256 mismatch aber Row-Set-Signature match → Whitespace-Drift im Archive-Header (timestamps, line-endings, oder pattern-impl-Bug).

**Diagnose-Schritte:**
1. `git show <commit_sha>:<archive_path> > /tmp/historical.md`
2. `diff /tmp/historical.md <newly_computed_archive>.md` — wenn nur Header-Lines (timestamp + cut-date) abweichen → Row-Set-Signature war richtige Strategie, kein Fix nötig.
3. Wenn Body-Lines abweichen → Pattern-Impl-Bug. Codex-Sparring auslösen.

---

## Diagnostic-Output-Konventionen

| Stream | Inhalt |
|---|---|
| stdout | `=== <Phase> START/OK/FAIL ===` markers; archive-write summaries; P7 Codex hand-off bundle |
| stderr | Backlink-hits; warnings (warn_continue/skip_override); rollback-messages; sparring-hints; full tracebacks bei unbekannter Exception |

Bei `--dry-run` schreibt P4/P5 `[dry-run]`-präfixierte Marker, KEINE files.

---

## Known v0.1 Limitations (Codex-R1 MEDIUM, deferred zu v0.1.1)

### MEDIUM-1: Backlink-Scan Symlink-Loop-Risiko (deferred)

`scan_backlinks(scan_paths)` macht `Path.rglob("*.md")` ohne Symlink-Guard. Bei Repos mit recursive-symlink-Strukturen → potential infinite-traversal.

- **Aktuelle Mitigation:** Dynastie-Depot hat keine recursive symlinks; Risiko-Likelihood low.
- **v0.1.1 TODO:** symlinked-dirs skippen oder `visited_realpaths`-Set führen.

### MEDIUM-2: Nested-Schema-Validation fehlt (deferred)

Siehe `yaml_schema.md` Known-Gaps. Symptom: Missing nested keys schlagen erst zur Runtime als `KeyError` durch statt als clean `ConfigError`.

- **Mitigation v0.1:** Worked-examples als Schablone nutzen.
- **v0.1.1 TODO:** per-pattern Pflicht-Key-Liste hinzufügen.

### MEDIUM-3: Archive-Path-Boundary nicht erzwungen (deferred)

Siehe `yaml_schema.md` Path-Safety-Gap. Symptom: `archive.path` kann beliebige absolute/relative Pfade sein, "Archive-Local-Only"-Disziplin nicht code-enforced.

- **Mitigation v0.1:** Pre-Commit-Config-Review + P7-Hand-Off zeigt absolute Pfad.
- **v0.1.1 TODO:** resolved-path-Check unter `repo_root / "05_Archiv/"`.

---

## Cross-Reference

- Spec §4 Error-Handling (full text): `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` lines 372-454
- Codex-R1 Review (Wave-5-Break-2): commit a0dc16d log + R1-result transcript
- Karpathy Approach-Reset: `00_Core/INSTRUKTIONEN.md §0`
