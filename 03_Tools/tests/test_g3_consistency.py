"""Tests for g3_consistency audit-check (Spec §5 Z2).

Synthetic CLAUDE.md fixtures via tmp_path — see plan Task 6.1.
"""

from __future__ import annotations

from pathlib import Path

from system_audit.checks.g3_consistency import check_g3_consistency


def _write_fixture(
    tmp_path: Path,
    yaml_block: str,
    routing_triggers: list[str] | None = None,
) -> tuple[Path, Path]:
    triggers = routing_triggers or ["!QuickCheck"]
    routing_md = "\n".join(
        f"| `{t}` | x | y | — |" for t in triggers
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "# CLAUDE.md\n\n"
        "## Routing-Table\n\n"
        "| Trigger | Lies | Skippe | Skill |\n"
        "|---|---|---|---|\n"
        f"{routing_md}\n\n"
        "### Authoritative Workflow-Registry (M1 — Spec Sektion 2)\n\n"
        "```yaml\n"
        f"{yaml_block}\n"
        "```\n",
        encoding="utf-8",
    )
    plan_md = tmp_path / "RUFLO-INTEGRATION-PLAN.md"
    plan_md.write_text(
        "# Plan\n\n"
        "## §Adoption-Gates\n\n"
        "### §Adoption-Gate Stream-Chain\n\n"
        "### §Adoption-Gate Hive-Mind\n",
        encoding="utf-8",
    )
    return claude_md, plan_md


def test_pass_empty_list(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions: []\n"
    )
    claude, plan = _write_fixture(tmp_path, yaml_block)
    result = check_g3_consistency(claude_md=claude, plan_md=plan)
    assert result.passed is True
    assert result.failures == []


def test_pass_commented_empty(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions:\n"
        "  # - skill: ...\n"
        "  # only comments, no entries\n"
        "  []\n"
    )
    claude, plan = _write_fixture(tmp_path, yaml_block)
    result = check_g3_consistency(claude_md=claude, plan_md=plan)
    assert result.passed is True


def test_pass_all_three_fields(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions:\n"
        "  - skill: ruflo:stream-chain\n"
        "    gate-ref: \"RUFLO-INTEGRATION-PLAN v1.2 §Adoption-Gates Stream-Chain\"\n"
        "    named-trigger: \"!StreamChain\"\n"
    )
    claude, plan = _write_fixture(
        tmp_path, yaml_block, routing_triggers=["!QuickCheck", "!StreamChain"]
    )
    result = check_g3_consistency(claude_md=claude, plan_md=plan)
    assert result.passed is True


def test_fail_missing_trigger(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions:\n"
        "  - skill: ruflo:stream-chain\n"
        "    gate-ref: \"RUFLO-INTEGRATION-PLAN v1.2 §Adoption-Gates Stream-Chain\"\n"
    )
    claude, plan = _write_fixture(tmp_path, yaml_block)
    result = check_g3_consistency(claude_md=claude, plan_md=plan)
    assert result.passed is False
    assert any("named-trigger" in f.message for f in result.failures)


def test_fail_drift_trigger(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions:\n"
        "  - skill: ruflo:stream-chain\n"
        "    gate-ref: \"RUFLO-INTEGRATION-PLAN v1.2 §Adoption-Gates Stream-Chain\"\n"
        "    named-trigger: \"!FooBar\"\n"
    )
    claude, plan = _write_fixture(
        tmp_path, yaml_block, routing_triggers=["!QuickCheck"]
    )
    result = check_g3_consistency(claude_md=claude, plan_md=plan)
    assert result.passed is False
    assert any(
        "!FooBar" in f.message or "routing" in f.message.lower()
        for f in result.failures
    )


def test_fail_bad_gate_ref(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions:\n"
        "  - skill: ruflo:foo\n"
        "    gate-ref: \"Plan v1.2 §NonExistentGate\"\n"
        "    named-trigger: \"!Foo\"\n"
    )
    claude, plan = _write_fixture(
        tmp_path, yaml_block, routing_triggers=["!QuickCheck", "!Foo"]
    )
    result = check_g3_consistency(claude_md=claude, plan_md=plan)
    assert result.passed is False
    assert any("gate-ref" in f.message.lower() for f in result.failures)


def test_fail_plan_md_none_strict(tmp_path: Path) -> None:
    """G3 ist Pflicht-Gate: plan_md=None → FAIL (kein Degraded-Mode)."""
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions: []\n"
    )
    claude, _plan = _write_fixture(tmp_path, yaml_block)
    result = check_g3_consistency(claude_md=claude, plan_md=None)
    assert result.passed is False
    assert any("plan_md" in f.message.lower() for f in result.failures)


def test_fail_plan_md_missing_strict(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions: []\n"
    )
    claude, _plan = _write_fixture(tmp_path, yaml_block)
    fake_plan = tmp_path / "non-existent-plan.md"
    result = check_g3_consistency(claude_md=claude, plan_md=fake_plan)
    assert result.passed is False
    assert any("not found" in f.message.lower() for f in result.failures)


def test_fail_gate_ref_canonical_but_not_live_anchor(tmp_path: Path) -> None:
    yaml_block = (
        "default-workflow-layer: superpowers\n"
        "ruflo-workflow-exceptions:\n"
        "  - skill: ruflo:plain\n"
        "    gate-ref: \"Plan v1.2 §Adoption-Gates\"\n"
        "    named-trigger: \"!Plain\"\n"
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "# CLAUDE.md\n\n"
        "## Routing-Table\n\n"
        "| Trigger | Lies | Skippe | Skill |\n"
        "|---|---|---|---|\n"
        "| `!Plain` | x | y | — |\n\n"
        "### Authoritative Workflow-Registry (M1 — Spec Sektion 2)\n\n"
        "```yaml\n"
        f"{yaml_block}\n"
        "```\n",
        encoding="utf-8",
    )
    plan_md = tmp_path / "RUFLO-INTEGRATION-PLAN.md"
    plan_md.write_text(
        "# Plan\n\n"
        "### §Adoption-Gate Stream-Chain\n\n"
        "### §Adoption-Gate Hive-Mind\n",
        encoding="utf-8",
    )
    result = check_g3_consistency(claude_md=claude_md, plan_md=plan_md)
    assert result.passed is False
    assert any(
        "live heading" in f.message.lower() or "live_anchors" in f.message.lower()
        for f in result.failures
    )
