# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-24 spät — **Jake-Van-Clief-Video-Analyse abgeschlossen** (Wiki-Source-Page `wiki/sources/videos/updating-system/2026-03-10-jake-van-clief-folder-system-ai-agents.md` uncommitted — Third-Run ingest-video-Pipeline, large-v3, 5879s whisper-Runtime, 321 Segments, Quality-Gate PASS). Adoption-Verdikt **`pending-brainstorm`** — vorläufige Analyse ergab ~80%-Already-Implemented-Deckung, aber User-Pain liegt an anderer Stelle → Brainstorm in neuer Session nach /clear (siehe Block „Nächste Session" unten). Null Commit. Vorher (2026-04-23 Nachmittag): **Phase G (TMO Q1) DONE** Beat + Guidance-Raise, Score 64→67, D2→D3, `fcf_trend_neg` Resolve-Gate CLEAR. Sync-Welle 5 Files + Score-Record Old-Pipeline committed (`620702a`). Chore-Commit CLAUDE.md + system_audit.py (`0f043c7`).
**Vorherige Aktualisierungen:** 2026-04-22 Spät — Task 19 + Fix-Welle E (`d7ecf71`/`e3ba381`) · 2026-04-22 Mittag — Tasks 15-18 (`486f2c1`/`fa238bf`/`ab7ae19`/`ca35f62` + Handover `51f5719`) · 2026-04-21 Nacht — Task 14 + Fix-Welle C+D (`ab6b3f5`).

> **Progress-Banner (Phase A-G):** ✅ A+B+C+D+E · 🔵 F deferred · ✅ G (TMO Q1 Beat+Raise, Old-Pipeline-Sync `620702a`) · ✅ TMO-Retro-Audit Option B (`2513108`) · ✅ XLSX-Tools Sync (`5ccfdd1` + `a413c32` R-Column-Fix) · ✅ Daily-Persist-Nachtrag (`8a4008b`) · ✅ Check-3+Check-6 system-audit Fixes (`c07f2c3`) · ✅ Video-Ingest Second-Run Dubibubii + Adoption-Decision 4R/2O/1A (`ea48e2a`) · ✅ Video-Ingest Third-Run Jake Van Clief + Analyse uncommitted (`pending-brainstorm`) · ⏳ **Konsolidierungstag Fr 24.04.** (Block 1 schrumpft um 2 Items, Block 3 Dashboard v2) · ⏳ **Brainstorm-Session Session-Start-Optimierung** (neu, siehe unten).

> **🧠 NÄCHSTE SESSION (/clear 2026-04-24 spät) — BRAINSTORM-INPUT:**
>
> **Auftrag:** Frischer `superpowers:brainstorming`-Start **ohne Vor-Framing durch vorherige Session**. Thema = CLAUDE.md ideal strukturieren + Session-Start-Token-Cost reduzieren + globale Verlinkung / Orphan-Elimination.
>
> **User-Pain-Points (verbatim eingelegt):**
> 1. **Session-Start-Cost steigt** zunehmend — CLAUDE.md + STATE.md + MEMORY-Index + Skill-Listings akkumulieren.
> 2. **CLAUDE.md nicht ideal strukturiert** — Mischung aus Routing + Applied-Learning + Token-Rules + Auto-Memory + Wiki-Hinweis.
> 3. **Token-Effizienz-Regeln „global"** anwenden und „besser mit allen Aufgaben, Syncs usw verbinden" — Rules sollen über mehr Workflows greifen, nicht nur projektlokal in CLAUDE.md versteckt.
> 4. **Fehlende globale Verlinkung** — analog Vault-100%-Closure (Orphans + Missing-Backlinks) wünscht User auch für Root-Ordner **Visibility-Layer**, **nicht** strukturellen Rewrite. Zitat: „kein grundlegender rewrite der gesamten struktur! Das zerstört uns ja das system".
>
> **Constraints (verbindlich):**
> - **Kein struktureller Reorg** — keine File-Moves, keine neuen Verzeichnisse, keine Umbenennungen von Kerndateien (STATE.md, CLAUDE.md, INSTRUKTIONEN.md, CORE-MEMORY.md bleiben wo sie sind).
> - In-Place-Content-Polish OK (z.B. CLAUDE.md schlanker, Applied-Learning-Ceiling straffer).
> - **Visibility-Layer-Fokus** für Orphans/Backlinks (system_audit-Erweiterung ist Kandidat, nicht automatisch gesetzt).
> - **Jake Van Clief's 7 Mechaniken** sind **Input, kein Plan** — siehe Wiki-Source-Page. Vorläufiges Verdikt ~80%-Already-Implemented. Jake's #3 Routing-Table ist `deferred`, Rest `already-implemented`/`observe`/`reject-partial`.
>
> **Verworfen in vorheriger Brainstorm-Runde (nicht wieder vorschlagen ohne neuen Evidenz-Input):**
> - STATE.md-Zerlegung in PIPELINE.md/SYSTEM.md
> - Applied-Learning in separate Datei bewegen
> - Workspace-Explicit-Labeling mit pro-Workspace-CLAUDE.mds
> - Jake-Komplett-Adoption
>
> **Quellen-Referenzen für Brainstorm:**
> - Wiki-Source: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/sources/videos/updating-system/2026-03-10-jake-van-clief-folder-system-ai-agents.md` (7 Mechaniken + Adoption-Matrix + Meta-Befund)
> - Dubibubii-Präzedenz (inverse Polarität): `…/2026-04-22-dubibubii-claude-code-powerful-settings.md`
> - Memory `feedback_friction_as_evidence.md` (Creator-Video-Skepsis-Pattern)
> - Memory `feedback_multi_source_drift_check.md` (21.04.-Drift-Lesson)
> - Transkript Raw: `…/raw/videos/updating-system/2026-03-10-jake-van-clief-folder-system-ai-agents/transcript.md`
>
> **Pre-Aktion Session-Start:** User clearen → STATE.md lesen → diesen Handover-Block lesen → Wiki-Source-Page **nicht automatisch** lesen (nur wenn Brainstorm dorthin geht) → frische Fragen stellen, nicht mit Lösungsvorschlägen starten.

---

## 🚀 NÄCHSTE SESSION — Post-Reset-Aufgaben Do Abend + Konsolidierungstag Fr

### Kontext-Konstanten

- **Weekly-Reset:** Donnerstag 23.04.2026 **22:00 CEST** → Full-Budget-Window öffnet (heute Abend)
- **Phase G DONE:** TMO Q1 FY26 Forward-Vollanalyse 23.04. Nachmittag (Pfad-2 Old-Pipeline). Beat + Guidance-Raise, Score 64→67, D2→D3, `fcf_trend_neg` Resolve-Gate CLEAR. Sync-Welle committed `620702a`. Siehe CORE-MEMORY §1 Eintrag 23.04.2026 Nachmittag für Details.
- **Portfolio-State aktuell:** 11 Satelliten, Nenner 8,5 (8×1,0 + 1×0,5 + 2×0), volle Rate **33,53€**, V D2-Rate **16,76€**, FLAG-Raten **0€** (MSFT + APH). Summe 285€.
- **Nächste Trigger:** V Q2 FY26 28.04. (D2-Entscheidung), MSFT Q3 FY26 29.04. (FLAG-Review).

### ~~Direkter Einstieg Post-Reset: TMO-Retro-Migration~~ **DONE 23.04. spät (Option B)**

**Sequenz:**

1. ~~**TMO-Record Retro-Migration**~~ **Retro-Audit Option B DONE 23.04. spät.** Draft `03_Tools/backtest-ready/_drafts/TMO_20260423-retro-audit.json` angelegt (gitignored), Post-hoc-Validation der Skill-Pipeline gegen den `620702a`-Record gefahren. Phase-Outcomes: P1 parse PASS · P2a freshness INFO (erwartet, Working-Tree clean) · P2b STATE-Tripwire PASS (67/3/False dreifach konsistent) · P3 N/A · P4 Dry-Run PASS (synth. Archiv ohne TMO) · P4-bis Duplicate-Guard PASS (real). Kein Re-Append — Informationsverlust-Aversion > Ästhetik. **Erster echter Skill-Forward-Run bleibt V Q2 FY26 28.04.** Siehe `log.md` §[2026-04-23] retro-audit für volles Phase-by-Phase-Protokoll.
2. **XLSX-Tools einmaliger Update** via openpyxl:
   - `03_Tools/Rebalancing_Tool_v3.4.xlsx` — TMO-Row Score 64→67, DEFCON D2→D3, Sparrate 17,81€→33,53€; volle Rate anderer 7 Satelliten 35,63€→33,53€; V 17,81€→16,76€; Nenner-Zelle 8,0→8,5
   - `03_Tools/Satelliten_Monitor_v2.0.xlsx` — TMO-Row Score/DEFCON/Rate/Delta-Spalten; Legende-Datum 17.04.→23.04.
   - Sparraten-Summe 285€ in beiden Tools verifizieren
3. **Commit:** `chore(tools): TMO D2→D3 in Rebalancing + Satelliten-Monitor nach Retro-Migration`

### Alternative: Phase F Provenance-Plan-Execution (Do Abend Post-Reset, falls Zeit + Energie)

**Nur wenn User sagt „jetzt Phase F":** Plan `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (7 Tasks, 40 Steps) + Spec `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`. TMO-Retro-Migration oben läuft dann gegen v2-Schema (Provenance-Gate aktiv).

### Konsolidierungstag Fr 24.04. — Backlog-Cleanup + Dashboard v2

**Zeitbudget-Warnung (Opus-Advisory 22.04.):** Block 1 harter Cutoff 50 Min → Block 2 startet 11:00 Uhr fest. Falls existence-Cleanup >50 Min → auf nächste Session verschieben (Housekeeping, kein Blocker).

**Block 0 — Pre-Check (Session-Start, 25 Min):**
0. **Tavily-Key Smoke-Test** (5 Min) — prüfen ob Key `tvly-dev-4PYXp...` noch valid oder bereits abgelaufen. Falls abgelaufen → sofort rotieren, BEVOR Block 2 startet.
0b. **Provenance-Gate Pfad-2 Smoke-Test** (5 Min) — TMO Old-Pipeline-Draft gegen v2-Schema validieren: `python 03_Tools/backtest-ready/archive_score.py --dry-run <draft>`. Falls fail → Phase-F-Entscheidung überprüfen.
0c. **Track 5a/5b Entscheidungspunkt** (NEU 23.04., 15 Min, ausgeführt NACH Block 2 v3.0.4-PASS):
    - **5a SEC EDGAR Skill-Promotion** ja/nein — Re-Validation nach 6-Paper-Ingest B21-B24 prüfen, Dashboard-Feed-Scope bedenken.
    - **5b FRED Macro-Regime-Filter** ja/nein — User-Pre-Aktion: FRED-API-Key registrieren (https://fred.stlouisfed.org/docs/api/api_key.html). B19 stärkt wissenschaftliche Begründung.
    - **Output:** Entscheidung protokollieren in STATE.md §Pipeline 🟡 (Pläne aktivieren ODER weiter 🔵 deferred). Dashboard v2 Block 3 übernimmt Feed-Scope entsprechend.
    - **Grund der Position vor Block 3:** Dashboard-Scope hängt von Feed-Entscheidung ab — EDGAR/FRED nachträglich wäre Re-Integration.

**Block 1 — System-Hygiene (Morgen, max. 50 Min):**
1. **Check-3 `markdown_header` future-date-exclude** — `03_Tools/system_audit/checks/markdown_header.py:51-63` — Long-Term-Gates (2028-04-01, 2027-10-19, 2026-10-17) aus Event-Kandidaten ausschließen. Prüfen ob `##`- und `###`-Header beide korrekt gefiltert werden.
2. **existence-Cleanup-Welle** — ~54 CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix. Grep-Pattern bereitstellen vor manuellem Edit (spart Zeit). **Falls >50 Min Gesamt-Block → hier abbrechen, Rest nächste Session.**
3. **Nach (1)+(2):** §27.5-Guard von `--minimal-baseline` auf `--core` hochziehen + INSTRUKTIONEN-§-Kommentar-Update
4. **Check-5 Batch-Output** (Opus-Empfehlung 22.04.) — gruppiert nach Sektion mit Patch-Suggestion. `system_audit/checks/existence.py` anpassen.
5. **Check-4 WARN-Semantik** (Opus-Empfehlung 22.04.) — `⚠️ Informativ` vs. `🔴 Funktional` trennen. `system_audit/types.py` oder `report.py`.
6. **Check-6 Naming-Convention-Fix** — ZIPs existieren alle (`06_Skills-Pakete/backtest-ready-forward-verify.zip` etc.), aber Check-6 sucht nach `_v1.0.0.zip`-Pattern → False Positive WARN. Fix: Check-6-Logik in `system_audit/checks/skill_version.py` auf Basename-Match ohne Versionsnummer erweitern (~5 Min).

**Block 2 — Morning Briefing + Key (ab 11:00, ~90 Min):**
7. **Morning-Briefing v3.0.4-Hotfix** — Plan `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, ~90 Min). **Gate A für Track 5a/5b.**
8. **Tavily Dev-Key Rotation** — Key im Dashboard rotieren (falls nicht schon Block 0 erledigt). **Gate für Tavily-Integration Dashboard v2.**

**Block 3 — Dashboard v2 (Nachmittag, ~60 Min) — Gate: Block 2 DONE + Block 0c Entscheidung:**
9. **Dashboard v2 bauen** (`dynasty-depot-dashboard` Artifact updaten):
   - Faktortabelle.md-Parser mit `<!-- DATA:TICKER -->`-Ankern (ersetzt hartkodierte Scores)
   - Freshness-Guard: >7d 🟡 Banner / >90d 🔴 Banner
   - Preisquellen: Shibui primär → defeatbeta Fallback → yfinance Non-US
   - Tavily-Integration (scoped: Earnings ≤3d + aktive FLAGs + 1 Macro-Headline)
   - FLAG-Lösungs-Pfad inline (was löst jedes FLAG auf?)
   - Scheduled Task `dynasty-dashboard-refresh` auf File-Read-Architektur umstellen
   > **Architektur-Entscheidung (22.04. Opus+Sonnet, FINAL):** Artifact ≠ Briefing-Ersatz. Hybrid: Artifact = Snapshot/Feed (30s), Briefing = Narrativ+Reassurance (3 Min). Excel-Tools (Rebalancing/Satelliten/Watchlist) NICHT integriert. Scope = 11 Satelliten.

**Block 4 — Optional (falls Zeit bleibt):**
10. TMO-Retro-Migration falls Do Abend 22:00+ nicht erledigt
11. **Daily-Persist manueller Append** (Opus-Empfehlung 22.04.) — `python 03_Tools/portfolio_risk.py --persist daily --cashflow <eur>` für fehlende Tage 20.-24.04. ausführen. R5 ist deklarativ aktiv aber faktisch seit 17.04. stale — Interim-Gate 2027-10-19 braucht kontinuierliche Daten.

> **R5-Status-Klarstellung:** `portfolio_returns.jsonl` + `benchmark-series.jsonl` haben je nur 1 Record (17.04.). R5 Phase 3 ist deklarativ aktiv, faktisch stale. Auflösung via manuellen Append (Block 4) oder Auto-Hook (Track 4 nach ETF/Gold-Ticker-Entscheidung).

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
