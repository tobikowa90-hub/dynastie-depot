---
title: "Stop Building AI Agents. Use This Folder System Instead."
type: source
medium: video
tags: [claude-code, folder-architecture, routing, creator-content, adoption-pending]
created: 2026-04-23
updated: 2026-04-24
sources: [2026-03-10-jake-van-clief-folder-system-ai-agents]
related: [2026-04-22-dubibubii-claude-code-powerful-settings]

video:
  platform: youtube
  video_id: "MkN-ss2Nl10"
  source_url: "https://www.youtube.com/watch?v=MkN-ss2Nl10"
  source_url_checked: 2026-04-24
  channel: "Jake Van Clief"
  uploaded: 2026-03-10
  duration_min: 23
  chapters: true
  view_count: 68208
  like_count: 2559
  subscriber_count: 27900

transcript:
  asr_model: "whisper"
  asr_model_version: "large-v3"
  asr_implementation: "openai-whisper 20250625"
  ytdlp_version: "2026.03.17"
  ffmpeg_version: "ffmpeg version 8.1-full_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg de"
  segments: 321
  transcript_sha256: "7da0a220e86a95ddeada31d398b5090bfac64a774dbdcc621aa77e3d4632ef47"
  info_sha256: "2376b08412a5940fcb400acf76d8a669a15613e3dded9bd6246cb98b45f5b89d"
  chapters_sha256: "7e91c5dd2a998682903aba3a14e3d99f3eba3b7f4d5c3501f737e468b5cbd6c7"

language:
  content_language: en
  transcript_language: en
  note_language: de

manual_review: false
manual_review_reasons: []

adoption_decision:
  verdict: pending-brainstorm
  rationale: "Vorläufige Analyse ergab ~80%-Already-Implemented-Deckung, aber User-Pain liegt an anderer Stelle (Session-Start-Cost + globale Verlinkung + CLAUDE.md-Struktur). Entscheidung auf nächste Brainstorm-Session vertagt."
  adopted: []
  observe: []
  rejected: []
  deferred: [routing-table-read-skip]
  reviewed: 2026-04-24
---

# Stop Building AI Agents. Use This Folder System Instead.

**Source:** [Jake Van Clief — 2026-03-10](https://www.youtube.com/watch?v=MkN-ss2Nl10)
**Raw transcript:** [[transcript]] (in `raw/videos/updating-system/2026-03-10-jake-van-clief-folder-system-ai-agents/`)

## Source-Credibility

- **Sprecher:** Jake Van Clief — **unabhängiger Creator**, 27,9k Subs, 68k Views auf diesem Video, Like-Ratio 3,75%. Nicht Anthropic-Vertreter.
- **Framing:** Pedagogisch (erklärt Markdown/Tokens/VS Code von Grund auf) + **Decadal-Thinking-Pitch** — „concepts that last not concepts replaced next month", beruft sich auf „200 years of software engineering", schreibt Research Paper über Rules-of-Transparency/Composition zurück zu 1972. Template gated (VIP/Premium-Tier).
- **Polarität vs. Dubibubii:** Inverse. Dubibubii pitcht *Friction-Reduction* (Auto Mode, Focus Mode, Slash-go); Jake pitcht **Routing-Discipline + Explicit Load/Skip**. Der Friction-as-evidence-Flag aus Memory `feedback_friction_as_evidence.md` **zieht hier nicht** — aber neuer Flag-Kandidat: „Folder = App, kein Python, keine DB" als Anti-Framework-These.
- **Use-Case:** Content-Creator-Workflow (Writing/Production/Community als 3 Beispiel-Workspaces) — näher an Precision-Systems als Dubibubii, aber nicht identisch.
- **Evidenz-Klasse:** Plausibel, aber **2nd-hand** (Jake's eigene Synthese, Paper noch unveröffentlicht). Mittlere Evidenz-Stärke; Pattern-Quelle, kein empirisches Finding.

## Key Takeaways (7 Mechaniken)

1. **Three-Layer Routing Architecture** — Layer 1 CLAUDE.md (map, auto-loaded, floor plan), Layer 2 Workspace-Context-MD (room-level, task-specific), Layer 3 Skills/MCP (plug-and-play).
2. **Three-Workspace Blueprint** — Getrennte Workspaces für distinct Work-Types (im Beispiel: community / production / writing room). Jeder mit eigenem Context-File, eigenen Conventions.
3. **Routing Table Read/Skip/Maybe-Skill** — „Core pattern", laut Jake „the most important pattern in the whole system". Explizite Tabelle pro Task: welche Files laden, welche skippen, welche Skills ggf. pullen.
4. **Production-Pipeline inside Workspace** — 4-Stage (brief → spec → build → output), stage-specific Doc-Loading; ein Workspace-MD kann n Pipeline-Stages bedienen ohne Sub-Agents.
5. **Naming Conventions replace Databases** — Filename-Patterns (z.B. `2026-03-launch-week.md`) encoden Date/Topic/Status; AI navigiert via Filename-Convention statt Vector-DB/SQL/Postgres. „The folder IS your app."
6. **Skills aus Workspace-MD gecalled** (nicht top-level) — conditional auf Task-Stage. Skills inside MD-Routing, nicht als Always-Loaded-Set.
7. **English-only Routing / „Folder = Your App"** — Anti-Framework-These: keine Python-Injection, kein DB-Setup für Routing; pure Markdown + Filesystem-Hierarchie + natural-language Instructions.

## Adoption-Matrix gegen Korrektheits-Primat

| # | Mechanik | Vorläufiges Verdikt | Begründung |
|---|----------|---------------------|------------|
| 1 | Three-Layer Routing | 🟢 **ALREADY-IMPLEMENTED** | CLAUDE.md→00_Core→Skills ist exakt Jake's Pattern. Project-Root-CLAUDE.md = Layer 1, `00_Core/STATE.md`+`INSTRUKTIONEN.md`+`WIKI-SCHEMA.md` = Layer 2, Skills+MCP = Layer 3. Keine Strukturänderung nötig. |
| 2 | Three-Workspace Blueprint | 🟡 **OBSERVE** | De facto schon 3 Workspaces (00_Core / 07_Obsidian Vault / 03_Tools), aber nicht explizit so gelabelt. Formalisierung = kosmetisch. Re-Eval falls 4. Workspace wächst. |
| 3 | Routing Table Read/Skip | 🟡 **DEFERRED-TO-BRAINSTORM** | Adressiert potenziell den 21.04.-Drift-Lesson (Multi-SSoT-Fragmentierung) und den Session-Start-Cost-Pain. Keine isolierte Einzel-Adoption — Entscheidung in breiterer Session-Start-Optimierungs-Brainstorm-Session. |
| 4 | Pipeline inside Workspace | 🟢 **ALREADY-IMPLEMENTED** | `dynastie-depot` Skill Schritt 1-7, `backtest-ready-forward-verify` P1-P4, `earnings-preview`-Skill. Unsere Pipelines sind dichter als Jake's brief→spec→build→output (mit Gates, Validation, Append-Locks). |
| 5 | Naming Conventions replace DB | 🟡 **PARTIAL-ALREADY** | `docs/superpowers/plans/2026-04-21-*.md`, `raw/videos/updating-system/2026-03-10-*.md`, JSONL-Record-Keys — alles schon Convention-driven. **Aber:** `score_history.jsonl` + `flag_events.jsonl` bleiben Schema-validated (append-only, Duplicate-Guard, §28.2-Gate) — das ist Feature, kein Friction. Keine Änderung. |
| 6 | Skills aus Workspace-MD gecalled | 🟢 **ALREADY-IMPLEMENTED** | CLAUDE.md `## Wiki-Modus`: „Bei Wiki-Operationen … `WIKI-SCHEMA.md` lesen und Workflows folgen." Exakt Jake's conditional-activation. Keine Änderung. |
| 7 | English-only / Folder = App | 🔴 **REJECT-PARTIAL** | Anti-Framework-These widerspricht Python-Toolchain (`system_audit.py`, `portfolio_risk.py`, `backtest-ready/archive_score.py`). Schema-Validation in Code ist Korrektheits-Feature (v3.0.3-Incident-Präzedenz: Halluzination wurde nur sichtbar, weil Tool-Calls *nicht* in MD-Convention versteckt). „Folder = App"-Metapher ok für Doc-Routing, nicht für Execution-Layer. |

### Meta-Befund

Jake's Architektur ist **~80% bereits implementiert** in Dynasty-Depot. Das ist kein Zufall — über Monate dieselbe Pattern-Sammlung (Layered Routing + Skills-as-Subsystems + Naming-Conventions) aus eigenen Schmerzpunkten rekonstruiert, die er aus 1972-SW-Engineering herleitet. Unique add-value wäre **#3 Routing-Table** — aber nur wenn in breiterer Session-Start-Optimierungs-Diskussion sinnvoll integriert, nicht als isoliertes Item.

## Adoption-Status

**Vorläufiges Verdikt: `pending-brainstorm`.** Entscheidung vertagt — Video ist Input für eine breitere Brainstorm-Session zum Thema **CLAUDE.md-Struktur + Session-Start-Token-Cost + globale Verlinkung / Orphan-Elimination**. Nicht als isolierte Jake-Adoption zu behandeln.

Nächste Brainstorm-Session startet frisch (nach /clear 2026-04-24). Input-Referenzen für diese Session: dieses Dokument + User-Pain-Points im Handover. Keine Pre-Commit-Empfehlung aus dieser Page — bewusst offen gelassen.

## Notes

**Bezug zu Dubibubii-Precedent (22.04.):**
- Dubibubii = Creator mit Friction-Reduction-Pitch → `feedback_friction_as_evidence.md` Memory als Gegenflag.
- Jake = Creator mit Routing-Discipline/Durability-Pitch → **kein analoger Memory-Gegenflag** nötig (die Polarität passt zu Dynasty-Depot-Korrektheits-Primat). **Aber** neuer Anti-Pattern-Kandidat: „Replace all validation-code with naming-conventions" — in Precision-Systems (schema-validierte JSONL-Appends, Test-Coverage für Scoring-Hygiene, etc.) ist Code ein **Feature**, kein Friction. Falls ein 3. Creator dieselbe „code raus, nur Folders + MD"-These pitcht, Memory-Evidenz-Pattern dokumentieren.

**Dokumentarischer Wert der Source-Page:**
1. **Template-Präzedenz** für künftige Creator-Video-Ingests mit Routing-Discipline-Framing (vs. Dubibubii-Template für Friction-Reduction-Framing).
2. **Re-Eval-Trigger:** Falls Dynasty-Depot-Scope sich erweitert (z.B. multi-project mit ähnlicher Struktur, autonome Multi-Agent-Workflows) und Workspace-Grenzen unscharf werden, lohnt #2 + #3 Re-Review.
3. **Empirik-Gate:** Falls Session-Start-Cost-Pain nach künftigen Maßnahmen fortbesteht und explizite Read/Skip-Tables andernorts messbaren Gewinn zeigen, #3 Re-Adoption-Prüfung.

Third-Run der `ingest-video`-Pipeline (nach Pilot `Charlie-Automates-Graphify` 23.04. Nachmittag + Second-Run `Dubibubii-Powerful-Settings` 23.04. Abend). Whisper-Runtime: 5879s (≈98 min) für 23,3 min Audio = ~4,2× realtime mit `large-v3`-Modell (Quality-Gate PASS, 321 Segments, null Warns). Transcript/info/chapters SHA256 in Frontmatter, pinned Tool-Versionen. Pipeline-Verhalten weiter deterministisch.
