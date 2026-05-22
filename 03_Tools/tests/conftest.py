"""Shared pytest configuration for 03_Tools tests.

Adds 03_Tools to sys.path so test modules can import sibling source files directly
(e.g. `import finnhub_client`, `import _atomic_io`).

Also provides a session-scoped autouse patch that prevents finnhub_client from
reading the real .env.finnhub file during unit tests. Tests that need a key should
supply one via monkeypatch.setenv("FINNHUB_API_KEY", ...).
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Ensure 03_Tools is importable when pytest is invoked from any directory.
_tools_dir = Path(__file__).resolve().parents[1]
if str(_tools_dir) not in sys.path:
    sys.path.insert(0, str(_tools_dir))


@pytest.fixture(autouse=True)
def _block_finnhub_env_file(monkeypatch):
    """Prevent finnhub_client from silently reading .env.finnhub during unit tests.

    Tests that need a valid key must supply it explicitly via:
        monkeypatch.setenv("FINNHUB_API_KEY", "test-key")
    """
    # Patch Path.exists so the .env.finnhub lookup always returns False.
    # We target only the specific file name to avoid side-effects on other Path.exists calls.
    _real_exists = Path.exists

    def _patched_exists(self: Path) -> bool:
        if self.name == ".env.finnhub":
            return False
        return _real_exists(self)

    monkeypatch.setattr(Path, "exists", _patched_exists)
