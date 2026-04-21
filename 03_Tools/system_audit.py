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
import contextlib
import datetime
import importlib
import sys
import traceback
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "03_Tools"))

from system_audit.checks import CORE, OPTIONAL  # noqa: E402
from system_audit.report import compute_exit_code, render_human, render_json  # noqa: E402
from system_audit.state_writer import write_last_audit  # noqa: E402
from system_audit.types import AuditContext, Category, CheckResult, FailureDetail  # noqa: E402

MINIMAL_BASELINE_KEYS = ("jsonl_schema", "pipeline_ssot", "log_lag")

# (name, spec, category) — category travels with the check so even a never-run
# (timed-out) check still carries the correct core/optional label in downstream
# aggregation (Codex Finding F: pre-fix, category was hardcoded "core").
ScopedCheck = tuple[str, str, Category]


def _load_run(spec: str) -> Callable[[Path, AuditContext], CheckResult]:
    mod_name, func_name = spec.split(":")
    mod = importlib.import_module(mod_name)
    return getattr(mod, func_name)


def _build_scoped_checks(args: argparse.Namespace) -> list[ScopedCheck]:
    """Select (name, spec, category) tuples based on mutually-exclusive scope flag."""
    if args.vault:
        return [(k, v, "optional") for k, v in OPTIONAL.items()]
    if args.full:
        return (
            [(k, v, "core") for k, v in CORE.items()]
            + [(k, v, "optional") for k, v in OPTIONAL.items()]
        )
    if args.minimal_baseline:
        return [(k, CORE[k], "core") for k in MINIMAL_BASELINE_KEYS if k in CORE]
    return [(k, v, "core") for k, v in CORE.items()]


def _run_one(
    name: str,
    spec: str,
    context: AuditContext,
    timeout_s: float,
    category: Category,
) -> tuple[CheckResult | None, Exception | None]:
    """Dispatch a single check with a per-call timeout.

    Returns (result, None) on normal completion or on a timeout (converted into
    a synthetic FAIL CheckResult). Returns (None, exc) on any tool-internal
    exception — either resolve-time (ImportError/AttributeError/ValueError on
    the module:function spec) or an uncaught exception raised inside the check.
    The caller must propagate such errors to rc=2.

    Timeout is SOFT: `future.result(timeout=...)` only stops waiting. The
    underlying worker thread keeps running (Python does not cancel a running
    task in a ThreadPoolExecutor, and setting `daemon=True` on an already-
    started thread raises RuntimeError in Py 3.11+). `shutdown(wait=False)`
    prevents `__exit__`-block on the abandoned worker. In practice this is
    acceptable because the audit tool is a one-shot CLI — the leaked thread
    dies with the process. Do NOT invoke this from a long-running service
    or test-loop without first isolating via subprocess (Codex + CodeRabbit
    Finding A — backlog: subprocess-based hard timeout for Task 14/15).
    """
    try:
        fn = _load_run(spec)
    except (ImportError, AttributeError, ValueError) as e:
        return None, e

    executor = ThreadPoolExecutor(
        max_workers=1, thread_name_prefix=f"audit-{name}",
    )
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
                    expected=f"complete within {timeout_s:g}s",
                    actual="timeout",
                    severity="error",
                    hint=f"check hung; raise --timeout-per-check or investigate {spec}",
                )],
                duration_ms=int(timeout_s * 1000),
                category=category,
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
            with contextlib.suppress(ValueError, OSError):
                reconfigure(encoding="utf-8", errors="replace")


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

    scoped_checks = _build_scoped_checks(args)
    include_optional = args.full or args.vault
    context = AuditContext(
        repo_root=REPO_ROOT,
        include_optional=include_optional,
        vault_timeout_s=args.timeout_per_check,
    )
    timestamp_utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    results: list[CheckResult] = []
    internal_errors: list[tuple[str, Exception]] = []

    if not scoped_checks:
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
        for name, spec, category in scoped_checks:
            result, err = _run_one(
                name, spec, context, args.timeout_per_check, category,
            )
            if err is not None:
                internal_errors.append((name, err))
                continue
            assert result is not None  # narrow type for mypy/readers
            results.append(result)

    if internal_errors:
        # Info-preservation (Codex Finding E): render the partial audit to stdout
        # (with partial=True + internal_errors[] in JSON) BEFORE escalating to rc=2
        # so automation + humans can still see what did complete. STATE.md stays
        # unwritten — corrupted audit state must not be persisted.
        ierrs_payload = [
            (name, type(exc).__name__, str(exc)) for name, exc in internal_errors
        ]
        if args.json:
            print(render_json(
                results, timestamp_utc=timestamp_utc, internal_errors=ierrs_payload,
            ))
        else:
            print(render_human(results, timestamp_utc=timestamp_utc))
            print("", file=sys.stderr)
            print("[partial] tool-internal errors encountered — results above are "
                  "incomplete:", file=sys.stderr)
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
