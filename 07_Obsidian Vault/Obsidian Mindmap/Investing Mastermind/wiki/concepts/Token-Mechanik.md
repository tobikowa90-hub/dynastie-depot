---
title: "Token-Mechanik"
type: concept
tags: [system, token-effizienz, claude, session-management]
sources: []
related:
  - "[[Context-Hygiene]]"
  - "[[CLAUDE-md-Konstitution]]"
  - "[[Context-Hygiene-Code]]"
  - "[[Update-Klassen-DEFCON]]"
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

1. **Pflicht-Lektüre zuerst:** `00_Core/STATE.md` (Hub, ~40 Z) + `00_Core/PORTFOLIO.md` (Live-State, default-load seit Tier-2-Refactor 25.04.2026). Andere 00_Core-Dateien on-demand via Routing-Table in CLAUDE.md — siehe [[Session-Start-Protokoll]].
2. **MCP-Minimalset:** Shibui + defeatbeta + WebSearch — alle anderen deaktivieren
3. **5-Min-Regel:** Vor jeder Pause `/compact` oder `/clear` — nie offene Session ohne Sync verlassen
4. **DEFCON 1 Stopp:** Score <50 → Analyse stoppen, keine weiteren API-Calls (Insider-Modul läuft immer durch)
5. **Sync-Pflicht (§18 v2.1 Trigger-basiertes Mapping):** Score/FLAG/Sparraten-Change-Set = log.md + CORE-MEMORY.md + Faktortabelle.md + PORTFOLIO.md + score_history.jsonl + config.yaml (+ conditional flag_events.jsonl). Multi-Event-Aktionen = Union der File-Sets. Details: [INSTRUKTIONEN §18 v2.1](../../../../00_Core/INSTRUKTIONEN.md).

## Backlinks
- [[Context-Hygiene]] — Umsetzung der Token-Mechanik
- [[CLAUDE-md-Konstitution]] — Konfiguration der Mechanismen
- [[Context-Hygiene-Code]] — Claude Code-spezifische Optimierungen
