"""validate-score-history pre-commit-Hook (Spec §3.2).

Validiert staged `score_history.jsonl` gegen das kanonische `ScoreRecord`-Schema
(`03_Tools/backtest-ready/schemas.py` — kein Schema-Doppel-SSoT) plus:
  - Byte-Level-CRLF-Reject VOR Text-Parse (Memory feedback_windows_python_crlf_text_mode)
  - Append-only-Guard via `git diff --cached` Hunk-Parser (Codex-F5):
    Legit-Append := AUSSCHLIESSLICH '+'-Zeilen, KEINE '-'-Zeile, alle '+'-Hunks
    am File-Ende. Deletion / In-Place-Edit / Mid-File-Insert = fail-close.

EOL-Artefakt-Konfusion ist ausgeschlossen: CRLF-Normalisierung ist einmaliger
Vorab-Commit (§4.1) + `.gitattributes` erzwingt LF → im Steady-State kein
EOL-only-'-'/'+'-Paar; kanonische Writer (`backtest-ready-forward-verify`,
`_atomic_io`) schreiben mit trailing-LF.

Aufruf: pre-commit übergibt die staged Pfade als argv (`language: system`).
Fail-close: EXIT 1 beim ersten Fehler, Grund auf stderr.
"""

from __future__ import annotations

import contextlib
import json
import re
import subprocess
import sys
from pathlib import Path

# schemas.py-Bootstrap analog archive_flag.py: 03_Tools/backtest-ready/ in den
# sys.path, damit `from schemas import ScoreRecord` den kanonischen SSoT trifft.
_TOOLS_ROOT = Path(__file__).resolve().parent.parent
_BACKTEST_DIR = _TOOLS_ROOT / "backtest-ready"
if str(_BACKTEST_DIR) not in sys.path:
    sys.path.insert(0, str(_BACKTEST_DIR))

from schemas import ScoreRecord  # noqa: E402  (after sys.path bootstrap)

with contextlib.suppress(Exception):
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

from pydantic import ValidationError  # noqa: E402

_HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def _fail(msg: str) -> int:
    print(f"❌ validate-score-history: {msg}", file=sys.stderr)
    return 1


def _git_head_line_count(path: Path) -> int | None:
    """Line count of the HEAD version of `path`, or None if not tracked yet."""
    rel = path.resolve().relative_to(_TOOLS_ROOT.parent)
    proc = subprocess.run(
        ["git", "show", f"HEAD:{rel.as_posix()}"],
        capture_output=True,
        check=False,
        cwd=_TOOLS_ROOT.parent,
    )
    if proc.returncode != 0:
        return None  # new file — whole content is a legit initial addition
    # Trailing-newline-robust (Codex-L1): eine N-Zeilen-Datei OHNE finales \n
    # hat nur N-1 \n. Kanonische Writer (_atomic_io) schreiben mit trailing-LF,
    # aber der Append-only-Guard ist der Kern-Schutz → defensiv exakt zählen.
    stdout = proc.stdout
    if not stdout:
        return 0
    return stdout.count(b"\n") + (0 if stdout.endswith(b"\n") else 1)


def _staged_diff(path: Path) -> str:
    rel = path.resolve().relative_to(_TOOLS_ROOT.parent)
    proc = subprocess.run(
        ["git", "diff", "--cached", "--unified=0", "--no-color", "--", rel.as_posix()],
        capture_output=True,
        check=False,
        cwd=_TOOLS_ROOT.parent,
        text=True,
    )
    return proc.stdout


def check_append_only(path: Path) -> str | None:
    """Return an error string if the staged diff is not a pure EOF-append."""
    diff = _staged_diff(path)
    if not diff.strip():
        return None  # nothing staged for this file / identical content
    head_total = _git_head_line_count(path)
    if head_total is None:
        return None  # newly tracked file — initial add is legit

    for line in diff.splitlines():
        if line.startswith(("---", "+++")):
            continue
        if line.startswith("\\"):
            continue  # "\ No newline at end of file" — kein Inhalt-Δ (Codex-L1)
        if line.startswith("-"):
            return (
                "score_history.jsonl is append-only — Deletion/In-Place-Edit "
                f"detected ({line[:80]!r})"
            )
        m = _HUNK_RE.match(line)
        if not m:
            continue
        old_start = int(m.group(1))
        old_count = int(m.group(2) or "1")
        new_start = int(m.group(3))
        # Codex-F5-Vertrag wörtlich: reiner EOF-Append-Hunk unter --unified=0
        # ist `@@ -<head_total>,0 +<head_total+1>,M @@` — old_count==0,
        # old_start==head_total, new_start==head_total+1. Jede Abweichung
        # (Replacement / Mid-File-Insert / Position-Anomalie) = fail-close.
        if old_count != 0 or old_start < head_total or new_start != head_total + 1:
            return (
                "score_history.jsonl is append-only — Non-EOF-append detected "
                f"(hunk {line.strip()!r}; HEAD has {head_total} lines)"
            )
    return None


def validate_file(path: Path) -> int:
    raw = path.read_bytes()
    if b"\r\n" in raw:
        return _fail(f"CRLF in JSONL '{path}' — LF-only required (Spec §4.1/§4.2)")

    for lineno, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            return _fail(f"{path}:{lineno} JSON parse error: {e}")
        try:
            ScoreRecord.model_validate(rec)
        except ValidationError as e:
            return _fail(f"{path}:{lineno} ScoreRecord schema violation: {e}")

    append_err = check_append_only(path)
    if append_err is not None:
        return _fail(append_err)
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
