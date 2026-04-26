---
title: "PIPELINE.md (Dynasty-Depot Pipeline-SSoT)"
type: concept
aliases:
  - "PIPELINE"
  - "PIPELINE.md"
tags: [system, single-source-of-truth, pipeline, planning]
created: 2026-04-25
updated: 2026-04-26
sources: []
related: [STATE, PORTFOLIO, SYSTEM, CORE-MEMORY]
---

# PIPELINE.md

> **Vault-externe Datei.** Liegt in `00_Core/PIPELINE.md` außerhalb des Obsidian Vaults. Diese Wiki-Page existiert nur als Backlink-Anker.

## Rolle (seit Tier-2-Refactor 2026-04-25)

**Pipeline-SSoT + Long-Term-Gates** — Single-Source-of-Truth für alle offenen Pläne, Gates und Termine. Ersetzt die frühere Fragmentierung über STATE.md + SESSION-HANDOVER.md + Plan-Files + Memory.

Strukturiert in:
- **🔴 Unmittelbar / Primär-Track** (offene Plan-Items, Hotfixes, Audit-Tasks, Konsolidierungstag-Blöcke)
- **Long-Term-Gates** (Score-Archiv-Review 2028-04-01, Score-Archiv-Interim-Gate 2026-10-17, R5-Interim-Gate 2027-10-19, etc.)
- Status-Marker (offen / in-progress / DONE / DEFER), zugehörige Spec/Plan-Files in `docs/superpowers/plans/`

## Wann lesen

On-demand bei Konsolidierungstag, System-Audit, Backlog-Review, Plan-Status-Check. Pipeline-Item-Changes erfordern §18-v2.1-Sync mit log.md (eigener Trigger neben Score-Events).

## Sync-Pflicht

Pipeline-Item-Status-Transition (ready→in-progress→done, deferred→active) triggert §18-v2.1-Pipeline-Item-Set: PIPELINE.md + log.md. Plan-Commits in `docs/superpowers/plans/` aktualisieren PIPELINE.md parallel.

## Pfad

`C:\Users\tobia\OneDrive\Desktop\Claude Stuff\00_Core\PIPELINE.md`
