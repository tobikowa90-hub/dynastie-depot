---
name: Token-Effizienz Operator-Detail
description: Operator-Action-Cues für Dynasty-Depot-Sessions (/compact, /model, /mcp, /clear). Claude-Action-Disziplin liegt inline in CLAUDE.md §Verhalten (Snapshot-First / DEFCON-1-Stopp / /compact-Cue).
type: ruleset
scope: operator-disziplin + skill-§-cross-refs
updated: 2026-05-26
---

# Token-Effizienz — Operator-Detail

> **Architektur-Hinweis (Refactor 2026-05-26):** Claude-Action-Disziplin (Snapshot-First / DEFCON-1-Stopp / /compact-Cue / Skills-lazy-load / §18-Sync) ist inline in `CLAUDE.md §Verhalten` verankert — wird bei jedem Session-Start automatisch geladen. Diese File ist **Operator-Lookup** für Slash-Commands + Skill-§-Cross-Refs (on-demand via Routing-Table-Pointer).

## Verweise
- [CLAUDE.md §Verhalten](../CLAUDE.md) — Claude-Action-Bullets (SSoT)
- [INSTRUKTIONEN.md §18](INSTRUKTIONEN.md#18-sync-pflicht--trigger-basiertes-file-set-mapping-v2-2026-04-24-00_core-refactor) — Sync-Pflicht-Mapping
- [APPLIED-LEARNING.md](APPLIED-LEARNING.md) — Tier-2-Learning-Log

## Operator-Cues (Slash-Commands)

- **`/compact` bei ~60% Kontext-Voll oder >5min Pause** — Preserve: Score / Tabelle / Urteil / FLAGs. Detail-Spec → `01_Skills/dynastie-depot/SKILL.md` §172. **Nach 3-4 Compacts:** Summary erstellen → `/clear` → neue Session.
- **`/model`** — Sonnet 4.6 default; `opus` für `!Analysiere`, Multi-Step-Refactors, strategische Entscheidungen.
- **MCP-Pause** — Tool Search lädt lazy. Manuell `/mcp disable` nur für ungenutzte Server bei Vault-Only-Sessions (Shibui + defeatbeta + WebSearch bleiben aktiv bei Analyse-Sessions).

## Skill-spezifische Ergänzungen

Workflow-Details bei einzigartigem Token-Profil bleiben kontextnah im jeweiligen Skill:

- `01_Skills/dynastie-depot/SKILL.md`:
  - **§170** Snapshot-First-Flow (Faktortabelle → Trigger? → Delta-Pull nur seit `score_datum`)
  - **§171** MCP-Aktivierung nach Arbeitsbereich (Analyse: Shibui + defeatbeta + WebSearch / Vault: filesystem / Chat: ungenutzte Server `/mcp disable`)
  - **§172** `/compact`-Threshold mit Preserve/Discard-Spec + 3-4-Compact-Reset-Rule
  - **§795** Token-Budget-Benchmark (~12-18k Werktag / ~2-3k Wochenende pro `!Analysiere`-Lauf)

**Konvention:** Skill-interne Token-Regeln nur bei Skills mit **einzigartigem Token-Profil** (eigene Compact-Schwellen, Budget-Benchmarks, MCP-Aktivierungs-Pattern). Leichte/programmatische Skills (`backtest-ready-forward-verify`, `non-us-fundamentals`, `quick-screener`) nutzen diese File als Baseline ohne eigene Regeln.

## Accessibility-Modell (unverändert seit 2026-04-24)

Diese File wird **NICHT auto-geladen** — sie ist Routing-Table-on-demand-File. Claude-Action-Bullets sind inline in CLAUDE.md verankert (Refactor 2026-05-26). Operator nutzt diese File als Lookup für Slash-Commands + Skill-§-Cross-Refs. Kein Enforcement-Mechanismus (kein Hook, kein Skill-Check, kein Audit).
