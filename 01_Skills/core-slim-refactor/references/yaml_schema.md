# YAML Config Schema — core-slim-refactor v0.1

Vollständiges Schema siehe `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` Sektion 2.2 (lines 146-281). Dieser Doc ist Quick-Reference + Backlink-Term-Enumeration-Checklist (OQ7 resolution).

---

## Top-Level Felder (Required)

| Feld | Typ | Beschreibung |
|---|---|---|
| `schema_version` | int | Aktuell `1`. |
| `profile_name` | string | Kebab-case identifier; landet in Codex hand-off bundle + Commit-Msg-Template. |
| `target` | object | Target file + section + immutability. |
| `pattern` | enum | Einer von `bucket-archive`, `slim-convention`, `date-cut`. |
| `<pattern>_block` | object | Pattern-spezifischer Block. Mutual-exclusion via `_check_mutual_exclusion`. |
| `backlink_scan` | object | P3 PFLICHT-Phase Konfiguration. |
| `audit` | object | P0/P8 audit-wrapping config. |
| `retry_policy` | object | Karpathy Approach-Reset-Schwelle config. |

## Top-Level Felder (Optional)

| Feld | Typ | Beschreibung |
|---|---|---|
| `executed` | object \| null | Wenn populated (3 sub-fields all non-null: `timestamp`, `commit_sha`, `reference_archive_sha`) blockt P1 Re-Run außer `--force-rerun`. Für retroaktive Doku-Configs. |

## Target

```yaml
target:
  file: "00_Core/CORE-MEMORY.md"          # relative to repo-root
  section: "## 13. Lifecycle-History"     # exact header-match; null = whole-file
  section_anchor_alt: null                # reserved for v0.2
  append_only_immutable: false            # if true → pattern MUST be date-cut
```

**Constraint (Codex-R1 HIGH-2):** `pattern=date-cut` erfordert `section: null` (wholesale-archive Semantik). Sonst → `ConfigError`.

## Pattern-Block Details

Pro Pattern siehe `references/configs/*.yaml` für vollständige Beispiele. Die 3 worked-examples decken alle erlaubten Felder ab.

## Backlink-Scan

```yaml
backlink_scan:
  scan_paths:
    - "00_Core/"
    - "CLAUDE.md"
    - "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/"
  search_terms:                # see Checklist below
    - "§13"
    - "§ 13"
    - "§13.X"
    - "section 13"
  on_match: fail_close         # fail_close (default) | warn_continue | skip_if_override
  skip_override_allowed: false # required true if on_match=fail_close + bypass needed
```

## Audit + Retry

```yaml
audit:
  pre_run: true                    # gate P0 with system_audit.py --core
  pre_run_pass_threshold: pass     # currently informational
  post_run_hint: true              # P7 prints post_audit_cmd
  fail_close_on_drift: true        # P0 fails closed on drift

retry_policy:
  max_identical_phase_failures: 2  # Karpathy 2-fail-stop
  identity_key: ["phase", "exception_class"]
```

---

## Backlink-Term-Enumeration-Checklist (OQ7 Resolution)

Pflicht-Checkliste pro Config-Author: für jedes §-Symbol das du in `search_terms:` einträgst, prüfe alle 4 Varianten:

| Variante | Beispiel | Erforderlich? |
|---|---|---|
| Kompakt | `§13` | YES — Default |
| Mit Leerzeichen | `§ 13` | YES — Common typing-variant |
| Sub-Nummerierung | `§13.1`, `§13.2`, etc. | YES if section has sub-numbers |
| English | `section 13` | YES if vault/docs use English |

Skill validiert NICHT automatisch (Karpathy Surgical-Changes — no auto-expand in code). Build-Gate-3 prüft per doc-existence-grep dass diese Checkliste in `yaml_schema.md` vorhanden ist.

---

## Known v0.1 Schema-Gaps (Codex-R1 MEDIUM-2, deferred)

- **Nested-Key Validation fehlt:** Schema-Validate prüft nur Top-Level + Pattern-Mutex + Executed-Field + Append-Only-Flag + Date-Cut-Section-Null. Missing nested keys wie `backlink_scan.scan_paths`, `<pattern_block>.archive.path` oder pointer-template-keys schlagen erst zur Runtime als `KeyError` durch (nicht als `ConfigError`).
- **Mitigation v0.1:** Bei Schema-Fehlern den Pattern-Block gegen das nächstgelegene worked-example unter `references/configs/` diffen — die 3 Worked-Examples decken alle erlaubten Felder ab.
- **v0.1.1 TODO:** Pattern-Block Pflicht-Key-Liste hinzufügen.

## Known v0.1 Path-Safety-Gap (Codex-R1 MEDIUM-3, deferred)

- **Archive-Path-Boundary fehlt:** Skill akzeptiert beliebige absolute oder relative `archive.path`-Werte (z.B. `C:/tmp/somewhere/foo.md` oder `../../outside-repo/x.md`). Discipline-Pflicht (SKILL.md §4 "Archive-Local-Only") wird NICHT erzwungen — nur per Config-Author-Disziplin.
- **Mitigation v0.1:** Pre-Commit-Review der Config + P7-Hand-Off-Bundle zeigt absolute Archive-Pfad.
- **v0.1.1 TODO:** Erzwingen dass resolved archive-path unter `repo_root / "05_Archiv/"` liegt.
