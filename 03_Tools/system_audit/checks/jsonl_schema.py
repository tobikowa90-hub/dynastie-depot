"""Check-1: Revalidate all JSONL stores against their Pydantic models.

Spec §5.1 Check-1. Missing/empty stores → SKIP with warning. Validation error per
line → FailureDetail(severity="error"). No SKIP-fallback for missing models
(Q1 resolved YES; Task 1 nachgeruestet PortfolioReturnRecord + BenchmarkReturnRecord).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

from pydantic import ValidationError

from system_audit.types import AuditContext, CheckResult, FailureDetail


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    stores_override: dict[str, Path] | None = None,
) -> CheckResult:
    start = time.monotonic()

    _backtest_path = str(repo_root / "03_Tools" / "backtest-ready")
    if _backtest_path not in sys.path:
        sys.path.insert(0, _backtest_path)
    from schemas import (
        BenchmarkReturnRecord,
        FlagEvent,
        PortfolioReturnRecord,
        ScoreRecord,
    )

    default_stores: dict[str, tuple[Path, type]] = {
        "score_history": (repo_root / "05_Archiv" / "score_history.jsonl", ScoreRecord),
        "flag_events": (repo_root / "05_Archiv" / "flag_events.jsonl", FlagEvent),
        "portfolio_returns": (repo_root / "05_Archiv" / "portfolio_returns.jsonl", PortfolioReturnRecord),
        "benchmark_series": (repo_root / "05_Archiv" / "benchmark-series.jsonl", BenchmarkReturnRecord),
    }

    if stores_override:
        models = {k: v[1] for k, v in default_stores.items()}
        stores = {k: (p, models[k]) for k, p in stores_override.items() if k in models}
    else:
        stores = default_stores

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0
    any_parsed = False

    for store_name, (path, model) in stores.items():
        path_str = str(path.relative_to(repo_root)) if path.is_relative_to(repo_root) else str(path)
        if not path.exists():
            failures.append(FailureDetail(
                location=f"{store_name}:{path_str}",
                expected="file present",
                actual="missing",
                severity="warning",
                hint="Backfill ausstehend oder Pfad falsch?",
            ))
            continue
        if path.stat().st_size == 0:
            failures.append(FailureDetail(
                location=f"{store_name}:{path_str}",
                expected="non-empty store",
                actual="empty",
                severity="warning",
                hint="Store leer — erster Record erwartet",
            ))
            continue

        any_parsed = True
        with path.open("r", encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                n_checked += 1
                try:
                    model.model_validate_json(line)
                    n_passed += 1
                except ValidationError as e:
                    errs = e.errors()
                    if errs:
                        first = errs[0]
                        loc_path = ".".join(str(p) for p in first["loc"]) or "<root>"
                        actual = f"{loc_path}: {first['msg']}"[:140]
                    else:
                        actual = str(e)[:140]
                    failures.append(FailureDetail(
                        location=f"{path.relative_to(repo_root)}:{lineno}",
                        expected=f"{model.__name__} valid",
                        actual=actual,
                        severity="error",
                        hint="Migration-Helper ausfuehren oder Backfill re-run",
                    ))

    has_error = any(f.severity == "error" for f in failures)
    has_warning = any(f.severity == "warning" for f in failures)

    if has_error:
        status: str = "FAIL"
    elif not any_parsed:
        status = "SKIP"
    elif has_warning:
        status = "WARN"
    else:
        status = "PASS"

    duration_ms = int((time.monotonic() - start) * 1000)

    return CheckResult(
        name="jsonl_schema",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=duration_ms,
        category="core",
    )
