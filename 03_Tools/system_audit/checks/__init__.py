"""Check registry. Each check exports `run(repo_root, context) -> CheckResult`.

Populated incrementally as checks are implemented. Orchestrator imports CORE/
OPTIONAL dicts and dispatches them.

Konvention (Klasse f, Validator-Catch-Lücken — Spec 2026-05-11-codebase-defect-patterns):
  Check-Functions MÜSSEN immer `CheckResult` zurückgeben (auch im Failure-Pfad).
  Silent `return None` ist verboten — stattdessen
  `CheckResult(status="WARN" oder "FAIL", failures=[FailureDetail(...)])`.
  Validatoren emit FailureDetail, never KeyError-escape.
"""
from __future__ import annotations

CORE: dict[str, str] = {
    "jsonl_schema": "system_audit.checks.jsonl_schema:run",
    "store_freshness": "system_audit.checks.store_freshness:run",
    "markdown_header": "system_audit.checks.markdown_header:run",
    "cross_source": "system_audit.checks.cross_source:run",
    "existence": "system_audit.checks.existence:run",
    "skill_version": "system_audit.checks.skill_version:run",
    "pipeline_ssot": "system_audit.checks.pipeline_ssot:run",
    "log_lag": "system_audit.checks.log_lag:run",
    "score_event_parity": "system_audit.checks.score_event_parity:run",
    "skill_frontmatter": "system_audit.checks.skill_frontmatter:run",
    "header_freshness": "system_audit.checks.header_freshness:run",
    "governance_parity": "system_audit.checks.governance_parity:run",
    "cross_source_reverse": "system_audit.checks.cross_source_reverse:run",
    "pointer_completeness": "system_audit.checks.pointer_completeness:run",
    "sum_consistency": "system_audit.checks.sum_consistency:run",
}      # name → "system_audit.checks.<module>:run"  (15 core checks)
OPTIONAL: dict[str, str] = {
    "vault_backlinks": "system_audit.checks.vault_backlinks:run",
    "status_matrix": "system_audit.checks.status_matrix:run",
}  # same shape, activated via --full / --vault
