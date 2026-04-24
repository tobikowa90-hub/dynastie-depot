---
name: Token-Effizienz Regeln
description: Operative Regeln zur Token-Effizienz für Dynasty-Depot-Sessions. Accessibility-Modell (kein Enforcement).
type: ruleset
scope: projekt-weit referenzierbar
enforcement: none (Accessibility-Modell)
updated: 2026-04-24
---

# Token-Effizienz — Operative Regeln

> **Accessibility-Hinweis (explizit, Entscheidung 2026-04-24):**
> Diese Regeln liegen vor und sind via Pointer aus CLAUDE.md erreichbar. Es existiert **kein Enforcement-Mechanismus** (kein Hook, kein Skill-Check, kein Audit). Anwendung erfolgt durch bewusste Entscheidung der jeweiligen Session — nicht durch automatische Kontrolle.

## Regeln

- **Snapshot-First:** STATE.md + Faktortabelle vor API — spart 3-5 Tool-Calls
- **Sync-Pflicht (alle sechs):** log.md + CORE-MEMORY.md + Faktortabelle + STATE.md + score_history.jsonl + flag_events.jsonl
- **Pause-Regel:** >5 Min → /compact (Preserve: Score/Tabelle/Urteil/FLAGs) oder /clear
- **DEFCON 1 Stopp:** Score <50 → Analyse stoppen (Insider-Modul läuft durch)
- **MCP:** Tool Search lädt lazy. Manuell deaktivieren nur bei Vault-Only-Sessions.
- **Modell:** Sonnet 4.6 default; `/model opus` für !Analysiere, Multi-Step-Refactors, strategische Entscheidungen.
