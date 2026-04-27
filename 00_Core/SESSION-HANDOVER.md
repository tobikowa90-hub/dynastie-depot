# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-27 später Tagesabschnitt — **Schema-Drift Phase 2 done (vault-wide)** + Tavily Rotation #1 final-verified (Vorgänger). Vault-only-Operation, kein Score/FLAG/Sparraten-Change.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `<phase-2-commit>` (Schema-Drift Phase 2 vault-wide).

**Diese Session committed:**

```
<phase-2-commit>  fix(wiki): schema-drift cleanup phase 2 — 34 vault-wide pages YAML-Array
```

**Vorgänger-Session (Stand vor Phase 2):**

```
737d647 chore(pipeline): tavily rotation #1 fully verified — old key revoked
f51b94a feat(analyses): pre-earnings briefs V (28.04.) + MSFT (29.04.)
531f459 fix(wiki): schema-drift cleanup phase 1 — sources/related YAML-Array
```

**Heute (27.04. spät / später Tagesabschnitt) abgeschlossen:**

- **Schema-Drift Phase 2 DONE (vault-wide)**: 34 drifted Pages konvertiert (15 concepts + 18 sources/papers + 1 sources/references) — Phase-1-Pattern (Block-Form `related:` + `sources: []`-Insert wenn fehlend) via neuem Tool `03_Tools/schema_drift_phase2.py` (line-end-preserving, regex-basiert, Dry-Run + Apply). 220 Wikilinks konvertiert, 33/34 `sources: []`-Inserts (Moat-Taxonomie hatte schon `sources:`). PyYAML-Bulk-Validation vault-weit 185/0 (367 Wikilinks in Arrays). Diffstat +287/-34. PIPELINE #15 → DONE. **Limitation:** 8 concept-pages mit `source:` (singular) bleiben unverändert (Phase-1 hat das auch nicht migriert; kein Pflicht-Feld, keine Backlink-Auswirkung).

**Vorgänger-Session (27.04. spät) abgeschlossen:**

- **Pre-Earnings-Briefs**: `02_Analysen/V_pre-earnings_2026-04-28.md` + `02_Analysen/MSFT_pre-earnings_2026-04-29.md` via `anthropic-skills:earnings-preview` (yfinance). V-Setup: technisch angeschlagen (-7,2 % unter 200MA, RelStärke -14pp), Konsens $3,099 EPS / $10,75 Mrd Rev, 4/4 Beats aber Surprise-Magnitude decel auf <1 %. MSFT-Setup: Recovery (+10,5 % in 2W, über 50DMA), Konsens $4,065 EPS / $81,40 Mrd Rev, 4/4 Beats +8,5 % Schnitt. Beide Briefs enthalten Bull/Base/Bear-Decision-Matrix + Schritt-für-Schritt-Earnings-Tag-Workflow inkl. Sync-Pflicht §18 für FLAG-Auflösungs-Szenario MSFT.
- **Tavily-Key-Rotation DONE**: alter Key `tvly-dev-4PYXp...` ersetzt. PROD-Connector (Claude.ai Web-UI) via Delete+Recreate (URL read-only) — Connector-Name bleibt `tavily`, friendly-name-Resolution `mcp__tavily__tavily_search` unverändert, **Repo-Prompts brauchen keinen Edit**. Lokal `~/.claude.json:777` editiert + Trailing-Space-Fix. **TODO User:** alten Key auf tavily.com revoken nach Smoke-Test (~10:00 MESZ Briefing-Cron). Claude Code lädt neuen Key erst nach Restart.
- **Schema-Drift-Cleanup Phase 1 DONE** (`531f459`, 16 Files, +222/-18): 14 Phase-A-Source-Pages + Synthesis-Page `Wissenschaftliche-Fundierung-DEFCON.md` von quoted-string `related: "[[A]], [[B]]"` auf YAML-Block-Array konvertiert + fehlendes `sources: []` ergänzt. Pattern an McLean-Pontiff validiert (Karpathy-Surgical), Block-Form gewählt für Konsistenz mit bereits bestehender `aliases:`-Struktur. PyYAML-Bulk-Validation 14/14 PASS, Synthesis-Page 74 Wikilinks (sources 34 + concepts 23 + related 6 + entities 11) intakt. **Codex-Final-Run M1 closed.**
- **PIPELINE-Sync DONE**: Item #15 Phase-2-Schema-Drift (vault-wide ~30 weitere Pages) als Deferred angelegt + Long-Term-Gates Tavily-Entry auf Rotation #2 ~04.05.2026 aktualisiert.
- **Standing-Dirty unverändert** (gleiche Liste seit 26.04.): app.json, wiki/concepts/PORTFOLIO.md, gelöschte canvas/base/2026-04-23.md.

### 🎯 Nächster Task — Earnings-First

**Priorität 1 (operativ, zeitkritisch — verdrängt alles andere):**

- **28.04.** V Q2 FY26 (after market close, ~22:00 MEZ) — D2-Entscheidung (Technicals-Reversal?). Brief liegt: `02_Analysen/V_pre-earnings_2026-04-28.md` §6 Decision-Matrix, §7 Schritt-für-Schritt-Workflow.
- **29.04.** MSFT Q3 FY26 (after market close, ~22:30 MEZ) — FLAG-Review CapEx/OCF (bereinigt <60 % = Auflösung). Brief liegt: `02_Analysen/MSFT_pre-earnings_2026-04-29.md` §6 + §7. Wichtig: **finale FLAG-Entscheidung erst mit 10-Q** (Press-Release reicht nicht für Finance-Lease-Bereinigung).

**Priorität 2 (Tech-Debt, deferred):**

- ~~**Schema-Drift-Cleanup Phase 2 (vault-wide)**~~ **DONE 27.04. später Tagesabschnitt** (siehe oben + PIPELINE #15). Pre-Validation User-Sichtprüfung: Obsidian-Backlinks der Phase-2-Pages bei nächstem Vault-Open kurz checken (Phase-1-Pattern war 5h+ live ohne Bug-Report; konservative Annahme).
- **Backtest-Strategie mit Inhalt füllen** (User-Initiative 27.04. spät) — Brainstorm angefangen aber zugunsten Tavily/Schema-Drift vertagt. Status: 28 score_history-Records (24 Backfill-Stubs ohne metriken_roh + 4 Forward), 2 FLAG-Events, 5 Tage portfolio_returns. Infrastructure groß, analytischer Output dünn. Frage offen: welche Backtest-Frage soll der erste Substantielle-Output beantworten? (Score-Predictiveness, FLAG-Event-Study, Sparraten-Kaskade-Sim, Real-Backfill, ...). **Trigger:** eigener Slot, brainstorming-Skill startet von vorn.
- **Morning Briefing v3.0.4 Hotfix** (PIPELINE #2, ~90 Min) — gates Dashboard v2 + Track 5a/5b. Eigener ungestörter Slot empfohlen.

### 🚨 Standing-Focus (operativ, unverändert)

- 28.04. V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?) — Brief ready
- 29.04. MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung) — Brief ready

### Wichtige Notizen

- **Score-Archiv unangetastet** — kein DEFCON-Trigger in dieser Session, kein `score_history.jsonl`-Append.
- **DEFCON v3.7 unverändert**, 11 Satelliten-Scores unverändert, Sparraten unverändert, FLAG-Status unverändert.
- **Dynastie-Depot Skill v3.7.3** geladen, aber kein operativer Skill-Call.
- **Tavily-Key**: neuer Key live in PROD + lokal. Alten Key revoken erst nach Smoke-Test morgen.
- **CodeRabbit-CLI** verfügbar via WSL Ubuntu (Memory `feedback_coderabbit_via_wsl.md`).

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*
