# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 19.04.2026 | **Für:** Nächste Session (Implementation)

---

## ▶️ TRIGGER

```
Session starten

Dann: Plan unter docs/superpowers/plans/2026-04-19-backtest-ready-forward-verify.md
laden und via superpowers:subagent-driven-development Task-by-Task abarbeiten.
Pre-Implementation-Gates (A: git-Performance, B: §-Citations-Audit) zuerst.
```

Claude liest automatisch `00_Core/STATE.md` (Single-Entry-Point). Danach Plan-File laden (Pfad oben).

---

## ✅ LETZTE SESSION (19.04.2026) — ERLEDIGT

**Kein Commit, reiner Planungs-Output.** Keine Portfolio-Änderungen — strategische Skill-Spec-Session via Superpowers.

### Kernereignisse

**1. Superpowers-Plan `backtest-ready-forward-verify` finalisiert**

Vollständiger Brainstorming → Writing-Plans-Durchlauf (superpowers v5.0.7) mit 4 Advisor-Reviews + 1 externem Reviewer-Feedback + 1 User-Post-Review mit 5 Beobachtungen.

**Plan-Datei:** `docs/superpowers/plans/2026-04-19-backtest-ready-forward-verify.md` (494 Zeilen, lokal per `.gitignore:18` — Projekt-Konvention "Superpowers docs nur lokal relevant").

**Design-Kern (Hard-Decisions):**
- **Scope:** Forward-Run only (Option A). Backfill + FLAG-Event-Studies bleiben CLI-direkt.
- **Trigger:** Auto-Aktivierung bei `!Analysiere` via dynastie-depot Schritt 7 — keine eigenen Trigger-Words.
- **Relation:** Standalone-Satelliten-Skill (~150-220 Zeilen), nicht Sub-Workflow von dynastie-depot.
- **Input-Vertrag:** Wrapper-Struktur `{record: ..., skill_meta: {expected_algebra_score, migration_from/to_version}}` — `record` = exakt `ScoreRecord`, `skill_meta` ephemer.
- **Schema-Bump:** neues `Optional[MigrationEvent]`-Feld auf `ScoreRecord` (from_version, to_version, algebra_score, forward_score, delta signed, outcome Enum).
- **Block-Semantik:** §28.2 `|Δ|>5` blockt **Fan-Out (7 Oberflächen)**, NICHT JSONL-Append. Record wird **immer** persistiert mit `outcome="block"`, Skill emittiert `STOP:`-Prefix auf stdout für dynastie-depot-Handler.
- **Drift-Check:** STATE.md-Tripwire only (1 Quelle), nicht 4-File-Matrix. Multi-File-Drift bleibt §27.4 Human-Gate.
- **Freshness-Gate:** 3 Required-Touch-Files {STATE.md, Faktortabelle.md, log.md} — CORE-MEMORY/config.yaml konditional ausgeklammert (Alert-Fatigue-Vermeidung).

**Pipeline P1-P6:** Draft-Read → Freshness → STATE-Tripwire → Δ-Gate → Dry-Run → Real-Append → git-add.

**6 Tasks:** Schema-Erweiterung (TDD, grün) → `_drafts/`-Ordner → Skill + Helpers → dynastie-depot Schritt 7 Delegation → §18/Meilenstein-Updates → E2E-Verification.

**2. Advisor-Korrekturen eingearbeitet (Plan-Revisionen)**

5 Runden Advisor-Feedback. Hauptumwürfe:
- Skill-Prosa ist nicht TDD-testbar → Smoke-Tests nur für deterministische Teile (Schema + Helpers + CLI-Invocations). E2E = qualitatives Urteil.
- `expected_algebra_score` ephemer in `skill_meta`, nicht im Schema (kein Bump für 1-2×/Jahr-Input).
- Wrapper-Struktur statt Strip-Pattern (strukturelle Trennung Record/Meta).
- STATE.md-Tripwire einzig statt 4-File-Matrix (Tautologie-Befund).
- Block → persistieren, nicht wegwerfen (Informationsverlust-Aversion + §28.2 korrekt gelesen).

**3. INSTRUKTIONEN unverändert** — kein §28-Update, nur Plan-Ebene. §18 + §27.4 + §28.2 werden im Skill point-linkt (§27.4-konform, keine Duplizierung).

### Was entstanden ist

- `docs/superpowers/plans/2026-04-19-backtest-ready-forward-verify.md` (lokal, 494 Z.)
- Keine Repo-Änderungen, keine Commits

---

## 🎯 NÄCHSTER FOKUS (Implementation-Session)

### Priorität 1: Skill `backtest-ready-forward-verify` — Implementation

**Workflow:**
1. `Session starten` → STATE.md lesen
2. Plan-File laden: `docs/superpowers/plans/2026-04-19-backtest-ready-forward-verify.md`
3. **Pre-Implementation-Gates** (im Plan dokumentiert):
   - Gate A: `time git status --porcelain` — <200ms? Sonst Freshness-Strategie re-evaluieren.
   - Gate B: §-Citations-Audit — §18/§26/§27.4/§28.2 im Plan gegen aktuelle INSTRUKTIONEN matchen.
4. `superpowers:subagent-driven-development` aufrufen — Fresh Subagent pro Task + Review zwischen Tasks.
5. 6 Tasks durcharbeiten (Task 1 Schema → Task 6 E2E). Committen pro Task wie im Plan spezifiziert.
6. Nach Task 6: erster Real-Run bei **TMO Q1 am 23.04.** (FLAG-Resolve-Gate) als echte End-to-End-Validation.

**Zeit-Estimate:** 2-4h fokussiertes Arbeiten (Tasks 1/2 klein, Task 3 Hauptaufwand, Tasks 4-6 Integration).

### Priorität 2: Earnings-Trigger (unverändert)

| Datum | Ticker | Klasse | Aktion |
|---|---|---|---|
| **23.04.** | **TMO** | **B** | Q1 FY26 — D2-Entscheidung + **fcf_trend_neg Resolve-Gate** (WC-Unwind? → Disclosure bleibt; sonst FLAG nachtragen) + **erster Real-Run des neuen Skills** |
| **28.04.** | **V** | **B** | Q2 FY26 — D2-Entscheidung (Technicals-Reversal bei Beat + Guidance?) |
| 28.04. | SNPS / SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | Q3 FY26 — CapEx/OCF FLAG-Review (bereinigt <60% = Auflösung) |
| Mai | BRK.B / ZTS / PEGA | B | Q-Earnings + Slot-16 |

---

## 🧭 START-PROTOKOLL NÄCHSTE SESSION

1. `Session starten` → `STATE.md` wird gelesen (Nenner 8.0, 35,63€/17,81€)
2. Implementation-Plan laden (Pfad oben)
3. Pre-Implementation-Gates laufen lassen
4. `superpowers:subagent-driven-development` aktivieren
5. Task 1 dispatchen

---

## 🚫 WAS NICHT ZU TUN

- **Kein** inline-Build des Skills aus dem Kopf — Plan ist single source, Abweichungen davon in CORE-MEMORY §5 loggen + Plan aktualisieren
- **Kein** TDD-Zyklus über SKILL.md-Prosa (Kategorien-Fehler, siehe Plan Task 3 "WICHTIG — Test-Philosophie")
- **Keine** `migration_event`-Felder in Alt-Records (bleiben `null` per Optional-Default)
- **Kein** Append-Block bei `|Δ|>5` — Record wird trotzdem persistiert, nur Fan-Out wird geblockt
- **Kein** Multi-File-Drift-Check im Skill (§27.4 bleibt Human-Gate)
- **Keine** Schema-Bumps für ephemere Skill-Inputs — Vertrag nutzt `skill_meta`-Wrapper

---

## 📂 KRITISCHE DATEIEN (Navigation)

- **Entry:** `00_Core/STATE.md` — Portfolio + Watches + Trigger
- **Plan:** `docs/superpowers/plans/2026-04-19-backtest-ready-forward-verify.md` (lokal, 494 Z.)
- **Regeln:** `00_Core/INSTRUKTIONEN.md v1.9` — §18 Sync-Pflicht, §27.4 Multi-Source-Drift, §28.1 Migration-Checklist, §28.2 Δ-Tabelle
- **Architektur:** `00_Core/KONTEXT.md` §11 — 4-Layer-Architektur
- **Tools-Base:** `03_Tools/backtest-ready/` — existierende Schemas + 2 Archive-CLIs (werden orchestriert, nicht umgebaut)
- **Archive:** `05_Archiv/score_history.jsonl` (27) + `flag_events.jsonl` (2)
- **Skill-Ziel:** `01_Skills/backtest-ready-forward-verify/` (wird angelegt)
- **Skill-Aufrufer:** `01_Skills/dynastie-depot/SKILL.md v3.7.1 → v3.7.2` (Schritt 7 wird delegiert)

---

## 🔬 System-Reife-Tracker

- v3.5 (16.04.): 85%
- v3.7 (17.04. Morgen): ~92%
- Backtest-Ready (17.04. Abend): ~95%
- Schema-SKILL-Aligned + Forward-Pipeline-bewährt (18.04. Abend): ~96%
- Scoring-Version-Migration-Workflow formalisiert (18.04. Nacht): ~97%
- **Skill-Plan für Forward-Verify finalisiert (19.04.): ~97% (Engine-Bau-Phase erreicht Sedimentierungs-Plateau)** — Implementation-Session treibt auf ~98% nach erfolgreichem TMO-Real-Run 23.04.

### Outstanding Engine-Arbeit

- **Skill-Implementation** (Priorität 1 nächste Session, 2-4h)
- Danach: Engine "fertig genug" — Fokus-Shift auf Content (Earnings-Analysen ab 23.04.)
