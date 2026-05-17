"""crlf-guard pre-commit-Hook (Spec §4.3) — Laufzeit-Netz gegen CRLF.

Byte-Level `\\r\\n`-Reject auf staged `*.jsonl *.patch *.py *.md`, fail-close.
Redundanz zu `.gitattributes` ist gewollt (defense-in-depth: `.gitattributes`
greift nicht bei `core.autocrlf`-Fehlkonfig auf fremder Maschine — Memory
`feedback_windows_python_crlf_text_mode`).

Aufruf: pre-commit übergibt die staged Pfade als argv (`language: system`).
Stand-alone CLI ohne Projekt-Imports — bewusst kein schemas.py-Bootstrap.
"""

from __future__ import annotations

import contextlib
import sys
from pathlib import Path

with contextlib.suppress(Exception):
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]


def find_crlf(paths: list[str]) -> list[str]:
    """Return the subset of paths whose bytes contain a CRLF sequence."""
    offenders: list[str] = []
    for p in paths:
        path = Path(p)
        if not path.is_file():
            continue
        if b"\r\n" in path.read_bytes():
            offenders.append(p)
    return offenders


def main(argv: list[str] | None = None) -> int:
    paths = list(sys.argv[1:]) if argv is None else argv
    offenders = find_crlf(paths)
    if offenders:
        for p in offenders:
            print(
                f"❌ crlf-guard: CRLF (\\r\\n) detected in '{p}' — "
                f"LF-only required (Spec §4.2/§4.3)",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
