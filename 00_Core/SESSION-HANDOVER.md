# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-24 Session-4-Ende — **00_Core Perfect-Organization Tier 2 Plan v1.1 BEREIT (Codex-Pre-Execution-reviewed).**

**Summary:**
- Session 1: 16 Commits (Tier-1-Execution + AL v2.5 + Sync-Welle + Codex-Reconciliation + Option-B-Compression 97→71 Zeilen)
- Session 2 (24.04.): Vault-Update `f9d65d1` + CodeRabbit-Pass `4cf0ea9` (8 Findings → 3 Fixes / 5 Declines)
- Session 3 (24.04.): Brainstorm 00_Core Perfect-Organization + Spec v0.3 3-fach-reviewed (Claude+Codex+Advisor). Scope **B**, Entscheidungs-Kaskade G2+H1+R2+V-Kompakt+L2+Outbound-only+Markdown+Kopf. Feature-Branch `refactor/00core-perfect-organization` angelegt.
- Session 4 (heute, 24.04.): **Plan-Session.** 3 Advisor-Flagged-Klärungen User-resolved (1a/2b/3a) → Spec v0.3→v0.4 ratified. Plan geschrieben via `superpowers:writing-plans` (10 Tasks / 101 Steps / 1823 Z). **Codex-Pre-Execution-Review RECONCILED_WITH_FOLLOWUPS:** 4 Findings (F1 🔴 AC #18-Gate explizit · F2 🟡 Atomarity-Drift Spec §8.2 vs. Plan · F3 🟡 Step 9.7 Hard-Pause · F4 ℹ️ Step 3.2 Example-Led) alle inline in Plan v1.1 resolved (1920 Z / 103 Steps final). Spec + Plan beide lokal durable (gitignored per `docs/superpowers/`).

**Acceptance (Spec v0.4):** 18 AC dokumentiert. Scoring-neutral (§28.3). DEFCON v3.7 unverändert. **Spec v0.4-Deltas zur v0.3:** Frontmatter `status: ratified` + `version: v0.4`; §6 PORTFOLIO-Primär-Rationale + Union-Regel-Formalisierung; AC #5 explizite Peer-Liste (10 Files); §10.2 alle 3 Klärungen resolved + Anhang D User-Signoff-Tabelle. **Plan v1.1-Deltas zur v1.0:** Step 2.7 Recovery-Regel, Step 2.8 Commit-Message umformuliert (Feature-Branch-Rationale + Merge-atomic via `--no-ff`), Step 3.2b exhaustive Ticker-Reconciliation, Step 8.4b 4-Surface AC #18-Gate, Step 9.7 🛑 HARD USER-PAUSE + Step 9.8 Gate-Check.

**Pending:**
- **Session 5 (Execution):** `superpowers:executing-plans` auf Feature-Branch `refactor/00core-perfect-organization`. ~3-4h konzentrierte Session. Empfohlene Checkpoints nach Task 2 (Atomic-Cutover) / Task 4 (Scripts-Smoke-Gate) / Task 6 (Governance) / Task 8 (Verification) / Task 9 (Review-Gates). Task 9 enthält Codex-Reconciliation (Step 9.2) + CodeRabbit-Pass via WSL (Step 9.5) + User-Sign-off (Step 9.7 🛑) + Merge `--no-ff` (Step 9.10 User-triggered).

**Vorherige Aktualisierungen:** 2026-04-24 Session-3-Ende — Spec v0.3 ratified · Session-2-Ende — Vault + CR-Pass · Session-1-Ende — 16 Commits Tier 1 · 2026-04-24 Mobile — Brainstorm+Spec+Plan Tier 1 · 2026-04-23 Nachmittag — Phase G (TMO Q1 DONE).

> **Progress-Banner Tier 2 (00_Core Perfect-Organization):** ✅ Brainstorm (Session 3) · ✅ Spec v0.4 ratified · ✅ Plan v1.1 Codex-Pre-Execution-reviewed (Session 4) · ⏳ Execution (Session 5).

> **🔄 RESUME-INPUT (Session 5 — Execution-Session, 2026-04-24 Session-4-Ende):**
>
> **Auftrag:** Plan `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md` v1.1 ausführen via `superpowers:executing-plans`. Branch: `refactor/00core-perfect-organization` (bereits angelegt, noch keine Refactor-Commits). ~3-4h konzentrierte Session empfohlen.
>
> **Setup (erstes im Session-Start):**
> 1. `Session starten` → STATE.md (Default) lesen, kompakte Zusammenfassung (Banner nennt „Session-4-Ende, Plan v1.1 bereit").
> 2. **`git checkout refactor/00core-perfect-organization`** (Branch bereits da; Spec + Plan sind lokal durable via gitignore, bleiben beim Switch erhalten).
> 3. Spec v0.4 skimmen: `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` (Anhänge B-D für Review-Historie).
> 4. **Plan v1.1 laden**: `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md` — 10 Tasks · 103 Steps · 1920 Z. Ganz lesen oder Task-by-Task streamen.
> 5. Diese SESSION-HANDOVER.md (dieser Block).
> 6. `superpowers:executing-plans` Skill-Call mit Plan als Input.
>
> **Execution-Checkpoints (empfohlen, User-bestätigt):**
> - **Nach Task 2** (atomic STATE-Split Cutover, Step 2.8 Commit) — größtes Revert-Risiko, visuelle Verifikation Hub/PORTFOLIO/PIPELINE/SYSTEM-Content.
> - **Nach Task 4** (Scripts-Smoke PASS) — Gate für Skills in Task 5.
> - **Nach Task 6** (Governance-Cutover) — CLAUDE.md + INSTRUKTIONEN §18 neu; schließt Spec-§8.2 Atomarity auf Merge-Zeitachse.
> - **Nach Task 8** (Pre/Post-Artefakt-Diff + AC #18-Gate) — finale Evidence-Sammlung.
> - **Task 9** (Review-Gates) — Codex 9.2/9.3, CodeRabbit 9.5, User-Sign-off 9.7 🛑 HARD PAUSE, Merge 9.10.
>
> **Nicht-Scope Session 5:** Über den Plan hinausgehen. Keine on-the-fly-Feature-Erweiterungen (DEFCON-Bump, Skill-Semantik-Änderungen, Vault-Sanierung). Plan ist binding — Deviations müssen als neuer Task/Step dokumentiert werden oder Execution pausieren.
>
> **Wichtige Notizen für Session 5:**
> - **Spec + Plan sind gitignored** (`docs/superpowers/`). Lokal durable, aber kein Remote-Push. User kann beide in IDE öffnen (Session 4 User hat Spec in IDE geöffnet, Session 5 kann dasselbe mit Plan machen für parallele Nachverfolgung).
> - **Skill-Versions:** `dynastie-depot` v3.7.2→v3.7.3 in Task 5/7; `backtest-ready-forward-verify` 1.0.0→1.0.1 in Task 5/7. Manuelle Desktop-ZIP-Installation in Step 7.5 ist User-Action (Pause markiert).
> - **CORE-MEMORY §1 Session-3-Eintrag** (Desktop-Brainstorm) und Session-4-Eintrag (Plan geschrieben — falls inzwischen appended) werden in Task 3 nach §13 (`[Meta]`-Topic) migriert. Kein Sonderfall.
> - **Codex-Pre-Execution-Review DONE** (Session 4) — Post-Impl Codex-Reconciliation (Step 9.2) ist separater, mandatory Gate laut Review-Stack v2.
> - **Hub-Invarianten** (Spec §3.3, 4 Punkte): HTML-Anker bleiben + Footer-Sentinel bleibt + _smoke_temp_repo.py-Assertions kompatibel + SystemAudit-Command-Contract. Plan Step 2.5 enthält Template mit exakten Markern.
>
> **Aktuelle Uncommitted-Items (informativ, nicht Scope):**
> - `03_Tools/Rebalancing_Tool_v3.4.xlsx` — Excel-Autosave (pre-existing)
> - `.claude/scheduled_tasks.lock` + `.claude/worktrees/` — Runtime
>
> **Push-Status nach Session 4:** Session-4 STATE.md + SESSION-HANDOVER.md Updates werden in Session-Close-Commit auf main gebündelt (kein `git push` bis User `!SyncBriefing` anstößt).
>
> ---
>
> **🗃 RESUME-INPUT (Session 4 — Plan-Session, ARCHIVIERT, DONE 2026-04-24):**
>
> **Auftrag war:** Execution-Plan schreiben für Spec v0.3. Skill: `superpowers:writing-plans`.
>
> **Ergebnis:** 3 Advisor-Klärungen resolved (1a/2b/3a) → Spec v0.4 ratified. Plan v1.0 (10 Tasks / 101 Steps / 1823 Z) geschrieben. Codex-Pre-Execution-Review RECONCILED_WITH_FOLLOWUPS (4 Findings) → Plan v1.1 (103 Steps / 1920 Z). Spec + Plan lokal durable (`docs/superpowers/` gitignored).
>
> ---
>
> **🗃 RESUME-INPUT (Session 2 — CodeRabbit + Vault, ARCHIVIERT, DONE 2026-04-24):**
>
> **Auftrag war:** Externe System-Integration des abgeschlossenen Refactors: (1) CodeRabbit-Pass via WSL, (2) Vault-Update-Sweep.
>
> **Ergebnis:**
> - Vault `f9d65d1`: `CLAUDE-md-Konstitution.md` auf 7-Section-Struktur + Tier-1-Refactor-Subsection + Änderungsprotokoll-Zeile 24.04.
> - CR-Pass `4cf0ea9`: 8 Findings triaggiert → 3 FIX (CLAUDE.md Edge-Cases Case-Drift/Sprach-Varianten, APPLIED-LEARNING Historie-Tabelle, Handover CR-Command-Bug) / 5 begründete Declines (Session-1-SHA-Stable, Quote-Empirisch-OK, Bullet-Count-CR-self-confirmed, Handover-Dense-wird-rebuilt, STATE-Numbering-Konvention, CORE-MEMORY-Dense-Konvention).
>
> **Sequenz war:**
> 1. `Session starten` → STATE.md (Default) lesen, kompakte Zusammenfassung ziehen
> 2. SESSION-HANDOVER.md (diese Datei) — dieser Resume-Block
> 3. **CodeRabbit-Pass** via WSL (Memory `coderabbit_cli_via_wsl.md` kanonisch):
>    ```bash
>    wsl.exe -- bash -lc "cd '/mnt/c/Users/tobia/OneDrive/Desktop/Claude Stuff' && coderabbit review --plain --type committed --base-commit d025c7f --config /dev/null"
>    ```
>    (Bug-Fix 24.04. Session 2: `--base` interpretiert `d025c7f` als Branch-Name → 339 Files > 150-Limit-Crash; `--base-commit` + `--type committed` scopt korrekt auf Diff-Commits. Quelle: Auto-Memory `coderabbit_cli_via_wsl.md` Z. 12.)
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
> **Push-Status:** Alle 16 Commits LOKAL auf `main`. Kein `git push`. Briefing-Sync per `!SyncBriefing` falls User das will (00_Core/-Edits in STATE+CORE-MEMORY+APPLIED-LEARNING+TOKEN-RULES+SESSION-HANDOVER vorhanden).

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
