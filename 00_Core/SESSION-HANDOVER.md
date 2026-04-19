# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 19.04.2026 Mittag (Tavily-Arc abgeschlossen bis Spec+Plan, Execution in neuer Session) | **Für:** Nächste Session — Tavily-Plan ausführen + 3 pending Tracks

---

## ⚡ SESSION 19.04. MITTAG — PROGRESS SAVE (Context Full)

### ✅ IN DIESER SESSION ABGESCHLOSSEN

**Infrastruktur-Installs:**
- `codex` Plugin (OpenAI Codex CLI 0.121.0, ChatGPT-Login aktiv) — Feedback-Memory `feedback_codex_over_advisor.md` setzt Codex als Default-Reviewer statt `advisor()` ab sofort.
- `tavily-mcp` lokal via `claude mcp add --scope user` (hosted HTTP, Dev-Key, 1000 Credits/Mo Free-Tier).
- Tavily-Connector in Claude.ai Web-UI registriert — UUID `4a633350-7128-4729-b8be-85373854fa4d`.
- Karpathy/autoresearch **abgelehnt** nach Reality-Check (GPU-LLM-Training-Harness, passt nicht).

**Tavily Morning-Briefing Integration — Design komplett:**

| Artefakt | Pfad | Commit | Status |
|---|---|---|---|
| Spec (MCP-Architektur final) | `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` | `6bd32f4` | ✅ Codex-freigegeben (3 Rounds), user-approved |
| Implementation Plan (13 Tasks) | `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md` | `d1b5bf7` (force-added, gitignored by default) | ✅ geschrieben, Execution pending |

**Arc-History (für Transparenz):**
- Initial MCP-Spec → Phase-0-R1 Tests (A/B/C) alle PASS → Codex-Review #1 identifizierte 7 Gaps → all fixed → User wollte CLI-Pivot testen → Phase-0-R2: REST `api.tavily.com` liefert HTTP 403 "Host not in allowlist" für Dev-Keys (Free-Tier) → **surgical revert zu MCP** (Codex-Fixes #1-7 behalten) → Codex-Review #2 fand 5 Inkonsistenzen nach Revert → all fixed → final.
- Probe-Trigger `trig_01XYuQ5mugsvZGZD4K52rjXh` bleibt inert (disabled, Cron 31.12., manuell triggerbar). Kann in Claude.ai gelöscht werden.

**Infrastruktur-State (für nächste Session wichtig):**
- Prod-Trigger `trig_01PyAVAxFpjbPkvXq7UrS2uG` hat jetzt Shibui + Tavily in `mcp_connections`, aber `allowed_tools` noch OHNE `mcp__tavily__tavily_search` → v2.2-Verhalten unverändert, Tavily inert bis Deploy
- Tavily-Dev-Key liegt im prod-Trigger `mcp_connections.url` (abrufbar via `RemoteTrigger get`). **Key-Rotation empfohlen** nach Go-Live (siehe Plan-Anhang).

---

## 🔥 NÄCHSTE SESSION — 4 OFFENE TRACKS

### TRACK 1 (PRIO) — Tavily-Plan ausführen

**Start:** In neuer Session → `Session starten` (liest STATE) → Plan öffnen: `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md`

**13 Tasks, ~60-90 Min Gesamtaufwand** inkl. manueller Desktop-App-Runs (T1/T3/T4 auf Probe, dann Prod-Deploy + T5 + Manual-Run + 3-Tage-Monitoring).

**Execution-Entscheidung am Plan-Start:**
- Subagent-Driven (recommended): fresh Subagent pro Task, schneller
- Inline Executing-Plans: Batch-Execution mit Checkpoints

Plan ist vollständig — Exakte RemoteTrigger-Payloads, exakter v3.0-Prompt-Content in Task 1, adversarial-T3 (Codex #1-Fix mit query-content-Assertion), rollback-runbook (Codex #5), Day-1-3-Monitoring (Codex #6).

**Nach Go-Live:** Key-Rotation in 7 Tagen (Reminder-Task im Plan-Anhang).

---

### TRACK 2 (PENDING seit gestern Nacht) — Phase 4a Sync-Commit

**Kontext:** Gestern Abend (18.04./19.04. Nacht) wurden Phase 1+2 des 4-Paper-Backtest-Validation-Frameworks durchgeführt, aber **noch nicht committed**.

**Uncommitted State (bei Session-Start via `git status` verifizieren):**
```
M 00_Core/CORE-MEMORY.md              ← §5 Lektion "4-Paper-Triage für §29"
M 00_Core/INSTRUKTIONEN.md            ← §29 eingefügt, Fußzeile v1.9→v1.10
M 00_Core/STATE.md                    ← Interim-Gate 2027-10-19 Bullet
M 01_Skills/backtest-ready-forward-verify/SKILL.md  ← §8 Retrospektive-Analyse-Bullet
M 01_Skills/dynastie-depot/SKILL.md   ← Fundamentals-Review-Bullet
M CLAUDE.md                           ← 4-Dim-Gate-Bullet + Counter 8/20→9/20
M 07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/index.md
M 07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md
M 07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Backtest-Methodik-Roadmap.md
M 07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md
?? 07_Obsidian Vault/...wiki/concepts/Factor-Information-Decay.md        ← NEU
?? 07_Obsidian Vault/...wiki/concepts/Factor-Investing-Framework.md      ← NEU
?? 07_Obsidian Vault/...wiki/concepts/PBO-Backtest-Overfitting.md        ← NEU
?? 07_Obsidian Vault/...wiki/concepts/Palomar-Methods-Reference.md       ← NEU
?? 07_Obsidian Vault/...wiki/concepts/Seven-Sins-Backtesting.md          ← NEU
?? 07_Obsidian Vault/...wiki/sources/Aghassi-2023-Fact-Fiction.md        ← NEU (Paper 1)
?? 07_Obsidian Vault/...wiki/sources/Bailey-2015-PBO.md                  ← NEU (Paper 2)
?? 07_Obsidian Vault/...wiki/sources/Flint-Vermaak-2021-Decay.md         ← NEU (Paper 3)
?? 07_Obsidian Vault/...wiki/sources/Palomar-2025-Portfolio-Optimization.md  ← NEU (Paper 4)
```

**Commit-Message (vorformuliert):**
```
feat(vault+system): 4-Paper-Backtest-Validation-Framework — §29 Retrospective-Gate + Vault-Ingest (9 new Pages)
```

**Nach Commit:** `!SyncBriefing` (00_Core/ wurde geändert).

**Warum dieser Track zuerst (vor Track 1):** Tavily-Plan-Execution modifiziert 00_Core/CORE-MEMORY.md, STATE.md und log.md (Housekeeping-Task 11). Wenn Phase 4a noch uncommitted ist, vermischen sich die Changesets. Saubere Reihenfolge: Track 2 commit → Track 1 ausführen.

---

### TRACK 3 (PENDING) — Paper-Integration systemweit

**User-Statement (19.04. Mittag):** *"Die Integration der Paper, universelle Verbindung mit dem Vault und Nutzung für das gesamte System stehen auch noch aus und dürfen nicht vergessen werden"*

**Interpretation (zu validieren mit User):**
1. ✅ Papers ingested (Aghassi, Bailey, Flint-Vermaak, Palomar — alle in wiki/sources/ Stand 19.04. Nacht)
2. ⏳ **Universelle Vault-Verbindung:** Cross-Linking zwischen neuen wiki/concepts/ (5 Notes) und wiki/sources/ (4 Papers) + Verknüpfung zu bestehenden Entity-Pages, Ticker-Dossiers, Factor-Pages. Backlinks pflegen. Index-Struktur aktualisieren.
3. ⏳ **Systemweite Nutzung:** Die Paper-Insights (PBO, Factor-Decay, 7 Sins of Backtesting, Palomar-Methods) müssen operativ ins System einfließen jenseits §29 Retrospective-Gate:
   - DEFCON-Scoring-System: Welche Paper-Findings ändern/validieren Scoring-Gewichte?
   - Skill `backtest-ready-forward-verify`: 4-Dim-Gate-Integration (PBO + AQR-Bench + Half-Life + Seven Sins) — ist in CLAUDE.md Applied-Learning v2.1 erwähnt, aber Skill-Level-Integration unklar
   - INSTRUKTIONEN.md §§: Braucht es eine §30 "Paper-gestützte Scoring-Anpassungen"?
   - Rebalancing-Tool: Paper-basierte Regeln einführen?

**Offene Fragen für User am Session-Start:**
- Was genau heißt "universelle Verbindung" — nur Obsidian-Backlinks oder Index-Ebene / Entity-Pages / Ticker-Dossiers?
- Welche Scope-Abgrenzung zu §29 (das bereits Retrospective-Gate integriert)?
- Ist das eine eigene Spec-Würdige Arbeit oder organisch als Backlog-Items in v3.1+ aufnehmen?

Vor Ausführung: **Brainstorming-Skill** ist Pflicht per CLAUDE.md (Creative Work).

---

### TRACK 4 (PENDING) — Phase 3 Infrastruktur (Portfolio-Risk-Tool erweitern)

**Braucht User-Input am Session-Start:**
- **ETF-Core-Ticker?** (IWDA.AS / SWDA.L / EUNL.DE / ähnlich — was im realen Depot?)
- **Gold-Ticker?** (SGLD.DE / 4GLD.DE / GC=F / ähnlich?)

Danach: `03_Tools/portfolio_risk.py` um ETF+Gold erweitern + `--persist weekly`-Modus für `05_Archiv/portfolio_returns.jsonl`. Erster Weekly-Snapshot-Run.

**Abhängigkeit:** Keine zu Track 1/2/3. Kann jederzeit gemacht werden.

---

### TRACK 5 (DEFERRED, nach Track 1) — SEC EDGAR + FRED MCPs

**Kontext:** In dieser Session diskutiert — wenn Tavily operativ läuft, sind SEC EDGAR und FRED die **nächsten Kandidaten** für System-Erweiterung.

| MCP | Lücke im System | Geschätzter Nutzen |
|---|---|---|
| **SEC EDGAR MCP** | 10-K/10-Q Risk Factors, Footnotes, 8-K Events, Proxy (Exec-Comp) | Mittel-hoch — Quality-Trap + Moat-Validation mit echten Filing-Footnotes, komplementiert Insider-Intelligence (Form 4 only) |
| **FRED MCP** | Macro-Daten (Fed Rates, Yield Curve, Inflation, GDP) | Niedrig-mittel — Sektor-spezifische DEFCON-Multiplikatoren (REITs/Banken/Utilities), aber optional |

**Entscheidungs-Reihenfolge:** Tavily erst produktiv + 3 Tage stabil → dann SEC EDGAR (höherer Hebel) → FRED nur wenn Sektor-Mods geplant.

**Install-Pfad (wenn soweit):** Analog Tavily — `claude mcp add` lokal + Claude.ai Connector-Registrierung + Remote-Trigger-mcp_connections-Update. Brainstorming-Skill vorher zwingend.

---

## ⚠️ OPEN RISKS / REMINDERS

1. **Tavily Dev-Key Rotation:** Nach Tavily-Go-Live innerhalb 7 Tagen. Key liegt exponiert in mcp_connections.url. Workflow: Tavily-Dashboard → Delete old Key → New Key → `claude mcp remove/add` LOKAL + `RemoteTrigger update` für prod-Trigger-URL-Austausch.
2. **Probe-Trigger `trig_01XYuQ5mugsvZGZD4K52rjXh`:** Inert aber existiert. Kann in Claude.ai UI gelöscht werden falls störend. RemoteTrigger-API hat kein Delete-Endpoint.
3. **Tavily-MCP-Connector in Claude.ai:** Bleibt aktiv, falls du manuell Tavily-Queries machen willst. Kann auch entfernt werden — Prod-Trigger hat unabhängig davon die Connector-UUID gespeichert.
4. **Codex-Plugin:** Review-Gate NICHT aktiviert (würde jeden Session-Stop blocken — user-Entscheidung 19.04.). Codex wird on-demand aufgerufen wie advisor vorher.

---

## 💡 LEARNINGS SESSION 19.04. MITTAG

**Codex als Reviewer (erste Real-Tests):**
- **3 Rounds Codex-Review** über den Tavily-Arc — je ~17-20k Tokens, jedem Round fand substantielle Gaps
- Codex erkennt **Terminology-Drift** nach Revert-Operationen exzellent (CLI-Residuen in MCP-Spec gefunden)
- **Neues Pattern:** Empirische Tests (Phase 0) VOR tiefer Spec-Arbeit — Codex-Flag #1 war empirisch widerlegbar in 5 Min (Test A)
- Reconcile-Call-Regel aus Feedback-Memory hat funktioniert (CLI-Fail war Primärevidenz → direkt Revert ohne Codex-Rückfrage)

**Superpowers-Workflow (mit `brainstorming → writing-plans`-Kette):**
- Brainstorming-Skill strikt gefolgt: 5 Clarifying-Questions → 2 Architektur-Varianten → 5 Design-Sektionen approval-pro-Sektion → Spec-Write → Self-Review → Codex → User-Review → Plan-Write
- **HARD-GATE** vor Implementation-Action respected — kein Edit am Prod-Trigger bisher, alles in Probe + Spec + Plan
- Plan-Skill produziert mit exakten RemoteTrigger-Payloads (13 Tasks, ~1100 Zeilen) — ausführbar mit minimalem Rückfrage-Budget

**Revert-Muster:**
- CLI→MCP-Pivot-Revert war ~30 Min Arbeit nachdem Phase-0-R2 failed; **keine architekturelle Überraschung** weil Codex-Fixes architekturneutral designt waren (dank frühem Codex-Pass)

---

## ▶️ TRIGGER (nächste Session)

```
Session starten
```

Claude liest `00_Core/STATE.md`. Dann hierher wechseln. Reihenfolge:
1. **Track 2** (Phase 4a Sync-Commit) — sauberer Changeset-Reset
2. **Track 1** (Tavily-Plan ausführen) — oder Track 3 wenn User Paper-Integration priorisiert
3. **Track 4** (Portfolio-Risk ETF+Gold) — wann immer User-Input für Ticker da ist
4. **Track 5** (SEC EDGAR / FRED) — nach Tavily stabil (3-Tage-Monitoring)

**Bei Start unbedingt klären:** Welcher Track heute? Track 3 (Paper-Integration) ist das am wenigsten spezifizierte und braucht erst Klärung des "universelle Verbindung"-Scopes.
