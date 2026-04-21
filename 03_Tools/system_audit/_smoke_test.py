"""Smoke tests for the system_audit package.

Run: python 03_Tools/system_audit/_smoke_test.py
"""
from __future__ import annotations

import sys

# Python auto-inserts the script's directory (03_Tools/system_audit/) at
# sys.path[0] on launch.  That shadows the stdlib 'types' module with our
# package-local types.py, breaking the stdlib import chain before any user
# code runs.  Pop it immediately so stdlib resolves normally; the explicit
# sys.path.insert below re-adds 03_Tools so 'system_audit.types' still
# resolves as a qualified sub-module (no conflict with stdlib 'types').
if sys.path and sys.path[0].endswith("system_audit"):
    sys.path.pop(0)

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "03_Tools"))

from system_audit.types import AuditContext, CheckResult, FailureDetail


def test_check_result_pass_semantics() -> None:
    r = CheckResult(
        name="demo", status="PASS", n_checked=3, n_passed=3,
        failures=[], duration_ms=10, category="core",
    )
    assert r.status == "PASS"
    assert not r.failures

def test_check_result_fail_error() -> None:
    r = CheckResult(
        name="demo", status="FAIL", n_checked=3, n_passed=2,
        failures=[FailureDetail(
            location="x.md:1", expected="a", actual="b",
            severity="error", hint=None,
        )],
        duration_ms=10, category="core",
    )
    assert any(f.severity == "error" for f in r.failures)

def test_check_result_warn_is_not_fail() -> None:
    r = CheckResult(
        name="demo", status="WARN", n_checked=3, n_passed=2,
        failures=[FailureDetail(
            location="x.md:1", expected="fresh", actual="stale",
            severity="warning", hint=None,
        )],
        duration_ms=10, category="core",
    )
    assert r.status == "WARN"
    assert all(f.severity == "warning" for f in r.failures)

def test_audit_context_repo_root() -> None:
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False, vault_timeout_s=20)
    assert ctx.repo_root == REPO_ROOT
    assert ctx.include_optional is False


if __name__ == "__main__":
    test_check_result_pass_semantics()
    test_check_result_fail_error()
    test_check_result_warn_is_not_fail()
    test_audit_context_repo_root()
    print("[OK] types smoke tests passed")
