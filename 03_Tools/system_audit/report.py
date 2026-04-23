"""Human + JSON renderer for audit results. Spec §6.3 / §6.4."""
from __future__ import annotations

import json
from collections import OrderedDict
from collections.abc import Sequence
from dataclasses import asdict

from system_audit.types import CheckResult, FailureDetail

STATUS_ICON = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️", "SKIP": "⏭️"}
SEVERITY_ICON = {"error": "🔴", "warning": "⚠️", "info": "ℹ️"}

GROUP_THRESHOLD = 3
PER_SECTION_PREVIEW = 2


def compute_exit_code(results: Sequence[CheckResult]) -> int:
    return 1 if any(r.status == "FAIL" for r in results) else 0


def _severity_icon(f: FailureDetail) -> str:
    return SEVERITY_ICON.get(f.severity, "•")


def _section_of(f: FailureDetail) -> str:
    """Derive the grouping key from a failure's location.

    Convention: location is `<section>[:<detail>]` — everything before the first
    colon is the section (source file, mirror name, or ticker group). Falls back
    to the full location if no colon is present.
    """
    loc = f.location
    return loc.split(":", 1)[0] if ":" in loc else loc


def _render_failure(f: FailureDetail, indent: str) -> list[str]:
    out = [f"{indent}{_severity_icon(f)} {f.location}: expected {f.expected} | actual {f.actual}"]
    if f.hint:
        out.append(f"{indent}  hint: {f.hint}")
    return out


def _group_failures(failures: Sequence[FailureDetail]) -> "OrderedDict[str, list[FailureDetail]]":
    """Group by section, ordered by group size (desc), then first-seen (stable)."""
    buckets: dict[str, list[FailureDetail]] = {}
    first_seen: dict[str, int] = {}
    for f in failures:
        s = _section_of(f)
        if s not in buckets:
            buckets[s] = []
            first_seen[s] = len(first_seen)
        buckets[s].append(f)
    sorted_sections = sorted(buckets, key=lambda s: (-len(buckets[s]), first_seen[s]))
    return OrderedDict((s, buckets[s]) for s in sorted_sections)


def render_human(results: Sequence[CheckResult], *, timestamp_utc: str) -> str:
    lines: list[str] = [f"🔍 System-Audit — {timestamp_utc}", ""]
    n_pass = n_fail = n_warn = n_skip = 0
    total_ms = 0

    for i, r in enumerate(results, 1):
        icon = STATUS_ICON.get(r.status, "?")
        ratio = f"{r.n_passed}/{r.n_checked}" if r.n_checked else "-"
        lines.append(f"Check-{i:<2} {r.name:<20} {icon} {r.status:<5} {ratio:<8} | {r.duration_ms:>5}ms")

        groups = _group_failures(r.failures) if r.failures else None
        use_grouped = (
            groups is not None
            and len(r.failures) > GROUP_THRESHOLD
            and max((len(b) for b in groups.values()), default=0) > 1
        )

        if not use_grouped:
            for f in r.failures:
                lines.extend(_render_failure(f, "         "))
        else:
            for section, bucket in groups.items():
                n_err = sum(1 for f in bucket if f.severity == "error")
                n_warn_b = sum(1 for f in bucket if f.severity == "warning")
                sev_summary = []
                if n_err:
                    sev_summary.append(f"{n_err}🔴")
                if n_warn_b:
                    sev_summary.append(f"{n_warn_b}⚠️")
                if len(bucket) - n_err - n_warn_b:
                    sev_summary.append(f"{len(bucket) - n_err - n_warn_b}ℹ️")
                sev_tag = " ".join(sev_summary) or str(len(bucket))
                lines.append(f"         [{section}] {len(bucket)} finding(s) — {sev_tag}")
                for f in bucket[:PER_SECTION_PREVIEW]:
                    lines.extend(_render_failure(f, "           "))
                if len(bucket) > PER_SECTION_PREVIEW:
                    lines.append(f"           ... {len(bucket) - PER_SECTION_PREVIEW} more in [{section}]")

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
