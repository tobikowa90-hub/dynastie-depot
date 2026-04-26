"""Check-12: Top-Level-Governance-Parity (Phase 2 Sweep-Driver F11).

Compares .claude/commands/SystemAudit.md numeric claims + flag list against
the live CORE-Registry + system_audit.py argparse spec.
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

SLASH_CMD_PATH = Path(".claude") / "commands" / "SystemAudit.md"

# Each tuple is an alt-set: documentation passes if ANY form in the alt-set
# appears in the slash-doc. Mirrors the argparse spec in system_audit.py
# (--verbose has -v short-form; the other flags are long-only).
# Codex-Phase-2-Final-Review Important #3: -v/--verbose and --timeout-per-check
# were missing — removing either from the slash-doc passed silently. Two real
# CLI flags went unaudited.
EXPECTED_FLAGS: tuple[tuple[str, ...], ...] = (
    ("--core",),
    ("--full",),
    ("--vault",),
    ("--minimal-baseline",),
    ("--no-write",),
    ("--json",),
    ("-v", "--verbose"),
    ("--timeout-per-check",),
)
COUNT_RE = re.compile(r"(\d+)\s*Kern-Checks?", re.IGNORECASE)


def _live_core_count(repo_root: Path) -> int:
    """Read CORE-Registry via dynamic import to count current checks.

    Reentrancy-Safety (Codex-Review P2-05): Diese Funktion laeuft im Audit-
    Run, wo `system_audit.checks` bereits durch den Orchestrator importiert
    wurde. Python's Module-Cache (`sys.modules`) verhindert Re-Execution —
    `importlib.import_module` gibt das gecachte Modul zurueck, KEIN reload.
    Das ist genau das Verhalten was wir wollen: live-state der CORE-Dict
    wie sie vom Orchestrator gesehen wird.

    sys.path-Mutation ist defensiv (falls Check stand-alone gerufen wird),
    in Audit-Run-Kontext bereits vorhanden durch system_audit.py:30-31 —
    `inserted=False`-Branch greift dann.
    """
    import importlib
    import sys as _sys
    sa_path = str(repo_root / "03_Tools")
    inserted = False
    if sa_path not in _sys.path:
        _sys.path.insert(0, sa_path)
        inserted = True
    try:
        mod = importlib.import_module("system_audit.checks")
        return len(mod.CORE)
    finally:
        if inserted:
            _sys.path.remove(sa_path)


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    expected_core_count: int | None = None,
) -> CheckResult:
    start = time.monotonic()
    failures: list[FailureDetail] = []

    cmd_path = repo_root / SLASH_CMD_PATH
    if not cmd_path.exists():
        return CheckResult(
            name="governance_parity", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(SLASH_CMD_PATH),
                expected="slash-command file present",
                actual="missing",
                severity="warning",
                hint="Repo ohne .claude/commands/SystemAudit.md? Test-Repo?",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    text = cmd_path.read_text(encoding="utf-8", errors="replace")
    n_checked = 0

    # 1. Count-Parity
    n_checked += 1
    expected = expected_core_count if expected_core_count is not None else _live_core_count(repo_root)
    m = COUNT_RE.search(text)
    if m:
        claimed = int(m.group(1))
        if claimed != expected:
            failures.append(FailureDetail(
                location=f"{SLASH_CMD_PATH}: '... Kern-Checks'",
                expected=f"{expected} Kern-Checks (matches len(CORE))",
                actual=f"{claimed} Kern-Checks",
                severity="error",
                hint=f"Slash-Doku-Drift: CORE-Registry hat {expected}, Doku sagt {claimed}",
            ))
    else:
        failures.append(FailureDetail(
            location=str(SLASH_CMD_PATH),
            expected="explicit 'N Kern-Checks' phrase",
            actual="phrase not found",
            severity="warning",
            hint="Numerik-Aussage zur Check-Anzahl ergaenzen",
        ))

    # 2. Flag-Coverage
    # Severity-Policy: alle Flags = error, AUSSER --minimal-baseline = warning
    # weil F11 explizit nennt dass --minimal-baseline ein neuer Add-On-Flag ist
    # der erst nach Slash-Doku-Stand eingefuehrt wurde (Codex-Review P2-04:
    # einzige spec-gestuetzte Warning-Exception).
    # Each alt-tuple passes if any form in the tuple appears (e.g. -v OR --verbose).
    for alts in EXPECTED_FLAGS:
        n_checked += 1
        if not any(alt in text for alt in alts):
            primary = alts[0]
            display = "/".join(alts) if len(alts) > 1 else primary
            severity = "warning" if "--minimal-baseline" in alts else "error"
            failures.append(FailureDetail(
                location=f"{SLASH_CMD_PATH}: flag list",
                expected=f"flag '{display}' documented",
                actual="flag not mentioned",
                severity=severity,  # type: ignore[arg-type]
                hint=f"Slash-Doku sollte {display} explizit nennen",
            ))

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")
    n_passed = n_checked - len(failures)

    return CheckResult(
        name="governance_parity",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=max(0, n_passed),
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
