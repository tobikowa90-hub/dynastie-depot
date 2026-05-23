"""CP18 HIGH-2 + HIGH-3 regression — §18-result parser must require
BOTH rc==0 AND status=='PASS'. Either branch alone was a false-PASS bug."""

import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_DIR / "scripts"))

from core_slim_refactor import _evaluate_p18_result  # noqa: E402


def test_rc0_status_pass_passes():
    passed, reason = _evaluate_p18_result(0, '{"status": "PASS"}')
    assert passed is True, reason


def test_rc0_status_fail_blocks_high2():
    """HIGH-2: rc==0 with status=FAIL must NOT pass the gate.
    Previously: JSON was only checked inside `if rc != 0`, so any rc==0
    response was accepted regardless of status."""
    passed, reason = _evaluate_p18_result(0, '{"status": "FAIL"}')
    assert passed is False
    assert "status=FAIL" in reason


def test_rc_nonzero_status_pass_blocks_high3():
    """HIGH-3: rc!=0 with status=PASS must NOT pass the gate.
    Previously: inner check was `if status != PASS` → status==PASS
    short-circuited the fail branch even though rc indicated failure."""
    passed, reason = _evaluate_p18_result(1, '{"status": "PASS"}')
    assert passed is False
    assert "rc=1" in reason


def test_rc_nonzero_status_fail_blocks():
    passed, _reason = _evaluate_p18_result(2, '{"status": "FAIL"}')
    assert passed is False


def test_empty_stdout_blocks():
    passed, reason = _evaluate_p18_result(0, "")
    assert passed is False
    assert "status=None" in reason


def test_invalid_json_blocks():
    passed, reason = _evaluate_p18_result(0, "not json at all")
    assert passed is False
    assert "json-parse-error" in reason


def test_missing_status_field_blocks():
    passed, reason = _evaluate_p18_result(0, '{"version": "0.1.0"}')
    assert passed is False
    assert "status=None" in reason
