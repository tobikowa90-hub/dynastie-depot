---
name: Applied Learning Log
description: Kuratierte Arbeitsprinzipien für Dynasty-Depot-Sessions (Tier 2 des 3-Tier-Lernsystems). Enthält Pflege-Regeln und Versionshistorie.
type: learning-log
updated: 2026-08-26
---

# Applied Learning — Kuratierte Arbeitsprinzipien

> Tier 2 des 3-Tier-Systems (Auto-Memory → Applied Learning → INSTRUKTIONEN.md).
> <15 Wörter pro Bullet. Nur operativ relevante Arbeitsprinzipien — keine Tool-References (→ Auto-Memory) und keine systemischen Regeln (→ INSTRUKTIONEN.md §§).

## Bullets (Stand: ⚠️ 21/20 — Kurator-Regel fällig)

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
- Cloud-Sync-Verify ist Pre-Phase-Pflicht für AgentDB-/Memory-DB-Tools — Path-Hash + DriveFS-Audit via WSL-sqlite3 (Cloud-Sync-Pitfall bei OneDrive/Google-Drive-Vaults; Präzedenz 02.05.2026)
- Bridge-/Substrate-Layer DONE-Verdict erfordert end-to-end Search-Verify mit known-query (similarity ≥ Schwelle), NICHT Storage+Reporter-Verify allein (Präzedenz: 7-Wochen-„Bridge connected"-Illusion ohne semantischen Recall-Test)
- Plugin-/Substrate-Layer ohne konkreten Workflow-Use-Case = Über-Engineering — Nutzen empirisch belegen vor Engineering-Welle (Sunset-Präzedenz 13.05.; analog quick-screener-Refresh-Verzicht 09.05.)
- Deferred-Sub-Scope: vor Execution prüfen ob Substrate-fail-close-Gates ihn unabhängig committbar machen — sonst Kosten umsonst
- Zustand (API-abfragbar) nie handpflegen, Urteil (Score/FLAG) bleibt SSoT — Regelbrüche entstehen an der Naht
- Entdopplung erst nach Vollständigkeits-Check aller Quellen — sonst zementiert der Umbau den Datenfehler
- Vor neuer Regel bestehendes Regelwerk nach demselben Fall durchsuchen — stille Übersteuerung erzeugt Drift
- Review-Befund: ganze Datei auf gleichartige Abhängigkeiten prüfen, nicht nur die gemeldete Zeile

## Promotion-Logik

Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).

## Historie

| Version | Datum | Änderung |
|---------|-------|----------|
| v2.6 | 02.05.2026 | **Bridge-Coherence-Scan** post-Ruflo-Phase-1.2-1.7-DONE: −3 Bullets entfernt (Doppel-Speicherung mit Auto-Memory verzerrte Bridge-PageRank-Recall). +1 neu (Pre-Append-Audit-Klausel). +1 Pflege-Regel-Erweiterung. Stand: **12/20**. |
| v2.7 | 07.05.2026 | +1 (Tooling-Bulk-Edit + CR-Pass koppeln) — empirische Evidenz aus Ruff-Cleanup. Stand: **13/20**. |
| v2.8 | 13.05.2026 | +3 generelle Engineering-Hygiene-Bullets aus Ruflo-Sunset. Stand: **16/20**. |
| v2.9 | 18.05.2026 | +1 (Deferred-Sub-Scope-Committbarkeit vor Execution prüfen). Tier-2-only (Bridge-Coherence). Stand: **17/20**. |
| v3.0 | 26.08.2026 | +1 (Zustand vs. Urteil trennen) — Scalable-Agentic-Investing-Anbindung. Empirie: KYCCF-xlsx-Zeile trug wochenlang Veeva-Wert; 135 €/Mt liefen 2,5 Monate in geflaggte Titel, weil kein Markdown-File einen neu angelegten Sparplan bemerken kann. Detail → `02_Analysen/2026-08-26_Depot-Reconciliation.md` §F. Stand: **18/20**. |
| v3.1 | 26.08.2026 | +3 aus der Architektur-Spec-Session (Entdopplungs-Vorbedingung · Regelwerk-Kollisionsprüfung · Datei-weite Befundprüfung). Empirie: drei FLAG-Quellen paarweise widersprüchlich; „freigesetzt → Block-Untergewicht" hätte `substitute_activation_global` still übersteuert; `check_freshness` und `parse_state_row` stehen in derselben Datei, eine Sparring-Runde sah nur eines. Detail → `03_Tools/depot-architecture-spec.md` §4.2/§4.4/§7.4. Stand: **⚠️ 21/20 — Kappe gerissen, Kurator-Regel fällig.** |

> **Offener Kurations-Auftrag (26.08.2026):** 21/20, Ziel laut Kurator-Regel ≤15. Bewusst nichts eigenmächtig gelöscht. Zwei Bullets sind inhaltlich überholt und wären die ersten Kandidaten: *„Advisor-Empfehlung nicht ohne neue Evidenz überstimmen"* (advisor ist projektweit durch Codex ersetzt, Memory `feedback_review_via_codex_not_advisor`) und *„Cloud-Sync-Verify ist Pre-Phase-Pflicht"* (kein aktiver Cloud-Sync, Memory `reference_no_cloud_sync_onedrive_inactive`). Entscheidung beim Owner.

> Versionen v1.0-v2.5 (17.-24.04.2026) → git log (Datei-Historie). Pre-v2.6 im 00_Core Slim-Refactor 23.05.2026 entfernt (Lean-Pflicht-Lese-Pfad-Disziplin, Memory `feedback_core_folder_lean_discipline`). Promotion-Events alle in git log + Auto-Memory abgedeckt.
