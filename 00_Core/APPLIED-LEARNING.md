---
name: Applied Learning Log
description: Kuratierte Arbeitsprinzipien für Dynasty-Depot-Sessions (Tier 2 des 3-Tier-Lernsystems). Enthält Pflege-Regeln und Versionshistorie.
type: learning-log
updated: 2026-05-07
---

# Applied Learning — Kuratierte Arbeitsprinzipien

> Tier 2 des 3-Tier-Systems (Auto-Memory → Applied Learning → INSTRUKTIONEN.md).
> <15 Wörter pro Bullet. Nur operativ relevante Arbeitsprinzipien — keine Tool-References (→ Auto-Memory) und keine systemischen Regeln (→ INSTRUKTIONEN.md §§).

## Bullets (Stand: 16/20)

> **Proaktive Pflege (seit 18.04.2026):** Bei jedem Monats-Übergang: 5-Min-Scan — Tool-References identifizieren und evakuieren. Verhindert Buildup, billiger als reaktive Überlauf-Sanierung.
>
> **Bridge-Coherence-Erweiterung (seit 02.05.2026, Ruflo-Phase-1.2-1.7-DONE):** Beim Monatsscan auch prüfen, ob ein Bullet bereits als Auto-Memory existiert (gleiches Topic / gleiches Kern-Lehre). Wenn ja → Tier-2-Bullet entfernen. Doppel-Speicherung verzerrt die Bridge-PageRank-Recall-Gewichtung; Tier-2 ist nur SSoT für Prinzipien, die NICHT in Auto-Memory leben.
>
> **Kurator-Regel bei Überlauf (20/20):** Hybrid-Strategie: (1) Tool-References → Auto-Memory; (2) stabile Regeln → neue INSTRUKTIONEN-§; (3) thematisch verwandte Bullets konsolidieren. Ziel: ≤15/20 nach Revision. Archivierung ist kein Weg (toter Code).

- Subagents nur für Code+Tests — Markdown/YAML-Edits direkt editieren (3×Subagent-Overhead unnötig)
- Paper-Ingest ≠ System-Update: Wissenschaft validiert Regeln, erzwingt keine neuen — Redundanz-Check vor jeder Scoring-Erweiterung
- Advisor-Empfehlung nicht ohne neue Evidenz überstimmen — Ästhetik-Argumente zählen nicht als Evidenz
- Parallel-Agents für !Analysiere REJECTED 17.04.: ~270k Token + Screener-Exception-Fehler — Genauigkeit > Wall-Time
- Backfill-Tolerant-Pattern für Cross-Validators: bei fehlenden Rohwerten moat.rating="narrow" → Quality-Trap-Validator deaktiviert, keine Schätzungen nötig
- Cross-Session AI-"Fixes" immer gegen `git diff HEAD` prüfen — Preview-Reads können Truncation fälschlich diagnostizieren
- Option B vor mechanischem FLAG-Trigger: schema-getriggert ≠ strukturell. WC-Noise / Multi-Year-Trend / OpInc-Parallelität prüfen (TMO 18.04. fcf_trend_neg nicht aktiviert)
- Backtest-Validation = 4-Dim-Gate (PBO + AQR-Bench + Half-Life + Seven Sins); Sin #7 n.a. für Long-Only.
- Anti-Hallucination-Guards: nicht nur Gründe, auch alternative Datenpfade/Fallbacks explizit verbieten (v3.0.3-Incident)
- Plan-Self-Review verfehlt Bash/sed/grep-Pipeline-Bugs — externe Review-Instanz (Codex) pflicht vor Execution
- 1:1-Migration-Commit darf keine Meta-Logging-Einträge ergänzen — separater Commit nach Verify-PASS
- Pre-Append-Audit-Klausel: vor erstem Live-Run neuer Pipeline-Version Audit PASS pflicht — kein Append bei FAIL (Provenance-Gate-Pattern, V/MSFT 28.04.)
- Tooling-Bulk-Edit: CR-Pass koppeln — Ruff/Codex sehen Lint, CR surfacet semantische Bestandsbugs (~50/Pass empirisch 07.05.)
- Cloud-Sync-Verify ist Pre-Phase-Pflicht für AgentDB-/Memory-DB-Tools — Path-Hash + DriveFS-Audit via WSL-sqlite3 (Cloud-Sync-Pitfall generalisiert aus Ruflo Phase 1.2)
- Bridge-/Substrate-Layer DONE-Verdict erfordert end-to-end Search-Verify mit known-query (similarity ≥ Schwelle), NICHT Storage+Reporter-Verify allein (Ruflo Mini-Welle #57 — 7 Wochen „Bridge connected"-Illusion ohne semantischen Recall-Test)
- Plugin-/Substrate-Layer ohne konkreten Workflow-Use-Case = Über-Engineering — Nutzen empirisch belegen vor Engineering-Welle (Ruflo-Sunset-Lesson 13.05.; analog quick-screener-Refresh-Verzicht 09.05.)

## Promotion-Logik

Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).

## Historie

| Version | Datum | Änderung |
|---------|-------|----------|
| v1.0 | 17.04.2026 | 19 Bullets gemischt. |
| v2.0 | 18.04.2026 | Evakuierung: 6 Tool-Refs → Auto-Memory, 4 systemische Regeln → INSTRUKTIONEN §27, auf **9 Kern-Arbeitsprinzipien** reduziert. Neues +1 (Option B FLAG-Entscheidung). |
| v2.1 | 18.04.2026 | Bullet „Scoring-Version-Bump re-verify" → INSTRUKTIONEN §28.2 promoted. |
| v2.2 | 20.04.2026 | +1 (Spec-§-Drift-Handling, aus Track-5-Plan-Writing). |
| v2.3 | 20.04.2026 Nacht-Spät | +1 (Anti-Hallucination-Datenpfad-Vollständigkeit, aus v3.0.3-Incident). |
| v2.4 | 21.04.2026 | +1 (Exhaustive-Drift-Check, aus Pre-Provenance-Plan-Compat-Check 12/27 silent v3.7-Threshold-Drift). |
| v2.5 | 24.04.2026 | +2 (Plan-Self-Review-Blindspot, Migrations-Invariante-vs-Meta-Logging — beide aus 3-fach-Review CLAUDE.md-Routing-Refactor, nach Tier-1-Deploy). Stand: **14/20**. |
| v2.6 | 02.05.2026 | **Bridge-Coherence-Scan** post-Ruflo-Phase-1.2-1.7-DONE: −3 Bullets entfernt (Info-Loss-Aversion, Spec-§-Drift, Exhaustive-Drift-Check — alle als Auto-Memory bereits evakuiert; Doppel-Speicherung verzerrte Bridge-PageRank-Recall). +1 neu (Pre-Append-Audit-Klausel aus Provenance-Gate-Plan v3.1 + V/MSFT-Pre-Earnings-Klausel 28.04.). +1 Pflege-Regel-Erweiterung (Bridge-Coherence beim Monatsscan). Stand: **12/20**. |
| v2.7 | 07.05.2026 | +1 (Tooling-Bulk-Edit + CR-Pass koppeln) — empirische Evidenz aus Ruff-Cleanup Cluster A+B: 96+ pre-existing CR-Findings (3 critical / 14 major union) durch zwei sukzessive `coderabbit review -t uncommitted --dir 03_Tools/`-Pässe surfacet, die Ruff allein nicht sieht (semantische Algo-Drift, hardcoded-Annahmen, missing cross-validators, Test-Fixture-Quality). Reaktiver Konsolidierungs-Backlog (PIPELINE #46 + #47) wäre durch periodische CR-Reviews während Authoring größtenteils vermieden worden. Stand: **13/20**. |
| v2.8 | 13.05.2026 | +3 generelle Engineering-Hygiene-Bullets aus Ruflo-Sunset. Stand: **16/20**. |
