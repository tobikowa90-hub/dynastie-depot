# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-22 Spät-Nacht (**Phase E 19/19 DONE ✅**) — CR-Re-Run gegen `e3ba381` = 1 OOS-Nitpick, Closure-Commit `57bee6b`. Nächste Session = **Phase G (TMO Q1 23.04. 14:30 CEST)** mit **Pfad-2 Old-Pipeline** (Weekly-Limit 93%, Reset Do 22:00 CEST).
**Vorherige Aktualisierungen:** 2026-04-22 Spät — Task 19 + Fix-Welle E (`d7ecf71`/`e3ba381`) · 2026-04-22 Mittag — Tasks 15-18 (`486f2c1`/`fa238bf`/`ab7ae19`/`ca35f62` + Handover `51f5719`) · 2026-04-21 Nacht — Task 14 + Fix-Welle C+D (`ab6b3f5`).

> **Progress-Banner (Phase A-G):** ✅ A+B+C+D+E (Systemhygiene-Welle + Audit-Tool v1.0 + Acceptance-Matrix + CR-Reconciliation) · 🔵 F (Provenance-Plan-Execution) **deferred per Pfad 2** · ⏳ G (TMO Q1 23.04. 14:30 CEST Old-Pipeline) · ⏳ **Konsolidierungstag Fr 24.04.** (Backlog-Cleanup, keine Neu-Scopes).

---

## 🚀 NÄCHSTE SESSION — Phase G (TMO Q1) oder Konsolidierungstag

### Kontext-Konstanten

- **Weekly-Limit:** 93% bei Session-Ende 22.04. Spät-Nacht → Minimal-Modus bis Reset
- **Reset:** Donnerstag 23.04.2026 **22:00 CEST** → Full-Budget-Window öffnet
- **TMO Q1 Earnings:** Donnerstag 23.04.2026 **14:30 CEST** (8:30 AM ET, pre-market US + Conference-Call gleichzeitig, MarketBeat-verifiziert)
- **Pfad-2-Entscheidung (locked):** TMO-Analyse Do Nachmittag **Old-Pipeline** (Provenance-Plan nicht stemmbar im Minimal-Modus). TMO-Record im Old-Format archivieren, **Retro-Migration post-Reset** (Do Abend 22:00+ oder Fr)

### Direkter Einstieg: TMO Q1 (Do 14:30 CEST, Pre-Reset)

**Trigger:** `!Analysiere TMO` nach Earnings-Release

> **📋 Pre-Earnings-Briefing vorab erstellt:** [`02_Analysen/TMO_pre-earnings_2026-04-23.md`](../02_Analysen/TMO_pre-earnings_2026-04-23.md) — via `earnings-preview`-Skill am Vortag (22.04. Spät-Nacht). Enthält Consensus ($5,24 EPS / $10,86B Revenue), Beat-Track 4/4, Analysten-Sentiment 24/26 Buy, Quartals-Trajektorie FCF/ΔWC/OpInc für `fcf_trend_neg` Resolve-Gate + **Entscheidungs-Matrix Miss/In-Line/Beat**. **Morgen als Basis nutzen, nicht neu fetchen** (Token-Spar).

**Spezifische Gates für TMO:**
- **D2-Entscheidung:** Score 64 aktuell, Live-Forward-Lauf gegen Q1-Actuals
- **`fcf_trend_neg` Resolve-Gate:** FY25 FCF -13,4% YoY war schema-getriggert aber Option-B-dokumentiert (WC-Delta -1766M erklärt). Q1 = natürlicher Resolve-Gate:
  - **WC-Unwind + FCF-Recovery bestätigt** → Disclosure bleibt Notiz, kein FLAG
  - **Fehlende Reversibilität** → `fcf_trend_neg`-Trigger **nachtragen** via `archive_flag.py trigger`
- **Old-Pipeline-Archiv:** SKILL.md Schritt 7 (backtest-ready-forward-verify Skill) → Draft + §28.2 Δ-Gate + Append. KEIN Provenance-Gate (Pfad 2).

**Token-Minimal-Modus:**
- Single-Pass-Analyse, keine Subagent-Exploration
- Keine Code-Review-Pässe (Codex/CodeRabbit) für TMO — ist keine Code-Änderung
- Multi-Source-Drift-Check §27.4: minimal (STATE.md + Faktortabelle + CORE-MEMORY §4 vs. neuer Score)
- Sync-Welle: log.md + CORE-MEMORY §4 + Faktortabelle + STATE.md + `score_history.jsonl` (+ `flag_events.jsonl` bei FLAG-Trigger)

### Alternative: Phase F Provenance-Plan-Execution (Do Abend Post-Reset)

**Nur wenn User sagt „jetzt Phase F":** Plan `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks, 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. Dann danach **TMO-Retro-Migration** des Old-Pipeline-Records.

### Konsolidierungstag Fr 24.04. — Backlog-Cleanup-only

**Keine neuen Scopes.** 5 Items:
1. **Check-3 `markdown_header` future-date-exclude** — `03_Tools/system_audit/checks/markdown_header.py:51-63` `_newest_event_date_state` — Long-Term-Gates (2028-04-01, 2027-10-19, 2026-10-17) aus Event-Kandidaten ausschließen
2. **existence-Cleanup-Welle** — ~54 CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix (Tool-Aufräum, nicht einzeln)
3. **Nach (1)+(2):** §27.5-Guard von `--minimal-baseline` auf `--core` hochziehen + INSTRUKTIONEN-§-Kommentar-Update
4. **Morning-Briefing v3.0.4-Hotfix** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, ~90 Min). Prod läuft Rollback v2.1.
5. **Tavily Dev-Key Rotation** — Key `tvly-dev-4PYXp...` im Dashboard rotieren (7-Tage-Uhr war an v3.0.4-Prod-Deploy gekoppelt; Key-Safety aber auch jetzt prüfen)
6. **Optional:** TMO-Retro-Migration falls Do Abend nicht erledigt + Daily-Persist-Auto-Hook-Baustein (Track 4)

---

## 🔍 Lageprüfung Session-Start

```bash
cd "C:\Users\tobia\OneDrive\Desktop\Claude Stuff"
python 03_Tools/system_audit.py --minimal-baseline   # 3/3 PASS, rc=0
git log --oneline 57bee6b..HEAD                       # Zeigt neue Commits seit Phase-E-Closure
```

STATE.md Banner sagt: „Phase E 19/19 DONE" + „Pfad-2" + „Phase G next".

---

## 📊 Commit-Graph (seit Baseline `ab6b3f5` bis Phase-E-Closure)

```
57bee6b log(phase-e-done): Phase E 19/19 RECONCILED + CR Re-Run + Pfad-2  ← CLOSURE
09e629f chore(vault): gitignore .obsidian/graph.json + cleanup stub files
d7ecf71 log(phase-e-95): Task 19 Acceptance + Codex RECONCILED + Fix-Welle E
e3ba381 fix(system-audit): Fix-Welle E — CodeRabbit Smoke-Cleanup
51f5719 handover(phase-e-18-done): Tasks 15-18 committed, Task 19 offen
ca35f62 handover(system-audit): Task 18 Sync-Welle — Pipeline-SSoT + §10-Audit
ab7ae19 chore(docs): Task 17 INSTRUKTIONEN §27.5 Migration-Regression-Guard
fa238bf feat(system-audit): Task 16 /SystemAudit slash-command wrapper
486f2c1 test(system-audit): Task 15 temp-repo smoke + seeded-drift integration
ab6b3f5 (baseline) log(task-14): Task 14 System-Audit Optional Checks + Fix-Welle C+D
```

**9 Phase-E-Commits** seit Baseline.

---

## 🎯 Deferred-Skill-Frage (Kontext bewahrt)

**Status-Matrix-Housekeeping-Skill `system-state-guardian`** — Opus-Vorschlag 2026-04-21 Abend. Entscheidung weiterhin auf **nach Phase G / Konsolidierungstag aufgehoben**. Parallel dazu: **System-Audit-Skill-Migration abgelehnt** per Projekt-Memory `project_system_audit_skill_decision.md` (Re-Eval-Trigger = ≥3 Audit-FAIL-Triage-Patterns, dann ggf. separater `system-audit-triage`-Skill — nicht Ersatz der Slash-Command).

---

## 🌐 Session-Übergabe-Protokoll

**Vor Session-Clear (diese Session):**
1. **`!SyncBriefing` empfohlen** (CLAUDE.md §25) — pushed `00_Core/` ins GitHub-Repo. Review-Gate Pflicht.
2. Unpushed-Commits seit letztem Push: `486f2c1`, `fa238bf`, `ab7ae19`, `ca35f62`, `51f5719`, `e3ba381`, `d7ecf71`, `09e629f`, `57bee6b` + Handover-Sync-Commit. **10 Commits gesamt** — größere Charge als üblich, Review-Aufmerksamkeit angemessen.

**Nach Session-Clear — Phase-G-Einstieg (Do Nachmittag ~14:30 CEST):**
1. `Session starten` → STATE.md (Banner „Phase E 19/19 DONE, Pfad-2, Phase G next")
2. Handover (diese Datei) — Phase G TMO-Details + Pfad-2-Kontext
3. TMO Q1 Earnings lesen (MarketBeat/IR-Portal/10-Q)
4. `!Analysiere TMO` — Old-Pipeline, Minimal-Modus
5. Sync-Welle (log + CORE-MEMORY §4 + Faktortabelle + STATE + JSONL)
6. Post-Reset (Do 22:00+ oder Fr): Phase F / Konsolidierungstag je nach User-Präferenz
