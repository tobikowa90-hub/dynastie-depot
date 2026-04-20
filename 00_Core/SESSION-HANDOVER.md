# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-20 (späte Session) | **Für:** Nächste Session — **Track 5a + 5b Execution** (primär) + Track 1 T1-Rerun (offen)

---

## ⚡ SESSION 20.04. (späte Session) — TRACK 5 IMPLEMENTATION-PLANS BEREIT

### Abgeschlossen
- **Plan 5a geschrieben + Codex-reviewed + 4 Fixes eingepflegt:** `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks, ~540 Zeilen, force-added). Scope: SEC EDGAR Skill-Promotion + INSTRUKTIONEN §17-Update + _extern/-Superseded-Banner.
- **Plan 5b geschrieben + Codex-reviewed + 7 Fixes + 1 Kompromiss eingepflegt:** `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks, ~1240 Zeilen, force-added). Scope: FRED Macro-Regime-Filter via β `fredapi`, ALFRED/FRED-Dual-Mode, Grid-Search 1620 Combos vectorized, INSTRUKTIONEN §31 + §22.1.
- **§-Mismatch-Pattern etabliert:** Spec-§22 → Ist §17, Spec-§19 → Ist §8, Spec-§5-Audit → Ist §1. Header-Notice in beiden Plänen, Spec unverändert. Codex-Attestierung. Applied-Learning-Bullet #10 + Auto-Memory `feedback_spec_section_drift.md`.

### Track 5 Execution — Ablauf für 2026-04-21

**Priorität 1 (Plan 5a zuerst — kleiner, sauberer Start):**
1. `Session starten` → STATE.md lesen → Plan 5a laden
2. Pre-Implementation-Gates A (Tavily-Stabilität) + B (Kollisionscheck verifiziert ✅) + C (Python-Env) + D (§-Mapping-Recheck) durchlaufen
3. `superpowers:subagent-driven-development` für Task-by-Task-Execution (recommended) oder `executing-plans` für Inline
4. Task 1 (Env + edgartools install) → Task 2 (SKILL.md) → Task 3 (smoke-test) → Task 4 (INSTRUKTIONEN §17) → Task 5 (Docs-Sync) → Task 6 (_extern Banner) → Task 7 (E2E 4 Use-Cases) → Task 8 (!SyncBriefing)
5. Task 9 ist deferred (90-Tage-Audit 2026-07-19) — STATE-Trigger-Zeile beim Commit von Task 5 setzen

**Priorität 2 (Plan 5b, danach):**
1. Gate C (FRED-API-Key registrieren, ~5 Min bei https://fred.stlouisfed.org/docs/api/api_key.html) — **User-Aktion vor Task 1.3**
2. Tasks 1-3 (Env + fred_client + Schema) → Tasks 4-8 (Backfill + Backtest + Grid-Search + Conservative-Choice + §31) → Task 9-11 (Daily-Run + Briefing-Integration + Docs-Sync) → Task 12 (!SyncBriefing) → Task 13 (Verification)
3. Tasks 14-15 deferred (30-Tage ~2026-05-20 + Interim-Gate 2027-10-19)

### Kritische Gates vor Start
- **Gate A — Tavily-Go-Live 3-Tage-Stabilität:** Track 1 Phase 1 ist noch nicht abgeschlossen (T1-Rerun pending, siehe unten). Spec §4.1 verlangt Tavily-Stabilität vor Track-5-Start. User-Entscheidung: Track 5 parallel starten ODER warten auf T1-PASS?
- **Gate C — FRED-API-Key beschaffen** (nur für Plan 5b, ~5 Min User-Aktion)

### ⚠️ Zeitliche Abhängigkeitskette (Review-Einwand 2026-04-20)

Track 5a hat eine **implizite Abhängigkeit von Tavily-Stabilität** die Gate A explizit festhält — daraus ergibt sich eine erzwungene Sequenz:

```
Morgen (21.04.):  Tavily Morning Briefing v3.0 Go-Live (T1-Rerun + T3 + T4 + Prod-Deploy)
                          ↓
+3 Tage (24.04.): Gate A freigegeben → Track 5a kann starten (sec-edgar-skill)
                          ↓
Nach Track 5a:    Track 5b (FRED Regime-Filter) — keine Tavily-Abhängigkeit,
                  aber logisch nach 5a sinnvoller (kleinerer Scope zuerst)
```

**Konkrete Gefahr ohne diese Notiz:** Gate A wird in 3 Tagen "vergessen" und Track 5a beginnt entweder zu früh (vor Tavily-Stabilität) oder zu spät (weil kein Trigger vorhanden).

**Empfehlung:** Am **24.04. morgens** beim Session-Start aktiv fragen: "Waren die letzten 3 Briefings (22./23./24.04.) stabil?" — Wenn ja: Gate A grün → Track 5a-Execution-Session starten.

**Track 5b hat keine Tavily-Abhängigkeit** — könnte theoretisch parallel zu Track 5a laufen, aber die natürliche Sequenz (5a zuerst, kleiner + sauberer) bleibt empfohlen. Ausnahme: falls FRED-API-Key bereits vorliegt und Track 5b-Execution separat gewünscht wird.

### Artefakte (beide in `docs/superpowers/plans/`, force-added per Konvention)
- `2026-04-20-track5a-edgar-skill-promotion.md`
- `2026-04-20-track5b-fred-regime-filter.md`
- Spec (v1.0 frozen, archiviert 2026-04-20): `05_Archiv/TRACK5-SPEC-edgar-fred-v1.0.md` (Commit `22cdeb8`)

### Nicht-Änderungen dieser Session
- Keine Scores / FLAGs / Sparraten (reine Planungs-Artefakte)
- Keine System-Code-Änderung (Plans sind Prosa, Implementation folgt 2026-04-21)
- Keine Vault-Updates (Post-Execution-Phase — Wiki-Pages entstehen wenn §31/edgar-skill tatsächlich Outputs produzieren)

---

---

## ⚡ SESSION 20.04. (00:13-00:40 MESZ) — TAVILY TRACK 1 PHASE 1 (Tasks 0-3 + T1 Probe-Iteration)

### Abgeschlossen
- **Task 0:** `03_Tools/morning-briefing-prompt-v2.md` back-fill (Embedded v2.2 Prompt-Content für Rollback-Integrität). Commit `dd0cd62`.
- **Task 1:** `03_Tools/morning-briefing-prompt-v3.md` geschrieben (v3.0 Base + Changelog + V3.1-Backlog). Commit `f5a0bba`.
- **Task 2:** Probe-Test-Fixtures `03_Tools/tests/tavily-probe-prompts/` (README + T1/T3/T4). Commit `bde3aff`.
- **Task 3:** Probe `trig_01XYuQ5mugsvZGZD4K52rjXh` konfiguriert (allowed_tools + Shibui + Tavily MCP, v3.0-Content geladen).
- **v3.0.1 Hotfix:** SCHRITT 1 mit `TZ='Europe/Berlin'` explizit. Discovered bei T1-Run #1 (Agent sah UTC-Sonntag → WOCHENEND-MODUS statt Werktag). Commit `d0c25ba`.
- **v3.0.2 Hotfix:** Sequenzierungs-Direktive SCHRITT 3 → 4.5 (Anti-Parallelisierung). Discovered bei T1-Run #2 (Agent startete Yahoo-curl + Tavily parallel → Yahoo-403 killte Tavily → Retry-Overhead >90s). Commit `a0311f2`.

### T1-Status: **FAIL** (per Codex-Review, spec §6(E) §11 hard-gate)
- Funktional: ✅ PASS (8/8 Sektionen, Materialitäts-Filter arbeitet, Slot-Struktur 4/5 getriggert: MSFT/AVGO/APH/TMO, 0% material today)
- Laufzeit: ❌ FAIL ("dauerte sehr lange") — Klasse 6 Runtime-Timeout-Risk
- Codex-Caveat: Prompt-Sequenzierung reduziert, garantiert aber keine Runtime-Parallelisierung. Bei v3.0.2-Rerun Re-Overshoot → strukturelle Lösung nötig (Tool-Call-Reduktion).

### Probe-Zustand jetzt
- Trigger: `trig_01XYuQ5mugsvZGZD4K52rjXh`, **v3.0.2 live, T1-Happy-Path-Content geladen, ready for manual run**
- Model: sonnet-4-6, allowed_tools: Bash+Read+Glob+Grep+mcp__tavily__tavily_search
- MCP: Shibui + Tavily (Dev-Key tvly-dev-4PYXp... — unverändert)

---

## ▶️ NÄCHSTE SESSION — START

### Priorität 1: T1-Rerun mit v3.0.2
1. Desktop App → Routines → `tavily-probe` → "Jetzt ausführen"
2. Laufzeit messen (Timer!). Pass-Kriterium: <90s
3. Output komplett an Claude pasten
4. Falls <90s UND funktional OK → T1 PASS → zu T3 weiter
5. Falls weiterhin >90s → strukturelle Lösung (Codex konsultieren für Tool-Call-Reduktion-Optionen)

### Verbleibende Tasks im Plan
- Task 4.6: T1-Result in `results/T1-YYYY-MM-DD.md` dokumentieren
- Task 5: T3 Adversarial Symbol-Trap (RMS.PA + SU.PA forciert)
- Task 6: T4 Fail-Open (HTTP 422 Pattern)
- Task 7: Gate-Review (alle 3 PASS?)
- Task 8: Prod-Deploy via RemoteTrigger update auf `trig_01PyAVAxFpjbPkvXq7UrS2uG`
- Task 9: Post-Update-Content-Verify (4 Assertions auf Prod)
- Task 10: Prod Manual-Run Verification (Tavily v3.0-First-Run)
- Task 11: Post-Deploy Housekeeping (memory/morning-briefing-config.md + CORE-MEMORY §10 + log.md + STATE.md-Version)
- Task 13: Day 1-3 Monitoring (Threshold 70% material)

### Artefakte (stabil)
- **Plan:** `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md`
- **Spec:** `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` (Klasse 6 >90s = Rollback-Gate)
- **v3.md:** `03_Tools/morning-briefing-prompt-v3.md` (v3.0.2 aktiv)
- **v2.md:** `03_Tools/morning-briefing-prompt-v2.md` (Rollback-Ready)

---

## ⚡ SESSION 20.04. (frühe Phase) — TOOL-EVALUATION ABGESCHLOSSEN

### Kontext

User hat eine Tool-Evaluation-Session durchgeführt mit der expliziten Bedingung: **"Wir nehmen nichts ins System auf, das dieses nicht wirklich besser macht."** Jedes Tool wurde durch dasselbe rigorose Prüfschema gezogen: Repo-Read → Claude-Analyse → Codex-Rescue Second-Opinion → gemeinsame Verdikt-Synthese.

### Ergebnis: 5 Tools + 1 Meta-Frage geprüft, alle verworfen

| Kandidat | Verdikt | Kern-Grund |
|---|---|---|
| **HKUDS/OpenSpace** (self-evolving skill MCP) | Reject | Trust-Boundary: LLM-self-confirm statt User-Gate, keine Git-Integration, broad-by-default Runtime. CLI vs. MCP = nur Invocation-Cosmetics. Separate Profil-Instanz wäre notwendige Grenze. |
| **Eigen-Telemetrie-Hook + !EvolveSkill** | Reject | Scheinwerkzeug. Skills sind Markdown-Instruktionen, keine callable Functions — `PostToolUse` kann Skill-Invocations nicht zuverlässig tracken. Success/Failure semantisch matschig. |
| **HKUDS/RAG-Anything** (multimodal RAG) | Reject | Drittes paralleles Wissenssystem würde Single-Source-of-Truth erodieren (CORE-MEMORY + Obsidian + RAG-Graph). 71-Note-Vault zu klein für Fixed-Overhead-Amortisation. MinerU/LibreOffice Ops-Ballast. |
| **Swarms-Video (AI Impact School)** | Reject | Pattern ist valide, aber bereits vorhanden via `Agent`-Tool + `superpowers:dispatching-parallel-agents` + Codex-Rescue + Sync-Pflicht-Pattern. Rebranding. |
| **Sequential-Thinking-MCP** | Reject | Scaffold-Overlay ohne Persistence. Opus-High-Effort + superpowers (`systematic-debugging`, `writing-plans`, `brainstorming`) decken strukturierten Denk-Scaffold bereits ab — semantisch reicher + persistent. |

### Meta-Frage: "Gibt es überhaupt noch sinnvolle Tools?"

Codex-Review identifizierte **einen plausiblen Kandidaten** und zwei Grenzfälle:

- **FRED-MCP** (`dracepj/fred-mcp`) — **HIGH Fit falls gewollt**, sonst nicht. Macro-Regime-Daten (Credit-Spreads, Yield-Curve, Unemployment, ISM, Industrial Production). Gated on: "Soll Macro-Dimension in DEFCON einfließen?" Bottom-up-Only bleibt → nicht relevant.
- **quantstats** (`ranaroussi/quantstats`) — MEDIUM Fit. Portfolio-Level-Risk-Tearsheets. Overlap mit existierendem `backtest-ready-forward-verify` + `portfolio_returns.jsonl` zu klären.
- **edgartools** (`dgunning/edgartools`) — MEDIUM Fit. Strukturierte 10-K/10-Q/8-K/Form-4 via MCP. Overlap mit sec-edgar-skill (Eskalations-Fallback per INSTRUKTIONEN §19) + insider-intelligence.

**Session-Konklusion beider Reviewer (Claude + Codex):** System ist für aktuellen Bottom-Up-Perimeter komplett. Weitere Tool-Evaluierung wäre Prokrastination gegenüber Pending-Work.

### User-Erkenntnis

> "Dachte eigentlich die hätten wir schon so halbwegs im System" (zu SEC EDGAR + FRED)

**Teils korrekt:**
- **SEC EDGAR:** ✅ partiell integriert — INSTRUKTIONEN §19 nennt SEC EDGAR als Fallback-Datenquelle (US), INSTRUKTIONEN §22 listet `sec-edgar-skill` als Eskalations-Fallback, WebFetch-Permission für `efts.sec.gov`. Track-5-Upgrade wäre von WebFetch→dedicated-MCP.
- **FRED:** ❌ nicht im System — keine Macro-Signale, keine Permissions, keine Referenz. Strategische Greenfield-Entscheidung.

---

## 🔥 NÄCHSTE SESSION — TRACK 1 TAVILY + MORNING BRIEFING

### Start (User-Trigger)

```
Session starten
```

Claude liest `00_Core/STATE.md`. Dann hierher wechseln.

### Artefakte

- **Plan:** `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md` (Commit d1b5bf7)
- **Spec:** `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` (Commit 6bd32f4)
- **Umfang:** 13 Tasks, ~60-90 Min inkl. manueller Desktop-App-Runs

### Dependency-Status aktualisiert

**Track 3 Paper-Integration ist abgeschlossen** (verifiziert via Git-Log: e7ec96c, 67ed120, 96b0b69, c1f0f21, f7920cf). Blockade von Track 1 aufgelöst.

### Schlüssel-Constraint

- **Tavily Dev-Key Rotation innerhalb 7 Tagen nach Go-Live** — Kalender-Trigger setzen
- **3-Tage-Monitoring** nach Tavily-Stabilität bevor Track 5 (SEC EDGAR + FRED) angegangen wird

---

## 🎯 TRACK 5 — SEC EDGAR + FRED (nach Tavily-Stabilität)

### Entscheidungs-Framework

**Nicht "installieren ja/nein", sondern "welchen Hebel":**

1. **SEC EDGAR-MCP** (z.B. `dgunning/edgartools`) — Upgrade von aktueller WebFetch-basierter Partial-Coverage zu strukturiertem Parser. **Höherer Hebel** laut Codex-Review. Konkrete Use-Cases: saubere 10-K/10-Q/8-K/Form-4-Objekte statt HTML-Scraping-Fallback.

2. **FRED-MCP** (`dracepj/fred-mcp`) — Greenfield-Macro-Layer. **Nur sinnvoll wenn:** Macro-Dimension aktiv in DEFCON-Scoring aufgenommen werden soll. Aktuell bottom-up-only. Diese Entscheidung ist **strategisch** (nicht technisch) — Scoring-Erweiterung, keine Tool-Installation.

### Reihenfolge (Codex-Empfehlung)

1. SEC EDGAR zuerst (klarer Hebel, bereits partiell im System)
2. FRED separat — erst wenn Macro-in-DEFCON-Strategie-Entscheidung getroffen ist

### Vor Track 5 prüfen

- Hat Tavily nach 3 Tagen stabil geliefert ohne Rate-Limit-/API-Ausfälle?
- Ist Morning-Briefing-Workflow im Alltag etabliert und bringt Wert?
- Falls nein zu einem der beiden: Tavily-Debugging vor Track 5 Priorität geben.

---

## 📋 PENDING PARALLEL TRACKS

### Track 4 — Portfolio-Risk-Tool ETF+Gold-Erweiterung

**Braucht User-Input am Session-Start:**
- **ETF-Core-Ticker?** (IWDA.AS / SWDA.L / EUNL.DE / ähnlich?)
- **Gold-Ticker?** (SGLD.DE / 4GLD.DE / GC=F / ähnlich?)

Danach: `03_Tools/portfolio_risk.py` um ETF+Gold erweitern. Natürliche Einbettung in `--persist daily`-Schema (aus Track 3 Phase 3).

---

## ⚠️ OPEN RISKS / REMINDERS

1. **Tavily Dev-Key Rotation** innerhalb 7 Tagen nach Go-Live (Track 1).
2. **Codex-Plugin Review-Gate** NICHT aktiviert (User-Entscheidung 19.04.) — Codex nur on-demand via `codex:codex-rescue`.
3. **Track-5-Entscheidung FRED** ist strategisch, nicht technisch — Macro-in-DEFCON-Frage vorher klären.
4. **Tool-Evaluation-Pattern bestätigt:** System ist reif, externe Angebote clearen Schwelle selten. Gilt bis strategische Scope-Erweiterung (z.B. Macro-Dimension) eintritt.

---

## 💡 LEARNINGS SESSION 20.04.

**Codex als Reviewer (6 Runden in einer Session):**
- Pattern `Claude-Position → Codex-Review → Synthese` bleibt robust und produktiv
- Codex identifiziert systematisch epistemische Schwächen (z.B. "Opus native thinking besser" = Inferenz, nicht dokumentiert)
- Bei Konvergenz beider Reviewer: klare Entscheidung ohne weitere Iteration
- Agent-IDs für `--resume`: OpenSpace (abfe677f), CLI-Review (a5e83e92), Eigen-Build (a574d235), RAG-Anything (a45ff964), Sequential-Thinking (a817bf82), Meta-Frage (aa87fe68)

**Tool-Evaluation-Kriterium geschärft:**
- Nicht "ist es sicher?" sondern "ersetzt es etwas Existierendes mit echtem Mehrwert oder dupliziert es es nur unter anderem Namen?"
- Trust-Boundary + Skill-Modifikation = separate Risikoklasse (OpenSpace)
- Additive Tools (RAG, Sequential-Thinking) werden primär auf ROI geprüft, nicht Sicherheit
- Eigen-Build ist oft überengineered — Inferenz "ich kann das besser machen" stimmt selten bei reifen Systemen

**Strategischer Insight:**
- System-Reife wird sichtbar daran dass externe Angebote die Schwelle nicht mehr clearen
- Das ist kein Stillstand — das ist Disziplin
- Nächste echte Erweiterungen sind strategische Scope-Entscheidungen (Macro-Dimension?) nicht Tool-Installationen

---

## ▶️ TRIGGER (nächste Session)

```
Session starten
```

1. Claude liest `STATE.md`
2. Wechsel hierher
3. Primär-Track: **Track 1 Tavily + Morning Briefing Execution**
4. Plan öffnen: `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md`
5. `executing-plans`-Skill invoken
6. Task 1 starten

Bei abweichender User-Priorität: Track 4 oder Track 5 ebenfalls möglich, aber Tavily-Stabilität vor Track 5 beachten.
