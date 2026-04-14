---
title: "Context-Hygiene — Claude Code spezifisch"
type: concept
tags: [system, claude-code, token-effizienz, mcp, settings]
related: "[[Context-Hygiene]], [[CLAUDE-md-Konstitution]], [[Token-Mechanik]]"
defcon_block: "System-Hygiene Claude Code"
operative_regel: "Tool Search (v2.1.7+) reduziert Token-Last um ~95% — nur mit Sonnet 4 / Opus 4 verfügbar."
---

# Context-Hygiene — Claude Code spezifisch

## Claude Code Optimierungen (settings.json)

### autoCompactWindow: 750000
- Zielgröße des Context-Fensters nach Auto-Komprimierung (750k von 1M Tokens)
- Frühere Komprimierung → ~250k Tokens Puffer für lange !Analysiere-Sessions
- Verhindert Qualitätsdegradation am Ende token-intensiver Workflows
- **Nur Claude Code** — in Chat/Cowork nicht verfügbar

### BASH_MAX_OUTPUT_LENGTH: 150000
- Verhindert silent truncation bei großen Terminal-Outputs
- Relevant für: `insider_intel.py scan ALL`, `eodhd_intel.py detail [TICKER]`
- Standard ohne Override: ~50.000 Zeichen (zu wenig für vollständige Scans)
- **Nur Claude Code**

### Deny Rules (angepasst — nicht .obsidian/** komplett)

```json
"permissions": {
  "deny": [
    "Edit(.obsidian/workspace.json)",
    "Write(.obsidian/workspace.json)",
    "Edit(.obsidian/appearance.json)",
    "Write(.obsidian/appearance.json)",
    "Edit(.obsidian/plugins/**)",
    "Write(.obsidian/plugins/**)",
    "Edit(node_modules/**)", "Write(node_modules/**)",
    "Edit(dist/**)", "Write(dist/**)",
    "Edit(.git/**)", "Write(.git/**)"
  ]
}
```

**Nicht ausschließen:**
- `.obsidian/app.json` → aktive Features (Backlinks, Graph View etc.)
- `.obsidian/core-plugins.json` → aktive Kern-Funktionen

**Begründung:** Kompletter `.obsidian/**`-Exclude blockiert Claude beim Lesen relevanter Vault-Konfiguration.

## Tool Search (Claude Code ab v2.1.7)

- **Funktion:** On-demand Tool-Discovery — lädt nur relevante MCP-Tool-Definitionen wenn Claude sie braucht
- **Vorteil:** ~95% Token-Reduktion vs. upfront-Loading aller Tool-Schemas
- **Aktivierung:** `ENABLE_TOOL_SEARCH=auto` (Standard-Einstellung ab v2.1.7)
- **Trigger:** Automatisch wenn MCP-Tools >10% des Kontextfensters belegen würden
- **Voraussetzung:** Sonnet 4 oder Opus 4 (Haiku nicht unterstützt)
- **Nur Claude Code** — in Chat/Cowork nicht verfügbar

## MCP-Session-Check (Chat + Cowork)

Tool Search gilt NUR für Claude Code. In Chat und Cowork:
- Manueller `/mcp disable [name]` nötig bei Session-Start
- Aktive MCP-Server mit `/mcp` auflisten
- Nicht benötigte Server deaktivieren (spart Init-Tokens)

**Empfehlung:** Ausgabe am Session-Start:
```
🔌 Aktive MCP-Server: [/mcp ausführen]
Analyse-Session: Shibui + defeatbeta + WebSearch
Vault-Session: filesystem
Nicht benötigt → /mcp disable [name]
```

## Backlinks
- [[Context-Hygiene]] — Allgemeine Regeln (plattformübergreifend)
- [[CLAUDE-md-Konstitution]] — Konfiguration ist dort dokumentiert
- [[Token-Mechanik]] — Kostenstruktur dahinter
