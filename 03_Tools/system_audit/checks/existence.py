"""Check-4: Backtick-wrapped path references must resolve to existing files.

Spec §5.1 Check-4 + Codex-Patch P3. Scope: CLAUDE.md + STATE.md + PORTFOLIO.md +
PIPELINE.md + SYSTEM.md + SESSION-HANDOVER.md + Pipeline-SSoT-referenzierte Plans
(NOT glob all plans). Ignoriert URLs, Wikilinks `[[...]]`, Code-Fences,
Whitelist-Pfade.
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from system_audit.types import AuditContext, CheckResult, FailureDetail

# PATH_RE rejects whitespace in paths by design — backtick-path-refs in Dynasty-Depot
# Konvention nutzen keine Spaces. Pfade mit Spaces (e.g. "07_Obsidian Vault/...") werden
# nicht gecheckt — das ist bewusst, verhindert false-positives auf prose-text-matches.
PATH_RE = re.compile(r"`([^\s`]+\.(py|md|yaml|yml|jsonl|xlsx|zip|sh|ps1))`")
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")

WHITELIST_PREFIXES = (
    "_drafts/", "node_modules/", ".git/", "venv/", "__pycache__/",
    "http://", "https://",
)


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
                if raw.endswith("SESSION-HANDOVER.md") and "00_Core" not in raw and legacy_handover.exists():
                    n_checked += 1
                    failures.append(FailureDetail(
                        location=f"{src.relative_to(repo_root) if src.is_relative_to(repo_root) else src}:{lineno}",
                        expected="00_Core/SESSION-HANDOVER.md (canonical path)",
                        actual=raw,
                        severity="error",
                        hint="Kanonischer Pfad 00_Core/SESSION-HANDOVER.md verwenden",
                    ))
                    continue
                n_checked += 1
                target = repo_root / raw if not raw.startswith("/") else Path(raw)
                if target.exists():
                    n_passed += 1
                else:
                    failures.append(FailureDetail(
                        location=f"{src.relative_to(repo_root) if src.is_relative_to(repo_root) else src}:{lineno}",
                        expected="referenced path exists",
                        actual=raw,
                        severity="error",
                        hint="Pfad umbenannt/geloescht? Referenz aktualisieren",
                    ))

    has_error = any(f.severity == "error" for f in failures)
    status = "FAIL" if has_error else "PASS"

    return CheckResult(
        name="existence", status=status,  # type: ignore[arg-type]
        n_checked=n_checked, n_passed=n_passed, failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
