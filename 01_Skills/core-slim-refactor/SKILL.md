---
name: core-slim-refactor
description: YAML-driven 8-Phase Markdown-Section-Refactor pipeline. Use when slimming SSoT-Files via Bucket-Archive (semantic row-cluster archival), Slim-Convention (fat-row compression with verbatim archive), or Date-Cut (banner/chronicle pre-cut archival). Activates on triggers !SlimRefactor <config>, "core-slim-refactor", or explicit config-path-mention.
version: 0.2.0
---

# core-slim-refactor v0.2.0 — Markdown-Section-Refactor Skill

## When to use

Activate when slimming a single SSoT-Markdown file via one of 3 empirisch-validierte Pattern. NOT for arbitrary text-edit, NOT for multi-file refactor (v0.2 boundary), NOT for code-files.

| Pattern | Use-Case | Worked-Example |
|---|---|---|
| **A — Bucket-Archive** | Semantic row-cluster (Ruflo-Sunset, MCP-Setup) out-of-band archive + 1 chronological pointer-entry | `references/configs/ruflo-sunset-bucket.yaml` |
| **B — Slim-Convention** | Fat-Rows > threshold (default 3500b) in-place compressed to Bold-Title + ~280-char-Outcome + pointer-tail | `references/configs/defcon-fat-rows-slim.yaml` |
| **C — Date-Cut** | Banner/Chronicle pre-cut wholesale archive + date-boundary-header | `references/configs/session-handover-date-cut.yaml` |

### Pattern-C: Date-Cut Modi (v0.2.0)

- `field: header` (Default, backward-compat zu v0.1.x) — Entries via `^## DATE`-Header-Split
- `field: bullet` (NEU v0.2.0) — Entries via `^- **Datum:** DATE`-Bullet-Liste; benoetigt `trailing_boundary` (z.B. `^## `) um Boundary zur Trailing-Content zu definieren

Siehe `references/configs/session-handover-banner-list-cut.yaml` fur Bullet-Worked-Example.
Compat-Matrix (v0.1.x vs v0.2.0): `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-design.md` §11.

## Invocation

```bash
python 01_Skills/core-slim-refactor/scripts/core_slim_refactor.py <config.yaml> [--dry-run] [--skip-audit] [--force-rerun]
```

**Flags:**
- `--dry-run` — P0-P7 simuliert (no file-writes). Output byte-genau dem live-run-delta.
- `--skip-audit` — Skip P0 audit ONLY. NEVER skips P3 Backlink-Scan. NOT erlaubt in operativen Runs (Karpathy).
- `--force-rerun` — Override `executed:` field guard (re-run post-hoc-documentation configs).
- `--skip-executed-writeback` (NEU v0.2.0) — Skippt P7b executed-Block-Auto-Populate komplett; Config bleibt unveraendert. Verwendung: v0.1.x-Config-1:1-Compat (§11.3) + CI-Pipelines die executed-Block manuell verwalten. Dry-run-Interaktion: `--dry-run` skippt Write-Back ohnehin (F-01-Invariante); `--skip-executed-writeback` ist expliziter Opt-out auch bei live-runs. NICHT kombinieren mit operativer Nutzung — Re-Run-Lock greift nicht wenn executed-Block null bleibt.

**P3 Backlink-Scan ist NICHT CLI-bypassable** — Bypass nur via YAML (`on_match != fail_close` AND `skip_override_allowed: true`), wird in stdout als WARNING geloggt.

## 8 Pflicht-Disziplinen (Karpathy + project-memory)

1. **Migrate-before-Strip** (P2): to-archive RowSet darf KEINE semantic-tags unique-haben die in to-keep fehlen — fail-close mit diagnostic.
2. **Pointer-Stub** (P5/P6): jede Mutation hinterlässt mindestens 1 Pointer-Eintrag (chronologisch oder boundary-header).
3. **Backlink-Scan** (P3): grep `search_terms` in `scan_paths`, fail-close default; bypass nur via 2-stufige YAML-Override (`on_match` + `skip_override_allowed`).
4. **Archive-Local-Only**: archives in `05_Archiv/`, niemals cloud-synced (Memory `reference_no_cloud_sync_onedrive_inactive`).
5. **§18-Skill-Gate** (P7): inline `<validator> system-zustand --dry-run --json` subprocess; fail-close on PASS!=PASS. **Validator-Probe-Reihenfolge (v0.1.2 HIGH-1):** (1) `03_Tools/para18_sync/validator.py` (real path) → (2) `01_Skills/paragraph-18-sync/scripts/p18_sync.py` (legacy alias, forward-compat) → (3) PATH-bare `paragraph-18-sync`. **Fail-close auch bei FileNotFoundError** (alle 3 Kandidaten missing) → SystemExit(EXIT_GATE_FAIL=8); pre-v0.1.2 silent-WARNING-skip war §4-Discipline-#5-Verstoß (T2-Empirie 2026-05-24, `feedback_core_slim_p7_p18_path_mismatch`). **P0/P7 subprocess calls pin `encoding="utf-8", errors="replace"`** (v0.1.1 HIGH-4) — Windows-cp1252 decode-crash auf UTF-8-Audit-Output ist damit ausgeschlossen. **Test/Dev escape-hatch:** `CORE_SLIM_REFACTOR_SKIP_GATE=1` env-var bypasst P7 vor Validator-Probe (Convention analog `CORE_SLIM_REFACTOR_FORCE_FAIL_PHASE`); operative Runs setzen das niemals. **SKIP-Mode-Side-Effect:** im SKIP-Pfad wird auch das Codex-Hand-off-Bundle (target/backup/baseline_sha/commit_msg_template) NICHT auf stdout emittiert — Skill kehrt nach `_emit_phase("P7 Hybrid-Gate", "SKIP")` direkt zurück. Das ist intentional (Tests/Dev brauchen das Bundle nicht); operative Runs erhalten es regulär da SKIP_GATE dort nie gesetzt ist.

**`audit.fail_close_on_drift` Default (v0.1.1):** `false` (advisory). Audit-Drift wird auf stderr emittiert, P0 läuft weiter. Opt-in via YAML `audit.fail_close_on_drift: true` für strict-mode (z.B. CI-Pipeline). Default-Flip war HIGH-3 Adoption-Blocker — auf real-Repos mit 10/15-PASS-Audit-State würde true-Default jeden Run abbrechen.
6. **Codex-Pass** (P7-out-of-skill): Skill druckt Pre-Commit-Bundle (diff-path + commit-msg-template + post-audit-cmd); User triggert Codex Single-Pass manuell per `/codex:codex-rescue` mit diff (Memory `feedback_review_via_codex_not_advisor`).
7. **CRLF/UTF-8-Hygiene**: ALL file-IO `open(..., newline="")`; `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` als Header (Memory `feedback_windows_python_crlf_text_mode` + `feedback_windows_console_ascii_safe_inline_python`).
8. **Atomic-Commit**: target + archive + (.gitignore-updated *.pre-refactor.bak excluded from commit) in 1 git-Commit; pre-commit-Hooks bestehen (Karpathy: never skip).

## Phase-DAG (P0-P8)

| Phase | Action | Output |
|---|---|---|
| **P0** | Pre-Audit-Baseline (`system_audit.py --core` + target SHA + byte-count + `shutil.copy(target, target.pre-refactor.bak)`) | baseline-snapshot |
| **P1** | YAML-load + schema-validate + `executed:` guard | ConfigObject |
| **P2** | Classify pattern-dispatched + Migrate-before-Strip Diff-Check | RowSet {archive, keep, slim_targets} |
| **P3** | Backlink-Scan (PFLICHT, fail-close default) | BacklinkReport |
| **P4** | Archive-Write (verbatim, pattern-dispatched) | `<archive>.md` |
| **P5** | Source-Mutation (replace-rule per pattern) | target.md modifiziert |
| **P6** | Pointer/Header-Prose Updates | target.md final |
| **P7** | Hybrid-Gate: inline `paragraph-18-sync system-zustand --dry-run --json` + Codex-hand-off-bundle stdout | Pre-Commit-Bundle |
| **P8** | (manual, post-commit) `system_audit.py --core` Drift-Sanity vs P0-Baseline | audit-pass-confirmation |

Skill-internes exec endet bei P7. P8 ist User-Post-Action; Skill druckt cmd-template.

## Exit-Codes

| Code | Klasse |
|---|---|
| 0 | Successful P7-completion |
| 2 | Config-Schema-Error (P1) |
| 3 | Audit-Drift (P0) |
| 4 | Classification-Empty (P2) |
| 5 | Migrate-before-Strip-Violation (P2) |
| 6 | Backlink-Hit (P3) |
| 7 | File-Write-Error (P4/P5/P6) |
| 8 | §18-Skill-Gate-Fail (P7) |
| 10 | Reference-Archive-Mismatch (CP14 gate) |
| 11 | Anchor-Not-Found (P2) — `cfg.target.section` configured but absent in target |
| 12 | Drift-Detected (P2a) — `expected_entry_count` mismatch bei `on_drift: fail_close` (NEU v0.2.0) |
| 13 | Bookkeeping-Failed (P7b) — executed-Block YAML-Write-Back IO-Error; Sidecar-Lock geschrieben (NEU v0.2.0) |
| 99 | Approach-Reset-Triggered (Karpathy 2-Fail-Stop) |

## Reference-Files

- `references/pattern_specs.md` — 3 Pattern-Definitionen + Known-Pitfalls
- `references/yaml_schema.md` — Full config-schema + Backlink-Term-Enumeration-Checklist
- `references/failure_modes.md` — Phase-Failure-Klassifikation + Recovery (inkl. v0.2.0 CLOSED-Items + Exit-Codes 12/13)
- `references/configs/*.yaml` — Worked-Examples: A (Bucket-Archive retro), B (Slim-Convention retro), C header-mode (executable), C bullet-mode (session-handover-banner-list-cut.yaml NEU v0.2.0)
- `tests/test_v0_2_0_compat_matrix.py` — v0.1.x vs v0.2.0 Compat-Matrix-Tests (Spec SS11)
- Compat-Matrix Spec §11: `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-design.md` §11
