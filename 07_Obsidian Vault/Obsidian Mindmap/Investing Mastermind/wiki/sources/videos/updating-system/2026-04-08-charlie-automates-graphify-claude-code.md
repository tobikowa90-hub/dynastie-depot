---
title: "Everything You Need To Know About Graphify For Claude Code"
type: source
medium: video
tags: [claude-code, knowledge-graph, plugin, tooling, token-efficiency, pilot-ingest]
created: 2026-04-23
updated: 2026-04-23
sources: [2026-04-08-charlie-automates-graphify-claude-code]
related: [Knowledge-Graph-Finance-Architecture, Token-Mechanik]

video:
  platform: youtube
  video_id: "A6lwT0Vd0fE"
  source_url: "https://www.youtube.com/shorts/A6lwT0Vd0fE"
  source_url_checked: 2026-04-23
  channel: "Charlie Automates"
  uploaded: 2026-04-08
  duration_min: 2
  chapters: false

transcript:
  asr_model: "whisper"
  asr_model_version: "small"
  asr_implementation: "openai-whisper 20250625"
  ytdlp_version: "2026.03.17"
  ffmpeg_version: "ffmpeg version 8.1-full_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg de"
  segments: 26
  transcript_sha256: "a2b1d73363ab765e5bd16ad1ecb021dfbf06619021875781926a0d7238257697"
  info_sha256: "3b435bae6c5a6ad5268b0feeb9f15083967879f71a9f06f4a18346337257977c"
  chapters_sha256: null

language:
  content_language: en
  transcript_language: en
  note_language: de

manual_review: false
manual_review_reasons: []
---

# Everything You Need To Know About Graphify For Claude Code

**Source:** [Charlie Automates — 2026-04-08](https://www.youtube.com/shorts/A6lwT0Vd0fE)
**Raw transcript:** [[transcript]] (in `raw/videos/updating-system/2026-04-08-charlie-automates-graphify-claude-code/`)

## Key Takeaways

- **Graphify** ist ein Plugin/Skill für Claude Code, das aus PDFs, Markdown, Screenshots und anderen Assets in einem Repo automatisch einen Knowledge-Graph baut.
- Inspiriert von **Andrej Karpathy** (Mitgründer OpenAI) — Idee: "raw folder dump it all, let Claude sift through it" — Claude Code nutzt aktuell typisch grep, was teuer ist.
- **Token-Effizienz**: ~70x weniger Tokens pro Query laut Demo, persistent über Sessions hinweg.
- Findet **semantische Cross-Domain-Verbindungen** (z.B. Business-Operations ↔ School-Community).
- Installation per Repo-Install-Command direkt in Claude Code.

## Relevanz für Dynastie-Depot

Direkter Bezug zu unserer **Vault-Architektur**: Wir bauen aktuell manuell den Wiki-Graphen (siehe heutige 100%-Backlink-Closure, 46 Aliases + Stub-Pages). Graphify könnte:
- **Auto-Linking** beim Paper-/Video-Ingest übernehmen (statt manueller Entity/Concept-Anlage in INGEST-Schritt 4-5)
- Das aktuelle WIKI-SCHEMA §INGEST-Workflow-Pflichtprogramm (Entities + Concepts + Synthesis-Updates) automatisieren
- Token-Budget für !Analysiere-Sessions deutlich reduzieren (Token-Mechanik)

**Status: Beobachtung.** Eval-Trigger: nächster größerer Multi-Paper-Ingest (Phase 2) — Graphify gegen den manuellen INGEST-Workflow vergleichen, dann entscheiden ob als Pre-Step in §INGEST aufnehmen.

## Notes

Pilot-Ingest der Video-Pipeline (Task 9 des Video-Ingest-Spec). Diente primär dem End-to-End-Test, nicht der inhaltlichen Tiefe — daher kompakte Takeaways. Bei Adoption-Entscheidung ggf. Re-Ingest mit `whisper large-v3` für höhere Transkript-Genauigkeit.
