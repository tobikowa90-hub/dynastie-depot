"""G3 3-Felder-Konsistenz-Check (Spec §5 — #42.3).

Verifies that every active entry in CLAUDE.md `ruflo-workflow-exceptions[]`
has all three fields populated AND consistent with cross-references:
  1. skill: non-empty string
  2. gate-ref: non-empty, canonicalizes to a closed Allow-Set member AND
     that canonical anchor exists as a live heading in RUFLO-INTEGRATION-PLAN.md
     (two-stage check — stale-anchor prevention per Spec §5 Z1 + Codex G2-R1-H2)
  3. named-trigger: non-empty, !-prefixed, present in Routing-Table

Parser is conservative (YAML-fenced-block extraction, not raw regex);
empty-list is valid PASS state (current default 2026-05-05).
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from system_audit.types import AuditContext
from system_audit.types import CheckResult as RegistryCheckResult
from system_audit.types import FailureDetail as RegistryFailureDetail

# Canonical Allow-Set for gate-ref normalization (closed list; new gates require
# code edit AND must also exist as live heading in RUFLO-INTEGRATION-PLAN.md).
CANONICAL_GATE_ALLOW_SET = frozenset({
    "Adoption-Gates",
    "Adoption-Gate Stream-Chain",
    "Adoption-Gate Hive-Mind",
})


@dataclass
class FailureDetail:
    level: str
    message: str
    check: str = "g3_consistency"
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass
class CheckResult:
    passed: bool
    failures: list[FailureDetail] = field(default_factory=list)


def _extract_m1_yaml_block(claude_md_text: str) -> str | None:
    heading_pattern = re.compile(
        r"^#{2,4}\s+Authoritative Workflow-Registry.*$",
        re.MULTILINE,
    )
    m = heading_pattern.search(claude_md_text)
    if not m:
        return None
    after = claude_md_text[m.end():]
    fence = re.search(r"```yaml\s*\n(.*?)```", after, re.DOTALL)
    if not fence:
        return None
    return fence.group(1)


def _extract_routing_triggers(claude_md_text: str) -> set[str]:
    triggers: set[str] = set()
    heading_pattern = re.compile(r"^##\s+Routing-Table.*$", re.MULTILINE)
    m = heading_pattern.search(claude_md_text)
    if not m:
        return triggers
    section = claude_md_text[m.end():]
    next_section = re.search(r"\n##\s+", section)
    if next_section:
        section = section[: next_section.start()]
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 2:
            continue
        first_cell = cells[1]
        for tok in re.findall(r"!\w+", first_cell):
            triggers.add(tok)
    return triggers


def _canonicalize_gate_ref(gate_ref: str) -> str | None:
    """Longest-match-first to avoid partial-matching 'Adoption-Gates' inside
    full string containing 'Adoption-Gate Stream-Chain'."""
    sorted_set = sorted(CANONICAL_GATE_ALLOW_SET, key=len, reverse=True)
    for canonical in sorted_set:
        if canonical in gate_ref:
            return canonical
    return None


def _extract_plan_anchors(plan_md_text: str) -> set[str]:
    anchors: set[str] = set()
    # Use [ \t] inside heading-suffix to avoid greedy \s+ swallowing newlines
    # (which made `Adoption-Gates` greedily extend to next heading line).
    pattern = re.compile(
        r"^#{1,6}[ \t]+§?[ \t]*(Adoption-Gates?(?:[ \t]+\S+(?:[ \t]+\S+)*)?)[ \t]*$",
        re.MULTILINE,
    )
    for m in pattern.finditer(plan_md_text):
        raw = m.group(1).strip()
        normalized = re.sub(r"\s+", " ", raw)
        if normalized == "Adoption-Gate":
            normalized = "Adoption-Gates"
        if normalized in CANONICAL_GATE_ALLOW_SET:
            anchors.add(normalized)
    return anchors


def check_g3_consistency(
    claude_md: Path,
    plan_md: Path | None = None,
) -> CheckResult:
    """Run G3 consistency check on CLAUDE.md + plan_md (two-stage gate-ref verify)."""
    failures: list[FailureDetail] = []

    if not claude_md.exists():
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message=f"CLAUDE.md not found: {claude_md}",
            )],
        )

    if plan_md is None:
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message=(
                    "G3-Gate: plan_md=None nicht akzeptabel. G3 ist Pflicht-Consistency-Gate; "
                    "two-stage gate-ref-Verify benötigt RUFLO-INTEGRATION-PLAN.md. "
                    "Wire-up in system_audit.py muss plan_md durchreichen."
                ),
            )],
        )
    if not plan_md.exists():
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message=f"G3-Gate: plan_md not found: {plan_md}",
            )],
        )

    text = claude_md.read_text(encoding="utf-8")
    yaml_block = _extract_m1_yaml_block(text)
    if yaml_block is None:
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message="M1 Registry heading or YAML fence not found in CLAUDE.md",
            )],
        )

    try:
        parsed = yaml.safe_load(yaml_block)
    except yaml.YAMLError as e:
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message=f"M1 Registry YAML parse error: {e}",
            )],
        )

    if not isinstance(parsed, dict):
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message=f"M1 Registry root not a dict: {type(parsed).__name__}",
            )],
        )

    exceptions = parsed.get("ruflo-workflow-exceptions") or []
    if not exceptions:
        return CheckResult(passed=True)

    if not isinstance(exceptions, list):
        return CheckResult(
            passed=False,
            failures=[FailureDetail(
                level="FAIL",
                message=f"ruflo-workflow-exceptions not a list: {type(exceptions).__name__}",
            )],
        )

    triggers = _extract_routing_triggers(text)
    plan_text = plan_md.read_text(encoding="utf-8")
    live_anchors = _extract_plan_anchors(plan_text)

    for idx, entry in enumerate(exceptions):
        if not isinstance(entry, dict):
            failures.append(FailureDetail(
                level="FAIL",
                message=f"G3-Drift: entry {idx} not a dict",
            ))
            continue

        skill = entry.get("skill")
        if not skill or not isinstance(skill, str):
            failures.append(FailureDetail(
                level="FAIL",
                message=f"G3-Drift: entry {idx} fehlt skill (or empty)",
                evidence={"entry": entry},
            ))

        gate_ref = entry.get("gate-ref")
        if not gate_ref or not isinstance(gate_ref, str):
            failures.append(FailureDetail(
                level="FAIL",
                message=f"G3-Drift: entry {idx} fehlt gate-ref (or empty)",
                evidence={"entry": entry},
            ))
        else:
            canonical = _canonicalize_gate_ref(gate_ref)
            if canonical is None:
                failures.append(FailureDetail(
                    level="FAIL",
                    message=(
                        f"G3-Drift: entry {idx} gate-ref does not match canonical "
                        f"Allow-Set {sorted(CANONICAL_GATE_ALLOW_SET)}: {gate_ref!r}"
                    ),
                    evidence={"entry": entry},
                ))
            elif canonical not in live_anchors:
                failures.append(FailureDetail(
                    level="FAIL",
                    message=(
                        f"G3-Drift: entry {idx} gate-ref canonical {canonical!r} "
                        f"NOT present as live heading in {plan_md.name}. "
                        f"Live anchors: {sorted(live_anchors)}"
                    ),
                    evidence={"entry": entry, "canonical": canonical,
                              "live_anchors": sorted(live_anchors)},
                ))

        trig = entry.get("named-trigger")
        if not trig or not isinstance(trig, str):
            failures.append(FailureDetail(
                level="FAIL",
                message=f"G3-Drift: entry {idx} fehlt named-trigger (or empty)",
                evidence={"entry": entry},
            ))
        elif not trig.startswith("!"):
            failures.append(FailureDetail(
                level="FAIL",
                message=(
                    f"G3-Drift: entry {idx} named-trigger lacks '!' prefix: {trig!r}"
                ),
                evidence={"entry": entry},
            ))
        elif trig not in triggers:
            failures.append(FailureDetail(
                level="FAIL",
                message=(
                    f"G3-Drift: entry {idx} named-trigger {trig!r} not present in "
                    f"Routing-Table triggers {sorted(triggers)}"
                ),
                evidence={"entry": entry, "routing_triggers": sorted(triggers)},
            ))

    return CheckResult(passed=(len(failures) == 0), failures=failures)


# Registry bridge — converts G3 CheckResult to system_audit.types.CheckResult
def run(
    repo_root: Path,
    context: AuditContext,
) -> RegistryCheckResult:
    """Check-Registry entry-point. Loads CLAUDE.md + RUFLO-INTEGRATION-PLAN.md
    via repo_root convention; converts internal CheckResult to registry shape."""
    start = time.monotonic()
    claude_md = repo_root / "CLAUDE.md"
    plan_md = repo_root / "00_Core" / "RUFLO-INTEGRATION-PLAN.md"
    inner = check_g3_consistency(claude_md=claude_md, plan_md=plan_md)

    reg_failures = [
        RegistryFailureDetail(
            location="CLAUDE.md::M1-Registry",
            expected="3-field consistency + live-anchor + routing-trigger",
            actual=f.message,
            severity="error",
            hint=None,
        )
        for f in inner.failures
    ]
    return RegistryCheckResult(
        name="g3_consistency",
        status="PASS" if inner.passed else "FAIL",
        n_checked=1,
        n_passed=1 if inner.passed else 0,
        failures=reg_failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
