"""Check-13: Cross-Source-Reverse-Direction (Phase 2 Sweep-Driver F18).

Existing cross_source.py iterates config.satelliten → mirror (single direction).
This check goes the other way: walks Vault/PORTFOLIO for tickers and asserts
each ticker appears in at least one of config.{satelliten,watchlist,keine_zuteilung}.

Severity: WARN, nicht FAIL. Neue Recherche-Kandidaten ohne config-Eintrag
sind legitim (Recherche-Phase). FAIL nur wenn ticker in Vault als 'satellit'
getaggt ist aber config-satelliten ihn nicht hat (echte Drift).
"""
from __future__ import annotations

import re
import time
from pathlib import Path

import yaml

from system_audit.types import AuditContext, CheckResult, FailureDetail

VAULT_ENTITIES_REL = Path(
    "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten"
)
# Ticker-Extraktion ausschliesslich via Frontmatter — kein Filename-Stem-Fallback,
# weil Vault-Dateien mit Stems wie API/INDEX/NOTES (1-5 char ALL-UPPER) sonst
# als Ticker false-positive matchen wuerden (Codex-Review P2-08).
# Pattern erlaubt optionale "..." Quotes (YAML scalar) sowie Punkte/Bindestriche
# fuer dotted/dashed Tickers wie BRK.B, RDS.A, BF-B. Line-Anchor + Frontmatter-only
# bleibt unverletzt — kein body-text false-positive (P2-08 Schutz bewahrt).
TICKER_FRONTMATTER_RE = re.compile(
    r'^\s*ticker:\s*"?([A-Z][A-Z0-9.\-]{0,9})"?\s*$',
    re.MULTILINE,
)


def _config_ticker_sets(cfg_path: Path) -> tuple[set[str], set[str], set[str]]:
    """Return (satelliten, watchlist, keine_zuteilung) ticker sets.

    Raises yaml.YAMLError on parse failure so the caller can surface a
    single explicit FAIL instead of silently returning empty sets (which
    would degrade into a flood of orphan-ticker warnings — Codex-Phase-2-
    Final-Review Important #2 fix).
    """
    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8", errors="replace")) or {}

    def _extract(key: str) -> set[str]:
        out: set[str] = set()
        for entry in data.get(key, []) or []:
            if isinstance(entry, dict) and "ticker" in entry:
                out.add(str(entry["ticker"]).strip())
            elif isinstance(entry, str):
                out.add(entry.strip())
        return out

    return _extract("satelliten"), _extract("watchlist"), _extract("keine_zuteilung")


def _vault_ticker_locations(vault_dir: Path) -> dict[str, str]:
    """Map ticker → 'satelliten' | 'ersatzbank'.

    Ticker-Extraction REQUIRES `ticker:`-Frontmatter-Feld. Files ohne
    Frontmatter werden silent uebersprungen (Recherche-Notes, Concept-Files,
    Index-Pages). Per WIKI-SCHEMA.md sollen entity-Files das Frontmatter haben.
    """
    out: dict[str, str] = {}
    if not vault_dir.exists():
        return out
    for md in vault_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        m = TICKER_FRONTMATTER_RE.search(text)
        if not m:
            continue
        ticker = m.group(1)
        rel_parts = md.relative_to(vault_dir).parts
        location = "ersatzbank" if "ersatzbank" in rel_parts else "satelliten"
        out[ticker] = location
    return out


def run(repo_root: Path, context: AuditContext) -> CheckResult:
    start = time.monotonic()
    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    cfg_path = repo_root / "01_Skills" / "dynastie-depot" / "config.yaml"
    if not cfg_path.exists():
        return CheckResult(
            name="cross_source_reverse", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(cfg_path.relative_to(repo_root)) if cfg_path.is_relative_to(repo_root) else str(cfg_path),
                expected="config.yaml present",
                actual="missing",
                severity="warning",
                hint="dynastie-depot config-Pfad pruefen",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    try:
        sat_set, watch_set, kein_set = _config_ticker_sets(cfg_path)
    except yaml.YAMLError as e:
        # Single-shot FAIL: surface the parser error explicitly instead of
        # silently treating every Vault ticker as orphan (Codex Phase-2-
        # Final-Review Important #2). First line of YAMLError typically
        # carries the problem-mark; rest is multi-line context.
        first = str(e).splitlines()[0] if str(e) else type(e).__name__
        rel_loc = str(cfg_path.relative_to(repo_root)) if cfg_path.is_relative_to(repo_root) else str(cfg_path)
        return CheckResult(
            name="cross_source_reverse", status="FAIL",
            n_checked=1, n_passed=0,
            failures=[FailureDetail(
                location=rel_loc,
                expected="config.yaml parses as valid YAML",
                actual=f"YAMLError: {first}",
                severity="error",
                hint="config.yaml ist defekt — Vault-Parity-Check kann nicht laufen, "
                     "bis Datei valides YAML ist. Parser-Fehler oben + git diff pruefen",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )
    config_union = sat_set | watch_set | kein_set
    vault_tickers = _vault_ticker_locations(repo_root / VAULT_ENTITIES_REL)

    for ticker, location in sorted(vault_tickers.items()):
        n_checked += 1
        if ticker in config_union:
            # Tag-Konsistenz: 'satelliten/<TICKER>.md' (location='satelliten')
            # muss in config.satelliten sein, nicht nur watchlist
            if location == "satelliten" and ticker not in sat_set:
                failures.append(FailureDetail(
                    location=f"Vault entities/satelliten/{ticker}.md",
                    expected=f"{ticker} in config.satelliten (matches Vault folder)",
                    actual=f"{ticker} only in {'watchlist' if ticker in watch_set else 'keine_zuteilung'}",
                    severity="error",
                    hint=f"Vault-Pfad sagt satellit, config sagt nicht — entweder Vault → ersatzbank/ verschieben oder config.satelliten ergaenzen",
                ))
            else:
                n_passed += 1
        else:
            failures.append(FailureDetail(
                location=f"Vault entities/satelliten/{location}/{ticker}.md",
                expected=f"{ticker} in config.yaml (satelliten/watchlist/keine_zuteilung)",
                actual=f"{ticker} not present in any config-list",
                severity="warning",
                hint=f"Vault hat {ticker} aber config.yaml nicht — Sync-Gap oder Recherche-Kandidat noch nicht eingetragen",
            ))

    if n_checked == 0:
        # No Vault tickers found — graceful no-op
        return CheckResult(
            name="cross_source_reverse", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(VAULT_ENTITIES_REL),
                expected="vault entities present",
                actual="no ticker-bearing notes found",
                severity="warning",
                hint="Vault leer? Repo-Layout veraendert?",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="cross_source_reverse",
        status=status,  # type: ignore[arg-type]
        n_checked=n_checked,
        n_passed=n_passed,
        failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
