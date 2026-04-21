"""Check-5: SKILL.md frontmatter `version:` vs 06_Skills-Pakete/<skill>_vX.Y.Z.zip.

Spec §5.1 Check-5. Higher SKILL.md version than any ZIP -> warning (not yet packaged).
Orphan ZIP without SKILL.md -> warning.
"""
from __future__ import annotations

import re
import time
from pathlib import Path

import yaml

from system_audit.types import AuditContext, CheckResult, FailureDetail

ZIP_VERSION_RE = re.compile(r"_v(\d+)\.(\d+)\.(\d+)\.zip$")


def _parse_semver(s: str) -> tuple[int, int, int] | None:
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", s.strip().lstrip("v"))
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def _skill_version(skill_dir: Path) -> tuple[int, int, int] | None:
    md = skill_dir / "SKILL.md"
    if not md.exists():
        return None
    text = md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None
    try:
        _, fm, _ = text.split("---", 2)
        data = yaml.safe_load(fm) or {}
    except (ValueError, yaml.YAMLError):
        return None
    v = data.get("version")
    return _parse_semver(str(v)) if v else None


def _zip_versions(packages_dir: Path, skill_name: str) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for zf in packages_dir.glob(f"{skill_name}_v*.zip"):
        m = ZIP_VERSION_RE.search(zf.name)
        if m:
            out.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))
    return sorted(out)


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()

    skills_dir = repo_root / "01_Skills"
    packages_dir = repo_root / "06_Skills-Pakete"
    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    if not skills_dir.exists():
        return CheckResult(
            name="skill_version", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location="01_Skills/", expected="skills dir", actual="missing",
                severity="warning", hint="Struktur geaendert?",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    for skill_dir in skills_dir.iterdir():
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        skill_name = skill_dir.name
        md_ver = _skill_version(skill_dir)
        if md_ver is None:
            continue
        n_checked += 1
        zip_vers = _zip_versions(packages_dir, skill_name)
        if not zip_vers:
            failures.append(FailureDetail(
                location=f"01_Skills/{skill_name}/SKILL.md",
                expected=f"ZIP 06_Skills-Pakete/{skill_name}_v{'.'.join(map(str, md_ver))}.zip",
                actual="no ZIPs found",
                severity="warning",
                hint="Skill-Packaging ausstehend",
            ))
            continue
        highest = zip_vers[-1]
        if highest < md_ver:
            failures.append(FailureDetail(
                location=f"01_Skills/{skill_name}/SKILL.md",
                expected=f"ZIP matches v{'.'.join(map(str, md_ver))}",
                actual=f"highest ZIP v{'.'.join(map(str, highest))}",
                severity="warning",
                hint="Neu-Packen vor Release",
            ))
        else:
            n_passed += 1

    if packages_dir.exists():
        existing_skill_names = {d.name for d in skills_dir.iterdir() if d.is_dir()}
        for zf in packages_dir.glob("*_v*.zip"):
            m = re.match(r"^(.+?)_v\d+\.\d+\.\d+\.zip$", zf.name)
            if m and m.group(1) not in existing_skill_names:
                failures.append(FailureDetail(
                    location=f"06_Skills-Pakete/{zf.name}",
                    expected="matching 01_Skills/<name>/",
                    actual="orphan ZIP",
                    severity="warning",
                    hint="Skill-Dir entfernt? ZIP archivieren",
                ))

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="skill_version", status=status,  # type: ignore[arg-type]
        n_checked=n_checked, n_passed=n_passed, failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
