---
title: CLAUDE.md Routing-Refactor — Tier 1 (Projekt-Eigene Session-Init-Reduktion)
date: 2026-04-24
status: draft
scope: dynasty-depot project-local
authors: Tobias Kowalski + Claude Opus 4.7
predecessor-spec: none
related:
  - docs/superpowers/specs/2026-04-21-system-audit-tool-design.md
  - 00_Core/INSTRUKTIONEN.md (§27, §28)
---

# CLAUDE.md Routing-Refactor — Tier 1

## Kontext

**Problem.** CLAUDE.md ist auf ~150 Zeilen gewachsen. Bei jedem Session-Start wird sie komplett gelesen, weil sie als Pflicht-Read im Harness konfiguriert ist. Die Datei mischt drei Rollen:

1. **Routing-Direktiven** (was bei welchem Trigger lesen)
2. **Statische Regeln** (Token-Effizienz, Verhalten, Sync-Pflicht)
3. **Lessons-Sammlung** (Applied Learning, 12 Bullets + Pflege-Regeln + Historie)

Die Lessons-Sammlung wächst monoton (12/20, Wachstumstrend ~1 Bullet/Woche). Token-Effizienz-Regeln sind ein Ruleset, das nicht bei jedem Session-Start im Vordergrund stehen muss. Das Resultat: jede Session zahlt unnötigen Token-Aufwand für Inhalte, die nur kontextabhängig relevant werden.

**Pain-Quelle Kategorie A vs B (Advisor-Klärung 2026-04-24):**
- **Kategorie A** = Harness-Auto-Reads (Skill-Listings, Tool-Schemas, MCP-Instructions, System-Reminders) — **out-of-scope** dieser Spec.
- **Kategorie B** = projekt-eigene Pflicht-Reads (CLAUDE.md, ~308 Zeilen mit Sub-Reads bei Default-Triggern) — **scope dieser Spec**.

Tier 1 dieses Refactors zielt **ausschließlich** auf Kategorie B.

**Ziel.** CLAUDE.md von ~150 auf ~70 Zeilen reduzieren, indem (a) Inhalte mit kontextabhängiger Relevanz in dedizierte Files ausgelagert werden, (b) eine Routing-Table die On-Demand-Lektüre-Logik systematisiert, (c) Tier-3-Lernsystem-Inhalte in eine eigene Datei wandern.

## Out-of-Scope

- **Kategorie A (Harness-Auto-Reads):** Skill-Listings + Tool-Deferred + MCP-Instructions + System-Reminders. Nicht von projekt-lokaler Konfiguration adressierbar.
- **Tier 2 STATE.md 3-Split (Variante B Hub):** STATE.md bleibt unverändert. Eigene Spec in separater Session.
- **Tier 2b CORE-MEMORY-Subkategorisierung:** Kalendarische Riesen-Liste → Subkategorien. Eigene Spec, nicht Tier 1.
- **Tier 3 `vault_backlinks`-Check-Erweiterung:** Bereits Backlog-Punkt STATE.md Z. 120. Nicht Tier 1.
- **Strukturelle Reorganisation außer den 2 neuen Files:** Keine Umbenennungen, keine Datei-Verschiebungen, keine Folder-Refactors.
- **Cross-Link-Updates in Vault-Notes:** Empfohlen (siehe Pre-Move-Grep), aber nicht Spec-Pflicht. Separater Cleanup-Sweep.

## Verbindliche Entscheidungen (User, 2026-04-24)

- **Entscheidung A = ja:** Routing-Table **ersetzt** die existierende On-Demand-Lektüre-Liste vollständig. Keine Duplizierung, vermeidet Drift.
- **Entscheidung B = c:** TOKEN-RULES.md ist **Accessibility-Modell**. Regeln liegen vor und sind via Pointer aus CLAUDE.md erreichbar. **Kein Enforcement-Mechanismus** (kein Hook, kein Skill-Check, kein Audit). Anwendung erfolgt durch bewusste Entscheidung der jeweiligen Session.
- **Match-Regel = Hybrid (c):** Exakte Trigger strikt. Eine Soft-Match-Ausnahme — bare Ticker-Symbol ohne Trigger-Wort wird als `!QuickCheck <Ticker>` behandelt. Bei Mehrfach-Match: Union der Lies-Spalten.
- **Trigger-Inventar = 9 Zeilen (Variante a):** Nur trigger-orientierte Zeilen. Latente-Intention-Zeilen (Score-Detail, Audit-Log-Bezug, Pre-15.04.-Chronik, Session-Fortsetzung) werden vom Default-Verhalten oder vom Hybrid-Soft-Match abgedeckt.
- **`## Kontinuierliches Lernen` = Variante (A):** Nur 3-Tier-Tabelle + Pointer in CLAUDE.md. Promotion-Logik und alle Bullets nach APPLIED-LEARNING.md.
- **`## Token-Effizienz (operativ)` = Variante (X):** Section komplett raus aus CLAUDE.md. Nur Pointer-Zeile in `## Pointer (Ausgelagertes)` am Fuß. Konsequent zur Accessibility-Entscheidung B=c.
- **Beide neuen Files:** projekt-lokal (`00_Core/`), nicht User-Level.

## Architektur

### CLAUDE.md (Ziel-Gliederung, ~70 Zeilen)

```
# SESSION-INITIALISIERUNG
  ## Pflicht-Read
  ## Verhalten                       (Sync-Pflicht, CORE-MEMORY live, briefing-sync §25, remote-Control)
  ## Kontinuierliches Lernen         (3-Tier-Tabelle + Pointer; Bullets+Historie ausgelagert)

## Projektstruktur                   (UNVERÄNDERT)

## Routing-Table                     (NEU — ersetzt On-Demand-Lektüre-Liste)

## Wiki-Modus                        (UNVERÄNDERT — Trigger + Pointer zu WIKI-SCHEMA.md)

## Pointer (Ausgelagertes)           (NEU — Tabelle: Datei | Zweck)
```

**Begründung der Top-Level-Reihenfolge:**
- `## Verhalten` und `## Kontinuierliches Lernen` sind Wenn-Dann-Regeln, die *bei Session-Start* triggern → gehören unter Session-Initialisierung, nicht als eigene Top-Level-Sections.
- `## Pointer` am Fuß folgt Inhaltsverzeichnis-Logik (Verweise zuletzt).

### Neue Files

#### `00_Core/APPLIED-LEARNING.md`

```markdown
---
name: Applied Learning Log
description: Kuratierte Arbeitsprinzipien für Dynasty-Depot-Sessions (Tier 2 des 3-Tier-Lernsystems). Enthält Pflege-Regeln und Versionshistorie.
type: learning-log
updated: 2026-04-24
---

# Applied Learning — Kuratierte Arbeitsprinzipien

> Tier 2 des 3-Tier-Systems (Auto-Memory → Applied Learning → INSTRUKTIONEN.md).
> <15 Wörter pro Bullet. Nur operativ relevante Arbeitsprinzipien — keine Tool-References (→ Auto-Memory) und keine systemischen Regeln (→ INSTRUKTIONEN.md §§).

## Bullets (Stand: 12/20)

[12 Bullets 1:1 aus heutiger CLAUDE.md übernommen, unverändert]

## Pflege-Regeln

**Proaktive Pflege (seit 18.04.2026):** Bei jedem Monats-Übergang 5-Min-Scan — Tool-References identifizieren und evakuieren. Verhindert Buildup, billiger als reaktive Überlauf-Sanierung.

**Kurator-Regel bei Überlauf (20/20):** Hybrid-Strategie:
1. Tool-References → Auto-Memory
2. Stabile Regeln → neue INSTRUKTIONEN-§
3. Thematisch verwandte Bullets konsolidieren

Ziel: ≤15/20 nach Revision. Archivierung ist kein Weg (toter Code).

## Promotion-Logik

Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).

## Historie

[v1.0 → v2.4 Block 1:1 aus CLAUDE.md übernommen]
```

**Migrations-Invariante (gilt ausschließlich während der Tier-1-Implementierung):**
Inhalte werden zeichengenau 1:1 aus heutiger CLAUDE.md übernommen. Keine Re-Editierung, keine Konsolidierung, keine Re-Phrasierung, keine Reihenfolge-Änderung der Bullets. Informationsverlust-Aversion (Memory `feedback_information_loss_aversion.md`).

**Trennung Migration vs. Kuration:** Die Pflege-Regel „Thematisch verwandte Bullets konsolidieren" (Kurator-Regel bei Überlauf) gilt **nur für zukünftige Kurations-Zyklen nach abgeschlossenem Deploy**, niemals während der Migration. Konsolidierung ist erlaubt als Anlass-bezogener Schritt mit Historie-Eintrag (analog v2.0-Konsolidierung 18.04.2026), nicht als nebenbei-Aktion während des Refactors.

#### `00_Core/TOKEN-RULES.md`

```markdown
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
> Diese Regeln liegen vor und sind via Pointer aus CLAUDE.md erreichbar. Es gibt **keinen Enforcement-Mechanismus** (kein Hook, kein Skill-Check, kein Audit). Anwendung erfolgt durch bewusste Entscheidung der jeweiligen Session — nicht durch automatische Kontrolle.

## Regeln

- **Snapshot-First:** STATE.md + Faktortabelle vor API — spart 3-5 Tool-Calls
- **Sync-Pflicht (alle sechs):** log.md + CORE-MEMORY.md + Faktortabelle + STATE.md + score_history.jsonl + flag_events.jsonl
- **Pause-Regel:** >5 Min → /compact (Preserve: Score/Tabelle/Urteil/FLAGs) oder /clear
- **DEFCON 1 Stopp:** Score <50 → Analyse stoppen (Insider-Modul läuft durch)
- **MCP:** Tool Search lädt lazy. Manuell deaktivieren nur bei Vault-Only-Sessions.
- **Modell:** Sonnet 4.6 default; `/model opus` für !Analysiere, Multi-Step-Refactors, strategische Entscheidungen.
```

### Routing-Table (CLAUDE.md, neue Section)

```markdown
## Routing-Table

> Pflicht-Read STATE.md immer. Tabelle nennt zusätzliche Reads, explizite Skips, Skill-Trigger.
> **Match-Regel (Hybrid):** Exakte Trigger strikt. Eine Soft-Match-Ausnahme — bare Ticker-Symbol ohne Trigger-Wort → behandle als `!QuickCheck <Ticker>`. Bei Mehrfach-Match (z.B. Ticker + Wiki-Begriff): Union der Lies-Spalten.
> **Bei Trigger-Miss:** konservativ mehr laden statt zu wenig.

| Trigger | Lies zusätzlich | Skippe | Skill-Call |
|---------|-----------------|--------|------------|
| `Session starten` (default) | (Resume-Fall: SESSION-HANDOVER.md) | CORE-MEMORY, INSTRUKTIONEN, KONTEXT, Faktortabelle, Wissenschaftliche-Fundierung-DEFCON | — |
| `!Analysiere <Ticker>` | INSTRUKTIONEN.md, Faktortabelle.md, `…/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` | KONTEXT, CORE-MEMORY (außer §5 bei Scoring-Edge-Case) | `dynastie-depot` + `backtest-ready-forward-verify` (Schritt 7, programmatisch) |
| `!QuickCheck <Ticker>` | Faktortabelle.md | INSTRUKTIONEN, KONTEXT, CORE-MEMORY, Wiss-Fundierung | `quick-screener` |
| `!Rebalancing` | INSTRUKTIONEN.md, KONTEXT.md | CORE-MEMORY, Faktortabelle, Wiss-Fundierung | — |
| `!SyncBriefing` | INSTRUKTIONEN.md (§25) | alle anderen | — |
| Wiki-Ops (`ingest`/`lint`/`query`, „Vault"/„Obsidian"/„Faktortabelle-Edit"/„Score-Update"/„Insider scan"/„entity"/„Satellit Seite") | `07_Obsidian Vault/.../WIKI-SCHEMA.md` | INSTRUKTIONEN, KONTEXT, CORE-MEMORY (außer Wiki-Bezug) | je nach WIKI-SCHEMA-Workflow (`insider-intelligence`, `non-us-fundamentals`, …) |
| `remote-Control` / „mobile weiter" | Auto-Memory `remote-trigger-api.md` | alles andere (Snapshot reicht) | — (User-getriggerter `ccr`-Spawn) |
| Konsolidierungstag / System-Audit / Backlog-Review | SESSION-HANDOVER.md, STATE.md §Pipeline + §System | KONTEXT, Faktortabelle (außer ticker-spezifisch) | `SystemAudit` (slash) bei Audit-Lauf |
| Strategie-/Allokations-Frage | KONTEXT.md | Faktortabelle, Wiss-Fundierung | — |
```

### Edge-Cases der Match-Regel

Die Hybrid-Match-Regel deckt drei Edge-Cases nicht implizit ab. Sie werden hier explizit normiert:

1. **Trigger + Wiki-Begriff (z.B. „!Analysiere TMO und update Vault-Faktortabelle"):**
   Beide Trigger matchen → Union der „Lies zusätzlich"-Spalten. Skip-Spalten verlieren ihre Wirkung sobald ein anderer Trigger die jeweilige Datei explizit anfordert (Skip wirkt nur, wenn kein Trigger der Tabelle die Datei anfordert). Skill-Calls beider Trigger werden ausgeführt.

2. **Tippfehler oder fast-exakte Trigger (z.B. `!Analysier`, `!Quickcheck` ohne Camel-Case):**
   Kein Fuzzy-Match. Behandlung wie Trigger-Miss → Default-Verhalten (`Session starten`-Row), aber Claude MUSS in derselben Antwort eine Rückfrage stellen („Meintest du `!Analysiere TMO`?"). Keine stillschweigende Selbstinterpretation.

3. **Bare Symbol das Ticker UND deutsches Wort sein kann (z.B. „V"):**
   Ticker-Soft-Match aktiviert sich nur wenn das Symbol zu den **11 aktuellen Satelliten-Tickern** (siehe STATE.md Portfolio-Tabelle) gehört. Mehrdeutige bare Symbole wie „V" matchen, weil V Satellit ist. Symbole wie „A", „M" oder „K" matchen nicht (kein Satellit). Im Zweifelsfall (z.B. unklare Groß/Kleinschreibung) Rückfrage statt Auto-Routing.

Diese drei Klauseln sind Teil des Routing-Verhaltens und werden in der `## Routing-Table`-Section in CLAUDE.md als kompakter Block unter der Tabelle aufgenommen (Implementierung-Plan spezifiziert exakte Formulierung).

### `## Pointer (Ausgelagertes)` (CLAUDE.md, neue Section am Fuß)

```markdown
## Pointer (Ausgelagertes)

| Datei | Zweck |
|-------|-------|
| `00_Core/APPLIED-LEARNING.md` | Tier-2-Arbeitsprinzipien + Pflege-Regeln + Historie |
| `00_Core/TOKEN-RULES.md` | Token-Effizienz-Regeln (Accessibility, kein Enforcement) |
| `00_Core/INSTRUKTIONEN.md` | Tier-3-Regeln (Scoring-Skalen, Workflows, §§) |
```

## Datenfluss / Lese-Logik

1. **Session-Start:** Harness lädt `CLAUDE.md` + `STATE.md` (Pflicht-Read). Routing-Table wird gelesen, aber keine Folgereferenzen automatisch geladen.
2. **User-Input klassifizieren:** Match gegen Trigger-Spalte (Hybrid-Regel). Bare Ticker → `!QuickCheck`. Bei Mehrfach-Match → Union der Lies-Spalten.
3. **On-Demand-Lektüre:** Nur Files aus „Lies zusätzlich"-Spalte des gematchten Triggers werden gelesen.
4. **Skip-Spalte:** Wirkt als expliziter Anti-Reflex — verhindert „sicherheitshalber alles lesen"-Verhalten.
5. **Skill-Call:** Falls in Skill-Spalte gelistet, Skill via `Skill`-Tool aktivieren (`backtest-ready-forward-verify` programmatisch aus `dynastie-depot` Schritt 7, kein eigener Trigger-Word).

## Pre-Move-Risk-Assessment

**Pre-Move-Grep ausgeführt 2026-04-24** mit Pattern `Applied Learning|Token-Effizienz` über `00_Core/`, `01_Skills/`, `03_Tools/`, `07_Obsidian Vault/`, `docs/`.

**Ergebnis:**
- **Keine gebrochenen Markdown-Links.** Keine externe Referenz zeigt auf `CLAUDE.md#applied-learning`, `CLAUDE.md#token-effizienz` oder ähnliche Anker.
- **Konzept-Bezüge** in `INSTRUKTIONEN.md`, `CORE-MEMORY.md`, `01_Skills/dynastie-depot/SKILL.md`, mehreren Vault-Notes — alle als historische Bezüge oder Bullet-Zitate. Bleiben funktional valide, weil Konzept „Applied Learning" nicht entfällt, sondern in dedizierter Datei lebt.
- **Versions-String** in `01_Skills/dynastie-depot/capex-fcf-template.md`: „Token-Effizienz v4.0" — Konzept-Versions-String, kein File-Pfad. Kein Bruch.

**Update-Empfehlungen (nicht Spec-Pflicht, separater Cleanup-Sweep):**
1. **`07_Obsidian Vault/.../wiki/concepts/CLAUDE-md-Konstitution.md`** — beschreibt CLAUDE.md-Sections strukturell mit Tabelle „Section | Charakter | Update-Frequenz". Nach Refactor: Tabelle aktualisieren (Applied Learning + Token-Effizienz wandern aus, Routing-Table + Pointer ergänzen).
2. **Konzept-Cross-Links** in Vault-Notes (Backtest-Methodik-Roadmap, Factor-Information-Decay, Session-Start-Protokoll, Wissenschaftliche-Fundierung-DEFCON) — könnten optional `[[Applied Learning]]` → `[[APPLIED-LEARNING]]` aktualisiert werden. Funktional irrelevant.

**Worktree-Treffer** (`.claude/worktrees/stupefied-bhabha-43cb6a/`) sind Spiegel-Kopien einer alten Worktree (gemäß `git status` untracked). Cleanup-Backlog-Punkt, nicht Spec-Scope.

## Governance / Pflege-Pflichten

### Routing-Table-Pflege

- **Trigger:** Beim Anlegen neuer Trigger-Words ODER neuer Skills mit eigener Trigger-Phrase ODER Renaming bestehender Trigger.
- **Regel:** Routing-Table in CLAUDE.md MUSS aktualisiert werden im selben Commit.
- **SSoT-Status:** Routing-Table ist SSoT für Trigger-Word → Lies-zusätzlich-Mapping. Wiki-Mode-Workflow-Details bleiben in WIKI-SCHEMA.md (Routing-Table verweist).

### APPLIED-LEARNING.md-Pflege

- **SSoT-Status nach Deploy:** APPLIED-LEARNING.md ist nach erfolgreicher Tier-1-Migration die **alleinige Wahrheitsquelle** für Tier-2-Bullets, Pflege-Regeln und Promotion-Logik. CLAUDE.md verweist nur per Pointer. Jede Bullet-Mutation findet ausschließlich in APPLIED-LEARNING.md statt — keine parallele Bullet-Liste in CLAUDE.md, in INSTRUKTIONEN.md oder in Vault-Notes (Konzept-Bezüge bleiben erlaubt, eigene Bullet-Listen nicht).
- **Proaktive-Pflege-Regel:** Bei jedem Monats-Übergang 5-Min-Scan — Tool-References identifizieren und nach Auto-Memory evakuieren. Unverändert aus heutiger Praxis.
- **Kurator-Regel bei Überlauf (20/20):** Hybrid-Strategie (Tool-Refs → Auto-Memory, stabile Regeln → INSTRUKTIONEN-§, thematische Konsolidierung). Ziel ≤15/20 nach Revision. Konsolidierung erfolgt nur als bewusster Kuration-Schritt mit Historie-Eintrag (siehe Migrations-Invariante).
- **Versionshistorie:** Bullet-Zählungen + Promotion-Events + Konsolidierungs-Events werden in `## Historie`-Section nachgehalten (analog v1.0-v2.4).

### TOKEN-RULES.md SSoT-Status

- **Nach Deploy alleinige Wahrheitsquelle** für Token-Effizienz-Regeln. CLAUDE.md verweist nur per Pointer. Falls eine Regel doch in CLAUDE.md zurückkehren soll, MUSS sie aus TOKEN-RULES.md entfernt werden (siehe TOKEN-RULES.md-Pflege „Drift-Prävention" unten). **Keine stillschweigende Doppel-Kuration.**

### TOKEN-RULES.md-Pflege

- **Bei Regel-Änderung:** Datei aktualisieren, Frontmatter `updated:` neu setzen.
- **Kein Enforcement:** Es existiert kein Hook und kein Audit-Check, der die Anwendung dieser Regeln prüft. Anwendung erfolgt durch bewusste Entscheidung der jeweiligen Session.
- **Drift-Prävention:** Falls eine Regel in CLAUDE.md zurückkehren soll (z.B. weil Pain-Schwelle erreicht), muss sie aus TOKEN-RULES.md entfernt oder explizit als Duplikat markiert werden. **Keine stillschweigende Duplizierung.**

## Acceptance-Kriterien

1. CLAUDE.md hat ≤80 Zeilen (Ziel ~70, Toleranz +10).
2. CLAUDE.md enthält die Top-Level-Sections in dokumentierter Reihenfolge: `# SESSION-INITIALISIERUNG` (mit Sub-Sections Pflicht-Read / Verhalten / Kontinuierliches Lernen) → `## Projektstruktur` → `## Routing-Table` → `## Wiki-Modus` → `## Pointer (Ausgelagertes)`.
3. `## Token-Effizienz (operativ)` ist aus CLAUDE.md vollständig entfernt.
4. `### Applied Learning (kuratiert, max. 20 Bullets)` ist aus CLAUDE.md vollständig entfernt; `## Kontinuierliches Lernen` enthält nur die 3-Tier-Tabelle + Pointer-Verweis.
5. `00_Core/APPLIED-LEARNING.md` existiert mit Frontmatter (name/description/type/updated) und enthält die 12 Bullets, die Pflege-Regeln, die Promotion-Logik und die Historie v1.0-v2.4 — Inhalte 1:1 aus heutiger CLAUDE.md übernommen.
6. `00_Core/TOKEN-RULES.md` existiert mit Frontmatter (name/description/type/scope/enforcement/updated), explizitem Accessibility-Hinweis und den 6 Regeln aus heutiger CLAUDE.md `## Token-Effizienz (operativ)`.
7. Routing-Table enthält genau die **9 Trigger-Daten-Zeilen** (Tabellen-Header + Markdown-Separator-Zeile zählen nicht) mit den 4 Spalten Trigger / Lies zusätzlich / Skippe / Skill-Call. Direkt unter der Tabelle steht der „Edge-Cases der Match-Regel"-Block mit den 3 normierten Cases.
8. `## Pointer (Ausgelagertes)` enthält genau die 3 Daten-Zeilen aus dokumentierter Tabelle (Header + Separator nicht mitgezählt).
9a. **Grep-Check auf alte Headings:** `grep -n "## Token-Effizienz (operativ)\|### Applied Learning (kuratiert" CLAUDE.md` liefert **0 Treffer**. (Pattern matcht die exakten alten Section-Header, nicht Pointer-Zeilen.)
9b. **Externe-Anker-Check:** `grep -rn "CLAUDE.md#applied-learning\|CLAUDE.md#token-effizienz" 00_Core/ 01_Skills/ 03_Tools/ 07_Obsidian\ Vault/ docs/` liefert **0 Treffer** (nach Migration weiterhin keine externen Anker-Links existent).
10. **Diff-Verifikation 1:1-Migration:** Implementierungs-Plan stellt ein Verify-Script bereit, das (a) den `### Applied Learning`-Block aus dem Pre-Migration-Commit der CLAUDE.md extrahiert, (b) den Bullet-Block + Pflege-Regeln + Historie aus der neuen `00_Core/APPLIED-LEARNING.md` extrahiert und (c) `git diff --no-index --no-color` zwischen beiden ausgibt. Akzeptanz: nur Frontmatter-Hinzufügung + Heading-Wrapper-Differenzen, kein einziger geänderter Bullet-Text. Analog für `## Token-Effizienz (operativ)` → `00_Core/TOKEN-RULES.md`.
11. **Negatives Scope-AC (Tier-1-Grenze):** Tier-1-Implementierung ändert keine Dateien außerhalb von (a) `CLAUDE.md`, (b) `00_Core/APPLIED-LEARNING.md` (neu), (c) `00_Core/TOKEN-RULES.md` (neu). Insbesondere keine Edits an `INSTRUKTIONEN.md`, `STATE.md`, `CORE-MEMORY.md`, Vault-Notes, Skill-Files oder Tools. Cross-Link-Updates im Vault sind separater Cleanup-Sweep (siehe Future Work).

## Future Work / Deferred

### Tier 2 — STATE.md 3-Split (Variante B Hub)

STATE.md wird zum ~10-Zeilen-Hub mit Banner + Pointer. Darunter:
- `00_Core/PORTFOLIO.md` — Portfolio-State + Watches + 30d-Trigger (konsolidiert mit 🟠 Portfolio-Triggers-Block)
- `00_Core/PIPELINE.md` — Pipeline-SSoT 🔴/🟡/🔵 + Long-Term-Gates ⏰
- `00_Core/SYSTEM.md` — System-Zustand + Audit + Backlog

Erwarteter Effekt: ~70% Session-Start-Cost-Reduktion. Eigene Spec, separate Session.

### Tier 2b — CORE-MEMORY.md Subkategorisierung

Kalendarische Riesen-Liste → Subkategorien + Verknüpfung mit adressierten System-Elementen. Eigene Spec.

### Tier 3 — `vault_backlinks`-Check-Erweiterung auf Root-Ordner

Bereits Backlog-Punkt STATE.md Z. 120. Audit-Check-Erweiterung, eigener kleiner Plan.

### Cross-Link-Update-Sweep im Vault

Nach Tier-1-Deploy: separater Sweep zur Aktualisierung von `CLAUDE-md-Konstitution.md` (Vault-Konzept-Note) und optional Konzept-Cross-Links in 4-5 Vault-Notes. Nicht spec-blockierend.

### Worktree-Cleanup

`.claude/worktrees/stupefied-bhabha-43cb6a/` ist gemäß `git status` untracked. Backlog-Aufgabe für Konsolidierungstag.

## Revision History

- **2026-04-24 v0.1 (initial draft):** Claude Opus 4.7 + User. Brainstorm-Sessions Sections 1+2 (Datei-Layout + CLAUDE.md-Zielstruktur) auf Desktop, Sections 3+4 (Routing-Table + Content-Migration) auf Mobile via /remote-control. Verbindliche Entscheidungen: A=ja (Routing-Table ersetzt On-Demand), B=c (TOKEN-RULES Accessibility), Match=Hybrid, Trigger-Inventar=9 Zeilen, KontLernen=A, TokenEff=X. Advisor-Konsultation auf Desktop adressierte 3 Blind-Spots (Pain #1 Kategorie A vs B, Accessibility-Explizität, Routing-Table-Ersetzung). Pre-Move-Grep ausgeführt — keine gebrochenen Anker. Bezug Memory `feedback_multi_source_drift_check.md` (kein Silent-Fix bei §-Drift in Spec).
- **2026-04-24 v0.2 (Codex-Review-Pass):** Codex-Verdict RECOMMEND_REVISE adressiert. Achse 3 (Match-Regel-Edge-Cases): neuer Sub-Abschnitt „Edge-Cases der Match-Regel" mit 3 Cases (Trigger+Wiki-Union, Tippfehler-Rückfrage, Bare-Symbol-Whitelist über STATE.md-Satelliten). Achse 4 (Falsifizierbarkeit): AC #9 in #9a (alte Headings) + #9b (externe Anker) gesplittet, AC #10 mit konkretem `git diff --no-index`-Verify-Script-Anker spezifiziert. Achse 5 (Anti-Hallucination): Migrations-Invariante explizit von Kurations-Regel getrennt, SSoT-Status nach Deploy für APPLIED-LEARNING.md + TOKEN-RULES.md deklariert. Achse 1: AC #7 klargestellt (9 Trigger-Daten-Zeilen, Header/Separator ausgeschlossen). Achse 2: AC #11 Negatives Scope-AC ergänzt (keine Edits außerhalb 3 Files). Bezug Memory `feedback_review_stack.md` (Codex-Reviewer-Slot vor Plan-Writing).

## Anhang A — Bezug zu projekt-weiten Memories

- `feedback_information_loss_aversion.md` — Bullets/Historie 1:1 übernehmen, kein Re-Editieren.
- `feedback_multi_source_drift_check.md` — Pre-Move-Grep + Routing-Table als SSoT, keine Duplizierung mit On-Demand-Liste.
- `feedback_review_stack.md` — Codex-Reconciliation nach Implementation-Plan-Draft, nicht jetzt.
- `feedback_spec_section_drift.md` — falls Plan später §-Drift entwickelt, Header-Notice + Codex-Attestierung, Spec frozen.
- `feedback_friction_as_evidence.md` — Routing-Table-Pflege-Pflicht ist explizit als Friction angelegt, weil Drift sonst silent eintritt.
