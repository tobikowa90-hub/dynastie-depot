"""Check-10: SKILL.md Frontmatter-Completeness (Phase 2 Sweep-Driver F8).

Pflicht-Felder: name, description, version. Fehlt eines → WARN (nicht FAIL,
weil Convention 'Draft-Skill ohne Frontmatter' etabliert ist).

Schliesst die Luecke in skill_version.py:82-84 wo `if md_ver is None: continue`
einen Skill silent skippt — F8-Pathologie quick-screener war so monatelang
unsichtbar im Audit.
"""

from __future__ import annotations

import time
from pathlib import Path

import yaml

from system_audit.audit_types import AuditContext, CheckResult, FailureDetail

REQUIRED_FRONTMATTER_FIELDS = ("name", "description", "version")


def _parse_frontmatter(skill_dir: Path) -> dict | None:
    md = skill_dir / "SKILL.md"
    if not md.exists():
        return None
    text = md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}  # no-frontmatter sentinel
    try:
        _, fm, _ = text.split("---", 2)
        data = yaml.safe_load(fm) or {}
        if not isinstance(data, dict):
            return {}
        return data
    except ValueError, yaml.YAMLError:
        return {}


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    skills_dir = repo_root / "01_Skills"
    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    if not skills_dir.exists():
        return CheckResult(
            name="skill_frontmatter",
            status="SKIP",
            n_checked=0,
            n_passed=0,
            failures=[
                FailureDetail(
                    location="01_Skills/",
                    expected="skills dir",
                    actual="missing",
                    severity="warning",
                    hint="Repo-Layout veraendert?",
                )
            ],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    for skill_dir in skills_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        if skill_dir.name.startswith("_"):
            continue  # _extern/, _archive/ etc. ignored
        if not (skill_dir / "SKILL.md").exists():
            continue  # no skill manifest = not audit-scope

        n_checked += 1
        fm = _parse_frontmatter(skill_dir)

        if fm is None:
            continue  # SKILL.md missing — already excluded above

        if fm == {}:
            failures.append(
                FailureDetail(
                    location=f"01_Skills/{skill_dir.name}/SKILL.md",
                    expected="frontmatter block (---\\nname: ...\\n---) at top of file",
                    actual="no frontmatter",
                    severity="warning",
                    hint="SKILL.md sollte frontmatter mit name+description+version haben (draft-skill?)",
                )
            )
            continue

        local_failures: list[FailureDetail] = []
        for field in REQUIRED_FRONTMATTER_FIELDS:
            if field not in fm or fm[field] in (None, "", []):
                local_failures.append(
                    FailureDetail(
                        location=f"01_Skills/{skill_dir.name}/SKILL.md",
                        expected=f"frontmatter field '{field}' present and non-empty",
                        actual=f"'{field}' missing or empty",
                        severity="warning",
                        hint=f"{skill_dir.name}: '{field}'-Feld in YAML-Frontmatter ergaenzen",
                    )
                )
        if local_failures:
            failures.extend(local_failures)
        else:
            n_passed += 1

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="skill_frontmatter",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
