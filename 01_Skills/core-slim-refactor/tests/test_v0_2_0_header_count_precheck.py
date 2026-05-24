"""v0.2.0 P2a Drift-Pre-Check -- Spec SS3.2, AC2/AC2b/AC2c.

EXIT_DRIFT_DETECTED = 12 (Code 11 belegt durch v0.1.1 EXIT_ANCHOR_NOT_FOUND).
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "core_slim_refactor.py"
sys.path.insert(0, str(ROOT / "tests"))
from _helpers import make_minimal_valid_cfg_yaml  # noqa: E402  Disziplin-Regel #4


def _make_target(tmp_path: Path, n_entries: int) -> Path:
    md = "# Log\n\n"
    for i in range(n_entries):
        md += f"## 2026-05-{(i % 28) + 1:02d}\nEntry {i}\n\n"
    p = tmp_path / "target.md"
    p.write_text(md, encoding="utf-8", newline="\n")
    return p


def _make_cfg(tmp_path: Path, target: Path, min_n: int, max_n: int, on_drift: str) -> Path:
    return make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=target,
        archive_path=tmp_path / "archive.md",
        schema_version=2,
        cut_before="2026-05-15",
        expected_entry_count={"min": min_n, "max": max_n, "on_drift": on_drift},
    )


def _run(cfg: Path, *extra_args: str) -> subprocess.CompletedProcess:
    # Positional 'config' arg (NOT --config) per real argparse in core_slim_refactor.py:555
    env = dict(os.environ)
    env["CORE_SLIM_REFACTOR_SKIP_GATE"] = "1"
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(cfg), "--dry-run", *extra_args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        check=False,
    )


def test_drift_fail_close_exits_12_with_structured_code(tmp_path):
    """AC2: drift + on_drift=fail_close -> Exit 12 + DRIFT_COUNT_OUT_OF_RANGE in stderr.

    n_entries=20 -> classify_date_cut produces 21 rows (14 archive + 7 keep incl. preamble).
    Range [100,130] guarantees drift. Structured-code must report actual count.
    """
    target = _make_target(tmp_path, n_entries=20)
    cfg = _make_cfg(tmp_path, target, min_n=100, max_n=130, on_drift="fail_close")
    res = _run(cfg)
    assert res.returncode == 12, f"stdout={res.stdout!r} stderr={res.stderr!r}"
    assert "DRIFT_COUNT_OUT_OF_RANGE" in res.stderr
    assert "classified=21" in res.stderr
    assert "range=[100,130]" in res.stderr


def test_drift_warn_continue_proceeds_exit_0(tmp_path):
    """AC2b: drift + on_drift=warn_continue -> Exit 0 + DRIFT_COUNT_OUT_OF_RANGE in stderr."""
    target = _make_target(tmp_path, n_entries=20)
    cfg = _make_cfg(tmp_path, target, min_n=100, max_n=130, on_drift="warn_continue")
    res = _run(cfg)
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    assert "DRIFT_COUNT_OUT_OF_RANGE" in res.stderr


def test_no_drift_when_in_range(tmp_path):
    """AC2c: count im Range -> Exit 0, kein DRIFT_COUNT_OUT_OF_RANGE."""
    target = _make_target(tmp_path, n_entries=20)
    cfg = _make_cfg(tmp_path, target, min_n=10, max_n=30, on_drift="fail_close")
    res = _run(cfg)
    assert res.returncode == 0, f"stderr={res.stderr!r}"
    assert "DRIFT_COUNT_OUT_OF_RANGE" not in res.stderr


def test_no_expected_count_skips_p2a(tmp_path):
    """Wenn expected_entry_count fehlt -> P2a wird nicht ausgefuehrt, kein Drift-Check."""
    target = _make_target(tmp_path, n_entries=20)
    # v0.1.x-shaped config: sv=1, kein expected_entry_count (Helper-Default)
    cfg = make_minimal_valid_cfg_yaml(
        tmp_path,
        target_path=target,
        archive_path=tmp_path / "archive.md",
        schema_version=1,
        cut_before="2026-05-15",
    )
    res = _run(cfg)
    assert res.returncode == 0
    assert "DRIFT_COUNT_OUT_OF_RANGE" not in res.stderr
