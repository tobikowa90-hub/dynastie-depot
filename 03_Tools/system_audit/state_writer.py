"""Idempotent Last-Audit-block writer for STATE.md.

Spec §6.5 + Codex-Patch P5: HTML-comment markers define a unique replacement region.
Atomic write via tmp-file + os.replace.
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

START_MARKER = "<!-- system-audit:last-audit:start -->"
END_MARKER = "<!-- system-audit:last-audit:end -->"
FOOTER_SENTINEL = "🦅 STATE.md v"


def _build_block(timestamp_utc: str, summary: str, run_cmd: str) -> str:
    return (
        f"{START_MARKER}\n"
        "---\n\n"
        "## 🔍 Last Audit\n\n"
        f"**Timestamp (UTC):** {timestamp_utc}\n"
        f"**Result:** {summary}\n"
        f"**Run:** `{run_cmd}`\n"
        "**Full-Report:** stdout (kein Archiv-File)\n\n"
        f"{END_MARKER}\n"
    )


def write_last_audit(
    state_path: Path,
    *,
    timestamp_utc: str,
    summary: str,
    run_cmd: str,
) -> None:
    text = state_path.read_text(encoding="utf-8")
    has_start = START_MARKER in text
    has_end = END_MARKER in text
    if has_start and not has_end:
        raise RuntimeError(
            f"STATE.md Marker-Block inkonsistent (start-Marker ohne end-Marker) — manuell fixen: {state_path}"
        )

    block = _build_block(timestamp_utc, summary, run_cmd)

    if has_start and has_end:
        start_idx = text.index(START_MARKER)
        end_idx = text.index(END_MARKER) + len(END_MARKER)
        if end_idx < len(text) and text[end_idx] == "\n":
            end_idx += 1
        new_text = text[:start_idx] + block + text[end_idx:]
    else:
        footer_idx = text.rfind(FOOTER_SENTINEL)
        if footer_idx == -1:
            new_text = text.rstrip() + "\n\n" + block
        else:
            line_start = text.rfind("\n", 0, footer_idx) + 1
            new_text = text[:line_start] + block + "\n" + text[line_start:]

    tmp = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", delete=False,
        dir=state_path.parent, prefix=".state_audit_", suffix=".tmp",
    )
    try:
        tmp.write(new_text)
        tmp.close()
        os.replace(tmp.name, state_path)
    except Exception:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass
        raise
