# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 ~Mittag — **Provenance-Gate Plan-Refresh-Prep DONE.** Brainstorming-Skill durchlaufen, Codex 2× sparring, 4 parallele Recon-Agenten dispatched + reviewed. **Decision: Plan v3 = A+ (Drift-Patch + Carryover-Substring-Whitelist + Task-6-Union-Scope).** Resume-Trigger ab hier: **„Provenance-Gate v3 schreiben"** (kontextfrei in fresh session, alle Anker liegen in diesem Banner).

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `338191b` (STATE.md Last-Audit-Refresh, 27.04.). Keine Uncommitted-Changes. Push synchron mit `origin/main`.

**Was diese Session GETAN hat:** Stale Plan v2 (`docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md`) + Spec (`docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`) gegen aktuellen System-Stand abgeglichen. 7 Tage Drift seit Plan-Schreiben (00_Core-Split, CLAUDE.md-Routing-Tier-1, Briefing v3.0.5, TMO Q1 23.04. ohne Gate appendiert). Codex Round 1: A+ empfohlen mit 2 HIGHs (§18-Union-Scope, Carryover-Policy). 4 Recon-Agents parallel: schemas.py-Anchors / SKILL+smoke+archive-Anchors / STATE→PORTFOLIO-Sweep / 00_Core-Authority-Recon. Synthese gemacht, Codex Round 2 mit 2 neuen HIGHs: parse_state_row-Helper-Verifikation + Carryover-Whitelist-Mechanismus. **Beide HIGHs resolved:** Helper ist vollständig auf PORTFOLIO.md (`REQUIRED_TOUCH_FILES = ("PORTFOLIO.md", "Faktortabelle.md", "log.md")`), Carryover-Policy = Substring-Whitelist (Option C, User-approved).

**Kein Code geschrieben in dieser Session.** Nur Diagnose + Decisions. Schreiben erfolgt in fresh session.

---

### 📋 Offene Tasks (fortgeführt in fresh session)

TaskList beim Session-Start lesen — Tasks #1-5 existieren bereits:
- ✅ #1 Kritische Review der 4 Agent-Outputs — completed
- ⏳ #2 Spec v2 schreiben — pending (NEXT)
- ⏳ #3 Plan v3 schreiben — pending (nach Spec v2)
- ⏳ #4 Spec + Plan committen
- ⏳ #5 User-Review-Gate

---

### 🎯 Ziel-Artefakte (fresh session schreibt diese)

**Datei 1: `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`** (überschreiben — Status: draft → v2)

**Datei 2: `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md`** (überschreiben — v2 → v3)

Architektur unverändert: **Variante E (Hybrid)** — Schicht B `provenance_gate.py::check_provenance` 8 Checks fail-close + Schicht D `ScoreRecord._check_vollanalyse_block_coverage` Schema-Guard + SSoT `versions.py::DEFCON_ACTIVE_VERSION`.

---

### 🔧 Spec v2 — Patches gegenüber 21.04.-Draft

1. **§5.2 Check #7 Carryover-Policy (NEU):** Substring-Whitelist-Mechanik:
   ```python
   PLATZHALTER_BLACKLIST: Final[frozenset[str]] = frozenset({
       "unknown", "tbd", "todo", "placeholder", "none", "na", "n/a", "?",
   })

   CARRYOVER_LEGITIMATE_TOKENS: Final[frozenset[str]] = frozenset({
       # Source-Substrings
       "gurufocus", "defeatbeta", "shibui", "openinsider", "sec_edgar",
       "yahoo", "zacks", "yfinance", "alphaspread", "tavily",
       "ir_", "stocktitan", "benzinga", "afm", "amf", "eodhd",
       # Reason-Substrings (workflow-Gründe)
       "skip_window", "pre_score", "pre_gate", "bridge", "carry_from",
   })

   def _is_placeholder(value: str) -> bool:
       stripped = value.strip().lower()
       if stripped in PLATZHALTER_BLACKLIST:
           return True
       if stripped.endswith("_carryover"):
           prefix_part = stripped[:-len("_carryover")]
           if not prefix_part:
               return True
           if not any(tok in stripped for tok in CARRYOVER_LEGITIMATE_TOKENS):
               return True
           return False  # legitimer Carryover
       return bool(_RE_QUESTION_MARKS.fullmatch(stripped))
   ```
   Akzeptiert: `gurufocus_carryover`, `skip_window_delta_lt_14d_pre_score_carryover`, `defeatbeta_carryover`. Lehnt ab: `xyzzy_carryover`, `unknown_carryover`, `_carryover`, `tbd_carryover`.

2. **STATE→PORTFOLIO-Sweep im Spec selbst:**
   - Z. 231: `parse_state_row(ticker, STATE.md)` → `parse_state_row(ticker, state_md_content)` (Funktionsname stabil, Doku: "from PORTFOLIO.md Portfolio-Tabelle")
   - Z. 232: `validates record gegen STATE.md` → `validates record gegen PORTFOLIO.md`
   - Z. 289 + 310 Test-Cases: `freshness_missing=["STATE.md"]` → `["PORTFOLIO.md"]`
   - Z. 267 Recovery: `(STATE/Faktortabelle/log.md touch)` → `(PORTFOLIO/Faktortabelle/log.md touch)`
   - Z. 340 Follow-up TMO: "TMO Q1 am 23.04.2026 (bereits in STATE.md Trigger-Liste)" → **TMO 23.04. ist bereits OHNE Gate appendiert (Record #28); fungiert als Pre-Gate-Audit-Subjekt für Plan-v3-Pre-Check (Step 0.1).** Neuer First-Live-Run = nächste !Analysiere-Vollanalyse nach Deploy.

3. **§10 Future-Compatibility um B27 ergänzen:** Nach B18/B20-Notes: `[[Ke-Huddart-Petroni-2003]] (B27, design-context, Phase-B paper-ingest 22.04.) → insider-intelligence v2 mit 24-Monats-Sell-Window deferred. Aktueller Block-Coverage-Validator nimmt insider-Block explizit aus (keine Roh-Felder in MetrikenRoh). Bei v2-Aktivierung würde diese Skip-Annahme falsch — dann Block-Coverage-Validator um insider-Block-Mapping erweitern.`

4. **§5.3 Block-Coverage-Validator Dual-Naming-Note:** technicals-Block muss BEIDE Field-Aliases prüfen:
   ```python
   "technicals": (
       "rel_strength_sp500_6m_pct", "rel_staerke_sp500_6m_pct",  # Dual-Naming, _sync_rel_staerke_alias spiegelt
       "kurs_vs_200ma_pct", "ma200_slope",
   ),
   ```
   `any()` über alle Felder — funktioniert auch ohne den `_sync_rel_staerke_alias`-Validator-Run, der ohnehin VOR `_check_vollanalyse_block_coverage` läuft (Pydantic mode=after sequenziell).

---

### 🔧 Plan v3 — Patches gegenüber Plan v2

**A) Re-Anchoring (alle Code-Edit-Anker neu — verifiziert via Recon-Agents 28.04.):**

| Datei | Plan-v2-Anker | Plan-v3-Anker (verifiziert) |
|---|---|---|
| schemas.py `_check_forward_version` | Z. 316-323 | **Z. 317-324** |
| schemas.py `_check_quality_trap` | Z. 410 | **Z. 363-411** |
| schemas.py Insertion neuer Validator `_check_vollanalyse_block_coverage` | nach Z. 410 | **Z. 412-413** (zwischen `_check_quality_trap`-Ende Z. 411 und `class FlagEvent` Z. 418) |
| schemas.py `class ScoreRecord` | implizit | **Z. 286** |
| schemas.py `class MetrikenRoh` | implizit | **Z. 224**, Felder Z. 230-265 |
| schemas.py `_smoke_tests()` | nach Case 7 | **nach Case 10** (Z. 824-840), neue Cases D1-D4 ab Z. 841. **Test-Erwartung: 14 Cases (10+4), nicht 11.** |
| archive_score.py `_build_valid_forward_record` | Z. 352-356 | **Z. 281-365** (Funktionsstart Z. 281, metriken_roh-Block Z. 352-356 stabil — Plan-v2-Patch korrekt) |
| SKILL.md Phase-Tabelle | Z. 92-100 | **Z. 96-107** |
| SKILL.md P3.5-Insertion-Point | impliziert | **Z. 144** (vor `### P3 — Algebra-Δ-Gate` Z. 145) |
| SKILL.md Stdout-Report Section | Z. 206-209 | **Z. 195** (Section-Header) / **Z. 214-216** (Error-Zeile mit `<P1\|P2b\|P4\|P5\|P6>`) |
| SKILL.md Authoritative-Sources Tabelle | Z. 46-54 | **Z. 50-60** (Insertion neuer Einträge **Z. 61**) |
| _smoke_test.py CASES | Z. 498-505 | **Z. 498-505** (stable) |
| _smoke_test.py case_7 Insertion | Z. 495 | **Z. 495** (stable) |
| _smoke_test.py Imports | Z. 180-190 | **Z. 180-186** |
| _smoke_test.py Fixture-Variable | `STATE_MD_FIXTURE` | **`PORTFOLIO_MD_FIXTURE`** (Z. 39 — bereits umbenannt) |

**B) Pflicht-Touch-Files-Realität (Helper bereits migriert):**
- `_forward_verify_helpers.py::REQUIRED_TOUCH_FILES = ("PORTFOLIO.md", "Faktortabelle.md", "log.md")` (Z. 25)
- `parse_state_row` Docstring: "from PORTFOLIO.md Portfolio-Tabelle" — Funktionsname backwards-compat, Inhalt PORTFOLIO.md
- `check_freshness` Docstring: explizit `PORTFOLIO.md, Faktortabelle.md, log.md`
- **Konsequenz:** Plan-v3-Test-Cases nutzen `freshness_missing=["PORTFOLIO.md"]` (vollanalyse-Fail) bzw. `["PORTFOLIO.md", "log.md"]` (Backfill-Skip). Plan-v3 dokumentiert Mock-Konvention explizit ("Tests mocken aus REQUIRED_TOUCH_FILES — wir testen Gate-Logik, nicht Helper-Output").

**C) Task 4.1 SKILL.md schrumpft:** Vorher-Block in Plan v2 referenzierte `parse_state_row(ticker, STATE.md)` — heute steht da bereits `parse_state_row(ticker, PORTFOLIO.md)` (SKILL.md Z. 102). Plan-v3-Task 4.1: nur reine P3.5-Phase-Einfügung in Tabelle, kein STATE→PORTFOLIO-Patch.

**D) Baseline 27→28 Records:**
- Plan v2 Z. 13, 62, 1099, 1100, 1148, 1154 — alle Stellen
- TMO 23.04. Record #28 ist appendiert (forward + vollanalyse + alle Felder befüllt + carryover-quellen). Ohne Gate gelaufen.
- Plan v3 Step 0.1 Pre-Check erwartet `PASS: 28 / FAIL: 0` (NICHT 27).
- Plan v3 VC.2: `wc -l` erwartet **28**.
- Plan v3 Task 2.7 Re-Validate-Sweep: 28 Records prüfen, **TMO-Record muss Block-Coverage passieren** (alle 4 Blöcke befüllt — verifiziert via TMO-quellen-Inspektion, alle 5 quellen belegt, alle metriken_roh-Felder gesetzt inkl. Dual-Naming).

**E) TMO-First-Live-Run-Relabel (4 Stellen):**
- Spec Z. 340: First-Live-Run-Annahme → Pre-Gate-Audit-Subjekt (siehe oben)
- Plan Z. 1100: "First-Live-Run erwartet: TMO Q1 23.04.2026" → **"Pre-Gate-Audit-Baseline: TMO Q1 23.04.2026 (Record #28, ohne Gate appendiert; muss Plan-v3-Step-0.1-Pre-Check + Task-2.7-Re-Validate-Sweep passieren)"**
- Plan Z. 1123: "First-Live-Run-Eintrag bei TMO Q1 23.04.2026 als zweiter §10-Block" → **streichen** (kein zweiter Eintrag, TMO ist Pre-Existence)
- Plan Z. 1164: "First-Live-Run bei TMO Q1 23.04.2026: Erwartete Pipeline-Sequenz im Erfolgsfall" → **streichen** (Hypothese obsolet, war pre-deploy gedacht)
- **Neuer First-Live-Run-Erwartungstext:** nächste !Analysiere-Vollanalyse nach Deploy. Kandidaten: V Q2 28.04. (heute) ODER MSFT Q3 29.04. (morgen) — abhängig davon, wann Plan v3 executiert wird. Eigener CORE-MEMORY-Eintrag mit Pipeline-Sequenz-Result.

**F) Authority-Mapping Task 6 (Codex HIGH-1 §18-Union-Scope):**

§18 v2.1 ist event-typed (4 Event-Typen mit File-Sets) + §18.2 Multi-Event-Union-Regel. Go-Live = System-Event (SYSTEM.md+log.md) + Doku-Edits (INSTRUKTIONEN+CORE-MEMORY). **Sync-Set = Union: `SYSTEM.md + log.md + INSTRUKTIONEN.md + CORE-MEMORY.md`** (kein PIPELINE.md, kein Score-Event-Set).

- **Task 6.1:** Ziel-Datei **`00_Core/SYSTEM.md`** (NICHT STATE.md). Insertion: direkt nach Z. 20 Forward-Verify-Pipeline-Bullet (kohärent — beide score_history.jsonl-Pipeline). Wortlaut: `**Provenance-Gate aktiv** (seit YYYY-MM-DD, Schicht B + D): provenance_gate.py::check_provenance läuft als Phase P3.5 zwischen P2b und P3 in backtest-ready-forward-verify. Acht Checks fail-close (Backfill-Skip / Freshness / Kurs-Referenz / Skill-Meta-Pflicht / Delta-Forward / Version-Drift / Platzhalter+Carryover-Whitelist / Recycled-Meta). Schema-Validator _check_vollanalyse_block_coverage als Schicht D gegen Direkt-CLI an archive_score.py. SSoT-Version in versions.py::DEFCON_ACTIVE_VERSION.`

- **Task 6.2:** **`00_Core/INSTRUKTIONEN.md §18.5`** als neue Sub-Section nach §18.4 (Stand-Footer-Konvention). Wortlaut: `### 18.5 Provenance-Gate für Score-Appends (seit YYYY-MM-DD, v3.7.4)\n\nScore-Append läuft via backtest-ready-forward-verify Skill, das nun Phase P3.5 (Provenance-Gate, fail-close) zwischen P2b und P3 ausführt. Bei FAIL phase=P3.5 gibt es keinen --force-Bypass — Recovery durch Workflow-Korrektur (Pflicht-Touch-Files berühren / analyse_typ umklassifizieren / quellen-Felder mit echten Quellen oder legitimen *_carryover-Suffixen befüllen / Versions-Drift via Migration-Pipeline lösen). Carryover-Token-Whitelist in 03_Tools/backtest-ready/provenance_gate.py::CARRYOVER_LEGITIMATE_TOKENS.` (Plus §18-Versionsgeschichte: `v2.1 → v2.2 (YYYY-MM-DD): §18.5 Provenance-Gate-Klausel ergänzt.`)

- **Task 6.3:** **`00_Core/CORE-MEMORY.md`** — neue Subsection unter **§10 "API-Audit-Log"** (Z. 277). Empfehlung Codex: §10 = Audit-Log-Pattern passt thematisch. Alternative §11 "Backtest-Ready Infrastructure" Z. 386 — semantisch näher zur Pipeline. **Plan v3-Wahl: §10**, weil Audit-Log-Format etabliert ist und Provenance-Gate ein Audit-Mechanismus ist. Wortlaut: `### YYYY-MM-DD — Provenance-Gate Go-Live\n\n- Was deployed: P3.5 fail-close in backtest-ready-forward-verify (Schicht B provenance_gate.py mit 8 Checks inkl. Carryover-Whitelist) + Schicht D ScoreRecord._check_vollanalyse_block_coverage + SSoT versions.py::DEFCON_ACTIVE_VERSION.\n- Plan: docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md (v3, refresh 28.04.). Spec: ...-design.md (v2).\n- Pre-Check vor Execution: 28/28 PASS (Step 0.1).\n- Smoke-Tests post-Execution: schemas 14/14 + archive_score 5/5 + provenance_gate 9/9 + skill 7/7.\n- Pre-Gate-Audit-Baseline: TMO Q1 23.04.2026 Record #28 (ohne Gate appendiert, alle Provenance-Felder gesetzt).\n- First-Live-Run erwartet: nächste !Analysiere-Vollanalyse nach Deploy (V 28.04. oder MSFT 29.04.).\n- Promotion-Trigger: nach 3-4 realen Anwendungen Applied-Learning-Scan.`

- **Task 6 Commit-Message:** Sync-Set explizit nennen: `git add "00_Core/SYSTEM.md" "00_Core/INSTRUKTIONEN.md" "00_Core/CORE-MEMORY.md" "00_Core/log.md"` (log.md = §18.2-Union-Pflicht für System-Event).

**G) Test-Mocks STATE.md → PORTFOLIO.md (alle Stellen):**
- Plan v2 Z. 571-577 (provenance_gate.py Case 2): `freshness_missing=["STATE.md"]` → `["PORTFOLIO.md"]`
- Plan v2 Z. 630-631 (Case 6 Backfill-Skip): `freshness_missing=["STATE.md", "log.md"]` → `["PORTFOLIO.md", "log.md"]`
- Plan v2 Z. 887-889 + 932 + 953 (case_7 Integration-Test): alle `STATE.md` → `PORTFOLIO.md`
- Plan v2 Z. 936-939 (P2b Tripwire-Erwartung "ZTS not in STATE.md"): → "ZTS not in PORTFOLIO.md"

**H) Schemas-Cases-Erwartung anpassen (Plan v2 Task 1.3 + Task 2.4):**
- Plan v2 erwartete `[OK] all schema smoke tests passed` (7/7)
- Aktueller Stand: schemas.py hat 10 Cases (PortfolioReturnRecord Case 8/9 + BenchmarkReturnRecord Case 10 seit 21.04. nachgerüstet, commit `404b057`)
- Plan v3 erwartet: `Run: python schemas.py` → `[OK] all schema smoke tests passed` (10 Cases vor Validator-Add). Nach D1-D4-Cases-Add: 14 Cases.

---

### ⚠️ Sonstige Drift-Verifikation (Codex Round 2 LOW)

- §18-Strategie: §18.5 als neue Sub-Section + Versionsgeschichte-Bump v2.1→v2.2 (Codex empfohlen, weil §18 normative Versionsgeschichte hat)
- check_freshness-Mock-Konvention dokumentiert in Plan v3 Task 5 / Spec §8.3 (Test mockt aus REQUIRED_TOUCH_FILES, nicht Helper-Output)
- _check_record_id ist field_validator (Z. 307-315), läuft VOR allen model_validators — relevant nur falls Record-ID-Validierung Carryover-Pattern beträfe (sie tut nicht — Record-ID-Format ist `YYYY-MM-DD_TICKER_TYP`)

---

### 🚀 Fresh-Session-Workflow

1. Session startet: STATE.md + PORTFOLIO.md geladen (default). Diesen Banner lesen. dynastie-depot-Skill aktivieren NICHT nötig (kein Analyse-Trigger), aber TaskList lesen.
2. Trigger: **„Provenance-Gate v3 schreiben"** oder Resume-Stand fortsetzen.
3. Task #2 in_progress: Spec v2 schreiben (Write-Tool, gesamten File-Inhalt). Spec v1 ist 358 LOC, Spec v2 ähnlich + Carryover-Section + B27-Note + STATE→PORTFOLIO-Sweep.
4. Task #2 completed → Task #3 in_progress: Plan v3 schreiben (Write-Tool, gesamten File-Inhalt, ersetzt Plan v2 1167 LOC). Header-Versionsbump. Alle Anker aus dieser Übergabe-Tabelle einsetzen.
5. Task #3 completed → Task #4: `git add` beide Files + Commit mit klarem Versionierung-Message (`refresh(provenance-gate): Plan v3 + Spec v2 — drift-patch + carryover-policy + task-6-union-scope`). Co-Author-Footer.
6. Task #4 completed → Task #5: User-Review-Gate. „Spec v2 + Plan v3 committed an `<commit-sha>`. Review bitte und gib go/no-go für Execution-Session."

**Geschätzter Aufwand:** ~2h für Spec v2 + Plan v3 schreiben + commit. **Keine Tool-Aufrufe für Recon nötig** — alle Anker und Patches in diesem Banner.

**Wichtig: Schreiben ist atomar.** Karpathy/Surgical-Changes-Prinzip aus CLAUDE.md §0 INSTRUKTIONEN. Keine Refactors über das Provenance-Gate hinaus. Keine Plan-Hub-Splits. Keine Audit-Tool-Integration (war Codex-MEDIUM, abgelehnt als Scope-Creep).

---

### 📅 Critical Operational (parallel zur Plan-Refresh-Session)

- **28.04. (heute) AMC ~22:00:** V Q2 FY26 Earnings — D2-Entscheidung. Pre-Brief `02_Analysen/V_pre-earnings_2026-04-28.md`. !Analysiere V morgens 29.04.
- **29.04. AMC ~22:30:** MSFT Q3 FY26 Earnings — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung). !Analysiere MSFT morgens 30.04.
- **01.05.:** Sparplan-Tag (EXUSA 825€ + reguläre Allokation). User-Action.
- **30.04.+:** 5a Skill-Promotion freigegeben (post-Earnings, separate Session, Plan `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md`).

**Wenn Plan-v3-Schreiben in dieselbe Session fällt wie V/MSFT-Analyse:** zuerst Analyse durchführen (Live-Trigger), dann Plan v3. Plan-v3-Schreiben ist nicht zeitkritisch.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€, DEFCON v3.7
- AVGO 84 (FLAG Insider seit 27.04.), TMO 67 D3 (post-Q1-Upshift 23.04.), MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`

### Memory-Hooks aktiv

- feedback_review_via_codex_not_advisor.md — Reviews via Codex (heute 2× single-pass, Round 2 mit verifiziertem HIGH-1 + Design-HIGH-2)
- feedback_codex_sparring_heuristic.md — Single-Pass Default; HIGH-Count ≥2 = Reconcile-Loop oder Verifikation. Heute: HIGH-1 mit File-Read resolved, HIGH-2 mit User-Decision resolved. Kein dritter Pass nötig.
- feedback_tavily_connector_uuid_rotation.md, feedback_onedrive_edit_collision.md, feedback_pre_commit_diff_inspection.md, feedback_windows_python_crlf_text_mode.md — Standing-Practices

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*
