"""Shared dataclasses for the system-audit check-registry contract (Spec §4.3)."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

Status = Literal["PASS", "WARN", "FAIL", "SKIP"]
Severity = Literal["error", "warning"]
Category = Literal["core", "optional"]


@dataclass(frozen=True)
class FailureDetail:
    location: str
    expected: str
    actual: str
    severity: Severity
    hint: str | None = None


@dataclass
class CheckResult:
    name: str
    status: Status
    n_checked: int
    n_passed: int
    failures: list[FailureDetail] = field(default_factory=list)
    duration_ms: int = 0
    category: Category = "core"


@dataclass
class AuditContext:
    """Read-only context passed to every check.run(repo_root, context)."""
    repo_root: Path
    include_optional: bool = False
    vault_timeout_s: int = 20
