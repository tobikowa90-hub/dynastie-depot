# CLAUDE.md Routing-Refactor (Tier 1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** CLAUDE.md von 98 auf ≤80 Zeilen schrumpfen durch Auslagerung von Applied Learning + Token-Effizienz in `00_Core/APPLIED-LEARNING.md` + `00_Core/TOKEN-RULES.md` und Einfügen einer Routing-Table, die On-Demand-Lektüre systematisiert.

**Architecture:** Drei sequentielle Phasen — (1) zwei neue Files mit 1:1-migrierten Inhalten + Frontmatter erstellen, (2) CLAUDE.md refaktorisieren (alte Sections raus, bestehende restrukturieren, neue Sections einfügen), (3) Acceptance-Verifikation gegen Spec v0.2. Inline-Bash-Verify-Commands (kein checked-in Script — AC #11 verbietet Edits außerhalb der 3 Files).

**Tech Stack:** Markdown (Editing), Bash + sed/awk (Inline-Verify), git (Commit per Task), Python (system_audit.py Smoke).

**Bezug:** Spec `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md` v0.2 (Codex-Reviewed, RECOMMEND_REVISE adressiert).

---

## File Structure

| Datei | Aktion | Verantwortung |
|-------|--------|---------------|
| `CLAUDE.md` | Modify | Session-Init-Konstitution, neue Routing-Table + Pointer, alte Sections raus |
| `00_Core/APPLIED-LEARNING.md` | Create | SSoT für Tier-2-Bullets, Pflege-Regeln, Historie |
| `00_Core/TOKEN-RULES.md` | Create | SSoT für Token-Effizienz-Regeln (Accessibility-Modell) |

**Negativ-Scope (AC #11):** Keine anderen Files werden in dieser Implementation geändert. Insbesondere nicht: `INSTRUKTIONEN.md`, `STATE.md`, `CORE-MEMORY.md`, Vault-Notes, Skill-Files, Tools, Tests.

**Pre-Migration Source-of-Truth:** `CLAUDE.md` Zustand am Start des Plans (HEAD-Commit `1358346` oder neuer, sobald Plan committed wird). Alle 1:1-Diffs verifizieren gegen diesen Pre-Migration-Stand.

---

## Task 1: Pre-Migration Snapshot + Pre-Conditions

**Files:**
- Read-only: `CLAUDE.md` (aktueller HEAD)
- Snapshot-Target: `/tmp/claude_md_pre_migration.md` (lokal, nicht committed)

**Zweck:** Den Stand der CLAUDE.md vor dem Refactor festhalten, um in Task 2/3/8 die 1:1-Migration der Bullets per `git diff --no-index` belegen zu können.

- [ ] **Step 1: Sichern der aktuellen CLAUDE.md ins Temp-Verzeichnis**

```bash
cp "CLAUDE.md" /tmp/claude_md_pre_migration.md
wc -l /tmp/claude_md_pre_migration.md
```

Expected: `98 /tmp/claude_md_pre_migration.md` (oder ähnlich, je nach EOL-Konvention; AC-Baseline)

- [ ] **Step 2: Extrahieren der Applied-Learning-Bullets in Snapshot-Datei**

```bash
sed -n '/^### Applied Learning/,/^[^#]*$/p' /tmp/claude_md_pre_migration.md > /tmp/old_applied_learning_block.md
wc -l /tmp/old_applied_learning_block.md
```

Expected: ≥20 Zeilen (Heading + Intro-Quote-Block + 12 Bullets + Historie).

- [ ] **Step 3: Extrahieren der Token-Effizienz-Section in Snapshot-Datei**

```bash
sed -n '/^## Token-Effizienz (operativ)/,/^## /p' /tmp/claude_md_pre_migration.md | sed '$d' > /tmp/old_token_eff_block.md
wc -l /tmp/old_token_eff_block.md
```

Expected: 8-10 Zeilen (Heading + 6 Regel-Bullets + Spacing). Das `sed '$d'` entfernt die nächste `## `-Zeile am Ende der Range.

- [ ] **Step 4: Pre-Conditions verifizieren — alte Sections existieren**

```bash
grep -c "^### Applied Learning" CLAUDE.md
grep -c "^## Token-Effizienz" CLAUDE.md
```

Expected: jeweils `1` (genau 1 Match pro alter Section).

- [ ] **Step 5: Pre-Conditions verifizieren — Ziel-Files existieren NICHT**

```bash
test -f 00_Core/APPLIED-LEARNING.md && echo "EXISTS" || echo "OK_NOT_EXISTS"
test -f 00_Core/TOKEN-RULES.md && echo "EXISTS" || echo "OK_NOT_EXISTS"
```

Expected: jeweils `OK_NOT_EXISTS`.

- [ ] **Step 6: Kein Commit (Snapshot-Files liegen in /tmp, nicht im Repo)**

Begründung: AC #11 (Negative Scope) verbietet Repo-Edits außerhalb der 3 Ziel-Files. Snapshots sind Verifikations-Hilfsmittel, nicht Tier-1-Artefakte.

---

## Task 2: Create `00_Core/APPLIED-LEARNING.md` (1:1 Migration)

**Files:**
- Create: `00_Core/APPLIED-LEARNING.md`
- Read-only: `/tmp/old_applied_learning_block.md` (aus Task 1)

**Zweck:** SSoT für Tier-2 Bullets + Pflege-Regeln + Historie. Inhalte zeichengenau 1:1 aus heutiger CLAUDE.md übernommen (Migrations-Invariante per Spec v0.2).

- [ ] **Step 1: Datei mit Frontmatter + 1:1-Inhalten schreiben**

Erstelle `00_Core/APPLIED-LEARNING.md` mit folgendem exakten Inhalt:

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

## Promotion-Logik

Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).

## Historie

v1.0 (17.04.2026) 19 Bullets gemischt. v2.0 (18.04.2026) Evakuierung: 6 Tool-Refs → Auto-Memory, 4 systemische Regeln → INSTRUKTIONEN §27, auf **9 Kern-Arbeitsprinzipien** reduziert. Neues +1 (Option B FLAG-Entscheidung). v2.1 (18.04.2026) Bullet „Scoring-Version-Bump re-verify" → INSTRUKTIONEN §28.2 promoted. v2.2 (20.04.2026) +1 (Spec-§-Drift-Handling, aus Track-5-Plan-Writing). v2.3 (20.04.2026 Nacht-Spät) +1 (Anti-Hallucination-Datenpfad-Vollständigkeit, aus v3.0.3-Incident). v2.4 (21.04.2026) +1 (Exhaustive-Drift-Check, aus Pre-Provenance-Plan-Compat-Check 12/27 silent v3.7-Threshold-Drift). v2.5 (24.04.2026) Migration aus CLAUDE.md in eigene Datei, Pflege-Regeln + Promotion-Logik mitgenommen, Bullet-Inhalt unverändert. Stand: **12/20**.
```

- [ ] **Step 2: Verify — Bullet-Anzahl exakt 12**

```bash
grep -c "^- " 00_Core/APPLIED-LEARNING.md
```

Expected: `12`

- [ ] **Step 3: Verify — Jeder Bullet-Text ist zeichengenau identisch zur alten CLAUDE.md**

```bash
grep "^- " /tmp/claude_md_pre_migration.md > /tmp/old_bullets.txt
grep "^- " 00_Core/APPLIED-LEARNING.md > /tmp/new_bullets.txt
git diff --no-index --no-color /tmp/old_bullets.txt /tmp/new_bullets.txt
```

Expected: `exit 0` (no differences). Falls Diff existiert → STOP, ein Bullet wurde versehentlich umformuliert. Korrigieren bis Diff leer.

- [ ] **Step 4: Verify — Pflege-Regel + Historie 1:1 vorhanden**

```bash
grep -c "Proaktive Pflege (seit 18.04.2026)" 00_Core/APPLIED-LEARNING.md
grep -c "Kurator-Regel bei Überlauf (20/20)" 00_Core/APPLIED-LEARNING.md
grep -c "v1.0 (17.04.2026) 19 Bullets gemischt" 00_Core/APPLIED-LEARNING.md
grep -c "v2.4 (21.04.2026) +1 (Exhaustive-Drift-Check" 00_Core/APPLIED-LEARNING.md
grep -c "v2.5 (24.04.2026) Migration aus CLAUDE.md" 00_Core/APPLIED-LEARNING.md
```

Expected: jeweils `1`.

- [ ] **Step 5: Commit**

```bash
git add 00_Core/APPLIED-LEARNING.md
git commit -m "feat(claude-md-routing): create APPLIED-LEARNING.md — Tier-2 SSoT für Bullets+Pflege+Historie

1:1 Migration aus CLAUDE.md ### Applied Learning Section.
12 Bullets unveraendert (Diff-Verify PASS), Pflege-Regeln + Historie mitgenommen.
Frontmatter (name/description/type/updated) ergaenzt, neuer Historie-Eintrag v2.5.

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2 AC #5.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: Create `00_Core/TOKEN-RULES.md` (1:1 Migration)

**Files:**
- Create: `00_Core/TOKEN-RULES.md`
- Read-only: `/tmp/old_token_eff_block.md` (aus Task 1)

**Zweck:** SSoT für Token-Effizienz-Regeln. Accessibility-Modell explizit (kein Enforcement). Inhalte zeichengenau 1:1 aus heutiger CLAUDE.md.

- [ ] **Step 1: Datei mit Frontmatter + Accessibility-Hinweis + 6 Regel-Bullets schreiben**

Erstelle `00_Core/TOKEN-RULES.md` mit folgendem exakten Inhalt:

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

- [ ] **Step 2: Verify — Genau 6 Regel-Bullets**

```bash
grep -c "^- \*\*" 00_Core/TOKEN-RULES.md
```

Expected: `6`

- [ ] **Step 3: Verify — Alle 6 Regel-Bullets zeichengenau identisch zur alten CLAUDE.md**

```bash
grep "^- \*\*" /tmp/claude_md_pre_migration.md | head -6 > /tmp/old_token_bullets.txt
grep "^- \*\*" 00_Core/TOKEN-RULES.md > /tmp/new_token_bullets.txt
git diff --no-index --no-color /tmp/old_token_bullets.txt /tmp/new_token_bullets.txt
```

Expected: `exit 0` (no differences). Hinweis: `head -6` ist OK weil die ersten 6 `- **`-Bullets in pre_migration.md die Token-Effizienz-Regeln sind (kein anderes Vorkommen davor — verifiziere mit `grep -n '^- \*\*' /tmp/claude_md_pre_migration.md` falls Zweifel).

- [ ] **Step 4: Verify — Accessibility-Hinweis vorhanden**

```bash
grep -c "Accessibility-Hinweis" 00_Core/TOKEN-RULES.md
grep -c "kein Enforcement-Mechanismus" 00_Core/TOKEN-RULES.md
```

Expected: jeweils `1`.

- [ ] **Step 5: Commit**

```bash
git add 00_Core/TOKEN-RULES.md
git commit -m "feat(claude-md-routing): create TOKEN-RULES.md — Accessibility-Modell SSoT

1:1 Migration aus CLAUDE.md ## Token-Effizienz (operativ) Section.
6 Regel-Bullets unveraendert (Diff-Verify PASS).
Frontmatter (name/description/type/scope/enforcement/updated) + Accessibility-Hinweis ergaenzt.
Explizit kein Enforcement-Mechanismus (Spec-Entscheidung B=c).

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2 AC #6.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: CLAUDE.md — Remove obsolete sections

**Files:**
- Modify: `CLAUDE.md` (Sections raus)

**Zweck:** Die migrierten Inhalte (Applied Learning, Token-Effizienz, On-Demand-Lektüre) aus CLAUDE.md entfernen. Zwischenzustand: CLAUDE.md ist temporär „kaputt" (Routing-Table noch nicht da), wird in Tasks 5-7 wieder kompletiert.

- [ ] **Step 1: Entferne `## Token-Effizienz (operativ)` Section vollständig**

Suche in `CLAUDE.md` den Block:
```markdown
## Token-Effizienz (operativ)

- **Snapshot-First:** STATE.md + Faktortabelle vor API — spart 3-5 Tool-Calls
- **Sync-Pflicht (alle sechs):** log.md + CORE-MEMORY.md + Faktortabelle + STATE.md + score_history.jsonl + flag_events.jsonl
- **Pause-Regel:** >5 Min → /compact (Preserve: Score/Tabelle/Urteil/FLAGs) oder /clear
- **DEFCON 1 Stopp:** Score <50 → Analyse stoppen (Insider-Modul läuft durch)
- **MCP:** Tool Search lädt lazy. Manuell deaktivieren nur bei Vault-Only-Sessions.
- **Modell:** Sonnet 4.6 default; `/model opus` für !Analysiere, Multi-Step-Refactors, strategische Entscheidungen.

```

und ersetze ihn durch eine **leere Zeichenkette** (komplett raus, inklusive der trailing-Leerzeile vor `## Kontinuierliches Lernen`).

- [ ] **Step 2: Entferne `### Applied Learning (kuratiert, max. 20 Bullets)` Sub-Section vollständig**

Suche in `CLAUDE.md` den Block, der mit `### Applied Learning (kuratiert, max. 20 Bullets)` beginnt und bis zum Ende der Datei reicht (inklusive Intro-Quote-Block, alle 12 Bullets, Historie). Entferne komplett.

- [ ] **Step 3: Entferne den `**On-Demand-Lektüre**` Block aus `# SESSION-INITIALISIERUNG`**

Suche in `CLAUDE.md` den Block:
```markdown
**On-Demand-Lektüre** (nur wenn Kontext explizit gebraucht wird):
- `CORE-MEMORY.md` — Scoring-Lektionen (§5), Positions-Entscheidungen (§3), Audit-Log (§10), aktuelle Meilensteine ab 15.04. (§1)
- `INSTRUKTIONEN.md` — Scoring-Skalen, Sparplan-Formel, Workflows (bei `!Analysiere`, `!Rebalancing`)
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` — **Status-Matrix** (Single Source of Truth für wissenschaftliche Befunde B1-B24+; automatisch aktiv via §4 Router in `!Analysiere`, via §28 bei Migration, via §29 bei Retrospective, via §33 bei Skill-Architektur-Proposals; nicht in mechanischen Workflows `!QuickCheck` / `!Rebalancing` / Screener)
- `KONTEXT.md` — Strategie, Allokation, Slot-Zuteilung (bei Strategie-Fragen)
- `Faktortabelle.md` — Detail-Metriken pro Ticker (bei Deep-Dive)
- `SESSION-HANDOVER.md` — Last-Session-Kontext (bei Fortsetzung)
- `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` — Chronik vor 15.04. (Projekt-Aufbau, Tool-Setups, erste Analysen)

```

und ersetze ihn durch **leere Zeichenkette** (komplett raus, inklusive Trailing-Leerzeile vor „Danach: kompakte Zusammenfassung..."). Entscheidung A der Spec: Routing-Table ersetzt diese Liste.

- [ ] **Step 4: Verify — Token-Effizienz raus**

```bash
grep -c "^## Token-Effizienz" CLAUDE.md
```

Expected: `0`

- [ ] **Step 5: Verify — Applied Learning Sub-Section raus**

```bash
grep -c "^### Applied Learning" CLAUDE.md
```

Expected: `0`

- [ ] **Step 6: Verify — On-Demand-Lektüre-Block raus**

```bash
grep -c "^\*\*On-Demand-Lektüre\*\*" CLAUDE.md
```

Expected: `0`

- [ ] **Step 7: Verify — Kein Bullet-Text aus Applied Learning übrig**

```bash
grep -c "Subagents nur für Code+Tests" CLAUDE.md
grep -c "Drift-Check.*exhaustive Schema-Validation" CLAUDE.md
```

Expected: jeweils `0` (Bullet-Text vollständig entfernt; Konzept lebt in APPLIED-LEARNING.md).

- [ ] **Step 8: Commit (intermediate state — CLAUDE.md temporär ohne Routing-Table/Pointer)**

```bash
git add CLAUDE.md
git commit -m "refactor(claude-md-routing): remove obsolete sections vor Routing-Table-Insertion

Entfernt:
- ## Token-Effizienz (operativ) (migriert nach 00_Core/TOKEN-RULES.md)
- ### Applied Learning (kuratiert) (migriert nach 00_Core/APPLIED-LEARNING.md)
- **On-Demand-Lektuere**-Block (wird durch Routing-Table ersetzt — Entscheidung A)

Zwischenzustand: CLAUDE.md temporaer ohne Routing-Table + Pointer. Wird in Tasks 5-7
wieder kompletiert.

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2 AC #3+#4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: CLAUDE.md — Restructure Kontinuierliches Lernen + Section-Reihenfolge

**Files:**
- Modify: `CLAUDE.md` (Section-Verschiebung + Schrumpfung)

**Zweck:** `## Kontinuierliches Lernen` von ~11 auf ~8 Zeilen schrumpfen (3-Tier-Tabelle bleibt, Promotion-Logik raus, Pointer rein) und gemäß Spec-Reihenfolge unter `## Verhalten` zwischen Verhalten und Projektstruktur einsortieren.

- [ ] **Step 1: `## Kontinuierliches Lernen (3-Tier-System)` neu schreiben**

Suche in `CLAUDE.md` den aktuellen Block (steht aktuell zwischen Wiki-Modus und dem entfernten Token-Effizienz, je nach Stand nach Task 4):

```markdown
## Kontinuierliches Lernen (3-Tier-System)

**Automatisch aktiv** (`autoMemoryEnabled + autoDreamEnabled`):

| Tier | Speicherort | Wer schreibt | Wann gelesen | Pflege |
|------|------------|--------------|-------------|--------|
| 1. Auto-Memory | `~/.claude/.../memory/*.md` | Claude automatisch | Session-Start | Auto-Dream konsolidiert |
| 2. Applied Learning | CLAUDE.md (diese Sektion) | Manuell bei Review | Session-Start | Monatlich: Obsoletes raus |
| 3. Formelle Regeln | INSTRUKTIONEN.md §§ | Bei bewiesenem Bedarf | Session-Start | Bei Systemänderungen |

**Promotion-Logik:** Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).
```

und ersetze ihn durch:

```markdown
## Kontinuierliches Lernen

| Tier | Speicherort | Wer schreibt | Wann gelesen | Pflege |
|------|------------|--------------|-------------|--------|
| 1. Auto-Memory | `~/.claude/.../memory/*.md` | Claude automatisch | Session-Start | Auto-Dream konsolidiert |
| 2. Applied Learning | `00_Core/APPLIED-LEARNING.md` | Manuell bei Review | On-Demand (per Routing-Table) | Monatlich + Kurator-Regel |
| 3. Formelle Regeln | `00_Core/INSTRUKTIONEN.md` §§ | Bei bewiesenem Bedarf | Per Routing-Table | Bei Systemänderungen |

Bullets, Pflege-Regeln, Promotion-Logik, Historie: siehe `00_Core/APPLIED-LEARNING.md`.
```

Änderungen: (a) Heading-Suffix „(3-Tier-System)" raus (kürzer), (b) „Automatisch aktiv"-Hinweis raus (Tier 2/3 sind nicht automatisch — irreführend gewesen), (c) Tier-2 Speicherort = neue Datei, (d) Tier-3 Speicherort mit `00_Core/`-Prefix, (e) Promotion-Logik als eigener Block raus (lebt jetzt in APPLIED-LEARNING.md), (f) ein Pointer-Satz am Ende.

- [ ] **Step 2: Section-Reihenfolge prüfen — `## Kontinuierliches Lernen` muss zwischen `## Verhalten` und `## Projektstruktur` stehen**

```bash
grep -n "^## " CLAUDE.md
```

Expected output (Reihenfolge entscheidend, exakte Zeilen-Nrn variieren):
```
NN:## Verhalten
NN:## Kontinuierliches Lernen
NN:## Projektstruktur
NN:## Wiki-Modus
```

Falls `## Kontinuierliches Lernen` an falscher Stelle steht: gesamten Block ausschneiden und unmittelbar **vor** `## Projektstruktur` einfügen (mit jeweils einer Leerzeile davor und danach).

- [ ] **Step 3: Verify — Promotion-Logik-Sentence raus**

```bash
grep -c "^\*\*Promotion-Logik:\*\*" CLAUDE.md
```

Expected: `0` (lebt nun in APPLIED-LEARNING.md `## Promotion-Logik`).

- [ ] **Step 4: Verify — Pointer-Satz auf APPLIED-LEARNING.md vorhanden**

```bash
grep -c "siehe \`00_Core/APPLIED-LEARNING.md\`" CLAUDE.md
```

Expected: `1`

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md
git commit -m "refactor(claude-md-routing): schrumpfe Kontinuierliches Lernen + Section-Reihenfolge

- ## Kontinuierliches Lernen: 11 -> 8 Zeilen (3-Tier-Tabelle bleibt, Promotion-Logik raus,
  Pointer auf 00_Core/APPLIED-LEARNING.md ergaenzt — Variant A der Spec).
- Section-Reihenfolge: ## Kontinuierliches Lernen zwischen ## Verhalten und ## Projektstruktur
  einsortiert (per SESSION-INITIALISIERUNG-Gruppierung der Spec).
- Tier-2 Speicherort + Tier-3 Pfad korrigiert (00_Core/-Prefix).

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2 AC #2+#4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: CLAUDE.md — Add `## Routing-Table` Section + Edge-Cases-Block

**Files:**
- Modify: `CLAUDE.md` (neue Section einfügen)

**Zweck:** Die neue Routing-Table mit 9 Trigger-Daten-Zeilen + Match-Regel-Note + Edge-Cases-Block einfügen, zwischen `## Projektstruktur` und `## Wiki-Modus`.

- [ ] **Step 1: Routing-Table-Section unmittelbar vor `## Wiki-Modus` einfügen**

Vor der Zeile `## Wiki-Modus` einfügen (mit jeweils einer Leerzeile davor und danach):

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

**Edge-Cases der Match-Regel:**
- **Trigger + Wiki-Begriff** (z.B. „!Analysiere TMO und update Vault-Faktortabelle"): Union beider „Lies zusätzlich"-Spalten; Skip-Spalten verlieren Wirkung wenn anderer Trigger die Datei explizit anfordert; Skill-Calls beider Trigger ausführen.
- **Tippfehler / fast-exakte Trigger** (z.B. `!Analysier`, `!Quickcheck`): Kein Fuzzy-Match. Default-Verhalten + Rückfrage stellen („Meintest du `!Analysiere TMO`?"). Keine Selbstinterpretation.
- **Bare Symbol mit Wort-Ambiguität** (z.B. „V"): Soft-Match nur bei Symbolen aus den 11 aktuellen Satelliten-Tickern (siehe STATE.md Portfolio-Tabelle). Bei Zweifel Rückfrage.
```

- [ ] **Step 2: Verify — Section-Header existiert**

```bash
grep -c "^## Routing-Table$" CLAUDE.md
```

Expected: `1`

- [ ] **Step 3: Verify — Genau 9 Trigger-Daten-Zeilen in der Tabelle (AC #7)**

```bash
awk '/^## Routing-Table/,/^## Wiki-Modus/' CLAUDE.md | grep -c "^| \`\|^| Wiki\|^| Konsolidierungstag\|^| Strategie\|^| Session"
```

Expected: `9` (Header + Separator zählen NICHT, da sie mit `| Trigger` und `|---` beginnen).

Alternative explizite Variante:
```bash
awk '/^## Routing-Table/,/^## Wiki-Modus/' CLAUDE.md | grep -E "^\| (\`|Wiki-Ops|Konsolidierungstag|Strategie)" | wc -l
```

Expected: `9`

- [ ] **Step 4: Verify — Edge-Cases-Block mit 3 Bullets vorhanden**

```bash
awk '/^\*\*Edge-Cases der Match-Regel:\*\*/,/^## Wiki-Modus/' CLAUDE.md | grep -c "^- \*\*"
```

Expected: `3`

- [ ] **Step 5: Verify — Section-Reihenfolge**

```bash
grep -n "^## " CLAUDE.md
```

Expected (Reihenfolge):
```
## Verhalten
## Kontinuierliches Lernen
## Projektstruktur
## Routing-Table
## Wiki-Modus
```

- [ ] **Step 6: Commit**

```bash
git add CLAUDE.md
git commit -m "feat(claude-md-routing): add ## Routing-Table mit 9 Triggers + Edge-Cases-Block

Routing-Table ersetzt die in Task 4 entfernte On-Demand-Lektuere-Liste (Entscheidung A).
9 Trigger-Daten-Zeilen, 4 Spalten (Trigger/Lies-zusaetzlich/Skippe/Skill-Call).

Match-Regel: Hybrid (exakte Trigger strikt, eine Soft-Match-Ausnahme fuer bare Ticker,
Mehrfach-Match = Union). Edge-Cases-Block normiert 3 Faelle:
Trigger+Wiki-Union, Tippfehler-Rueckfrage, Bare-Symbol-Whitelist via STATE.md.

Position: zwischen ## Projektstruktur und ## Wiki-Modus.

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2 AC #7.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 7: CLAUDE.md — Add `## Pointer (Ausgelagertes)` Section am Fuß

**Files:**
- Modify: `CLAUDE.md` (Pointer-Section einfügen)

**Zweck:** Ausgelagerte Files referenzierbar machen (3 Pointer auf APPLIED-LEARNING, TOKEN-RULES, INSTRUKTIONEN).

- [ ] **Step 1: Pointer-Section am Ende der Datei einfügen**

Hänge an das Ende von `CLAUDE.md` (mit Leerzeile davor) an:

```markdown
## Pointer (Ausgelagertes)

| Datei | Zweck |
|-------|-------|
| `00_Core/APPLIED-LEARNING.md` | Tier-2-Arbeitsprinzipien + Pflege-Regeln + Historie |
| `00_Core/TOKEN-RULES.md` | Token-Effizienz-Regeln (Accessibility, kein Enforcement) |
| `00_Core/INSTRUKTIONEN.md` | Tier-3-Regeln (Scoring-Skalen, Workflows, §§) |
```

- [ ] **Step 2: Verify — Section-Header existiert**

```bash
grep -c "^## Pointer (Ausgelagertes)$" CLAUDE.md
```

Expected: `1`

- [ ] **Step 3: Verify — Genau 3 Daten-Zeilen in Pointer-Tabelle (AC #8)**

```bash
awk '/^## Pointer \(Ausgelagertes\)/,EOF' CLAUDE.md | grep -c "^| \`00_Core/"
```

Expected: `3`

- [ ] **Step 4: Verify — Alle 3 referenzierten Files existieren**

```bash
test -f 00_Core/APPLIED-LEARNING.md && echo "OK_APPLIED" || echo "MISSING"
test -f 00_Core/TOKEN-RULES.md && echo "OK_TOKEN" || echo "MISSING"
test -f 00_Core/INSTRUKTIONEN.md && echo "OK_INSTR" || echo "MISSING"
```

Expected: `OK_APPLIED`, `OK_TOKEN`, `OK_INSTR` (jeweils existent).

- [ ] **Step 5: Verify — Pointer-Section ist letzte Section**

```bash
grep -n "^## " CLAUDE.md | tail -1
```

Expected: Letzte Zeile zeigt `^## Pointer (Ausgelagertes)$`.

- [ ] **Step 6: Commit**

```bash
git add CLAUDE.md
git commit -m "feat(claude-md-routing): add ## Pointer (Ausgelagertes) am Fuss

3 Pointer auf ausgelagerte SSoT-Files (APPLIED-LEARNING, TOKEN-RULES, INSTRUKTIONEN).
Position: letzte Section in CLAUDE.md (Inhaltsverzeichnis-Logik).

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2 AC #8.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 8: Acceptance-Verifikation gegen Spec v0.2

**Files:**
- Read-only: `CLAUDE.md`, `00_Core/APPLIED-LEARNING.md`, `00_Core/TOKEN-RULES.md`
- Tool: `03_Tools/system_audit.py` (read-only Smoke)

**Zweck:** Alle 11 Acceptance-Kriterien mechanisch nachweisen. Falls ein AC fehlschlägt → STOP, Bug-Hunt-Pass durchführen, ggf. Tasks 4-7 nachbessern.

- [ ] **Step 1: AC #1 — Line-Count ≤80**

```bash
wc -l CLAUDE.md
```

Expected: `≤ 80 CLAUDE.md` (Ziel ~70-76, Toleranz +10).

Falls >80: Identifiziere überflüssige Leerzeilen oder Wiederholungen, kürze. Falls strukturell zu groß → Hinweis im AC-Report (zur Spec-Revision).

- [ ] **Step 2: AC #2 — Section-Reihenfolge korrekt**

```bash
grep -n "^# \|^## " CLAUDE.md
```

Expected (in dieser Reihenfolge, exakte Line-Nrn variieren):
```
1:# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt
NN:## Verhalten
NN:## Kontinuierliches Lernen
NN:## Projektstruktur
NN:## Routing-Table
NN:## Wiki-Modus
NN:## Pointer (Ausgelagertes)
```

- [ ] **Step 3: AC #3 — Token-Effizienz-Section vollständig entfernt**

```bash
grep -c "^## Token-Effizienz" CLAUDE.md
```

Expected: `0`

- [ ] **Step 4: AC #4 — Applied Learning Sub-Section vollständig entfernt**

```bash
grep -c "^### Applied Learning" CLAUDE.md
grep -c "Subagents nur für Code+Tests" CLAUDE.md
```

Expected: jeweils `0` (Heading + Bullet-Text beide weg).

- [ ] **Step 5: AC #5 — APPLIED-LEARNING.md existiert mit allen Pflichten**

```bash
test -f 00_Core/APPLIED-LEARNING.md
head -8 00_Core/APPLIED-LEARNING.md | grep -c "^name: \|^description: \|^type: \|^updated: "
grep -c "^- " 00_Core/APPLIED-LEARNING.md
grep -c "Proaktive Pflege\|Kurator-Regel\|Promotion-Logik\|## Historie" 00_Core/APPLIED-LEARNING.md
```

Expected: File exists, Frontmatter-Felder `4`, Bullets `12`, Pflege+Promotion+Historie ≥`4`.

- [ ] **Step 6: AC #6 — TOKEN-RULES.md existiert mit allen Pflichten**

```bash
test -f 00_Core/TOKEN-RULES.md
head -8 00_Core/TOKEN-RULES.md | grep -c "^name: \|^description: \|^type: \|^scope: \|^enforcement: \|^updated: "
grep -c "Accessibility-Hinweis" 00_Core/TOKEN-RULES.md
grep -c "^- \*\*" 00_Core/TOKEN-RULES.md
```

Expected: File exists, Frontmatter-Felder `6`, Accessibility-Hinweis `1`, Regel-Bullets `6`.

- [ ] **Step 7: AC #7 — Routing-Table 9 Trigger-Daten-Zeilen + Edge-Cases-Block**

```bash
awk '/^## Routing-Table/,/^## Wiki-Modus/' CLAUDE.md | grep -E "^\| (\`|Wiki-Ops|Konsolidierungstag|Strategie)" | wc -l
awk '/^\*\*Edge-Cases der Match-Regel:\*\*/,/^## Wiki-Modus/' CLAUDE.md | grep -c "^- \*\*"
```

Expected: `9` Trigger-Daten-Zeilen, `3` Edge-Case-Bullets.

- [ ] **Step 8: AC #8 — Pointer (Ausgelagertes) genau 3 Daten-Zeilen**

```bash
awk '/^## Pointer \(Ausgelagertes\)/,EOF' CLAUDE.md | grep -c "^| \`00_Core/"
```

Expected: `3`

- [ ] **Step 9: AC #9a — Alte Headings raus aus CLAUDE.md**

```bash
grep -E "^## Token-Effizienz \(operativ\)|^### Applied Learning \(kuratiert" CLAUDE.md | wc -l
```

Expected: `0`

- [ ] **Step 10: AC #9b — Externe Anker-Links auf alte Sections existieren weiterhin nicht**

```bash
grep -rn "CLAUDE.md#applied-learning\|CLAUDE.md#token-effizienz" 00_Core/ 01_Skills/ 03_Tools/ "07_Obsidian Vault/" docs/ 2>/dev/null | wc -l
```

Expected: `0`

- [ ] **Step 11: AC #10 — Diff-Verifikation 1:1-Migration (Bullets identisch)**

```bash
# Applied Learning Bullets
grep "^- " /tmp/claude_md_pre_migration.md | head -12 > /tmp/old_al_bullets.txt
grep "^- " 00_Core/APPLIED-LEARNING.md > /tmp/new_al_bullets.txt
git diff --no-index --no-color /tmp/old_al_bullets.txt /tmp/new_al_bullets.txt
echo "AL-Diff exit: $?"

# Token-Effizienz Bullets
grep "^- \*\*" /tmp/claude_md_pre_migration.md | head -6 > /tmp/old_token_bullets.txt
grep "^- \*\*" 00_Core/TOKEN-RULES.md > /tmp/new_token_bullets.txt
git diff --no-index --no-color /tmp/old_token_bullets.txt /tmp/new_token_bullets.txt
echo "Token-Diff exit: $?"
```

Expected: beide diffs leer, beide exit `0`.

- [ ] **Step 12: AC #11 — Negative Scope (nur 3 Files modified)**

```bash
git diff --name-only "$(git rev-parse HEAD~6)" HEAD
```

Expected: genau diese Pfade (Reihenfolge egal, aber keine anderen):
```
00_Core/APPLIED-LEARNING.md
00_Core/TOKEN-RULES.md
CLAUDE.md
```

Falls weitere Files geändert wurden: STOP, AC #11 verletzt — Revert oder Erklärung im AC-Report.

Hinweis: `HEAD~6` adressiert den Commit unmittelbar vor Task 2 (Plan-Commit). Hintergrund: 6 substantive Task-Commits (Task 2 + 3 + 4 + 5 + 6 + 7). Marker-Commit (Step 15) folgt erst nach diesem Schritt. Falls Zwischen-Fixes nötig waren und die Commit-Zahl differiert, per `git log --oneline -20` den richtigen Baseline-Hash ermitteln und ersetzen.

- [ ] **Step 13: Smoke-Test — system-audit `--minimal-baseline`**

```bash
python 03_Tools/system_audit.py --minimal-baseline
echo "Exit: $?"
```

Expected: `3/3 PASS`, exit `0`. Sicherstellt, dass das system_audit-Tool nicht durch CLAUDE.md-Änderungen verwirrt ist (Check-1 jsonl_schema, Check-6 pipeline_ssot, Check-7 log_lag bleiben PASS).

- [ ] **Step 14: Cleanup Snapshot-Dateien**

```bash
rm -f /tmp/claude_md_pre_migration.md /tmp/old_applied_learning_block.md /tmp/old_token_eff_block.md /tmp/old_bullets.txt /tmp/new_bullets.txt /tmp/old_token_bullets.txt /tmp/new_token_bullets.txt /tmp/old_al_bullets.txt /tmp/new_al_bullets.txt
```

Expected: keine Output (rm -f ist silent bei Nicht-Existenz).

- [ ] **Step 15: Final-Commit (AC-Report) — wenn alle 11 AC PASS**

Falls alle AC PASS: kein Code-Commit nötig (alles bereits aus Tasks 2-7 committed). Stattdessen ein leerer Marker-Commit mit AC-Report-Zusammenfassung:

```bash
git commit --allow-empty -m "verify(claude-md-routing): Tier-1 AC-Report — 11/11 PASS

AC #1 (Line-Count ≤80): PASS
AC #2 (Section-Reihenfolge): PASS
AC #3 (Token-Effizienz raus): PASS
AC #4 (Applied Learning raus + Kontinuierliches Lernen geschrumpft): PASS
AC #5 (APPLIED-LEARNING.md komplett): PASS
AC #6 (TOKEN-RULES.md komplett): PASS
AC #7 (Routing-Table 9 Zeilen + Edge-Cases): PASS
AC #8 (Pointer 3 Zeilen): PASS
AC #9a (alte Headings raus): PASS
AC #9b (externe Anker existieren weiterhin nicht): PASS
AC #10 (Diff 1:1 Bullets identisch): PASS
AC #11 (Negative Scope nur 3 Files): PASS

Smoke: system_audit --minimal-baseline 3/3 PASS.

Spec: docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md v0.2.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

Falls einzelne AC FAIL: STOP, kein Marker-Commit. Stattdessen FAIL-Liste an User reporten + Korrektur-Tasks vorschlagen.

---

## Post-Implementation Follow-ups (NICHT Teil dieses Plans)

- **Codex-Reconciliation-Pass** (Memory `feedback_review_stack.md`): Nach AC-Report-Commit Spec + Plan + Implementation gegen Memory-Drift prüfen.
- **CodeRabbit-Pass:** Weniger relevant (Markdown-Refactor, kein Code), aber inverted-Sequenz für Refactor-Sicherheit erwägen.
- **Vault-Update-Sweep:** `07_Obsidian Vault/.../wiki/concepts/CLAUDE-md-Konstitution.md` strukturell aktualisieren (separate Aufgabe, nicht spec-blockierend).
- **STATE.md-Pipeline-SSoT-Update:** Tier-1-Refactor als ✅ DONE eintragen.
- **CORE-MEMORY.md §1-Eintrag:** Meilenstein „CLAUDE.md Routing-Refactor Tier 1 deployed".
- **Tier 2 STATE-Split (Variante B Hub):** Eigene Brainstorm-Session, separates Spec.
