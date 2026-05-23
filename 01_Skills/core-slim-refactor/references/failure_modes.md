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

## CP18 Codex-Review Befunde (2026-05-23, Wave-7-Break-4)

### HIGH-1: P7 SystemExit umging Rollback (CLOSED)

`phase_p7` signalisiert Gate-Fail via `SystemExit(EXIT_GATE_FAIL)`. `SystemExit`
erbt von `BaseException`, NICHT von `Exception` — das ursprüngliche
`except Exception` am P7-Call-Site (eingeführt für Break-2 HIGH-1) hat den
Atomicity-Rollback **stillschweigend übersprungen**. Die dokumentierte
P7-Atomicity-Garantie war faktisch broken.

- **Fix Commit:** Diff CP18-HIGH-Fix-Bundle. Alle Rollback-Sites (P5/P6/P7) catchen jetzt `(Exception, SystemExit)`.
- **Regression-Test:** `tests/test_pipeline.py::test_backup_restored_on_p7_sysexit` (env-sentinel `P7_SYSEXIT` → SystemExit; asserts target+archive cleanup).

### HIGH-2: §18-Gate akzeptierte rc==0 mit status=FAIL (CLOSED)

`phase_p7` prüfte den JSON-`status` nur innerhalb `if r.returncode != 0`.
rc==0-Antworten mit `{"status": "FAIL"}` wurden silent als Gate-PASS interpretiert.

- **Fix:** Refactor zu pure-function `_evaluate_p18_result(rc, stdout)` → require BOTH rc==0 AND status=="PASS".
- **Regression-Test:** `tests/test_p18_gate_parser.py::test_rc0_status_fail_blocks_high2`.

### HIGH-3: §18-Gate akzeptierte rc!=0 mit status=PASS (CLOSED)

Innerer Check `if data.get("status") != "PASS"` short-circuitete den Fail-Branch
auch wenn rc Failure signalisierte. Subprocess-Failures mit hängengebliebenem
JSON-PASS-Body bestanden den Gate.

- **Fix:** Selbe Logik wie HIGH-2 — beide Konditionen müssen erfüllt sein.
- **Regression-Test:** `tests/test_p18_gate_parser.py::test_rc_nonzero_status_pass_blocks_high3`.

### MEDIUM-4: §18-Subprocess Timeout (CLOSED inline)

Vorher kein `timeout=`-Parameter → hängender p18-Prozess hätte Skill unbegrenzt blockiert. `subprocess.run(..., timeout=30)` + `TimeoutExpired` → EXIT_GATE_FAIL.

### MEDIUM-5: §18-stderr Surfacing (CLOSED inline)

Vorher wurde nur stdout geschrieben; stderr-Diagnostics gingen verloren. Jetzt: `r.stderr[-2000:]` auf jedem Fail-Branch.

### MEDIUM-6: classify_date_cut `section_anchor`-Parameter unused (deferred v0.1.1)

`patterns.py::classify_date_cut` akzeptiert `section_anchor`-Parameter aber
ignoriert ihn — die Klassifikation scant immer das gesamte Dokument.
Config-Schema erzwingt `target.section: null` für date-cut (siehe `config.py`
`test_date_cut_requires_null_section`), daher kein Verhaltens-Bug — nur
Signatur-Klarheits-Gap.

- **Mitigation v0.1:** Schema-Block sorgt für consistent wholesale-only-Semantik.
- **v0.1.1 TODO:** Entweder Parameter entfernen, oder anchor-scoped date-cut implementieren (Spec-Erweiterung nötig).

### MEDIUM-7: Duplicate Section-Anchors silent-ambiguous (deferred v0.1.1)

`patterns.py::_find_section_indices` nimmt den **ersten** Match ohne Duplicate-Detection. Bei wiederholten Headings (z.B. zwei `## 13. System-Lifecycle-History`) wird der falsche Block mutiert, ohne Warnung.

- **Likelihood:** LOW — Dynastie-Depot-Convention sind Section-Headings unique pro File.
- **v0.1.1 TODO:** Duplicate-Detection bei Classify-Phase + fail-close mit Diagnostic.

### MEDIUM-8: Backup-Overwrite ohne Integrity-Check (deferred v0.1.1)

`phase_p0` schreibt Backup an feste `<target>.pre-refactor.bak`-Pfad ohne Hash/Size-Verifikation. Bei aufeinanderfolgenden Skill-Runs ohne success-cleanup wird der vorherige Backup-Inhalt überschrieben.

- **Mitigation v0.1:** `_cleanup_backup_on_success` löscht Backup nach erfolgreichem Run; Karpathy-Disziplin: nie zwei Skill-Runs ohne Commit dazwischen.
- **v0.1.1 TODO:** Unique-Path-Suffix (timestamp) ODER refuse-overwrite + post-write-Hash-Verify.

### LOW-1: Missing-Anchor kollabiert in EXIT_CLASSIFY_EMPTY (deferred v0.1.1)

Anchor-not-found → leere Section → generic exit 4. Diagnose weniger präzise als `failure_modes.md`-Tabelle suggeriert ("Adjust keywords/cut_before/fat_threshold" hilft nicht bei tippfehler im section-anchor).

- **v0.1.1 TODO:** Separater EXIT_ANCHOR_NOT_FOUND oder explicit stderr-Hint bei leerer Section + section_anchor set.

### LOW-2: Exit-Code-Test-Coverage-Gaps (partial-CLOSED)

Codex-Tabelle bemängelte uncovered Codes 3/4/6/8/10/99. CP18 schließt 8 (test_backup_restored_on_p7_sysexit). 4 ist bereits durch worked-example-A/B-EXIT-4-Verhalten covered (siehe `.gate3-pass`). Verbleibend für v0.1.1: 3 (audit-drift), 6 (backlink-hit fail-close), 10 (reference-mismatch — bereits XFAIL covered für AK3), 99 (Approach-Reset).

- **v0.1.1 TODO:** Dedicated Tests für 3/6/99 mit Force-Audit-Drift-Sentinel + Force-Backlink-Hit-Fixture + Force-Approach-Reset-Trigger.

---

## First-Practical-Test 2026-05-23 abends (B-1 log.md Date-Cut)

Erster echter Praxistest des promoted v0.1.0 Skills gegen Vault `log.md` (Pattern C Date-Cut, cut_before=2026-05-17, 86 entries archived / 29 keep, 507K → 167K). Exit 0, P0-P7 clean durchgelaufen. **7 v0.1.1-Backlog-Items aufgedeckt** durch Real-World-Anwendung — genau wofür Praxistests da sind.

### MEDIUM-9: Pattern C Bullet-List-Variante fehlt (deferred v0.1.1)

`SESSION-HANDOVER.md` hat Banner-Chronik als `- **Datum:** YYYY-MM-DD ...`-Bullet-Liste, nicht als `## YYYY-MM-DD`-Header. Aktuelle `classify_date_cut`-Mechanik (Z.284-307) baut Entries via Header-Regex-Split (`_split_into_entries`), unterstützt nur Header-Form. Bei naivem Pattern-Edit auf `- \*\*Datum:` würde Trailing-Content (Resume-Anweisung Z.16+) in den letzten Datum-Body kollabieren und mit-archiviert.

- **Mitigation v0.1:** Pattern C nur auf `## DATE`-Header-Files anwenden (log.md, sec-edgar-skill-history-style); SESSION-HANDOVER bleibt unrefactored bis v0.1.1.
- **v0.1.1 TODO:** Entweder `date_parser.mode: bullet` mit trailing-boundary-stop-pattern, oder neuer `Pattern D — banner-list-cut`.

### MEDIUM-10: Worked-Example-Real-State-Drift silent-failure (deferred v0.1.1)

`session-handover-date-cut.yaml` (CP9 7:08p) hatte Date-Regex `^## (\d{4}-\d{2}-\d{2})` — matched nur 6/111 Entries weil log.md zwischen Build-Time und First-Real-Run (24h später) neue `## [DATE]`-Bracket-Entries dazu bekam. P2-Classify klassifizierte 105 Bracket-Entries silent als pre-header-keep-Body, 86 archive-Entries enthielten falsche Trailing-Bracket-Bodies. **Kein Test detected** weil Build-Gates gegen frozen Build-Time-State liefen.

- **Mitigation v0.1.1 (Edit applied here, 2026-05-23):** Regex auf `^## \[?(\d{4}-\d{2}-\d{2})\]?` erweitert (covered beide Format-Varianten).
- **v0.1.1 TODO:** First-Class Date-Parser-Format-Flexibility — `\[?...\]?` als Default-Pattern statt Hand-Patch; oder empirischer Header-Count-Pre-Check (Codex-Vorschlag: parsed headers vs expected structure) der drift-Signal vor Mutation surfaced.

### MEDIUM-11: `fail_close_on_drift` semantischer Misnomer (deferred v0.1.1)

`core_slim_refactor.py` Z.112: `if r.returncode != 0 and cfg.audit.get("fail_close_on_drift", True)` — Code-Verhalten ist **any-nonzero-audit-fail-close**, nicht echte baseline-drift-vs-P8. Echte Drift-vs-Baseline-Logik (snapshot P0 vs snapshot P8 vergleichen, fail nur bei delta) ist nicht implementiert.

- **Mitigation v0.1 (Edit applied here, 2026-05-23):** Worked-Example-Config setzt `fail_close_on_drift: false` mit inline-Comment-Rationale; pre-existing audit-FAILs (in STATE.md last-audit-block dokumentiert) werden advisory akzeptiert.
- **v0.1.1 TODO:** Entweder Variable umbenennen auf `fail_close_on_any_nonzero` (ehrlicher), oder echte Baseline-Drift-Logik implementieren (snapshot-compare zwischen P0 + P8) und Variable behalten.

### MEDIUM-12: Pointer-Template `archive_link` zeigt absoluten Windows-Pfad als Display-Text (deferred v0.1.1)

Im Live-Run-Output (mutated log.md Z.6) lautet der Pointer-Header:
```
> **Pre-2026-05-17 Banner-History archived** -> [C:\Users\tobia\OneDrive\Desktop\Claude Stuff\05_Archiv\log-bis-2026-05-16-archiv.md](../../../05_Archiv/log-bis-2026-05-16-archiv.md)
```
URL-Teil (relativer Pfad) ist korrekt — Markdown-Reader öffnet ihn richtig. Display-Text-Teil (absoluter Windows-Pfad) ist visuell hässlich + nicht portable.

- **Mitigation v0.1:** Skill v0.1 funktional korrekt, nur visueller Display-Bug. Akzeptabel für First-Run.
- **v0.1.1 TODO:** Pointer-Template `{archive_link}`-Resolution sollte basename ODER relative-from-target-path liefern, nicht absolute path. Hotfix-Priorität HIGH (Vault-UX-Defect).

### MEDIUM-13: Backup-File `.pre-refactor.bak` nicht geschrieben (deferred v0.1.1)

SKILL.md L48 + `failure_modes.md` Z.37 dokumentieren explizit: `phase_p0` schreibt `shutil.copy(target, target.pre-refactor.bak)` als Atomicity-Guarantee-Foundation. Im Live-Run 2026-05-23 18:46:32Z **kein** Backup-File gefunden (verifiziert via `find . -name "log.md.pre-refactor.bak"`). Entweder Code-Path silent-skipped oder Cleanup zu früh.

- **Mitigation v0.1:** Run erfolgreich abgeschlossen (Exit 0), kein Rollback nötig — Backup-Fehlen kam nicht zum Tragen. Aber dokumentierte Atomicity-Garantie war faktisch broken.
- **v0.1.1 TODO:** Code-Pfad-Tracing: warum `_run_p0` Backup nicht erzeugte (vermutet: `--skip-audit`-Pfad oder Bedingungs-Logik-Bug). Hotfix-Priorität HIGH (broken-contract).

### MEDIUM-14: `executed:`-Block nicht auto-populated post-live-run (deferred v0.1.1)

Pattern-Specs L52-56 implizit-Erwartung: Post-Live-Run wird `executed: {timestamp, commit_sha, reference_archive_sha}` auto-geschrieben in Config (analog zu retro-doc-archived A+B configs). Empirisch im First-Live-Run **nicht passiert** — Config blieb `executed: null`. Re-Run ohne `--force-rerun` hätte naiv das Skill nochmal ausgeführt (kein Re-Run-Lock).

- **Mitigation v0.1 (Edit applied here, 2026-05-23):** `executed:`-Block manuell befüllt mit timestamp (aus archive-header) + sha256 (empirisch berechnet) + commit_sha=`TBD-post-commit` als follow-up-placeholder.
- **v0.1.1 TODO:** Skill schreibt Config-Update als post-P7-step (vor Skill-Exit), inkl. `commit_sha: pending` (User updated post-commit via follow-up-edit).

### MEDIUM-15: P3 Backlink-Scan ist term-only, semantischer Vault-Backlink-Graph fehlt (deferred v0.1.1)

`backlink_scan.search_terms` ist schmaler Termin-Set (z.B. `["log.md", "Banner-Entry"]`). Greift File-Pointer-Refs sauber, aber **semantische Cross-Links** auf archivierte Bodies (z.B. PIPELINE-#-Numbers, Anchor-Refs, Embed-Includes) werden nicht detected. Im 86-archive-Bodies-Bundle waren >100 PIPELINE-#-Refs (#26/#37/#42 etc.) die teils von anderen 00_Core-Files referenziert sein könnten — Risk silent broken backlinks.

- **Mitigation v0.1:** Vault-Konvention `[[wikilink]]` + Pipeline-`#`-Refs sind via git-grep auch nach Archive auffindbar (archive-files bleiben lokal). Akzeptiert für First-Run.
- **v0.1.1 TODO:** Breiterer `vault-backlink-graph-scan` als Option in `backlink_scan.mode: graph`; nutzt obsidian-bases oder regex-Graph-Build über alle `[[…]]` und `§\d+` und `#\d+`-Refs in scan_paths.

### LOW-3: Archived bodies enthalten Wikilinks → orphan-risk (akzeptiert)

Codex-Diff-Re-Review-Befund: Im Archive `log-bis-2026-05-16-archiv.md` sind `[[…]]`-Wikilinks (z.B. zu Vault-Entities AMZN/MSFT/etc.) enthalten. Nach Archive-Verschiebung sind Sources der Links (im post-mutated log.md) entfernt — orphan-Wikilink-Risiko in Obsidian-Graph-Layer.

- **Mitigation v0.1:** Archive bleibt local-only readable via direct-file-open; Wikilink-Targets selbst existieren weiter im Vault. Obsidian Graph-View zeigt evtl. orphan-cluster im Archive-File aber Links auflösen sauber zu existierenden Targets.
- **Akzeptierter Tradeoff:** Cost-Benefit klar pro Retention-Slim, contra Graph-Visual-Coherence — letzteres ist sekundär.

---

## v0.1.1 Hotfix-Priorisierung (Codex-Single-Pass-Vorschlag 2026-05-23 abends-spät + Test-Empirie-Update)

**Original-Codex-Empfehlung (3 Items):**

1. **HIGH — Pointer-Display-Text-Bug** (MEDIUM-12) — Vault-UX-Defect, portable across all future runs
2. **HIGH — Empirischer Header-Count-Pre-Check** (MEDIUM-10) — fängt silent worked-example-drift (Re-Klassifiziert zu v0.2.0 als Feature siehe PIPELINE #81)
3. **HIGH — Backup-Contract-Fix** (MEDIUM-13) — dokumentierte Atomicity-Garantie ist broken

**Test-Empirie-Update 2026-05-23 abends-spät (nach Pattern A+B `--dry-run --force-rerun` auf retro-doc Worked-Examples):**

4. **HIGH-3 (NEU promoted aus MEDIUM-11)** **MEDIUM-11 ist Skill-Adoption-Blocker**, nicht nur Misnomer. Empirische Bestätigung:
   - Pattern A `ruflo-sunset-bucket.yaml --dry-run --force-rerun` → **Exit 3 (EXIT_AUDIT)** (P0 blocked)
   - Pattern B `defcon-fat-rows-slim.yaml --dry-run --force-rerun` → **Exit 3 (EXIT_AUDIT)** (P0 blocked)
   - **Root-Cause:** alle 3 Worked-Examples haben `fail_close_on_drift: true` (Default), Code Z.112 prüft any-nonzero → auf jedem real Repo mit imperfekter Audit-State (dynastie-depot heute: 10/15 PASS — normal, nicht außergewöhnlich) failt P0 hart.
   - **Konsequenz:** Skill in v0.1.0 effektiv nicht nutzbar ohne Config-Patch. Adoption-Blocker für jeden New-User.
   - **Fix-Optionen:** (a) Default auf `false` (advisory) — schnellste Fix, oder (b) Variable-Rename auf `fail_close_on_any_nonzero` + Default `false` + Doku-Update — semantisch ehrlicher.
5. **MEDIUM-NEW (NEU promoted aus LOW-1)** **Diagnostic-Output bei P2 Classify-Fail.** Pattern A+B mit `--skip-audit` liefern nur `=== P2 Classify FAIL ===` ohne irgendeine Reason. By-design EXIT 4 (CORE-MEMORY §13 bereits geslimmt), aber User sieht das nicht.
   - **Fix-Empfehlung:** stderr-Hint mit Classify-Statistik (n_rows scanned, n_matches found, threshold/anchor used) bei Exit 4 + separater Exit-Code `EXIT_ANCHOR_NOT_FOUND` (5) vs `EXIT_CLASSIFY_EMPTY` (4).

**Updated v0.1.1 Bundle (5 Items, ~2-3h Aufwand):** HIGH-1 MED-12 + HIGH-2 MED-13 + HIGH-3 MED-11 + MEDIUM-NEW LOW-1-Promoted + optional MED-11-Variable-Rename (separat oder mit HIGH-3 gebundled).

**v0.2.0 Feature-Items (unverändert):** MEDIUM-9 SH-Bullet-Adapter, MEDIUM-10 Header-Count-Pre-Check, MEDIUM-14 executed-Auto-Populate, MEDIUM-15 Backlink-Graph.

**Karpathy-Reflection (Test-Empirie):** User-Vorschlag "weitere Tests" hat 3 substantielle neue Befunde geliefert in 15 min Aufwand: (a) Vault-Survey 0 weitere Pattern-C-Targets → strategischer Befund v0.2.0-Bedarf, (b) MED-11 ist Adoption-Blocker → HIGH-Promote, (c) LOW-1 ist HIGH-Promote-Kandidat → MEDIUM-Promote. Empirie > Annahme bestätigt.

---

## Cross-Reference

- Spec §4 Error-Handling (full text): `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` lines 372-454
- Codex-R1 Review (Wave-5-Break-2): commit a0dc16d log + R1-result transcript
- Codex-CP18-Review (Wave-7-Break-4, 2026-05-23): 3 HIGH (all CLOSED via diff-bundle) + 5 MEDIUM (2 CLOSED inline / 3 deferred v0.1.1) + 2 LOW (deferred v0.1.1)
- Codex-First-Practical-Test-Review (2026-05-23 abends, agent a22827a45aff160a0): 7 v0.1.1 backlog items confirmed, 0 HIGH blockers post-edit
- Karpathy Approach-Reset: `00_Core/INSTRUKTIONEN.md §0`
