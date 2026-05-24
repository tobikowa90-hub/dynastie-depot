import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
TESTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(TESTS_DIR))

from _helpers import make_minimal_valid_cfg_yaml  # noqa: E402  Disziplin-Regel #4
from config import ConfigError, load_config  # noqa: E402


def _write_yaml(tmp_path, name, data):
    p = tmp_path / name
    p.write_text(yaml.safe_dump(data), encoding="utf-8", newline="")
    return p


def _minimal_bucket_archive_config():
    return {
        "schema_version": 1,
        "profile_name": "test-bucket",
        "executed": None,
        "target": {
            "file": "00_Core/CORE-MEMORY.md",
            "section": "## §13",
            "section_anchor_alt": None,
            "append_only_immutable": False,
        },
        "pattern": "bucket-archive",
        "bucket_archive": {
            "classify": {
                "by": "keyword",
                "keywords": ["Test-Keyword"],
                "keep_keywords": [],
                "case_sensitive": True,
            },
            "archive": {
                "path": "05_Archiv/test-archive.md",
                "header_template": "# Test\nCut: {timestamp}\nSource: {target_file} {section}\nTotal Rows: {n_rows}\n",
            },
            "pointer": {
                "insert_at": "chronological",
                "template": "| {pointer_date} | TEST | {n_rows} rows | {archive_link} |\n",
            },
        },
        "backlink_scan": {
            "scan_paths": ["00_Core/"],
            "search_terms": ["§13"],
            "on_match": "fail_close",
            "skip_override_allowed": False,
        },
        "audit": {
            "pre_run": True,
            "pre_run_pass_threshold": "pass",
            "post_run_hint": True,
            "fail_close_on_drift": True,
        },
        "retry_policy": {
            "max_identical_phase_failures": 2,
            "identity_key": ["phase", "exception_class"],
        },
    }


def test_load_valid_bucket_archive_config(tmp_path):
    cfg_path = _write_yaml(tmp_path, "valid.yaml", _minimal_bucket_archive_config())
    cfg = load_config(cfg_path)
    assert cfg.profile_name == "test-bucket"
    assert cfg.pattern == "bucket-archive"
    assert cfg.executed is None


def test_unknown_yaml_key_rejected(tmp_path):
    data = _minimal_bucket_archive_config()
    data["bogus_field"] = "should reject"
    cfg_path = _write_yaml(tmp_path, "bogus.yaml", data)
    with pytest.raises(ConfigError, match=r"unknown.*bogus_field"):
        load_config(cfg_path)


def test_mutual_exclusion_violation(tmp_path):
    data = _minimal_bucket_archive_config()
    data["slim_convention"] = {"fat_threshold_bytes": 3500}
    cfg_path = _write_yaml(tmp_path, "mutex.yaml", data)
    with pytest.raises(ConfigError, match="mutual exclusion"):
        load_config(cfg_path)


def test_executed_partial_rejected(tmp_path):
    data = _minimal_bucket_archive_config()
    data["executed"] = {
        "timestamp": "2026-05-23T11:30:00Z",
        "commit_sha": None,
        "reference_archive_sha": "abc",
    }
    cfg_path = _write_yaml(tmp_path, "partial.yaml", data)
    with pytest.raises(ConfigError, match=r"executed.*all.*non-null"):
        load_config(cfg_path)


def test_missing_required_field(tmp_path):
    data = _minimal_bucket_archive_config()
    del data["profile_name"]
    cfg_path = _write_yaml(tmp_path, "missing.yaml", data)
    with pytest.raises(ConfigError, match="profile_name"):
        load_config(cfg_path)


def test_append_only_immutable_blocks_non_date_cut(tmp_path):
    data = _minimal_bucket_archive_config()
    data["target"]["append_only_immutable"] = True
    cfg_path = _write_yaml(tmp_path, "immutable.yaml", data)
    with pytest.raises(ConfigError, match=r"append_only_immutable.*date-cut"):
        load_config(cfg_path)


def test_date_cut_requires_null_section(tmp_path):
    """HIGH-2 Codex-R1: pattern=date-cut + non-null section must fail-close."""
    data = _minimal_bucket_archive_config()
    data["pattern"] = "date-cut"
    del data["bucket_archive"]
    data["date_cut"] = {
        "cut_before": "2026-04-01",
        "date_parser": {"field": "header", "pattern": r"^## (\d{4}-\d{2}-\d{2}) "},
        "archive": {"path": "05_Archiv/x.md", "header_template": "# x\n"},
        "pointer": {"insert_at": "section_top", "template": "> x\n"},
    }
    # section is "## §13" (non-null) from _minimal — should reject
    cfg_path = _write_yaml(tmp_path, "datecut_section.yaml", data)
    with pytest.raises(ConfigError, match=r"date-cut.*target\.section=null"):
        load_config(cfg_path)


# ===== v0.2.0 Schema-Erweiterungen (Task 1.1 Step 2 - Disziplin-Regel #4: helper-Pflicht) =====


def test_field_header_with_trailing_boundary_rejected(tmp_path):
    """F-04: field=header + trailing_boundary gesetzt -> ConfigError: trailing_boundary_only_in_bullet_mode."""
    # _force_invalid_combo injects trailing_boundary under date_parser despite field=header.
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=2,
        field="header",
        _force_invalid_combo={"date_parser_trailing_boundary": "^## "},
    )
    with pytest.raises(ConfigError, match="trailing_boundary_only_in_bullet_mode"):
        load_config(cfg)


def test_field_bullet_without_trailing_boundary_rejected(tmp_path):
    """F-04: field=bullet ohne trailing_boundary -> ConfigError: bullet_mode_requires_trailing_boundary."""
    # Helper via _force_invalid_combo={} bypasst die Pre-Check-Validation; bullet_regex wird
    # emittiert, trailing_boundary aber NICHT (Helper appendet trailing_boundary nur wenn gesetzt).
    # So entsteht das intentional-broken Fixture fuer den Validation-Error-Test (Disziplin-Regel #4).
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=2,
        field="bullet",
        bullet_regex=r"^- \*\*Datum:\*\*\s+(\d{4}-\d{2}-\d{2})",
        trailing_boundary=None,  # intentionally missing
        _force_invalid_combo={},  # bypass helper pre-check, trailing_boundary not emitted
    )
    with pytest.raises(ConfigError, match="bullet_mode_requires_trailing_boundary"):
        load_config(cfg)


def test_invalid_field_value_rejected(tmp_path):
    """F-04: field=footer -> ConfigError: invalid_date_parser_field."""
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=2,
        field="footer",  # invalid value - triggers else-branch in helper + gate in config
    )
    with pytest.raises(ConfigError, match="invalid_date_parser_field"):
        load_config(cfg)


def test_commit_sha_regex_validation(tmp_path):
    """AC3b: commit_sha muss ^(pending|[0-9a-f]{7,40})$ matchen."""
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=2,
        executed={
            "timestamp": "2026-05-24T12:00:00Z",
            "reference_archive_sha": "a" * 64,
            "commit_sha": "NOTAVALIDHEX",
        },
        commit_sha="NOTAVALIDHEX",
    )
    with pytest.raises(ConfigError, match="invalid_commit_sha"):
        load_config(cfg)
