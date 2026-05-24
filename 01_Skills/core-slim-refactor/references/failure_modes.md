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

### MEDIUM-13: Backup-File `.pre-refactor.bak` Lifecycle (RESOLVED v0.1.1 — kein Code-Bug)

**Ursprüngliche Beobachtung (2026-05-23 18:46:32Z):** Post-Run `find . -name "log.md.pre-refactor.bak"` ergab leer; vermutet als broken Atomicity-Contract.

**Phase-1-Diagnose (v0.1.1, 2026-05-23 spätabends):** Kein Code-Bug. Backup-Lifecycle ist by-design:

1. `phase_p0` L98-99: `if not args.dry_run: shutil.copy2(target, backup_path)` — `--dry-run` skipt Backup-Erstellung by-design (dokumentiert in SKILL.md "P0 simulated, no file-writes").
2. `main` L510: `_cleanup_backup_on_success(baseline)` — bei erfolgreichem Run (P7-OK + exit 0) wird Backup gelöscht. Atomicity gilt nur während Run-Window P0→P7-OK; nach erfolgreichem Exit ist Backup gewollt weg (kein orphan-File neben target.md, kein commit-pollution).
3. Bei Failure ab P5 wird via `_restore_backup` aus Backup re-instantiated, dann re-raise — Backup bleibt für post-mortem stehen (NICHT cleanup'd on failure-path).

**Empirisch validiert via Python 3.14.3:** `Path("X.md").with_suffix(".md.pre-refactor.bak")` → `X.md.pre-refactor.bak` (korrekt). `.gitignore` L35 `*.pre-refactor.bak` filtert vom commit (verifiziert).

**v0.1.1 Action:** Doku-Klarstellung (dieser Eintrag) + Lifecycle-Regression-Tests in `tests/test_v0_1_1_bugfixes.py` (`test_high2_backup_skipped_in_dry_run`, `test_high2_backup_created_in_non_dry_run`). **Kein Code-Touch.**

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
6. **HIGH-4 (NEU promoted 2026-05-23 ~22:25 via Cross-Check-Discovery + Codex-Re-Audit ~22:38, agent `ae2e863dc1869630a`)** **Subprocess-Capture UTF-8-Crash an P0 (L104-111) UND P7 (L349-357) — selber Patch, 2 Sites.** `subprocess.run([...], capture_output=True, text=True)` ohne explizites `encoding` → Windows-Default cp1252 → Reader-Thread `UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d` bei UTF-8-Bytes (system_audit-Output enthält z.B. `§`-Pfade aus PIPELINE.md:75). Folge-Crash: `r.stdout=None` aber Zeile 111/357 macht `sys.stdout.write(r.stdout)` ohne None-Guard → `TypeError: write() argument must be str, not None`.
   - **Reproduktion (deterministisch):** `python 01_Skills/core-slim-refactor/scripts/core_slim_refactor.py 01_Skills/core-slim-refactor/references/configs/session-handover-date-cut.yaml --dry-run --force-rerun` — auf jedem realen 00_Core-Refactor mit non-ASCII-Findings im Audit-Output.
   - **Konsequenz:** Skill-Adoption-Blocker für jeden 00_Core-Slim-Refactor — standalone `system_audit.py --core` läuft sauber, aber Skill-P0-Pfad crasht im Reader-Thread.
   - **Fix-Empfehlung:** `encoding='utf-8', errors='replace', timeout=30` + `sys.stdout.write(r.stdout or '')` + `sys.stderr.write(r.stderr or '')` an beiden Sites identisch.
   - **Memory-Reinfall-Klasse:** `feedback_windows_console_ascii_safe_inline_python` + `feedback_windows_python_crlf_text_mode` — beide warnen vor genau diesem Anti-Pattern.
   - **TDD-Tests für v0.1.1 (Codex Q5):** (1) None-Guard Mock `subprocess.run` mit `stdout=None` in P0/P7 → kein TypeError, (2) Windows-Locale-Sim mit cp1252-failing-aber-UTF-8-valid Bytes-Fixture → Phase crasht nicht, (3) Integration-Test P0 mit non-ASCII (`§`, Umlaute) → stabiler Exit-Code.
   - **First-Real-Run-Gap-Diagnose:** Vault `log.md`-Scope hatte vermutlich ASCII-only Audit-Output ODER `cfg.audit.pre_run=false` umgangen P0-Capture-Pfad — Locale-Decode-Failure nie ausgelöst.

**Codex-FALSE-POSITIVE 2026-05-23 ~22:38 (Reinfall-Doku, NICHT in v0.1.1 reagieren):** Codex flagte `except A, B:` (L65/491/498/504) als "Python-2-Syntax-Bug" — **falsch**, valide Python 3.14 per **PEP 758** (akzeptiert für 3.14, klammerlose Tuple-Form), `ast.parse` bestätigt SyntaxValid:OK. Identischer Reinfall wie CP3 paragraph-18-sync 2026-05-22 (Memory `feedback_pre_commit_diff_inspection` PEP-758-Codex-Misread). v0.1.1-Build überspringt diese 4 Findings explizit.

**Codex-MEDIUMs defer v0.1.2/v0.2.0 (Karpathy 2-Phase Bugfix-only):** (a) `_repo_root()` text=True ohne encoding (L58-63) — latent, nur bei non-ASCII Repo-Pfad; (b) Direct-Write statt `os.replace()`-atomic (L238-239 P4 + L298-299 P5) — architektural-Improvement, Backup-Logik schützt bereits.

**Updated v0.1.1 Bundle (6 Items, ~2.5-3.5h Aufwand):** HIGH-1 MED-12 + HIGH-2 MED-13 + HIGH-3 MED-11 + HIGH-4 NEU-Subprocess-UTF-8 (P0+P7 1 Patch 2 Sites) + MEDIUM-NEW LOW-1-Promoted + optional MED-11-Variable-Rename (separat oder mit HIGH-3 gebundled).

**v0.2.0 Feature-Items (unverändert):** MEDIUM-9 SH-Bullet-Adapter, MEDIUM-10 Header-Count-Pre-Check, MEDIUM-14 executed-Auto-Populate, MEDIUM-15 Backlink-Graph.

**Karpathy-Reflection (Test-Empirie):** User-Vorschlag "weitere Tests" hat 3 substantielle neue Befunde geliefert in 15 min Aufwand: (a) Vault-Survey 0 weitere Pattern-C-Targets → strategischer Befund v0.2.0-Bedarf, (b) MED-11 ist Adoption-Blocker → HIGH-Promote, (c) LOW-1 ist HIGH-Promote-Kandidat → MEDIUM-Promote. Empirie > Annahme bestätigt.

---

## v0.1.2 Hotfix (2026-05-24, post-T2-Empirie)

### HIGH-1 v0.1.2: P7 §18-Skill-Gate Path-Mismatch (CLOSED)

T2-Empirie 2026-05-24 (commit `359c296`) hat aufgedeckt: P7 sondiert nur `01_Skills/paragraph-18-sync/scripts/p18_sync.py` (Spec-Stub, nie gelandet) und PATH-bare `paragraph-18-sync` (nicht installiert). Real-Validator lebt seit 2026-05-22 unter `03_Tools/para18_sync/validator.py` — beide pre-fix Sondierungs-Pfade missen ihn. FileNotFoundError-Branch loggte nur `WARNING: ... skipping §18-gate` und kehrte zurück → silent-skip-by-design-violation gegen SKILL.md §4-Discipline-#5 ("fail-close on any §18-gate failure"). Operative Runs hätten gegen broken Sync-State commiten können.

- **Fix:** Pure-Function `_resolve_p18_command(repo_root)` mit 3-Step-Probe (real path PRIMARY, legacy alias forward-compat, PATH-bare fallback). FileNotFoundError → `SystemExit(EXIT_GATE_FAIL=8)` (kein silent-skip mehr).
- **Test:** `tests/test_v0_1_2_bugfixes.py::test_real_validator_picked_when_present` + `test_legacy_alias_used_when_only_legacy_present` + `test_real_validator_preferred_over_legacy` + `test_bare_path_fallback_when_neither_present`.
- **Memory:** `feedback_core_slim_p7_p18_path_mismatch.md`.

### MEDIUM-2 v0.1.2: Pointer-Placement footer-blind Fallback (CLOSED)

T2-Empirie sichtbar in CORE-MEMORY.md L425 — Pointer landete POST-Footer-Bullet statt davor. Root-Cause: chronological-Fallback (line 139-147) und section_bottom-Mode (line 156-161) appendeten Pointer unbedingt am Section-Ende ohne Footer-Erkennung. `dt > pointer_date` Bedingung im Main-Loop firet selten (alle kept-rows pre-today) → Fallback ist Default-Path.

- **Fix:** Neuer Helper `_insert_after_last_table_row(lines, pointer_row)` in `patterns.py` walks backwards, findet last `_is_table_row` Index, inseriert Pointer immediately after. 2 Call-Sites refactored. Pre-Fix-Trailing-Blank-Pop/Append-Logik entfernt (auch Beitrag zur Reflow-Noise).
- **Test:** `tests/test_v0_1_2_bugfixes.py::test_pointer_inserted_before_footer_bullet` + 3 weitere edge-case tests.
- **Sentinel-Note:** `pointer_context.get("pointer_date", "9999-99-99")` Fallback in `patterns.py:120` bleibt unverändert — `_build_pointer_context` setzt pointer_date immer, Sentinel würde nur bei externem caller-Bug feuern.

### Test/Dev Escape-Hatch: `CORE_SLIM_REFACTOR_SKIP_GATE` (NEU)

Hinzugefügt analog `CORE_SLIM_REFACTOR_FORCE_FAIL_PHASE`. Bypasst P7 vor Validator-Probe (`_emit_phase("P7 Hybrid-Gate", "SKIP")`) für Test-Isolation und Dev-Iteration. Operative Runs setzen das nie. **Side-Effect:** SKIP-Mode emittiert KEIN Codex-Hand-off-Bundle auf stdout (Skill kehrt vor Bundle-Print zurück) — intentional, Tests/Dev brauchen es nicht.

### MEDIUM-16 v0.1.2: Section-Reflow selective splice (deferred v0.2.0)

T2-Empirie-Test #2 §13 Lifecycle produzierte Diff -32/+7 vs erwartet -26/+1. Extra +6 = Whitespace/Footer-Re-Layout-Noise aus `_iter_section_rows` + `split("\n")/"\n".join(...)`-Mutation-Pipeline. Mathematisch korrekt, kein Datenverlust — reine Diff-Optik. MEDIUM-2-Fix entfernte einen Teil (Trailing-Blank-Pop/Append). Rest wäre algorithmischer Refactor von `mutate_bucket_archive` (split-rebuild → position-based-splice). Out-of-Scope für v0.1.2-Bugfix per Karpathy §0.6 Approach-Reset (Pre-Implementation-Abort).

- **Defer:** v0.2.0 Build-Phase, additiv zu MEDIUM-9/10/14 Pre-Lock.
- **Risk:** Diff-Optic-Only — kein Operational-Impact.

### Codex Single-Pass Review v0.1.2 (2026-05-24 ~15:40)

PASS-WITH-NOTES. 0 HIGH, 0 MEDIUM-blockers. 2 LOW Findings: (1) SKIP-Mode Bundle-Print intentional, in SKILL.md klargestellt (commit dieser Welle); (2) `repo_root` Defensive-Type-Guard nicht implementiert per Karpathy §0.2 (`_repo_root()` returnt immer Path, Defensive für unmögliches Szenario). Single-Pass war ausreichend per `feedback_codex_sparring_heuristic.md` (kein Sparring-Trigger).

---

## Cross-Reference

- Spec §4 Error-Handling (full text): `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` lines 372-454
- Codex-R1 Review (Wave-5-Break-2): commit a0dc16d log + R1-result transcript
- Codex-CP18-Review (Wave-7-Break-4, 2026-05-23): 3 HIGH (all CLOSED via diff-bundle) + 5 MEDIUM (2 CLOSED inline / 3 deferred v0.1.1) + 2 LOW (deferred v0.1.1)
- Codex-First-Practical-Test-Review (2026-05-23 abends, agent a22827a45aff160a0): 7 v0.1.1 backlog items confirmed, 0 HIGH blockers post-edit
- Codex-Re-Audit (2026-05-23 ~22:38 post-Cross-Check-Discovery, agent ae2e863dc1869630a, gpt-5.3-codex single-pass): 4 HIGH reported → final 3 valide (HIGH-1 confirmed L264-276, HIGH-4 NEU P0+P7 Subprocess-UTF-8) + 1 PEP-758-FP (Memory `feedback_pre_commit_diff_inspection`) + 2 MEDIUM defer v0.2.0
- Memory-Reinfall-Klassen für HIGH-4: `feedback_windows_console_ascii_safe_inline_python` + `feedback_windows_python_crlf_text_mode`
- Karpathy Approach-Reset: `00_Core/INSTRUKTIONEN.md §0`

---

## v0.2.0 Feature-Release (2026-05-24) - CLOSED Items

### MEDIUM-9 - CLOSED v0.2.0

Resolution: Pattern-C `_split_bullet_block`-Helper + `classify_date_cut` field-branching.
Worked-Example: `references/configs/session-handover-banner-list-cut.yaml`.

### MEDIUM-10 - CLOSED v0.2.0

Resolution: P2a Drift-Pre-Check zwischen P2 und P3 (`expected_entry_count` + `on_drift`).
Default `warn_continue` (Q3-Verdict); Structured stderr-Code `DRIFT_COUNT_OUT_OF_RANGE`.
Exit-Code 12 `EXIT_DRIFT_DETECTED` bei `on_drift: fail_close`.

### MEDIUM-14 - CLOSED v0.2.0

Resolution: P7b Auto-Populate-Phase post-P7-success. Atomic-Rename via `os.replace`.
Bei IO-Failure: Sidecar-Lock `<cfg>.executed-pending` + Exit-Code 13 `EXIT_BOOKKEEPING_FAILED`.
CLI-Flag `--skip-executed-writeback` fur v0.1.x-1:1-Compat (R3-3 Spec).
**v0.2.0-Limitation:** PyYAML strippt Comments (Q1-Verdict accepted; ruamel.yaml v0.3-TODO).

### MEDIUM-16 - CLOSED v0.2.0

Resolution: `_splice_section` + `_build_line_byte_offsets` Helper; `mutate_bucket_archive`
refactored auf splice statt list-rebuild. Line-Alignment-Invariante eliminiert intra-grapheme-split.
Diff-Stabilitat: T2-§13-Replay liefert EXACT -26/+1 (vs v0.1.2 -32/+7).
**v0.2.0-Limitation:** Intra-line-Edits sind explizit out-of-scope (wurden `unicodedata.normalize`
+ grapheme-iterator brauchen; v0.3-Item falls Bedarf entsteht).
**AC5-Note:** Replay-Diff ist -26/+1 byte-identisch zu v0.1.1-Expected; MEDIUM-16-Bug war
Pointer-Placement (post-Footer vs pre-Footer), nicht Line-Count-Delta.

### Exit-Codes v0.2.0 (Erganzung)

| Code | Phase | Symptom | Recovery |
|---|---|---|---|
| 12 | P2a | EXIT_DRIFT_DETECTED - count mismatch bei `on_drift: fail_close` | regex-Update, Worked-Example refreshen, ODER `on_drift: warn_continue` setzen |
| 13 | P7b | EXIT_BOOKKEEPING_FAILED - YAML-Write-Back IO-Error | Sidecar-Lock-Inhalt manuell in YAML ubernehmen + Sidecar loschen, ODER `--force-rerun` mit existing Sidecar als explicit Operator-Ack |

### Unicode-Boundary-Garantie (F-05)

`_splice_section` aborted via `AssertionError("splice_boundary_not_line_aligned")` bei
non-line-aligned start/end-Bytes. Markdown-Mutationen operieren NIE intra-line in v0.2.0.
Grapheme-Cluster (ZWJ-Emoji, combining marks, Flag-Pair) bleiben intakt.

### Q1 PyYAML-Comment-Loss bei executed-Write-Back

Akzeptiert fur v0.2.0. Workaround: User-Konfigs mit Inline-Comments sollten `executed:`-Block
am File-Ende halten (keine Comments unterhalb). v0.3-Item: ruamel.yaml-Migration fur Comment-Preservation.

### Q4 Header-Mode-Regression-Test

Header-Mode-Configs (`field: header` oder field weglassen) liefern byte-identische Output
gegen v0.1.x - verifiziert via AC1d + Worked-Example-Regression-Suite (`ruflo-sunset-bucket.yaml`,
`defcon-fat-rows-slim.yaml`, log.md historische Date-Cuts).
