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
    papers/                 ← akademische PDFs/MDs
    tools/                  ← Tool-Docs, Skill-Manifeste
    earnings/               ← Earnings-Reports, Transkript-Quellen
    macro/                  ← Macro/Konjunktur-Quellen
    videos/                 ← yt-dlp+whisper-Pipeline-Output
      earnings-calls/<slug>/  (transcript.md, info.json, chapters.json, run.log)
      interviews/<slug>/
      conferences/<slug>/
      analyses/<slug>/
    assets/                 ← heruntergeladene Bilder und Anhänge
  wiki/
    entities/               ← Personen, Organisationen, Produkte, Projekte
    concepts/               ← Ideen, Themen, Frameworks, Methoden
    sources/                ← eine Zusammenfassungsseite pro ingested Source
      papers/               ← akademische Quellen
      tools/                ← Skills, Datenquellen, Tools
      references/           ← Methodik, Standards, Benchmarks
      videos/               ← spiegelt raw/videos/-Kategorien
        earnings-calls/  interviews/  conferences/  analyses/
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
medium: paper | video | tool | report   # nur bei type=source erforderlich
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug]          # source pages that mention this topic
related: [other-page-slug]      # other wiki pages that connect to this
aliases:                        # Title-Case-Synonyme für Backlink-Auflösung
  - "Display Name 1"
  - "Display Name 2"
---
```

**Bei `medium: video`** zusätzliche Blöcke (siehe §INGEST-VIDEO):

```yaml
video:
  platform: youtube              # youtube | vimeo | direct | other
  video_id: "abc123XYZ"
  source_url: "https://..."
  source_url_checked: YYYY-MM-DD
  channel: "Channel Name"
  uploaded: YYYY-MM-DD           # Original-Upload, nicht Ingest
  duration_min: 312
  chapters: true

transcript:
  asr_model: "whisper"
  asr_model_version: "large-v3"
  asr_implementation: "openai-whisper 20231117"
  ytdlp_version: "2024.04.09"
  ffmpeg_version: "6.1.1"
  segments: 1847
  transcript_sha256: "..."
  info_sha256: "..."
  chapters_sha256: "..."         # null wenn keine Chapters

language:
  content_language: en           # gesprochen im Video
  transcript_language: en        # persistiertes Transkript
  note_language: de              # Sprache der Obsidian-Notizen-Prosa

manual_review: false             # true wenn Quality-Gate WARN ausgelöst
manual_review_reasons: []        # z.B. ["word_density_low"]
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

**Video-spezifische Slugs:**

| Thing | Convention | Example |
|---|---|---|
| Video slug | `<YYYY-MM-DD>-<channel>-<topic>` | `2024-05-04-brk-annual-qa` |
| Channel slug | kebab-case Kurzform | `brk`, `acquired`, `bg2`, `tmo` |
| Same-day collision | suffix `-2`, `-3` | `2026-04-22-tmo-q1-2` |

---

## Cross-Referencing

- Use Obsidian wiki-link syntax: `[[Page Title]]`
- Every named entity or concept first mentioned on a page should be wiki-linked if a page exists for it
- Proactively create a new page for any entity/concept important enough to deserve one
- Every new page must be linked from at least one existing page — no orphans
- Source pages link to entity and concept pages they mention; entity/concept pages link back to source pages via frontmatter `sources:` field
- **Sibling-Linking:** Konzeptseiten im gleichen Themencluster (z.B. alle DEFCON-Konzepte) verlinken sich gegenseitig — nicht nur zum Hub
- **Sub-Ordner-Transparenz:** Backlinks `[[Page Title]]` resolven über Basename, pfad-unabhängig. Wiki-Pages in `wiki/sources/papers/`, `wiki/sources/videos/<kat>/` usw. werden identisch zu Top-Level-Pages verlinkt — die Sub-Ordner-Struktur ist ein Organisations-Layer, kein Schema-Diskriminator. Der wahre Source-Typ steht im Frontmatter `medium:`-Feld.
- **Alias-Pflicht für Title-Case-Refs:** Wenn ein Page-Filename kebab-case ist (`gpt-4.md`), aber im Vault als `[[GPT-4]]` referenziert wird, MUSS die Page einen `aliases:`-Block im Frontmatter haben. Ohne Alias bricht der Backlink. Bei Bulk-Ingest aller neuen Pages auf Title-Case-Aliases prüfen.

---

## Workflows

### INGEST

> **Bei Video-Quellen:** Zuerst §INGEST-VIDEO ausführen (Schritte 1-7). Diese Liste hier (Schritte 4-9) wird dann ab Schritt 4 fortgesetzt.

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

### INGEST-VIDEO
Triggered when the human says: *"ingest video <url>"* or runs `python 03_Tools/video_ingest.py <url>`.

Eigenständiger Workflow — NICHT Pre-Step zu generischem INGEST.

1. **yt-dlp download** → `raw/videos/<kategorie>/<slug>/{audio.m4a, info.json, chapters.json}`
2. **whisper transcribe** → `raw/videos/<kategorie>/<slug>/transcript.md` (mit Timestamps)
3. **Cleanup (Variante A)** — `audio.m4a` löschen; transcript/info/chapters bleiben
4. **Hashes berechnen** — sha256 für transcript.md, info.json, chapters.json
5. **Quality-Gate** prüfen (siehe Tabelle unten):
   - PASS → continue
   - FAIL → abort, kein Source-Page-Write, error nach `run.log`
   - WARN → continue, aber `manual_review: true` ins Source-Page-Frontmatter
6. **`run.log` schreiben** — Tool-Versionen (yt-dlp, whisper, ffmpeg), Exit-Codes, Wall-Clock-Dauer pro Schritt, Quality-Gate-Resultate
7. **Source-Page anlegen** in `wiki/sources/videos/<kategorie>/<slug>.md` mit vollständigem Frontmatter (siehe §Page Frontmatter)
8. **Standard-INGEST ab Schritt 4** der INGEST-Workflow-Liste — Entities, Concepts, Synthesis, index.md, log.md, Auto-Lint

**Quality-Gate (analog Algebra-Δ-Gate INSTRUKTIONEN §28.2):**

| # | Check | Threshold | Severity | Action |
|---|---|---|---|---|
| 1 | Transkript nicht leer | `len > 500 chars` | FAIL | abort |
| 2 | Duration vorhanden | `duration_min > 0` | FAIL | abort |
| 3 | Wort-Dichte | `words/min ∈ [80, 250]` | WARN | `manual_review` |
| 4 | Segment-Count | `segments/min ∈ [3, 30]` | WARN | `manual_review` |
| 5 | Sprach-Match | `whisper_lang == content_language` (übersprungen wenn `expected_lang` leer) | WARN | `manual_review` |
| 6 | Chapters extrahiert | bool | INFO | `chapters: true/false` |
| 7 | URL erreichbar | HTTP 200 zur Ingest-Zeit | FAIL | abort |

**Reproduzierbarkeit:** Tool-Versionen sind in **zwei** Orten gepinnt — `run.log` (vollständig) und `wiki/sources/videos/<kategorie>/<slug>.md` Frontmatter `transcript:`-Block (kanonisch für Audit).

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
8. **Cross-Medium-Aggregation:** Concept- und Entity-Pages aggregieren über alle `medium`-Typen hinweg (Paper, Video, Tool, Report). Eine Concept-Page zu „Moat" zieht Quellen aus `sources/papers/` UND `sources/videos/conferences/` etc. — die Sub-Ordner-Struktur ändert nichts an der semantischen Verlinkung.

---

## Session Start Checklist (Wiki-Modus)

Bei Wiki-Operationen (ingest / lint / query):
1. `index.md` lesen — aktuellen Wiki-State erfassen
2. Letzte 5 Einträge in `log.md` lesen
3. Bestätigen: *"Wiki geladen. [N] Seiten. Was möchtest du tun?"*
