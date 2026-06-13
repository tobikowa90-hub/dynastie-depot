"""Deterministic primitives for backtest-ready-forward-verify skill.

Separated from SKILL.md because schema/STATE/git/MigrationEvent manipulation
is Python territory — the skill only orchestrates (Markdown prosa).

Lives in 03_Tools/backtest-ready/ next to schemas.py so `from schemas import ...`
works directly. Smoke test adds this directory to sys.path.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Literal

from schemas import MigrationEvent

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Required-Touch set for freshness gate (basenames only — matched against
# git-status output by basename so path prefix is irrelevant).
REQUIRED_TOUCH_FILES = ("PORTFOLIO.md", "Faktortabelle.md", "log.md")

# DEFCON emoji → numeric level mapping
_DEFCON_EMOJI: dict[str, int] = {
    "\U0001f7e2": 4,  # 🟢
    "\U0001f7e1": 3,  # 🟡
    "\U0001f7e0": 2,  # 🟠
    "\U0001f534": 1,  # 🔴
}

# Pre-compiled: strips **...** bold-wrap from a cell value
_RE_BOLD = re.compile(r"\*\*(.+?)\*\*")

# Pre-compiled: matches a markdown table row split on |
_RE_TABLE_ROW = re.compile(r"^\s*\|(.+)\|\s*$")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _strip_bold(s: str) -> str:
    """Remove all **...**  bold markers from string."""
    return _RE_BOLD.sub(r"\1", s)


def _cells_from_row(line: str) -> list[str] | None:
    """Parse a markdown table row into a list of cell strings (stripped).

    Returns None if the line is not a table row.
    Handles arbitrary whitespace around pipes.
    """
    m = _RE_TABLE_ROW.match(line)
    if not m:
        return None
    inner = m.group(1)
    # Split by | and strip; leading/trailing empties are from the outer pipes
    parts = [p.strip() for p in inner.split("|")]
    return parts


def _parse_defcon(cell: str) -> int:
    """Extract DEFCON numeric level from cell.  Handles bold-wrap.

    Cell examples: '🟢 4', '**🟠 2**', '🟡 3'
    """
    clean = _strip_bold(cell).strip()
    # Find leading emoji character
    for emoji, level in _DEFCON_EMOJI.items():
        if emoji in clean:
            return level
    # Fallback: try to extract trailing digit
    m = re.search(r"([1-4])\s*$", clean)
    if m:
        return int(m.group(1))
    raise ValueError(f"Cannot parse DEFCON level from cell: {cell!r}")


def _parse_score(cell: str) -> int:
    """Extract integer score from cell.  Handles bold-wrap (**63**)."""
    clean = _strip_bold(cell).strip()
    return int(clean)


def _parse_flags_active(cell: str) -> bool:
    """Return True iff the FLAG cell begins with 🔴 (hard active flag).

    Rules (from spec):
      ✅           → False (no flag)
      ✅ (...)     → False (no flag, parenthetical note)
      ⚠️ ...       → False (watch, not hard flag)
      🔴 ...       → True  (active flag)

    Bold-wrap and leading whitespace are stripped first.
    ⚠️ is U+26A0 + U+FE0F (variation selector); we match on U+26A0 alone.
    """
    clean = _strip_bold(cell).strip()
    # 🔴 is U+1F534
    return clean.startswith("\U0001f534")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def parse_wrapper(path: str) -> tuple[dict, dict]:
    """Read draft JSON from path. Return (record_dict, skill_meta_dict).

    Expected JSON structure::

        {
            "record": { ...ScoreRecord fields... },
            "skill_meta": { ...optional migration info... }
        }

    - If ``skill_meta`` is absent or empty dict: return ({...record...}, {}).
    - If ``skill_meta`` is present and non-empty: validate that all 3 required
      keys are present (expected_algebra_score, migration_from_version,
      migration_to_version).  Raise ValueError if incomplete.
    """
    p = Path(path)
    with p.open("r", encoding="utf-8") as fh:
        draft = json.load(fh)

    if "record" not in draft:
        raise ValueError(
            f"draft JSON at {path!r} missing 'record' key — "
            "expected wrapper format {'record': {...}, 'skill_meta': {...}}"
        )

    record_dict: dict = draft["record"]
    skill_meta: dict = draft.get("skill_meta", {}) or {}

    if skill_meta:
        required = {"expected_algebra_score", "migration_from_version", "migration_to_version"}
        missing = required - set(skill_meta.keys())
        if missing:
            raise ValueError(
                f"skill_meta is present but incomplete — missing keys: {sorted(missing)}"
            )

    return record_dict, skill_meta


def parse_state_row(ticker: str, state_md_content: str) -> dict:
    """Extract ``{score: int, defcon: int, flags_active: bool}`` for *ticker*
    from PORTFOLIO.md Portfolio-Tabelle.

    Handles:
    - Bold-wrap on any cell (``**63**``, ``**🟠 2**``, ``**17,81€**``)
    - All 4 DEFCON emojis (🟢🟡🟠🔴 → 4/3/2/1)
    - FLAG column variants: ``✅``, ``✅ (...)``, ``⚠️ ...``, ``🔴 ...``
    - Tickers with dots (``BRK.B``)
    - Arbitrary whitespace around pipes

    Table column order (Ticker-relative — robust to leading columns):
        Ticker  Ticker+1=Score  Ticker+2=DEFCON  Ticker+3=Rate  Ticker+4=FLAG
    The 2026-06 Umstrukturierung prepended a "Tier" column (Tier|Ticker|Score|
    DEFCON|Rate|FLAG|Trigger), so Ticker is no longer guaranteed to be column 0.
    Score/DEFCON/Rate/FLAG keep their order relative to Ticker in both the pre-
    and post-restructure layouts, so we locate the Ticker cell and read the
    others at fixed offsets from it.

    Raises:
        ValueError: if ticker is not found in any table row.
    """
    for line in state_md_content.splitlines():
        cells = _cells_from_row(line)
        if cells is None or len(cells) < 5:
            continue
        # Locate the Ticker cell dynamically (strip bold for exact match)
        ticker_idx = next(
            (i for i, c in enumerate(cells) if _strip_bold(c).strip() == ticker),
            None,
        )
        if ticker_idx is None or ticker_idx + 4 >= len(cells):
            continue
        # Found the row — extract columns relative to the Ticker column
        score = _parse_score(cells[ticker_idx + 1])
        defcon = _parse_defcon(cells[ticker_idx + 2])
        flags_active = _parse_flags_active(cells[ticker_idx + 4])
        return {"score": score, "defcon": defcon, "flags_active": flags_active}

    raise ValueError(f"ticker '{ticker}' not found in PORTFOLIO.md")


def build_migration_event(
    skill_meta: dict,
    forward_score: float,
) -> tuple[MigrationEvent, str]:
    """Always builds a MigrationEvent (never None).

    Returns ``(event, outcome_label)`` where outcome_label is:

    - ``""`` (empty string) for ``outcome="accepted"``
    - ``"PFLICHT: CORE-MEMORY §5 ..."``  for ``outcome="log_only"``
    - ``"STOP: §28.2 |Δ|=<N> > 5 ..."``  for ``outcome="block"``

    *delta* is signed (forward_score − algebra_score).

    The bucketing logic is duplicated between this helper and the MigrationEvent
    schema validator by design (defense-in-depth).  If they disagree, the
    pydantic model_validate call will raise — this is the intended double-check.
    """
    algebra = float(skill_meta["expected_algebra_score"])
    from_version: str = skill_meta["migration_from_version"]
    to_version: str = skill_meta["migration_to_version"]

    delta = round(forward_score - algebra, 6)
    abs_delta = abs(delta)

    if abs_delta <= 2:
        outcome: Literal["accepted", "log_only", "block"] = "accepted"
    elif abs_delta <= 5:
        outcome = "log_only"
    else:
        outcome = "block"

    # Build and validate via pydantic (double-check: schema re-validates bucketing)
    event = MigrationEvent.model_validate(
        {
            "from_version": from_version,
            "to_version": to_version,
            "algebra_score": algebra,
            "forward_score": float(forward_score),
            "delta": delta,
            "outcome": outcome,
        }
    )

    # Build the fan-out signal string
    if outcome == "accepted":
        signal = ""
    elif outcome == "log_only":
        signal = (
            "PFLICHT: CORE-MEMORY §5 Eintrag für Migration-Event (log_only outcome). "
            "Siehe INSTRUKTIONEN §28.2."
        )
    else:  # block
        signal = (
            f"STOP: §28.2 |Δ|={abs_delta:g} > 5. Fan-Out (7 Oberflächen) blockiert "
            f"bis Algebra-Ursache identifiziert. Siehe CORE-MEMORY §5. "
            f"JSONL-Commit läuft durch — Record ist Historie-relevant."
        )

    return event, signal


def check_freshness(repo_root: str) -> list[str]:
    """Run ``git status --porcelain=v1 -z`` from *repo_root*.

    Check which of the three REQUIRED_TOUCH_FILES (PORTFOLIO.md, Faktortabelle.md,
    log.md) are **not** modified (i.e., not shown in git status output).

    Returns the list of missing (not-modified) filenames.  Empty list = all fresh.

    Conditional files (CORE-MEMORY.md, config.yaml) are **not** checked — they
    only touch on content changes, and the plan rejects including them to avoid
    alert fatigue.

    Matches files by basename, so ``00_Core/PORTFOLIO.md`` in git output maps to
    ``PORTFOLIO.md``.

    Format spec (``man git-status``, porcelain v1 with ``-z``):

    - Normal entry:  ``XY SP <path> NUL``
    - Rename/Copy:   ``XY SP <path1> NUL <path2> NUL``
      (status R/C — both old and new path consumed; basename added for both
      so a rename of PORTFOLIO.md still counts as touched.)

    The ``-z`` mode disables filename quoting / backslash-escaping, so paths
    with spaces, Umlauts, embedded newlines, or other special chars survive
    the round-trip intact (PIPELINE #22).
    """
    # CR 2026-05-07: timeout=30 verhindert indefinite-block (NFS, locked .git/index,
    # huge untracked-trees). FileNotFoundError-Catch fängt git-fehlt-im-PATH +
    # repo_root-existiert-nicht (subprocess.run wirft FileNotFoundError BEVOR
    # returncode existiert). Returncode-Check verhindert silent „alle unmodified"
    # bei nicht-Repo / Permissions. Alle drei Fehlermodi → RuntimeError mit
    # klarem repo_root-Kontext.
    # PIPELINE #22 (2026-05-09): kein encoding= → bytes-mode, da -z literal NUL
    # ausgibt (NUL ist nicht text-decodable als field separator).
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain=v1", "-z"],
            cwd=repo_root,
            capture_output=True,
            timeout=30,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"git status timed out after 30s in {repo_root}") from exc
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"git status could not run in {repo_root} "
            f"(git nicht installiert oder repo_root existiert nicht): {exc}"
        ) from exc
    if result.returncode != 0:
        stderr_str = (result.stderr or b"").decode("utf-8", errors="replace").strip()
        stdout_str = (result.stdout or b"").decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"git status failed in {repo_root} (returncode={result.returncode}): "
            f"{stderr_str or stdout_str or '(no output)'}"
        )

    modified_basenames: set[str] = set()
    # Each entry is NUL-terminated; the trailing NUL after the last entry yields
    # an empty trailing token after split — drop it.
    entries = result.stdout.split(b"\x00")
    if entries and not entries[-1]:
        entries.pop()

    i = 0
    while i < len(entries):
        entry = entries[i]
        # Layout: XY (2 bytes) + space (1 byte) + path bytes
        if len(entry) < 4:
            i += 1
            continue
        xy = entry[:2]
        path_str = entry[3:].decode("utf-8", errors="replace")
        modified_basenames.add(Path(path_str).name)

        # Rename (R) or Copy (C) status: NEXT entry is the second path
        # (no XY prefix, raw path bytes — git docs: in -z mode "from" follows "to").
        # Accept R/C in either index (porcelain XY can be 'R ', ' R', 'RM', etc.).
        if (xy[0:1] in (b"R", b"C") or xy[1:2] in (b"R", b"C")) and i + 1 < len(entries):
            second_path = entries[i + 1].decode("utf-8", errors="replace")
            modified_basenames.add(Path(second_path).name)
            i += 2
            continue
        i += 1

    missing = [fname for fname in REQUIRED_TOUCH_FILES if fname not in modified_basenames]
    return missing
