# LLM Wiki Schema — WIKI-SCHEMA.md

> **Scope:** Gilt ausschließlich für Wiki-Operationen im Obsidian Vault (ingest, query, lint, edit).
> Für Dynasty-Depot Analyse-Sessions → `00_Core/` Dateien lesen.

---

## Role

You are the maintainer of this wiki. The human curates sources and asks questions.
You write and maintain all wiki pages. You never modify files under `raw/`.
This document is the authoritative schema. Follow it in every session.

---

## Directory Structure

```
07_Obsidian Vault/          ← Vault-Root (nach Integration in Claude Stuff)
  WIKI-SCHEMA.md            ← dieses Dokument (Schema + Regeln)
  CLAUDE.md                 ← kurzer Scope-Hinweis (auto-geladen)
  index.md                  ← Content-Katalog; bei jeder Operation aktualisieren
  log.md                    ← append-only Activity Log
  raw/                      ← immutable Quelldokumente (nie editieren)
    assets/                 ← heruntergeladene Bilder und Anhänge
  wiki/
    entities/               ← Personen, Organisationen, Produkte, Projekte
    concepts/               ← Ideen, Themen, Frameworks, Methoden
    sources/                ← eine Zusammenfassungsseite pro ingested Source
    synthesis/              ← Quer-Analysen, Thesen, evolving understanding
    queries/                ← gespeicherte Antworten auf wichtige Fragen
```

---

## Page Frontmatter

Every page in `wiki/` uses this YAML frontmatter:

```yaml
---
title: "Page Title"
type: entity | concept | source | synthesis | query
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug]          # source pages that mention this topic
related: [other-page-slug]      # other wiki pages that connect to this
---
```

---

## Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| File names | kebab-case.md | `neural-networks.md` |
| Source slugs | kebab-case from title | `attention-is-all-you-need` |
| Page titles | Title Case | `Neural Networks` |
| Tags | lowercase, hyphenated | `machine-learning`, `ai` |
| Dates | ISO 8601 | `2026-04-09` |

---

## Cross-Referencing

- Use Obsidian wiki-link syntax: `[[Page Title]]`
- Every named entity or concept first mentioned on a page should be wiki-linked if a page exists for it
- Proactively create a new page for any entity/concept important enough to deserve one
- Every new page must be linked from at least one existing page — no orphans
- Source pages link to entity and concept pages they mention; entity/concept pages link back to source pages via frontmatter `sources:` field
- **Sibling-Linking:** Konzeptseiten im gleichen Themencluster (z.B. alle DEFCON-Konzepte) verlinken sich gegenseitig — nicht nur zum Hub

---

## Workflows

### INGEST
Triggered when the human says: *"ingest [source]"* or drops a file in `raw/`.

1. Read the source document
2. Present 3–5 bullet key takeaways; briefly discuss with the human
3. Create a source summary page in `wiki/sources/<slug>.md`
   - **Backlink-Pflicht:** Source-Seite MUSS einen Link zum Raw-Dokument enthalten (`[[Originaltitel]]`)
4. Create or update entity pages for all named entities of significance
   - **Autoren-Pflicht:** Für jeden Autor mit `[[Wiki-Link]]` im Raw-Frontmatter eine Entity-Seite anlegen
   - **Ersatz-Ticker-Pflicht:** Referenzierte Ersatz-Ticker in Entity-Seiten brauchen eigene Seiten in `entities/ersatzbank/`
5. Create or update concept pages for key ideas introduced or reinforced
6. Update any synthesis pages whose thesis is affected by the new source
7. Update `index.md` — add all new/changed pages
8. Append an entry to `log.md`
9. **Auto-Lint:** Prüfe alle neu erstellten/geänderten Seiten auf Orphans und broken Links — sofort fixen

Rule: a single ingest may touch 5–20 pages. That is expected and correct.

### QUERY
Triggered when the human asks a question.

1. Read `index.md` to identify relevant pages
2. Read those pages; synthesize an answer with inline citations using `[[Page]]`
3. After answering, ask: *"Want me to save this as a query page?"*
4. If yes, create `wiki/queries/<slug>.md` and update `index.md` and `log.md`

### LINT
Triggered when the human says: *"lint"*.

1. Scan all pages for orphan pages (no inbound links from other pages)
2. Look for contradictions or stale claims between pages
3. Identify important concepts mentioned in passing but lacking their own page
4. Note data gaps that a web search or new source could fill
5. Suggest new questions or sources to investigate
6. Report all findings; ask the human which issues to fix now

---

## Log Entry Format

```
## [YYYY-MM-DD] operation | Title or Description
- Summary of what was done
- Pages created: [[Page1]], [[Page2]]
- Pages updated: [[Page3]], [[Page4]]
```

Operations: `ingest`, `query`, `lint`, `edit`, `setup`

---

## Index Entry Format

Entries in `index.md` are grouped by page type. Each line:

```
- [[Page Title]] — one-line description (N sources)
```

---

## Growth Rules

1. Prefer **updating** existing pages over creating new ones when new info fits
2. `source` pages are granular — one per document ingested
3. `concept` and `entity` pages synthesize across sources — they grow richer over time
4. `synthesis` pages are the highest-value artifact — accumulated understanding, evolving thesis
5. When a topic appears in 3+ sources, create a dedicated synthesis page if one doesn't exist
6. When a synthesis page contradicts a new source, note the contradiction explicitly on both pages
7. Do not let `index.md` grow stale — update it on every operation that creates or renames pages

---

## Session Start Checklist (Wiki-Modus)

Bei Wiki-Operationen (ingest / lint / query):
1. `index.md` lesen — aktuellen Wiki-State erfassen
2. Letzte 5 Einträge in `log.md` lesen
3. Bestätigen: *"Wiki geladen. [N] Seiten. Was möchtest du tun?"*
