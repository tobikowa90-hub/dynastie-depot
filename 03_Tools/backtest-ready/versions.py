"""Dynasty-Depot: DEFCON version constants. Single source of truth.

Referenced by schemas.py (_check_forward_version), provenance_gate.py
(check_provenance #6), SKILL.md text.
Bei Migration v3.7 -> v3.8: nur DEFCON_ACTIVE_VERSION hier anpassen.
"""
from typing import Final

DEFCON_ACTIVE_VERSION: Final[str] = "v3.7"

__all__ = ["DEFCON_ACTIVE_VERSION"]
