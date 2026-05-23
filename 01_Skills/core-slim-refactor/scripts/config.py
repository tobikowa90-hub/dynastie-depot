"""core-slim-refactor v0.1 — Config Load + Manual Schema Validate.

jsonschema NOT used (verified unavailable in Plan-Stage). Manual validation
enforces 8 rules per spec §2.2.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


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
    _check_unknown_keys(raw)
    _check_pattern_value(raw)
    _check_mutual_exclusion(raw)
    _check_executed_field(raw)
    _check_append_only_immutable(raw)
    _check_date_cut_section_wholesale(raw)

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


if __name__ == "__main__":
    cfg = load_config(sys.argv[1])
    print(f"OK: loaded profile={cfg.profile_name} pattern={cfg.pattern}")
