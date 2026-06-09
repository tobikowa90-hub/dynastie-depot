---
title: "PORTFOLIO.md (Dynasty-Depot Live-State)"
type: concept
aliases:
  - "PORTFOLIO"
  - "PORTFOLIO.md"
tags: [system, single-source-of-truth, live-state, projection-layer]
created: 2026-04-25
updated: 2026-06-09
sources: []
related: [STATE, PIPELINE, SYSTEM, CORE-MEMORY, Faktortabelle]
---

# PORTFOLIO.md

> **Vault-externe Datei.** Liegt in `00_Core/PORTFOLIO.md` außerhalb des Obsidian Vaults. Diese Wiki-Page existiert nur als Backlink-Anker.

## Rolle (seit Tier-2-Refactor 2026-04-25)

**Live-State** — default-load bei Session-Start (90% der Sessions). Enthält:
- Portfolio-Tabelle: 13 Satelliten mit Score, DEFCON, Rate, FLAG, nächster Trigger
- Sparraten-Nenner + Einzelraten + Summen-Check
- Aktive Watches (Grenzfälle, FLAG-Review-Pfade)
- 30-Tage-Trigger (klassifizierte Earnings-/Watch-Termine)
- Allokation-Status (60/35/5 Ziel + US-Hard-Cap-Check)

Operative Inhalte, die früher in [[STATE]] lebten — beim Tier-2-Refactor ausgelagert, damit STATE.md als schlanker Hub bleibt (~40 Z).

## Wann lesen

Pflicht-Lektüre bei jedem `Session starten`-Trigger zusammen mit [[STATE]]. Pipeline-Themen → [[PIPELINE]], Infrastruktur-/Audit-Themen → [[SYSTEM]].

## Sync-Pflicht

Score/FLAG/Sparraten-Changes triggern §18-v2.1-Sync inkl. PORTFOLIO.md (siehe [[Backtest-Ready-Infrastructure]] und [INSTRUKTIONEN §18](../../../../../00_Core/INSTRUKTIONEN.md)). Tripwire-Verifikation gegen `03_Tools/backtest-ready/_forward_verify_helpers.py:25` (`REQUIRED_TOUCH_FILES`).

## Pfad

`C:\Users\tobia\OneDrive\Desktop\Claude Stuff\00_Core\PORTFOLIO.md`
