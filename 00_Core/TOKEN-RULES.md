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

## Skill-spezifische Ergänzungen

Skill-interne Token-Regeln (Workflow-Details in DEFCON-Analyse-Kontext) leben in `01_Skills/dynastie-depot/SKILL.md`:
- **§172 `/compact` bei 60%-Threshold** mit Preserve/Discard-Spec + „Nach 3-4 Compacts: Summary → `/clear` → neu"
- **§171 MCP-Aktivierung nach Arbeitsbereich** (Analyse: Shibui+defeatbeta+WebSearch / Vault: filesystem / Chat: `/mcp disable` nicht benötigter Server)
- **§170 Snapshot-First-Flow:** Faktortabelle → Trigger? → Delta (Shibui nur für Delta seit `score_datum`)
- **§795 Token-Budget-Benchmark:** ~12-18k Werktag | ~2-3k Wochenende (pro !Analysiere-Lauf)

Diese Datei bleibt SSoT für **allgemeine** Session-Token-Regeln; skill-spezifische Details bleiben kontextnah im Skill.

**Konvention:** Skill-interne Token-Regeln nur bei Skills mit **einzigartigem Token-Profil** (eigene Compact-Schwellen, Budget-Benchmarks, MCP-Aktivierungs-Pattern). Leichte oder programmatische Skills (z.B. `backtest-ready-forward-verify`, `non-us-fundamentals`, `quick-screener`) nutzen TOKEN-RULES.md als Baseline, ohne eigene Regeln.
