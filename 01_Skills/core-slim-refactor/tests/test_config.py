import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

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
