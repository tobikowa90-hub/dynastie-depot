# 🛠️ CODE_GUIDELINES.md — §0 Code-Verhaltens-Regeln (Karpathy)

> **Ausgelagert aus `INSTRUKTIONEN.md §0`** (09.06.2026, De-Monolith-Pilot — Token-Effizienz per-Trigger-Load). INSTRUKTIONEN.md behält Stub + Sub-Anchors für Cross-Reference-Erhalt. Diese Datei wird via CLAUDE.md Routing-Table „Code-Edit-Session" geladen — **vor jedem Code-/File-Edit zwingend lesen + befolgen.**
> Zurück: [`INSTRUKTIONEN.md`](INSTRUKTIONEN.md) | Konstitution: [`../CLAUDE.md`](../CLAUDE.md)

---

## §0. Code-Verhaltens-Regeln (Präambel)

> Diese Regeln gelten universell für alle Code- und File-Edit-Operationen
> (insbesondere durch Claude Code). Sie sind **nicht** auf Markdown-Sync,
> Wiki-Operationen oder reine Lese-Vorgänge anzuwenden.
>
> Quelle: Adaptation der Karpathy-Beobachtungen zu LLM-Coding-Failure-Modes.
> Beispiel-Diffs (Python): https://github.com/forrestchang/andrej-karpathy-skills/blob/main/EXAMPLES.md
>
> **Upstream-Watch (Plugin `andrej-karpathy-skills:karpathy-guidelines`, gepinnt v1.0.0, installiert 2026-05-16):** §0 ist die kanonische SSoT und funktionale **Obermenge** des Plugins — §0.1–§0.4 sind eine enge deutschsprachige Adaption der 4 Plugin-Regeln; §0.5/§0.6 + Bezugs-Tabelle + Konflikt-Auflösung + Sync/Wiki-Carve-out = projekt-spezifisch. Das Plugin-Skill ist **advisory, nie Override gegen §0** (analog Memory-Guard-Rail §17.1). Bei Plugin-Versions-Bump: §0.1–§0.4 gegen neuen Plugin-Wortlaut diff-prüfen (Freshness-Gate); §0-Wortlaut bleibt maßgeblich, Divergenz nur via bewussten §0-Edit auflösen, nicht durch stilles Plugin-Folgen.
>
> **Tradeoff:** Diese Regeln biasen zu Vorsicht über Geschwindigkeit. Bei
> trivialen Edits (Tippfehler, ein-Zeilen-Konstanten) Urteil walten lassen.

### §0.1 Think Before Coding
- Annahmen explizit machen, nicht still raten
- Bei mehreren plausiblen Interpretationen: Rückfrage statt Auswahl
- Bei einfacherer Alternative: aktiv pushen, nicht der ersten Idee folgen
- Bei Konfusion: stoppen und benennen, was unklar ist

### §0.2 Simplicity First (Anti-Overengineering)
- Minimum-Code, der das Problem löst — nichts Spekulatives
- Keine Abstraktionen für Single-Use-Code
- Keine "Flexibilität" oder "Konfigurierbarkeit", die nicht angefordert wurde
- Keine Error-Handler für unmögliche Szenarien
- Test: Würde ein Senior-Engineer sagen "das ist überkomplex"? → vereinfachen

### §0.3 Surgical Changes
- Nur anfassen, was angefasst werden muss
- Kein Drive-by-Refactoring benachbarter Code-/Kommentar-/Format-Bereiche
- Bestehenden Stil matchen, auch wenn man es anders machen würde
- Bei aufgefallenem Dead-Code: erwähnen, nicht selbst löschen
- **Orphans:** Imports/Variablen/Funktionen, die *deine* Änderung verwaist hat → entfernen. Pre-existing Dead-Code → erwähnen, nicht löschen.
- Test: Jede geänderte Zeile traceable zur User-Anfrage? Wenn nein → zurücknehmen

### §0.4 Goal-Driven Execution

| Statt... | ... in verifizierbares Ziel transformieren |
|---|---|
| "Add validation" | Test für invalid inputs schreiben, dann grün machen |
| "Fix bug" | Test schreiben, der Bug reproduziert, dann grün machen |
| "Refactor X" | Tests vor und nach Refactor grün |

- Erfolgs-Kriterien vor Implementierung definieren
- Bei Bug-Fixes: erst Test schreiben, der Bug reproduziert
- Bei Refactor: Tests vor und nach grün
- Multi-Step-Tasks: kurzer Plan mit `verify:`-Kriterien pro Schritt
  (Format konsistent zu `docs/superpowers/plans/`)

### §0.5 Pre-Refactor-Caller-Scan
- Vor Änderung an einer Funktion/Klasse/Tool-Schnittstelle/öffentlichen Konstante mit ≥1 externem Aufrufer: `Grep` auf Symbol-Name **codebase-weit vor** Edit
- Ziel: Caller-Surface kennen bevor Signatur/Verhalten kippt — verhindert Edit→Run→Caller-Break→Retry-Spiralen
- Gilt **nicht** für: File-lokale Helpers (private/`_`-prefixed), Markdown-Edits, String-Konstanten ohne Semantik, neue Symbole
- Gilt **explizit für**: Python-Function-Renames, Schema-Field-Renames (`backtest-ready` ScoreRecord-Schema), MCP-Tool-Signatur-Änderungen, xlsx-Cell-Mapping-Refactor, Skill-Trigger-Phrasen
- Test: „Wenn ich diese Signatur breche, finde ich den Bruch sofort durch Test/Lauf?" — wenn nein, erst Caller scannen

### §0.6 Approach-Reset-Schwelle
- Wenn 2 strukturell-identische Versuche an derselben Stelle scheitern (gleiche Fehlermeldung, gleiche Hypothese, gleiches Diff-Pattern): **Stop, kein dritter identischer Versuch**
- Options: (a) Codex-Sparring 1-Pass-Diff-Review (`codex:rescue`), (b) Approach-Wechsel via Plan-Tool, (c) User-Konsultation mit Fakten-Lage
- „Strukturell-identisch" = gleicher Edit-Vektor (selbe File/Funktion/Hypothese), auch wenn Wortlaut variiert
- **Erlaubt:** 3. Versuch wenn (a) neue Fakten dazwischen (z.B. Codex-Befund, neuer Grep-Treffer, User-Korrektur), ODER (b) Approach explizit anders (anderer File, andere Hypothese, andere Layer)
- **Gilt nicht für:** Codex-Sparring-Loops selbst (max 3 Runden per Memory `feedback_codex_sparring_heuristic`), Smoke-Test-Retries (deterministische Setup-Probleme), Network-Retries
- Test: „Würde ich denselben Edit nochmal machen mit derselben Erwartung?" — wenn ja, das ist die Schwelle

### Bezug zu bestehenden Regeln

| Regel | Verhältnis zu §0 |
|---|---|
| §27.5 Migration-Regression-Guard | §0.3 Surgical Changes ist die generalisierte Form — §27.5 ist spezifisch für Migrations-Tasks |
| §29.5 Look-Ahead-Prevention | §0.4 Goal-Driven ist die generalisierte Form — §29.5 ist spezifisch für Backtest-Code |
| §18 Sync-Pflicht | §0 gilt nicht für Sync-Operationen — Sync ist mechanisch, nicht kreativ |
| Memory `feedback_pre_commit_diff_inspection` | §0.5 Pre-Refactor-Caller-Scan ist Pre-Edit-Variante; Memory ist Pre-Commit-Variante (Hunk-Selection vor `git add`) — komplementär |
| Memory `feedback_codex_sparring_heuristic` | §0.6 Approach-Reset-Schwelle ist allgemein (2-Versuche-Stop); Memory ist Codex-spezifisch (3-Runden-Max im Sparring) — §0.6 löst aus, Memory steuert Eskalations-Kadenz |

**Konflikt-Auflösung:** Bei Konflikt zwischen §0 und einem späteren spezifischen § gewinnt der spezifische §. §0 ist Default-Verhalten, kein Override.
