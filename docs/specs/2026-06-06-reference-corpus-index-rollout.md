# Spec: Referenz-Korpus-Index (context-mode) — Rollout

**Status:** Spec fertig (Grill-Runde 2026-06-06). Normativer §18-Einbau **PENDING** — separate Session.
**Herkunft:** Grill-with-docs-Runde 2026-06-06. Tiefenbegründung: `docs/adr/0001-no-live-state-in-reference-index.md`.

## Problem / Ziel

context-mode wird bisher nur in Teilen genutzt (passiver Auto-Capture + Ad-hoc-PDF/Großtext). Empirie: ~9,8 KB/Tag Ersparnis (Token-Spar-Case allein trägt nicht). Der ungenutzte Hebel ist **`ctx_index`/`ctx_search` als persistenter Referenz-Korpus-Index** für **Recall** (Ziel C) + späteres `/compact`-Fenster (Ziel B). Token-Ersparnis (A) ist nebensächlich.

## Entscheidungen (Grill-Ergebnis)

| Ast | Entscheidung |
|---|---|
| **Ziel** | C (Recall) + B (Compact-Fenster); A nebensächlich |
| **Scope** | Inhalts-typ-basiert. **IN:** `…/synthesis/Wissenschaftliche-Fundierung-DEFCON.md`, Vault-**Synthesis**-Seiten, Earnings-Rohtext-Ordner (pro Aktie). **HART RAUS:** Live-State (Scores, Faktortabelle, DEFCON-Status, FLAGs) — egal in welcher Datei, auch Vault-Score-Seiten. |
| **Frische** | Re-Index am Schreib-Punkt (Wiki-Ingest-Workflow für Synthesis · Earnings-Workflow §19.1 für neue Earnings-Docs · Wiss-Fundierung ad-hoc). Kein Cron, keine §18-Kopplung. Stale-Flag (Content-Hash) = fail-safe Signal „gegen Quelle gegenkontrollieren". |
| **Invocation** | Pull-basiert/explorativ (breite Lookups über viel Text). Scoring-Pfad (`!Analysiere`) bleibt **autoritativer Vollread** — kein Snippet-Ersatz für Regel-/Begründungs-Autorität (gleiche Logik wie `INSTRUKTIONEN.md` raushalten). |
| **Schutzprinzip** | Live-State-Schutz durch **Exklusion, nicht Frische** (ADR-0001). Memory-Guard-Rail (§17.1) eine Ebene tiefer. |

## Rollout-Checklist (separate §18-Session)

Discovery braucht *bindend* (normativ) **und** *auffindbar* (advisory):

1. **`00_Core/TOKEN-RULES.md`** — neuer Bullet „Referenz-Korpus-Index" (Recall-/Effizienz-Betriebsregel: was rein/raus, pull-basiert, Live-State nie). *Bindend.*
2. **`CLAUDE.md` Routing-Table, Zeile „Wiki-Ops"** — Notiz: Reference-Lookups → `ctx_search` (explorativ); Scoring-Pfad liest autoritativ voll. *Bindend.*
3. **`00_Core/INSTRUKTIONEN.md §17.1`** (Memory-Guard-Rail) — optionales Ein-Zeiler-Korollar „Live-State nie in Such-Index" mit Verweis auf ADR-0001. *Bindend.*
4. **Tier-1-Memory** `feedback_reference_corpus_index_pattern.md` (+ MEMORY.md-Index) — *auffindbar*, zeigt auf Anker + ADR. **→ bereits 2026-06-06 geschrieben.**
5. **ADR-0001** — Tiefenbegründung. **→ bereits geschrieben.**
6. **§18-Sync:** `SYSTEM.md` (System-Zustand-Change) + `log.md`, alles in **einem** Commit.
7. **Vor Commit:** Codex-Sparring-Pass über die Anker-Diffs (`feedback_review_via_codex_not_advisor`).

## Nicht-Ziele / bewusst draußen

- Kein Auto-Verdrahten in den Scoring-Pfad (Korrektheit > Runtime).
- Kein periodischer Cron-Re-Index.
- Kein Index von Live-State / SSoT-Files.
- Kein eager-Index von `05_Archiv/` — erst bei realem Abfrage-Bedarf (Use-Case-getrieben).
- Pocock `improve-codebase-architecture` ist hier **nicht** anwendbar (zielt auf Code/`03_Tools`, nicht den Markdown-Referenz-Layer).
