---
status: accepted
date: 2026-06-06
---

# Referenz-Korpus-Index: Live-State niemals indexieren — Schutz durch Exklusion, nicht durch Frische

## Kontext & Entscheidung

Für besseres Recall (Ziel C) und ein späteres `/compact`-Fenster (Ziel B) bauen wir einen **Referenz-Korpus-Index** über context-mode `ctx_index`/`ctx_search` auf große, textlastige Korpora (`…/synthesis/Wissenschaftliche-Fundierung-DEFCON.md`, Vault-Synthesis-Seiten, Earnings-Rohtext-Ordner). Token-Ersparnis (Ziel A) ist mit empirisch ~9,8 KB/Tag nebensächlich und allein kein Adoptions-Grund.

Wir haben entschieden: **Inhalte mit Live-State-Semantik (Scores, Faktortabelle, DEFCON-Status, FLAGs) kommen niemals in den Index — egal in welcher Datei sie liegen, auch nicht in Vault-Score-Seiten.** Die Scope-Grenze ist inhalts-typ-basiert (Referenz/Synthesis ja, Live-State nie), nicht ordner-basiert.

Der entscheidende Grund: Die `ctx_search`-Snippets sind **nicht autoritativ**, und kein Frische-Modell ist je perfekt echtzeitig — zwischen einem §18-Sync-Write und dem Re-Index liegt immer ein Fenster. Würde man Live-State indexieren, könnte eine Suche in diesem Fenster einen veralteten Score liefern (z.B. AVGO `53` statt aktuell `56`). Robusten Schutz gegen diese Fehlerklasse bietet **nur die Exklusion**, nicht die Index-Aktualität. Das ist die Memory-Guard-Rail (Routing/INSTRUKTIONEN §17.1) konsequent auf Sub-Datei-Ebene angewandt: Memory/Such-Index ist strikt advisory, nie Override gegen Live-Dateien.

## Considered Options

- **Alles indexieren + aggressiv frisch halten (verworfen):** Würde Live-State einschließen und sich auf Re-Index-Latenz verlassen. Bricht bei der genannten Fenster-Race und kollidiert mit `feedback_correctness_over_runtime`.
- **Gar nicht adoptieren (verworfen):** Lässt den Recall-Mehrwert über Referenz-Korpora liegen.
- **Exklusion von Live-State + Re-Index am Schreib-Punkt + Stale-Flag-Sicherheitsnetz (gewählt).**

## Consequences

- Live-State-Recall bleibt ausschließlich Sache der SSoT-Live-Dateien (`PORTFOLIO.md` etc.) und der Routing-Table — daran ändert der Index nichts.
- Frische-Modell für den indexierten Referenz-Content: Re-Index an natürlichen Schreib-Punkten (Wiki-Ingest-Workflow für Synthesis, Earnings-Workflow §19.1 für neue Earnings-Dokumente), kein Cron, keine §18-Kopplung. Ein als *stale* geflaggter Treffer ist das Signal „gegen Quelle gegenkontrollieren" (fail-safe).
- Künftige Versuchung „Index ist frisch genug, Scores reinnehmen" ist durch dieses ADR explizit ausgeschlossen.
