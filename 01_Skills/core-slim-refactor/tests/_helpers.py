"""Test helpers for core-slim-refactor v0.2.0 tests.

EMPIRISCH VERIFIZIERT 2026-05-24: Helper erzeugt vollstaendige Required-Fields-Configs
(alle 7 _REQUIRED_TOP Felder) gegen real scripts/config.py.

Disziplin-Regel #4: ALLE neuen v0.2.0-Test-Fixtures muessen diesen Helper verwenden.
Inline-YAMLs ohne Required-Fields failen an _check_required_fields VOR neuen Gates.
"""

from __future__ import annotations

from pathlib import Path


def make_minimal_valid_cfg_yaml(
    tmp_path: Path,
    target_path: Path,
    archive_path: Path,
    *,
    schema_version: int = 1,
    profile_name: str = "test-profile",
    cut_before: str = "2026-05-17",
    field: str = "header",
    bullet_regex: str | None = None,
    trailing_boundary: str | None = None,
    expected_entry_count: dict | None = None,
    executed: dict | None = None,
    commit_sha: str | None = None,
    _force_invalid_combo: dict | None = None,
) -> Path:
    """Erzeugt vollstaendige Required-Fields-Config fuer Tests.

    Baut YAML line-by-line statt textwrap.dedent (dedent failt bei multi-line
    Substitutionen mit gemischter Indentation -- empirisch verifiziert).

    _force_invalid_combo: dict mit key->value-Paaren die nach Helper-Erzeugung
    in den YAML-Text injiziert werden. Ermoeglicht intentional-broken Fixtures
    fuer Validation-Error-Tests (z.B. trailing_boundary bei field=header).
    Format: {"date_parser_trailing_boundary": "^## "} injiziert trailing_boundary
    unter date_parser (nach der letzten date_parser-Zeile).
    Wenn gesetzt, werden helper-seitige Pre-Checks fuer bullet_regex/trailing_boundary
    uebersprungen.
    """
    # Pre-Checks nur wenn kein force_invalid_combo
    if (
        _force_invalid_combo is None
        and field == "bullet"
        and (not bullet_regex or not trailing_boundary)
    ):
        raise ValueError("bullet field requires bullet_regex + trailing_boundary")

    lines: list[str] = []
    lines.append(f"schema_version: {schema_version}")
    lines.append(f"profile_name: {profile_name}")
    lines.append("target:")
    lines.append(f'  file: "{target_path.as_posix()}"')
    lines.append("  section: null")
    lines.append("  section_anchor_alt: null")
    lines.append("  append_only_immutable: false")
    lines.append("pattern: date-cut")
    lines.append("date_cut:")
    lines.append(f'  cut_before: "{cut_before}"')
    lines.append("  date_parser:")
    if field == "header":
        lines.append("    field: header")
        lines.append(r'    pattern: "^## \\[?(\\d{4}-\\d{2}-\\d{2})\\]?"')
        if _force_invalid_combo and "date_parser_trailing_boundary" in _force_invalid_combo:
            lines.append(
                f"    trailing_boundary: '{_force_invalid_combo['date_parser_trailing_boundary']}'"
            )
    elif field == "bullet":
        lines.append("    field: bullet")
        if bullet_regex:
            lines.append(f"    pattern: '{bullet_regex}'")
        if trailing_boundary:
            lines.append(f"    trailing_boundary: '{trailing_boundary}'")
        # _force_invalid_combo can omit trailing_boundary by not passing it
    else:
        # Edge-Case-Tests koennen field=footer o.ae. setzen, um Validation-Error zu provozieren.
        lines.append(f"    field: {field}")
        lines.append('    pattern: "x"')
    lines.append("  archive:")
    lines.append(f'    path: "{archive_path.as_posix()}"')
    lines.append('    header_template: "X"')
    lines.append("  pointer:")
    lines.append("    insert_at: section_top")
    lines.append('    template: "X"')
    if expected_entry_count is not None:
        mn = expected_entry_count["min"]
        mx = expected_entry_count["max"]
        on_drift = expected_entry_count.get("on_drift", "warn_continue")
        lines.append("  expected_entry_count:")
        lines.append(f"    min: {mn}")
        lines.append(f"    max: {mx}")
        lines.append(f"    on_drift: {on_drift}")
    lines.append("backlink_scan:")
    lines.append("  scan_paths: []")
    lines.append("  search_terms: []")
    lines.append("  on_match: warn_continue")
    lines.append("  skip_override_allowed: true")
    lines.append("audit:")
    lines.append("  pre_run: false")
    lines.append("  pre_run_pass_threshold: pass")
    lines.append("  post_run_hint: false")
    lines.append("  fail_close_on_drift: false")
    lines.append("retry_policy:")
    lines.append("  max_identical_phase_failures: 2")
    lines.append('  identity_key: ["phase", "exception_class"]')
    if executed is None:
        lines.append("executed: null")
    else:
        ts = executed.get("timestamp", "2026-05-24T12:00:00Z")
        ras = executed.get("reference_archive_sha", "a" * 64)
        csha = commit_sha if commit_sha is not None else executed.get("commit_sha", "pending")
        lines.append("executed:")
        lines.append(f'  timestamp: "{ts}"')
        lines.append(f'  reference_archive_sha: "{ras}"')
        lines.append(f'  commit_sha: "{csha}"')
    cfg = tmp_path / "cfg.yaml"
    cfg.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return cfg
