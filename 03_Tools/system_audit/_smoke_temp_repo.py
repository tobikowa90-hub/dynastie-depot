"""Spec §7.4: Run system_audit against a temp-copy of the real repo.

Verifies:
- Exit-Code ∈ {0, 1}
- STATE.md gets Last-Audit block written
- Timestamp within last 120 seconds
"""
from __future__ import annotations

import sys

# Python auto-inserts the script's directory (03_Tools/system_audit/) at
# sys.path[0] on launch.  That shadows the stdlib 'types' module with our
# package-local types.py, breaking the stdlib import chain before any user
# code runs.  Pop it when detected; the explicit sys.path.insert below
# re-adds 03_Tools so 'system_audit.types' still resolves as a qualified
# sub-module (no conflict with stdlib 'types').
# NOTE: resolve()-variant (Path(__file__).resolve().parent) was tested and
# breaks on Python 3.14.3 — 'from pathlib import Path' itself triggers
# functools → types → shadow before the pop runs.  Keeping endswith-guard.
if sys.path and sys.path[0].endswith("system_audit"):
    sys.path.pop(0)

# Windows console defaults to cp1252; captured subprocess stdout may contain
# emoji (e.g. status-section heading) that crashes on re-print.  Reconfigure
# our own stdout/stderr to utf-8 with replace fallback.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

import datetime
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td) / "repo"
        # Copy essentials (not .git, not __pycache__)
        shutil.copytree(
            REPO_ROOT, tdp,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", "node_modules", ".venv"),
        )
        # Init git so log_lag check has a commit
        subprocess.run(["git", "init", "-q"], cwd=tdp, check=True)
        subprocess.run(["git", "-c", "user.name=smoke", "-c", "user.email=s@s", "add", "."],
                       cwd=tdp, check=True, capture_output=True)
        subprocess.run(["git", "-c", "user.name=smoke", "-c", "user.email=s@s", "commit",
                        "-q", "-m", "smoke"], cwd=tdp, check=True, capture_output=True)

        rc = subprocess.run(
            [sys.executable, "03_Tools/system_audit.py", "--core"],
            cwd=tdp, capture_output=True, text=True, encoding="utf-8", timeout=60,
        )
        print(rc.stdout)
        if rc.stderr:
            print("--- stderr ---\n" + rc.stderr, file=sys.stderr)

        # Spec §7.4 primary intent: temp-copy write-path works. Current live
        # baseline may have known pre-existing FAILs (rc=1); rc=2 = Tool-Bug.
        # See Plan-Header-Notice "Task 15 Smoke Baseline Exit-Code Relaxation".
        assert rc.returncode in {0, 1}, (
            f"baseline smoke expected rc in {{0, 1}}, got rc={rc.returncode}. "
            f"Stdout:\n{rc.stdout}\nStderr:\n{rc.stderr}"
        )

        state_text = (tdp / "00_Core" / "STATE.md").read_text(encoding="utf-8")
        assert "<!-- system-audit:last-audit:start -->" in state_text, "marker missing"
        assert "<!-- system-audit:last-audit:end -->" in state_text, "end-marker missing"

        # Timestamp within 120s (relaxed for temp-repo overhead)
        m = re.search(r"Timestamp \(UTC\):\*\*\s*(\S+)", state_text)
        assert m, "timestamp not found in STATE.md"
        ts = datetime.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
        now = datetime.datetime.now(datetime.timezone.utc)
        delta = (now - ts).total_seconds()
        assert 0 <= delta < 120, f"timestamp not recent: {delta}s ago"
        print(f"[OK] smoke temp-repo passed; audit rc={rc.returncode}, timestamp {delta:.1f}s ago")
    return 0


def smoke_seeded_drift() -> int:
    """Seed a defcon-drift into score_history.jsonl, expect exit-code 1 + FAIL Check-1."""
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td) / "repo"
        shutil.copytree(REPO_ROOT, tdp, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        subprocess.run(["git", "init", "-q"], cwd=tdp, check=True)
        subprocess.run(["git", "-c","user.name=s","-c","user.email=s@s","add","."], cwd=tdp, check=True, capture_output=True)
        subprocess.run(["git", "-c","user.name=s","-c","user.email=s@s","commit","-q","-m","init"], cwd=tdp, check=True, capture_output=True)

        hist = tdp / "05_Archiv" / "score_history.jsonl"
        lines = hist.read_text(encoding="utf-8").splitlines()
        first = json.loads(lines[0])
        first["defcon_level"] = 1 if first["defcon_level"] != 1 else 4  # arbitrary mismatch
        lines[0] = json.dumps(first, ensure_ascii=False)
        hist.write_text("\n".join(lines) + "\n", encoding="utf-8")

        rc = subprocess.run(
            [sys.executable, "03_Tools/system_audit.py", "--core", "--json"],
            cwd=tdp, capture_output=True, text=True, encoding="utf-8", timeout=60,
        )
    assert rc.returncode == 1, f"expected rc=1, got {rc.returncode}, stderr={rc.stderr}"
    data = json.loads(rc.stdout)
    fail_names = [c["name"] for c in data["checks"] if c["status"] == "FAIL"]
    assert "jsonl_schema" in fail_names, f"expected jsonl_schema FAIL, got {fail_names}"
    print(f"[OK] seeded-drift smoke: jsonl_schema FAIL detected, rc=1")
    return 0


if __name__ == "__main__":
    main()
    smoke_seeded_drift()
