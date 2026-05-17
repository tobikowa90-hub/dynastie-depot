"""Smoke-Harness für die pre-commit-Validatoren (Spec §5 Akzeptanz #2).

Generiert die Fixtures und prüft je Validator: valide-Fixture → rc 0,
invalide-Fixture → rc 1. Der git-abhängige Append-only-Guard von
validate_score_history wird hier NICHT getriggert (Fixtures sind ungestaged →
`git diff --cached` leer → check_append_only returnt None); dieser Pfad wird
beim echten `pre-commit run --all-files` (Akzeptanz #1) + Codex-Review (Spec §6)
abgedeckt. Hier verifiziert: Schema- + CRLF- + xlsx-Pfade.

Lauf: `python 03_Tools/precommit/_smoke_test.py`
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FIX = _HERE / "_fixtures"
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_FIX))

import _generate_fixtures
import crlf_guard
import validate_flag_events
import validate_score_history
import xlsx_smoke_test


def _expect(label: str, got: int, want: int) -> None:
    status = "OK" if got == want else "FAIL"
    print(f"  [{status}] {label}: rc={got} (expected {want})")
    if got != want:
        raise AssertionError(f"{label}: expected rc={want}, got {got}")


def main() -> int:
    print("generating fixtures…")
    _generate_fixtures.main()

    print("crlf-guard:")
    _expect("lf_clean", crlf_guard.main([str(_FIX / "crlf_lf_clean.input")]), 0)
    _expect(
        "crlf_contaminated",
        crlf_guard.main([str(_FIX / "crlf_carriage_return_contaminated.input")]),
        1,
    )

    print("validate-score-history:")
    _expect(
        "valid_append",
        validate_score_history.main([str(_FIX / "score_history_valid_append.input")]),
        0,
    )
    _expect(
        "schema_violation",
        validate_score_history.main([str(_FIX / "score_history_schema_violation.input")]),
        1,
    )

    print("validate-flag-events:")
    _expect(
        "valid",
        validate_flag_events.main([str(_FIX / "flag_events_valid.input")]),
        0,
    )
    _expect(
        "schema_violation",
        validate_flag_events.main([str(_FIX / "flag_events_schema_violation.input")]),
        1,
    )

    print("xlsx-smoke-test:")
    _expect(
        "clean",
        xlsx_smoke_test.main([str(_FIX / "Watchlist_Ersatzbank_Monitor_fixture_clean.xlsx")]),
        0,
    )
    _expect(
        "empty_a1",
        xlsx_smoke_test.main([str(_FIX / "Watchlist_Ersatzbank_Monitor_fixture_empty_a1.xlsx")]),
        1,
    )

    print("✅ all pre-commit validator smoke tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
