"""paragraph-18-sync auto-invoke reminder (Pre-Commit-Hook, Layer 3 Defense-in-Depth).

Spec: INSTRUKTIONEN.md P18.0 (NEU 2026-05-23 spätabends, v2.5).

Advisory WARN. Scant die als CLI-Args übergebenen staged-files gegen das P18-File-
Set; wenn EIN Match → stderr-WARN + Recovery-Hint; exit 0 (kein Hard-Block).

Bypass: ENV `PARA18_VERIFIED=1` → silent + exit 0 (zu setzen NACH `!ParaSync18 <event>`
Validator-Pass mit exit 0). Bypass ist explizit; nicht via `--no-verify`-Hook-Skip.

Hook-Vertrag analog crlf_guard.py: non-mutierend, language: system, pass_filenames: true.
"""

from __future__ import annotations

import os
import re
import sys

# Windows-Console cp1252 safety (Memory feedback_windows_console_ascii_safe_inline_python).
# Hook scant Args + writes ASCII-only stderr; reconfigure ist Belt-and-suspenders.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except AttributeError, OSError:
    pass

# Pattern-Set P18.0 — file-pattern-driven Auto-Invoke-Trigger.
# Doppelte Pflege gegen INSTRUKTIONEN P18.0 + CLAUDE.md Routing-Table = bewusst:
# pre-commit-Hook muss standalone funktionieren (kein Yaml-SSoT-Load zur Hook-Zeit).
_SYNC_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"^00_Core/(PIPELINE|PORTFOLIO|CORE-MEMORY|Faktortabelle|SYSTEM|STATE)\.md$"),
    re.compile(r"^07_Obsidian Vault/.+/log\.md$"),
    re.compile(r"^05_Archiv/(score_history|flag_events)\.jsonl$"),
    re.compile(r"^01_Skills/dynastie-depot/config\.yaml$"),
    re.compile(r"^01_Skills/[^/]+/SKILL\.md$"),
    re.compile(
        r"^03_Tools/(Rebalancing_Tool|Satelliten_Monitor|Watchlist_Ersatzbank_Monitor)_v[0-9.]+\.xlsx$"
    ),
)


def _classify_events(matched_files: list[str]) -> list[str]:
    """Infer event-types per P18.0 from matched files. Returns sorted, deduped list."""
    events: set[str] = set()
    for f in matched_files:
        norm = f.replace("\\", "/")
        if any(
            token in norm
            for token in (
                "PORTFOLIO.md",
                "Faktortabelle.md",
                "score_history.jsonl",
                "flag_events.jsonl",
                "dynastie-depot/config.yaml",
                "Rebalancing_Tool",
                "Satelliten_Monitor",
            )
        ):
            events.add("score-flag-sparraten")
        if norm.endswith("00_Core/PIPELINE.md"):
            events.add("pipeline-item")
        if norm.endswith("00_Core/SYSTEM.md") or re.match(r"^01_Skills/[^/]+/SKILL\.md$", norm):
            events.add("system-zustand")
        if norm.endswith("00_Core/STATE.md"):
            events.add("critical-alert")
        if "log.md" in norm or "CORE-MEMORY.md" in norm:
            # CORE-MEMORY + log.md are sync-targets, not event-classifiers themselves.
            # If they're the only matches, fall back to pipeline-item as the most-common
            # event-type so the user gets a non-empty suggestion.
            events.add((events and next(iter(events))) or "pipeline-item")
    if not events:
        events.add("pipeline-item")
    return sorted(events)


def main(argv: list[str]) -> int:
    if os.environ.get("PARA18_VERIFIED") == "1":
        # User has manually run !ParaSync18 and confirmed PASS. Silent pass.
        return 0

    staged = [a for a in argv[1:] if a]
    matched = [f for f in staged if any(p.match(f.replace("\\", "/")) for p in _SYNC_PATTERNS)]
    if not matched:
        return 0

    events = _classify_events(matched)
    primary = events[0]
    also = " ".join(f"--also {e}" for e in events[1:])

    sys.stderr.write(
        "\n"
        "================================================================================\n"
        " P18 AUTO-INVOKE-REMINDER (paragraph-18-sync, INSTRUKTIONEN P18.0)\n"
        "================================================================================\n"
        f" Staged P18-Files erkannt ({len(matched)}):\n"
    )
    for f in matched:
        sys.stderr.write(f"   - {f}\n")
    sys.stderr.write(
        "\n"
        f" Inferred event-type(s): {', '.join(events)}\n"
        f" Empfohlener Skill-Call (vor `git commit`):\n"
        f"   !ParaSync18 {primary}"
    )
    if also:
        sys.stderr.write(f" {also}")
    sys.stderr.write(
        "\n\n"
        " Bypass (NACH manuellem Validator-Pass): set PARA18_VERIFIED=1\n"
        " Doktrin: 00_Core/INSTRUKTIONEN.md P18.0 + CLAUDE.md Routing-Table P18-File-Touch\n"
        "================================================================================\n"
        " (advisory WARN — Commit läuft weiter; Hook blockt NICHT.)\n"
        "\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
