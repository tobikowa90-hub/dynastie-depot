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


def test_jsonl_schema_pass_on_good_fixture() -> None:
    from system_audit.checks.jsonl_schema import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "jsonl_schema"
    result = run(REPO_ROOT, ctx, stores_override={
        "score_history": fx / "good_score.jsonl",
        "flag_events": fx / "empty.jsonl",
        "portfolio_returns": fx / "empty.jsonl",
        "benchmark_series": fx / "empty.jsonl",
    })
    assert result.status in ("PASS", "WARN", "SKIP"), f"expected PASS/WARN/SKIP, got {result.status}"
    assert all(f.severity != "error" for f in result.failures)

def test_jsonl_schema_fail_on_bad_fixture() -> None:
    from system_audit.checks.jsonl_schema import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "jsonl_schema"
    result = run(REPO_ROOT, ctx, stores_override={
        "score_history": fx / "bad_score.jsonl",
        "flag_events": fx / "empty.jsonl",
        "portfolio_returns": fx / "empty.jsonl",
        "benchmark_series": fx / "empty.jsonl",
    })
    assert result.status == "FAIL"
    assert any(f.severity == "error" for f in result.failures)
    assert any("bad_score.jsonl:1" in f.location for f in result.failures)

def test_jsonl_schema_skip_on_missing_file(tmp_path=None) -> None:
    from system_audit.checks.jsonl_schema import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, stores_override={
        "score_history": REPO_ROOT / "does" / "not" / "exist.jsonl",
        "flag_events": REPO_ROOT / "no.jsonl",
        "portfolio_returns": REPO_ROOT / "no.jsonl",
        "benchmark_series": REPO_ROOT / "no.jsonl",
    })
    assert result.status == "SKIP"
    assert all(f.severity == "warning" for f in result.failures)


def test_store_freshness_warn_on_stale() -> None:
    import tempfile, json, datetime
    from system_audit.checks.store_freshness import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        pr = tdp / "portfolio_returns.jsonl"
        bs = tdp / "benchmark-series.jsonl"
        # 14 calendar days = ≥10 business days, robust to long-weekend execution
        stale = (datetime.date.today() - datetime.timedelta(days=14)).isoformat()
        pr.write_text(json.dumps({"schema_version":"1.0","date":stale}) + "\n", encoding="utf-8")
        bs.write_text(json.dumps({"schema_version":"1.0","date":stale}) + "\n", encoding="utf-8")
        ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
        result = run(REPO_ROOT, ctx, stores_override={
            "portfolio_returns": pr,
            "benchmark_series": bs,
        })
    assert result.status == "WARN"
    assert all(f.severity == "warning" for f in result.failures)
    assert len(result.failures) == 2

def test_store_freshness_pass_on_fresh() -> None:
    import tempfile, json, datetime
    from system_audit.checks.store_freshness import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        pr = tdp / "portfolio_returns.jsonl"
        bs = tdp / "benchmark-series.jsonl"
        today = datetime.date.today().isoformat()
        pr.write_text(json.dumps({"schema_version":"1.0","date":today}) + "\n", encoding="utf-8")
        bs.write_text(json.dumps({"schema_version":"1.0","date":today}) + "\n", encoding="utf-8")
        ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
        result = run(REPO_ROOT, ctx, stores_override={
            "portfolio_returns": pr, "benchmark_series": bs,
        })
    assert result.status == "PASS"
    assert result.failures == []

def test_store_freshness_skip_on_missing() -> None:
    from system_audit.checks.store_freshness import run
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, stores_override={
        "portfolio_returns": REPO_ROOT / "does-not-exist-1.jsonl",
        "benchmark_series": REPO_ROOT / "does-not-exist-2.jsonl",
    })
    assert result.status == "SKIP"


def test_markdown_header_pass_on_aligned() -> None:
    from system_audit.checks.markdown_header import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "markdown_header"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, targets_override=[
        (fx / "state_ok.md", "state"),
        (fx / "core_memory_ok.md", "core_memory"),
        (fx / "faktortabelle_ok.md", "faktortabelle"),
    ])
    assert result.status == "PASS", f"got {result.status}, failures={result.failures}"

def test_markdown_header_fail_on_stale() -> None:
    from system_audit.checks.markdown_header import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "markdown_header"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, targets_override=[
        (fx / "state_stale.md", "state"),
    ])
    assert result.status == "FAIL"
    assert any(f.severity == "error" for f in result.failures)

def test_markdown_header_warn_on_lag() -> None:
    from system_audit.checks.markdown_header import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "markdown_header"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, targets_override=[
        (fx / "state_warn.md", "state"),
    ])
    assert result.status == "WARN"
    assert all(f.severity == "warning" for f in result.failures)
    assert len(result.failures) == 1


def test_cross_source_pass_on_aligned() -> None:
    from system_audit.checks.cross_source import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "cross_source"
    ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
    result = run(REPO_ROOT, ctx, sources_override={
        "config": fx / "config.yaml",
        "state": fx / "state.md",
        "faktortabelle": fx / "faktortabelle.md",
        "vault_entities_dir": None,
    })
    assert result.status in ("PASS", "WARN"), f"got {result.status}, failures={result.failures}"
    assert all(f.severity != "error" for f in result.failures)

def test_cross_source_fail_on_divergence() -> None:
    import shutil, tempfile
    from system_audit.checks.cross_source import run
    fx = REPO_ROOT / "03_Tools" / "system_audit" / "fixtures" / "cross_source"
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        shutil.copy(fx / "config.yaml", tdp / "config.yaml")
        shutil.copy(fx / "faktortabelle.md", tdp / "faktortabelle.md")
        state = (fx / "state.md").read_text(encoding="utf-8").replace("AVGO | 84", "AVGO | 85")
        (tdp / "state.md").write_text(state, encoding="utf-8")
        ctx = AuditContext(repo_root=REPO_ROOT, include_optional=False)
        result = run(REPO_ROOT, ctx, sources_override={
            "config": tdp / "config.yaml",
            "state": tdp / "state.md",
            "faktortabelle": tdp / "faktortabelle.md",
            "vault_entities_dir": None,
        })
    assert result.status == "FAIL"
    assert any("AVGO" in f.actual for f in result.failures)

def test_flag_parser_all_six_variants() -> None:
    """Spec §7.3 Parser-Golden-Test: alle 6 beobachteten FLAG-Strings."""
    from system_audit.checks.cross_source import parse_flag_icon
    assert parse_flag_icon("✅") == ("ok", None)
    assert parse_flag_icon("⚠️ Insider-Review") == ("warn", "Insider-Review")
    assert parse_flag_icon("✅ Insurance Exception") == ("ok", "Insurance Exception")
    assert parse_flag_icon("✅ Screener-Exception") == ("ok", "Screener-Exception")
    assert parse_flag_icon("🔴 Score-basiert") == ("flag", "Score-basiert")
    assert parse_flag_icon("🔴 CapEx/OCF 83.6%") == ("flag", "CapEx/OCF 83.6%")

def test_flag_mismatch_matrix() -> None:
    """Spec §5.1 Check-3 FLAG-Matrix."""
    from system_audit.checks.cross_source import compare_flag
    assert compare_flag(False, "ok") == "match"
    assert compare_flag(False, "warn") == "warning"
    assert compare_flag(False, "flag") == "error"
    assert compare_flag(True, "flag") == "match"
    assert compare_flag(True, "ok") == "error"
    assert compare_flag(True, "warn") == "error"


def test_existence_pass_on_existing_paths() -> None:
    import tempfile
    from system_audit.checks.existence import run
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "target.py").write_text("", encoding="utf-8")
        (tdp / "doc.md").write_text("Siehe `target.py` und `absent.py`.", encoding="utf-8")
        ctx = AuditContext(repo_root=tdp, include_optional=False)
        result = run(tdp, ctx, scan_files_override=[tdp / "doc.md"])
    assert result.status == "FAIL"
    assert any("absent.py" in f.actual for f in result.failures)
    assert not any("target.py" in f.actual for f in result.failures)


if __name__ == "__main__":
    test_check_result_pass_semantics()
    test_check_result_fail_error()
    test_check_result_warn_is_not_fail()
    test_audit_context_repo_root()
    test_failure_detail_is_frozen()
    test_check_result_skip_status()
    test_check_result_failures_mutable()
    print("[OK] types smoke tests passed")
    test_jsonl_schema_pass_on_good_fixture()
    test_jsonl_schema_fail_on_bad_fixture()
    test_jsonl_schema_skip_on_missing_file()
    print("[OK] jsonl_schema smoke tests passed")
    test_store_freshness_warn_on_stale()
    test_store_freshness_pass_on_fresh()
    test_store_freshness_skip_on_missing()
    print("[OK] store_freshness smoke tests passed")
    test_markdown_header_pass_on_aligned()
    test_markdown_header_fail_on_stale()
    test_markdown_header_warn_on_lag()
    print("[OK] markdown_header smoke tests passed")
    test_cross_source_pass_on_aligned()
    test_cross_source_fail_on_divergence()
    test_flag_parser_all_six_variants()
    test_flag_mismatch_matrix()
    print("[OK] cross_source smoke tests passed")
    test_existence_pass_on_existing_paths()
    print("[OK] existence smoke tests passed")
