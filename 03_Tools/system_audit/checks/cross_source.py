# -*- coding: utf-8 -*-
"""Check-3: Score/DEFCON/FLAG consistency across config.yaml / STATE.md /
Faktortabelle.md / Vault entity frontmatter.

Spec §5.1 Check-3, Codex-Patch P3 (FLAG-Parsing-Matrix).
"""
from __future__ import annotations

import re
import time
from pathlib import Path
from typing import Literal

import yaml

from system_audit.types import AuditContext, CheckResult, FailureDetail

FlagIcon = Literal["ok", "warn", "flag"]


def parse_flag_icon(cell: str) -> tuple[FlagIcon, str | None]:
    """Return (status, optional reason). Emoji is status, suffix text is reason."""
    s = cell.strip()
    if s.startswith("🔴"):
        return "flag", s[len("🔴"):].strip() or None
    if s.startswith("⚠️"):
        return "warn", s[len("⚠️"):].strip() or None
    if s.startswith("✅"):
        return "ok", s[len("✅"):].strip() or None
    raise ValueError(f"Unrecognized FLAG cell: {cell!r}")


def compare_flag(config_flag: bool, state_icon: FlagIcon) -> Literal["match", "error", "warning"]:
    """Implement Spec §5.1 Check-3 FLAG-Parsing-Matrix."""
    if state_icon == "ok":
        return "match" if not config_flag else "error"
    if state_icon == "warn":
        return "warning" if not config_flag else "error"
    # state_icon == "flag"
    return "match" if config_flag else "error"


def _parse_state_table(path: Path) -> dict[str, dict]:
    """Parse 'Ticker | Score | DEFCON | Rate | FLAG | ...' markdown table."""
    out: dict[str, dict] = {}
    in_table = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^\|\s*Ticker\s*\|\s*Score\s*\|\s*DEFCON", line):
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                break
            if re.match(r"^\|\s*-+", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            ticker = cells[0].replace("**", "").strip()
            try:
                score = int(re.sub(r"\D", "", cells[1]))
                defcon = int(re.sub(r"\D", "", cells[2].split()[-1]))
                flag_icon, flag_reason = parse_flag_icon(cells[4])
            except (ValueError, IndexError):
                continue
            out[ticker] = {"score": score, "defcon": defcon, "flag_icon": flag_icon, "flag_reason": flag_reason}
    return out


def _parse_faktortabelle(path: Path) -> dict[str, dict]:
    """Parse live Faktortabelle.md — header-driven column lookup.

    Live structure has 11+ columns including FCF-Marge, ROIC, Gross Margin,
    Debt/EBITDA, Moat before Score/DEFCON/FLAG. HTML-Comment-Rows between
    data rows (<!-- DATA:... -->) must be skipped, not treated as table-end.
    FLAG cell uses the same icon format as STATE.md (✅/⚠️/🔴 + reason text),
    not a boolean — convert via parse_flag_icon.
    """
    out: dict[str, dict] = {}
    col_idx: dict[str, int] | None = None
    saw_sep = False

    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()

        # Skip HTML comments between header-separator and/or data rows
        if stripped.startswith("<!--"):
            continue

        if col_idx is None:
            # Still searching for header
            if re.match(r"^\|\s*Position\s*\|", line):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                col_idx = {name: i for i, name in enumerate(cells)}
                continue
            continue

        if not saw_sep:
            # Next non-empty | line after header should be the separator
            if re.match(r"^\|\s*-+", line):
                saw_sep = True
                continue
            # Tolerant: if we hit a data row without explicit sep, proceed
            if not stripped.startswith("|"):
                continue
            saw_sep = True  # best-effort

        if not stripped.startswith("|"):
            break  # end of table

        cells = [c.strip() for c in stripped.strip("|").split("|")]

        def get(name: str) -> str | None:
            i = col_idx.get(name) if col_idx else None
            return cells[i] if i is not None and i < len(cells) else None

        def strip_bold(s: str | None) -> str:
            return (s or "").replace("**", "").strip()

        ticker_raw = strip_bold(get("Position"))
        if not ticker_raw or ticker_raw.startswith("-"):
            continue

        score_raw = strip_bold(get("Score"))
        defcon_raw = strip_bold(get("DEFCON"))
        flag_raw = strip_bold(get("FLAG"))
        if score_raw is None or defcon_raw is None:
            continue

        try:
            score_m = re.search(r"\d+", score_raw)
            score = int(score_m.group(0)) if score_m else None
            defcon_m = re.search(r"\d+", defcon_raw)
            defcon = int(defcon_m.group(0)) if defcon_m else None
        except ValueError:
            continue

        if score is None or defcon is None:
            continue

        # FLAG via icon parser; fallback boolean form for legacy/test fixtures
        flag_value: bool | None = None
        if flag_raw:
            try:
                icon, _reason = parse_flag_icon(flag_raw)
                flag_value = (icon == "flag")
            except ValueError:
                low = flag_raw.lower()
                if low in ("true", "ja", "yes"):
                    flag_value = True
                elif low in ("false", "nein", "no"):
                    flag_value = False

        out[ticker_raw] = {"score": score, "defcon": defcon, "flag": flag_value}

    return out


def _parse_vault_entities(entities_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not entities_dir.exists():
        return out
    for md in entities_dir.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        try:
            _, fm, _ = text.split("---", 2)
        except ValueError:
            continue
        try:
            data = yaml.safe_load(fm) or {}
        except yaml.YAMLError:
            continue
        if "score" not in data:
            continue
        ticker = data.get("ticker") or md.stem
        out[ticker] = {
            "score": int(data["score"]),
            "defcon": int(data.get("defcon", -1)) if data.get("defcon") is not None else None,
            "flag": bool(data.get("flag", False)),
        }
    return out


def run(
    repo_root: Path,
    context: AuditContext,
    *,
    sources_override: dict[str, Path | None] | None = None,
) -> CheckResult:
    start = time.monotonic()
    sources = sources_override or {
        "config": repo_root / "01_Skills" / "dynastie-depot" / "config.yaml",
        "state": repo_root / "00_Core" / "STATE.md",
        "faktortabelle": repo_root / "00_Core" / "Faktortabelle.md",
        "vault_entities_dir": repo_root / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind" / "wiki" / "entities",
    }

    failures: list[FailureDetail] = []
    n_checked = 0
    n_passed = 0

    cfg_path = sources["config"]
    if cfg_path is None or not cfg_path.exists():
        return CheckResult(
            name="cross_source", status="SKIP", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(cfg_path), expected="config.yaml present",
                actual="missing", severity="warning", hint="Skill-config-Pfad pruefen",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )

    try:
        config = yaml.safe_load(cfg_path.read_text(encoding="utf-8", errors="replace")) or {}
    except yaml.YAMLError as e:
        return CheckResult(
            name="cross_source", status="FAIL", n_checked=0, n_passed=0,
            failures=[FailureDetail(
                location=str(cfg_path.relative_to(repo_root)) if cfg_path.is_relative_to(repo_root) else str(cfg_path),
                expected="valid YAML",
                actual=f"YAMLError: {str(e)[:120]}",
                severity="error",
                hint="config.yaml manuell pruefen",
            )],
            duration_ms=int((time.monotonic() - start) * 1000),
            category="core",
        )
    satelliten = config.get("satelliten", [])
    state_by_ticker = _parse_state_table(sources["state"]) if sources.get("state") and sources["state"].exists() else {}
    fakt_by_ticker = _parse_faktortabelle(sources["faktortabelle"]) if sources.get("faktortabelle") and sources["faktortabelle"].exists() else {}
    vault_by_ticker = _parse_vault_entities(sources["vault_entities_dir"]) if sources.get("vault_entities_dir") else {}

    for sat in satelliten:
        try:
            ticker = sat["ticker"]
            c_score = sat["score"]
            c_defcon = sat["defcon"]
            c_flag = bool(sat.get("flag", False))
        except (KeyError, TypeError) as e:
            failures.append(FailureDetail(
                location=f"config.yaml: {sat if isinstance(sat, str) else sat.get('ticker', '<unknown>')}",
                expected="ticker+score+defcon keys",
                actual=f"malformed entry: {str(e)[:80]}",
                severity="error",
                hint="config.yaml-Entry strukturell defekt",
            ))
            continue

        for mirror_name, mirror in [("STATE.md", state_by_ticker), ("Faktortabelle.md", fakt_by_ticker), ("Vault", vault_by_ticker)]:
            if ticker not in mirror:
                if mirror_name == "Vault":
                    continue
                failures.append(FailureDetail(
                    location=f"{mirror_name}: {ticker}",
                    expected="present",
                    actual="missing",
                    severity="error",
                    hint=f"{mirror_name}-Zeile fuer {ticker} fehlt — config.yaml autoritativ",
                ))
                continue
            m = mirror[ticker]
            n_checked += 1

            if m.get("score") != c_score:
                failures.append(FailureDetail(
                    location=f"{mirror_name}: {ticker}",
                    expected=f"score={c_score}",
                    actual=f"{ticker} score={m.get('score')}",
                    severity="error",
                    hint=f"{mirror_name}-Zeile aktualisieren, config.yaml ist Wahrheitsquelle",
                ))
                continue
            # Skip DEFCON mismatch for Vault when defcon is absent (valid when entity carries only score)
            if mirror_name == "Vault" and m.get("defcon") is None:
                pass  # DEFCON not required in Vault frontmatter
            elif m.get("defcon") != c_defcon:
                failures.append(FailureDetail(
                    location=f"{mirror_name}: {ticker}",
                    expected=f"defcon={c_defcon}",
                    actual=f"{ticker} defcon={m.get('defcon')}",
                    severity="error",
                    hint=f"DEFCON-Mismatch — {mirror_name} syncen",
                ))
                continue
            if mirror_name == "STATE.md":
                verdict = compare_flag(c_flag, m["flag_icon"])
                if verdict == "error":
                    failures.append(FailureDetail(
                        location=f"{mirror_name}: {ticker}",
                        expected=f"FLAG matches config flag={c_flag}",
                        actual=f"icon={m['flag_icon']} reason={m.get('flag_reason')}",
                        severity="error",
                        hint="FLAG-Status reconcile (Spec §5.1 Check-3 Matrix)",
                    ))
                    continue
                elif verdict == "warning":
                    failures.append(FailureDetail(
                        location=f"{mirror_name}: {ticker}",
                        expected="watch-active consistent with config false",
                        actual=f"icon={m['flag_icon']} reason={m.get('flag_reason')}",
                        severity="warning",
                        hint="Watch ist informativ — kein Fehler",
                    ))
                    n_passed += 1
                    continue
            if mirror_name == "Faktortabelle.md":
                if m.get("flag") is not None and bool(m["flag"]) != c_flag:
                    failures.append(FailureDetail(
                        location=f"{mirror_name}: {ticker}",
                        expected=f"flag={c_flag}",
                        actual=f"flag={m['flag']}",
                        severity="error",
                        hint="Faktortabelle-FLAG-Spalte syncen",
                    ))
                    continue
            n_passed += 1

    has_error = any(f.severity == "error" for f in failures)
    has_warn = any(f.severity == "warning" for f in failures)
    status = "FAIL" if has_error else ("WARN" if has_warn else "PASS")

    return CheckResult(
        name="cross_source", status=status,  # type: ignore[arg-type]
        n_checked=n_checked, n_passed=n_passed, failures=failures,
        duration_ms=int((time.monotonic() - start) * 1000),
        category="core",
    )
