# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-21 Mittag (**Pivot zu Systemhygiene-TOP-Priority** nach Entdeckung massiverer Drift als vermutet: 12/27 Records silent defcon-Drift + CORE-MEMORY-Header-Stand-Drift + Pipeline-SSoT-Lücke)
**Für nächste Session:** **Phase A+B+C+D+E+F in dieser Reihenfolge** (komplette Systemhygiene-Welle + Audit-Tool-Bau + Provenance-Plan-Execution, noch in time für TMO Q1 am 23.04.)

---

## 🎯 WICHTIGSTE AUSSAGE ZUERST

Heute wurde durch einen Pre-Check entdeckt, dass **„Systemhygiene" und „Drift-Check" in den letzten 3 Tagen selektiv statt exhaustive durchgeführt wurden.** Konkret 12 von 27 Records silent schema-inkonsistent (alle defcon_level-Drift seit 18.04.-Threshold-Migration), CORE-MEMORY-Header stale, Pipeline-Aufgaben über 4+ Quellen fragmentiert statt als SSoT.

User-Mandat: **„Nichts darf vergessen werden. Alles up-to-date halten. WIRKLICH das gesamte System nachziehen."**

**Externes Tool `codebase-memory-mcp` wurde evaluiert und verworfen** — löst Code-AST-Index-Problem, nicht unser Markdown/YAML/JSONL-Drift-Problem. Externer SQLite-Cache wäre zusätzliche Drift-Quelle (Ironie).

**Konsequenz:** Internes `03_Tools/system_audit.py` bauen + Slash-Command `/SystemAudit` + STATE.md-Section „Last Audit", aber **zuerst manueller Sync-Sweep** (sonst baut das Tool gegen kaputte Baseline).

---

## 🚀 NÄCHSTE SESSION — Sequenzielle Primär-Pipeline

### Phase A: CORE-MEMORY nachziehen (~15 Min)

**Warum:** Header sagt `Stand: 17.04.2026` — real ist 21.04. Letzter §1-Eintrag ist 20.04. Nacht-Spät; heutige Events (21.04. Drift-Migration, Provenance-Spec+Plan, §27.4-Schärfung) fehlen vollständig.

Schritte:
1. `00_Core/CORE-MEMORY.md` Header-Zeile `**Stand:**` auf `21.04.2026 Mittag` setzen
2. §1 System-Meilensteine drei neue Einträge am Ende der Tabelle anfügen:
   - **21.04.2026 Mittag — Drift-Migration score_history.jsonl 12/27 → 27/27** (commit `ca76114`): Pre-Check vor Provenance-Gate-Plan-Execution deckte 12 Records silent defcon-Drift seit 18.04.-Threshold-Migration auf. `migrate_defcon_drift.py` idempotent + atomar, 12 defcon_level-Korrekturen (Score 71-76 D4→D3, Score 61-63 D3→D2). Snap-to-Schema erfolgreich; re-validate 27/27 PASS. Zeile 25 V_vollanalyse 17.04. 72/D4→D3 = genauer Auslöser-Fall der Provenance-Spec.
   - **21.04.2026 Mittag — Score-Append Provenance-Gate Spec + Plan v2 ratifiziert** (commit `206c0a1`): Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md` Architektur-Variante E (Hybrid Pipeline-Gate B + reduzierter Schema-Guard D) nach 5 Codex-Sparring-Runden. Plan v2 mit 4 Codex-Patches: Task 0 Pre-Execution-Baseline-Check + Task 2 Step 2.7 Re-Validate-Sweep + Task 3 Step 3.1a-d Granularitäts-Split + Task 6 CORE-MEMORY-§10-Timing-Fix. 7 Tasks, 40 Steps, First-Live-Test geplant TMO Q1 23.04.
   - **21.04.2026 Mittag — §27.4 Vertikal-Drift-Klausel + Applied Learning 12/20 + Systemhygiene-Pivot:** INSTRUKTIONEN §27.4 um „Zweite Klasse — Vertikal-Drift (Schema-Migration auf Altdaten)" erweitert mit Präzedenzfall 21.04.2026. CLAUDE.md Applied Learning v2.4 Bullet 12/20 („Drift-Check = exhaustive Schema-Validation aller Records, nicht Spot-Check"). Memory `feedback_exhaustive_drift_check.md` NEU (Tier 1, Index 13/13). Systemhygiene zu TOP-Priority gemacht — interner System-Audit-Tool-Bau in nächster Session.

3. §10 API-Audit-Log einen neuen Eintrag anfügen:
   - **2026-04-21 Mittag — Drift-Audit-Sweep Ergebnis:**
     - score_history.jsonl: 12 FAIL (alle defcon_level-Drift) → migriert → 27/27 PASS
     - flag_events.jsonl: 2/2 PASS
     - config.yaml Satelliten Score+DEFCON: 11/11 == STATE.md
     - portfolio_returns.jsonl + benchmark-series.jsonl: je 1 Record (17.04.), **stale seit 4 Tagen** (R5-Phase-3 „aktiv" laut STATE.md aber Daily-Append-Cron existiert nicht; Manual-Trigger-Pflicht vergessen; Track-4-Backlog-Item)
     - **Systemweiter Audit NICHT durchgeführt** (Markdown-Cross-Source, Existence-Check, Skill-Versions, Vault-Backlinks, docs/superpowers-vs-STATE-Referenzen) — das macht erst `system_audit.py` in Phase E.

4. Falls §3 Aktive Positions-Entscheidungen „Stand: 04.04.2026 — pre-v3.7"-Label **bewusst historisch** ist (wahrscheinlich, da sie den pre-v3.7-Zustand dokumentieren): Label auf `Historisch, pre-v3.7 — aktuelle Positions-Realität in STATE.md + Faktortabelle.md` schärfen. Falls nicht historisch gedacht: nachziehen auf aktuellen Stand.

### Phase B: SESSION-HANDOVER-Nacharbeit + log.md (~10 Min)

**Warum:** Dieser Handover-Stand ist nach Phase A+C technisch nicht mehr aktuell — Header dann alt, weil A+B+C durchgeführt. Aber Phase B ist trivial, weil dieser Handover bereits der neue Zustand ist.

Schritte:
1. Nach Phase A+C und Phase D-Start: kleiner Handover-Update „A+B+C completed, D in progress".
2. Wiki `log.md` Eintrag für die Sync-Welle (analog zu heutigem drift-migration-Eintrag, aber für „A+B+C Sync-Welle post-Drift-Migration").

### Phase C: STATE.md Pipeline-SSoT-Section (~15 Min)

**Warum:** User hat eine 7-Punkte-Pipeline-Übersicht synthetisiert, die nirgendwo zentral lebt. Fragmentiert über STATE.md + SESSION-HANDOVER.md + Plan-Files + Memory. Jedes Mal rekonstruieren wir das aus 4 Quellen — genau der Anti-Pattern unserer Lesson.

Schritte: in `00_Core/STATE.md` nach „Nächste kritische Trigger (30 Tage)"-Section eine neue Section `## 🗺 Aktive Pipeline (SSoT)` einfügen, strukturiert als:

```markdown
## 🗺 Aktive Pipeline (SSoT)

### 🔴 Unmittelbar / Primär-Track
1. **Morning Briefing v3.0.4 Hotfix** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, ~90 Min). Prod läuft v2.1 (Rollback nach Halluzinations-Incident 20.04.). Hotfix ergänzt §3a Anti-Fallback-Guard + neuer Test T5 Adversarial-Stale-Shibui. Gate A erst nach v3.0.4-PASS.
2. **Score-Append Provenance-Gate** — Plan v2 `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. Critical vor TMO Q1 23.04. (erster echter Forward-Run durch neue Pipeline mit P3.5 fail-close).
3. **System-Audit-Tool `03_Tools/system_audit.py`** — Sub-Spec + Plan in dieser Session (siehe Phase D+E).

### 🟠 Portfolio — Kritische Triggers 10 Tage
- **23.04. TMO Q1** — D2-Entscheidung + fcf_trend_neg Resolve-Gate. Erster Live-Test Provenance-Gate + §4-Router Status-Matrix B1-B24 + backtest-ready-forward-verify.
- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal?)
- **29.04. MSFT Q3 FY26** — FLAG-Review CapEx/OCF

### 🟡 Bereit, wartet auf Gate A (~24.04. frühestens nach v3.0.4-Deploy)
4. **Track 5a SEC EDGAR Skill-Promotion** — Plan `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks). Re-Validation-Check nach 6-Paper-Ingest B21-B24 möglicherweise nötig.
5. **Track 5b FRED Macro-Regime-Filter** — Plan `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks). User-Aktion vor Start: FRED-API-Key registrieren. B19 (LLM-Regime-Shift-Bias) stärkt wissenschaftliche Begründung.

### 🔵 Deferred / Explizit zurückgestellt
6. **v3.1 Cache-Refactor** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md`. Trigger: „262s im Alltag stört" oder „>400s-Alert wiederholt".
7. **Track 4 ETF+Gold-Erweiterung** — Blockiert auf User-Input (ETF-Ticker IWDA.AS/SWDA.L/EUNL.DE? Gold-Ticker SGLD.DE/4GLD.DE/GC=F?). Gleichzeitig **Open-Backlog-Item Daily-Persist-Stale** auflösen (portfolio_returns.jsonl seit 4 Tagen stale).
8. **KG-Roadmap v0.1** — `draft-frozen`. Re-Review-Trigger: Cross-Entity-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17.

### ⏰ Long-Term-Gates
- **AVGO OpenInsider Manual-Check** — vor FLAG-Aktivierung (Watch aktiv, kein Termin)
- **Tavily Dev-Key Rotation** — innerhalb 7 Tagen nach Prod-Deploy v3.0.4 (~bis 28.04. falls Deploy am 22.04.)
- **Track 5a 90-Tage-Audit** — 2026-07-19
- **Score-Archiv-Interim-Gate** — 2026-10-17
- **R5 Interim-Gate** — 2027-10-19
- **Review-Gate §29.6** — 2028-04-01
```

**Pflege-Pattern (nach Aufbau):** Diese Section ist Pflicht-Update bei jedem Plan-Commit + jedem Gate-Passage. §18 Sync-Pflicht-Liste erweitert um diese Section.

### Phase D: Sub-Spec für `system_audit.py` (~60 Min)

**Ablauf:** Brainstorming-Skill → Spec → Codex-Review → Ratifikation.

**Scope (Codex-aligned Quality-Gates):**
- **Kern (Pflicht):**
  - JSONL Schema-Validation (alle 4 Stores `score_history` + `flag_events` + `portfolio_returns` + `benchmark-series` gegen Pydantic-Schemas wo vorhanden; strukturelle Keys-Konsistenz wo kein Schema)
  - Markdown Header-Stand-Drift (`Stand:`-Feld in STATE.md + CORE-MEMORY.md + Faktortabelle.md vs neueste §1/§10/Entry-Datum — bei Differenz >2 Tage FAIL)
  - Cross-Source Score/DEFCON/Sparrate (STATE.md ↔ Faktortabelle.md ↔ config.yaml ↔ Vault-Entities)
  - Existence-Check (alle in CLAUDE.md/STATE.md/Handover referenzierten Pfade müssen existieren)
  - Skill-Version `01_Skills/*/SKILL.md` frontmatter `version:` vs `06_Skills-Pakete/*.zip`-Name-Pattern
  - Pipeline-SSoT-Consistency (alle Pläne in `docs/superpowers/plans/` müssen in STATE.md-Pipeline-SSoT referenziert sein; Reverse: alle Referenzen in STATE.md-Pipeline müssen existierende Plan-Files sein)
  - log.md letzter Eintrag Datum vs neuester git-commit-Datum (max 1 Tag Lag)
- **Optional (mit Timeout):**
  - Vault-Backlink-Integrity (130 Notes — separater Check mit Timeout/Caching; nicht im Standard-Run)
  - Obsidian B-Nummerierung Status-Matrix-Konsistenz
- **Output:** strukturiert `N/M PASS` + Kategorie-FAIL-Listen. Exit-Codes: 0 PASS / 1 FAIL / 2 IO-Fehler.
- **Invocation:** CLI `python 03_Tools/system_audit.py [--core | --full]` + Slash-Command `/SystemAudit` (Config über `.claude/`-Command-Datei).
- **STATE.md-Integration:** Section „Last Audit: YYYY-MM-DD HH:MM — N/M PASS" wird vom Tool selbst am Ende des Runs aktualisiert.

**Codex-bestätigte Anti-Pattern:**
- KEIN SessionStart-Hook (kollidiert mit CLAUDE.md SESSION-INITIALISIERUNG „zuerst nur STATE.md lesen")
- KEIN Pre-Commit-Hook als Default (Friction-Risiko; optional später als opt-in)
- SessionEnd-Hook höchstens als leichter Warnung-Hinweis, nicht Voll-Audit

### Phase E: Plan + Build Audit-Tool (~90-120 Min)

**Ablauf:** writing-plans-Skill → Plan-File → Subagent-Driven Execution oder Inline.

**Erwartete Struktur (geschätzt):**
- Task 0: Test-Fixtures-Setup + CLI-Skeleton
- Tasks 1-7: ein Task pro Kern-Check (je TDD: failing test → min impl → green → commit)
- Task 8: Aggregator + Strukturiertes Report-Format
- Task 9: Slash-Command `.claude/commands/SystemAudit.md` + STATE.md-Last-Audit-Section-Writer
- Task 10: (Optional) Vault-Backlink-Subcommand mit Timeout
- Task 11: First-Run gegen aktuelles Repo → baseline

**Nach Phase E Ende:** `/SystemAudit` läuft, STATE.md hat initiale „Last Audit"-Zeile.

### Phase F: Provenance-Plan Execution (~60-90 Min)

**Ablauf:**
1. `/SystemAudit` laufen lassen — Pre-Check analog Task 0 im Provenance-Plan.
2. Falls PASS: Subagent-Driven oder Inline-Execution des Provenance-Plans (docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md).
3. Plan enthält 4 Codex-Patches: Task 0 Baseline-Check + Step 2.7 Re-Validate-Sweep + Task 3.1a-d Granularitäts-Split + Task 6 CORE-MEMORY §10 Timing-Fix.
4. Nach Plan-Completion (alle 6 Task-Commits): `/SystemAudit` erneut für Verifikation.

**Erwartete Artefakte nach Phase F:**
- `03_Tools/backtest-ready/versions.py` (SSoT DEFCON_ACTIVE_VERSION)
- `03_Tools/backtest-ready/provenance_gate.py` (Schicht B, 8 Checks, 9 Smoke-Tests)
- `03_Tools/backtest-ready/schemas.py` erweitert (Schicht D Block-Coverage-Validator)
- `01_Skills/backtest-ready-forward-verify/SKILL.md` mit Phase P3.5
- `01_Skills/backtest-ready-forward-verify/_smoke_test.py` mit Case 7 Integration-Test
- STATE.md + INSTRUKTIONEN §18 + CORE-MEMORY §10 Go-Live-Einträge

### Phase G: TMO Q1 23.04. — First-Live-Run

Natürlicher Trigger. Full Pipeline end-to-end: P1→P2a→P2b→**P3.5 NEU** (8 Checks fail-close)→P3 (Δ-Gate fcf_trend_neg-Resolve)→P4/P5/P6. Zweiter CORE-MEMORY §10-Eintrag mit konkretem Result folgt.

---

## 📊 VOLLSTÄNDIGE AGENDA-INVENTUR (Stand 21.04.2026 Mittag)

### Aktive Pläne in `docs/superpowers/plans/`
| Plan-File | Status | Tasks | Blocker |
|---|---|---|---|
| `2026-04-20-briefing-v3.0.4-hotfix.md` | ready for execution | 13 | keiner, nur Priorität (verschoben wegen v2.1-Stabilität post-Incident) |
| `2026-04-21-score-append-provenance-gate.md` | v2 ready (Codex-patched) | 7 Tasks 40 Steps | pending Systemhygiene-Sweep (Phase A-E) |
| `2026-04-20-track5a-edgar-skill-promotion.md` | Codex-reviewed | 9 | pending Gate A (v3.0.4 3-Tage-Stabilität) + optionale Re-Validation-Check nach 6-Paper-Ingest |
| `2026-04-20-track5b-fred-regime-filter.md` | Codex-reviewed | 15 | User-Aktion FRED-API-Key + pending Gate A |
| `2026-04-20-briefing-v3.1-cache-refactor.md` | deferred | — | Trigger: 262s stört im Alltag / >400s-Alert wiederholt |

### Heute NEU geschrieben
| Datei | Status | Kontext |
|---|---|---|
| `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md` | draft, commit `206c0a1` | Architektur-Variante E (Hybrid B+D), 5 Codex-Sparring-Runden |
| `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` | v2, commit `206c0a1` | 4 Codex-Patches eingearbeitet |
| `03_Tools/backtest-ready/migrate_defcon_drift.py` | executed + committed `ca76114` | One-Shot-Tool idempotent, 12/27 → 27/27 |
| `00_Core/INSTRUKTIONEN.md §27.4` | erweitert commit `ca76114` | Vertikal-Drift-Klausel neu |
| `CLAUDE.md` Applied Learning 12/20 | commit `ca76114` | v2.4-Historie-Eintrag |
| Memory `feedback_exhaustive_drift_check.md` | NEU (Tier 1) | Exhaustive-Drift-Check-Regel |
| `07_Obsidian Vault/.../log.md` | Eintrag heute commit `ca76114` | Drift-Migration + System-Audit-Lesson |

### Heute NICHT geschrieben (aber entschieden für nächste Session)
- Sub-Spec `docs/superpowers/specs/2026-04-22-system-audit-tool-design.md` (Phase D)
- Plan `docs/superpowers/plans/2026-04-22-system-audit-tool.md` (Phase E)
- Tool selbst `03_Tools/system_audit.py` + Slash-Command `.claude/commands/SystemAudit.md` (Phase E)
- `00_Core/CORE-MEMORY.md` 21.04. Sync (Phase A — siehe oben für genaue Schritte)
- `00_Core/STATE.md` Pipeline-SSoT-Section (Phase C — siehe oben für Struktur)

### Open Backlog (aus STATE.md + heutigem Audit)
1. **Daily-Persist seit 4 Tagen stale** — `portfolio_returns.jsonl` + `benchmark-series.jsonl` je 1 Record (17.04.). R5-Phase-3 „aktiv" aber Daily-Append-Cron existiert nicht. Auflösung: in Track 4 mit ETF/Gold-Erweiterung + Cron-/Hook-Mechanismus.
2. **System-Audit-Tool fehlt** — wird Phase D+E nachgeholt.
3. **Codex Round 2 für Tavily-Spec** (stand als PENDING vor v3.0.4-Hotfix-Plan) — überholt durch v3.0.4-Plan der dieselbe Spec überarbeitet. **Status: formal erledigt.**

---

## 🧠 HEUTIGE LESSONS LEARNED (persistent)

1. **„Drift-Check" = exhaustive, nicht Spot-Check.** Applied Learning 12/20. Memory `feedback_exhaustive_drift_check.md`. §27.4 Vertikal-Drift-Klausel. Trigger: bei „Hygiene"/„Drift"-Wortwahl + bei jedem Schema-/Threshold-Migration-Commit Re-Validate-Sweep über alle persistierten Stores.

2. **Pain-Point-Driven Self-Improvement schlägt Meta-Framework.** Externe Tools (codebase-memory-mcp) lösen oft andere Problemklasse + erzeugen eigene Drift-Flächen (externer SQLite-State). Domain-spezifische interne Helper-Skripte (~200-300 LOC) sind präziser.

3. **Horizontal-Drift + Vertikal-Drift sind verschiedene Klassen:**
   - Horizontal: Multi-Source-SSoT-Divergenz (§27.4 ursprünglich, INSTRUKTIONEN/CORE-MEMORY/config.yaml/Vault-Entities erzählen unterschiedliche Stories)
   - Vertikal: Schema-Migration tickt vorwärts, Altdaten bleiben silent inkonsistent (§27.4 neue Klausel 21.04.)
   - **Beide brauchen exhaustive Sweep, nicht Spot-Check.**

4. **Sequenzierungs-Entscheidungen sind Evidenz-abhängig.** Codex empfahl β (Provenance zuerst) basierend auf dem Stand vor CORE-MEMORY-Header-Drift-Entdeckung. Mit neuer Evidenz war γ (Systemhygiene zuerst) richtig. Codex-Verdikte sind nicht lock-in — bei neuer Evidenz Re-Evaluation.

5. **SessionStart-Hooks für Systemchecks kollidieren mit CLAUDE.md SESSION-INITIALISIERUNG** (Pflicht „zuerst nur STATE.md lesen"). Slash-Commands sind sauberer.

---

## 📚 REFERENZEN (heute Session-relevant)

### Git-Commits 21.04.2026 Mittag
- `ca76114` drift-migration+system-hygiene — 6 files, 140 insertions
- `206c0a1` plan+spec(provenance-gate) — 2 files, 1524 insertions (force-added trotz .gitignore docs/superpowers)

### Memory-Files (user's ~/.claude/projects/.../memory/)
- `feedback_exhaustive_drift_check.md` NEU — exhaustive Validation-Regel
- `MEMORY.md` Index auf 13 topic files aktualisiert

### Codex-Runden heute
- **Codex Run 1 (Plan-Review):** YELLOW auf 4 Punkte — alle adressiert (Task 0 + Step 2.7 + 3.1a-d Split + Task 6 §10 Timing)
- **Codex Run 2 (Audit-Strategie):** Sequenzierung β, Automatismus Slash-Command + STATE.md-Section, Memory-Promotion §27.4-Schärfung statt neuer §, Audit-Tool-Risiko = Scope-Creep. Empfehlung dann durch User-CORE-MEMORY-Drift-Entdeckung auf γ revidiert.

### Externe Tool-Evaluation (verworfen)
- `github.com/DeusData/codebase-memory-mcp` — falsche Scope (Code-AST statt Markdown/YAML/JSONL), externer SQLite-Cache = neue Drift-Quelle, Windows-SmartScreen-Install-Friction. Internes `system_audit.py` präziser.

---

## ▶️ TRIGGER NÄCHSTE SESSION

```
Session starten
```

1. Claude liest `STATE.md` (wird post-Phase-C aktualisiert sein durch diese Session-Arbeit)
2. Wechsel hierher
3. **Phase A starten** — CORE-MEMORY-Header + §1 + §10 nachziehen (~15 Min)
4. **Phase B** — log.md + kleiner Handover-Hinweis (~10 Min)
5. **Phase C** — STATE.md Pipeline-SSoT-Section einbauen (~15 Min)
6. Nach A+B+C: einen Sync-Commit (analog `ca76114`-Pattern)
7. **Phase D** — System-Audit-Tool Sub-Spec mit Brainstorming-Skill (~60 Min)
8. **Phase E** — Plan + Build mit writing-plans-Skill (~90-120 Min)
9. **Phase F** — Provenance-Plan-Execution (~60-90 Min)
10. **Phase G am 23.04.** — TMO Q1 First-Live-Run (natürlicher Trigger)

**Bei Abweichung:** Portfolio-Ereignis (Earnings-Beat/Miss), Markt-Bewegung, oder User-Interrupt → Flex-Routing, aber A+B+C bleiben Pflicht vor Tool-Bau.

---

## ⚠️ OPEN RISKS / REMINDERS

1. **TMO Q1 am 23.04.** — Erster echter Live-Test aller neuen Infrastruktur. Bei Tool-Bau-Verzögerung muss spätestens Mi 22.04. Abend Provenance-Plan durchgelaufen sein.
2. **v3.0.4 Briefing-Hotfix bleibt pending** — v2.1 Prod läuft stabil (heute morgen Stale-Shibui-Konstellation sauber durchlaufen). v3.0.4 kann nach Audit-Tool in einer eigenen Session.
3. **Tavily Dev-Key Rotation** — ab v3.0.4-Deploy-Datum läuft 7-Tage-Uhr (`tvly-dev-4PYXp...`).
4. **Track 4 ETF/Gold-Input** — User-Decision weiter ausstehend; auflösen in einer dedizierten Session.
5. **CORE-MEMORY §3 Stand 04.04.** — prüfen ob bewusst historisch oder Drift; Phase A Schritt 4.
6. **Multi-Source-Drift-Prevention §27.4 horizontal** — weiterhin Pflicht (unverändert); plus neue Vertikal-Klausel.

---

*Alles aus heutiger Session durable persistiert. Nichts schwebt im Speicher. Phase A-G klar sequenziert. TMO Q1 Deadline 23.04. erreichbar.*
