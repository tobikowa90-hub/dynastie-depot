"""Smoke tests for the system_audit package.

Run: python 03_Tools/system_audit/_smoke_test.py
"""
from __future__ import annotations

import sys

# Python auto-inserts the script's directory (03_Tools/system_audit/) at
# sys.path[0] on launch.  That shadows the stdlib 'types' module with our
# package-local types.py, breaking the stdlib import chain before any user
# code runs.  Pop it when detected; the explicit sys.path.insert below
# re-adds 03_Tools so 'system_audit.types' still resolves as a qualified
# sub-module (no conflict with stdlib 'types').
# NOTE: resolve()-variant (Path(__file__).resolve().parent) was tested and
# breaks on Python 3.14.3 — 'from pathlib import Path' itself triggers
# functools → types → shadow before the pop runs.  Keeping endswith-guard.
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


def test_failure_detail_is_frozen() -> None:
    import dataclasses
    f = FailureDetail(
        location="x", expected="a", actual="b",
        severity="error", hint=None,
    )
    try:
        f.location = "y"
    except dataclasses.FrozenInstanceError:
        return
    raise AssertionError("FailureDetail should be frozen")


def test_check_result_skip_status() -> None:
    r = CheckResult(
        name="demo", status="SKIP", n_checked=0, n_passed=0,
        duration_ms=0, category="core",
    )
    assert r.status == "SKIP"
    assert r.failures == []


def test_check_result_failures_mutable() -> None:
    r = CheckResult(
        name="demo", status="FAIL", n_checked=1, n_passed=0,
        duration_ms=0, category="core",
    )
    r.failures.append(FailureDetail(
        location="x", expected="a", actual="b",
        severity="error", hint=None,
    ))
    assert len(r.failures) == 1


if __name__ == "__main__":
    test_check_result_pass_semantics()
    test_check_result_fail_error()
    test_check_result_warn_is_not_fail()
    test_audit_context_repo_root()
    test_failure_detail_is_frozen()
    test_check_result_skip_status()
    test_check_result_failures_mutable()
    print("[OK] types smoke tests passed")
