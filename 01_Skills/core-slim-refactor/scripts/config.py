"""core-slim-refactor v0.2.0 — Config Load + Manual Schema Validate.

jsonschema NOT used (verified unavailable in Plan-Stage). Manual validation
enforces 8 rules per spec SS2.2 + v0.2.0 schema-version gate + field/trailing_boundary
validation + expected_entry_count validation + commit_sha regex-check (Spec SS3.1-SS3.3+SS11.1).
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

# === v0.2.0 commit_sha regex (AC3b, Spec SS3.3) ===
_COMMIT_SHA_RE = re.compile(r"^(pending|[0-9a-f]{7,40})$")


class ConfigError(Exception):
    """Raised when config violates schema. Exit-code 2 mapping in entry-point."""


_ALLOWED_TOP_KEYS = {
    "schema_version",
    "profile_name",
    "executed",
    "target",
    "pattern",
    "bucket_archive",
    "slim_convention",
    "date_cut",
    "backlink_scan",
    "audit",
    "retry_policy",
}
_ALLOWED_PATTERNS = {"bucket-archive", "slim-convention", "date-cut"}
_PATTERN_SUBBLOCK = {
    "bucket-archive": "bucket_archive",
    "slim-convention": "slim_convention",
    "date-cut": "date_cut",
}
_REQUIRED_TOP = {
    "schema_version",
    "profile_name",
    "target",
    "pattern",
    "backlink_scan",
    "audit",
    "retry_policy",
}


@dataclass
class ConfigObject:
    raw: dict
    path: Path
    schema_version: int
    profile_name: str
    executed: dict | None
    target: dict
    pattern: str
    pattern_block: dict
    backlink_scan: dict
    audit: dict
    retry_policy: dict


def _has_v2_keys(raw: dict) -> bool:
    """True wenn Config v0.2.0-only Keys verwendet. raw = full YAML-dict (NICHT pattern_block).

    v0.2.0-Definition: `field: bullet` (neuer Wert fuer existing key), `trailing_boundary`
    (neuer Key in date_parser), `expected_entry_count` (neuer Key in date_cut).
    `field: header` ist KEIN v0.2.0-Marker (existiert bereits in v0.1.x).
    Empirisch verifiziert 2026-05-24 via smoke-test gegen scripts/config.py.
    """
    dc = raw.get("date_cut", {}) or {}
    dp = dc.get("date_parser", {}) or {}
    if dp.get("field") == "bullet":
        return True
    if "trailing_boundary" in dp:
        return True
    return "expected_entry_count" in dc


def load_config(path: Path | str) -> ConfigObject:
    """Load YAML config + run all schema-validations. Raise ConfigError on any violation."""
    path = Path(path)
    if not path.exists():
        raise ConfigError(f"config not found: {path}")

    with path.open(encoding="utf-8", newline="") as f:
        try:
            raw = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ConfigError(f"YAML parse error in {path}: {e}") from e

    if not isinstance(raw, dict):
        raise ConfigError(f"config root must be mapping, got {type(raw).__name__}")

    _check_required_fields(raw)

    # === v0.2.0 Schema-Version-Gate (Spec SS11.1, post-empirie 2026-05-24) ===
    # schema_version is Required-Top (guaranteed present after _check_required_fields).
    # v0.1.x-Configs use schema_version=1; v0.2.0-Runtime accepts both 1 and 2.
    # v0.2.0-only Keys without schema_version=2 are rejected (prevents silent misuse).
    schema_version = raw["schema_version"]
    if schema_version not in (1, 2):
        raise ConfigError(f"unsupported_schema_version: {schema_version} (allowed: 1, 2)")
    if _has_v2_keys(raw) and schema_version != 2:
        raise ConfigError("schema_version_required_for_v2_keys")

    _check_unknown_keys(raw)
    _check_pattern_value(raw)
    _check_mutual_exclusion(raw)
    _check_executed_field(raw)
    _validate_executed_block(raw)
    _check_append_only_immutable(raw)
    _check_date_cut_section_wholesale(raw)
    _validate_date_parser_v2(raw)
    _validate_expected_entry_count(raw)

    pattern = raw["pattern"]
    return ConfigObject(
        raw=raw,
        path=path,
        schema_version=raw["schema_version"],
        profile_name=raw["profile_name"],
        executed=raw.get("executed"),
        target=raw["target"],
        pattern=pattern,
        pattern_block=raw[_PATTERN_SUBBLOCK[pattern]],
        backlink_scan=raw["backlink_scan"],
        audit=raw["audit"],
        retry_policy=raw["retry_policy"],
    )


def _check_required_fields(raw: dict) -> None:
    missing = _REQUIRED_TOP - set(raw.keys())
    if missing:
        raise ConfigError(f"missing required field(s): {sorted(missing)}")


def _check_unknown_keys(raw: dict) -> None:
    unknown = set(raw.keys()) - _ALLOWED_TOP_KEYS
    if unknown:
        raise ConfigError(f"unknown top-level key(s): {sorted(unknown)}")


def _check_pattern_value(raw: dict) -> None:
    p = raw["pattern"]
    if p not in _ALLOWED_PATTERNS:
        raise ConfigError(f"pattern must be one of {sorted(_ALLOWED_PATTERNS)}, got {p!r}")


def _check_mutual_exclusion(raw: dict) -> None:
    declared = raw["pattern"]
    expected_block = _PATTERN_SUBBLOCK[declared]
    if expected_block not in raw:
        raise ConfigError(f"pattern={declared} declared but {expected_block} sub-block missing")
    other_blocks = set(_PATTERN_SUBBLOCK.values()) - {expected_block}
    populated_others = [b for b in other_blocks if b in raw and raw[b] is not None]
    if populated_others:
        raise ConfigError(
            f"mutual exclusion: pattern={declared} but also populated: {populated_others}"
        )


def _check_executed_field(raw: dict) -> None:
    ex = raw.get("executed")
    if ex is None:
        return
    if not isinstance(ex, dict):
        raise ConfigError(f"executed must be null or dict, got {type(ex).__name__}")
    required = {"timestamp", "commit_sha", "reference_archive_sha"}
    missing = required - set(ex.keys())
    nulls = [k for k in required if k in ex and ex[k] is None]
    if missing or nulls:
        raise ConfigError(
            f"executed must have all 3 sub-fields non-null (missing={sorted(missing)}, nulls={sorted(nulls)})"
        )


def _check_append_only_immutable(raw: dict) -> None:
    flag = raw["target"].get("append_only_immutable", False)
    if flag is True and raw["pattern"] != "date-cut":
        raise ConfigError(
            f"target.append_only_immutable=true requires pattern=date-cut, got {raw['pattern']!r}"
        )


def _check_date_cut_section_wholesale(raw: dict) -> None:
    """HIGH-2 Codex-R1: Pattern C operates wholesale; section-scope would silently drop entries."""
    if raw["pattern"] != "date-cut":
        return
    section = raw["target"].get("section")
    if section not in (None, "", "null"):
        raise ConfigError(
            f"pattern=date-cut requires target.section=null (wholesale archive); "
            f"got section={section!r}. Section-scoped date-cut is not supported in v0.1."
        )


def _validate_date_parser_v2(raw: dict) -> None:
    """Validate date_parser.field + trailing_boundary (Spec SS3.1, F-04).

    Called only when pattern=date-cut (after _check_pattern_value + _check_mutual_exclusion).
    For non-date-cut patterns there is no date_parser sub-block.
    """
    if raw.get("pattern") != "date-cut":
        return
    dc = raw.get("date_cut", {}) or {}
    dp = dc.get("date_parser", {}) or {}
    field = dp.get("field", "header")
    if field not in ("header", "bullet"):
        raise ConfigError(f"invalid_date_parser_field: got={field!r} allowed=['header','bullet']")
    tb = dp.get("trailing_boundary")
    if field == "bullet" and tb is None:
        raise ConfigError("bullet_mode_requires_trailing_boundary")
    if field == "header" and tb is not None:
        raise ConfigError("trailing_boundary_only_in_bullet_mode")


def _validate_expected_entry_count(raw: dict) -> None:
    """Validate expected_entry_count block if present (Spec SS3.2)."""
    if raw.get("pattern") != "date-cut":
        return
    dc = raw.get("date_cut", {}) or {}
    eec = dc.get("expected_entry_count")
    if eec is None:
        return
    if not isinstance(eec, dict):
        raise ConfigError("expected_entry_count_must_be_mapping")
    mn = eec.get("min")
    mx = eec.get("max")
    if not (isinstance(mn, int) and isinstance(mx, int)):
        raise ConfigError("expected_entry_count_min_max_must_be_int")
    if mn < 0 or mx < 0 or mn > mx:
        raise ConfigError(f"expected_entry_count_invalid_range: min={mn} max={mx}")
    on_drift = eec.get("on_drift", "warn_continue")
    if on_drift not in ("warn_continue", "fail_close"):
        raise ConfigError(f"expected_entry_count_invalid_on_drift: got={on_drift!r}")


def _validate_executed_block(raw: dict) -> None:
    """Validate executed.commit_sha regex (Spec SS3.3, AC3b).

    Runs after _check_executed_field which already ensures executed is dict-or-null
    and all 3 sub-fields are present+non-null. This adds regex format validation.
    """
    ex = raw.get("executed")
    if ex is None:
        return
    if not isinstance(ex, dict):
        return  # _check_executed_field already raised for non-dict; defensive guard
    csha = ex.get("commit_sha")
    if csha is not None and not _COMMIT_SHA_RE.match(str(csha)):
        raise ConfigError(f"invalid_commit_sha: got={csha!r} expected=^(pending|[0-9a-f]{{7,40}})$")


if __name__ == "__main__":
    cfg = load_config(sys.argv[1])
    print(f"OK: loaded profile={cfg.profile_name} pattern={cfg.pattern}")
