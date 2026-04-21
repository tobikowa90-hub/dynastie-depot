# -*- coding: utf-8 -*-
"""Human + JSON renderer for audit results. Spec §6.3 / §6.4."""
from __future__ import annotations

import json
from dataclasses import asdict
from typing import Sequence

from system_audit.types import CheckResult

STATUS_ICON = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️", "SKIP": "⏭️"}


def compute_exit_code(results: Sequence[CheckResult]) -> int:
    return 1 if any(r.status == "FAIL" for r in results) else 0


def render_human(results: Sequence[CheckResult], *, timestamp_utc: str) -> str:
    lines: list[str] = [f"🔍 System-Audit — {timestamp_utc}", ""]
    n_pass = n_fail = n_warn = n_skip = 0
    total_ms = 0

    for i, r in enumerate(results, 1):
        icon = STATUS_ICON.get(r.status, "?")
        ratio = f"{r.n_passed}/{r.n_checked}" if r.n_checked else "-"
        lines.append(f"Check-{i:<2} {r.name:<20} {icon} {r.status:<5} {ratio:<8} | {r.duration_ms:>5}ms")
        for f in r.failures[:3]:
            lines.append(f"         • {f.location}: expected {f.expected} | actual {f.actual}")
            if f.hint:
                lines.append(f"           hint: {f.hint}")
        if len(r.failures) > 3:
            lines.append(f"         ... {len(r.failures) - 3} more failure(s) suppressed")
        total_ms += r.duration_ms
        if r.status == "PASS":
            n_pass += 1
        elif r.status == "FAIL":
            n_fail += 1
        elif r.status == "WARN":
            n_warn += 1
        elif r.status == "SKIP":
            n_skip += 1

    total = len(results)
    lines.append("")
    lines.append(f"Summary: {n_pass}/{total} PASS, {n_fail} FAIL, {n_warn} WARN, {n_skip} SKIP")
    lines.append(f"Duration: {total_ms}ms")
    exit_code = 1 if n_fail > 0 else 0
    lines.append(f"Exit-Code: {exit_code}")
    return "\n".join(lines)


def render_json(
    results: Sequence[CheckResult],
    *,
    timestamp_utc: str,
    internal_errors: Sequence[tuple[str, str, str]] | None = None,
) -> str:
    """Render audit results as JSON.

    internal_errors: list of (check_name, exception_type, message) tuples. When
    non-empty, marks the payload partial, overrides exit_code to 2, and attaches
    an internal_errors array. STATE.md write is caller's responsibility — it
    must skip on partial so no corrupted audit state is persisted.
    """
    partial = bool(internal_errors)
    exit_code = 2 if partial else (1 if any(r.status == "FAIL" for r in results) else 0)
    summary = {
        "total": len(results),
        "passed": sum(1 for r in results if r.status == "PASS"),
        "failed": sum(1 for r in results if r.status == "FAIL"),
        "warned": sum(1 for r in results if r.status == "WARN"),
        "skipped": sum(1 for r in results if r.status == "SKIP"),
    }
    payload: dict = {
        "audit_timestamp_utc": timestamp_utc,
        "summary": summary,
        "exit_code": exit_code,
        "partial": partial,
        "duration_ms": sum(r.duration_ms for r in results),
        "checks": [asdict(r) for r in results],
    }
    if partial:
        payload["internal_errors"] = [
            {"check": name, "type": etype, "msg": emsg}
            for name, etype, emsg in internal_errors
        ]
    return json.dumps(payload, ensure_ascii=False, indent=2)
