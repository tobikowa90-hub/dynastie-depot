"""core-slim-refactor v0.1 — Backlink-Scanner (Karpathy Pre-Refactor-Caller-Scan).

PFLICHT-Phase P3. Fail-close default. Bypass nur via 2-stufige YAML-Override.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class BacklinkHit:
    file: Path
    line_no: int
    term: str
    line_text: str


@dataclass
class BacklinkReport:
    hits: list[BacklinkHit] = field(default_factory=list)

    def summary(self) -> str:
        if not self.hits:
            return "BacklinkReport: 0 hits"
        return "\n".join(
            f"{h.file}:{h.line_no}: [{h.term}] {h.line_text.strip()[:120]}" for h in self.hits
        )


def scan_backlinks(
    scan_paths: Iterable[Path | str],
    search_terms: Iterable[str],
    case_sensitive: bool = True,
) -> BacklinkReport:
    """Grep search_terms across scan_paths. Returns BacklinkReport.

    Recursively scans .md files only. Skips binary + non-markdown.
    """
    report = BacklinkReport()
    terms = list(search_terms)
    if not case_sensitive:
        terms = [t.lower() for t in terms]

    for raw_path in scan_paths:
        path = Path(raw_path)
        if not path.exists():
            continue
        if path.is_file():
            _scan_file(path, terms, case_sensitive, report)
        else:
            for md_file in path.rglob("*.md"):
                _scan_file(md_file, terms, case_sensitive, report)
    return report


def _scan_file(
    path: Path,
    terms: list[str],
    case_sensitive: bool,
    report: BacklinkReport,
) -> None:
    try:
        with path.open(encoding="utf-8", newline="") as f:
            for i, line in enumerate(f, start=1):
                haystack = line if case_sensitive else line.lower()
                for t in terms:
                    if t in haystack:
                        report.hits.append(
                            BacklinkHit(
                                file=path.resolve(),
                                line_no=i,
                                term=t,
                                line_text=line.rstrip("\r\n"),
                            )
                        )
    except OSError, UnicodeDecodeError:
        pass  # skip unreadable files (binary, encoding error)
