---
name: Applied Learning Log
description: Kuratierte Arbeitsprinzipien für Dynasty-Depot-Sessions (Tier 2 des 3-Tier-Lernsystems). Enthält Pflege-Regeln und Versionshistorie.
type: learning-log
updated: 2026-04-24
---

# Applied Learning — Kuratierte Arbeitsprinzipien

> Tier 2 des 3-Tier-Systems (Auto-Memory → Applied Learning → INSTRUKTIONEN.md).
> <15 Wörter pro Bullet. Nur operativ relevante Arbeitsprinzipien — keine Tool-References (→ Auto-Memory) und keine systemischen Regeln (→ INSTRUKTIONEN.md §§).

## Bullets (Stand: 14/20)

> **Proaktive Pflege (seit 18.04.2026):** Bei jedem Monats-Übergang: 5-Min-Scan — Tool-References identifizieren und evakuieren. Verhindert Buildup, billiger als reaktive Überlauf-Sanierung.
>
> **Kurator-Regel bei Überlauf (20/20):** Hybrid-Strategie: (1) Tool-References → Auto-Memory; (2) stabile Regeln → neue INSTRUKTIONEN-§; (3) thematisch verwandte Bullets konsolidieren. Ziel: ≤15/20 nach Revision. Archivierung ist kein Weg (toter Code).

- Subagents nur für Code+Tests — Markdown/YAML-Edits direkt editieren (3×Subagent-Overhead unnötig)
- Paper-Ingest ≠ System-Update: Wissenschaft validiert Regeln, erzwingt keine neuen — Redundanz-Check vor jeder Scoring-Erweiterung
- Informationsverlust-Aversion > Ästhetik: bei Delete-vs-Keep Default = erhalten + Zeitstand-Banner
- Advisor-Empfehlung nicht ohne neue Evidenz überstimmen — Ästhetik-Argumente zählen nicht als Evidenz
- Parallel-Agents für !Analysiere REJECTED 17.04.: ~270k Token + Screener-Exception-Fehler — Genauigkeit > Wall-Time
- Backfill-Tolerant-Pattern für Cross-Validators: bei fehlenden Rohwerten moat.rating="narrow" → Quality-Trap-Validator deaktiviert, keine Schätzungen nötig
- Cross-Session AI-"Fixes" immer gegen `git diff HEAD` prüfen — Preview-Reads können Truncation fälschlich diagnostizieren
- Option B vor mechanischem FLAG-Trigger: schema-getriggert ≠ strukturell. WC-Noise / Multi-Year-Trend / OpInc-Parallelität prüfen (TMO 18.04. fcf_trend_neg nicht aktiviert)
- Backtest-Validation = 4-Dim-Gate (PBO + AQR-Bench + Half-Life + Seven Sins); Sin #7 n.a. für Long-Only.
- Spec-§-Drift in Plan: Header-Notice mit Ist-§-Mapping + Codex-Attestierung, Spec frozen lassen — nicht Silent-Fix, nicht Spec-PR-Blocker
- Anti-Hallucination-Guards: nicht nur Gründe, auch alternative Datenpfade/Fallbacks explizit verbieten (v3.0.3-Incident)
- „Drift-Check" = exhaustive Schema-Validation aller Records, nicht Spot-Check (12/27 silent defcon-Drift entdeckt 21.04. via Pre-Check)
- Plan-Self-Review verfehlt Bash/sed/grep-Pipeline-Bugs — externe Review-Instanz (Codex) pflicht vor Execution
- 1:1-Migration-Commit darf keine Meta-Logging-Einträge ergänzen — separater Commit nach Verify-PASS

## Promotion-Logik

Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).

## Historie

v1.0 (17.04.2026) 19 Bullets gemischt. v2.0 (18.04.2026) Evakuierung: 6 Tool-Refs → Auto-Memory, 4 systemische Regeln → INSTRUKTIONEN §27, auf **9 Kern-Arbeitsprinzipien** reduziert. Neues +1 (Option B FLAG-Entscheidung). v2.1 (18.04.2026) Bullet „Scoring-Version-Bump re-verify" → INSTRUKTIONEN §28.2 promoted. v2.2 (20.04.2026) +1 (Spec-§-Drift-Handling, aus Track-5-Plan-Writing). v2.3 (20.04.2026 Nacht-Spät) +1 (Anti-Hallucination-Datenpfad-Vollständigkeit, aus v3.0.3-Incident). v2.4 (21.04.2026) +1 (Exhaustive-Drift-Check, aus Pre-Provenance-Plan-Compat-Check 12/27 silent v3.7-Threshold-Drift). v2.5 (24.04.2026 nach Tier-1-Deploy) +2 (Plan-Self-Review-Blindspot, Migrations-Invariante-vs-Meta-Logging — beide aus 3-fach-Review CLAUDE.md-Routing-Refactor). Stand: **14/20**.
