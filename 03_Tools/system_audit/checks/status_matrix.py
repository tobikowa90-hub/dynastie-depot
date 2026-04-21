"""Optional Check-9: B1..BN monotonicity + no-duplicate in Status-Matrix."""
from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

B_LABEL_RE = re.compile(r"\bB(\d+)\b")


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    target = repo_root / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
    if not target.exists():
        return CheckResult(name="status_matrix", status="SKIP", n_checked=0, n_passed=0,
                           failures=[], duration_ms=0, category="optional")

    text = target.read_text(encoding="utf-8")
    m = re.search(r"Status-Matrix", text, re.IGNORECASE)
    if not m:
        return CheckResult(name="status_matrix", status="SKIP", n_checked=0, n_passed=0,
                           failures=[], duration_ms=int((time.monotonic() - start) * 1000),
                           category="optional")
    section_start = m.start()
    after = text[section_start:]
    next_h = re.search(r"^##\s+(?!Status)", after, re.MULTILINE)
    section = after[:next_h.start()] if next_h else after

    numbers = sorted(set(int(lm.group(1)) for lm in B_LABEL_RE.finditer(section)))
    failures: list[FailureDetail] = []
    if numbers:
        all_nums = [int(lm.group(1)) for lm in B_LABEL_RE.finditer(section)]
        dup = {n for n in all_nums if all_nums.count(n) > 1}
        for n in sorted(dup):
            failures.append(FailureDetail(
                location=str(target.relative_to(repo_root)),
                expected=f"B{n} unique", actual=f"B{n} appears {all_nums.count(n)}×",
                severity="error", hint="Duplicate B-Nummer in Status-Matrix",
            ))
        for i in range(numbers[0], numbers[-1]):
            if i not in numbers:
                failures.append(FailureDetail(
                    location=str(target.relative_to(repo_root)),
                    expected=f"B{i} present", actual=f"B{i} missing",
                    severity="error", hint="B-Nummerierung monoton",
                ))

    has_error = any(f.severity == "error" for f in failures)
    status = "FAIL" if has_error else "PASS"
    return CheckResult(
        name="status_matrix", status=status,  # type: ignore[arg-type]
        n_checked=len(numbers), n_passed=len(numbers) - len(failures),
        failures=failures, duration_ms=int((time.monotonic() - start) * 1000),
        category="optional",
    )
