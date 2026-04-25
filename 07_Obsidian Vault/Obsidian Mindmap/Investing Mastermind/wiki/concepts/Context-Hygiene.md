---
title: "Context-Hygiene"
type: concept
tags: [system, token-effizienz, claude, context-management]
related: "[[Token-Mechanik]], [[CLAUDE-md-Konstitution]], [[Context-Hygiene-Code]], [[Update-Klassen-DEFCON]]"
defcon_block: "System-Hygiene"
operative_regel: "Nur Pflicht-Lektüren im Session-Init laden — alles weitere strikt on-demand."
---

# Context-Hygiene

## Definition
Context-Hygiene bezeichnet die Disziplin, das Kontextfenster einer Claude-Session frei von unnötigem Rauschen zu halten. Konkret: nur die tatsächlich benötigten Dateien laden, MCP-Server auf das Minimum reduzieren und regelmäßig komprimieren. Eine schlechte Context-Hygiene führt zu langsameren Antworten, höherem Token-Verbrauch und Qualitätsdegradation gegen Sessionende.

## Regeln

### Init-Sequenz (Pflicht, Stand Tier-2-Refactor 2026-04-25)
```
1. STATE.md      → Hub: Verweise + Critical-Alerts + Last-Audit (~40 Z)
2. PORTFOLIO.md  → Live-State (default-load, 90% der Sessions)
```
Alle weiteren Dateien (PIPELINE / SYSTEM / CORE-MEMORY / INSTRUKTIONEN / KONTEXT / Faktortabelle / SESSION-HANDOVER) **on-demand via Routing-Table** in CLAUDE.md — trigger-spezifisch geladen, nicht beim Start.

Vorher (bis 16.04.2026): 4-Datei-Auto-Read (CORE-MEMORY + KONTEXT + INSTRUKTIONEN + Faktortabelle, ~1.200 Z) — abgelöst per [[Session-Start-Protokoll]]-Migration.

### MCP-Session-Typen

| Session-Typ | Aktive MCP-Server | Deaktivieren |
|-------------|------------------|--------------|
| Analyse | Shibui + defeatbeta + WebSearch | filesystem, andere |
| Wiki/Vault | filesystem | Shibui, defeatbeta |
| Hybrid | alle drei | — |

### Compact-Regeln
- **autoCompact:** bei 75% (settings.json: `autoCompactPercentageOverride: 75`)
- **Manueller /compact:** bei 60% mit Preserve-Anweisung
- **Preserve-Pflicht:** Score/Tabelle/Urteil/FLAGs (nie verwerfen)
- **Discard:** Datei-Inhalte bereits geschriebener Dateien

## Claude Code vs. Chat

| Feature | Claude Code | Chat / Cowork |
|---------|-------------|---------------|
| Tool Search | automatisch (ENABLE_TOOL_SEARCH=auto) | nicht verfügbar |
| MCP-Kontrolle | /mcp disable | manuell pro Session |
| autoCompact | settings.json konfigurierbar | nicht konfigurierbar |

→ Siehe [[Context-Hygiene-Code]] für Claude Code-spezifische Einstellungen

## Backlinks
- [[Token-Mechanik]] — Grundlagen der Token-Kosten
- [[CLAUDE-md-Konstitution]] — Session-Verhalten definiert dort
- [[Context-Hygiene-Code]] — Claude Code Implementierungsdetails
