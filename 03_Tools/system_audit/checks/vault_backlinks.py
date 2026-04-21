"""Optional Check-8: Obsidian wikilinks [[Note]] must resolve.

Timeout is sourced from context.vault_timeout_s (AuditContext default 20s,
overridable per orchestrator invocation).
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]+)?(?:#[^\]]+)?\]\]")


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    timeout_s = context.vault_timeout_s
    vault = repo_root / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind"
    if not vault.exists():
        return CheckResult(name="vault_backlinks", status="SKIP", n_checked=0, n_passed=0,
                           failures=[], duration_ms=0, category="optional")

    notes = {p.stem for p in vault.rglob("*.md") if "/raw/" not in str(p).replace("\\", "/")}

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    for md in vault.rglob("*.md"):
        if "/raw/" in str(md).replace("\\", "/"):
            continue
        if (time.monotonic() - start) > timeout_s:
            return CheckResult(
                name="vault_backlinks", status="SKIP", n_checked=n_checked, n_passed=n_passed,
                failures=failures + [FailureDetail(
                    location="vault_backlinks", expected=f"scan < {timeout_s}s",
                    actual="timed out", severity="warning", hint="Scope reduzieren oder Timeout erhöhen",
                )],
                duration_ms=int((time.monotonic() - start) * 1000),
                category="optional",
            )
        for lineno, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for m in WIKILINK_RE.finditer(line):
                n_checked += 1
                target = m.group(1).strip()
                if target in notes:
                    n_passed += 1
                else:
                    failures.append(FailureDetail(
                        location=f"{md.relative_to(repo_root)}:{lineno}",
                        expected=f"[[{target}]] resolves",
                        actual="no matching note",
                        severity="error",
                        hint=f"Note '{target}' fehlt oder umbenannt",
                    ))

    has_error = any(f.severity == "error" for f in failures)
    status = "FAIL" if has_error else "PASS"
    return CheckResult(
        name="vault_backlinks", status=status,  # type: ignore[arg-type]
        n_checked=n_checked, n_passed=n_passed, failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="optional",
    )
