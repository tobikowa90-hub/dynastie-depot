"""Edge-case tests for ``_forward_verify_helpers.check_freshness``.

PIPELINE #22 (2026-05-09): the production helper now uses
``git status --porcelain=v1 -z`` (NUL-separator) instead of text-mode porcelain,
so paths with spaces, Umlauts, embedded newlines, or rename/copy status no
longer break basename matching.

These tests are unit-level: they monkey-patch ``subprocess.run`` inside the
helper module so a synthetic ``stdout`` byte-stream stands in for actual git
output. That isolates the parser logic from filesystem peculiarities (Windows
forbids ``\\n`` in filenames; NTFS Umlaut handling depends on git locale; etc.)
and keeps the test cross-platform.

Real-git integration is covered by Case 6 in
``01_Skills/backtest-ready-forward-verify/_smoke_test.py`` (unchanged).

Run::

    python 03_Tools/backtest-ready/_forward_verify_helpers_test.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

# sys.path: make _forward_verify_helpers importable when run from anywhere
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

import _forward_verify_helpers as helpers  # noqa: E402


# ---------------------------------------------------------------------------
# Helper: stub for subprocess.run that returns a fake CompletedProcess
# ---------------------------------------------------------------------------
class _FakeCompleted:
    """Minimal stand-in for subprocess.CompletedProcess (bytes mode)."""

    def __init__(self, stdout: bytes = b"", stderr: bytes = b"", returncode: int = 0):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


def _patch_run(stdout_bytes: bytes):
    """Return a context manager that patches ``helpers.subprocess.run``."""

    class _Ctx:
        def __enter__(self_inner):
            self_inner._orig = helpers.subprocess.run
            helpers.subprocess.run = lambda *a, **kw: _FakeCompleted(stdout=stdout_bytes)
            return self_inner

        def __exit__(self_inner, *exc):
            helpers.subprocess.run = self_inner._orig
            return False

    return _Ctx()


# A real (existing) directory so the helper's ``cwd=repo_root`` doesn't
# trip on FileNotFoundError before our stub takes over.  The stub bypasses
# the actual git call, so contents don't matter.
def _tmpdir_path() -> str:
    return tempfile.gettempdir()


# ---------------------------------------------------------------------------
# Case 9 — ASCII paths (baseline)
# ---------------------------------------------------------------------------
def case_9() -> None:
    """All 3 required files modified with ASCII paths → no missing."""
    stdout = b"M  00_Core/PORTFOLIO.md\x00M  00_Core/Faktortabelle.md\x00M  00_Core/log.md\x00"
    with _patch_run(stdout):
        result = helpers.check_freshness(repo_root=_tmpdir_path())
    assert result == [], f"expected [], got {result}"


# ---------------------------------------------------------------------------
# Case 10 — Path with spaces
# ---------------------------------------------------------------------------
def case_10() -> None:
    """Path with spaces (``07_Obsidian Vault/...``) — -z mode preserves
    them literally; legacy text-mode would have wrapped in double-quotes."""
    stdout = b"M  07_Obsidian Vault/work area/log.md\x00M  00_Core/PORTFOLIO.md\x00"
    with _patch_run(stdout):
        result = helpers.check_freshness(repo_root=_tmpdir_path())
    # log.md and PORTFOLIO.md detected; Faktortabelle.md still missing
    assert result == ["Faktortabelle.md"], f"expected ['Faktortabelle.md'], got {result}"


# ---------------------------------------------------------------------------
# Case 11 — Path with Umlauts (raw UTF-8 bytes, no quote-escape under -z)
# ---------------------------------------------------------------------------
def case_11() -> None:
    """Umlaut in directory component — raw UTF-8 bytes survive round-trip.
    ``\\xc3\\xa4`` = ä, ``\\xc3\\xb6`` = ö, ``\\xc3\\xbc`` = ü.
    Legacy text-mode would have emitted ``"00_K\\303\\266re/log.md"`` and
    the helper would have stripped only outer quotes, leaving octal
    escapes in the basename — that's the bug this case guards against."""
    stdout = (
        # 00_Köre/log.md      → "K" + 0xC3 0xB6 + "re/log.md"
        b"M  00_K\xc3\xb6re/log.md\x00"
        # 00_Über/Faktortabelle.md
        b"M  00_\xc3\x9cber/Faktortabelle.md\x00"
        # 00_Übung/PORTFOLIO.md
        b"M  00_\xc3\x9cbung/PORTFOLIO.md\x00"
    )
    with _patch_run(stdout):
        result = helpers.check_freshness(repo_root=_tmpdir_path())
    assert result == [], f"expected [], got {result}"


# ---------------------------------------------------------------------------
# Case 12 — Rename status R (two paths separated by NUL)
# ---------------------------------------------------------------------------
def case_12() -> None:
    """``R<sp>path1<NUL>path2<NUL>``: the consumer must skip *both* path
    fields (advance 2 entries) and add basenames for *both*. Otherwise the
    second NUL-token would be parsed as a malformed entry header.

    The basename of the renamed PORTFOLIO.md is captured regardless of
    git's path order (TO-FROM in -z mode), because we add both."""
    stdout = (
        # Rename: 00_Core/PORTFOLIO.md ↔ 00_Core/PORTFOLIO_OLD.md
        b"R  00_Core/PORTFOLIO.md\x00"
        b"00_Core/PORTFOLIO_OLD.md\x00"
        # Plain modify of Faktortabelle.md and log.md
        b"M  00_Core/Faktortabelle.md\x00"
        b"M  00_Core/log.md\x00"
    )
    with _patch_run(stdout):
        result = helpers.check_freshness(repo_root=_tmpdir_path())
    assert result == [], f"expected [], got {result}"

    # Sub-case: Copy status C — same two-path layout
    stdout_c = (
        b"C  00_Core/PORTFOLIO.md\x00"
        b"00_Core/PORTFOLIO_TEMPLATE.md\x00"
        b"M  00_Core/Faktortabelle.md\x00"
        b"M  00_Core/log.md\x00"
    )
    with _patch_run(stdout_c):
        result_c = helpers.check_freshness(repo_root=_tmpdir_path())
    assert result_c == [], f"expected [] for copy status, got {result_c}"

    # Sub-case: only the rename — Faktortabelle and log still missing.
    # Confirms the second NUL-token is consumed as path-2, NOT as a new
    # entry (which would crash on len < 4 or pollute basenames).
    stdout_only_rename = b"R  00_Core/PORTFOLIO.md\x0000_Core/PORTFOLIO_OLD.md\x00"
    with _patch_run(stdout_only_rename):
        result_only = helpers.check_freshness(repo_root=_tmpdir_path())
    assert sorted(result_only) == sorted(["Faktortabelle.md", "log.md"]), (
        f"expected ['Faktortabelle.md','log.md'], got {result_only}"
    )

    # Sub-case: R/C in Y column (worktree status), X=M.  Codex-Single-Pass
    # 2026-05-09 minor-coverage-gap: only the X column had been exercised.
    # The OR-branch ``xy[1:2] in (b"R", b"C")`` must equally consume two
    # NUL-tokens.  ``MR`` = modified in index + rename pending in worktree.
    stdout_y_rename = (
        b"MR 00_Core/PORTFOLIO.md\x00"
        b"00_Core/PORTFOLIO_NEW.md\x00"
        b"M  00_Core/Faktortabelle.md\x00"
        b"M  00_Core/log.md\x00"
    )
    with _patch_run(stdout_y_rename):
        result_y = helpers.check_freshness(repo_root=_tmpdir_path())
    assert result_y == [], f"expected [] for Y-column rename, got {result_y}"


# ---------------------------------------------------------------------------
# Case 13 — Newline embedded in path
# ---------------------------------------------------------------------------
def case_13() -> None:
    """Newline-in-path: under -z, a literal ``\\n`` byte is part of the
    path. Text-mode ``splitlines()`` would have shattered such an entry
    into two malformed pieces; -z keeps it intact and the parser uses
    the NUL boundary instead.

    We use a newline in a *directory* component so basename matching
    against REQUIRED_TOUCH_FILES still succeeds. Cross-platform safe
    (synthetic bytes — no real file with newline-in-name needed)."""
    stdout = (
        # weird\nfolder/log.md  (newline byte mid-path)
        b"M  weird\nfolder/log.md\x00M  00_Core/PORTFOLIO.md\x00M  00_Core/Faktortabelle.md\x00"
    )
    with _patch_run(stdout):
        result = helpers.check_freshness(repo_root=_tmpdir_path())
    assert result == [], f"expected [], got {result}"

    # Sub-case: newline-in-basename — basename keeps newline literally,
    # no match against REQUIRED_TOUCH_FILES → all 3 missing.
    stdout_nl_basename = b"M  00_Core/foo\nbar.md\x00"
    with _patch_run(stdout_nl_basename):
        result_nb = helpers.check_freshness(repo_root=_tmpdir_path())
    assert sorted(result_nb) == sorted(["PORTFOLIO.md", "Faktortabelle.md", "log.md"]), (
        f"expected all 3 missing, got {result_nb}"
    )


# ---------------------------------------------------------------------------
# Case 14 — Sentinel: error-handling preserved (returncode != 0)
# ---------------------------------------------------------------------------
def case_14() -> None:
    """Refactor must keep the returncode-check semantics. Stub a non-zero
    exit and a stderr payload (bytes) — helper raises RuntimeError that
    decodes the bytes for the message."""

    class _FakeFailed(_FakeCompleted):
        pass

    orig = helpers.subprocess.run
    helpers.subprocess.run = lambda *a, **kw: _FakeFailed(
        stdout=b"", stderr=b"fatal: not a git repository", returncode=128
    )
    try:
        try:
            helpers.check_freshness(repo_root=_tmpdir_path())
        except RuntimeError as exc:
            msg = str(exc)
            assert "returncode=128" in msg, f"missing returncode in msg: {msg!r}"
            assert "not a git repository" in msg, f"stderr-bytes not decoded into message: {msg!r}"
            return
        raise AssertionError("expected RuntimeError on returncode != 0")
    finally:
        helpers.subprocess.run = orig


# ---------------------------------------------------------------------------
# Harness
# ---------------------------------------------------------------------------
CASES = [
    (9, "ASCII paths (baseline)", case_9),
    (10, "Path with spaces", case_10),
    (11, "Path with Umlauts (UTF-8 bytes)", case_11),
    (12, "Rename/Copy status R/C (two-path entries)", case_12),
    (13, "Newline embedded in path", case_13),
    (14, "Returncode error-handling preserved", case_14),
]


def run_all() -> None:
    passed = 0
    failed = 0
    for n, label, fn in CASES:
        try:
            fn()
            print(f"[{n}/{len(CASES) + 8}] PASS: {label}")
            passed += 1
        except Exception as exc:
            print(f"[{n}/{len(CASES) + 8}] FAIL: {label} — {type(exc).__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print(f"OK all {passed}/{len(CASES)} edge cases passed (PIPELINE #22)")
    else:
        print(f"FAIL {failed} case(s) failed, {passed}/{len(CASES)} passed")
        sys.exit(1)


if __name__ == "__main__":
    run_all()
