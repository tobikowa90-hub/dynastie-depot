#!/usr/bin/env python3
"""Suchraum-Komplement fuer die Depot-Architektur-Spec.

Beantwortet genau eine Frage: welche Datei im Repo kann Regelwerk oder
Live-State tragen, wird aber in der Spec nirgends genannt? Das ist die
Fehlerklasse, an der 00_Core/STATE.md fuenf Pruefrunden ueberlebt hat
(Spec 13, Codex-Befund C5-H2): ein Suchraum, der nach Datei-Sorte definiert
ist, findet keine Datei, die zu keiner der gesuchten Sorten gehoert.

Der Suchraum wird deshalb nicht geraten, sondern deklariert und mitgedruckt --
jede ausgeschlossene Verzeichnis-Klasse steht mit Begruendung im Report.

Matching ist strikt auf den Basename (nur .xlsx darf ohne Endung zitiert
werden -- so zitiert die Spec sie durchgaengig). Bewusst NICHT auf den Stem:
"STATE" in einer Aufzaehlung ist keine Behandlung als Quelle, und genau dieser
Nachlass liess v1.6 bei der Selbstpruefung durchgehen.

Exit 1, wenn Liste A nicht leer ist (Datei wird vom Agenten per Regel
geladen, kommt in der Spec aber nicht vor). Sonst Exit 0.

Run:
  python 03_Tools/spec_inventory_diff.py
  python 03_Tools/spec_inventory_diff.py --out 02_Analysen/spec-inventar.md
  python 03_Tools/spec_inventory_diff.py --spec 03_Tools/morning-briefing-spec.md
"""

import argparse
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SPEC_DEFAULT = "03_Tools/depot-architecture-spec.md"

# Was der Agent per Regel laedt bzw. was der Hook erzwingt. Aus diesen Dateien
# wird Tier A abgeleitet -- nicht handgepflegt, sondern extrahiert.
AGENT_READ_SOURCES = (
    "CLAUDE.md",
    ".pre-commit-config.yaml",
    "03_Tools/precommit/para18_sync_reminder.py",
)

FILE_TOKEN = re.compile(r"[\w./\\-]*[\w-]+\.(?:md|ya?ml|jsonl?|xlsx|py|toml|ps1|txt)\b")
EXTS = (".md", ".yaml", ".yml", ".json", ".jsonl", ".xlsx", ".py", ".toml", ".ps1", ".txt")

# Deklarierter Ausschluss. Wird im Report mit Begruendung und Anzahl gedruckt.
EXCLUDED_PREFIXES = (
    ("02_Analysen/", "Analyse-Output, kein Regelwerk"),
    ("04_Templates/", "Vorlagen, kein Live-State"),
    ("05_Archiv/", "historisch -- Ausnahme: *.jsonl (Live-Append-Ziele)"),
    ("06_Skills-Pakete/", "ZIP-Distribution, keine gelesene Quelle"),
    ("07_Obsidian Vault/", "Wiki-Korpus -- Ausnahme: WIKI-SCHEMA.md, log.md"),
)
VAULT_KEEP = ("WIKI-SCHEMA.md", "log.md")
NOISE_MARKERS = (
    "__pycache__/",
    "/tests/",
    "/test_fixtures/",
    "/_fixtures/",
    "node_modules/",
    ".venv/",
)


def git_files() -> list[tuple[str, bool]]:
    """(relpath, tracked) fuer alle getrackten + untracked-nicht-ignorierten Dateien."""

    def run(*args: str) -> list[str]:
        out = subprocess.run(
            ["git", "ls-files", "-z", *args], cwd=REPO, capture_output=True, text=True, check=True
        ).stdout
        return [p.replace("\\", "/") for p in out.split("\0") if p]

    tracked = run()
    untracked = run("--others", "--exclude-standard")
    return [(p, True) for p in tracked] + [(p, False) for p in untracked]


def excluded_reason(rel: str) -> str | None:
    """None = gehoert in den Suchraum. Sonst der Grund fuer den Ausschluss."""
    base = rel.rsplit("/", 1)[-1]
    if any(m in "/" + rel for m in NOISE_MARKERS):
        return "Cache / Test-Fixture"
    if base.startswith(("_test", "test_")):
        return "Cache / Test-Fixture"
    if rel.startswith("05_Archiv/"):
        return (
            None
            if rel.endswith(".jsonl")
            else "historisch -- Ausnahme: *.jsonl (Live-Append-Ziele)"
        )
    if rel.startswith("07_Obsidian Vault/"):
        return None if base in VAULT_KEEP else "Wiki-Korpus -- Ausnahme: WIKI-SCHEMA.md, log.md"
    for prefix, reason in EXCLUDED_PREFIXES:
        if rel.startswith(prefix):
            return reason
    return None


def read(rel: str) -> str:
    path = REPO / rel
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def tokens_in(text: str) -> set[str]:
    """Basenames aller Datei-artigen Tokens im Text."""
    found = set()
    for m in FILE_TOKEN.finditer(text):
        found.add(m.group(0).replace("\\", "/").rsplit("/", 1)[-1])
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--spec", default=SPEC_DEFAULT, help=f"zu pruefende Spec (default: {SPEC_DEFAULT})"
    )
    ap.add_argument("--out", help="Report zusaetzlich in diese Datei schreiben")
    args = ap.parse_args()

    spec_text = read(args.spec)
    if not spec_text:
        print(f"FEHLER: Spec nicht lesbar: {args.spec}", file=sys.stderr)
        return 2

    all_files = git_files()
    all_basenames = {rel.rsplit("/", 1)[-1] for rel, _ in all_files}

    universe: list[tuple[str, bool]] = []
    skipped: dict[str, int] = {}
    for rel, tracked in all_files:
        if not rel.endswith(EXTS):
            continue
        reason = excluded_reason(rel)
        if reason:
            skipped[reason] = skipped.get(reason, 0) + 1
        else:
            universe.append((rel, tracked))

    spec_tokens = tokens_in(spec_text)
    agent_tokens: set[str] = set()
    for src in AGENT_READ_SOURCES:
        agent_tokens |= tokens_in(read(src))

    def mentioned(rel: str) -> bool:
        base = rel.rsplit("/", 1)[-1]
        if base in spec_tokens:
            return True
        # Nur .xlsx zitiert die Spec durchgaengig ohne Endung ("Satelliten_Monitor_v4.0").
        # Fuer Textdateien waere derselbe Nachlass falsch: "STATE" in einer Aufzaehlung
        # ist keine Behandlung als Quelle -- genau daran scheiterten fuenf Pruefrunden.
        return base.endswith(".xlsx") and base[: -len(".xlsx")] in spec_text

    # Mehrdeutig: ein Basename, den die Spec nennt, zeigt im Repo auf mehrere Dateien.
    by_base: dict[str, list[str]] = {}
    for rel, _ in universe:
        by_base.setdefault(rel.rsplit("/", 1)[-1], []).append(rel)
    ambiguous = {b: paths for b, paths in by_base.items() if len(paths) > 1 and b in spec_tokens}

    tier_a, tier_b = [], []
    for rel, tracked in universe:
        if mentioned(rel):
            continue
        (tier_a if rel.rsplit("/", 1)[-1] in agent_tokens else tier_b).append((rel, tracked))

    stale = sorted(t for t in spec_tokens if t not in all_basenames)

    lines: list[str] = []
    add = lines.append
    add("# Suchraum-Komplement -- " + args.spec)
    add("")
    add("## Deklarierter Suchraum")
    add("")
    add("Grundmenge: `git ls-files` (getrackt) + untracked-nicht-ignoriert.")
    add("Endungen: " + " ".join(EXTS))
    add("Tier A = Basename kommt in " + ", ".join(AGENT_READ_SOURCES) + " vor.")
    add("Treffer heisst: exakter Basename im Spec-Text (.xlsx auch ohne Endung).")
    add("")
    add("| Dateien | ausgeschlossen, weil |")
    add("|---|---|")
    for reason, count in sorted(skipped.items(), key=lambda kv: -kv[1]):
        add(f"| {count} | {reason} |")
    add("")
    # Die Endungsliste ist selbst ein Suchraum nach Datei-Sorte -- also die Klasse
    # von Lücke, an der STATE.md durchrutschte. Deshalb wird sie mitgedruckt statt
    # stillschweigend vorausgesetzt.
    uncovered: dict[str, int] = {}
    for rel, _ in all_files:
        if rel.endswith(EXTS):
            continue
        base = rel.rsplit("/", 1)[-1]
        ext = "." + base.rsplit(".", 1)[-1] if "." in base else "(ohne Endung)"
        uncovered[ext] = uncovered.get(ext, 0) + 1
    if uncovered:
        add(
            "Endungen im Repo, die dieses Script gar nicht ansieht: "
            + " * ".join(f"{k} {v}" for k, v in sorted(uncovered.items(), key=lambda kv: -kv[1]))
        )
        add("")
    add(
        f"Im Suchraum: **{len(universe)}** Dateien. "
        f"Erwaehnt: **{len(universe) - len(tier_a) - len(tier_b)}**. "
        f"Nicht erwaehnt: **{len(tier_a) + len(tier_b)}** (A {len(tier_a)} / B {len(tier_b)})."
    )
    add("")

    def block(title: str, rows: list[tuple[str, bool]], note: str) -> None:
        add(f"## {title}")
        add("")
        add(note)
        add("")
        if not rows:
            add("- (leer)")
            add("")
            return
        groups: dict[str, int] = {}
        for rel, _ in rows:
            head = rel.split("/")[0] if "/" in rel else "(Wurzel)"
            groups[head] = groups.get(head, 0) + 1
        if len(groups) > 1:
            add(
                "Verteilung: "
                + " * ".join(f"{k} {v}" for k, v in sorted(groups.items(), key=lambda kv: -kv[1]))
            )
            add("")
        for rel, tracked in sorted(rows):
            add(f"- [ ] `{rel}`" + ("" if tracked else "  <- untracked"))
        add("")

    block(
        f"A -- vom Agenten gelesen, in der Spec nicht genannt ({len(tier_a)})",
        tier_a,
        "Die STATE.md-Klasse. Jede Zeile einzeln entscheiden: in die Spec aufnehmen oder begruendet abhaken.",
    )
    block(
        f"B -- im Suchraum, in der Spec nicht genannt ({len(tier_b)})",
        tier_b,
        "Nachrangig, aber ebenfalls einzeln abzuhaken -- B10 stand auch in keiner .md.",
    )

    add(f"## C -- mehrdeutige Nennung ({len(ambiguous)})")
    add("")
    add(
        "Die Spec nennt einen Basename, der im Repo mehrfach existiert. Gilt als erwaehnt, ist aber unscharf."
    )
    add("")
    if ambiguous:
        for base, paths in sorted(ambiguous.items()):
            add(f"- `{base}` -> " + ", ".join(f"`{p}`" for p in sorted(paths)))
    else:
        add("- (leer)")
    add("")

    add(f"## D -- Spec nennt, Repo hat nicht ({len(stale)})")
    add("")
    add("Veraltete oder erst zu erzeugende Referenz (z.B. REGELWERK.yaml ist Soll, nicht Ist).")
    add("")
    if stale:
        for tok in stale:
            add(f"- `{tok}`")
    else:
        add("- (leer)")
    add("")

    report = "\n".join(lines)
    print(report)
    if args.out:
        out_path = REPO / args.out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report + "\n", encoding="utf-8", newline="\n")
        print(f"\n[geschrieben] {args.out}")

    return 1 if tier_a else 0


if __name__ == "__main__":
    sys.exit(main())
