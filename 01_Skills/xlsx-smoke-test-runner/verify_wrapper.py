"""verify_wrapper.py — Post-Write Re-Validation (SPEC §4.2).

Lädt 03_Tools/precommit/xlsx_smoke_test.py via importlib.util — Standard-Import
nicht möglich, weil:
  - `03_Tools/` startet mit Ziffer (kein Package-Name)
  - `03_Tools/precommit/` hat KEIN __init__.py (Glob 2026-05-25 verified)

Verträge:
  - read-only auf das xlsx; Hook delegiert openpyxl.load_workbook
  - Caller-friendly: rc-Fail → VerifyResult(ok=False), NIE Exception
  - fail-loud nur bei IO-Problem (FileNotFoundError)
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

_GATE_RE = re.compile(r"\(Punkt\s+([A-G])(?:\s*,\s*minimal)?\)")
_PROFIL_RE = re.compile(r"profil=([A-Za-z_]+)")


def _load_hook_module() -> ModuleType:
    """Lädt 03_Tools/precommit/xlsx_smoke_test.py via importlib.util.

    verified via: Glob `03_Tools/**/__init__.py` 2026-05-25 = precommit/ leer.
    """
    hook_path = (
        Path(__file__).resolve().parents[2] / "03_Tools" / "precommit" / "xlsx_smoke_test.py"
    )
    if not hook_path.is_file():
        raise FileNotFoundError(f"Hook-Modul nicht gefunden: {hook_path}")
    spec = importlib.util.spec_from_file_location("xlsx_smoke_test_hook", hook_path)
    if spec is None or spec.loader is None:
        raise FileNotFoundError(f"Hook-Modul nicht ladbar: {hook_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["xlsx_smoke_test_hook"] = module
    spec.loader.exec_module(module)
    return module


@dataclass(frozen=True)
class VerifyResult:
    """Ergebnis-Container für post-Write-Verifikation (SPEC §4.2)."""

    ok: bool
    profile: str
    failed_gate: str | None
    detail: str


def _resolve_profile(mod: ModuleType, path: Path) -> str:
    resolved = mod._resolve_profil(path)
    return resolved[0] if resolved is not None else "UNKNOWN"


def _parse_gate(detail: str) -> str | None:
    m = _GATE_RE.search(detail)
    return m.group(1) if m else None


def _parse_profile_from_detail(detail: str) -> str | None:
    m = _PROFIL_RE.search(detail)
    return m.group(1) if m else None


def verify_after_write(path: Path, *, run_g: bool = True) -> VerifyResult:
    """Run Hook-Validation nach openpyxl-Save.

    `run_g`: v0.1 no-op; Hook entscheidet §G-Lauf intern via Profil (Sat-only).
    Reserved für v0.2-Skip-Flag.

    Wirft FileNotFoundError nur bei fehlender Datei (fail-loud).
    Hook-Fail liefert VerifyResult(ok=False, ...) — keine Exception.
    """
    p = Path(path)
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(f"verify_after_write: {p} nicht vorhanden")

    mod = _load_hook_module()
    stderr_capture = io.StringIO()
    stdout_capture = io.StringIO()
    try:
        with contextlib.redirect_stderr(stderr_capture), contextlib.redirect_stdout(stdout_capture):
            rc = mod.validate_file(p)
    except FileNotFoundError, PermissionError:
        raise  # fail-loud (SPEC §4.2)
    except Exception as e:  # noqa: BLE001 — caller-friendly per SPEC §4.2 + Codex-R3 MED-1
        return VerifyResult(
            ok=False,
            profile=_resolve_profile(mod, p),
            failed_gate="UNKNOWN",
            detail=f"hook crashed: {type(e).__name__}: {e}",
        )
    detail = stderr_capture.getvalue().strip()

    if rc == 0:
        return VerifyResult(
            ok=True,
            profile=_resolve_profile(mod, p),
            failed_gate=None,
            detail="",
        )

    profile = _parse_profile_from_detail(detail) or _resolve_profile(mod, p)
    return VerifyResult(
        ok=False,
        profile=profile,
        failed_gate=_parse_gate(detail) or "UNKNOWN",
        detail=detail,
    )


def verify_batch(paths: list[Path], *, run_g: bool = True) -> list[VerifyResult]:
    """Sequenzieller Batch-Verify; ALLE Pfade laufen auch bei Fail (kein early-exit)."""
    return [verify_after_write(Path(p), run_g=run_g) for p in paths]


__all__ = [
    "VerifyResult",
    "_load_hook_module",
    "verify_after_write",
    "verify_batch",
]
