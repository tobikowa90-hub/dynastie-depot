# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-24 Session-1-Ende — **CLAUDE.md Routing-Refactor Tier 1 EXECUTION + Sync-Welle + Codex-Reconciliation DONE.** Plan v0.2.1 (8 Tasks) + Section-A (AL v2.5) + STATE.md Pipeline-SSoT + CORE-MEMORY §1 + Codex-Fix + Option-B-Compression + Handover-Close + TOKEN-RULES-CrossRef = **14 Commits**, alle LOKAL auf `main`. **CLAUDE.md 97→71 Zeilen** (Spec-Ziel ~70 erreicht). 11/11 AC PASS mit 2 dokumentierten Abweichungen. Codex-Verdikt `RECONCILED_WITH_FOLLOWUPS`, alle 3 Findings abgearbeitet (#1 Plan-intentional, #2 minor accepted, #3 Tool-Setups-Descriptor restauriert). **Session 2 PENDING:** CodeRabbit-Pass (WSL) + Vault-Update-Sweep. **Session 3 (Brainstorm-Kandidat):** 00_Core Perfect-Organization (Tier 2b CORE-MEMORY Restrukturierung + Tier 2 STATE-Split + Global-Linking-Strategie) — siehe STATE.md #12.
**Vorherige Aktualisierungen:** 2026-04-24 Mobile — Brainstorm+Spec+Plan CLAUDE.md-Routing (DONE, 5 Commits) · 2026-04-23 Nachmittag — Phase G (TMO Q1 DONE) · 2026-04-22 Spät — Task 19 + Fix-Welle E · 2026-04-22 Mittag — Tasks 15-18 · 2026-04-21 Nacht — Task 14 + Fix-Welle C+D.

> **Progress-Banner Tier 1:** ✅ Brainstorm (Desktop 24.04.) · ✅ Spec v0.2 (Mobile) · ✅ Plan v0.2.1 3-fach-reviewed (Mobile) · ✅ **Execution** (Session 1 heute, 8 Tasks + Section A) · ✅ **Sync-Welle** (STATE + CORE-MEMORY) · ✅ **Codex-Reconciliation** · ✅ **Option-B-Compression** (86→71 Zeilen, Spec-Ziel erreicht) · ⏳ **CodeRabbit-Pass** (Session 2) · ⏳ **Vault-Update-Sweep** (Session 2).

> **🔄 RESUME-INPUT (Session 2 — CodeRabbit + Vault, 2026-04-24 Session-1-Ende):**
>
> **Auftrag:** Externe System-Integration des abgeschlossenen Refactors: (1) CodeRabbit-Pass via WSL, (2) Vault-Update-Sweep.
>
> **Sequenz für Session 2:**
> 1. `Session starten` → STATE.md (Default) lesen, kompakte Zusammenfassung ziehen
> 2. SESSION-HANDOVER.md (diese Datei) — dieser Resume-Block
> 3. **CodeRabbit-Pass** via WSL (Memory `coderabbit_cli_via_wsl.md` kanonisch):
>    ```bash
>    wsl.exe -- bash -lc 'cd "/mnt/c/Users/tobia/OneDrive/Desktop/Claude Stuff" && coderabbit review --plain --base d025c7f --config /dev/null'
>    ```
>    Commit-Range: `d025c7f..HEAD` (12 Commits). Erwartete niedrige Finding-Rate bei Markdown-Refactor; potenzielle Findings: Typos, interne Link-Breaks, Tabellen-Konsistenz. **Sequenz Codex→CodeRabbit** bereits korrekt gelaufen (Codex war Session 1).
> 4. **Vault-Update-Sweep** — Prüfe zuerst ob `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/CLAUDE-md-Konstitution.md` existiert; falls ja: strukturell aktualisieren auf neue 7-Section-Struktur (SESSION-INIT / Verhalten / KontLernen / Projektstruktur / Routing-Table / Wiki-Modus / Pointer). Falls nein: neue Konzept-Note anlegen wenn sinnvoll, oder als Backlog-Punkt notieren.
> 5. Nach Session 2 Abschluss: **Session 3 Brainstorm-Kandidat** = 00_Core Perfect-Organization (siehe STATE.md #12)
>
> **Spec/Plan-Anker (historisch):**
> - Spec v0.2: `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md`
> - Plan v0.2.1: `docs/superpowers/plans/2026-04-24-claude-md-routing-refactor.md`
>
> **Resultate Tier 1 (für CR-Context):**
> - CLAUDE.md 97→71 Zeilen (Spec-Ziel ~70 erreicht)
> - 2 neue SSoT-Files: `00_Core/APPLIED-LEARNING.md` (14/20 Bullets, v2.5) + `00_Core/TOKEN-RULES.md` (Accessibility-Modell)
> - Neue `## Routing-Table` (9 Trigger + 3 Edge-Cases + Hybrid-Match) ersetzt On-Demand-Lektüre
> - `## Pointer (Ausgelagertes)` 4 Zeilen (AL/Token/Instruktionen/Meilensteine-Archiv — User-Entscheidung gegen Info-Verlust, AC #8 dokumentiert abweichend)
> - Sync-Welle: STATE.md Pipeline-SSoT (Tier-1 als DONE #5 + Renumber-Kaskade) + CORE-MEMORY §1-Eintrag
> - Codex-Reconciliation: RECONCILED_WITH_FOLLOWUPS, alle 3 Findings abgearbeitet
>
> **Commits-Übersicht Session 1 (Baseline `d025c7f`):**
> `9ae0dcc`(AL) → `81829b5`(Token) → `e586d27`(remove) → `3e81a14`(KontLernen) → `ca66785`(Routing) → `2a67221`(Pointer-4Z) → `b99cf3b`(AC-Marker) → `1bd7492`(AL v2.5) → `3f76917`(STATE) → `0964d85`(CORE-MEMORY) → `1e79386`(Codex-Fix#3) → `3bd8632`(Option-B-Compression 86→71) → `a555a1b`(Handover+Deferred#12) → `d069b85`(TOKEN-RULES-CrossRef zu SKILL.md)
>
> **Execution-Mode für Session 2:** Direkt-Editieren (Markdown), kein Subagent-Mode (CLAUDE.md Applied-Learning Bullet #1). CodeRabbit ist externer Subprocess (keine Subagent-Problematik).
>
> **Untracked Working-Tree-Items (unverändert, informativ):**
> - `03_Tools/Rebalancing_Tool_v3.4.xlsx` — Excel-Autosave
> - `.claude/scheduled_tasks.lock` + `.claude/worktrees/` — Runtime-Files
>
> **Push-Status:** Alle 14 Commits LOKAL auf `main`. Kein `git push`. Briefing-Sync per `!SyncBriefing` falls User das will (00_Core/-Edits in STATE+CORE-MEMORY+APPLIED-LEARNING+TOKEN-RULES+SESSION-HANDOVER vorhanden).

---

## 📦 ABGESCHLOSSENE ARBEIT (2026-04-24 — Brainstorm/Spec/Plan CLAUDE.md-Routing)

### Original-Brainstorm-Input (für historische Referenz)

> Brainstorm **mitten in der Arbeit pausiert**, nicht frisch starten. Desktop-Session war Opus 4.7 + `superpowers:brainstorming`-Skill aktiv. Sections 1+2 approved, nächste Schritte glasklar.
>
> **Auftrag für Mobile-Session:** Direkt Section 3 (Routing-Table-Entwurf) präsentieren + User-Approval einholen. Sections 1+2 **nicht wiederholen** — bestätigt. Skill `superpowers:brainstorming` aktiv halten (Section-by-Section + Approval-Gate + HARD-GATE keine Implementation bis Spec-Approval).
>
> **Scope Tier 1 (diese Session):**
> - CLAUDE.md von ~150 auf ~70 Zeilen
> - Zwei neue Files: `00_Core/APPLIED-LEARNING.md` + `00_Core/TOKEN-RULES.md`
> - Projekt-lokal (nicht User-Level)
> - **Kein struktureller Reorg** außer den 2 neuen Files, keine Umbenennungen
>
> **Ziel-Gliederung CLAUDE.md (5 Top-Level, ~70 Z., User-revidiert):**
> ```
> # SESSION-INITIALISIERUNG
>   ## Pflicht-Read
>   ## Verhalten                (Sync-Pflicht, CORE-MEMORY live, briefing-sync §25, remote-Control)
>   ## Kontinuierliches Lernen  (3-Tier knapp, Details in APPLIED-LEARNING.md)
> ## Projektstruktur           (UNVERÄNDERT)
> ## Routing-Table (Read/Skip/Skill)  (NEU — Jakes #3, ERSETZT On-Demand-Lektüre)
> ## Wiki-Modus                (Trigger + Pointer zu WIKI-SCHEMA.md)
> ## Pointer (Ausgelagertes)   (NEU — → APPLIED-LEARNING, TOKEN-RULES, INSTRUKTIONEN)
> ```
> Begründung der Revision: Verhalten + Kontinuierliches Lernen sind Wenn-Dann-Regeln die bei Session-Start triggern — gehören unter Session-Init, nicht Top-Level. Pointer ans Fuß-Ende (Inhaltsverzeichnis-Logik).
>
> **Entscheidungen (verbindlich, Desktop):**
> - **A = ja:** Routing-Table **ERSETZT** die existierende On-Demand-Lektüre-Liste (keine Duplizierung, vermeidet Drift)
> - **B = c:** TOKEN-RULES **Accessibility statt Enforcement** — Regeln liegen vor, via Pointer nachlesbar, **kein Enforcement-Mechanismus**. Spec muss das explizit sagen.
> - **Variante B Hub** für STATE.md (Tier 2, DEFERRED — nicht diese Session)
> - **Projekt-lokal** beide neuen Files
> - **Kein Codex jetzt** (erst nach Spec-Draft, Memory `feedback_review_stack.md`)
>
> **Deferred (Spec unter „Future Work" notieren):**
> - **Tier 2** STATE.md 3-Split Variante B (Hub): STATE.md bleibt als ~10-Z-Hub + Banner + Pointer; darunter `00_Core/PORTFOLIO.md` (Portfolio-State + Watches + 30d-Trigger, konsolidiert mit 🟠 Portfolio-Triggers-Block) / `00_Core/PIPELINE.md` (Pipeline-SSoT 🔴/🟡/🔵 + Long-Term-Gates ⏰) / `00_Core/SYSTEM.md` (System-Zustand + Audit + Backlog). Erwartet ~70% Session-Start-Cost-Reduktion. Separate Session.
> - **Tier 2b** CORE-MEMORY.md Subkategorisierung (kalendarische Riesen-Liste → Subkategorien + Verknüpfung mit adressierten System-Elementen). User beiläufig geparkt.
> - **Tier 3** `vault_backlinks`-Check-Erweiterung auf Root-Ordner. Bereits Backlog-Punkt STATE.md Z. 120.
>
> **Advisor-Blind-Spots (alle addressieren im Spec):**
> 1. **Pain #1 nur halb adressiert.** Spec ehrlich: Tier 1 löst Kategorie **B** (projekt-eigen, ~308 Z.). Kategorie **A** (Harness: Skill-Listings + Tool-Deferred + MCP-Instructions + System-Reminders) bleibt **out-of-scope** dieser Runde.
> 2. **TOKEN-RULES = (c) Accessibility**, nicht Enforcement — explizit schreiben.
> 3. **Routing-Table ersetzt** On-Demand-Lektüre — nicht paralleles Dasein.
>
> **Pre-Spec-Checklist (vor Spec-Finalisierung abarbeiten):**
> 1. Governance-Text mitmigrieren nach APPLIED-LEARNING.md: 12/20 Bullets + Historie v1.0-v2.4 + Proaktive-Pflege-Regel (Monats-Übergang 5-Min-Scan) + Kurator-Regel-bei-Überlauf (15/20-Ziel).
> 2. Pre-Move-Grep: `grep -rn "Applied Learning\|Token-Effizienz" 00_Core/ 01_Skills/ 03_Tools/ docs/` — externe Referenzen finden, die beim Move brechen könnten.
> 3. Tier 2b CORE-MEMORY im Spec unter „Deferred / Future Work" mit 2-Zeiler (Problem + Lösung).
> 4. Revision History im Spec: Handover-verworfene STATE-Split-Entscheidung heute 2026-04-24 mit feinerer 3-Teilung + Variante-B-Hub revidiert. Bezug Memory `feedback_multi_source_drift_check.md`.
>
> **Trigger-Words-Kandidaten für Section 3 Routing-Table:**
> - `Session starten` → Default, Pflicht-Read STATE.md
> - `!Analysiere <Ticker>` → INSTRUKTIONEN + Faktortabelle + Wissenschaftliche-Fundierung-DEFCON + Skill `dynastie-depot` + Skill `backtest-ready-forward-verify`
> - `!Rebalancing` → INSTRUKTIONEN + KONTEXT
> - `!QuickCheck <Ticker>` → Faktortabelle + Skill `quick-screener`
> - `!SyncBriefing` → §25
> - Wiki-Ops (`ingest`/`lint`/`query`/Obsidian/Vault/Faktortabelle-Edit/Score-Update/Insider-Scan) → WIKI-SCHEMA.md
> - `remote-Control`/mobile weiter → Memory `remote-trigger-api.md` (User-Präferenz: **nur manuell**, keine auto-Routine — /remote-control Slash erzeugt Link/QR-Code)
> - Konsolidierungstag/System-Audit/Backlog → SYSTEM/PIPELINE-relevant (Tier 2 aktuell STATE.md §Pipeline+§System)
>
> Format-Vorschlag: `| Trigger | Lies zusätzlich (über Pflicht-Read hinaus) | Skippe | Skill-Call |`. Robuste Trigger-Klassifikation: bei Miss besser konservativ mehr laden.
>
> **Content-Migration-Templates (Section 4):**
>
> `00_Core/APPLIED-LEARNING.md`:
> - Frontmatter: `type: learning-log`, `updated: 2026-04-24`
> - Sections: Kuratierte Bullets (12/20) · Proaktive-Pflege-Regel · Kurator-Regel-bei-Überlauf · Historie v1.0-v2.4
> - Inhalt **unverändert** aus heutiger CLAUDE.md-§ „Applied Learning" übernehmen
>
> `00_Core/TOKEN-RULES.md`:
> - Frontmatter: `type: ruleset`, `scope: projekt-weit referenzierbar (Accessibility-Modell, kein Enforcement)`
> - Sections: Accessibility-Hinweis (explizit „kein Enforcement, Verfügbarkeit") · Regeln (Snapshot-First, Sync-Pflicht alle sechs, Pause-Regel, DEFCON 1 Stopp, MCP lazy-load, Modell-Default)
> - Inhalt aus heutiger CLAUDE.md-§ „Token-Effizienz (operativ)" übernehmen
>
> **Arbeits-Modus für Mobile-Session:**
> - Section-by-Section + User-Approval (kein Sprung)
> - Approval nach Section 3 (Routing-Table) einholen
> - Approval nach Section 4 (Content-Migration) einholen
> - Dann Spec schreiben: `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md`
> - Self-Review (Placeholder/Consistency/Scope/Ambiguity) → User-Review
> - **HARD-GATE:** keine Write/Edit an CLAUDE.md oder neuen Files ohne Spec-Approval
> - Dann `superpowers:writing-plans` für Implementation-Plan
> - Codex erst nach Spec-Draft (Reviewer-Matrix, Memory `feedback_review_stack.md`)
>
> **Git-Stand (bereits auf `main` gepusht):**
> - `2f6e8ba` docs(handover): Brainstorm-Input CLAUDE.md-Routing
> - `7baa543` ingest-video(third-run): Jake Van Clief Folder-System
> - Uncommitted am Desktop (informativ): `03_Tools/Rebalancing_Tool_v3.4.xlsx` (Excel-Autosave, vermutlich Revert), `.claude/scheduled_tasks.lock` + `.claude/worktrees/` (Runtime, .gitignore-Kandidaten)
>
> **Quellen-Referenzen** (bei Bedarf nachlesen, nicht automatisch):
> - Jake-Wiki-Source (7 Mechaniken + Adoption-Matrix): `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/sources/videos/updating-system/2026-03-10-jake-van-clief-folder-system-ai-agents.md`
> - Dubibubii-Präzedenz: `…/2026-04-22-dubibubii-claude-code-powerful-settings.md`
> - Memory: `feedback_friction_as_evidence.md`, `feedback_multi_source_drift_check.md`, `feedback_review_stack.md`, `feedback_information_loss_aversion.md`
>
> **Startpunkt Mobile-Session:** Kurze State-Confirmation (1-2 Sätze: „Brainstorm-State übernommen, setze mit Section 3 fort"), dann direkt Section 3 (Routing-Table-Entwurf) präsentieren + Approval-Gate. **Nicht** Section 1 oder 2 wiederholen — bestätigt.

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
