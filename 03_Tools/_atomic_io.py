"""Atomic JSONL append — tear-safe single-writer, stdlib-pure (no portalocker dep).

Pattern: read existing content → write to tempfile in same dir → fsync(tmpf) →
os.replace → POSIX-guarded fsync(dir_fd). Crash before replace leaves original
target intact AND tempfile visible for recovery inspection.

**Scope (Plan-v1.2 Spec-v1.1 §3 M5 honest re-scope):**
- Tear-safe for single-writer (Crash-mid-Write rollback-safe; Target stays
  Old-Content-or-New-Content, never partial)
- Atomic-replace-visibility: nach `os.replace`, nachfolgende Reader sehen
  Old-Content oder New-Content, nie partial
- Post-crash-durability-after-rename: POSIX-guarded Directory-fsync syncs den
  Rename-Dir-Entry durabel; Windows: no-op (MoveFileEx-Semantik implizit)
- Pre-replace-Failures (z.B. fsync OSError vor `os.replace`): Tempfile BLEIBT
  liegen für Tear-Recovery-Inspection — NICHT `os.unlink`'d. Target unverändert.

**NICHT abgedeckt (Tier-B Future):** Multi-Writer-Konkurrenz (read-rewrite-replace
race window zwischen Read und Replace → last-writer-wins). Locking via portalocker
deferred per Spec §8 Open Question 2.

**Performance-Hinweis:** O(N) pro Append durch full-rewrite. Bei großen JSONL-Files
(>10k Lines) Append-mit-O_APPEND statt rewrite ist folge-Optimierung — separate Task.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

from pydantic import BaseModel


def _fsync_dir_posix(parent: Path) -> None:
    """POSIX-only: fsync the parent directory to durably commit rename-entry.

    No-op on Windows (`os.open(dir, O_RDONLY)` is not portable, and rename
    durability is handled by MoveFileEx-Semantik in `os.replace`).
    """
    if os.name != "posix":
        return
    dir_fd = os.open(str(parent), os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)


def atomic_jsonl_append(path: Path, record: BaseModel) -> None:
    """Append a single JSONL line tear-safely (single-writer-scope).

    Reads existing file (if any), appends new line, writes complete content
    to a same-dir tempfile, fsyncs tempfile, atomically replaces target,
    fsyncs parent directory (POSIX only) for post-rename durability.

    Crash-Semantik (Spec-v1.1 §3 M5):
    - Vor `os.replace`: Tempfile bleibt liegen (Recovery-Inspection), Target unchanged
    - Nach `os.replace`: Target hat neuen Content; dir-fsync syncs Rename-Eintrag durabel

    Args:
        path: Target JSONL file (parents created if missing).
        record: Pydantic model with .model_dump_json() method. Pydantic v2
            model_dump_json() defaults: UTF-8 native, no ASCII-escape — preserves
            Umlaute/non-ASCII without `ensure_ascii=False` flag.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    line = record.model_dump_json() + "\n"

    # Read existing content (empty if file doesn't exist).
    # try/except is robust to deletion-between-stat-and-read in case the
    # single-writer scope is ever relaxed.
    try:
        existing = path.read_bytes()
    except FileNotFoundError:
        existing = b""

    # Write to tempfile in same dir for atomic replace on same-volume
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    # NOTE: Pre-replace-Failures (fsync OSError, write OSError) propagieren bewusst;
    # Tempfile bleibt liegen — Spec-v1.1 §3 M5 "Tempfile bleibt für Recovery".
    # KEIN try/except mit os.unlink — das würde die Spec-Semantik verletzen.
    with os.fdopen(fd, "wb") as tmpf:
        tmpf.write(existing)
        tmpf.write(line.encode("utf-8"))
        tmpf.flush()
        os.fsync(tmpf.fileno())
    Path(tmp_name).replace(path)
    _fsync_dir_posix(path.parent)
