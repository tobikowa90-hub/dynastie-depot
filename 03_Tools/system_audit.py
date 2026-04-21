"""Dynasty-Depot system-audit entry-point.

Usage:
  python 03_Tools/system_audit.py [--core|--full|--vault|--minimal-baseline]
                                  [--no-write] [--json] [-v]
                                  [--timeout-per-check SEC]

Exit codes:
  0 — all PASS/WARN/SKIP
  1 — >=1 FAIL (drift detected)
  2 — tool-internal error (ImportError, uncaught check exception) — STATE.md NOT written

Spec: docs/superpowers/specs/2026-04-21-system-audit-tool-design.md §4.2/§6.1
Plan: docs/superpowers/plans/2026-04-21-system-audit-tool.md Task 13
Plan-Header-Notice dokumentiert --minimal-baseline + --timeout-per-check als additiv
ueber Spec §6.1 (Spec frozen v0.2).
"""
from __future__ import annotations

import argparse
import datetime
import importlib
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "03_Tools"))

from system_audit.checks import CORE, OPTIONAL  # noqa: E402
from system_audit.report import compute_exit_code, render_human, render_json  # noqa: E402
from system_audit.state_writer import write_last_audit  # noqa: E402
from system_audit.types import AuditContext, CheckResult, FailureDetail  # noqa: E402

MINIMAL_BASELINE_KEYS = ("jsonl_schema", "pipeline_ssot", "log_lag")


def _load_run(spec: str):
    mod_name, func_name = spec.split(":")
    mod = importlib.import_module(mod_name)
    return getattr(mod, func_name)


def _build_registry(args: argparse.Namespace) -> tuple[dict[str, str], str]:
    """Select check-registry subset based on mutually-exclusive scope flag.

    Returns (registry, scope_label). scope_label used for run_cmd-annotation only.
    """
    if args.vault:
        return {k: v for k, v in OPTIONAL.items() if "vault" in k}, "--vault"
    if args.full:
        return {**CORE, **OPTIONAL}, "--full"
    if args.minimal_baseline:
        return {k: CORE[k] for k in MINIMAL_BASELINE_KEYS if k in CORE}, "--minimal-baseline"
    return dict(CORE), "--core"


def _run_one(
    name: str, spec: str, context: AuditContext, timeout_s: float
) -> tuple[CheckResult | None, Exception | None]:
    """Dispatch a single check with a per-call timeout.

    Returns (result, None) on clean completion or timeout (synthetic FAIL result),
    (None, exc) on tool-internal exception (rc=2 case).

    Fresh ThreadPoolExecutor per call to avoid __exit__-hang when a check times
    out: `with`-form would block in __exit__ waiting for the abandoned thread.
    """
    try:
        fn = _load_run(spec)
    except (ImportError, AttributeError, ValueError) as e:
        return None, e

    executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix=f"audit-{name}")
    try:
        future = executor.submit(fn, REPO_ROOT, context)
        try:
            return future.result(timeout=timeout_s), None
        except FuturesTimeoutError:
            synthetic = CheckResult(
                name=name,
                status="FAIL",
                n_checked=0,
                n_passed=0,
                failures=[FailureDetail(
                    location=name,
                    expected=f"complete within {timeout_s:.0f}s",
                    actual="timeout",
                    severity="error",
                    hint=f"check hung; raise --timeout-per-check or investigate {spec}",
                )],
                duration_ms=int(timeout_s * 1000),
                category="core",
            )
            return synthetic, None
        except Exception as e:  # noqa: BLE001 — uncaught check exception = tool bug (rc=2)
            return None, e
    finally:
        executor.shutdown(wait=False)


def _summary_for_state(results: list[CheckResult]) -> str:
    """Compact "N/M PASS (X FAIL, Y WARN, Z SKIP)" line for STATE.md Last-Audit block."""
    n_pass = sum(1 for r in results if r.status == "PASS")
    n_fail = sum(1 for r in results if r.status == "FAIL")
    n_warn = sum(1 for r in results if r.status == "WARN")
    n_skip = sum(1 for r in results if r.status == "SKIP")
    total = len(results)
    tail = []
    if n_fail:
        tail.append(f"{n_fail} FAIL")
    if n_warn:
        tail.append(f"{n_warn} WARN")
    if n_skip:
        tail.append(f"{n_skip} SKIP")
    suffix = f" ({', '.join(tail)})" if tail else ""
    return f"{n_pass}/{total} PASS{suffix}"


def _reconfigure_stdout_utf8() -> None:
    """Windows cp1252 default crashes render_human on emoji. Best-effort upgrade."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass  # non-reconfigurable stream (e.g. redirected buffer)


def _build_run_cmd(argv: list[str] | None) -> str:
    args_used = argv if argv is not None else sys.argv[1:]
    base = "python 03_Tools/system_audit.py"
    return f"{base} {' '.join(args_used)}".rstrip() if args_used else base


def main(argv: list[str] | None = None) -> int:
    _reconfigure_stdout_utf8()

    parser = argparse.ArgumentParser(
        description="Dynasty-Depot system-audit (drift detector)",
        prog="system_audit.py",
    )
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--core", action="store_true", help="Run core checks (default)")
    scope.add_argument("--full", action="store_true", help="Run core + optional checks")
    scope.add_argument("--vault", action="store_true", help="Run only vault-optional checks")
    scope.add_argument(
        "--minimal-baseline", action="store_true",
        help="Run minimal structural checks only (jsonl_schema + pipeline_ssot + log_lag) — "
             "Task-17 regression gate pre-drift-cleanup",
    )
    parser.add_argument("--no-write", action="store_true",
                        help="Skip STATE.md Last-Audit update (dry-run)")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON instead of human report")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Reserved for future per-check detail")
    parser.add_argument("--timeout-per-check", type=float, default=20.0,
                        metavar="SEC",
                        help="Per-check wall-clock timeout in seconds (default 20)")
    args = parser.parse_args(argv)

    if args.timeout_per_check <= 0:
        print(f"[error] --timeout-per-check must be positive (got {args.timeout_per_check})",
              file=sys.stderr)
        return 2

    registry, _scope_label = _build_registry(args)
    include_optional = args.full or args.vault
    context = AuditContext(
        repo_root=REPO_ROOT,
        include_optional=include_optional,
        vault_timeout_s=int(args.timeout_per_check),
    )
    timestamp_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    results: list[CheckResult] = []
    internal_errors: list[tuple[str, Exception]] = []

    if not registry:
        # --vault with no OPTIONAL registered (pre-Task-14) lands here — degenerate case.
        # Emit explicit SKIP so exit-code is 0 AND the user sees "nothing ran", not
        # a silent "all green".
        results.append(CheckResult(
            name="no_checks_registered",
            status="SKIP",
            n_checked=0,
            n_passed=0,
            failures=[FailureDetail(
                location="registry",
                expected="1+ check in selected scope",
                actual="empty registry",
                severity="warning",
                hint="--vault requires OPTIONAL checks (Task 14); try --core",
            )],
            duration_ms=0,
            category="optional",
        ))
    else:
        for name, spec in registry.items():
            result, err = _run_one(name, spec, context, args.timeout_per_check)
            if err is not None:
                internal_errors.append((name, err))
                continue
            assert result is not None  # narrow type for mypy/readers
            results.append(result)

    if internal_errors:
        for name, exc in internal_errors:
            print(
                f"[error] check '{name}' tool-internal failure: "
                f"{type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
            traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)
        return 2

    if args.json:
        print(render_json(results, timestamp_utc=timestamp_utc))
    else:
        print(render_human(results, timestamp_utc=timestamp_utc))

    exit_code = compute_exit_code(results)

    if not args.no_write:
        try:
            write_last_audit(
                REPO_ROOT / "00_Core" / "STATE.md",
                timestamp_utc=timestamp_utc,
                summary=_summary_for_state(results),
                run_cmd=_build_run_cmd(argv),
            )
        except RuntimeError as e:
            print(f"[error] STATE.md write failed (marker-block inconsistent): {e}",
                  file=sys.stderr)
            return 2
        except PermissionError as e:
            print(f"[warn] STATE.md write permission denied: {e}", file=sys.stderr)
            # Report already emitted on stdout — don't escalate to rc=2.

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
