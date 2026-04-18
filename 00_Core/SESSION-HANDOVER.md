# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 19.04.2026 (nach Implementation + Deployment) | **Für:** Nächste Session (TMO Q1 am 23.04. als erster Real-Run)

---

## ▶️ TRIGGER

```
Session starten
```

Claude liest automatisch `00_Core/STATE.md` (Single-Entry-Point). Keine Plan-Datei mehr zu laden — Implementation-Session ist abgeschlossen, v3.7.2 operativ.

---

## ✅ LETZTE SESSION (19.04.2026, Implementation + Deployment + Full Audit) — ERLEDIGT

**Scope:** Plan `backtest-ready-forward-verify` → deployed + institutionalisiert. 12 Commits, keine Portfolio-Änderungen (reine Infrastruktur + Doku-Sync).

### Kernergebnisse

**1. Skill `backtest-ready-forward-verify` (v1.0) deployed — Forward-Run Pipeline-Kapsel**

Pipeline P1-P6: Draft-Read → Freshness-Warn → STATE.md-Tripwire → §28.2 Δ-Gate (conditional) → Dry-Run → Real Append → git add. Stdout-Report mit 6 Fällen: OK / freshness / PFLICHT / STOP / duplicate / FAIL. `trigger_words: []` — aktiviert sich **nur programmatisch** aus dynastie-depot Schritt 7. ZIP gepackt + in Claude Desktop installiert.

**Critical Files:**
- `01_Skills/backtest-ready-forward-verify/SKILL.md` (230 Zeilen Prosa)
- `01_Skills/backtest-ready-forward-verify/_smoke_test.py` (6 TDD-Cases, grün)
- `03_Tools/backtest-ready/_forward_verify_helpers.py` (4 Funktionen: `parse_wrapper`, `parse_state_row`, `build_migration_event`, `check_freshness`)

**2. Schema-Erweiterung `MigrationEvent` mit Self-Validators**

`ScoreRecord.migration_event: Optional[MigrationEvent] = None`. MigrationEvent-Felder: from_version, to_version, algebra_score, forward_score, delta (signed), outcome (Literal accepted/log_only/block). **Zwei self-validators** als defense-in-depth gegen Builder-Bugs (append-only → korrupt Record permanent):
- `_check_delta` — `delta == round(forward - algebra, 6)`
- `_check_outcome_bucket` — §28.2 Bucketing (|Δ|≤2 → accepted | 3-5 → log_only | >5 → block)

7/7 Smoke-Tests grün in `schemas.py`.

**3. dynastie-depot v3.7.1 → v3.7.2 (Schritt 7 delegiert)**

Kein DEFCON-Bump (§28.3 Nicht-Migration-Trigger — Scoring-Semantik unverändert v3.7). Schritt 7 ersetzt inline-`archive_score.py`-Aufruf durch:

```
Skill(skill="backtest-ready-forward-verify", args="<pfad-zum-draft>")
```

plus 6-Fall-Stdout-Parser in dynastie-depot SKILL.md Schritt 7.

**4. Institutionalisierung**

- INSTRUKTIONEN §18 v1.7 (score_history.jsonl-Write via Skill orchestriert)
- CORE-MEMORY §1 Meilenstein 19.04.
- STATE.md System-Zustand + Header-Stand
- 5 Vault-Konzept-Pages (Score-Archiv / FLAG-Event-Log / Backtest-Ready-Infrastructure / Analyse-Pipeline / **DEFCON-System** v3.5→v3.7 Content-Update)
- 2 Vault-Synthese-Pages (index / Investing-Mastermind-Index)
- 1 Vault-Source-Page (dynastie-depot-skill — Monolith-Claim entfernt, Rechenbeispiel + Anker synchronisiert)
- CLAUDE.md + KONTEXT.md + `03_Tools/backtest-ready/README.md` + PIPELINE.md
- log.md 19.04. Session-Entry (§18-Pflicht)

**5. Reviews & Gates**

Pre-Gates A (git-Perf 34ms) + B (§-Citations §18/§27.4/§28.1/§28.2/§28.3) grün. Subagent-Driven-Development mit 2× Spec-Review + 2× Code-Quality-Review (1× Request-Changes, dann Re-Review approved). E2E-Verification 6 Szenarien: 5/6 ✓, 1 Gap (P2b fehlender Stopp-Vermerk) sofort gefixt.

### Commits (12)

```
33cdd74  feat(schema): MigrationEvent field on ScoreRecord
1bd50ac  feat(schema): MigrationEvent self-validating (delta + §28.2 bucket)
2f3e828  chore(backtest-ready): _drafts/ ordner + gitignore
7d43492  feat(skill): backtest-ready-forward-verify — Forward-Run Pipeline-Kapsel
7e0b021  docs(skill): clarify P4 bare-record write
603ea74  fix(skill): tighten (wrapper strict, P2b exact, porcelain, STOP float, assertion)
018257e  refactor(dynastie-depot): Schritt 7 delegiert (v3.7.1 → v3.7.2)
8b856b4  docs(core): skill backtest-ready-forward-verify institutionalisiert (§18/meilenstein/state)
2d97ba1  docs(skill): P2b explicit Stopp-semantik (E2E-review gap)
07431d0  docs: v3.7.2 version-sync (dynastie-depot header + 4 Vault concept pages)
44e94f0  docs: v3.7.2 skill-deployment propagation (CLAUDE/KONTEXT/PIPELINE/README/Vault)
6f6dced  docs(vault): DEFCON-System.md v3.5 → v3.7 content update (4-Fix-Tabelle)
```

### Deployment-Stand

- ✅ Beide ZIPs (backtest-ready-forward-verify + dynastie-depot_v3.7.2) gepackt + in Desktop-App installiert
- ✅ `06_Skills-Pakete/` nicht aktualisiert (alte `dynastie-depot_v3.7.1.zip` bleibt als Archiv-Referenz) — optional bei Gelegenheit nachziehen

---

## 🎯 NÄCHSTER FOKUS

### Priorität 1: TMO Q1 FY26 — erster Real-Run der Skill-Pipeline (23.04.2026)

**Doppelte Bewährungsprobe:**
1. **FLAG-Resolve-Gate `fcf_trend_neg`** — WC-Unwind + FCF-Recovery bestätigt → Disclosure bleibt Notiz; fehlende Reversibilität → FLAG-Trigger nachtragen (Option B aus 18.04.-Entscheidung greift dann nicht mehr).
2. **D2-Entscheidung** — Score 64 ±1 bestätigt = D2 weiter; Score <60 = Ersatzvorbereitung ZTS aktivieren; Score ≥65 = D3-Recovery.
3. **Skill-Pipeline-Live-Test** — dynastie-depot Schritt 7 soll Draft nach `_drafts/TMO_<datum>-<zeit>.json` schreiben, Skill invoken, Stdout-Report parsen. Erwartet: `OK record_id=2026-04-23_TMO_vollanalyse score=<N> defcon=<D>` + Exit 0. Bei unerwartetem STOP/FAIL: CORE-MEMORY §5 Befund loggen.

**Merke:** Bei `[freshness: ...]`-Warnung prüfen, ob Schritte 0-6 vollständig liefen. Bei `FAIL phase=P2b score drift`: Draft vs. STATE.md-Stand prüfen — STATE muss vor Skill-Invocation aktualisiert sein (Schritt 6 regulär).

### Priorität 2: Earnings-Trigger-Kette

| Datum | Ticker | Klasse | Aktion |
|---|---|---|---|
| **23.04.** | **TMO** | **B** | Q1 FY26 — s.o. |
| **28.04.** | **V** | **B** | Q2 FY26 — D2-Entscheidung (Technicals-Reversal bei Beat + Guidance-Bestätigung?) |
| 28.04. | SNPS / SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | Q3 FY26 — CapEx/OCF FLAG-Review (bereinigt <60% = Auflösung) |
| Mai | BRK.B / ZTS / PEGA | B | Q-Earnings + Slot-16-Kandidatur |

### Optionale Engine-Arbeit (nicht blockierend)

- `06_Skills-Pakete/dynastie-depot_v3.7.2.zip` + `backtest-ready-forward-verify.zip` als Deployment-Archiv ablegen (aktuell fehlen die v3.7.2-ZIPs dort, alte v3.7.1 noch vorhanden)
- Rebalancing_Tool_v3.4 Sparraten-Spalte (Nenner 8.0 → 35,63€) manuell nachziehen falls noch nicht geschehen

---

## 🧭 START-PROTOKOLL NÄCHSTE SESSION

1. `Session starten` → `STATE.md` wird gelesen (Nenner 8.0, 35,63€/17,81€, v3.7.2)
2. Bei TMO-Earnings (23.04.): `!Analysiere TMO` auslösen. Schritte 0-6 wie gewohnt.
3. Schritt 7: Draft-Wrapper bauen + Skill invoken. Stdout-Report-Parsing folgt 6-Fall-Tabelle aus dynastie-depot SKILL.md.
4. Sync-Commit alle 6 Dateien (§18).

---

## 🚫 WAS NICHT ZU TUN

- **Kein** inline-`archive_score.py`-Call mehr in Schritt 7 — Pfad geht jetzt ausschließlich über den Skill. Ausnahme: Backfill + manuelle Recovery nach partiellem P5-Abbruch (duplicate record_id).
- **Kein** `migration_event` von Hand in den Draft schreiben — wenn `skill_meta` gesetzt, baut der Skill den MigrationEvent selbst.
- **Kein** Append-Block bei `|Δ|>5` — Record wird trotzdem persistiert (Historie-Integrität). Nur Fan-Out über 7 Oberflächen wird blockiert.
- **Kein** Multi-File-Drift-Check via Skill (§27.4 bleibt Human-Gate am „fertig"-Punkt).
- **Kein** Re-Invoke nach `FAIL phase=P4 duplicate record_id` — manueller `git add 05_Archiv/score_history.jsonl` + direkter Sync-Commit.
- **Kein** DEFCON-Bump bei reinen Skill-Paket-Updates (§28.3 Nicht-Migration-Trigger-Regel).

---

## 📂 KRITISCHE DATEIEN (Navigation)

- **Entry:** `00_Core/STATE.md` — Portfolio + Watches + Trigger (Stand 19.04., v3.7.2)
- **Regeln:** `00_Core/INSTRUKTIONEN.md` (v1.9 + §18 v1.7) — §18 Sync-Pflicht (score_history.jsonl via Skill), §27.4 Multi-Source-Drift, §28.1 Migration-Checklist, §28.2 Δ-Tabelle, §28.3 Nicht-Migration-Trigger
- **Architektur:** `00_Core/KONTEXT.md` §11 — 4-Layer-Architektur (State/Narrative/History/Projection)
- **Lektionen:** `00_Core/CORE-MEMORY.md` §1 (Meilensteine ab 15.04., neuer Eintrag 19.04.), §5 (Scoring-Lektionen), §11 (Live-Verify-Protokoll)
- **Skill-Haupt:** `01_Skills/dynastie-depot/SKILL.md` (v3.7.2 — Schritt 7 delegiert)
- **Skill-Satellit:** `01_Skills/backtest-ready-forward-verify/SKILL.md` + `_smoke_test.py`
- **Tools:** `03_Tools/backtest-ready/` — schemas.py (15 Modelle, 6 Validators), archive_score.py + archive_flag.py (CLI), `_forward_verify_helpers.py` (Skill-Helpers), README.md
- **Archive:** `05_Archiv/score_history.jsonl` (27 Records) + `flag_events.jsonl` (2 Records)
- **Draft-Handoff:** `03_Tools/backtest-ready/_drafts/` (ephemer, gitignored)

---

## 🔬 System-Reife-Tracker

- v3.5 (16.04.): 85%
- v3.7 (17.04. Morgen): ~92%
- Backtest-Ready (17.04. Abend): ~95%
- Schema-SKILL-Aligned + Forward-Pipeline-bewährt (18.04. Abend): ~96%
- Scoring-Version-Migration-Workflow formalisiert (18.04. Nacht): ~97%
- Skill-Plan für Forward-Verify finalisiert (19.04. Morgen): ~97%
- **Skill deployed + institutionalisiert + Vault-Schuld geschlossen (19.04. Abend): ~98%** — Engine "fertig genug", Fokus-Shift auf Content
- Nach erfolgreichem TMO-Real-Run 23.04.: ~99% (empirische Validation der letzten Unsicherheit)

### Outstanding Engine-Arbeit

- Nur noch optionale Kosmetik (ZIP-Archive, Rebalancing_Tool-Spalte). **Kein blockierender Engine-Punkt mehr offen.** Ab hier: Content-Fokus — Earnings-Analysen, FLAG-Resolves, Slot-16-Suche.
