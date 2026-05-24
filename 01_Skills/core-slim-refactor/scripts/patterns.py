"""core-slim-refactor v0.1 — 3 Pattern Impls + shared helpers.

Pattern A: Bucket-Archive.
Pattern B: Slim-Convention.
Pattern C: Date-Cut.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# ───────────────── Shared types ─────────────────


@dataclass
class RowSet:
    archive: list[str] = field(default_factory=list)
    keep: list[str] = field(default_factory=list)
    slim_targets: list[str] = field(default_factory=list)  # Pattern B only


# ───────────────── Shared helpers ─────────────────


def _iter_section_rows(md: str, section_anchor: str | None) -> tuple[list[str], int, int]:
    """Return (lines_in_section, start_index, end_index_exclusive).

    If section_anchor=None, returns whole file. start/end are line-indices in
    the full file's split('\\n') list (used by mutators to splice back).
    """
    lines = md.split("\n")
    if section_anchor is None:
        return lines, 0, len(lines)

    start = None
    for i, line in enumerate(lines):
        if line.strip() == section_anchor.strip():
            start = i
            break
    if start is None:
        return [], 0, 0

    end = len(lines)
    section_level = section_anchor.count("#")
    for j in range(start + 1, len(lines)):
        stripped = lines[j].strip()
        if stripped.startswith("#"):
            j_level = len(stripped) - len(stripped.lstrip("#"))
            if 0 < j_level <= section_level:
                end = j
                break
    return lines[start:end], start, end


def _is_table_row(line: str) -> bool:
    """Detect markdown table row (starts with `|`)."""
    s = line.strip()
    return s.startswith("|") and s.endswith("|")


def _insert_after_last_table_row(lines: list[str], pointer_row: str) -> list[str]:
    """v0.1.2 MEDIUM-2: footer-aware pointer-insert. Walk backwards, find last
    `_is_table_row` index, insert pointer immediately after it (= before any
    trailing footer bullets, prose notes, or blanks). Falls back to plain
    append if section has no table rows.

    Pre-fix: chronological-fallback and section_bottom both appended
    unconditionally, placing pointer POST-footer (observed CORE-MEMORY.md L425
    after T2-Empirie 2026-05-24).
    """
    for i in range(len(lines) - 1, -1, -1):
        if _is_table_row(lines[i]):
            return [*lines[: i + 1], pointer_row, *lines[i + 1 :]]
    return [*lines, pointer_row]


def _extract_row_date(row: str) -> str | None:
    """Extract first ISO-8601 date YYYY-MM-DD from row."""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", row)
    return m.group(1) if m else None


# ───────────────── Pattern A: Bucket-Archive ─────────────────


def classify_bucket_archive(md: str, section_anchor: str | None, cfg: dict) -> RowSet:
    """Classify rows by keyword-match. Returns RowSet(archive, keep)."""
    section_lines, _, _ = _iter_section_rows(md, section_anchor)
    classify_cfg = cfg["classify"]
    keywords = classify_cfg["keywords"]
    keep_keywords = classify_cfg.get("keep_keywords", [])
    case_sensitive = classify_cfg.get("case_sensitive", True)

    def _match(row: str, terms: list[str]) -> bool:
        hay = row if case_sensitive else row.lower()
        targs = terms if case_sensitive else [t.lower() for t in terms]
        return any(t in hay for t in targs)

    rs = RowSet()
    for line in section_lines:
        if not _is_table_row(line):
            continue
        if "---" in line:  # table delimiter row
            continue
        if _match(line, keep_keywords):
            rs.keep.append(line)
            continue
        if _match(line, keywords):
            rs.archive.append(line)
        else:
            rs.keep.append(line)
    return rs


def mutate_bucket_archive(
    md: str,
    section_anchor: str | None,
    rowset: RowSet,
    cfg: dict,
    pointer_context: dict,
) -> str:
    """Replace archived rows with 1 chronological pointer-row. Returns new md."""
    if not rowset.archive:
        return md

    pointer_row = cfg["pointer"]["template"].format(**pointer_context).rstrip("\n")
    archive_set = set(rowset.archive)

    lines = md.split("\n")
    section_lines, sec_start, sec_end = _iter_section_rows(md, section_anchor)

    new_section_lines: list[str] = []
    pointer_inserted = False
    insert_at = cfg["pointer"].get("insert_at", "chronological")
    pointer_date = pointer_context.get("pointer_date", "9999-99-99")

    if insert_at == "chronological":
        kept_with_dates = []
        for line in section_lines:
            if line in archive_set:
                continue
            kept_with_dates.append((line, _extract_row_date(line)))

        for line, dt in kept_with_dates:
            if (
                not pointer_inserted
                and _is_table_row(line)
                and dt is not None
                and dt > pointer_date
            ):
                new_section_lines.append(pointer_row)
                pointer_inserted = True
            new_section_lines.append(line)
        if not pointer_inserted:
            # v0.1.2 MEDIUM-2: footer-aware fallback. Previously stripped only
            # trailing blanks, leaving footer bullets/prose AFTER the pointer.
            new_section_lines = _insert_after_last_table_row(new_section_lines, pointer_row)
            pointer_inserted = True
    elif insert_at == "section_top":
        for line in section_lines:
            if not pointer_inserted and _is_table_row(line) and "---" not in line:
                new_section_lines.append(pointer_row)
                pointer_inserted = True
            if line in archive_set:
                continue
            new_section_lines.append(line)
    else:  # section_bottom
        for line in section_lines:
            if line in archive_set:
                continue
            new_section_lines.append(line)
        # v0.1.2 MEDIUM-2: same footer-aware insertion as chronological fallback —
        # appending unconditionally placed pointer POST-footer-bullet.
        new_section_lines = _insert_after_last_table_row(new_section_lines, pointer_row)

    return "\n".join(lines[:sec_start] + new_section_lines + lines[sec_end:])


# ───────────────── Pattern B: Slim-Convention ─────────────────


def classify_slim_convention(md: str, section_anchor: str | None, cfg: dict) -> RowSet:
    """Detect fat-rows > threshold, honor exclude_keywords + exclude_dates."""
    section_lines, _, _ = _iter_section_rows(md, section_anchor)
    threshold = cfg["fat_threshold_bytes"]
    exclude_keywords = cfg.get("exclude_keywords", [])
    exclude_dates = cfg.get("exclude_dates", [])

    rs = RowSet()
    for line in section_lines:
        if not _is_table_row(line):
            continue
        if "---" in line and line.count("---") >= 1 and line.count("|") >= 2:
            stripped_cells = [c.strip() for c in line.split("|")[1:-1]]
            if all(set(c) <= set("-: ") for c in stripped_cells if c):
                continue
        row_bytes = len(line.encode("utf-8"))
        if row_bytes <= threshold:
            rs.keep.append(line)
            continue
        if any(kw in line for kw in exclude_keywords):
            rs.keep.append(line)
            continue
        row_date = _extract_row_date(line)
        if row_date in exclude_dates:
            rs.keep.append(line)
            continue
        rs.slim_targets.append(line)
        rs.archive.append(line)
    return rs


_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_PIPELINE_RE = re.compile(r"PIPELINE\s+(#\d+)")
_SHORT_SHA_RE = re.compile(r"\b([0-9a-f]{7})\b")


def _build_slim_row(fat_row: str, cfg: dict, slim_context: dict) -> str:
    """Build slim-version of fat-row: bold-title + outcome (max chars) + pointer-tail."""
    slim_cfg = cfg["slim"]
    outcome_max = slim_cfg["outcome_max_chars"]
    tail_fmt = slim_cfg["pointer_tail_format"]
    archive_link = slim_context["archive_link"]

    cells = [c.strip() for c in fat_row.split("|")[1:-1]]
    if not cells:
        return fat_row

    date_cell = cells[0] if cells else ""
    body_text = " ".join(cells[1:]) if len(cells) > 1 else ""

    title = ""
    if slim_cfg.get("extract_bold_title", True):
        m = _BOLD_RE.search(body_text)
        if m:
            title = f"**{m.group(1)}**"

    body_no_bold = _BOLD_RE.sub("", body_text)
    outcome = body_no_bold.strip()[:outcome_max]

    pipeline_ids = ""
    if slim_cfg.get("extract_pipeline_ids", True):
        ids = _PIPELINE_RE.findall(body_text)
        pipeline_ids = " ".join(ids) if ids else "(none)"

    short_shas = ""
    if slim_cfg.get("extract_short_shas", True):
        shas = _SHORT_SHA_RE.findall(body_text)
        short_shas = " ".join(shas) if shas else "(none)"

    tail = tail_fmt.format(
        archive_link=archive_link,
        pipeline_ids=pipeline_ids,
        short_shas=short_shas,
    )

    body_text_slim = f"{title} {outcome} — {tail}" if title else f"{outcome} — {tail}"
    new_cells = [date_cell, body_text_slim, *cells[2:]]
    return "| " + " | ".join(new_cells) + " |"


def mutate_slim_convention(
    md: str,
    section_anchor: str | None,
    rowset: RowSet,
    cfg: dict,
    slim_context: dict,
) -> str:
    """Replace each slim_target with its slim-version. Idempotent on already-slimmed input."""
    if not rowset.slim_targets:
        return md

    replacements = {fat: _build_slim_row(fat, cfg, slim_context) for fat in rowset.slim_targets}

    lines = md.split("\n")
    section_lines, sec_start, sec_end = _iter_section_rows(md, section_anchor)
    new_section_lines = [replacements.get(line, line) for line in section_lines]
    return "\n".join(lines[:sec_start] + new_section_lines + lines[sec_end:])


# ───────────────── Pattern C: Date-Cut ─────────────────


def _split_into_entries(md: str, header_pattern: str) -> list[tuple[str, str]]:
    """Split markdown into (header_line, body_with_header) chunks per header_pattern."""
    pattern = re.compile(header_pattern)
    lines = md.split("\n")
    entries: list[tuple[str, list[str]]] = [("", [])]
    for line in lines:
        if pattern.match(line):
            entries.append((line, [line]))
        else:
            entries[-1][1].append(line)
    return [(h, "\n".join(body)) for h, body in entries]


def classify_date_cut(md: str, section_anchor: str | None, cfg: dict) -> RowSet:
    """Classify entries by header-date vs cut_before. Entries before cut_before are archived."""
    cut_before = cfg["cut_before"]
    parser = cfg["date_parser"]
    pattern = parser["pattern"]
    date_re = re.compile(pattern)

    entries = _split_into_entries(md, pattern)
    rs = RowSet()
    for header, body in entries:
        if not header:
            rs.keep.append(body)
            continue
        m = date_re.match(header)
        if not m:
            rs.keep.append(body)
            continue
        entry_date = m.group(1)
        if entry_date < cut_before:
            rs.archive.append(body)
        else:
            rs.keep.append(body)
    return rs


def mutate_date_cut(
    md: str,
    section_anchor: str | None,
    rowset: RowSet,
    cfg: dict,
    pointer_context: dict,
) -> str:
    """Replace archived entries with single date-boundary pointer-header. Keep order intact."""
    if not rowset.archive:
        return md

    pointer_text = cfg["pointer"]["template"].format(**pointer_context)
    insert_at = cfg["pointer"].get("insert_at", "section_top")

    parser = cfg["date_parser"]
    pattern = parser["pattern"]
    date_re = re.compile(pattern)
    cut_before = cfg["cut_before"]

    entries = _split_into_entries(md, pattern)
    kept_chunks: list[str] = []
    pointer_inserted = False
    for header, body in entries:
        if not header:
            kept_chunks.append(body)
            continue
        m = date_re.match(header)
        if not m:
            kept_chunks.append(body)
            continue
        entry_date = m.group(1)
        if entry_date < cut_before:
            continue
        if not pointer_inserted and insert_at == "section_top":
            kept_chunks.append(pointer_text.rstrip("\n"))
            pointer_inserted = True
        kept_chunks.append(body)

    if not pointer_inserted:
        kept_chunks.append(pointer_text.rstrip("\n"))

    return "\n".join(kept_chunks)
