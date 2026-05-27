"""Check-4: Backtick-wrapped path references must resolve to existing files.

Spec §5.1 Check-4 + Codex-Patch P3. Scope: CLAUDE.md + STATE.md + PORTFOLIO.md +
PIPELINE.md + SYSTEM.md + SESSION-HANDOVER.md + Pipeline-SSoT-referenzierte Plans
(NOT glob all plans). Ignoriert URLs, Wikilinks `[[...]]`, Code-Fences,
Whitelist-Pfade.

False-Positive-Filter (2026-05-06):
- Memory-File-Pattern (`feedback_*.md`, `reference_*.md`, `user_*.md`,
  `project_*.md` ohne Slash) → skip (lebt in `~/.claude/.../memory/`).
- Bare-Filename ohne Slash (Prosa-Mention wie `archive_flag.py`,
  `STATE.md`) → skip wenn weder repo-relativ existent noch bekannte Memory-Klasse.
- Alias `00_Core/log.md` → resolve auf
  `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md`
  (Shorthand-Konvention, dokumentiert in SESSION-HANDOVER.md).
"""

from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.audit_types import AuditContext, CheckResult, FailureDetail

# PATH_RE rejects whitespace in paths by design — backtick-path-refs in Dynasty-Depot
# Konvention nutzen keine Spaces. Pfade mit Spaces (e.g. "07_Obsidian Vault/...") werden
# nicht gecheckt — das ist bewusst, verhindert false-positives auf prose-text-matches.
PATH_RE = re.compile(r"`([^\s`]+\.(py|md|yaml|yml|jsonl|xlsx|zip|sh|ps1))`")
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")

WHITELIST_PREFIXES = (
    "_drafts/",
    "node_modules/",
    ".git/",
    "venv/",
    "__pycache__/",
    "http://",
    "https://",
    "~/",  # User-Home-Refs (z.B. `~/.claude/CLAUDE.md`) liegen außerhalb Repo.
)

# Auto-Memory-Files leben außerhalb des Repos in `~/.claude/.../memory/`. Bare-Mentions
# in Prosa wie `feedback_xyz.md` sind dokumentarische Pointer, keine Repo-Refs.
MEMORY_FILE_RE = re.compile(r"^(feedback|reference|user|project)_[\w-]+\.md$")

# Shorthand-Alias-Resolution: `00_Core/log.md` ist Convention für die Vault-log.md.
# Dokumentiert in SESSION-HANDOVER.md (Path-Shorthand-Hint).
ALIAS_RESOLUTIONS = {
    "00_Core/log.md": "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md",
}

# Plan-Files unter `docs/superpowers/plans/` beschreiben Target-Architektur und
# enthalten häufig forward-declared Refs (Tools, die der Plan erst bauen wird) —
# Findings dort als WARN markieren statt FAIL. Active-Core-Refs bleiben unverändert
# error-severity.
PLAN_PATH_PREFIX = "docs/superpowers/plans/"


def _iter_text_without_fences(text: str):
    """Yield (lineno, line) skipping fenced code blocks."""
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield lineno, line


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    scan_files_override: list[Path] | None = None,
) -> CheckResult:
    start = time.monotonic()

    base = [
        repo_root / "CLAUDE.md",
        repo_root / "00_Core" / "STATE.md",
        repo_root / "00_Core" / "PORTFOLIO.md",
        repo_root / "00_Core" / "PIPELINE.md",
        repo_root / "00_Core" / "SYSTEM.md",
        repo_root / "00_Core" / "SESSION-HANDOVER.md",
    ]
    pipeline_plans: list[Path] = []

    if scan_files_override is None:
        pipeline_path = repo_root / "00_Core" / "PIPELINE.md"
        if pipeline_path.exists():
            # Forward-dependency on Task 9 Check-6 — guard gracefully.
            try:
                from system_audit.checks.pipeline_ssot import extract_plan_refs

                refs = extract_plan_refs(pipeline_path.read_text(encoding="utf-8"))
                pipeline_plans = [repo_root / r for r in refs if (repo_root / r).exists()]
            except ImportError:
                pipeline_plans = []  # Check-6 not yet implemented; skip plan-ref augmentation
        scan_files = base + pipeline_plans
    else:
        scan_files = scan_files_override

    legacy_handover = repo_root / "SESSION-HANDOVER.md"

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    for src in scan_files:
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        for lineno, line in _iter_text_without_fences(text):
            clean = WIKILINK_RE.sub("", line)
            for m in PATH_RE.finditer(clean):
                raw = m.group(1)
                if any(raw.startswith(p) for p in WHITELIST_PREFIXES):
                    continue
                # Memory-File-Pattern: lebt außerhalb Repo, Mention nicht Ref.
                if MEMORY_FILE_RE.match(raw):
                    continue
                # Bare-Filename ohne Slash: Prosa-Mention, kein Path-Ref.
                # (Echte Pfade in diesem Repo haben mindestens einen Folder-Prefix.)
                if "/" not in raw:
                    continue
                if (
                    raw.endswith("SESSION-HANDOVER.md")
                    and "00_Core" not in raw
                    and legacy_handover.exists()
                ):
                    n_checked += 1
                    failures.append(
                        FailureDetail(
                            location=f"{src.relative_to(repo_root) if src.is_relative_to(repo_root) else src}:{lineno}",
                            expected="00_Core/SESSION-HANDOVER.md (canonical path)",
                            actual=raw,
                            severity="error",
                            hint="Kanonischer Pfad 00_Core/SESSION-HANDOVER.md verwenden",
                        )
                    )
                    continue
                # Alias-Resolution (Shorthand-Konvention).
                resolved = ALIAS_RESOLUTIONS.get(raw, raw)
                n_checked += 1
                target = repo_root / resolved if not resolved.startswith("/") else Path(resolved)
                if target.exists():
                    n_passed += 1
                else:
                    src_rel = str(
                        src.relative_to(repo_root) if src.is_relative_to(repo_root) else src
                    ).replace("\\", "/")
                    severity = "warning" if src_rel.startswith(PLAN_PATH_PREFIX) else "error"
                    failures.append(
                        FailureDetail(
                            location=f"{src.relative_to(repo_root) if src.is_relative_to(repo_root) else src}:{lineno}",
                            expected="referenced path exists",
                            actual=raw,
                            severity=severity,
                            hint="Pfad umbenannt/geloescht? Referenz aktualisieren",
                        )
                    )

    has_error = any(f.severity == "error" for f in failures)
    has_warning = any(f.severity == "warning" for f in failures)
    if has_error:
        status = "FAIL"
    elif has_warning:
        status = "WARN"
    else:
        status = "PASS"

    return CheckResult(
        name="existence",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
