"""Optional Check-9: B1..BN monotonicity + no-duplicate in Status-Matrix."""
from __future__ import annotations

import re
import time
from collections import Counter
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

B_LABEL_RE = re.compile(r"\bB(\d+)\b")
# Header-anchored match prevents false-negatives when "Status-Matrix" appears
# in prose before the actual heading (Code-Review Blocker #1).
HEADER_RE = re.compile(r"^#{1,6}\s+[^\n]*Status-Matrix[^\n]*$", re.MULTILINE | re.IGNORECASE)


def run(repo_root: Path, context: AuditContext) -> CheckResult:  # noqa: ARG001 — context kept for registry-contract uniformity (§4.3), this check has no per-run config
    start = time.monotonic()
    target = repo_root / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "synthesis" / "Wissenschaftliche-Fundierung-DEFCON.md"
    if not target.exists():
        return CheckResult(name="status_matrix", status="SKIP", n_checked=0, n_passed=0,
                           failures=[], duration_ms=0, category="optional")

    text = target.read_text(encoding="utf-8")
    m = HEADER_RE.search(text)
    if not m:
        return CheckResult(name="status_matrix", status="SKIP", n_checked=0, n_passed=0,
                           failures=[], duration_ms=int((time.monotonic() - start) * 1000),
                           category="optional")
    section_start = m.start()
    after = text[section_start:]
    # Skip the matched header line itself when searching for the next heading,
    # otherwise the Status-Matrix heading would match against its own exclusion.
    body_start = m.end() - m.start()
    # Terminate at the next heading of the SAME OR HIGHER level (fewer or
    # equal `#`) that isn't itself a Status-Matrix heading. Subsections
    # (deeper level) must stay inside the section so `### Matrix` etc. get
    # scanned. Without level-awareness the first `###` would prematurely cut.
    header_line = m.group(0)
    level = len(header_line) - len(header_line.lstrip("#"))
    term_pattern = rf"^#{{1,{level}}}\s+(?!.*Status-Matrix)"
    next_h = re.search(term_pattern, after[body_start:], re.MULTILINE | re.IGNORECASE)
    section = after[:body_start + next_h.start()] if next_h else after

    all_nums = [int(lm.group(1)) for lm in B_LABEL_RE.finditer(section)]
    numbers = sorted(set(all_nums))
    failures: list[FailureDetail] = []
    dup_numbers: set[int] = set()
    if numbers:
        counts = Counter(all_nums)
        dup_numbers = {n for n, c in counts.items() if c > 1}
        for n in sorted(dup_numbers):
            failures.append(FailureDetail(
                location=str(target.relative_to(repo_root)),
                expected=f"B{n} unique", actual=f"B{n} appears {counts[n]}×",
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
    # n_passed counts unique B-numbers that are not duplicated. Gap-failures
    # reference numbers that are NOT in `numbers` by definition, so they must
    # not reduce n_passed — otherwise `B1 B3 B5` (3 unique, 2 gaps) yields
    # n_passed=1 instead of the correct 3.
    return CheckResult(
        name="status_matrix", status=status,  # type: ignore[arg-type]
        n_checked=len(numbers), n_passed=len(numbers) - len(dup_numbers),
        failures=failures, duration_ms=int((time.monotonic() - start) * 1000),
        category="optional",
    )
