"""v0.2.0 Compat-Matrix Tests - Spec SS11 (rewritten 2026-05-24 nach empirischem Real-config.py-Audit)."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))

from _helpers import make_minimal_valid_cfg_yaml  # noqa: E402  Disziplin-Regel #4: helper-Pflicht
from config import ConfigError, load_config  # noqa: E402


def test_v0_1_x_config_with_schema_version_1_loads_ok(tmp_path):
    """Reale v0.1.x-Config (schema_version=1, keine v0.2.0-Keys) - OK auf v0.2.0-Runtime.

    Empirie 2026-05-24: schema_version ist Required-Top in v0.1.x (_REQUIRED_TOP in config.py:39).
    """
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=1,
    )
    out = load_config(cfg)
    # ConfigObject-Dataclass (config.py:50-62) - Attribut + Block-Subscript, KEIN dict-Subscript.
    assert out.pattern == "date-cut"
    assert out.schema_version == 1
    assert out.pattern_block["date_parser"].get("field", "header") == "header"


def test_v0_2_0_keys_with_schema_version_1_rejected(tmp_path):
    """field: bullet aber schema_version: 1 belassen - ConfigError: schema_version_required_for_v2_keys.

    Empirie 2026-05-24: das ist der realistische Misuse-Fall (User editiert nested-Key ohne
    schema_version zu bumpen). Test mit fehlendem schema_version wuerde am _check_required_fields
    failen statt am v2-key-gate.
    """
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=1,  # v0.1.x-Wert ABER v0.2.0-Keys -> sollte rejected werden
        field="bullet",
        bullet_regex=r"^- \*\*Datum:\*\*\s+(\d{4}-\d{2}-\d{2})",
        trailing_boundary=r"^## ",
    )
    with pytest.raises(ConfigError, match="schema_version_required_for_v2_keys"):
        load_config(cfg)


def test_schema_version_2_only_without_features_ok(tmp_path):
    """Config nur mit schema_version: 2, sonst v0.1.x-Schema - OK (explicit version-marker)."""
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=2,
    )
    out = load_config(cfg)
    # ConfigObject-Dataclass-Attribut, KEIN dict-Subscript/get.
    assert out.schema_version == 2


def test_v0_1_x_runtime_silent_accept_documentation(tmp_path):
    """DOCUMENTATION-Test (Spec SS11.2): v0.1.x-Runtime akzeptiert silent v0.2.0-Configs.

    Empirie 2026-05-24: real config.py hat KEINE schema_version-Wert-Validation und
    _check_unknown_keys prueft nur Top-Level. v0.1.x-Runtime auf v0.2.0-Config passiert silent.
    v0.2.0-Runtime MUSS daher selbst schema_version in (1, 2) erzwingen + nested-key-strict-Check
    ergaenzen (siehe Task 1.2 Step 2 Gate-Logic).

    Dieser Test ist eine Regression-Boundary: wenn jemand in der Zukunft eine schema_version-
    Validation in v0.1.x-Runtime rueckportiert, soll der Test darauf aufmerksam machen, dass die
    Compat-Story neu bewertet werden muss.

    Wir verwenden hier expected_entry_count (anderes v0.2.0-Key als der bullet-Test darueber),
    um den Boundary zu dokumentieren OHNE redundant zu sein: v0.2.0-Runtime lehnt den Misuse
    ab, v0.1.x-Runtime (legacy) wuerde das gleiche Fixture silent akzeptieren (Spec SS11.2).
    """
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=tmp_path / "x.md",
        archive_path=tmp_path / "a.md",
        schema_version=1,
        expected_entry_count={"min": 1, "max": 5, "on_drift": "warn_continue"},
    )
    with pytest.raises(ConfigError, match="schema_version_required_for_v2_keys"):
        load_config(cfg)
