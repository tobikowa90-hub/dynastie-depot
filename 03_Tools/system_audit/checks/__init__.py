"""Check registry. Each check exports `run(repo_root, context) -> CheckResult`.

Populated incrementally as checks are implemented. Orchestrator imports CORE/
OPTIONAL dicts and dispatches them.
"""
from __future__ import annotations

CORE: dict[str, str] = {
    "jsonl_schema": "system_audit.checks.jsonl_schema:run",
    "store_freshness": "system_audit.checks.store_freshness:run",
    "markdown_header": "system_audit.checks.markdown_header:run",
    "cross_source": "system_audit.checks.cross_source:run",
}      # name → "system_audit.checks.<module>:run"
OPTIONAL: dict[str, str] = {}  # same shape, activated via --full / --vault
