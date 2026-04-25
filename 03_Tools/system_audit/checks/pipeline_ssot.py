"""Check-6: PIPELINE.md Pipeline-SSoT-Section Plan-Refs muessen existieren.

MVP = Reverse-Only (Spec §5.1 Check-6). Forward-Richtung (Plan-Frontmatter
status: ready|in-progress) deferred in Spec §10.5 / §12 Follow-up-Plan.
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

PIPELINE_HEADER_RE = re.compile(r"^##\s+🗺\s+Aktive Pipeline", re.MULTILINE)
PLAN_PATH_RE = re.compile(r"(docs/superpowers/plans/\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md)")


def extract_plan_refs(pipeline_text: str) -> list[str]:
    """Isolate pipeline section; return all plan-path references in order (dedup)."""
    m = PIPELINE_HEADER_RE.search(pipeline_text)
    if not m:
        return []
    after = pipeline_text[m.end():]
    end_rel = len(after)
    for next_match in re.finditer(r"^##\s+(?!🗺)", after, re.MULTILINE):
        end_rel = next_match.start()
        break
    for hr in re.finditer(r"^---\s*$", after, re.MULTILINE):
        if hr.start() < end_rel:
            end_rel = hr.start()
            break
    section = after[:end_rel]
    seen: list[str] = []
    for pm in PLAN_PATH_RE.finditer(section):
        p = pm.group(1)
        if p not in seen:
            seen.append(p)
    return seen


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    pipeline_path_override: Path | None = None,
) -> CheckResult:
    start = time.monotonic()
    pipeline_path = pipeline_path_override or repo_root / "00_Core" / "PIPELINE.md"

    if not pipeline_path.exists():
        return CheckResult(
            name="pipeline_ssot", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(pipeline_path), expected="PIPELINE.md present",
                actual="missing", severity="warning", hint=None,
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    text = pipeline_path.read_text(encoding="utf-8", errors="replace")
    refs = extract_plan_refs(text)
    failures: list[FailureDetail] = []
    n_checked = len(refs)
    n_passed = 0

    for ref in refs:
        target = repo_root / ref
        if target.exists():
            n_passed += 1
        else:
            failures.append(FailureDetail(
                location=str(pipeline_path.relative_to(repo_root)) if pipeline_path.is_relative_to(repo_root) else str(pipeline_path),
                expected=f"{ref} exists",
                actual=f"{ref} missing",
                severity="error",
                hint="Pipeline-Referenz aktualisieren oder Plan-Datei wiederherstellen",
            ))

    has_error = any(f.severity == "error" for f in failures)
    status = "FAIL" if has_error else "PASS"

    return CheckResult(
        name="pipeline_ssot", status=status,  # type: ignore[arg-type]
        n_checked=n_checked, n_passed=n_passed, failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
