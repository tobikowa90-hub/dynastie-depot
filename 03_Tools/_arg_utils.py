"""Argument helpers — Token-Match statt Substring (L1 preventive).

governance_parity FLAG-Cell-Substring-Match (historical bug) ist bereits
via FLAG_TOKEN_RE-Tokenisierung gefixt; dieser Helper ist preventive für
Future-Sites die argv-Flags prüfen.

Verwendung:
    if flag_match(argv, "--force"):
        ...   # exakter Token, nicht Substring in "--force-recompute"
"""

from __future__ import annotations

from collections.abc import Iterable


def flag_match(args: Iterable[str], flag: str) -> bool:
    """Return True iff `flag` appears as exact token in `args`.

    Substring-safe: `flag_match(["--force-recompute"], "--force")` → False.

    Args:
        args: argv-like iterable of strings.
        flag: exact token to match (typically `--name` or `-x`).
    """
    return any(arg == flag for arg in args)
