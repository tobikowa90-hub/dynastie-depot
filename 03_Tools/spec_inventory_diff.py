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

Exit 1, wenn A1 oder A2 nicht leer ist (Datei liegt auf dem Leseweg des
Agenten, kommt in der Spec aber nicht vor). Sonst Exit 0.

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
# 02_Analysen ist bewusst NICHT mehr ausgeschlossen: R5 fusste auf
# 02_Analysen/2026-09-04_Depot-Live-Verifikation.md.
EXCLUDED_PREFIXES = (
    ("04_Templates/", "Vorlagen, kein Live-State"),
    ("05_Archiv/", "historisch -- Ausnahme: *.jsonl (Live-Append-Ziele)"),
    ("06_Skills-Pakete/", "ZIP-Distribution, keine gelesene Quelle"),
    ("07_Obsidian Vault/", "Wiki-Korpus ohne Urteil/Regel im Frontmatter"),
)
VAULT_KEEP = ("WIKI-SCHEMA.md", "log.md")

# Frontmatter-Felder, die eine Vault-Seite zur Urteils- oder Regelwerk-Quelle machen.
# Empirisch erhoben (04.09.2026), nicht geraten: `score_aktuell` steht auf 15
# Entity-Seiten (12 mit echtem Wert), `operative_regel` auf 23 Concept-Seiten mit
# echten Scoring-Regeln. Ein pauschaler "Vault ist nur Wiki"-Ausschluss ist damit
# widerlegt -- das war dieselbe Ausschluss-nach-Sorte-Falle wie bei STATE.md.
# Bewusst NICHT drin: `defcon_relevanz` (41) -- Relevanz-Tag auf Papern, keine Regel.
VAULT_RULE_KEYS = (
    "score_aktuell",
    "score_valid_until",
    "flag",
    "defcon",
    "defcon_block",
    "operative_regel",
    "naechsterTrigger",
    "ersatz",
    "ticker",
)
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


def vault_rule_pages(files: list[tuple[str, bool]]) -> set[str]:
    """Vault-Seiten, deren Frontmatter Urteil (Score/FLAG) oder Regelwerk traegt."""
    hits = set()
    for rel, _ in files:
        if not (rel.startswith("07_Obsidian Vault/") and rel.endswith(".md")):
            continue
        txt = read(rel)
        if not txt.startswith("---"):
            continue
        end = txt.find("\n---", 3)
        frontmatter = txt[3:end] if end != -1 else ""
        if any(re.search(rf"^{k}:", frontmatter, re.MULTILINE) for k in VAULT_RULE_KEYS):
            hits.add(rel)
    return hits


def excluded_reason(rel: str, vault_rule: set[str]) -> str | None:
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
        if base in VAULT_KEEP or rel in vault_rule:
            return None
        return "Wiki-Korpus ohne Urteil/Regel im Frontmatter"
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
    vault_rule = vault_rule_pages(all_files)
    vault_md_total = sum(
        1 for rel, _ in all_files if rel.startswith("07_Obsidian Vault/") and rel.endswith(".md")
    )

    universe: list[tuple[str, bool]] = []
    skipped: dict[str, int] = {}
    for rel, tracked in all_files:
        if not rel.endswith(EXTS):
            continue
        reason = excluded_reason(rel, vault_rule)
        if reason:
            skipped[reason] = skipped.get(reason, 0) + 1
        else:
            universe.append((rel, tracked))

    spec_tokens = tokens_in(spec_text)
    agent_tokens: set[str] = set()
    for src in AGENT_READ_SOURCES:
        agent_tokens |= tokens_in(read(src))
    # Ein Hop weiter: was die per Regel gelesenen Dateien ihrerseits nennen.
    # `UMSTRUKTURIERUNG-2027.md` war NUR so erreichbar -- ueber `STATE.md`, nicht
    # ueber `CLAUDE.md` -- und landete deshalb in Liste B statt A. Wer nur A
    # abarbeitet, laeuft am staerksten Treffer vorbei.
    first_order = set(agent_tokens)
    for rel, _ in all_files:
        if rel.rsplit("/", 1)[-1] in first_order and rel.endswith((".md", ".yaml", ".yml", ".py")):
            agent_tokens |= tokens_in(read(rel))

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

    # A1/A2 getrennt, weil der Hop Tier A sonst von 3 auf 90 aufblaeht und als
    # Prioritaets-Signal wertlos wird. A1 = direkt in einer Regel-Datei genannt,
    # A2 = erst ueber deren Inhalt erreichbar (die UMSTRUKTURIERUNG-Klasse).
    tier_a1, tier_a2, tier_b = [], [], []
    for rel, tracked in universe:
        if mentioned(rel):
            continue
        base = rel.rsplit("/", 1)[-1]
        if base in first_order:
            tier_a1.append((rel, tracked))
        elif base in agent_tokens:
            tier_a2.append((rel, tracked))
        else:
            tier_b.append((rel, tracked))

    stale = sorted(t for t in spec_tokens if t not in all_basenames)

    lines: list[str] = []
    add = lines.append
    add("# Suchraum-Komplement -- " + args.spec)
    add("")
    add("## Deklarierter Suchraum")
    add("")
    add("Grundmenge: `git ls-files` (getrackt) + untracked-nicht-ignoriert.")
    add("Endungen: " + " ".join(EXTS))
    add(
        f"Tier A = Basename kommt in {', '.join(AGENT_READ_SOURCES)} vor -- **plus ein Hop**: "
        f"was diese Dateien ihrerseits nennen ({len(first_order)} Basenames erster Ordnung, "
        f"{len(agent_tokens)} nach dem Hop)."
    )
    add(
        f"Vault: {len(vault_rule)} von {vault_md_total} .md-Seiten sind im Suchraum, weil ihr "
        f"Frontmatter Urteil/Regel traegt ({', '.join(VAULT_RULE_KEYS)}); der Rest ist Korpus."
    )
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
    offen = len(tier_a1) + len(tier_a2) + len(tier_b)
    add(
        f"Im Suchraum: **{len(universe)}** Dateien. "
        f"Erwaehnt: **{len(universe) - offen}**. "
        f"Nicht erwaehnt: **{offen}** "
        f"(A1 {len(tier_a1)} / A2 {len(tier_a2)} / B {len(tier_b)})."
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
        f"A1 -- direkt in einer Regel-Datei genannt, in der Spec nicht ({len(tier_a1)})",
        tier_a1,
        "Die STATE.md-Klasse, schaerfste Stufe. Jede Zeile einzeln: in die Spec aufnehmen oder begruendet abhaken.",
    )
    block(
        f"A2 -- erst ueber den Inhalt einer Regel-Datei erreichbar ({len(tier_a2)})",
        tier_a2,
        "Die UMSTRUKTURIERUNG-Klasse: zweite Ordnung. Genau hier lag der staerkste Fund von R6, waehrend A1 leer aussah.",
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

    return 1 if tier_a1 or tier_a2 else 0


if __name__ == "__main__":
    sys.exit(main())
