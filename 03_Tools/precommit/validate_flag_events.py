"""validate-flag-events pre-commit-Hook (Spec §3.3).

Validiert staged `flag_events.jsonl` gegen das kanonische `FlagEvent`-Schema
(`03_Tools/backtest-ready/schemas.py` — identisch zu dem Schema, das
`archive_flag.py` beim Write nutzt; kein Schema-Doppel-SSoT).

Fail-close: Byte-Level-CRLF / JSON-Parse / Schema-Verstoß → EXIT 1.
WARN-only: Open/Resolve-Paarungs-Anomalie → stderr, KEIN EXIT 1.
Begründung WARN statt fail-close: offene FLAGs leben Cross-File auch in
PORTFOLIO.md; ein pre-commit-Hook sieht nur das jsonl — harte Blockade hier
erzeugte False-Positives auf legitime Out-of-Band-Resolves. Schema/CRLF sind
rein lokal entscheidbar → fail-close korrekt.

Aufruf: pre-commit übergibt die staged Pfade als argv (`language: system`).
"""

from __future__ import annotations

import contextlib
import json
import sys
from pathlib import Path

# schemas.py-Bootstrap analog validate_score_history.py / archive_flag.py.
_TOOLS_ROOT = Path(__file__).resolve().parent.parent
_BACKTEST_DIR = _TOOLS_ROOT / "backtest-ready"
if str(_BACKTEST_DIR) not in sys.path:
    sys.path.insert(0, str(_BACKTEST_DIR))

from schemas import FlagEvent  # noqa: E402  (after sys.path bootstrap)

with contextlib.suppress(Exception):
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

from pydantic import ValidationError  # noqa: E402


def _fail(msg: str) -> int:
    print(f"❌ validate-flag-events: {msg}", file=sys.stderr)
    return 1


def _warn(msg: str) -> None:
    print(f"⚠️  validate-flag-events: {msg}", file=sys.stderr)


def _check_pairing(events: list[dict]) -> None:
    """Rebuild FLAG-State from the event sequence; WARN on dangling resolutions.

    A resolution without a preceding open trigger for the same flag_id is a
    sanity hint only (kein EXIT 1) — see module docstring.
    """
    open_keys: set[str] = set()
    for rec in events:
        flag_id = rec.get("flag_id", "")
        event_typ = rec.get("event_typ")
        if event_typ == "trigger":
            open_keys.add(flag_id)
        elif event_typ == "resolution":
            if flag_id not in open_keys:
                _warn(
                    f"resolution for flag_id '{flag_id}' has no preceding open "
                    f"trigger in this file (Cross-File-State? — sanity hint, "
                    f"non-blocking)"
                )
            else:
                open_keys.discard(flag_id)


def validate_file(path: Path) -> int:
    raw = path.read_bytes()
    if b"\r\n" in raw:
        return _fail(f"CRLF in JSONL '{path}' — LF-only required (Spec §4.1/§4.2)")

    events: list[dict] = []
    for lineno, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            return _fail(f"{path}:{lineno} JSON parse error: {e}")
        try:
            FlagEvent.model_validate(rec)
        except ValidationError as e:
            return _fail(f"{path}:{lineno} FlagEvent schema violation: {e}")
        events.append(rec)

    _check_pairing(events)  # WARN-only, never blocks
    return 0


def main(argv: list[str] | None = None) -> int:
    paths = list(sys.argv[1:]) if argv is None else argv
    for p in paths:
        path = Path(p)
        if not path.is_file():
            continue
        rc = validate_file(path)
        if rc != 0:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
