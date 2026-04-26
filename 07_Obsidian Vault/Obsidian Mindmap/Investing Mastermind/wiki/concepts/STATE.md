---
title: "STATE.md (Dynasty-Depot Hub)"
type: concept
aliases:
  - "STATE"
  - "STATE.md"
tags: [system, single-source-of-truth, hub]
created: 2026-04-23
updated: 2026-04-25
sources: []
related: [PORTFOLIO, PIPELINE, SYSTEM, CORE-MEMORY, Faktortabelle]
---

# STATE.md

> **Vault-externe Datei.** Liegt in `00_Core/STATE.md` außerhalb des Obsidian Vaults. Diese Wiki-Page existiert nur als Backlink-Anker.

## Rolle (seit Tier-2-Refactor 2026-04-25)

**Hub** — schlanker Navigations- und Critical-Alert-Layer (~40 Z). Enthält:
- Verweise auf die 3 Live-Satelliten ([[PORTFOLIO]] / [[PIPELINE]] / [[SYSTEM]])
- ⚠️ Critical-Alerts (≤ 10 Tage, handgepflegt)
- Navigation-Tabelle (on-demand Lektüre per Trigger)
- Last-Audit-Block (`system_audit.py`-Timestamp + Result)

Operative Inhalte (Scores, FLAGs, Sparraten, Watches, 30-Tage-Trigger) leben jetzt in [[PORTFOLIO]] — nicht mehr in STATE.md selbst.

## Wann lesen

Pflicht-Lektüre bei jedem `Session starten`-Trigger zusammen mit [[PORTFOLIO]] (default-load für 90% der Sessions). Andere 00_Core-Dateien on-demand via Routing-Table in CLAUDE.md.

## Pfad

`C:\Users\tobia\OneDrive\Desktop\Claude Stuff\00_Core\STATE.md`
