---
title: "Token-Mechanik"
type: concept
tags: [system, token-effizienz, claude, session-management]
related: "[[Context-Hygiene]], [[CLAUDE-md-Konstitution]], [[Context-Hygiene-Code]], [[Update-Klassen-DEFCON]]"
defcon_block: "System-Hygiene"
operative_regel: "Token-Kosten durch strukturiertes Laden minimieren — kein redundantes Vollladen großer Dateien."
---

# Token-Mechanik

## Definition
Token-Mechanik beschreibt, wie Claude-Sessions Kontextfenster-Kapazität verbrauchen und wie dieser Verbrauch durch Struktur minimiert wird. Jedes geladene Dokument, jedes Tool-Result und jede Konversationsrunde kostet Tokens. Bei 200k Kontextfenster und langen Analysen kann ineffizientes Laden zu vorzeitiger Komprimierung oder Qualitätsdegradation führen.

## Schlüsselprinzipien

| Prinzip | Mechanismus | Auswirkung |
|---------|-------------|-----------|
| Snapshot-First | Faktortabelle lesen vor API-Abfragen | Spart 3–5 Tool-Calls |
| On-Demand-Loading | Wiki-Seiten nur bei Bedarf laden | Kein Vorab-Kontextverbrauch |
| /compact bei 60% | Frühzeitige Komprimierung | Verhindert Late-Session-Degradation |
| Tool Search | MCP-Tools nur bei Bedarf laden | ~95% Tool-Token-Reduktion (Claude Code v2.1.7+) |
| BASH_MAX_OUTPUT | 150.000 Zeichen Limit | Verhindert silent truncation bei großen Outputs |

## Operative Regeln für DEFCON-Sessions

1. **Pflicht-Lektüre zuerst:** `00_Core/STATE.md` (seit 17.04.2026 Single-Entry-Point, ~80 Zeilen). Andere 00_Core-Dateien on-demand — siehe [[Session-Start-Protokoll]].
2. **MCP-Minimalset:** Shibui + defeatbeta + WebSearch — alle anderen deaktivieren
3. **5-Min-Regel:** Vor jeder Pause `/compact` oder `/clear` — nie offene Session ohne Sync verlassen
4. **DEFCON 1 Stopp:** Score <50 → Analyse stoppen, keine weiteren API-Calls (Insider-Modul läuft immer durch)
5. **Sync-Pflicht (4 Dateien):** log.md + CORE-MEMORY + Faktortabelle + STATE.md nach jeder Analyse aktualisieren (§18 INSTRUKTIONEN)

## Backlinks
- [[Context-Hygiene]] — Umsetzung der Token-Mechanik
- [[CLAUDE-md-Konstitution]] — Konfiguration der Mechanismen
- [[Context-Hygiene-Code]] — Claude Code-spezifische Optimierungen
