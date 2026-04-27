"""Phase-2 Schema-Drift-Cleanup: related quoted-string → YAML Block-Array.

Pattern (Phase-1-validated, McLean-Pontiff-Reference):
  before: related: "[[A]], [[B]], [[C]]"
  after:  sources: []   (only if sources: field absent)
          related:
            - "[[A]]"
            - "[[B]]"
            - "[[C]]"

Run:
  python 03_Tools/schema_drift_phase2.py --dry-run    # show diff stats
  python 03_Tools/schema_drift_phase2.py --apply      # write files
"""
import argparse
import pathlib
import re
import sys

VAULT = pathlib.Path("07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki")
RELATED_LINE = re.compile(r'^related:\s*"([^"]*)"\s*$', re.MULTILINE)
SOURCES_LINE = re.compile(r'^sources:', re.MULTILINE)


def convert(text: str):
    """Returns (new_text, items_count, sources_inserted) or None if skip."""
    line_end = "\r\n" if "\r\n" in text else "\n"
    m = RELATED_LINE.search(text)
    if not m:
        return None

    content = m.group(1).strip()
    if not content:
        replacement = "related: []"
        items_count = 0
    else:
        items = [i.strip() for i in re.split(r',\s*', content) if i.strip()]
        for item in items:
            if not (item.startswith('[[') and item.endswith(']]')):
                return None  # bail on non-wikilink tokens
        block = ["related:"] + [f'  - "{item}"' for item in items]
        replacement = line_end.join(block)
        items_count = len(items)

    new_text = text[:m.start()] + replacement + text[m.end():]

    sources_inserted = False
    if not SOURCES_LINE.search(new_text):
        m2 = re.search(r'^related:', new_text, re.MULTILINE)
        new_text = new_text[:m2.start()] + "sources: []" + line_end + new_text[m2.start():]
        sources_inserted = True

    return new_text, items_count, sources_inserted


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write files")
    parser.add_argument("--dry-run", action="store_true", help="show stats only")
    args = parser.parse_args()
    if not args.apply and not args.dry_run:
        parser.error("specify --dry-run or --apply")

    files = []
    for p in VAULT.rglob("*.md"):
        txt = p.read_text(encoding="utf-8", newline="")
        if re.search(r'^related:\s*"', txt, re.MULTILINE):
            files.append(p)

    print(f"Phase-2 candidates: {len(files)}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print("-" * 100)

    converted = 0
    skipped = 0
    total_items = 0
    total_sources_inserted = 0

    for f in sorted(files):
        txt = f.read_text(encoding="utf-8", newline="")
        result = convert(txt)
        if result is None:
            skipped += 1
            print(f"SKIP   {f.relative_to(VAULT)} (non-wikilink token)")
            continue
        new_text, items_count, sources_inserted = result
        converted += 1
        total_items += items_count
        if sources_inserted:
            total_sources_inserted += 1
        marker = "+S" if sources_inserted else "  "
        if args.apply:
            f.write_text(new_text, encoding="utf-8", newline="")
            print(f"WRITE  {marker} {items_count:>2} items  {f.relative_to(VAULT)}")
        else:
            print(f"WOULD  {marker} {items_count:>2} items  {f.relative_to(VAULT)}")

    print("-" * 100)
    print(f"Converted: {converted} | Skipped: {skipped} | "
          f"Total wikilinks: {total_items} | sources:[] inserted: {total_sources_inserted}")
    return 0 if skipped == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
