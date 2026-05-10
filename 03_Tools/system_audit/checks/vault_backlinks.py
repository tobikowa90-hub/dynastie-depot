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
# Inline-Code-Spans (single backticks) und Schema-Beispiele wie `[[Page Title]]`
# sind dokumentarische Mentions, keine echten Wikilinks. Strip-vor-Match um
# False-Positives auf Convention-Beispiele (WIKI-SCHEMA.md, log.md Pass-Notes,
# archive/log historisierte Refs) zu vermeiden.
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    timeout_s = context.vault_timeout_s
    vault = repo_root / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind"
    if not vault.exists():
        return CheckResult(name="vault_backlinks", status="SKIP", n_checked=0, n_passed=0,
                           failures=[], duration_ms=0, category="optional")

    # Notes-Set inkludiert raw/-Files als valide Wikilink-Targets (Obsidian sieht
    # sie als Vault-Notes), aber wir scannen sie nicht für outgoing wikilinks
    # (raw-Imports sind unkurriert, ihre internen Links sind irrelevant).
    # Plus Frontmatter-Aliases pro Note: Obsidian resolved `[[Clifford S. Asness]]`
    # auf eine Note `clifford-asness.md` mit `aliases: ["Clifford S. Asness"]`.
    # Ohne Alias-Resolution würden alle Author-Stubs mit Full-Name-Refs als
    # dangling falsch-positiv getriggert (siehe 2026-05-10 Audit-Run, 8 Findings).
    notes = set()
    alias_re = re.compile(r"^aliases:\s*$\n((?:^\s+-\s.+$\n?)+)", re.MULTILINE)
    alias_item_re = re.compile(r'^\s+-\s+"?([^"\n]+?)"?\s*$', re.MULTILINE)
    for p in vault.rglob("*.md"):
        notes.add(p.stem)
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # Nur Frontmatter (zwischen den ersten zwei `---`-Markern) für Aliases scannen.
        if not text.startswith("---"):
            continue
        fm_end = text.find("\n---", 4)
        if fm_end < 0:
            continue
        fm = text[4:fm_end]
        m = alias_re.search(fm)
        if not m:
            continue
        for am in alias_item_re.finditer(m.group(1)):
            notes.add(am.group(1).strip())

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    for md in vault.rglob("*.md"):
        md_path = str(md).replace("\\", "/")
        if "/raw/" in md_path:
            continue
        # Frozen historic archive (Quartals-Rollover per INSTRUKTIONEN §18.6).
        # Analog log_lag-Konvention: archive/log/ ist read-only, dangling Refs
        # auf nie-indexierte Notes (z.B. Video-Titel-Plan-Pages) sind historisch
        # akzeptabel und sollen nicht actionable getriggert werden.
        if "/archive/log/" in md_path:
            continue
        if (time.monotonic() - start) > timeout_s:
            return CheckResult(
                name="vault_backlinks", status="SKIP", n_checked=n_checked, n_passed=n_passed,
                failures=[*failures, FailureDetail(
                    location="vault_backlinks", expected=f"scan < {timeout_s}s",
                    actual="timed out", severity="warning", hint="Scope reduzieren oder Timeout erhöhen",
                )],
                duration_ms=int((time.monotonic() - start) * 1000),
                category="optional",
            )
        in_fence = False
        for lineno, raw_line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if raw_line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = INLINE_CODE_RE.sub("", raw_line)
            for m in WIKILINK_RE.finditer(line):
                n_checked += 1
                # Markdown-Table-Pipe-Escape: `[[BRKB\|BRK.B]]` in Tabellen-Zellen
                # ist die korrekte Schreibweise (Pipe muss escaped werden, sonst
                # parst Markdown ihn als Cell-Separator). Regex captured trailing
                # backslash → strip vor Resolution.
                target = m.group(1).strip().rstrip("\\")
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
