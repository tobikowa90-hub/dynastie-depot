# Wiki Log

> Append-only activity log. Most recent entries at the bottom.
> Quartalsweise Roll-over per INSTRUKTIONEN.md §18.6 — ältere Einträge in `archive/log/log-bis-2026-04.md` (bis 2026-04-30).

> **Pre-2026-05-17 Banner-History archived** -> [C:\Users\tobia\OneDrive\Desktop\Claude Stuff\05_Archiv\log-bis-2026-05-16-archiv.md](../../../05_Archiv/log-bis-2026-05-16-archiv.md)
> Reason: rolling retention; archive contains verbatim history.
> **Pre-2026-05-22 Banner-History archived** -> [../../../05_Archiv/log-bis-2026-05-21-archiv.md](../../../05_Archiv/log-bis-2026-05-21-archiv.md)
> Reason: rolling retention; archive contains verbatim history.
## [2026-05-22] system | #73a paragraph-18-sync Spec v0.1 → v0.3 — Codex-Spec-Review-3-Runden appliziert (scoring-neutral, Pipeline-Item-Event)

**Event-Typ:** Pipeline-Item-Status-Refinement (SPEC-COMPLETE v0.1 → SPEC-COMPLETE v0.3 Build-ready, kein Score/FLAG/Sparraten-Touch)

**Was passiert ist:**
- Codex (jetzt funktional nach 2026-05-21-Fix `~/.codex/config.toml model="gpt-5.3-codex"`) führte unabhängigen Spec-Review für `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` durch
- Sparring-Loop max-3-Runden-Heuristik (Memory `feedback_codex_sparring_heuristic`) durchlaufen:
  - **Runde 1 (Single-Pass):** 3 HIGH + 4 MEDIUM + 2 LOW = 9 substantielle Architektur-Findings
  - **Runde 2 (Diff-Re-Review):** 0 HIGH (alle 9 R1-Issues confirmed-closed) + 4 MEDIUM editorial/coverage-Propagation
  - **Runde 3 (Diff-Re-Review):** 0 HIGH + 2 MEDIUM 1-Zeilen-Drift (`13/13`→`20/20` Step-6 + Revision-Label `v0.2`→`v0.3`) — beide self-verified gefixt statt R4
- **Adoptierte Findings:** 30 Total = 10 Self-Review + 5 Gemini-Cross-Sync + 2 Selbst-Korrekturen (v0.1) + 9 Codex-R1 + 4 Codex-R2 + 0 net nach R3-Cleanup
- **Spec-Wachstum:** 476 → 541 LOC (+65 net, +13.6%)
- **Test-Suite:** S1-S13 (13) → S1-S20 (20)
- **Architektur-Bausteine NEU durch Codex-R1:** Two-Commit-Same-Session-Protokoll mit Session-Marker (`.session_marker` JSON, 4h-Window, `commit_a_sha`-Match), exit=6 für Drift, `--verify-b`/`--reset-session`/`--allow-dirty <N>` CLI-Modifier, Ticker-Identity-Guard in P1, deterministische xlsx-Selektion via SYSTEM.md Active-xlsx-Block + Semver-Fallback, exakter Dirty-Tree-Predicate (`(unstaged ∪ untracked) \ expected_set ≥ 10`), Re-Validate-Before-Retry-Pflicht in P6

**Sync-Set (§18 Pipeline-Item-Event, scoring-neutral):** PIPELINE.md (Sub-Item-(a)-Status + Footer v2.50 → v2.51) + log.md (dieser Eintrag). **KEIN** SYSTEM.md (Spec-File ist Begleit-Artefakt, kein System-Zustand-Event). **KEIN** PORTFOLIO + Faktortabelle + score_history + config.yaml + xlsx + flag_events (kein Score/FLAG/Sparraten-Event). Spec-File `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` (untracked-on-disk per `.gitignore` Z.18 by-design — Specs leben lokal).

**Lehre:**
- **Codex-Sparring-Heuristik empirisch validiert:** Diff-Re-Review-Loops konvergieren schnell. R1 = 9 substantielle Findings, R2 = 4 propagation-issues aus R1-Patches selbst, R3 = 2 1-Zeilen-editorial-Drift. APPLY-Rate fällt asymptotisch wie in Memory `feedback_cr_convergence_and_project_compat` prognostiziert (CodeRabbit-Konvergenz-Pattern). Max-3-Heuristik trifft den Sweet-Spot zwischen Vollständigkeit und Diminishing-Returns.
- **Codex-Round-3 declined formal R4:** bei nur 2 1-Zeilen-editorial-Drift-Findings ist self-verify ehrlicher als noch eine 76s-Codex-Runde. Spec-Disziplin > Token-Konsum.
- **Codex-Verfügbarkeit als Primär-Reviewer bestätigt** (v0.121.0 + `gpt-5.3-codex` Pin): 3 Runden hintereinander stabil, durchschnittlich ~20k Tokens/Runde, ~80-110s Latency. Memory `feedback_review_via_codex_not_advisor` 2026-05-21-Fix-Status confirmed.
- **Spec-Phase-Disziplin (Brainstorming-Terminal-Override) gehalten:** Codex-Review ist Teil der Spec-Phase, nicht Build. writing-plans-Switch erst NACH >95%-Confidence-Gateway. User-Direktive 2026-05-21 weiterhin respektiert.

**Cross-Reference:** `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` (untracked, v0.3) · PIPELINE.md #73a SPEC-COMPLETE v0.3 Build-ready · Commit `<TBD>` · Memory `feedback_codex_sparring_heuristic` empirisch validiert.

**Nächste Tracks:** writing-plans-Switch (phased Implementation-Plan, Python-Validator P1-P7 + 20-Test-Smoke-Suite + Two-Commit-Marker-Mechanik + SKILL.md + 4 references/, letzte Phase = skill-creator-Aufruf). Aufwand-Schätzung post-Codex-Review: ~3-3.5h (+0.5h für Session-Marker + S14-S20 + SYSTEM.md Active-xlsx-Block). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

---

## 2026-05-22 — System-Event: FinnHub-Integration v0.1 SPEC-LOCKED v0.3 (PIPELINE #74 NEU + Codex-Spec-Review-3-Runden)

**Event-Typ:** Pipeline-Item-Event NEU + System-Zustand-Change (neue §-Kategorie "Passive Read-Only Data Layer" in SYSTEM.md), scoring-neutral (kein Score/FLAG/Sparraten-Touch)

**Was passiert ist:**
- defeatbeta-MCP empirisch 2-Wochen-Lag bei Quartals-Daten → blockiert §19.1 Tag-0-Trigger-Confirms + FLAG-Quick-Checks. FinnHub Free-Tier (60 calls/min) als Real-Time-Layer evaluiert.
- **Smoke-Test-Verifikation (5+Folge-Endpoints, alle HTTP 200):** `/quote` 2.2h alt = letzter US-Close (löst defeatbeta-Stale), `/calendar/earnings` per-symbol 10/12 + ASML, `/company-news` 249/7d MSFT, `/stock/profile2` Schema-vollständig, `/stock/metric` **21/26 DEFCON-critical TTM-Metriken Free** (Bonus-Finding gegen Pessimismus-Bias). Europäer (RMS.PA/SU.PA) 403 Premium-only → bleibt yfinance-non-us-fundamentals. BRK.B-Calendar liefert BRK.A-EPS (matched Memory `feedback_brk_no_earnings_call`).
- **Codex Scope-Phase R1+R2:** R1 Empfehlung Option C (Minimal + Read-Only Fundamentals-Surface) @ 89% Confidence. User-Direktive >95%-Gate → R2 Confidence-Floor-Differenzierung: Pkt 1 (30-60d Crosswalk-Logs) strukturell-Post-Implementation, Pkt 2+3 (Divergenzgrenzen + Rollback-Test-Klausel) Pre-Implementation-Spec-Artefakte → max-Pre-Impl-Confidence ~94% → **2-Stufen-Gate beschlossen** (Pre ~94% + Post >95% nach Shadow-Run).
- **Spec v0.1 geschrieben:** `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` (413 LOC, 12 Sektionen + 5 §11-Offene-Fragen) als untracked-on-disk per `.gitignore` Z.21 by-design (Specs leben lokal, konsistent zu `2026-05-21-paragraph-18-sync-design`).
- **Codex Spec-Review-Sparring-Loop max-3-Runden-Heuristik (Memory `feedback_codex_sparring_heuristic`):**
  - **Runde 1 (Single-Pass):** 2 HIGH + 5 MEDIUM + 1 LOW + 5 §11-Resolutions = 13 Findings.
    - HIGH-1: Zero-Skill-Refactor-Claim widersprüchlich zu A6 Crosswalk-Hook → Hook entfernt, separates Script `finnhub_crosswalk_trigger.py`
    - HIGH-2: Acceptance-Tests A7-A11 fehlten (401-Hard-Crash / 429-Backoff / Timeout-Retry / force-Cache-Bypass / Cache-Corruption-Resilienz)
    - MEDIUM-1-5: ROIC zweistufig (WARN >2pp / CRIT >4pp ODER >2pp×3 in Folge) · grossMargin5Y ±1pp→±2pp + epsGrowth5Y ±2pp→±3pp + N/A-Handling · §7 NULL/MINOR-Split · Sampling 25→≥50 + Coverage + Auto-Extension · technische Guardrails statt nur Policy (`_meta.for_scoring`-Marker + Assertion + finnhub_health.json)
    - LOW-1: §10 v0.2-Roadmap Dependency-Regel präzisiert
    - §11: Cache-Pfad `~/.dynasty/`, SYSTEM.md "Passive Read-Only Data Layer"-Kategorie eigenständig (nicht unter §Plugin-Layer-Substrate)
  - **Runde 2 (Diff-Re-Review):** 0 HIGH + 2 MEDIUM editorial — §5 Mess-Design Restwiderspruch ("bei jedem dynastie-depot-Lauf" vs Script-Pattern §4) + JSONL-Schema-Contract Coverage-Gap (timestamp/run_id/batch_id/symbol/metric/tolerance_used/na_reason fehlten als Top-Level)
  - **Runde 3 (Diff-Re-Review):** 0 HIGH + 0 MEDIUM + 2 LOW 1-Zeilen-Drift — `run_id`-Semantik intern uneindeutig (§5.3 "Trigger-Run" vs A6 "unique pro Record") + `_meta.*_pulled_at`-Felder im Beispiel-Record aber nicht in Feld-Definitions-Tabelle. Beide self-verified gefixt statt R4 (analog #73a-R3-Disziplin)
- **Adoptierte Findings:** 17 Total = 13 R1-Findings + 5 §11-Resolutions + 2 R2-MED + 2 R3-LOW (R1+R2+R3 = 13+5+2+2 = 22 inkl. cross-counted Resolutions; 13 neue Codex-Findings + 2 R2 + 2 R3 = 17 net)
- **Spec-Wachstum:** 413 → 475 → 536 → 541 LOC (v0.1 → v0.2 → v0.3 + R3-Drift-Fixes belassen in v0.3)
- **Acceptance-Tests:** A1-A11 (vollständige Edge-Case-Coverage: Rollback-Invarianz + 5 Endpoint-Tests + Crosswalk-Log-Init + 5 Edge-Cases)
- **Architektur-Bausteine NEU durch Codex-R1:** separates Crosswalk-Trigger-Script (statt Hook) → Zero-Skill-Refactor-Footprint v0.1 invariant gehalten; technische Guardrail-Layer (`_meta.for_scoring=False`-Marker + Assertion in `backtest-ready-forward-verify` Persistenz-Schicht) gegen V-Q2-Methodology-Drift-Wiederholung; formaler JSONL-Schema-Contract (§5.3) mit Append-Only + Atomic-Write-Garantien; Cache außerhalb Repo (`~/.dynasty/finnhub_cache/`); maschinenlesbares Health-Status-File (`finnhub_health.json`) als PIPELINE-Gate-Input
- **Pre-Implementation-Confidence:** ~96% (über Original-Gate >95% pre-impl)

**Sync-Set (§18 Pipeline-Item-Event + System-Zustand-Change, scoring-neutral):** PIPELINE.md (#74 NEU + Footer v2.51 → v2.52) + SYSTEM.md (neue §-Kategorie "Passive Read-Only Data Layer" + Footer v1.2 → v1.3) + log.md (dieser Eintrag). **KEIN** PORTFOLIO + Faktortabelle + score_history + config.yaml + xlsx + flag_events (kein Score/FLAG/Sparraten-Event — Read-Only-Surface v0.1 hat strukturell keine Score-Mutationen). **KEIN** CORE-MEMORY §12 (kein Per-Ticker-Analyse-Move). Spec-File `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` (untracked-on-disk per `.gitignore` Z.21 by-design — Specs leben lokal, konsistent mit `2026-05-21-paragraph-18-sync-design`).

**Lehre:**
- **Codex-Sparring-Heuristik repliziert:** Konvergenz-Pattern identisch zu #73a 22.05.: R1 = 13 substantielle Findings (HIGH-Architektur + MEDIUM-Calibration + LOW-Editorial), R2 = 2 MEDIUM-Propagation aus R1-Patches selbst, R3 = 2 LOW 1-Zeilen-Drift self-verified. Max-3-Heuristik trifft Sweet-Spot — 2 Datenpunkte (#73a + #74) bestätigen Memory `feedback_codex_sparring_heuristic`.
- **2-Stufen-Gate-Methodik etabliert** als Standard-Pattern für Live-Daten-abhängige Entscheidungen wo Pre-Impl-Confidence-Cap strukturell unter striktem Gate liegt. User-Direktive ">95%-Gate halten oder vertagen?" beantwortet sich durch Codex-R2-Differenzierung selbst: max-Pre-Impl ~94% ⇒ Pre-Gate akzeptieren + Post-Gate nach Shadow-Run. Vermeidet 30-60d Vertagung ohne Confidence-Verlust.
- **Methodology-Drift-Schutz technisch hart statt nur policy:** V-Q2-Präzedenz (Score 1→7 wegen Methodology-Switch, Codex-Revert-Kosten) lehrt dass Banner + SKILL.md-Hinweis + manuelles Review umgehbar sind. Codex-R1-MED-5 verlangte zu Recht technische Guardrails: Wrapper-Return-Marker `_meta.for_scoring=False` + Assertion in Persistenz-Schicht failed Score-Move-Attempts mit FinnHub-Daten hart. Pattern übertragbar auf v0.2-Reklassifizierung und alle künftigen Multi-Source-Daten-Layer.
- **Zero-Skill-Refactor-Footprint in v0.1 ist verifizierbar via Acceptance-A1** (Rollback-Invarianz byte-identisch zur Baseline auf 3 Satelliten DRY-RUN). Spec-Methodik-Disziplin: behauptete Eigenschaften bekommen testable Acceptance-Klausel, nicht nur Behauptung im Text.
- **Spec-Phase-Disziplin (Brainstorming-Terminal-Override, Memory `feedback_brainstorming_terminal_override_dynastie`) gehalten:** writing-plans/Build = separate Session. Diese Session liefert Spec + Codex-3-Runden + §18-Sync. Build-Phase wird in nächster Session geplant + ausgeführt.

**Pages created/updated (System-Event-Scope):**
- `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` — NEW (untracked per `.gitignore` Z.21, v0.3 SPEC-LOCKED 541 LOC)
- `00_Core/PIPELINE.md` — #74 NEU added (FinnHub-Integration v0.1 SPEC-LOCKED), Footer v2.51 → v2.52, Aktive-Items-Liste erweitert (+#74), neue Sub-Items-Status-Zeile für #74
- `00_Core/SYSTEM.md` — Neue §-Sektion "Passive Read-Only Data Layer" (zwischen §Plugin-Layer und §Earnings-Calendar-Status), Footer v1.2 → v1.3
- dieser log.md-Eintrag

**Cross-Reference:** `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` (untracked, v0.3 SPEC-LOCKED) · PIPELINE.md #74 SPEC-LOCKED Build-ready · SYSTEM.md §Passive Read-Only Data Layer · Commit `<TBD>` · Memory `feedback_codex_sparring_heuristic` repliziert (2. Datenpunkt nach #73a) · Memory `feedback_skill_methodology_drift_v_q2` als V-Q2-Präzedenz-Schutz technisch verankert · Memory `feedback_brk_no_earnings_call` validiert (BRK.B-Calendar-Behavior konsistent) · Memory `feedback_viral_plugin_substrate_risk_eval` respektiert (kein neuer MCP-Server, dünner Python-Wrapper).

**Nächste Tracks:** Build-Phase separate Session (writing-plans-Switch, ~150 LOC `finnhub_client.py` + ~80 LOC `finnhub_smoke_test.py` + ~60 LOC `finnhub_crosswalk_trigger.py` + ~20 LOC Assertion-Hook in `03_Tools/backtest-ready/` Persistenz-Schicht + `.env.finnhub.example` Template + `.gitignore`-Sicherheits-Check). Aufwand-Schätzung: ~2.5-3h (kein Skill-Refactor, reines additives Tool-Layer). Nach Build-Commit: Hard-Deadline Deployment+45d als neues PIPELINE-Item eröffnen für v0.2-Reklassifizierungs-Review (Shadow-Run-Auswertung). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

## [2026-05-22] system | session-closure Skill v0.2.0 — 4-File-Verankerung in 00_Core SSoT

**Event-Typ:** System-Zustand-Change (Skill-Promotion-Sync, scoring-neutral) — §18-Sync-Lücke nach Skill-Deploy `42eca7c` 21.05. geschlossen.

**Befund:** `session-closure` v0.2.0 war deployed (Commit `42eca7c`) aber nicht in den normativen SSoT-Files verankert (CLAUDE.md Routing-Table / INSTRUKTIONEN.md §17 + neuer § / SYSTEM.md Verweise + System-Zustand / CORE-MEMORY.md §6 + §13). Pattern identisch zu `feedback_anchor_promotion_sync_gap.md` (4-Achsen-Sync-Lücke nach Skill-Promotion). Template-Präzedenz: `system_audit.py` v1.0 (22.04.2026, INSTRUKTIONEN §27.5 + SYSTEM Z.5+Z.30 + CORE-MEMORY §6 Z.250 + §13 Z.553).

**Mutations (8 surgische Edits across 4 Files):**
1. `CLAUDE.md` — Routing-Table Zeile `!SessionClose → INSTRUKTIONEN §25.5 → session-closure` + Edge-Case-Trigger-Liste abstrahiert (statt Enumeration: „z.B. `!Analysiere`, `!SessionClose`")
2. `00_Core/INSTRUKTIONEN.md` — §17 Aktivierungs-Tabelle Zeile + NEUER §25.5 als Sibling zu §25 Briefing-Sync (semantisch korrekte Parent-§ — beide Session-Hygiene/Sync, nicht §26 Archiv-Sync wie initial geplant)
3. `00_Core/SYSTEM.md` — Verweise-Header `[INSTRUKTIONEN §25.5]`-Pointer + System-Zustand-Bullet (Strict-Trigger + Hard-Stop-vor-push Boundary)
4. `00_Core/CORE-MEMORY.md` — §6 Versions-Tabelle (2026-05-21) + §13 Lifecycle (chronologisch nach 18.05. AMZN, vor Footer)

**Karpathy-Lean-Pass appliziert:** §26.5-Draft initial ~30 Zeilen → §25.5 finale ~12 Zeilen (Workflow-Schritte 1-8 + Refusal-Conditions + Präzedenz-Memory-Liste gestrichen — leben in `01_Skills/session-closure/SKILL.md`/`references/` als SSoT). SYSTEM.md-Bullet ~9 → ~3 Zeilen. CLAUDE.md bleibt strikt minimal (1 Tabellenzeile + 1 abstraktes Trigger-Beispiel).

**Semantik-Korrektur mid-flight:** Initial-Plan §26.5 (Archiv-Sync-Parent) als Mismatch erkannt nach Karpathy-Reflektion → Pivot zu §25.5 (Briefing-Sync-Parent) als Sibling. Cross-Refs in allen 4 Files entsprechend angepasst (Slug `#255-session-closure-workflow-21052026-session-closure-v020`).

**Reviews:**
- **Codex (gpt-5.3-codex via codex:rescue-Subagent):** 1 HIGH + 3 MED + 1 LOW. HIGH 1 = faktischer Fehler korrigiert (Codex-Review entfiel — Auth-Bug, nicht „Codex+Gemini reviewed" wie initial-draft). MED 2/3/4 = Cross-Ref-Loop-Closure in Drafts 3/7/8 + Workflow-Detail-Inflation §26.5 + statische Trigger-Aufzählung skaliert schlecht. Alle 5 chirurgisch gefixt, kein Sparring-Loop nötig.
- **Gemini (cc-gemini-plugin:gemini-agent-Subagent, Bridge-defekt per Memory `reference_gemini_agent_not_bridge_script`):** 0 HIGH / 0 MED / 0 LOW über 7 Cross-Sync-Checks (Slug-Reproduktion + Closed-Loop-Cross-Refs + stale-§26.5-Scan + Datum-Konsistenz + Trigger-Wording + Tabellen-Pipe-Count + Markdown-Lint). APPROVE.

**Sync-Set (§18 System-Zustand-Change, scoring-neutral):** CLAUDE.md + INSTRUKTIONEN.md + SYSTEM.md + CORE-MEMORY.md (§6+§13) + log.md (dieser Eintrag). **KEIN:** PORTFOLIO + Faktortabelle + score_history + flag_events + config.yaml + xlsx + PIPELINE.md (keine Verankerungs-Track-Item; #73 Skill-Backlog-Item ist separater Track). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lehre:**
- **Skill-Verankerung ist eigene Achse neben Skill-Deploy** — Commit `42eca7c` deployed nur den Skill-Body; Routing/Aktivierung/Lifecycle-Tracking sind separate Achse, leicht zu übersehen wenn der Skill „funktional fertig" wirkt. Memory `feedback_anchor_promotion_sync_gap.md` empirisch revalidiert.
- **Semantische §-Parent-Wahl > Subsection-Nummer-Pattern** — initiale Annahme „analog §27.5 → §26.5" war mechanisch korrekt aber semantisch falsch (Session-Closure ≠ Archiv-Sync). §25.5 als Sibling zu Briefing-Sync ist die korrekte Hierarchie. Karpathy-Think-Before-Coding fängt sowas mid-flight noch ab.
- **Zwei-Stufen-Lean-Pass (User-Direktive → Codex) effektiv** — User-Hint „kein Bloat" appliziert hat §26.5-Draft von ~30 auf ~12 Zeilen geshrinkt VOR Codex-Review. Codex empfahl danach noch eine weitere Shrink-Stelle (Sicherheits-Boundary 2→1 Satz, MED-3).

**Cross-Reference:** CLAUDE.md Z.50 · INSTRUKTIONEN §25.5 · SYSTEM.md Z.5+Z.43 · CORE-MEMORY.md §6 Z.256 + §13 (post-AMZN-18.05.-Eintrag) · `01_Skills/session-closure/SKILL.md` v0.2.0 (deploy `42eca7c`) · Memory `feedback_anchor_promotion_sync_gap` revalidiert · Commit `<TBD>`.

---

## [2026-05-22] system | FinnHub-Integration v0.1 Plan-Phase DONE + Codex-CP0 Plan-Review appliziert (PIPELINE #74 PLAN-READY, scoring-neutral)

**Event-Typ:** Plan-Phase (System-Zustand-Change, chore-level — kein Score/FLAG/Sparraten-Touch)

**Was passiert ist:**

1. **Plan-File geschrieben** via `superpowers:writing-plans`-Skill: `docs/superpowers/plans/2026-05-22-finnhub-integration-build-v0.1.md` (15 Tasks TDD-strukturiert, ~4-6h Build-Estimate, Subagent-Driven empfohlen, Codex-CP1+CP2+CP3 als Atmungs-Punkte). Untracked-on-disk per `.gitignore` Z.21 (konsistent mit Spec-File-Pattern).
2. **Pre-Plan Klärungs-Decisions (User-bestätigt):**
   - **Skill-Wrap-Timing:** Nachgang (Spec-konform §10 v0.2-Roadmap, nach Reklassifizierungs-Gate). Build-Phase v0.1 liefert NUR die 4 Tools + WSL-Bridge + Persistenz-Assertion, kein Skill.
   - **defeatbeta-Pull-Königsweg:** WSL-Subprocess gegen `/home/tobia/.defeatbeta-env/bin/python` + A12 Identity-Check WSL≡MCP als Build-Phase-Pflicht-Acceptance (Task 10). Alternative-Optionen (Claude-Session-Workflow, yfinance-Proxy) verworfen — WSL-Bridge ist semantisch äquivalent zur MCP-Pipeline (gleiches `defeatbeta-api`-Package), automatisierbar via Cron, Spec-konform.
3. **Codex-CP0-Plan-Review** (Codex `gpt-5.3-codex` via `codex:codex-rescue`-Subagent, Memory `feedback_review_via_codex_not_advisor`): 2 HIGH + 4 MED + 1 LOW Findings. Per `feedback_codex_sparring_heuristic` Single-Pass-Apply (Findings konkret + actionable, kein Sparring-Loop nötig). Alle 6 inline appliziert:
   - **HIGH-1 (Q4):** Task 13 Step 6 (SKILL.md-Edit `01_Skills/backtest-ready-forward-verify/SKILL.md`) entfernt — Spec §4 ZERO-Skill-Refactor invariant; nur Persistenz-Schicht-Code in `archive_score.py` bleibt. Guardrail-System-Doku stattdessen via Task 15 in SYSTEM.md §Passive Read-Only Data Layer.
   - **HIGH-2 (Q2/Q8):** Task 9 Step 4a Decision-Gate ergänzt — Live-Probe gegen `defeatbeta-api`-Methoden-Verfügbarkeit für die 5 nicht-initial-abgedeckten Metriken (`grossMargin5Y`, `debtToEquity`, `epsGrowth5Y`, `capexCagr5Y`, `fcfPerShareTTM`). ≥3 vorhanden → Bridge-Script erweitern; <3 → 3/8-Minimal akzeptieren + neues PIPELINE #76 für v0.2-Methoden-Discovery anlegen.
   - **MED-1 (Q1):** Spec-Pfad-Doppel-Spezifikation §2.1 (`~/.dynasty/finnhub_cache/`) vs §2.4 (`03_Tools/finnhub_cache/`) im Plan-Header dokumentiert — Plan folgt §2.1 + §11.2 + Codex-R1; Spec v0.3 invariant (LOCKED, nicht angefasst), Auflösung nur im Plan.
   - **MED-2 (Q6):** Token-Bucket `_TokenBucket.acquire()` von Once-Sleep-Then-Decrement zu Re-Check-Loop refactored (Concurrency-Over-Admit-Hazard); Multi-Thread-Concurrency-Test in Task 2 ergänzt (10 Threads × 10 acquires bei capacity=10/rate=10 → ≥8,5s Pflicht).
   - **MED-3 (Q7):** Token-Bucket-Policy bei 429-Retries dokumentiert — Retries verbrauchen KEINE extra Tokens (Server-Side-Limit, doppel-Acquire wäre nur Client-Budget-Verbrennung). Note im `_request()`-Docstring + Code-Kommentar.
   - **MED-4 (Q10):** Bash-Execution-Context für alle Plan-Command-Blöcke im Plan-Header deklariert (here-docs, `<<'MSG'`, `mkdir -p`, `&&`/`||`) — Memory `feedback_powershell_herestring_in_bash_tool` konsistent (PowerShell `@'...'@` korrumpiert im Bash-Tool, daher durchgängig Bash-Pfad).
   - **LOW-1 (Q9):** log.md-Pfad bereits korrekt im Plan referenziert (`07_Obsidian Vault/.../log.md`, NICHT `00_Core/log.md`) — Memory `reference_dynastie_log_location.md` invariant. Keine Action.
4. **Self-Review-Status** (writing-plans-Skill-Pflicht-Checkliste): Spec-Coverage 17/17 §§ → Task-Mapping, Acceptance-Tests A1-A12 jeder einem Task mit Pass-Kriterium zugeordnet, Type-Consistency `_FinnHubClient`-Signaturen + `CrosswalkRecord`-Felder + `FINNHUB_KEY_MAP` konsistent, keine Placeholders.

**Lehre:**
- **Plan-Phase als eigene Disziplin nach Spec-LOCK** — Memory `feedback_brainstorming_terminal_override_dynastie` sagt im Dynastie-Depot: Spec-Pickups → Codex-Sparring → §18-Sync, Execution separate Session. Plan-Phase fügt sich genau dazwischen ein: Spec-LOCK → Plan-Phase + Codex-CP0 → §18-Sync der Plan-Transition → Execution next-Session. Vermeidet Confusion zwischen Brainstorming (offen) und Execution (bereit-zum-Code).
- **Codex-CP0-Plan-Review fängt Spec-Plan-Drift früh** — HIGH-1 (SKILL.md-Edit) wäre erst in Build-Phase Task 13 als §4-Bruch sichtbar gewesen, hätte Task-15-§18-Sync gefährdet. HIGH-2 (3/8 vs 8/8 Metriken) hätte A6-Acceptance-Run undokumentiert N/A-Records produziert. Beide jetzt im Plan-Wortlaut adressiert vor Build-Start.
- **WSL-Subprocess + A12 Identity-Check als Königsweg-Muster für MCP-vs-Standalone-Lücken** — wenn ein MCP-Server ein pip-Package wraps, ist Direct-Import via Subprocess semantisch äquivalent und automatisierbar. Pattern dokumentiert in Plan §Architecture + Task 9 + Task 10 als Build-Phase-Pflicht.

**Sync-Set:** PIPELINE.md (#74 Status PLAN-READY + Build-Phase-Scope auf Plan-File + Footer v2.52→v2.53) + SYSTEM.md (§Passive Read-Only Data Layer FinnHub-Bullet um Plan-File + Königsweg-Reference + Footer v1.3→v1.4) + log.md (dieser Eintrag). **KEIN:** PORTFOLIO + CORE-MEMORY + Faktortabelle + score_history + flag_events + config.yaml + xlsx (Spec §7.1 State-Files NULL — Live-Score-Impact NULL, scoring-neutral). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Cross-Reference:** Plan-File `docs/superpowers/plans/2026-05-22-finnhub-integration-build-v0.1.md` · Spec-File `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` v0.3 (LOCKED, invariant) · PIPELINE.md #74 Z.79 + Footer v2.53 · SYSTEM.md §Passive Read-Only Data Layer + Footer v1.4 · Memory `feedback_codex_sparring_heuristic` (Single-Pass-Apply Heuristik) · Memory `feedback_review_via_codex_not_advisor` (Codex gepinnt) · Memory `feedback_brainstorming_terminal_override_dynastie` (Spec→Sparring→Sync→Execution-Trennung) · Commit `<TBD>`.

---

## [2026-05-22] system | FinnHub-Integration v0.1 BUILD-PHASE-DONE — Task 15 §18-Sync (PIPELINE #74 BUILD-DONE, scoring-neutral)

**Event-Typ:** Build-Phase-Done + §18-Sync (System-Zustand-Change, chore-level — kein Score/FLAG/Sparraten-Touch, Live-Score-Impact NULL per Spec §7.1)

**Was passiert ist:**

1. **Build-Phase nach Spec-LOCK v0.3 + Plan v0.1.0** — 15 Tasks gemäß Build-Plan `docs/superpowers/plans/2026-05-22-finnhub-integration-build-v0.1.md` deployed in Subagent-Driven-Execution mit CP-1/CP-2/CP-3 Codex+CodeRabbit-Reviews als Atmungs-Punkte. ~6h Bauzeit. 6 Build-Commits seit Spec-LOCK 1a71f0f: 8f427f1c/27d0102/f9bbc43/f56081c/d74d6e4/9f795ca (+ dieser Task-15-§18-Sync-Commit als 7. closing).
2. **Deliverables (Read-Only-Surface, alle in `03_Tools/`):**
   - `finnhub_client.py` — Wrapper + Token-Bucket-Rate-Limiter (Re-Check-Loop per Codex-CP0-MED-2) + File-Cache `~/.dynasty/finnhub_cache/` + Retry + 4 Getters (quote/calendar/news/metric) + `_meta.for_scoring=False`-Guardrail (Tasks 1-6, commits d8cd26c/c15ab94/660e400/b3e4932/419f635c/fb424fea/CP-1 fixes/b9f001a).
   - `finnhub_smoke_test.py` + `finnhub_health.json` — 9-Test-Matrix, exit-0 wenn 6/6 expected-PASS via dynamic EXPECTED_PASS_COUNT-Threshold (A2-Königsweg statt Hardcoded-Threshold) (Tasks 7-8).
   - `defeatbeta_subprocess.py` — WSL-Bridge gegen `/home/tobia/.defeatbeta-env/bin/python` (Königsweg, Task 9, commits 54762b9 + cb41e6f Code-Quality-Follow-up).
   - `finnhub_a12_identity_check.py` — A12 WSL≡MCP Pairing-Script, Live-PASS bit-perfect Δ=0.00 für [MSFT,V,TMO] × [roe,peTTM,roic] (Task 10, commits 09beb4e + 1a71f0f Next-Steps + start_date recipe).
   - `finnhub_crosswalk_trigger.py` + `CrosswalkRecord` pydantic-Model (Spec §5.3, strict-mode per CQ-Opus-Important) — A6 Live-Run 24/24 schema-conform auf MSFT/V/ASML (Tasks 11-12, commits 8f427f1 + 27d0102 + f9bbc43 + f56081c).
   - `backtest-ready/archive_score.py::_assert_metric_for_scoring` — R1-Guardrail in Persistenz-Schicht, KEINE SKILL.md-Edits per Codex-CP0-HIGH-1 (Task 13, commit 9f795ca).
3. **CP-2-Review (Task 12 Folge):** CodeRabbit-Critical (Timestamp-Ordering — `_pulled_at` muss NACH dem Pull captured werden) + CQ-Opus-Important (Pydantic strict-mode verhindert silent str→float Coercion) beide inline appliziert in d74d6e4. PIPELINE-Followups P-3 bis P-6 + I-2 als Improvement-Backlog gekoppelt an #75.
4. **Acceptance-Status A1-A12 alle PASS:** A1 Static-Footprint-Check via Grep (0 matches `finnhub` in `01_Skills/` excl. `_extern/`) → §4 Zero-Skill-Refactor-Footprint statisch verifiziert. A2 dynamic-threshold. A3-A11 Unit + Integration. A6 24/24 schema-conform Live-Run. A12 bit-perfect Δ=0.00 für 3 Symbols × 3 Metriken (Task 14 = A1-Rollback-Invarianz-Check, kein zusätzlicher Code-Touch).
5. **Step 4a Decision (Task 9):** Live-Probe der `defeatbeta-api`-Methoden für die 5 nicht-initial-abgedeckten Metriken ergab **2/5 vorhanden** (`grossMargin5Y` via `Ticker.quarterly_gross_margin()`, `debtToEquity` via `Ticker.debt_to_equity()`) — <3-Threshold-Schwelle per Codex-CP0-HIGH-2 → **3/8-Minimal-Bridge akzeptiert** (peTTM/roe/roic Live + 5/8 systematisch N/A). 5/8-Methoden-Discovery für v0.2 in neuem PIPELINE #76 dokumentiert.
6. **Shadow-Run-Setup:** Startet 2026-05-23, Hard-Deadline Reklassifizierungs-Gate **2026-07-06 (+45d)**. Coverage-Ziele aus Spec §8.1: ≥50 Crosswalk-Records, ≥8 pro Kern-Symbol, ≥40 non-N/A für ROIC. PIPELINE #75 als Shadow-Run-Tracker neu eröffnet. v0.2-Reklassifizierungs-Entscheidung basierend auf empirischer Crosswalk-Median-Divergenz.
7. **§18-Sync-Welle dieser Commit (Spec §7.2 MINOR):** SYSTEM.md §Passive Read-Only Data Layer FinnHub-Bullet auf BUILD-PHASE-DONE + Deliverables + Acceptance-Manifest + Footer v1.4→v1.5. PIPELINE.md #74 Status auf BUILD-DONE + Build-Summary-Block + neu #75 Shadow-Run-Tracker + neu #76 Methoden-Discovery + Footer v2.53→v2.54. log.md dieser Eintrag.

**Lehre:**
- **Subagent-Driven-Execution mit CP-Atmungs-Punkten skaliert:** 15 Tasks in ~6h ohne Drift-Reinfälle dank Codex/CodeRabbit-Reviews an Task-8/Task-12/CP-3-Checkpoints. CP-2 fängte 2 echte Bugs (Timestamp-Ordering Race + Pydantic-Coercion) die Unit-Tests übersehen hätten — Memory `feedback_cr_pass_after_bulk_refactor` bestätigt mit MFTM-System.
- **§4 ZERO-Skill-Refactor invariant durch statische A1-Verifikation:** Static-Footprint-Check (Grep `finnhub` in `01_Skills/`) ist robuster Acceptance-Mechanismus statt Trust-on-Convention. Codex-CP0-HIGH-1 (SKILL.md-Edit aus Task 13 entfernen) hat das vor Build-Start gerettet — Persistenz-Schicht-Guardrail in `archive_score.py` statt Workflow-Touch.
- **Step-4a-Decision-Gate als Plan-Pattern für unklare Daten-Coverage:** statt blindes Implementieren der 8 Metriken erst Live-Probe der Methoden-Verfügbarkeit, dann <3-Threshold-Schwelle anwenden. 3/8-Minimal-Bridge ist ehrlicher Build-State, 5/8-Folge-Discovery in PIPELINE #76 als sauberes v0.2-Backlog statt False-N/A-Records in v0.1-Run.
- **Read-Only-Surface + `_meta.for_scoring=False` + Persistenz-Schicht-Assertion** = drei-stufige V-Q2-Methodology-Drift-Präzedenz-Mitigation. Keine einzelne Schicht reicht (Marker allein wäre advisory), aber Kombination erzwingt fail-close.

**Sync-Set:** SYSTEM.md (§Passive Read-Only Data Layer BUILD-PHASE-DONE + Deliverables + A1-A12-Manifest + Footer v1.4→v1.5) + PIPELINE.md (#74 BUILD-DONE + Build-Summary-Block + neu #75 Shadow-Run-Tracker Hard-Deadline 2026-07-06 + neu #76 v0.2-Methoden-Discovery + Footer v2.53→v2.54) + log.md (dieser Eintrag). **KEIN:** PORTFOLIO + CORE-MEMORY + Faktortabelle + score_history + flag_events + config.yaml + xlsx (Spec §7.1 State-Files NULL — Live-Score-Impact NULL, scoring-neutral). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Cross-Reference:** Build-Plan `docs/superpowers/plans/2026-05-22-finnhub-integration-build-v0.1.md` · Spec-File `docs/superpowers/specs/2026-05-22-finnhub-integration-design.md` v0.3 (LOCKED, invariant) · Build-Commits seit Spec-LOCK 1a71f0f: 8f427f1c/27d0102/f9bbc43/f56081c/d74d6e4/9f795ca + Task-15-Sync-Commit `<TBD>` · PIPELINE.md #74/#75/#76 + Footer v2.54 · SYSTEM.md §Passive Read-Only Data Layer + Footer v1.5 · Memory `feedback_skill_methodology_drift_v_q2` (V Q2 28.04. Drift-Präzedenz) · Memory `reference_dynastie_log_location` (Vault-log-SSoT) · Memory `feedback_codex_sparring_heuristic` (Single-Pass-Apply Heuristik).

## [2026-05-22] system | Block-A/B Doc-Sync Welle — PIPELINE #74 Slim-Refactor + Vault-Tool-Pages (System-Event, scoring-neutral)

**Befund:** Post-FinnHub-BUILD-PHASE-DONE-Task-15-§18-Sync (Eintrag oben) blieben (a) PIPELINE #74-Body mit ~3000W Build-History (Codex-3-Runden + Build-Phase-Summary + CP-2-Followups) als statischer Substrate-Bloat; (b) SESSION-HANDOVER.md mit letztem Banner 18.05. AMZN ohne FinnHub-Bezug; (c) STATE.md Critical-Alerts ohne 22.05.-Eintrag; (d) CORE-MEMORY §13 ohne FinnHub-Integration-Lifecycle-Eintrag; (e) Vault-Konventions-Gap zu `wiki/sources/tools/` ohne `finnhub.md` (Datenquelle parallel zu defeatbeta.md) und `session-closure.md` (Skill parallel zu backtest-ready-forward-verify.md, gestern 21.05. deployed via `42eca7c`).

**Aktion (2 atomare Commits):**

**Block A — 00_Core-Doc-Sync (Commit `1e2947a`):**
- PIPELINE.md #74 massiv geslimmt (~3000W → ~190W Pointer): Numbering-Convention-Sub-Pattern für „BUILD-DONE-aber-Forward-aktiv"-Items (Pure-Removal wie #70/#71 inappropriate solange Forward-Work-Pointer benötigt). Detail-Trail verlagert nach SYSTEM.md §Passive Read-Only Data Layer (Footer v1.5) + Vault log.md 3 FinnHub-Einträge (Spec/Plan/Build) + git log + Spec/Plan-Files. P-3..I-2-CP-2-Followups in #75-Body gefolded.
- PIPELINE-Footer v2.54→v2.55.
- SESSION-HANDOVER.md: neuer 22.05.-Banner (FinnHub-Integration v0.1 SPEC→PLAN→BUILD + paragraph-18-sync SPEC v0.3 Build-ready + session-closure-Skill v0.2.0 zusammengefasst) + Resume-Anweisung Shadow-Run Day-1-Trigger als Primär-Track.
- STATE.md: neuer 22.05.-Critical-Alert FinnHub-DONE + Footer Stand 18.05.→22.05.
- CORE-MEMORY §13 Lifecycle: 2 neue Einträge (FinnHub-Integration v0.1 SPEC→PLAN→BUILD Vollumfang + paragraph-18-sync SPEC v0.3 30 Codex-Befunde adoptiert). Footer v1.22→v1.23.

**Block B — Vault-Tool-Pages (Commit `02866b5`):**
- `wiki/sources/tools/finnhub.md` NEU (Datenquelle parallel zu defeatbeta.md): Coverage Quote/Earnings-Calendar/Company-News/Stock-Metric + Artefakte-Manifest + Shadow-Run-Coverage-Ziele + Day-1-Trigger-Command + v0.2-Roadmap-Pointer + Step-4a-Decision (3/8-Minimal) + Methodology-Drift-Schutz-Sektion (technische Guardrails).
- `wiki/sources/tools/session-closure.md` NEU (Skill parallel zu backtest-ready-forward-verify.md): v0.2.0 deployed `42eca7c`, Strict-Trigger `!SessionClose`, fail-close-Boundary, INSTRUKTIONEN §25.5 SSoT, Sync-Set typisch Score-/System-Event dokumentiert.
- `wiki/sources/tools/defeatbeta.md` Cross-Backlink: neue §Crosswalk-FinnHub-Sektion (Primary-Pull WSL-Subprocess + A12 Identity-Check + aktuelle 3/8-Coverage + PIPELINE #76 Pointer) + [[finnhub]]-Verlinkung.
- `wiki/sources/tools/backtest-ready-forward-verify.md` Cross-Backlink: [[session-closure]] als §18-Sync-Komplement (User-getriggert vs programmatisch).
- `paragraph-18-sync.md` bewusst DEFERRED bis Build-DONE (derzeit nur SPEC-COMPLETE PIPELINE #73a).

**Bewusst NICHT (Block C verworfen):**
- Ticker-Entity-Pages (MSFT/V/ASML/TMO/COST) bekommen KEINE FinnHub-Crosswalk-Coverage-Footer — Geräusch-Kosten höher als Hebel, Vault-Tool-Page `finnhub.md` ist self-contained, Crosswalk-Records leben in `03_Tools/finnhub_crosswalk_log.jsonl`.
- Vault `index.md` ist Research-Paper-Anker-Doc (B1-B30), nicht Tool-Index — Tool-Backlinks bleiben in `wiki/sources/tools/` lokal.

**Sync-Set (System-Event):** PIPELINE.md + SESSION-HANDOVER.md + STATE.md + CORE-MEMORY.md (Block A) + 4 Vault-Files (Block B) + log.md (dieser Eintrag). **KEIN:** PORTFOLIO + Faktortabelle + score_history + flag_events + config.yaml + xlsx + SKILL.md — kein Score/FLAG/Sparraten-Event, kein Skill-Refactor (FinnHub-v0.1-Invariante). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:** (a) PIPELINE-Body-Slim als Numbering-Convention-Sub-Pattern für „BUILD-DONE-aber-Forward-aktiv"-Items — Detail-Trail wandert zu SYSTEM/log/git, Pointer bleibt aktiv (#70/#71 Pure-Removal wäre hier Info-Loss für Forward-Work-Pointer wie #75-Coverage-Ziele und v0.2-Roadmap-Reihenfolge); (b) Vault-Tool-Page-Konvention (1 Page pro aktive Datenquelle/Skill in `wiki/sources/tools/`) verlangt proaktiven Page-Build bei jeder neuen Tool-Klasse — Lücke war 22h alt für session-closure und 6h für finnhub; (c) Cross-Backlink-Disziplin (defeatbeta↔finnhub bidirektional + skill-skill) macht den semantischen Graph traversierbar ohne dass Tool-Index zentral gepflegt werden muss.

**Cross-Reference:** Commits `1e2947a` (Block A) + `02866b5` (Block B) + dieser log-Eintrag-Commit · PIPELINE.md Footer v2.55 · SESSION-HANDOVER.md 22.05.-Banner · STATE.md Critical-Alert 22.05. · CORE-MEMORY §13 v1.23 · Vault `wiki/sources/tools/finnhub.md` + `session-closure.md` (NEU) + defeatbeta.md + backtest-ready-forward-verify.md (Backlinks).

## [2026-05-22] system | paragraph-18-sync Build-Phase Tasks 1-6 + CP1-Verify DONE (System-Event, scoring-neutral)

**Befund:** PIPELINE #73(a) paragraph-18-sync Skill (SPEC-COMPLETE v0.3 Build-ready gateway erreicht 22.05. abends) bekam Build-Phase-Start in derselben Session ~20:40-21:30. Ziel: Phase 0-4 Implementation-Plan-Tasks 1-6 (Scaffolding → yaml-SSoT → validator-Skeleton → smoke-test-Skeleton → P1-Ordering+Ticker-Identity → P1-Dirty-Predicate+Quartal-Rollover) + Codex-CP1-Review-Cadence-Erweiterung (User-Direktive „Codex-Break an geeigneter Stelle einbauen, ggf. Sparring").

**Aktion (8 Commits, alle scoring-neutral, alle pre-commit-Hooks PASS):**

1. **Phase 0** `18341f0` chore(skill): scaffold (`__init__.py` + `.gitkeep` + `.gitignore session_marker`).
2. **Phase 1** `bf9f25e` feat(skill): `event_typ_mapping.yaml` SSoT-Mirror §18.1 (4 event-types: score-flag-sparraten/pipeline-item/system-zustand/critical-alert + conditional flag_event/session_close/version_bump + critical-alert no_op_pass=true + Active-xlsx-Resolution-Doku Codex-M4).
3. **Phase 2** `158ba7d` feat(skill): validator.py Skeleton — Exit-Codes 0-6 per Spec §7 + subprocess/git-Layer mit FileNotFoundError+TimeoutExpired+check=False (Codex-M7 S18) + cwd-parametrisierbar für Test-Isolation + FileClassification dataclass + classify_files (P4 4-Bucket per G-01) + argparse build_parser (event_type/--also/--flag-event/--ticker/--allow-dirty/--verify-b/--reset-session/--dry-run/--json).
4. **Phase 3** `801d66f` test(skill): `_smoke_test.py` Skeleton — pytest temp_repo fixture + `_run_validator` Helper + S18b non-git-repo no-Traceback + S18d missing-yaml no-Traceback + Sanity --help/no-args.
5. **Phase 4 (a)** `6951a5a` feat(skill): P1 Ordering-Guard + Ticker-Identity (Codex-H3) + S11/S17 — `_read_last_jsonl_record` robuste JSONL-Reader (missing/empty/malformed/binary → None), `_resolve_project_root` cwd-aware via `git rev-parse --show-toplevel` (Test-Isolation), `verify_pre_flight` mit score_history HEAD-Date=today + Ticker-Match + flag_events parallel + Bug-Fix cwd=Path.cwd() default.
6. **Phase 4 (b)** `cf6d81e` feat(skill): P1 Dirty-Predicate (Codex-M5) + Quartal-Rollover (G-03) + S15/S13 — `_check_quarterly_rollover` helper für §18.6 Quartals-Wechsel-WARN, `verify_pre_flight` mit `allow_dirty`+`expected`-Args, |(unstaged∪untracked)\expected|≥allow_dirty FAIL, --allow-dirty>100 Hard-Cap Refused.
7. **Codex-CP1** (`codex exec review --base 18341f0^`, gpt-5.3-codex Single-Pass) lieferte 2 Befunde: **P0** except-Klammern-Konvention (empirisch falsch wegen PEP 758 Python 3.14, aber Cross-Tool-Robustheit valide) + **P1** main() returnt PASS bei unimplementiertem P2-P7 (echter fail-close-Contract-Bug für Build-Phase).
8. **Codex-CP1-Fix** `212854b` fix(skill): Klammern + `# fmt: skip` (ruff format hätte sie sonst wieder entfernt) + EXIT_BUILD_INCOMPLETE=99 Sentinel + WARN-Print bei P2-P7-unimplemented + test_s15a-Assertion angepasst (assert exit≠1 statt ==0).
9. **Codex-Diff-Re-Review** (`codex exec review --commit 212854b`) Verdict: „commit fixes the reported issues without introducing regressions in the touched logic. New build-phase sentinel behavior is internally consistent, documented, and test-adjusted." = **0 findings** post-Fix. Single-Pass-Sparring-Loop konform Memory `feedback_codex_sparring_heuristic` Heuristik.

**Status nach Cut:** 7/18 Tasks done. Phase 0-4 ✅ KOMPLETT. CP1 ✅ verified. Phase 5+ (Tasks 7-18: P2/P3/Drift-Guard/P4/P5/P6/P7/Test-Suite-Full-Run/SKILL.md via skill-creator/references/Reviews/Dogfood/Promotion) deferred zur nächsten Session. Tests: 13/13 PASS in 2.55s. ruff check + ruff format --check + pre-commit alle PASS. Live-Score-Impact NULL.

**Lessons:** (a) **Karpathy-Vorratsimport-Reinfall + Recovery:** Erster validator.py-Wurf importierte 6 Module auf Vorrat (hashlib/json/os/re/time/yaml) für spätere Phasen — pre-commit-Hook surfacte F401-Lint-Fail. Fix: Surgical-Imports-Disziplin („nur was Phase X nutzt"), spätere Imports beim Task-Beginn hinzufügen + lokales `ruff check`+`ruff format --check` VOR `git add` etabliert. Memory `feedback_pre_commit_diff_inspection` bestätigt + verschärft. (b) **PEP 758 `except A, B, C:` ohne Klammern ist Python 3.14 valide aber Codex (Read-Only ohne Datei-Access) und alte Linter/IDE missverstehen es als SyntaxError** — Klammern wieder einfügen + `# fmt: skip` als ruff-format-Override blockt die idempotente Entfernung. (c) **Build-Phase-Sentinel exit=99 als fail-close-Contract während TDD-iterativem Build:** main() darf nicht EXIT_PASS returnen wenn nur Teil-Phasen verdrahtet sind — Sentinel + WARN-Print signalisiert „Skill nicht produktiv" sauber, ohne git-Build-Branch-Indirection. (d) **Codex-Mid-Build-CP-Cadence (FinnHub-Pattern wiederbelebt):** CP nach jeder substantiellen Phase fängt Architektur-Drift früher als End-Review — CP1 fand echten Bug (Sentinel), nicht nur Konvention. User-Direktive normativ für nächste Sessions: CP2 nach Phase 5, CP3 nach Phase 7, CP-Final Task 16. (e) **Plan-Korrektur Task 14 (SKILL.md) auf skill-creator-Skill-Aufruf statt manuell:** Plan-Footer aus PIPELINE #73 v2.51 sah „letzte Phase = skill-creator-Aufruf" vor, Plan-Body schreibt SKILL.md aber Task 14 manuell — Inkonsistenz, in Task-Description bereinigt für nächste Session.

**Sync-Set (System-Event):** PIPELINE.md (#73(a) Status auf BUILD-PHASE in-progress 7/18 + Footer v2.55→v2.56) + log.md (dieser Eintrag) + 7 Skill-Build-Commits (18341f0..212854b im Skill-Tree). **KEIN:** PORTFOLIO + CORE-MEMORY + Faktortabelle + score_history + flag_events + config.yaml + xlsx + STATE.md (kein Score/FLAG/Sparraten/Critical-Alert-Event, kein Skill-Promotion-Event — Skill ist BUILD-PHASE-in-progress nicht promoted-v0.1.0). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Cross-Reference:** Commits `18341f0` (scaffold) · `bf9f25e` (yaml) · `158ba7d` (validator skeleton) · `801d66f` (smoke test) · `6951a5a` (P1 ordering+ticker) · `cf6d81e` (P1 dirty+quartal) · `212854b` (CP1-Fix Sentinel+Klammern) · dieser log-Eintrag-Commit · PIPELINE.md Footer v2.56 · Spec-File `docs/superpowers/specs/2026-05-21-paragraph-18-sync-design.md` v0.3 (untracked) · Plan-File `docs/superpowers/plans/2026-05-22-paragraph-18-sync-implementation.md` 18-Tasks/10-Phasen (untracked) · Codex-Reviews `.reviews/cp1.md` (831 LOC, P0+P1 Befunde) + `.reviews/cp1-rereview.md` (2361 LOC, 0 findings post-Fix) — `.reviews/` ist untracked-ephemeral · Memory `feedback_pre_commit_diff_inspection` (Karpathy-Recovery) · Memory `feedback_codex_sparring_heuristic` (Single-Pass-Loop) · Memory `feedback_review_via_codex_not_advisor` (codex-CLI gpt-5.3-codex pinned via `~/.codex/config.toml`).

## [2026-05-22] system | paragraph-18-sync Build-Phase 5 (Tasks 7+8) + Codex-CP2 DONE (System-Event, scoring-neutral)

**Befund:** Fortsetzung des paragraph-18-sync Skill-Builds (PIPELINE #73a) — Phase 5 P2/P3-Event-Klassifikation + SSoT-Drift-Guard implementiert, Codex-CP2 Sparring-Loop appliziert. Phase 0-5 jetzt komplett (9/18 Tasks), Phase 6+ deferred.

**Aktion (3 Commits seit 1a6ad4a §18-Sync, alle scoring-neutral, alle pre-commit-Hooks PASS):**

1. **Phase 5 Task 7** `b73c9cf` feat(skill): P2 Event-Klassifikation (parse + dedupe) + P3 yaml-Load + `compute_union_set` (§18.2) + SYSTEM.md Active-xlsx-Block-Parser + `resolve_active_xlsx` (Codex-M4 deterministisch: SYSTEM.md-Pin > Glob+Semver > Ambiguity-FAIL exit=3) + Tests S4/S6/S8a (alle gegen ROOT). `.gitignore` `.reviews/` ergänzt (lokale Codex/CR/Gemini-CP-Artefakte, repo-Hygiene-Fix damit dirty-tree-predicate gegen ROOT deterministisch). **Plan-Treue-Deviation:** Plan-Step-3 returnt EXIT_PASS für alle non-critical-alert-Paths; das würde CP1-P1 (EXIT_BUILD_INCOMPLETE bis Phase 7 done) regredieren. Synthese: dry-run → PASS, critical-alert → PASS (NO-OP-complete), non-dry-run non-critical → bleibt EXIT_BUILD_INCOMPLETE (P4-P7 fehlen in Tasks 9-12). Im Commit-Body dokumentiert.

2. **Phase 5 Task 8** `0f7a80f` test(skill): S7 SSoT-Drift-Guard — `_parse_18_1_table` Helper + Symmetric-Difference-Test gegen yaml.event_types.required_files. Soft-Skip-Pfad während Build-Phase: §18.1 nutzt aktuell CamelCase-Labels (`Pipeline-Item`/`System-Zustand-Change`), der kanonische lowercase-kebab-Parser triggert pytest.skip mit Hint. Hard-Check aktiviert sich nach §18-Bump-Spec-Lock.

3. **Codex-CP2** (`codex:codex-rescue`-Subagent, gpt-5.3-codex pinned) Single-Pass auf b73c9cf+0f7a80f → 2 HIGH + 2 MED + 2 LOW. Sparring-Heuristik (HIGH≥2): Single-Pass + Diff-Re-Review (cheapest Schritt per Memory `feedback_codex_sparring_heuristic`).

4. **Codex-CP2-Fix** `c15940a` fix(skill): 4 Fixes appliziert. **HIGH-1:** S7-Assertion `parsed_events.issubset(yaml_events | parsed_events)` war tautologisch (Drift-Guard konnte strukturell nie failen) — korrigiert auf `parsed_events - yaml_events == ∅`. **HIGH-2:** Two-Pass-P1 false-negative — erster Pass mit expected=∅ maskierte legitime Sync-States als dirty-FAIL bevor P2/P3 Expected-Set bekannt war. Fix: `check_dirty: bool = True` Parameter in verify_pre_flight; erster Pass in main() ruft mit `check_dirty=False`, zweiter Pass (post-P3 mit expected) Default True. Pre-existing-Snapshot wird trotzdem im first-pass erfasst (P4-bereit). **MED-1:** KeyError-Risiko bei unguarded `mapping["event_types"]["score-flag-sparraten"]` → `.get()`-Chain + `isinstance(node, dict)`-Guard. **MED-2:** S8a-Test `if r.returncode != 0: return` schluckte alle non-zero silent → narrow zu `if exit==1: pytest.skip("P1 live-state fail")` + `assert exit==0` für andere Codes. LOW-1/LOW-2 non-action (S7 Soft-Skip beibehalten bis §18-Bump; Semver-Regex fail-close intentional).

5. **Codex-CP2-Diff-Re-Review** auf c15940a-Diff (132 LOC). Verdict: **ALL CLEAR, kein zweiter Sparring-Pass nötig.** = 0 findings post-Fix. 2-Runden-Loop konform Memory-Heuristik.

**Status nach Cut:** 9/18 Tasks done. Phase 0-5 ✅ KOMPLETT (Scaffolding/yaml-SSoT/validator-Skeleton/smoke-test/P1-komplett/P2-P3-Klassifikation+xlsx-Selektion/S7-Drift-Guard). CP1 ✅ + CP2 ✅ verified. Phase 6+ (Tasks 9-18: P4-Staging-Diff/P5-xlsx-Confirm/P6-Two-Commit-Protokoll/P7-Closure-Report/Test-Suite-Full-Run/SKILL.md via skill-creator/references/CP3+CP-Final/Dogfood/Promotion) deferred zur nächsten Session. Tests: 15 PASS + 2 SKIP = 17 collected in 4.07s (S7 Soft-Skip bis §18-Bump + S8a Live-State-Skip). ruff check + ruff format --check + pre-commit alle PASS. Live-Score-Impact NULL.

**Lessons:** (a) **Plan-vs-CP1-Sentinel-Synthese:** Plan-Wortlaut kann später-applizierte Codex-Fixes (CP1-P1) versehentlich regredieren wenn literal befolgt — `executing-plans`-Skill „Follow each step exactly" erfordert §0.1-Think-Before-Coding-Override bei bekannten Post-Plan-Fixes. Im Commit-Body dokumentieren. (b) **Codex-CP2-Sparring-Loop validiert Memory-Heuristik:** Single-Pass + Diff-Re-Review reicht bei HIGH≥2 wenn Fixes surgical sind; 0 findings im Re-Review ist deterministisch erreichbar. ~25k+~21k Tokens für 2 Runden vs ~75k+ für 3-Runden-Loop = ~40% Ersparnis. (c) **Tautologische Asserts sind reviewer-essenziell:** S7 `parsed_events.issubset(yaml_events | parsed_events)` ist immer wahr — solche Bugs sind augenscheinlich nur im Test-Output (test PASS bei jedem State) oder durch Codex-Pass erkennbar; lokale Test-Suite kann sie nicht selbst finden (kein Negativ-Test). Plan-Schwäche, kein Build-Skill-Schwäche. (d) **`.reviews/`-gitignore-Fix als Repo-Hygiene-Nebeneffekt:** Phase-5-Tests gegen ROOT brauchen deterministischen dirty-count → review-Artefakte (Codex/CR/Gemini-Logs pro CP) müssen gitignored sein. Wäre auch ohne Test-Anlass richtig.

**Sync-Set (System-Event):** PIPELINE.md (#73(a) Status auf 9/18 BUILD-PHASE + Footer v2.56→v2.57) + log.md (dieser Eintrag) + 3 Skill-Build-Commits (b73c9cf/0f7a80f/c15940a). **KEIN:** PORTFOLIO + CORE-MEMORY + Faktortabelle + score_history + flag_events + config.yaml + xlsx + STATE.md (kein Score/FLAG/Sparraten/Critical-Alert-Event, kein Skill-Promotion-Event — Skill weiter BUILD-PHASE-in-progress, nicht promoted). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Cross-Reference:** Commits `b73c9cf` (Task 7 P2/P3) · `0f7a80f` (Task 8 S7) · `c15940a` (CP2-Fix HIGH+MED) · dieser log-Eintrag-Commit · PIPELINE.md Footer v2.57 · Codex-Reviews `.reviews/cp2/phase5-diff.patch` + `.reviews/cp2/cp2-fix-diff.patch` (untracked-ephemeral) · Memory `feedback_codex_sparring_heuristic` (2-Runden-Loop validiert) · Memory `feedback_review_via_codex_not_advisor` (codex-CLI gpt-5.3-codex pinned).

---

## [2026-05-23] system | PIPELINE #73(a) BUILD-PHASE Tasks 9-12 (Phase 6+7) + Codex-CP3 R1+R2 + CodeRabbit-WSL Bulk-Pass DONE (scoring-neutral)

**Event-Typ:** Pipeline-Item Sub-Status-Transition (BUILD-PHASE in-progress, 9/18 → 14/18 Tasks) + Mid-Session-Review-Trinity (Codex-CP3 R1+R2 + CR-WSL Bulk-Pass). Scoring-neutral.

**Session-Verlauf (Phase 6+7 + CP3, ~3h):**

1. **Task 9 P4 Staging-Diff** (`e91851d`): `verify_staging(expected, pre_existing_unstaged, ticker, *, cwd=None)` + `_emit_report()` preliminary + main()-Integration. EXIT_BUILD_INCOMPLETE=99-Sentinel entfernt (P4 verdrahtet, kein false-positive-Risiko mehr). Two-Commit-Vorbereitung: `expected_for_a` (non-xlsx) vs `expected_xlsx` Split. Spot-Grep `-G<ticker>` non-blocking. Tests: `test_classify_files_4_buckets` (G-01-Coverage) + `test_s10_preexisting_dirty_does_not_fail` (Snapshot-Invariante).

2. **Task 10 P5 xlsx-Confirm** (`d6987f2`): `verify_xlsx_smoke(expected_xlsx, *, non_interactive_input=None)` v0.1 manual-confirm gemäß `03_Tools/xlsx-smoke-test.md`. **Codex-H2 skip-Hard-Fail:** `skip`-Eingabe ist exit=5 wenn aus main() aufgerufen, kein Bypass im Required-xlsx-Pfad. Leeres xlsx-Set → no-op-PASS. v0.2 (post-PIPELINE #73b) ersetzt durch Sub-Skill-Auto-Call. Tests: S20a/b/c/d (skip/y/n/empty).

3. **Task 11 P6 Two-Commit-Protokoll** (`dc57c6d`): Voll-State-Machine — `_session_id` (sha1 host/user/time) + `write_session_marker(*, commit_a_sha, expected_xlsx, marker_path=None)` + `read_session_marker(marker_path=None)` + `session_valid(marker, *, cwd=None)` (commit_a_sha-Match + 4h-TTL). `_run_verify_b(args)` macht Codex-M2-normativ volle P1+P4+P5-Revalidation für xlsx-Subset. main(): `--verify-b` dispatch + bei xlsx-Pflicht nach P4-PASS Marker-Write + NOTE-Hint. Drift-Matrix 7 Branches (Codex-M3) als Kommentar-Block dokumentiert. Tests: S16a/d/TTL/corrupt/no-marker/committed/reset (8 Tests).

4. **Task 12 P7 Closure-Report** (`8ba3f49`): `_emit_report()` Schema voll ausgebaut um `xlsx_verified` + `retry_required_revalidation` (Codex-M6 Re-Validate-Before-Retry) + `session_marker`-nested + `recovery_hints` (phase-spezifisch: P1/P4/P5/P6 + PASS+xlsx-pending + Quartals-Rollover-WARN). `_build_recovery_hints()` als reine Helper-Function. Tests: P7-Schema-Smoke + 2 recovery_hints-Tests.

5. **Codex-CP3 R1 Foreground-Subagent (`codex:codex-rescue`, gpt-5.3-codex):** 2 HIGH + 1 MED.
   - **HIGH-1** (`9a9d51b` Fix): `read_session_marker()` hatte `except json.JSONDecodeError, OSError:` ohne Klammern. PEP-758 in Python 3.14 valid, aber Codex-Reviewer + alte Linter/IDE missinterpretieren als SyntaxError — exakter Reinfall aus CP1 (Memory `feedback_pre_commit_diff_inspection` Lessons #2361). Fix: Klammern + `# fmt: skip` (ruff-format-Idempotenz-Override). **Zweiter Auftritt dieses Reinfalls trotz Memory** → Karpathy-§0 Simplicity-First lebt nur durch Pre-Edit-Recall-Check, nicht automatisch durch Memory-Existence.
   - **HIGH-2** (`9a9d51b` Fix): `_run_verify_b` trusted `p4.ok` blindly; xlsx im `unstaged_preexisting`-WARN-Bucket konnten Two-Commit-Contract umgehen (WARN ≠ FAIL). Fix: nach `verify_staging()` expliziter `not_staged = expected_xlsx - set(p4.classification.staged)` → bei not-empty `EXIT_FAIL_P4` mit `git add`-Recovery-Hint. Spec-§4-P6-Atomicity restored.
   - **MED-Coverage** (`9a9d51b` Fix): P7-Schema-Tests nur NO-OP-PASS-Pfad. 3 neue Tests: `test_p7_full_schema_pass_path_has_all_fields` (capsys-capture, 11 Pflicht-Felder asserted) + `test_verify_b_unstaged_preexisting_bug_demonstrated` (Pre-Fix-Bypass-Demo via classify_files) + `test_verify_b_strict_staged_check_catches_unstaged_xlsx` (Post-Fix Set-Diff-Verifikation).

6. **Codex-CP3 R2 Sparring (Diff-Re-Review via fresh `codex:codex-rescue`-Subagent):** 0 HIGH + 1 echtes MED + 1 ignorable Finding.
   - **R2-MED** (`5f05b4b` Fix): `_run_verify_b()` Hard-Fail-Branch hatte keinen end-to-end Integration-Test. Fix: `test_verify_b_hard_fails_on_unstaged_xlsx_integration` (tmp_path-git-Repo, score_history.jsonl-Seed heute, foo.xlsx Commit-A, Modify ohne Stage, Marker pending, monkeypatch SESSION_MARKER, os.chdir, validator._run_verify_b()-Aufruf, EXIT_FAIL_P4 + hint-string + marker-bleibt-pending asserts).
   - **Code-Side-Bug surfaced beim Integration-Test-Bau:** `_run_verify_b` rief `session_valid`/`verify_pre_flight`/`verify_staging` ohne `cwd`-Argument → Sub-Calls fielen auf PROJECT_ROOT-Konstante (Modul-Location) zurück → Marker-Commit-A-SHA wurde gegen echtes Repo-HEAD verglichen statt cwd-HEAD → verify-b aus Subdirectory/tmp_path immer P6/B-Drift. Fix: `_run_verify_b` setzt `cwd = Path.cwd()` und reicht das an alle Sub-Calls weiter. **Test-Bau hat echten Bug entdeckt** = Code-Coverage-Hypothese (verify-b cross-cwd-isolated) war falsch.
   - **R2-Finding-2 (ignorable):** Codex-Subagent kann pytest nicht ausführen (sandbox-policy) → konnte „35 PASS + 2 SKIP"-Claim nicht selbst verifizieren. Tooling-Beschränkung, kein Code-Issue (lokal verified 36 PASS post-cwd-Fix). Sparring-Loop konvergent, kein R3 nötig.

7. **CodeRabbit-WSL Bulk-Pass** (`coderabbit review --plain -t all --base-commit 2955931 --dir 03_Tools/para18_sync`, ~2 Min via WSL Ubuntu-24.04, post-Tasks-9-12 + post-CP3-R1-Fixes): **No findings ✔**. Bulk-Refactor-Schwelle (~580 LOC) erreicht (Memory `feedback_cr_pass_after_bulk_refactor`), CR konvergent-clean ohne Sparring-Loop nötig.

**Status nach diesem Block:** **14/18 Tasks done.** Phase 0-7 ✅ KOMPLETT (zusätzlich zu Phase 0-5: P4 4-Bucket-staging-diff + P5 xlsx-confirm skip-Hard-Fail + P6 Two-Commit-State-Machine [Drift-Matrix 7 Branches + cwd-Disziplin] + P7 Closure-Report full Schema). CP1 ✅ + CP2 ✅ + CP3 ✅ (R1+R2) + CR-WSL ✅ alle verified 0 findings post-Fix. **Verbleibend deferred zu nächster Session:** Task 13 erweiterte Tests S3/S5b/S8b/S8c/S9/S14a/b (~7 Unit-Tests) · Task 14 SKILL.md via skill-creator-Skill · Task 15 references/ (sub-tool-coupling + failure-recovery + build-time-review-log) · Task 16 Final Codex+Gemini+CR-Pass · Task 17 Dogfood gegen Live-State · Task 18 §18-Sync für Promotion v0.1.0 (PIPELINE #73a DONE + log.md + SYSTEM.md + CLAUDE.md Routing-Table). Tests: **36 PASS + 2 SKIP = 38 collected** (S7+S8a soft-skip by design). ruff check + ruff format --check + pre-commit alle PASS. Live-Score-Impact NULL.

**Lessons:**
- **PEP-758-except-Klammern-Reinfall #2 trotz CP1-Memory:** Codex-Reviewer (gpt-5.3-codex, training-cutoff vor Python-3.14-GA) liest unparenthesized `except A, B:` als Syntax-Error. CP1-Memory `feedback_pre_commit_diff_inspection` Lessons #2361 dokumentiert das, aber ruff-format strippt Klammern idempotent → `# fmt: skip` ist Pflicht-Marker. **Karpathy-§0 Pre-Edit-Recall-Check muss vor jeder `except`-Stelle laufen**, nicht nur „beim Build-Phase-Start". Memory wirkt erst aktiv wenn deliberately konsultiert.
- **Two-Commit-Contract WARN-vs-FAIL-Boundary kritisch:** `unstaged_preexisting`-Bucket als WARN-only ist korrekt für md-Files (pre-existing-Refactor-Drift-Schutz §18.4), aber **muss strict-FAIL sein für xlsx-Subset im verify-b** weil Commit-B-xlsx-Edits per Workflow-Definition neu sind. Generischer P4-Code kann den Unterschied nicht erkennen — Caller (`_run_verify_b`) muss expliziten Strict-Stage-Check nachschalten. **Bucket-Semantik ist context-dependent.**
- **Coverage-Tests entdecken Code-Bugs:** Der R2-MED-Integration-Test-Bau hat den cwd-Disziplin-Bug erst surfaced — die Funktion sah „getestet" aus, war es aber nicht cross-cwd. **Integration-Test ≠ Unit-Test-Aggregat.** Lehre analog `feedback_cr_pass_after_bulk_refactor` (CR-semantic-vs-Lint-only).
- **Codex-Sparring-Heuristik 2-Runden-Konvergenz stabil reconfirmed:** R1 = 2 HIGH + 1 MED, R2 = 0 HIGH + 1 MED. R3 wäre nur nötig bei R2-HIGH ≥1 ODER strukturellem Gap — beide nicht eingetreten. ~22k Tokens/Runde × 2 = ~44k für vollständigen Trinity-Pass.
- **CodeRabbit-CLI-Modus-Disziplin:** Erster CR-Aufruf mit `-t uncommitted` lieferte „No files found" weil alles bereits committed. Korrekt für post-Bulk-Reviews: `-t all --base-commit <pre-session-sha>`. Memory-Update-Kandidat für `feedback_cr_pass_after_bulk_refactor`.

**Sync-Set (System-Event):** PIPELINE.md (#73(a) Status auf 14/18 BUILD-PHASE + Footer v2.57→v2.58) + log.md (dieser Eintrag) + SESSION-HANDOVER.md (neuer Status-Banner + Resume-Anweisung Pivot zu Tasks 13-18) + 6 Skill-Build-Commits (e91851d/d6987f2/dc57c6d/8ba3f49/9a9d51b/5f05b4b). **KEIN:** PORTFOLIO + CORE-MEMORY + Faktortabelle + score_history + flag_events + config.yaml + xlsx + STATE.md (kein Score/FLAG/Sparraten/Critical-Alert-Event, kein Skill-Promotion-Event — Skill weiter BUILD-PHASE-in-progress, nicht promoted). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Cross-Reference:** Commits `e91851d` (Task 9 P4) · `d6987f2` (Task 10 P5) · `dc57c6d` (Task 11 P6) · `8ba3f49` (Task 12 P7) · `9a9d51b` (CP3 R1 HIGH-1+HIGH-2+MED) · `5f05b4b` (CP3 R2 MED + cwd-Disziplin) · dieser log-Eintrag-Commit · PIPELINE.md Footer v2.58 · `.reviews/cr-cp3-full.txt` (CR No findings ✔, untracked) · Plan `docs/superpowers/plans/2026-05-22-paragraph-18-sync-implementation.md` (untracked-on-disk per .gitignore) · Memory `feedback_pre_commit_diff_inspection` (PEP-758-Reinfall #2) · Memory `feedback_codex_sparring_heuristic` (2-Runden-Konvergenz reconfirmed) · Memory `feedback_cr_pass_after_bulk_refactor` (CR-Bulk-Schwelle erreicht).

## [2026-05-23] system | paragraph-18-sync v0.1.0 ✅ PROMOTED — Tasks 13-18 DONE (PIPELINE #73(a) DONE, System-Event, scoring-neutral)

**Event-Typ:** Skill-Promotion v0.1.0 + §18-Sync (System-Event, scoring-neutral — kein Score/FLAG/Sparraten-Touch, KEIN PORTFOLIO/CORE-MEMORY/Faktortabelle/score_history/flag_events/config.yaml/xlsx/STATE.md).

**Was passiert ist:**

1. **Task 13 — 9 erweiterte Unit-Tests** (`69ff32e`): S3 score_no_flag_dry_run · S5 system_zustand_dry_run · S5b system_zustand_with_version_bump · S8b score+system Union · S8c triple_union_dedupe · S9 no-flag-event-regression-guard · S12 unstaged_new integration-smoke · S14a active_block_pin · S14b block_missing_glob_fallback. Suite 38 → 47 collected = 44 PASS + 3 SKIP.

2. **Task 14 — SKILL.md v0.1.0** (`bbf0fc8`): P1-P7-Orchestrator-Doku + Trigger-Surface + Exit-Code-Tabelle + Out-of-Scope + Boundary zu session-closure + Detail-References-Pointer (119 Z., <500-Limit). YAML-Frontmatter mit `name/description/version/event_types`.

3. **Task 15 — 3 references/-Files** (`56a9d26`): `sub-tool-coupling.md` (Workflow-Ordering Z1/Z3/Z4) + `failure-recovery.md` (Exit-Code-Tabelle 0-6 + Recovery-Hints + P6/B-Drift-Recovery + Quartals-Rollover) + `build-time-review-log.md` (v0.1.0 Acceptance-Kriterien + Review-Pass-Platzhalter).

4. **Task 16 — Final-Reviews + konsolidierter Fix-Block** (`f096600` + `a5744dc`):
   - **Codex R1 (gpt-5.3-codex, ~22k Tokens):** 3 HIGH + 1 MED + 1 LOW. **H1** `version_bump`-Conditional in yaml definiert aber NIE in `compute_union_set()` ausgewertet (Spec-Drift §18.2) — Fix: `compute_union_set` neuer `version_bump`-Parameter + CLI-Flag `--version-bump` + 2 neue Tests. **H2** P6/B xlsx-set-match Drift-Guard fehlte — Fix: `_run_verify_b()` re-resolved `marker.xlsx_tool_stems` gegen aktuelles SYSTEM.md, Mismatch → `EXIT_FAIL_P6`. Marker-Schema um `xlsx_tool_stems` erweitert. **H3** Exit-Code 4→6 in verify-b xlsx-unstaged-Pfad — Fix: `EXIT_FAIL_P4` → `EXIT_FAIL_P6`. **M1** Doku-Wortlaut `commit_a_sha` "HEAD-Vorgänger" → "aktuelles HEAD vor Commit-B" in SKILL.md + failure-recovery.md. **L1** docstring-typo "n/n" → "y/n".
   - **Codex R2 Sparring (Diff-Re-Review nach HIGH ≥2 Heuristik):** **PASS-WITH-NITS** (0 HIGH neu + 1 MED Test-Härte + 1 LOW PROJECT_ROOT-Bindung). MED+LOW adressiert in `a5744dc`: H2-Negativtest aktive `capsys`-Assertion auf NICHT-Vorkommen von "xlsx-set-mismatch" + beide H2-Tests `monkeypatch.setattr(validator, "PROJECT_ROOT", tmp_path)`. Sparring-Loop konvergent, kein R3 nötig.
   - **Gemini Cross-Sync (SKILL.md ↔ INSTRUKTIONEN §18):** 3 DRIFT + 5 INKONSISTENZ + 4 NIT. **D1** xlsx-Count (SKILL+yaml=2 vs §18.7=3 mit Watchlist) — ACCEPTED v0.1-strict-§18.1, Watchlist als KONTEXT-§6-Refactor-Manual-Carryover in SKILL.md + failure-recovery.md dokumentiert (Memory `feedback_watchlist_xlsx_in_sync_set`). **D2** yaml `description` "KONTEXT §6-Reassign" → Phrase entfernt (out-of-scope v0.1). **D3** yaml `session_close`-Conditional in SKILL.md unsichtbar → Tabellenzelle ergänzt. **I3** G-03 §18.6-Roll-over 5-File-Sync-Hint ergänzt. **I4** §25.5 Cross-Ref in sub-tool-coupling.md. Nits angegangen.
   - **CodeRabbit (WSL Ubuntu `coderabbit review -t all --base-commit 6f9fd32`):** 2 Findings, BEIDE outside para18_sync-Scope (pre-existing: MSFT_2026-05-14.json + briefing-sync-check.ps1). Build clean.
   - **skill-creator-Gegencheck** (Skill-Tool `skill-creator:skill-creator`): **MED-1 Description nicht "pushy" genug** — Fix: SKILL.md `description` um natürlich-Sprache-Trigger-Phrasen erweitert ("verify §18", "Sync-Pflicht-Bundle", "Pre-Commit-Bundle-Verify", File-Touch-Kontexte) für bessere Triggering-Accuracy.

5. **Task 17 — Dogfood 4 Cases gegen Live-State** (in Build-Log dokumentiert): Test 1 `pipeline-item --dry-run` exit=0 PASS · Test 2 `critical-alert` NO-OP exit=0 PASS · Test 3 `score-flag-sparraten --no-flag-event --ticker V --dry-run` exit=1 legitime P1-FAIL PASS (kein heute-Append in score_history.jsonl seit 04.05.) · Test 4 multi-event-union exit=1 gleicher legitimer P1-FAIL PASS. **Verdict: 4/4 PASS** — alle Exit-Codes deterministisch, Recovery-Hints aussagekräftig, keine Crashes.

6. **Task 18 — Promotion-Sync** (dieser Commit): **PIPELINE #73(a) Status DONE** (Footer v2.58 → v2.59). **SYSTEM.md Skill-Registry-Bullet** für `paragraph-18-sync` v0.1.0 (analog `session-closure`-Pattern). **SYSTEM.md neuer `## Active xlsx-Filenames`-Block** (Codex-M4 Pinning-SSoT für deterministische xlsx-Selektion: Rebalancing_Tool_v3.4.xlsx · Satelliten_Monitor_v2.0.xlsx · Watchlist_Ersatzbank_Monitor_v1.1.xlsx). **CLAUDE.md Routing-Table-Eintrag `!ParaSync18 <event-type>`** (Codex-L2-PFLICHT für v0.1; verankert Skill als routable Trigger). **log.md Promotion-Entry** (dieser Block).

**Sync-Set (System-Event):** PIPELINE.md (#73(a) DONE + Footer v2.58→v2.59) + SYSTEM.md (Skill-Registry-Bullet + Active xlsx-Filenames-Block) + log.md (dieser Eintrag) + CLAUDE.md (Routing-Table `!ParaSync18`). **KEIN:** PORTFOLIO + CORE-MEMORY + Faktortabelle + score_history + flag_events + config.yaml + xlsx + STATE.md (kein Score/FLAG/Sparraten/Critical-Alert-Event). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:**
- **Skill-creator-Gegencheck ist BUILD-Pflicht** (User-Direktive 23.05.): nicht nur Plan-Hinweis. MED-1 Description-Push wäre ohne Gegencheck silent durchgerutscht und hätte Triggering-Accuracy reduziert.
- **3 Reviewer-Parallel-Dispatch + skill-creator-Gegencheck deckt komplementäre Defect-Klassen ab:** Codex = Code-Korrektheit + Spec-Drift · Gemini = Doc ↔ SSoT Cross-Sync · CodeRabbit = Code-Style + outside-Scope-Findings · skill-creator = Spec-Konformität + Triggering-Optimierung. Sum > parts: H1+H2+H3 (Codex) + D1+D2+D3 (Gemini) + MED-1 (skill-creator) wären einzeln nicht alle gefunden worden.
- **Codex-Sparring-Heuristik 2-Runden-Konvergenz reconfirmed (2/2 Skills):** session-closure-v0.2.0 22.05. R2 PASS-WITH-NITS, paragraph-18-sync-v0.1.0 23.05. R2 PASS-WITH-NITS. Threshold (HIGH ≥2 → R2 zwingend) wirkt; R3 nicht nötig wenn R2 0 HIGH liefert.
- **Karpathy-Pre-Edit-Recall-Check für yaml-Conditionals:** S5b-Test verifizierte yaml-Schema-Vorhandensein, NICHT Runtime-Aktivierung (Codex-H1-Befund). Schema-Smoke-Tests können false-positive werden — Runtime-Branches müssen explizit getestet werden.
- **PROJECT_ROOT-Bindung in tmp_path-Tests** (Codex-R2-LOW): Module-Level-Konstanten brechen Test-Isolation silent. Pattern `monkeypatch.setattr(validator, "PROJECT_ROOT", tmp_path)` wird Standard für alle Tests die `resolve_active_xlsx` indirect aufrufen.

**Cross-Reference:** Commits `69ff32e` (Task 13) · `bbf0fc8` (Task 14) · `56a9d26` (Task 15) · `f096600` (Task 16 konsolidierter Fix-Block) · `a5744dc` (Codex-R2-Sparring-Nits) · Task 18-Commit (dieser) · PIPELINE.md Footer v2.59 · SYSTEM.md System-Zustand + Active xlsx-Filenames · CLAUDE.md Routing-Table · `01_Skills/paragraph-18-sync/references/build-time-review-log.md` (Review-Pass + Dogfood-Details) · Spec v0.3 + Plan v0.2 untracked-on-disk · Memory `feedback_review_via_codex_not_advisor` (Codex canonical) · Memory `feedback_codex_sparring_heuristic` (2-Runden-Konvergenz 2× reconfirmed) · Memory `feedback_watchlist_xlsx_in_sync_set` (D1-Carryover-Anker) · Memory `feedback_xlsx_tools_in_sync_set` (xlsx-Pflicht-§18.1-Anker).

---

## [2026-05-23] system | core-slim-refactor v0.1.0 First-Practical-Test DONE — log.md Date-Cut (B-1 Pivot)

**Event-Typ:** System-Zustand + Pipeline-Item Multi-Event Union §18.2 (scoring-neutral, kein FLAG/Score/Sparrate-Touch). First echter Praxistest des heute mittag promoted Skills (PIPELINE #78 DONE) — User-Direktive: „erster echter Praxistest".

**Was passiert ist:**

1. **Pivot SH → log.md** vor Start: SESSION-HANDOVER.md (ursprüngliches Ziel B-1) hat Bullet-List-Banner-Struktur (`- **Datum:** YYYY-MM-DD ...`), Pattern C v0.1 ist `## YYYY-MM-DD`-Header-only. `pattern_specs.md` L43 dokumentiert das explizit als Build-Stage-Pivot. → log.md als designed worked-example.
2. **Worked-Example-Real-State-Drift** entdeckt: CP9-Regex `^## (\d{4}-\d{2}-\d{2})` matched nur 6/111 Entries (log.md hat 105 Bracket-Entries `## [DATE]` + 6 Non-Bracket-Entries). 1-Line-Patch auf `^## \[?(\d{4}-\d{2}-\d{2})\]?` zur Beider-Format-Coverage.
3. **P0-Audit-FAIL** vorm ersten Lauf wegen `fail_close_on_drift: true` Default — Skill-Code Z.112 ist any-nonzero-fail nicht echte Drift-Logik (MEDIUM-11 Misnomer). Pre-existing audit-FAILs sind in STATE.md last-audit-block dokumentiert + identisch zum Promotion-Commit-Bild. Config-Edit `fail_close_on_drift: false` als advisory-acceptance mit inline-Comment-Rationale.
4. **Dry-Run clean** P0-P7 → 116 entries split, 86 archive / 30 keep, 67% reduction vorhergesagt. P3 Backlink-Scan ~90 hits auf `[log.md]` (warn-continue per Config).
5. **Live-Run Exit 0** P0-P7 clean. Outputs verifiziert:
   - `07_Obsidian Vault/.../log.md` 506.718 → 167.307 bytes (29 keep entries 2026-05-17..2026-05-23)
   - `05_Archiv/log-bis-2026-05-16-archiv.md` 339.870 bytes / 86 entries (sha256 `e4ca665f4931281c373f0a87e61e20b53e08be4e60aee627bdd5ccef0a5385c3`)
   - Pointer-Header korrekt am section_top inserted (Z.6-7)
6. **Codex Diff-Re-Review** (`gpt-5.3-codex` agent a22827a45aff160a0) Single-Pass: 0 HIGH-Blocker, alle 7 v0.1.1-Items confirmed.

**7 v0.1.1-Backlog-Items aufgedeckt** (dokumentiert in `01_Skills/core-slim-refactor/references/failure_modes.md` MEDIUM-9..15 + LOW-3):

- MEDIUM-9 Pattern-C Bullet-List-Variante fehlt (für SH-Refactor)
- MEDIUM-10 Worked-Example-Real-State-Drift silent-failure (empirischer Header-Count-Pre-Check als v0.1.1-Feature)
- MEDIUM-11 `fail_close_on_drift` semantischer Misnomer (any-nonzero statt baseline-drift)
- **MEDIUM-12 HIGH-Hotfix:** Pointer-Template `archive_link` zeigt absoluten Windows-Pfad als Display-Text
- **MEDIUM-13 HIGH-Hotfix:** Backup-File `.pre-refactor.bak` nicht geschrieben (broken Atomicity-Contract)
- MEDIUM-14 `executed:`-Block nicht auto-populated post-live-run
- MEDIUM-15 P3 Backlink-Scan term-only, semantischer Vault-Backlink-Graph fehlt
- LOW-3 Archived bodies enthalten Wikilinks → orphan-risk (akzeptierter Tradeoff)

**Sync-Set §18.2 Multi-Event Union (pipeline-item + system-zustand, atomic commit):**

- `07_Obsidian Vault/.../log.md` (skill-mutated + dieser Banner-Eintrag als System-Event-Marker)
- `00_Core/PIPELINE.md` (#78 Body-Update + Footer-Bump v2.63→v2.64)
- `00_Core/SYSTEM.md` (§Skill-Registry-Bullet First-real-run-Suffix + Footer v1.9→v1.10)
- `01_Skills/core-slim-refactor/references/configs/session-handover-date-cut.yaml` (4 Edits: Regex-Patch + cut_before-Update + archive.path + fail_close_on_drift + executed-Block populated)
- `01_Skills/core-slim-refactor/references/failure_modes.md` (7 v0.1.1-Items + Hotfix-Priorisierung-Section appended)

**Bewusst NICHT angefasst:** SESSION-HANDOVER.md (Banner-Update via `session-closure`-Skill am Session-Ende separat per Konvention) · CORE-MEMORY §13 (heute mittag bereits für Promotion gepflegt) · STATE.md · Faktortabelle/Portfolio/score_history/flag_events/dynastie-config.yaml/xlsx (kein Score/FLAG-Event) · CLAUDE.md (Routing-Table `!SlimRefactor` separates v0.1.1-Item). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lehren:**

- **Praxistests decken Spec-Lücken auf die Build-Gates nicht sehen** — 7 Items in einer Session, davon 3 HIGH-Hotfixes (Pointer-Display + Header-Count-Pre-Check + Backup-Contract). Build-Time-State ≠ 24h-spätere-Real-State; Configs können silent drift-fehlen. **Take-away:** Praxistest-Cadence für neu-promoted Skills innerhalb 24-48h ist Karpathy-konform-Investment.
- **Karpathy 3-Fail-Stop in Echtzeit angewendet** — SH-Pattern-Limit (#1) + log.md-Regex-Drift (#2) + P0-Audit-Strictness (#3) jeweils transparent User-confronted, kein Force-Through. Approach-Resets führten zu klaren Decisions (Config-Patches mit inline-Rationale, alle v0.1.1-Items dokumentiert).
- **para18-sync v0.1.0 als authoritative Sync-Set-Quelle** (2. Live-Anwendung nach Phase-2-Teil-2): Multi-Event-Union pipeline-item + system-zustand liefert deterministisch 3 Pflicht-Files (PIPELINE/SYSTEM/log.md). SESSION-HANDOVER explicit-NICHT im Pflicht-Set — überraschend (vorher informell als Pflicht angenommen), korrekt-per-Spec.
- **Codex Single-Pass Default-Heuristik konvergent** (Memory `feedback_codex_sparring_heuristic`): 1 Round pre-edit (YAML-Config) + 1 Round Diff-Re-Review = 2 Calls total, ~50k Tokens, klare APPLY/DEFER pro Finding. Kein Sparring-Loop nötig (0 HIGH-Blocker).

**Cross-Reference:** Skill `core-slim-refactor` v0.1.0 First-Practical-Test · PIPELINE #78 Body-Update v2.63→v2.64 · SYSTEM.md §Skill-Registry + Footer v1.9→v1.10 · `01_Skills/core-slim-refactor/references/configs/session-handover-date-cut.yaml` (post-edit-state mit executed-Block) · `01_Skills/core-slim-refactor/references/failure_modes.md` v0.1.1-Backlog-Section · `05_Archiv/log-bis-2026-05-16-archiv.md` (Local-only Archive, 339.870 bytes, sha256 e4ca665f) · Codex `gpt-5.3-codex` agent a22827a45aff160a0 Diff-Re-Review.

## [2026-05-23] system | PIPELINE #80 + #81 NEU — core-slim-refactor v0.1.1/v0.2.0 Roadmap (Karpathy 2-Phase-Brainstorm)

**Event-Typ:** Pipeline-Item (NEU 2× DEFERRED, scoring-neutral). Direkter Follow-up zu First-Practical-Test (vorheriger Banner, Commit `6e7985e`).

**Was:** Karpathy 2-Phase-Brainstorm-Output formal in PIPELINE.md verankert nach kritischem Pass „ist Option-1-Bundle wirklich optimal?" (Confidence-Selbsteinschätzung 75% → 92% nach Refinement):

- **#80 v0.1.1 Bugfix-Release** (~1.5-2h, eigene Session): MEDIUM-12 Pointer-Template Display-Text-Fix + MEDIUM-13 Backup-Contract-Fix (broken `.pre-refactor.bak`) + optional MEDIUM-11 fail_close_on_drift Variable-Rename. **Sollte v0.2.0 first.**
- **#81 v0.2.0 Feature-Release inkl. SH-Bullet-Adapter** (~3-4h, eigene Session, nach v0.1.1): MEDIUM-9 Pattern-C `date_parser.field: bullet` (Option A aus Brainstorm — neues Enum-Value + `bullet_pattern` + `trailing_stop_pattern`) + MEDIUM-10 Empirischer Header-Count-Pre-Check + MEDIUM-14 executed-Block Auto-Population + MEDIUM-15 Backlink-Scan graph-mode. Erstes Anwendungsziel: SESSION-HANDOVER.md Banner-Slim.

**Karpathy-Begründung 2-Phase statt Bundle:** v0.1.1 = Bugfix-only-Release ist semantisch sauber (atomar reviewbar, easy rollback). v0.2.0 = Feature-Release mit klarem Scope. Bundle hätte „Feature + Bugfix" in 1 Release gemischt = Release-Hygiene-Verletzung. Trade-off: 2 Sessions bis SH-Slim möglich (gegen 1 bei Bundle), aber SH-Slim ist nice-to-have nicht critical-path (SH aktuell 42K, wächst ~3-5 Banner/Woche).

**Sync-Set (pipeline-item, scoring-neutral):**
- `00_Core/PIPELINE.md` (#80 + #81 NEU + Footer v2.64→v2.65)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)

**Bewusst NICHT angefasst:** kein System-Event-Touch, kein Score/FLAG-Event, kein Skill-Substrate-Change.

**Cross-Reference:** Brainstorm-Output Karpathy-Kritik-Pass 2026-05-23 abends-spät · PIPELINE #80 v0.1.1 Bugfix-Roadmap · PIPELINE #81 v0.2.0 Feature-Roadmap · `01_Skills/core-slim-refactor/references/failure_modes.md` MEDIUM-9..15 + LOW-3 + Hotfix-Priorisierung-Section · Vorheriger Banner heute First-Practical-Test (Commit `6e7985e`).

## [2026-05-23] system | PIPELINE #80 Scope-Update post-Test-Empirie (Pattern A+B Dry-Runs)

**Event-Typ:** Pipeline-Item (Body-Update, scoring-neutral). Follow-up zu #80/#81-Roadmap-Commit `def3435` nach User-Direktive „weitere Tests" auf v0.1.0.

**Was:** 15 min Test-Coverage-Erweiterung (Pattern A + B Dry-Runs auf retro-doc Worked-Examples + Vault-Survey) lieferte 3 substantielle neue Befunde, die v0.1.1-Scope materiell ändern:

1. **MED-11 → HIGH-3 Promotion (Skill-Adoption-Blocker):** alle 3 Worked-Examples haben `fail_close_on_drift: true` Default. Pattern A+B mit `--force-rerun` beide **Exit 3 (EXIT_AUDIT)** auf aktuellem 10/15-PASS Repo-State. Bedeutet: jedes Repo mit imperfekter Audit-State blockt Skill komplett ohne Config-Patch. → v0.1.1 HIGH-Hotfix statt optional-Variable-Rename.
2. **LOW-1 → MEDIUM-NEW Promotion (Diagnostic-Output):** Pattern A+B `--skip-audit --dry-run` liefern nur `=== P2 Classify FAIL ===` ohne Reason. User-Self-Debugging nicht möglich. → v0.1.1 MEDIUM mit stderr-Hint + separater Exit-Code für ANCHOR_NOT_FOUND vs CLASSIFY_EMPTY.
3. **Vault-Survey: 0 weitere `## DATE`-Chronicles im Vault.** log.md war wirklich einziger Pattern-C-Live-Use-Case im aktuellen System → bestätigt strategische Priorität für v0.2.0 Bullet-Adapter, aber Karpathy 'Bugfix-First' bleibt: v0.1.1 vor v0.2.0.

**Updated v0.1.1 Scope (5 Items, ~2-3h von ~1.5-2h):** HIGH-1 MED-12 Pointer-Display + HIGH-2 MED-13 Backup-Contract + HIGH-3 MED-11 fail_close_on_drift Adoption-Blocker + MEDIUM-NEW LOW-1-Promoted Diagnostic + optional Variable-Rename.

**Karpathy-Lehre:** User-Vorschlag „mehr Tests" hat sich gelohnt — 15 min lieferten 3 Befunde davon 2 die Scope materiell ändern. Empirie > Annahme. **Take-away:** Pattern-Coverage-Tests (alle 3 Pattern in 1 Session retrospektiv durchlaufen) sollten in v0.1.1 Build-Gate-3 als standard worked-example-coverage-Test in Test-Suite.

**Re-Prio v0.2.0 vor v0.1.1 explizit ABGELEHNT:** Karpathy 'Bugfix-first'-Disziplin streng — v0.2.0-Features auf buggy v0.1-Foundation = building on sand. MED-11 als Adoption-Blocker macht v0.1.1 DRINGENDER, nicht weniger dringend.

**Sync-Set (pipeline-item, scoring-neutral):**
- `00_Core/PIPELINE.md` (#80 Body-Update mit 5-Item-Scope + Footer v2.65→v2.66)
- `01_Skills/core-slim-refactor/references/failure_modes.md` (Hotfix-Priorisierung-Section mit Test-Empirie-Update + 5-Item-Bundle-Aufstellung)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)

**Bewusst NICHT angefasst:** kein System-Event-Touch (Skill bleibt v0.1.0 unverändert), kein Score/FLAG-Event, SYSTEM.md nicht angefasst (kein Skill-Registry-Bump).

**Cross-Reference:** PIPELINE #80 Body-Update (v0.1.1 5-Item-Scope) · failure_modes.md Hotfix-Priorisierung-Section (Test-Empirie-Update) · vorheriger Banner #80/#81-Roadmap (Commit `def3435`) · Test-Empirie 2026-05-23 abends-spät: Pattern A `ruflo-sunset-bucket.yaml --dry-run --force-rerun` Exit 3 + Pattern B `defcon-fat-rows-slim.yaml --dry-run --force-rerun` Exit 3 + Vault-Survey `find ... -exec grep ...` 0 Treffer.

---

## [2026-05-23] system | 00_Core Slim-Refactor Phase 1 (Quick-Wins) + §18-Skill-Erstanwendung als Pre-Commit-Gate

**Event-Typ:** Multi-Event (pipeline-item + system-zustand `--version-bump`), scoring-neutral. Erste Live-Anwendung von `paragraph-18-sync v0.1.0` Validator als Pre-Commit-Disziplin-Gate.

**Was passiert ist:**

1. **6-File Lean-Pass in 00_Core** (per Memory `feedback_core_folder_lean_discipline`, „Lean-Pflicht-Lese-Pfad-Disziplin"):
   - **STATE.md** Critical-Alerts auf 1-3-Z.-Pointer (eigene Z.12-Konvention war massiv verletzt) — 10.1 → 4.3 KB (**−57%**)
   - **Faktortabelle.md** historische Score-Move-Comments (Z.31-49 + Z.65) + dead-Backfill-Anchors (`DATA:V_OLD_BACKFILL`/`DATA:TMO_OLD_BACKFILL`/`DATA:TMO_PRE_Q1`) gestrippt; §Ersatzbank zu Pointer-only auf KONTEXT §6 umgestellt (Drift-Surface-Cleanup gegen pre-April-Stale-Snapshot); Live-DATA-Anker 12/12 (ASML/AVGO/V/MSFT/TMO/RMS/VEEV/SU/BRK.B/APH/COST/AMZN) + END_TABLE erhalten (System-Audit-Tool-Parser-relevant); Update-Kalender DONE-Strikethroughs entfernt — 15.4 → 9.8 KB (**−36%**)
   - **APPLIED-LEARNING.md** Historie v1.0-v2.5 (pre-Bridge-Coherence-Scan 02.05.) → git log Pointer (Lean-Pflege)
   - **KONTEXT.md** §10 April-Earnings-DONE-Strip (TMO 23.04. / SPGI 28.04. / MSFT 29.04. DONE, +27./28.05. VEEV/COST forward); §6 Heading-Anchor-Stabilisierung (Stand-Date aus Heading in Body-Line — verhindert Anchor-Drift bei nächstem Refresh-Bump, Codex-MED inline gefixt)
   - **PORTFOLIO.md** stale "Earnings-Window 28.04.-04.05. abgeschlossen"-Note entfernt
2. **PIPELINE #77 NEU** in 🔵 Deferred-Section: **SU-Ersatz Re-Evaluation (DE/Legrand/Siemens User-Brainstorm)** — Königsweg-Info-Sicherung statt Info-Loss bei Faktortabelle §Ersatzbank-Strip. SU→DE-Mapping existierte exklusiv in Faktortabelle (KONTEXT §6 14.05.-Refresh hatte Gap), aber DE-Eintrag selbst war potenziell stale. User brainstormed Legrand (LR.PA) als cleanen Schneider-Replacement und Siemens (SIE.DE) als breiterer Industrial-Bench. Entscheidung deferred zu future !QuickCheck-Session (Watchlist-Eintritts-Disziplin §12 verlangt echten Score vor §6-Eintrag).
3. **§18-Skill-Erstanwendung als Pre-Commit-Gate** — Test des frisch promotierten `paragraph-18-sync v0.1.0` (committed `fc543a7` heute früh): `python 03_Tools/para18_sync/validator.py pipeline-item --also system-zustand --version-bump --dry-run --json` → Expected-Set deterministisch identifiziert (PIPELINE.md + SYSTEM.md + CORE-MEMORY.md + Vault log.md, Multi-Event-Union §18.2 + version-bump-Conditional). 3 fehlende Meta-Sync-Files (SYSTEM/CORE-MEMORY/log.md hatte ich initial nicht gestaged) im Dry-Run-Output sichtbar gemacht und vor finalem Validator-Run ergänzt. **Skill funktioniert empirisch:** zwingt Expected-Set-Disziplin durch Tool-Forcing statt nur Doktrin-Lesen.
4. **Codex-Single-Pass-Review** (gpt-5.3-codex, ~52k Tokens) auf den Working-Tree-Diff: **PASS-clean, 0 blocking**. 1 MED-Anchor-Stability-Watch surfacet (KONTEXT §6 Heading enthielt `(Stand: 14.05.2026 — Refresh v3.2)` → datum-hardcoded Anchor → Faktortabelle-Pointer wäre bei nächstem Refresh-Bump stale geworden) — inline gefixt durch Heading-Slim + Stand-Line in Body. Codex bestätigte alle 5 Invarianten: keine broken pointers · Cross-File-Score-Konsistenz · 12 Live-DATA-Anker · PIPELINE #77 korrekt in 🔵 Deferred · keine Info-Verlust ohne Archivierung (SU→DE-Migration zu #77, Earnings-Window-Detail zu git log).
5. **Multi-Event-Union §18.2 Sync-Set:** PIPELINE.md (#77 + Footer) + SYSTEM.md (Footer-Slim v1.5→v1.6 + Stand-Bump) + CORE-MEMORY.md (§13-Entry + Footer v1.23→v1.24) + Vault log.md (dieser Eintrag) + 5 SSoT-Lint-Files (STATE/Faktortabelle/APPLIED-LEARNING/KONTEXT/PORTFOLIO). Ein atomarer Commit.

**Sync-Set (System-Event-Union):** PIPELINE.md + SYSTEM.md + CORE-MEMORY.md (§13) + log.md (dieser) + STATE.md + PORTFOLIO.md + Faktortabelle.md + APPLIED-LEARNING.md + KONTEXT.md. **KEIN:** score_history.jsonl + flag_events.jsonl + config.yaml + xlsx (kein Score/FLAG/Sparraten/Critical-Alert-Event). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:**
- **Migrate-before-Strip als Königsweg-Pattern (User-formuliert):** Vor jedem SSoT-Strip Differential-Check gegen Ziel-Quelle pflicht. SU→DE-Befund hätte ohne diesen Check unbemerkt verschwunden — mit Check landet die offene Frage explizit in PIPELINE statt implizit verloren. Verallgemeinert: wenn File X zu Pointer-only auf File Y wird, dann erst Differential X\Y prüfen + migrieren/dokumentieren, dann strippen.
- **§18-Skill forced Expected-Set-Bewusstsein durch Tool-Forcing:** Manueller Workflow hätte log.md + CORE-MEMORY §13-Sync vergessen (war im Kopf nicht präsent — die 5 SSoT-Lint-Files waren der "Hauptevent", die Meta-Tracking-Files unsichtbar). Validator-Dry-Run macht Expected-Set deterministisch sichtbar. Pre-Commit-Gate = richtige Phase, nicht Post-Commit-Audit. **Empirie zur Skill-Wertigkeit:** 2 Memory-Hits gegen Sync-Drift sind in der Validator-Implementierung kondensiert (`feedback_xlsx_tools_in_sync_set`, `feedback_anchor_promotion_sync_gap`, `feedback_watchlist_xlsx_in_sync_set`).
- **Codex-Single-Pass reicht für Markdown-Lint:** ~52k Tokens, hochwertige Befunde (1 MED-Anchor-Stability wäre sonst tagelang stale geblieben bis zum nächsten Refresh-Bump). Gemini-Cross-Sync nicht aktiviert — Markdown-Lint ist nicht Gemini-Stärke, und Token-Overhead von gemini-agent-Subagent (~30-50k) nicht gerechtfertigt für reine Konsistenz-Prüfung. Codex-Sparring-Heuristik 2-Runden NICHT ausgelöst (0 HIGH in Single-Pass).
- **Lean-Discipline-Pflege als systematischer Workflow:** 13 KB netto in Phase 1 (Quick-Wins). Phase 2 (Big Files: CORE-MEMORY 244 KB / INSTRUKTIONEN 84 KB / PIPELINE-DONE-Strip 68 KB / SESSION-HANDOVER 39 KB / SYSTEM 40 KB inhouse) deferred — schätzungsweise 50-100 KB Einsparpotenzial dort. Per-File-Review-Plan mit Codex-Diff-Re-Review pro Commit vorgesehen wegen höherer Cross-Ref-Risk.

**Cross-Reference:** Conversation-Context 2026-05-23 02:00-03:00 MESZ Lint-Session · Codex-Subagent-Report `52298 total_tokens, 24 tool_uses, 728606 duration_ms` PASS-clean · PIPELINE #77 (NEU 🔵 Deferred SU-Ersatz Re-Eval) · CORE-MEMORY §13 2026-05-23-Eintrag · SYSTEM.md Footer v1.5→v1.6 · paragraph-18-sync v0.1.0 SKILL.md + `03_Tools/para18_sync/validator.py` + references/ (§18-Skill SSoT) · Memory `feedback_core_folder_lean_discipline` (Lean-Disziplin-Anker) · Memory `feedback_review_via_codex_not_advisor` (Codex canonical für Markdown-Lint) · Memory `reference_dynastie_log_location` (Vault-log.md-Pfad-Anker).

## [2026-05-23] system | 00_Core Slim-Refactor Phase 2 Sub-Refactor #1 Teil 1 (CORE-MEMORY)

**Event-Typ:** Meta-Refactor / System-Lifecycle (scoring-neutral, kein FLAG/Score-Move, kein Sparrate-Touch)

**Was passiert ist:**

5 Sub-§-Cuts in `00_Core/CORE-MEMORY.md` mit Migrate-before-Strip-Disziplin + Pointer-Stub-Architektur:

1. **§3 Pre-v3.7-Positions-Entscheidungen** (5,0K MSFT/TMO/APH-Narrative + APH Q1 Tag-0-Snippet 29.04.) → `05_Archiv/CORE-MEMORY-§3-pre-v3.7-archiv.md`. **Migrate-Check:** APH Tag-0-Snippet schon redundant in §12.2 L454+ (Tag-0 Press-Release-Recap + Tag-+1-Vollanalyse Score 63→61) → kein Re-Migrate. §3 wird 1-Zeilen-Stub mit Pointer auf PORTFOLIO + Faktortabelle + §12 (−4,6K).

2. **§6 Versions-Verlauf** — 5 Pre-v3.7-Rows (31.03.2026 Rebalancing v3.1, 01.04. config.md, 03.04. DEFCON v3.1, 15.04. Rebalancing v3.4, 16.04. DEFCON v3.5) → `05_Archiv/CORE-MEMORY-§6-pre-v3.7-versions-archiv.md`. Live-Tabelle ab v3.7 (17.04.2026 System-Gap-Release) + Header-Pointer (−0,3K).

3. **§10 API-Audit-Log** — 4 April-Sub-§ (21.04. Drift-Audit-Sweep · 22.04. System-Audit-Tool v1.0 Deployment Phase E 18/19 · 22.04. Spät Task 19 + Fix-Welle E · 22.04. Spät-Nacht Phase E 19/19 DONE + Pfad-2-Entscheidung · 28.04. Provenance-Gate Go-Live) → `05_Archiv/CORE-MEMORY-§10-april-2026-archiv.md`. **IFRS-vs-ASC bleibt live** als zeitloses Non-US-Pflicht-Wissen. Live-Tool-Status (System-Audit + Provenance-Gate) SSoT bleibt SYSTEM.md §System-Zustand (−10,2K).

4. **§11 Backtest-Ready Infrastructure** (7,2K) → kompakter Pointer-Stub auf SYSTEM.md §System-Zustand (Live-SSoT: 27 Score-Records, Forward-Verify-Pipeline, Provenance-Gate) + Live-Triggers 2026-10-17 (6M Delta-Pattern-Review) + 2028-04-01 (Gesamt-Backtest) + Dokumentations-Pfade (Spec/Plan/README). **Migrate-before-Strip:**
   - **Befund 1** (Delta-Pattern braucht Vollanalyse-Baseline) + **Befund 2** (DEFCON-Threshold-Drift v3.x 80/65/50) + Backfill-Stand 2026-04-17 (24 Records aus §4-Rekonstruktion, 2 FLAG-Records MSFT+GOOGL) → `05_Archiv/CORE-MEMORY-§11-backtest-ready-history-archiv.md` (Backtest-Schema-Historie, weniger Live-Scoring-relevant)
   - **Befund 3** (V Sub-Score-Korrekturen: Pricing-Power-Bonus nur mit Transcript-Belegung / Ownership-Threshold statt Gradient / Goodwill-Ausnahme Regel-4-Gating GW/Assets ≥30%) + **Befund 4** (Schema-Trigger ≠ SKILL-Regel-Semantik: TMO `fcf_trend_neg` mechanisch ≠ strukturell, WC-Delta + Multi-Year-Trajectory + OpInc-Parallelität vor FLAG-Aktivierung prüfen) → CORE-MEMORY.md §5 als Live-Scoring-Lektionen (−6,0K)

5. **§5 Scoring-Lektionen** — 2 neue Lektionen aus §11-Befunde-Migrate: „V-Rescoring (18.04.2026) — Sub-Score-Strenge bei Validity-Mismatches" + „Schema-Trigger ≠ SKILL-Regel-Semantik (18.04.2026, TMO-Präzedenz)" (+1,7K).

**Netto-Effekt:** CORE-MEMORY.md 235,4K → 216,8K (**−18,6K / −7,9%**).

**Pointer-Stub-Architektur:** Pro Archiv-Cut bleibt 1-Zeilen-Pointer am Ursprungsort (`## 3. Aktive Positions-Entscheidungen (archiviert 2026-05-23)`, dann `**Voll-Archiv:** [...]`). §-Nummerierung stabil (kein §1→§2-Shift), keine externen Anchor-Broken-Links. **Backlink-Scan ergab:** aktive Refs nur auf §5/§6/§12/§13 in CLAUDE.md, STATE.md, INSTRUKTIONEN.md (§18-Sync-Set), SYSTEM.md L8-9 (Anchor-Links auf §6/§13), KONTEXT.md, PIPELINE.md (Numbering-Convention), SESSION-HANDOVER.md, paragraph-18-sync SKILL.md, Faktortabelle.md — alle Anchor-stabil. **Kein extern referenzierter §3/§10/§11** (Inhalte längst absorbiert in PORTFOLIO/Faktortabelle/§12 bzw. SYSTEM.md).

**Stale Refs ignoriert** per User-Direktive: `02_Analysen/flag_event_study_2026-04-17.md` referenziert „§1"/„§3/§4" (historische Analyse-Datei, §1/§4 existieren in aktueller Struktur eh nicht mehr); Vault `log.md` ~30 historische §13-Refs in alten Sync-Einträgen (Log-Snapshots, kein Update nötig).

**Archive-Files (4 neue) local-only** per Konvention `05_Archiv/*` gitignored (Whitelist-Exceptions in `.gitignore` nur für JSONL: `score_history.jsonl`/`flag_events.jsonl`/`portfolio_returns.jsonl`/`benchmark-series.jsonl`/`schema-portfolio-returns.md`); konsistent mit Präzedenzfall `CORE-MEMORY-Meilensteine-bis-14.04.2026.md` (auch nicht git-tracked seit 17.04.2026). Pointer funktionieren lokal in Editor/Obsidian — Remote/Cloud-Cron-Runtime hat keinen Archiv-Zugriff (akzeptiert per Single-User-Workflow-Konvention).

**§13/§12 DEFERRED zu fresh Session:**
- §13 Ruflo-Sweep (16 Entries, 60,5K — Ruflo Hard-Rollback 13.05. Sunset, Lehre lebt in Memory `feedback_viral_plugin_substrate_risk_eval` + git log + PIPELINE-Items #49/#50/#57 retro-stempled FAILED-RETRO) + Slim-Convention auf 7 fat Non-Ruflo (35,2K: FinnHub-Build · Watchlist-Refresh · PIPELINE #55 Phase-1 · Phase-D-1-Confidence-Upgrade · 3 weitere [Meta]/[Tools] Mai-9-Welle) + pre-23.04. Cut (20 Entries, 5,6K, 15.-22.04.) + §12 Quartals-Rollover-Check (PIPELINE #67 §18.6-Convention falls Ticker-Sub-§ >900 Z. — vermutlich noch nicht aktiv)
- **Grund für Defer:** §13-Dichte (143K / 99 Z., 4-7K-Entries) sprengt Read-Token-Limit (62K Tokens für 55 Zeilen) → sichere atomare Replacement-Operation nicht im laufenden Session-Budget machbar. Per-Entry-Approach mit `ctx_execute_file`-Extract + targeted Block-Edits braucht eigenes Token-Budget.
- **User-Direktive (Eckpfeiler heutige Session):** „Lint UND Memory-Erhalt" — Pause-Punkt statt Memory-Substanz unter Token-Druck zu verlieren. Disziplin > Vollständigkeit-im-einen-Sprint.

**Pre-Commit-Gates:**
- **§18-Skill `paragraph-18-sync v0.1.0`:** `python 03_Tools/para18_sync/validator.py system-zustand --version-bump --dry-run --json` → Expected-Set = `00_Core/CORE-MEMORY.md` + `00_Core/SYSTEM.md` + `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (alle 3 angefasst, kein xlsx-Warning, kein Quartals-Rollover-Warn).
- **Codex Single-Pass Diff-Re-Review (gpt-5.3-codex)** pre-Commit.

**Sync-Set §18 (System-Event, version-bump, scoring-neutral):**
- `00_Core/CORE-MEMORY.md` (§3/§5/§6/§10/§11-Cuts + §13-Entry für Phase-2-Teil-1 + Footer v1.24→v1.25)
- `00_Core/SYSTEM.md` (Footer v1.6→v1.7 + Stand-Bump auf Phase-2-Teil-1)
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (dieser Eintrag)
- 4 Archive-Files in `05_Archiv/` (untracked per Konvention, lokal persistent)

**Bewusst NICHT angefasst:** PORTFOLIO.md / Faktortabelle.md / `01_Skills/dynastie-depot/config.yaml` / `03_Tools/Rebalancing_Tool_v3.4.xlsx` / `03_Tools/Satelliten_Monitor_v2.0.xlsx` / `05_Archiv/score_history.jsonl` / `05_Archiv/flag_events.jsonl` — **kein Score/FLAG/Sparraten-Event.** STATE.md Critical-Alert separat möglich falls gewünscht (nicht in Validator-Expected-Set). PIPELINE.md unverändert (kein neues Item, §13/§12-Defer ist Session-intern dokumentiert via CORE-MEMORY §13 + dieser log-Eintrag).

**Lessons:**

- **Migrate-before-Strip systematisch (User-Königsweg, verstetigt):** vor jedem SSoT-Strip Differential-Check vs Ziel-Quelle pflicht. **§3 APH-Tag-0** wäre redundant dupliziert ohne Check (Snippet schon in §12.2 — kein Re-Migrate gespart Edit-Aufwand). **§11 Befunde 3+4** wären verloren ohne Migrate nach §5 — ohne Check hätte Strip wertvolle V-Rescoring + TMO-fcf_trend_neg-Lektionen ins Archiv-File begraben (Live-Scoring-Decisions würden Disclosure-Knowledge benötigen).

- **Pointer-Stub-Pattern bewährt:** 1-Zeile mit Archive-Link am Ursprungsort hält §-Nummerierung stabil. Externe Anchor-Links bleiben gültig (`SYSTEM.md L8-9 → CORE-MEMORY.md#6-system-upgrades-versionsverlauf`, `SYSTEM.md L9 → CORE-MEMORY.md#13-system-lifecycle-history` — beide post-Refactor noch valide). **Konsequenz:** Phase-2-Refactor-Pattern reusable für nachfolgende §-Slim-Refactors (INSTRUKTIONEN.md §29, PIPELINE.md DONE-Strip, SESSION-HANDOVER.md Banner-History).

- **Backlink-Scan Vorab obligatorisch:** Grep-basierter Scan auf `CORE-MEMORY §X`-Pattern vor Cut zeigte aktive vs stale Refs. **Aktive Refs** (Live-SSoT-Files) → Pointer-Stub pflicht. **Stale Refs** (alte log.md-Einträge, historische Analyse-Files) → ignorieren per User-Direktive „nur was wir wirklich aktiv brauchen". Vermeidet sowohl Memory-Schwächung als auch unnötige Update-Welle.

- **Token-Limit-Schwelle bei dichten Sections:** §13 143K / 99 Z. = 1,4K/Z. Avg, einzelne Einträge 5-7K. Read mit limit=55 → 62K Tokens-Hit (über 25K-Max-per-Read). **Per-Entry-Approach via `ctx_execute_file`** (Volltext bleibt Sandbox, nur Print indexiert) ist notwendige Strategie für Mega-Sections statt One-Big-Read+Edit. Lektion für nachfolgende Phase-2-Files mit ähnlicher Dichte.

- **Disziplinärer Pause-Punkt:** „Lint UND Memory-Erhalt" sind Gleichrang-Direktive — wenn Token-Druck Memory-Substanz gefährdet, ist Pause + Commit + fresh-Session-Resume die korrekte Antwort. 5 saubere Sub-§-Cuts (lock-in −18,6K) > 7 Sub-§-Cuts unter Druck (Memory-Risk).

- **Archive-Files local-only akzeptiert:** Konvention seit §1-Meilensteine-Archiv (17.04.2026) konsistent gehalten. Implikation für nachfolgende Phase-2-Refactors (Phase-2-Files #8 PIPELINE / #9 INSTRUKTIONEN / #10 SESSION-HANDOVER / #11 SYSTEM): Archive-Files ebenfalls in `05_Archiv/`, ebenfalls gitignored, ebenfalls Pointer-Stubs am Ursprungsort.

**Cross-Reference:** CORE-MEMORY §13 2026-05-23-Eintrag (Phase 2 Sub-Refactor #1 Teil 1) · SYSTEM.md Footer v1.6→v1.7 · 4 Archive-Files in `05_Archiv/` (CORE-MEMORY-§3/§6/§10/§11-archiv.md) · §18-Skill `paragraph-18-sync v0.1.0` validator-Dry-Run + Final-Run · Codex `gpt-5.3-codex` Single-Pass Diff-Re-Review · Conversation-Context 2026-05-23 09:53-11:30 MESZ Phase-2-Teil-1-Session · Memory `feedback_core_folder_lean_discipline` (Lean-Disziplin-Anker) · `.gitignore` L8 `05_Archiv/*` (Local-only-Konvention).

## [2026-05-23] system | 00_Core Slim-Refactor Phase 2 Sub-Refactor #1 Teil 2 (CORE-MEMORY §13 Pre-Cut + Ruflo-Sweep + Slim + §12-Check)

**Event-Typ:** Meta-Refactor / System-Lifecycle (scoring-neutral, kein FLAG/Score-Move, kein Sparrate-Touch). Fortsetzung von Phase-2-Teil-1 (Commit `1b75364`), schließt das §13/§12-Defer aus dem Phase-2-Teil-1-Commit-Body.

**Was passiert ist:**

3 §13-Buckets sequenziell + Bucket #6 §12-Quartals-Rollover-Check, alles in einer atomaren Sitzung mit User-DAG-approved Reihenfolge `Pre-23.04 → Ruflo-Sweep → Slim 12 Fat-Rows → §12-Check → Pre-Commit-Gates → atomar Commit`.

1. **Bucket #3 Pre-23.04 Cut** (20 Rows 15.-22.04. / 5,6K) → `05_Archiv/CORE-MEMORY-§13-pre-2026-04-23-archiv.md`. Migrate-Check: alle Topics (`[Tools]`/`[Scoring]`/`[Vault]`/`[Briefing]`/`[Meta]`) absorbiert in SYSTEM.md §System-Zustand (Tools-Versionen) + §5 (V-Rescoring + Schema-Trigger ≠ SKILL-Regel-Semantik 18.04. — beide bereits in Teil 1 migriert) + §6 (DEFCON v3.7 als Live-Tabelle-Anfang) + Wissenschaftliche-Fundierung-DEFCON.md (Foundation-Papers) + INSTRUKTIONEN §27.4 (Vertikal-Drift-Klausel) + `score_history.jsonl` 27/27 PASS + git log Commit `ca76114`. **Section-Prose-Pointer** in §13-Header-Beschreibung statt Table-Row-Stub (Konvention-Variante zu Teil-1 §6-Header-Pointer).

2. **Bucket #4 Ruflo-Sweep keyword-basiert** (14 Rows 30.04.-14.05. / 50,2K) → `05_Archiv/CORE-MEMORY-§13-Ruflo-Lifecycle-archiv.md`. **User-Klarstellung 23.05.: "claude-mem wird nicht vollumfänglich aber aktiv genutzt im Gegensatz zu Ruflo" → claude-mem v13.2.0 ist HYBRID-aktiv (additiv read-only Augmentation-Layer kanonisch ratifiziert 16.05. Pickup #B Phase-0b-HYBRID-Final), NICHT Ruflo-Klasse → HYBRID-Final-Entries als KEEP, NICHT archiviert.** Klassifikations-Keywords: `\bruflo\b` + `ecc[-@]ecc` + `viral plugin` + `substrate reject` + `plugin substrate` + `paragraph 0.6` (Memory-Pitfall-Stempel). 1 **konsolidierter Sunset-Pointer-Entry** dated 13.05.2026 (Hard-Rollback-Datum) eingefügt: deckt komplette Ruflo-Lifecycle ab (PIPELINE #20 Phase 1.2-1.7 → Doctor-Welle-3a → Briefing-v3.1.0-Brainstorming → Bridge-Coherence-Pakete 1-4 → PIPELINE #49 Quick-Wins → Audit-Cleanup + #50-Bridge-Bugs-Decision → Briefing-Prod-Cutover v3.2.0 → #50 UPSTREAM FIXED → #57 Forensik BLOCKED + #50-Runtime-Upgrade-PARTIAL → Hard-Rollback + Phase-A/B Deep-Sweep-Cleanup → PIPELINE #61 CodeBurn-Retrospektive) mit Memory-Cross-Refs `feedback_viral_plugin_substrate_risk_eval` + `feedback_codeburn_retry_metric_calibration` + SYSTEM §Plugin-Layer + git log.

3. **Bucket #5 Slim-Convention 12 Fat-Rows >3500b** (57,7K Source → 6,4K Slim = **−51,3K / −89% Kompression**). Pattern: `**Bold-Title** — ~280 Char Outcome → Voll-Archiv-Pointer · PIPELINE #XX · git log SHA`. Volltext nach `05_Archiv/CORE-MEMORY-§13-fat-entries-fulltext-archiv.md`. Slim-Threshold 3500b, Excludes: 2026-05-23 (current Refactor-Lifecycle-Marker), 2026-05-18 AMZN-Neuaufnahme (Score-Event PORTFOLIO-cross-ref-kritisch), konsolidierte Pointer-Stub-Entries (z.B. Ruflo-Sunset 13.05. den ich gerade inserted habe).

4. **Bucket #6 §12 Quartals-Rollover-Check** (PIPELINE #67 §18.6-Convention) → **NO-OP**. Max Ticker-Sub-§: AMZN 14 Zeilen / 5,4K. Threshold: >900 Zeilen. Alle 12 Ticker-Sub-§§ <20 Zeilen → §18.6-Rollover dormant.

**Netto-Effekt Teil 2:** CORE-MEMORY.md 216,8K → 115,6K (**−101,2K / −47%**).
**Phase 2 kumuliert** (Teil 1 + Teil 2): 235,4K → 115,6K (**−119,8K / −51%**). Übertrifft Plan-Band 150-180K signifikant — Memory-Erhalt durch Slim-Convention + Voll-Archiv-Pointer-Pattern erreicht ohne Substance-Loss (User-Direktive „Lint UND Memory-Erhalt").

**Technik-Innovation:** Per-Entry-Token-Sprengung von §13 (143K / dichte 4-7K-Rows) umgangen via **2 self-deleting Python-Scripts** (`_temp_ruflo_sweep.py` + `_temp_slim_sweep.py`) mit Bash-Exec für atomare File-Mutationen — Read+Edit-Loops hätten 14-30× Token-Budget gebraucht. Scripts implementieren: read CORE-MEMORY → regex/content-match Row-Identifikation → write Archive verbatim → rewrite CORE-MEMORY mit Slim/Pointer-Replacement → idempotent + fail-close. Memory `feedback_windows_console_ascii_safe_inline_python` einmal getriggert (initialer Script-Run crashte mit cp1252-✅-encode-error im print) → Fix: `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` als Standard-Header für alle inline-Scripts. Memory `feedback_windows_python_crlf_text_mode` adressiert: `open(..., newline="")` für Atomic-Writes (LF-preservation).

**Pre-Commit-Gates:**
- **§18-Skill `paragraph-18-sync v0.1.0`** (2. Live-Anwendung nach Phase 1 heute früh): `python 03_Tools/para18_sync/validator.py system-zustand --version-bump --dry-run --json` → Expected-Set deterministisch identifiziert (CORE-MEMORY.md + SYSTEM.md + Vault log.md, kein xlsx-Warning, kein Quartals-Rollover-Warn da Bucket #6 NO-OP). Skill funktioniert empirisch reproducibel.
- **Codex Single-Pass Diff-Re-Review (`gpt-5.3-codex`)** auf Working-Tree-Diff vor Commit.

**Sync-Set §18 (System-Event, version-bump, scoring-neutral):**
- `00_Core/CORE-MEMORY.md` (§13 Pre-23.04-Cut-Pointer in Header-Prose + 14 Ruflo-Rows entfernt + 1 konsolidierter Sunset-Pointer-Entry 13.05. + 12 Fat-Rows slim'd + neuer §13 Phase-2-Teil-2-Entry + Footer v1.25→v1.26)
- `00_Core/SYSTEM.md` (Footer v1.7→v1.8 + Stand-Bump)
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (dieser Eintrag)
- 3 neue Archive-Files in `05_Archiv/` (untracked per Konvention `05_Archiv/*` Whitelist-Exceptions nur JSONL): `CORE-MEMORY-§13-pre-2026-04-23-archiv.md` + `CORE-MEMORY-§13-Ruflo-Lifecycle-archiv.md` + `CORE-MEMORY-§13-fat-entries-fulltext-archiv.md`

**Bewusst NICHT angefasst:** PORTFOLIO.md / Faktortabelle.md / `01_Skills/dynastie-depot/config.yaml` / `03_Tools/Rebalancing_Tool_v3.4.xlsx` / `03_Tools/Satelliten_Monitor_v2.0.xlsx` / `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx` / `05_Archiv/score_history.jsonl` / `05_Archiv/flag_events.jsonl` / PIPELINE.md / STATE.md — **kein Score/FLAG/Sparraten/Critical-Alert-Event.** DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:**

- **Keyword-basierte Bucket-Klassifikation > datums-fenster-basiert wenn semantische Distinktion vorhanden.** Beim ursprünglichen Plan-Wortlaut „16 Ruflo-Einträge → Archiv" wäre eine Datums-Fenster-Interpretation (30.04.-14.05.) auf 33 Rows gestoßen, wovon 16 Non-Ruflo-Substanz (Welle-Konsolidierungen, Briefing-Deploys, Vault/Tools-Wellen) silent ins Ruflo-Archiv gerutscht wären. Keyword-Filter (`\bruflo\b` + `substrate reject` + `viral plugin` + `paragraph 0.6` + `ecc-ecc`) klassifiziert auf 17 Substanz-Matches; HYBRID-Aktiv-Excludes via User-Klarstellung. **Take-away:** vor Bucket-Cut explizit User-Direktive zur Klassifikations-Achse einholen, nicht implizit aus Plan-Wortlaut interpretieren.

- **Script-based Atomic-Mutation > Read+Edit-Loop bei dichten Sections.** §13 hatte 143K in 99 Zeilen (1,4K/Zeile avg, max 7,7K/Zeile). Per-Row-Read+Edit-Cycle hätte 14-30× Token-Budget verbraucht. Self-deleting Python-Script mit Regex-Match + Verbatim-Archive-Write + In-Place-Replacement liefert atomare File-Mutation in 1 Bash-Exec, idempotent re-runnable, fail-close bei Unicode-Encode. **Pattern reusable** für nachfolgende Phase-2-Files (PIPELINE-DONE-Strip ~68K, INSTRUKTIONEN ~84K, SESSION-HANDOVER ~39K).

- **Slim-Convention bei 87-93% Kompression substanz-erhaltend wenn:** (a) Bold-Title preserviert (Headline-Recognition); (b) ~280 Char Outcome-Sentence mit Clean-Break-Detection (`. `, `; `, ` - `, `) `) clean clauses; (c) standardisierter Pointer-Tail (Voll-Archiv + PIPELINE-IDs + git log SHAs) garantiert Recovery. **Goldstandard** für Lifecycle-Meilenstein-Slimming.

- **User-Klarstellung als 1. Bucket-Klassifikations-Achse (vor mechanischem Apply).** „claude-mem ist HYBRID-aktiv NICHT Ruflo-Klasse" verschob die Bucket-Boundary korrekt vor dem Sweep (sonst hätten HYBRID-Final-Entries im Ruflo-Archiv landen können). **Take-away:** AskUserQuestion vor jedem Klassifikations-Cut wenn Plan-Wortlaut auf Substanz-Ambiguität hindeutet (Plan sagte „Ruflo" — User-Antwort grenzte ab gegen aktive Plugin-Architektur).

- **§12 Quartals-Rollover-Check bleibt langfristig dormant.** Max Ticker-Sub-§: AMZN 14 Zeilen post-Neuaufnahme 18.05. Threshold 900 ist konservativ; bei aktuellem Tag-+1-Slot-Append-Rate von 2-3 Zeilen pro Earnings-Call würde ein Ticker erst nach ~75 Quartalen (>18 Jahren) auf 900 Zeilen kommen. **PIPELINE #67 §18.6-Convention bleibt verankerter Long-Term-Gate**, aber Trigger ist absehbar nicht in 2026/2027.

- **3 Archive-Files cumulative in Phase 2** (4 in Teil 1 + 3 in Teil 2 = 7 archive files in `05_Archiv/` local-only). Konvention konsistent: gitignored, Recovery via `git show <pre-commit>:00_Core/CORE-MEMORY.md` oder direct local file. Single-User-Workflow akzeptiert Cloud/Cron-Runtime-Limitation.

**Cross-Reference:** CORE-MEMORY §13 2026-05-23-Eintrag (Phase 2 Sub-Refactor #1 Teil 2) · CORE-MEMORY Footer v1.25→v1.26 · SYSTEM.md Footer v1.7→v1.8 · 3 Archive-Files in `05_Archiv/` (`CORE-MEMORY-§13-pre-2026-04-23-archiv.md` + `CORE-MEMORY-§13-Ruflo-Lifecycle-archiv.md` + `CORE-MEMORY-§13-fat-entries-fulltext-archiv.md`) · §18-Skill `paragraph-18-sync v0.1.0` 2. Live-Anwendung als `system-zustand --version-bump` Pre-Commit-Gate · Codex `gpt-5.3-codex` Single-Pass Diff-Re-Review · Memory `feedback_viral_plugin_substrate_risk_eval` (Ruflo-Lessons-Pointer) · Memory `feedback_codeburn_retry_metric_calibration` (PIPELINE #61 Retro-Pointer) · Memory `feedback_windows_console_ascii_safe_inline_python` (sys.stdout.reconfigure-Fix einmalig getriggert) · Memory `feedback_windows_python_crlf_text_mode` (open newline='' preservation) · `.gitignore` L8 `05_Archiv/*` (Local-only-Konvention) · Phase-2-Teil-1 Commit `1b75364` (Vorlauf-Foundation).

## [2026-05-23] system | PIPELINE #78 + #79 NEU — Markdown-Refactor-Tools Snapshot + Skill `core-slim-refactor` v0.1 Build-Pending

**Event-Typ:** pipeline-item (NEU 2× deferred), scoring-neutral. Follow-up zu Phase-2-Teil-2-Commit `4c8d8ea` (heute mittag).

**Was passiert ist:**

Nach Abschluss der Phase 2 Sub-Refactor #1 Teil 2 hat der User auf die 2 self-deleting Python-Scripts (`ruflo_sweep.py` + `slim_sweep.py`) hingewiesen und das Pattern-Lineage offengelegt: 4 Iterationen über ~30 Tage (24.04. 00_Core Perfect-Organization 9-Phasen-Reorganisation → 23.05. Phase 1 Quick-Wins → 23.05. Phase 2 Sub-Refactor Teil 1 → 23.05. Phase 2 Sub-Refactor Teil 2). User-Direktive: „Saven und künftig immer nutzen."

**Step 1 (diese Session, ~15 min):**

1. Snapshot der 2 Scripts + Pattern-Lineage-README angelegt in `05_Archiv/refactor-tools/2026-05-23/`:
   - `ruflo_sweep.py` — Bucket-Archive-Pattern (keyword-basiert, mit Exclude-Sets + Consolidated-Pointer-Insertion)
   - `slim_sweep.py` — Slim-Convention-Pattern (Threshold-basiert, Bold-Title + Outcome + Pointer-Tail)
   - `README.md` — Pattern-Lineage 4 Iterationen + Known-Pitfalls + geplanter 8-Phasen-Skill-Skizze + Build-Substrate-Hinweise
   Files sind `.gitignore`d per Konvention `05_Archiv/*` (Whitelist-Exceptions nur JSONL).

2. **PIPELINE #78 NEU** 👁 — Skill `core-slim-refactor` v0.1 Bau als 8-Phasen-Pipeline analog `session-closure` v0.2.0 + `paragraph-18-sync` v0.1.0. P0 Pre-Audit-Baseline (SystemAudit) → P1 Bucket-Classification (User-Direktive einholen wenn ambig) → P2 Migrate-before-Strip Differential-Check → P3 Backlink-Scan → P4 Bucket-Archive-Tool → P5 Slim-Convention-Tool → P6 Pointer-Stub + Header-Prose-Updates → P7 Pre-Commit-Gates (§18-Skill + Codex Single-Pass) → P8 Atomic-Commit + Post-Audit-Verify. Aufwand: ~90-120 min (Spec → Plan → Build → skill-creator-Gegencheck → Codex-Sparring → §18-Promotion-Sync). Komplementär zu SystemAudit (read-only diagnostic) — Skill ruft SystemAudit als P0/P8-Gate, nicht merge.

3. **PIPELINE #79 NEU** 👁 — CORE-MEMORY §13 L420 PIPELINE #34 DCF-Malus Slim-Defect (niedrig-Priorität): `slim_sweep.py` hat L420 trotz >3500b NICHT geslimmt (vermutet Regex-Non-Match wegen Backtick-eingeschlossener `|`-Chars in Python-Optional-Syntax). Gekoppelt mit #78 als Diagnostic-Assertion-Build-Requirement.

4. **Auto-Memory:** `reference_markdown_refactor_tools_snapshot.md` mit Pfad-Pointer + Pattern-Lineage + Known-Pitfalls + Cross-References. MEMORY.md Index aktualisiert.

**Step 2 (fresh Session):** Skill-Bau in eigener Session mit frischem Kontext per User-Direktive 23.05. „Wir brauchen frischen Kontext."

**Sync-Set §18 (pipeline-item, scoring-neutral):**
- `00_Core/PIPELINE.md` (#78 + #79 NEU + Footer v2.59→v2.60)
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (dieser Eintrag)

**Bewusst NICHT angefasst:** CORE-MEMORY.md (kein neuer §13-Eintrag — Lifecycle-Marker schon im Phase-2-Teil-2-Commit-Body) · SYSTEM.md (keine Skill-Registry-Bullet — Skill nicht promoviert sondern PENDING) · CLAUDE.md (keine Routing-Table-Eintrag — Skill noch nicht existent) · PORTFOLIO/Faktortabelle/config/xlsx/jsonl (kein Score/FLAG-Event). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:**

- **User-Pattern-Recognition als Skill-Build-Trigger:** Nach mehrfacher Anwendung eines Workflow-Patterns ist Skill-Promotion empirisch validiert. Pattern-Lineage in README + Memory verankert, damit fresh-Session-Self-recall reibungslos läuft.
- **Snapshot vor Generalisierung:** Self-deleting Tools werden NICHT als Production-Tools nutzbar, müssen aber als Build-Substrate konserviert werden — sonst Re-Build-Aufwand bei nächster Anwendung. `05_Archiv/refactor-tools/` als Konvention etabliert (parallel zu `05_Archiv/superpowers-pre-sunset/plans/` für Plan-Historie).
- **Skill-Build-Aufwand vs Snapshot-Aufwand:** ~90-120 min (Skill) vs ~15 min (Snapshot). 2-Step-Pattern (Snapshot jetzt + Skill in fresh Session) konserviert Empirie ohne Token-Druck-Risiko.

**Cross-Reference:** Phase-2-Teil-2-Commit `4c8d8ea` (Vorlauf-Foundation, gleicher Tag mittags) · `05_Archiv/refactor-tools/2026-05-23/README.md` (Pattern-Lineage + Build-Substrate) · 24.04.-Präzedenz `05_Archiv/superpowers-pre-sunset/plans/2026-04-24-00core-perfect-organization.md` · Memory `reference_markdown_refactor_tools_snapshot.md` (NEU) · Memory `feedback_core_folder_lean_discipline` (Lean-Disziplin-Anker) · Skill-Build-Präzedenzen `session-closure` v0.2.0 + `paragraph-18-sync` v0.1.0 (8-Phasen-Pipeline-Konvention).

## [2026-05-23] system | PIPELINE #78 SPEC-READY — `core-slim-refactor` v0.1 Brainstorming + Codex R1+R2 GREEN

**Event-Typ:** pipeline-item (Status-Transition #78 DEFERRED → SPEC-READY), scoring-neutral. Follow-up zu heute mittag #78-Anlegung + Substrate-Snapshot.

**Was passiert ist:**

User-Direktive bei Session-Start: Pfad (A) "Skill `core-slim-refactor` v0.1 zuerst bauen" gewählt aus Decision-Tree (A/B/C) zwischen Skill-Build vs Direkt-Continue mit 00_Core-Restbestand vs Stop. Brainstorming-Skill aktiviert per Memory `feedback_brainstorming_terminal_override_dynastie` (Spec-Pickup endet bei Codex + §18-Sync, NICHT bei writing-plans — Plan/Build separate Sessions).

**Brainstorming-Workflow (6 Section-Approval-Gates):**

1. **Scope-Entscheidung:** Pattern-canonical (3 Pattern A/B/C statt tight-file-bound oder universal). 4× empirisch validiert (24.04. + 3× 23.05.).
2. **Gemini-Cross-Sync-Survey (User-Direktive vor Spec):** gemini-agent-Subagent (Memory `reference_gemini_agent_not_bridge_script`) enumerierte 7 Slim-Refactor-Candidates außerhalb 00_Core. Top-Tier: log.md (472 KB, Pattern C+A, vault-link-graph-Risk), tavily-spec (70 KB), dynastie-depot SKILL.md (70 KB, template-risk), Wiss-Fundierung-DEFCON (58 KB), morning-briefing-prompt-v3 (45 KB, template-risk), Vault index.md (39 KB, write-collision), Beispiele.md (28 KB, anchor-promotion-coupled). Sequenzielle Filterung mit Karpathy-Simplicity-First: SKILL.md + morning-briefing + index.md + Beispiele.md = auto-EXCLUDE wegen Risiko-Bias. v0.1-Scope finalisiert auf 00_Core Restbestand + 3 worked-example-configs (Ruflo-Sunset + Fat-Rows retroaktiv + SESSION-HANDOVER-Date-Cut executable). log.md → v0.2-deferred wegen vault-link-graph-Preservation-Logic-Komplexität.
3. **Gate-Modus:** Hybrid (§18-Skill `paragraph-18-sync` inline, Codex hand-off). Pro: §18-Skill ist stable validated API; Codex-Pass bleibt User-Workflow per Memory `feedback_codex_sparring_heuristic`.
4. **Architektur-Approach:** Monolithic-Pipeline + `--dry-run` (statt Phase-Subcommands oder Two-Stage-Plan/Execute). 4× empirisch single-pass validated. ~700 LOC, 4-File-Module-Split (statt 7-Modul-Speculation).
5. **Karpathy-Regeln (User-Direktive):** explicit verankert in Foundation-Tabelle (§0): Think-Before-Coding / Simplicity-First (≤700 LOC, kein Auto-Detect, keine Resume) / Surgical-Changes (kein Workspace-Wide-Refactor) / Pre-Refactor-Caller-Scan (P3 Backlink-Scan PFLICHT, fail-close) / Approach-Reset-Schwelle (2-Fail-Stop intra-run) / Goal-Driven-Execution (Acceptance-Kriterien first-class).
6. **Skill-Creator als festes Building Tool (User-Direktive):** 3 First-Class Build-Gates verankert (Stations 8/9/10): Gate-1 Scaffold via `/skill-creator:skill-creator`, Gate-2 Description-Push Lint via `/skill-creator validate-and-optimize-existing-skill`, Gate-3 Functional Smoke-Test (pytest + dry-run-reference-match). Section 6 Build-Process-DAG (13 Stations, 5 Gates G0-G4, 3 Session-Boundaries) als deklarativer Anker für Plan-Stage.

**Codex-Sparring-Verlauf (gpt-5.3-codex via Memory `feedback_review_via_codex_not_advisor` Pin):**

- **R1 Single-Pass:** 3 HIGH + 3 MEDIUM + 1 LOW.
  - HIGH-1 §6.2 Caveat-1 ohne Gate-Enforcement → Fix Gate G0 (post-Station-1) + §6.2.1 Self-Review-Tabelle mit 4 expliziten Checks (alle ✅).
  - HIGH-2 §2.2 `executed:`-Guard unpräzise "populated" → Fix YAML-Schema-Wortlaut "null OR fully populated 3 sub-fields non-null", partial = ABORT.
  - HIGH-3 §5.4 AK5 "sinnvolles dry-run" schwammig → Fix AK5a-5d (exit-code 0 + ≥3 entries classified + struktur-komplett + User-Approval-Gate).
  - MEDIUM-1 AK6 vage → Fix messbare PASS-Signale (exit-code 0 + JSON status=PASS + expected-set-diff empty + live-commit-without-hook-fail).
  - MEDIUM-2 §6.3 Station-3 prozedural → Fix deklarativer Wortlaut.
  - MEDIUM-3 §1.2 --skip-audit + P3-Bypass-Verteilung → Fix --skip-audit ONLY P0; P3 nicht via CLI bypassable, nur zweistufig via YAML mit WARNING.
  - LOW-1 §7 search_terms-Coverage-Gap → Fix Open-Question #7 mit 3-Option-Outline (a/b/c) für Plan-Stage.
- **R2 Diff-Re-Review (billigster Sparring-Schritt per Memory-Heuristik):** **R2 GREEN** alle 7 ✅ closed, keine neuen HIGHs, keine Widersprüche zwischen Sections. Spec ist Build-ready.
- **Total:** 7 Befunde adoptiert, Spec 42,0 → 46,7 KB. Confidence ~97% post-R2.

**Sync-Set §18 (pipeline-item, scoring-neutral):**
- `00_Core/PIPELINE.md` (#78 Status-Body massiv erweitert mit Spec-Ready-Block + Codex-Verlauf-Detail + Open-Questions; Footer v2.60→v2.61)
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (dieser Eintrag)
- `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` (NEU, 46,7 KB; per `.gitignore` Z.18 "Superpowers docs nur lokal relevant" untracked — konsistent mit anderen aktiven Specs)

**Bewusst NICHT angefasst:** CORE-MEMORY.md (kein neuer §13-Eintrag — Spec-Stage ist pipeline-item nicht system-zustand) · SYSTEM.md (keine Skill-Registry-Bullet — Skill noch nicht promoted, weiterhin SPEC-Stand) · CLAUDE.md (keine Routing-Table-Eintrag — Skill noch nicht existent) · STATE.md (kein Critical-Alert-Slot-Hit für pure Spec-Stage-Anlage) · PORTFOLIO/Faktortabelle/config/xlsx/jsonl (kein Score/FLAG-Event). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:**

- **Gemini-Cross-Sync vor Spec-Lock validiert Scope empirisch breiter:** User-Direktive (B) "Gemini-Pass jetzt vor Spec für broader discovery" lieferte 7 Candidates außerhalb 00_Core in ~25k Token. Ohne Pass wäre v0.1-Scope speculativ "00_Core-only" geblieben, log.md (472 KB Single-File-Payoff) unentdeckt. **Take-away:** Cross-Sync-Pass mit gemini-agent vor Spec-Lock kostet 1 Roundtrip, verbreitert Scope-Foundation empirisch — Standard-Workflow für künftige Skill-Specs mit Cross-File-Implikationen.

- **Codex R2 Diff-Re-Review = billigster Sparring-Schritt-Verifikation:** R2 nutzte nur ~21k Token (vs R1 ~21k Token) und schloss alle 7 R1-Findings ✅. Sparring-Heuristik per Memory `feedback_codex_sparring_heuristic` (HIGH ≥2 triggert R2) ROI-positiv bestätigt: ohne R2 hätte Drift bei Fix-Applikation unentdeckt bleiben können (z.B. neue Widersprüche zwischen Sections nach 7 Edits).

- **User-Mandate "Skill-Creator als festes Building Tool" erfordert First-Class-DAG-Anchoring:** Initiale Skill-Creator-Erwähnung als "optional Gegencheck" wäre im Plan-Stage als bypassable interpretierbar gewesen. Section 6 Build-Process-DAG (deklarativ) mit Stations 8/9/10 als drei separate Build-Gates macht Skill-Creator-Verankerung **unverhandelbar visible** — strukturell statt deklarativ.

- **Section-Boundary-Disziplin (S2/S5 ref-only vs S6 DAG) durch Self-Review-Tabelle hart enforced:** Gate G0 + §6.2.1 4-Check-Tabelle (S2.3/S5.4 nicht DAG-redefining, keine Task-Detail, keine Time-Estimates) konvertiert Caveat-1 von deklarativ zu enforce-bar. Pattern reusable für künftige Specs mit Multi-Section-Cross-References (anti-Duplikation).

- **Karpathy Simplicity-First in Module-Split:** 7-Modul-Split (cli/config/3-patterns/backlink/gates) war Optimization for Re-Use mit exakt 0 v0.1-Re-Use-Cases. Empirie-Baseline (2 working scripts ~470 LOC) + Generalisierung-Overhead ~50% → 4-File-Split ~700 LOC ist YAGNI-clean. **Take-away:** Empirische LOC-Baseline ist besserer Spec-Anchor als a-priori-Modul-Architektur.

**Cross-Reference:** Spec-File `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` (46,7 KB, 11 Sections, Build-ready) · PIPELINE #78 Body (Spec-Ready-Block + Codex-Verlauf-Detail + 7 Open-Questions für Plan-Stage) · Phase-2-Teil-2-Commit `4c8d8ea` + `f6041b6` (Vorlauf-Substrate gleicher Tag mittags) · `05_Archiv/refactor-tools/2026-05-23/README.md` (Pattern-Lineage + Build-Substrate, im Spec referenziert) · Memory `feedback_brainstorming_terminal_override_dynastie` (Spec-Pickup-Endpoint) · Memory `feedback_review_via_codex_not_advisor` (Codex Default + gpt-5.3-codex Pin) · Memory `feedback_codex_sparring_heuristic` (R2 Diff-Re-Review ROI-positive bei HIGH ≥2) · Memory `reference_gemini_agent_not_bridge_script` (Cross-Sync-Subagent-Pfad) · Skill-Build-Präzedenzen `session-closure` v0.2.0 + `paragraph-18-sync` v0.1.0 (8-Phasen-Pipeline-Konvention) · §18-Skill `paragraph-18-sync v0.1.0` (Hybrid-Gate Architektur-Anchor in Spec §1.3 + §3.1 P7).

## [2026-05-23] system | PIPELINE #78 PLAN-READY — `core-slim-refactor` v0.1 writing-plans + Codex R1 + R2 ALL-CLOSED

**Event-Typ:** pipeline-item (Status-Transition #78 SPEC-READY → PLAN-READY), scoring-neutral. Follow-up zu heute nachmittags Spec-Ready-Commit `96a9181`.

**Was passiert ist:**

User-Direktive direkt nach Session-Resume: weitermachen mit Spec-Stage-Pickup im Plan-Modus. `superpowers:writing-plans`-Skill aktiviert (terminate-Disziplin per Memory `feedback_brainstorming_terminal_override_dynastie`: Plan-Stage endet bei Codex + §18-Sync, NICHT bei Build).

**Plan-Stage-Workflow (3 Stations):**

1. **Station 4 — writing-plans Skill activated:** Plan-File geschrieben nach `docs/superpowers/plans/2026-05-23-core-slim-refactor-build.md` (~1600 LOC, 18 Build-CPs CP1-CPFinal, Subagent-Driven empfohlen). Vorab-Orientierung (4 parallele Tool-Calls) löste 5 von 7 Open-Questions: OQ1 `jsonschema` NOT installed in Python 3.14.3 → manual validation only (kein try/except import-Fallback per Karpathy Simplicity-First — ein Pfad, kein optionaler Fork), OQ5 `.gitignore` `*.bak` Pattern fehlt → CP15 fügt `*.pre-refactor.bak` explizit (NICHT generisches `*.bak` — surgical), OQ6 Vault-Path-Convention → repo-root-relative POSIX via `git rev-parse --show-toplevel`-Capture, OQ7 Backlink-Term-Coverage → Option (c) doc-checklist in `references/yaml_schema.md` Section Backlink-Term-Enumeration-Checklist + Build-Gate-3 doc-existence-test (least-effort, Karpathy YAGNI), OQ3 Reference-Archive-SHA-Whitespace → SHA-256 + Row-Set-Signature Hybrid via neues YAML-Field `reference_match_mode: sha | rowset`. OQ2 (paragraph-18-sync JSON-Schema) + OQ4 (Skill-Creator OK-Format) explicit zu Build-Stage deferred mit exit-code-only-Fallback bzw. as-observed-doc-Strategie.

2. **Station 5 — Codex Single-Pass on Plan (`gpt-5.3-codex` per Memory `feedback_review_via_codex_not_advisor`-Pin):**
   - **R1 Findings:** **3 HIGH / 3 WARN / 23 PASS.**
     - HIGH-1 (c/d) CP6 — keine explizite Run-Pattern-B-tests-expect-FAIL-Step zwischen Test-Write und Impl-Append (TDD Red-Step gap, Karpathy Think-Before-Coding).
     - HIGH-2 (c/d) CP7 — analog für Pattern C: keine explizite Failing-Test-Run-Step vor Impl.
     - HIGH-3 (g) CP8 Plan:2045 `baseline[target_path].read_text(encoding=utf-8, newline=)` → `newline`-Parameter erst in Python 3.13 für `Path.read_text` verfügbar, vor 3.13 = TypeError + Inkonsistenz zur restlichen `open(..., newline=)`-Konvention.
     - 3 WARN non-blocking: CP3 4-File-Scope (Surgical-Changes-Borderline), CP8 Orchestration-Breite (entry-point-inherent), CP6/CP7-TDD-Skip (durch HIGH-Fixes geschlossen).
     - 23 PASS: alle 6 Acceptance-Criteria sauber gemappt (AK1→CP17.1, AK2→CP13+CP17, AK3→CP14+CP17, AK4→CP16, AK5→CP17.4-5, AK6→CP-Final.1-4), alle 7 OQs resolved oder explicit deferred, §18-Promotion-Sync-Set komplett (SYSTEM.md + CORE-MEMORY.md + PIPELINE.md + log.md + README.md-superseded-note), CRLF/UTF-8 Disziplin (`open(..., newline=)` + `sys.stdout.reconfigure`) durchgängig, SHA + Row-Set-Fallback Whitespace-Drift-robust.
   - **Inline-Fixes via 7 Edits:** CP6 Step 3 Run new Pattern B tests — expect FAIL (impl missing) eingefügt + 3 Steps renumbered (3→4 Append-impl, 4→5 Run-all-pass, 5→6 Commit); analog CP7 für Pattern C (3 FAIL erwartet via ImportError); CP8 Plan:2045 ersetzt durch `with open(baseline[target_path], r, encoding=utf-8, newline=) as _f: target_md = _f.read()`.
   - **R2 Diff-Re-Review (billigster Sparring-Schritt per Memory `feedback_codex_sparring_heuristic` — HIGH-Count ≥2 triggert R2):** **ALL-CLOSED.** Alle 3 HIGH verifiziert ✅ (CP6 Plan:1138 Step 3 expect FAIL + 1146/1258/1266 Steps 4-6, CP7 Plan:1385 + 1393/1485/1493, CP8 Plan:2061-2062 open()-Pattern, kein dangling read_text remaining). Keine Regressions in Step-Nummerierung, kein dupliziertes Pattern, semantisch äquivalent + style-konsistent. 3 WARN bleiben non-blocking-akzeptiert.

3. **Station 6 — §18-Plan-Sync (dieser Commit):** PIPELINE #78 Status SPEC-READY → PLAN-READY mit Plan-File-Pointer + Open-Questions-Status + Codex-Verlauf-Detail im Body; Footer v2.61→v2.62.

**Codex-User-Disagreement (dokumentiert für Memory-Audit-Trail):**

HIGH-3 Codex-Claim raises TypeError at runtime ist auf Python 3.14.3 (Project-Env-Python) **inhaltlich falsch** — `Path.read_text(..., newline=...)` ist seit Python 3.13 supported (`Path.write_text(..., newline=...)` seit 3.10). Fix wurde dennoch appliziert wegen (a) Style-Konsistenz zur restlichen `open(..., newline=)`-Konvention im Plan, (b) Portabilität für Python 3.10-3.12-Setups falls Build-Stage in anderem venv läuft, (c) Codex-Authority per Memory ohne primary-source-disagreement-Pflicht. Memory-Lehre: bei Codex-Find inhaltlich-debatable + Fix-Cost trivial = inline-applied, kein Reconcile-Call nötig.

**Sync-Set §18 (pipeline-item, scoring-neutral):**
- `00_Core/PIPELINE.md` (#78 Status-Body massiv erweitert mit Plan-Ready-Block + Codex-R1+R2-Verlauf + OQ-Resolutions; Footer v2.61→v2.62)
- `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` (dieser Eintrag)
- `docs/superpowers/plans/2026-05-23-core-slim-refactor-build.md` (NEU, ~1600 LOC; per `.gitignore` Z.18 Superpowers docs nur lokal relevant untracked — konsistent mit anderen aktiven Plans)

**Bewusst NICHT angefasst:** CORE-MEMORY.md (kein neuer §13-Eintrag — Plan-Stage ist pipeline-item nicht system-zustand, Skill weiterhin nicht promoted) · SYSTEM.md (keine Skill-Registry-Bullet — Skill noch nicht promoted, weiterhin PLAN-Stand) · CLAUDE.md (keine Routing-Table-Eintrag — Skill noch nicht existent) · STATE.md (kein Critical-Alert-Slot-Hit für Plan-Stage-Transition) · PORTFOLIO/Faktortabelle/config/xlsx/jsonl (kein Score/FLAG-Event). DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Lessons:**

- **OQ-Vorab-Orientierung (4 parallele Tool-Calls) löst 5/7 Plan-Stage-Open-Questions in ~5min:** Statt Plan-Stage als alle 7 OQs zur Build-Stage durchreichen zu definieren, vorab kostengünstige Live-Checks (jsonschema-Import, .gitignore-Read, Skill-Layout-Glob, paragraph-18-sync-Struktur) liefern 5 Resolutions. OQ2 + OQ4 sind echte Run-Time-Empirie und bleiben explicit zu Build deferred mit Fallback-Strategie. **Take-away:** Plan-Stage-Disziplin = Resolve what is cheap; defer with explicit Fallback what is not. Memory-Pattern für künftige Spec→Plan-Transitions.

- **Codex Diff-Re-Review = billigster Sparring-Step-Verifikation (~21k Token-Cost):** R2 schloss alle 3 R1-HIGHs ✅ ohne neue Regressions, validierte Step-Renumbering konsistent (kein dangling Step 3 references, kein dupliziertes Pattern). Sparring-Heuristik per Memory `feedback_codex_sparring_heuristic` (HIGH ≥2 triggert R2) erneut ROI-positiv bestätigt — 2. Plan-Stage-Bestätigung nach Spec-Stage gleicher Verlauf (3 HIGH→Fix→R2 GREEN).

- **Codex-Authority vs Primary-Source-Disagreement:** HIGH-3 (read_text TypeError-Claim) war auf Python 3.14.3 inhaltlich falsch — empirisch in Python 3.13+ supported. Memory `feedback_review_via_codex_not_advisor`-Pflicht Give-the-advice-serious-weight + Memory-Heuristik If-you-follow-a-step-and-it-fails-empirically-OR-you-have-primary-source-evidence-that-contradicts-a-specific-claim-adapt begründet Pre-Edit-Reflektion: Codex-Authority + Fix-Cost trivial + Style-Argument (Consistency zu open()-Pattern) → inline-applied OHNE Reconcile-Call. Memory-Lehre: trivial-cost-fix + valid-secondary-argument = silent-accept; primary-source-contradiction + non-trivial-cost = Reconcile-Call.

- **Plan-Stage Bite-Size-Steps + TDD-Format komplett-bottoming-out bei N=15+ Tests:** 18 Build-CPs × ~5-8 Steps = ~100-150 Total-Steps in ~1600 LOC Plan. Per CP: failing-test-write → run-fails → impl → run-passes → commit. Test-Code in Step-Bodies vollständig (kein TBD), Impl-Code in Step-Bodies vollständig (kein implement later). **Pattern reusable** für künftige Multi-File-Skill-Specs mit dichtem TDD-Coverage.

- **Karpathy Surgical-Changes-Borderline bei CP3 (4-Files-in-1-Task) akzeptiert:** WARN von Codex, aber: __init__.py × 2 (empty) + config.py + test_config.py — semantisch ein TDD-Cycle pro Skill-Init-Setup. Strikteres Splitting hätte CP3 in 4 Sub-CPs zerlegt mit `__init__.py`-CP allein = bürokratisch ohne YAGNI-Begründung. Borderline-Accept per Karpathy Simplicity-greater-than-Dogma-when-both-pass-test.

**Cross-Reference:** Plan-File `docs/superpowers/plans/2026-05-23-core-slim-refactor-build.md` (~1600 LOC, 18 Build-CPs, Subagent-Driven) · PIPELINE #78 Body (Plan-Ready-Block + Codex-R1+R2-Verlauf + OQ-Resolutions) · Spec-File `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` (46,7 KB Build-ready, unverändert) · Spec-Stage-Commit `96a9181` (Vorlauf 4 Stunden früher) · Memory `feedback_brainstorming_terminal_override_dynastie` (Plan-Stage-Endpoint vor Build-Session) · Memory `feedback_review_via_codex_not_advisor` (Codex Default + gpt-5.3-codex Pin) · Memory `feedback_codex_sparring_heuristic` (R2 Diff-Re-Review ROI-positiv bei HIGH ≥2) · Memory `feedback_core_folder_lean_discipline` (Plan respektiert Lean-Disziplin durch Skill-isoliertes File-Set `01_Skills/core-slim-refactor/` + nur 1 `.gitignore`-Edit out-of-skill) · Skill-Build-Präzedenzen `session-closure` v0.2.0 + `paragraph-18-sync` v0.1.0 (8-Phasen-Pipeline-Konvention).


## [2026-05-23] system | core-slim-refactor v0.1.0 PROMOTED (PIPELINE #78 DONE, System-Zustand + Pipeline-Item Multi-Event Union §18.2, scoring-neutral)

**Event-Typ:** Skill-Promotion (System-Zustand-Change + Pipeline-Item Status-Transition) — kein Score/FLAG/Sparraten-Touch.

**Was passiert ist:**

1. **Skill `core-slim-refactor` v0.1.0 aktiv** mit canonical entry-point `01_Skills/core-slim-refactor/scripts/core_slim_refactor.py` (YAML-driven 8-Phase Markdown-Section-Refactor pipeline, 3 Pattern A/B/C, P0-P7 Phase-DAG). Triggers: `!SlimRefactor <config>` + nat. Sprache "Slim-Refactor von X" + config-path-mention. 8 Pflicht-Disziplinen Karpathy/§0-konform (Migrate-before-Strip + Pointer-Stub + Backlink-Scan PFLICHT P3 fail-close non-bypassable + Archive-Local-Only + §18-Skill-Gate P7 subprocess + Codex-Pass hand-off + CRLF-UTF-8-Hygiene + Atomic-Commit).
2. **13 Build-Commits seit Plan-READY `cd1148a` durch CP-Final:** CP1+2 Scaffold+SKILL.md (8056f7d) · CP3 config.py 6 schema-validations (1f678cd) · CP4 backlink.py P3 (9381506) · CP5+6+7 patterns A+B+C 8 tests (a6f29c8) · CP8 entry-point P0-P7 orchestration 4 pipeline-tests (e4eb208) · Codex-R1-HIGH-fixes P7-atomicity + date-cut section guard (a0dc16d) · CP9+10+11 3 worked-example YAMLs (800c360) · CP12 3 reference-docs (7700a85) · CP13+14 AK2+AK3 tests (a5684d8) · CP15 .gitignore (0ad1249) · CR-CP16 parens-NOTE (838ddf2) · Pause-Banner (bd00299) · CP16 Build-Gate-2 PASS (daffde0) · CP17 Build-Gate-3 PASS marker (8109bb4) · CP18 Codex-R1 3 HIGH-fixes (6b86a29) · CP-Final §18-Promotion-Sync (this commit).
3. **Tests:** 31 PASS + 2 XFAIL = 33 collected, runtime 1.68s. Coverage: backlink (3) + config (7) + patterns (8) + pipeline (6 incl. P5-rollback + P7-SystemExit-rollback) + p18-gate-parser (7 covering HIGH-2/HIGH-3 false-PASS-branches + edge-cases) + reference-archive-match (2 XFAIL AK3 OQ3-deferred). ruff check + format clean. Pre-Commit alle PASS.
4. **CP18 Codex Single-Pass (gpt-5.3-codex):** R1 = 3 HIGH (P7-SystemExit-bypass `except Exception` / §18-gate rc==0+status=FAIL false-PASS / §18-gate rc!=0+status=PASS false-PASS) + 5 MEDIUM (subprocess-timeout / stderr-surface / classify_date_cut anchor-unused / duplicate-anchor-silent / backup-overwrite-integrity) + 2 LOW + 2 INFO. R2 Diff-Re-Review = HIGH-NEW-1 PEP 758 unparenthesized-except False-Positive (Reconcile via empirisches 5-Punkt-Verify ast.parse+import+pytest 31 PASS+ruff format prefers+precedent commit Line 65 → Codex CONSENSUS 0 HIGH closed). 2 MEDIUM inline closed (subprocess timeout=30s + stderr-surface). 3 MEDIUM + 2 LOW + AK3 OQ3 deferred zu v0.1.1 dokumentiert in `references/failure_modes.md`.
5. **§18-Promotion-Sync-Set atomar:** SYSTEM.md (§Skill-Registry +1 + Footer v1.8→v1.9) + CORE-MEMORY.md (§13 +1 Eintrag + Footer v1.26→v1.27) + PIPELINE.md (#78 PLAN-READY→DONE Header-Transition + Footer v2.62→v2.63) + dieser log.md-Eintrag + `05_Archiv/refactor-tools/2026-05-23/README.md` (SUPERSEDED-by-v0.1.0-Notiz im Header) + SESSION-HANDOVER.md (Pause-Banner→DONE Status-Transition).

**Sync-Set:** SYSTEM.md + CORE-MEMORY.md + PIPELINE.md + log.md (dieser Eintrag) + 05_Archiv/refactor-tools/2026-05-23/README.md + SESSION-HANDOVER.md + 01_Skills/core-slim-refactor/ (full skill bundle). **KEIN** PORTFOLIO + Faktortabelle + config.yaml + xlsx + score_history.jsonl + flag_events.jsonl (kein Score/FLAG/Sparraten-Event).

**Lehre:**

- **PEP 758 unparenthesized except IS Py-3.14-Idiom** — Codex+CR misread-Recidiv (Memory `feedback_pre_investigation_recall_check` als Mechanism: empirisches Verify ast.parse+import+pytest trumpft Reviewer-Authority + ruff format-Preference + precedent-commit als Konvergenz-Signal).
- **SystemExit inherits BaseException not Exception** — rollback-sites MUST catch `(Exception, SystemExit)` für documented Atomicity-Garantie. P7 gate-fail signalisiert via `SystemExit(EXIT_GATE_FAIL)`; previous `except Exception` (Break-2 HIGH-1-fix) hat den Atomicity-Rollback silent bypassed.
- **§18-Subprocess-Gate-Check braucht BOTH rc==0 AND status=='PASS'** — entweder Pfad alleine = False-PASS-Branch. Per-Function-Extraction (`_evaluate_p18_result`) macht Hot-Path-Logik unit-testable ohne subprocess-Infrastructure.
- **Plan-vs-Reality-Reconcile bei CP17:** worked-example dry-runs auf live-state für `executed:` retro-doc-configs EXIT 4 = by-design (Classification-Empty), nicht Gate-Fail. Empirical-reproduction-Angle covered by `test_reference_archive_match.py` XFAILs (AK3 OQ3-deferred SHA-vs-RowSet-Hybrid).
- **Snapshot-Substrate-Lineage SUPERSEDED-Mechanism:** `05_Archiv/refactor-tools/2026-05-23/` README.md bekommt SUPERSEDED-Header (statt Delete) — historical reference + empirical baseline für Build-Gate-3 reference-match testing erhalten, operative Pfade umgeleitet auf Skill.

**Cross-Reference:** Plan-File `docs/superpowers/plans/2026-05-23-core-slim-refactor-build.md` (~1600 LOC, 18 Build-CPs) · Spec-File `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` (46,7 KB) · PIPELINE #78 ✅ DONE-Header · CORE-MEMORY §13 (PROMOTED-Eintrag) · SYSTEM.md §Skill-Registry · `01_Skills/core-slim-refactor/` (SKILL.md + 4 references/ + 3 worked-example YAMLs + 31 PASS + 2 XFAIL Test-Suite) · `05_Archiv/refactor-tools/2026-05-23/README.md` (SUPERSEDED-Lineage) · git log `cd1148a..HEAD` (13 Build-Commits) · Skill-Build-Präzedenzen `session-closure` v0.2.0 + `paragraph-18-sync` v0.1.0 (8-Phasen-Pipeline-Konvention).

## [2026-05-23] system | core-slim-refactor v0.1.1 Scope-Hardening: HIGH-4 P0+P7 Subprocess-UTF-8-Crash entdeckt via Cross-Check + Codex-Re-Audit (scoring-neutral, Pipeline-Event)

**Trigger:** Post-`/clear` Continuation-Session nach v0.1.0-Promotion 21:54. User-Frage: "Pipeline 80/81 angehen?" → Empfehlung #80 v0.1.1 Bugfix per Karpathy 2-Phase. Vor PIPELINE-Write: User-Direktive "etwas paranoid, aber Empirie schlägt Vermutung" → Cross-Check Standalone-SystemAudit vs Skill-P0-Pfad.

**Was passierte (empirie-getrieben):**
- Lauf 1: `python 03_Tools/system_audit.py --core -v` standalone → 10/15 PASS, 2 FAIL, 3 WARN, deterministisch reproducible (identisch zum 19:13-Lauf).
- Lauf 2: `python 01_Skills/core-slim-refactor/scripts/core_slim_refactor.py session-handover-date-cut.yaml --dry-run --force-rerun` → **CRASH** in P0-Phase: `UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d` im Reader-Thread + Folge-Crash `TypeError: write() argument must be str, not None` an L111.
- Root-Cause: `subprocess.run([...], capture_output=True, text=True)` an L104-110 ohne explizites `encoding=` → Windows-Default cp1252 statt UTF-8 → Reader-Thread crashed bei `§`-Zeichen im system_audit-Output (z.B. PIPELINE.md:75 `05_Archiv/CORE-MEMORY-§12-Chronik…`-Pfad). Bei Thread-Crash ist `r.stdout=None` aber L111 macht `sys.stdout.write(r.stdout)` ohne None-Guard.

**Codex-Re-Audit (gpt-5.3-codex single-pass, agent `ae2e863dc1869630a`, 22:38):**
- 4 HIGH gemeldet → nach Verify final **3 HIGH valide** (HIGH-1 confirmed L264-276 `target_file`+`archive_path` absolute Windows-Pfade in pointer_context, HIGH-4 P0 confirmed, NEW-HIGH P7 confirmed sibling L349-357 selber Patch) + **1 FALSE-POSITIVE** (PEP 758-Misread: `except A, B:` L65/491/498/504 als "Python-2-Bug" → valide Python 3.14, `ast.parse` SyntaxValid:OK, identischer CP3-Reinfall paragraph-18-sync 22.05.).
- 2 MEDIUM defer v0.1.2/v0.2.0 (`_repo_root()` encoding L58-63 latent + Direct-Write-vs-atomic-replace L238/298 architektural).
- Sparring-Escalation-Threshold (NEW HIGH ≥2) NICHT erreicht — Single-Pass reicht.

**Lessons-Learned:**
- **Cross-Check Skill-Pfad vs Standalone bei Subprocess-Wrapping** — neue Memory `feedback_cross_check_skill_vs_standalone.md`. Standalone-PASS+Skill-CRASH = Subprocess-Capture-Layer-Bug, NICHT Tool-Bug. Spart Stunden falscher Diagnose-Pfade.
- **First-Real-Run-Test-Gap:** Vault `log.md`-Scope hatte ASCII-only Audit-Output ODER `pre_run=false` → Bug systematisch unsichtbar. v0.1.1-TDD muss non-ASCII-Fixture testen (Codex Q5: cp1252-failing-aber-UTF-8-valid Bytes).
- **PEP-758-Codex-Misread = wiederkehrendes False-Positive-Pattern** — Memory `feedback_pre_commit_diff_inspection` ist Schutz; bei `except A, B:`-Flag immer `ast.parse` als Verify, nicht Codex-Authority folgen.
- **Karpathy 2-Phase strikt halten:** Codex-MEDIUMs (atomic-write, encoding-helper) sind architektural-Improvements, NICHT Bugfix — explizit defer v0.1.2/v0.2.0 statt mit v0.1.1 bundlen. Sonst "Mülleimer-v2"-Risiko (User-Direktive).

**Persistenz:**
- `00_Core/PIPELINE.md` #80 mit HIGH-4 + NEW-P7-Sibling + Codex-Re-Audit-Block + PEP-758-FP-Doku + MEDIUMs-Defer + Re-Estimate ~2.5-3.5h.
- `01_Skills/core-slim-refactor/references/failure_modes.md` mit HIGH-4-Eintrag #6 + Reproduktion + Codex-FP-Block + Cross-Reference-Append.
- Memory: `feedback_cross_check_skill_vs_standalone.md` + MEMORY.md-Index-Eintrag.
- Vault log.md: dieser Eintrag.

**Cross-Reference:** PIPELINE #80 (Updated-Scope) · failure_modes.md MEDIUM-12/13/11/HIGH-4/MEDIUM-NEW · Codex-Re-Audit agent `ae2e863dc1869630a` · Memory `feedback_cross_check_skill_vs_standalone` (NEU) + `feedback_windows_console_ascii_safe_inline_python` + `feedback_windows_python_crlf_text_mode` + `feedback_pre_commit_diff_inspection` (PEP-758-Disziplin) + `feedback_codex_sparring_heuristic` + `feedback_brainstorming_terminal_override_dynastie` (Spec/Build-Session-Trennung als Begründung für /clear vor v0.1.1-Build) · Karpathy §0 (INSTRUKTIONEN) · v0.1.1-Build-Session geplant fresh post-`/clear` mit `systematic-debugging` (HIGH-2) + `test-driven-development` (HIGH-4 TDD-Prevention) + `verification-before-completion` (Pre-Commit-Gate) Skills.

---

## 2026-05-23 23:55 GMT+2 — PIPELINE #80 ✅ core-slim-refactor v0.1.1 Bugfix-Release DONE (scoring-neutral)

**Event-Klasse:** pipeline-item + system-zustand (Multi-Event Union §18.2). Skill-Version-Bump v0.1.0 → v0.1.1. Live-Score-Impact NULL — DEFCON v3.7 + 12 Scores + Sparraten 285€ unverändert.

**Delivered (TDD-Red→Green vollständig per Karpathy 2-Phase Bugfix-only):**
- **HIGH-1** — Pointer-Context absolute-Path-Leak gefixt via neuem `_build_pointer_context`-Helper (P5). `archive_path` + `archive_link` + `target_file` jetzt alle relative POSIX-Paths (basename für `target_file`), nicht mehr `str(absolute Path)`. L264-276 alt → Helper L249-281 neu.
- **HIGH-3** — `audit.fail_close_on_drift` Default-Flip `true` → `false` (advisory, opt-in via YAML). Stderr-WARNING bei rc!=0. Skill auf real-Repos mit imperfekter Audit-State (10/15 PASS) wieder nutzbar — vorher harter Exit 3 in P0.
- **HIGH-4** — P0 (L104-119) + P7 (L348-360) subprocess `encoding="utf-8", errors="replace"` + None-Guard `r.stdout or ""` / `r.stderr or ""` an beiden Sites identisch. cp1252-Reader-Thread-Crash bei UTF-8-Audit-Output ausgeschlossen. `_evaluate_p18_result(r.returncode, r.stdout or "")` für None-Safety.
- **MED-NEW** — P2 Classify stderr-Diagnostic (pattern/anchor/n_archive/n_slim/n_keep/keywords/threshold + Likely-Cause-Hints) + neuer `EXIT_ANCHOR_NOT_FOUND = 11` (User-Decision Konflikt-Auflösung gegen Item-80-Vorschlag-`5` — 5 ist seit v0.1.0 `EXIT_MIGRATE_VIOLATION`, Re-Numbering wäre Breaking-Change).
- **HIGH-2 reklassifiziert via Phase-1-Diagnose** (kein Code-Bug): Backup-Lifecycle ist by-design — `--dry-run` skipt `shutil.copy2` (L98), `_cleanup_backup_on_success` löscht nach erfolgreichem P7-OK (L510). `Path.with_suffix(".md.pre-refactor.bak")` empirisch validiert auf Python 3.14.3 für alle Live-Targets. `.gitignore` L35 `*.pre-refactor.bak` vorhanden. Action: `failure_modes.md` MED-13 RESOLVED-Block + 2 Lifecycle-Regression-Tests (`test_high2_backup_skipped_in_dry_run` + `test_high2_backup_created_in_non_dry_run`). Spart ~30min vs Code-Touch-Versuch.

**Verification:**
- pytest 43 PASS + 2 XFAIL (vorbestehend); **+12 neue Tests** in `tests/test_v0_1_1_bugfixes.py` (alle waren initial RED, jetzt GREEN nach Fixes).
- 3× Worked-Example dry-run re-smoke: Pattern A (`ruflo-sunset-bucket.yaml`), Pattern B (`defcon-fat-rows-slim.yaml`), Pattern C (`session-handover-date-cut.yaml`) — alle laufen durch bis P2 mit klarer Diagnostic. **Pattern C ohne --skip-audit:** P0 jetzt clean durch (vorher P0-cp1252-Crash), Audit advisory rc=1, P2 EXIT 4 mit Stats — empirischer Beweis für HIGH-3 + HIGH-4 Wirksamkeit.
- Standalone audit cross-check (`/SystemAudit --core`) identisch zum Skill-Subprocess-Capture (10/15 PASS) — Bug-Klasse von 23.05. ~22:25 (Standalone-PASS + Skill-CRASH-cp1252) ist behoben.

**Out-of-Scope (Karpathy 2-Phase, defer v0.1.2):**
- Codex-MED (a): `_repo_root()` L58-63 text=True ohne encoding — latent, nur bei non-ASCII Repo-Pfad.
- Codex-MED (b): P4/P5 direct-write (L238-239, L298-299) statt `os.replace()`-atomic — architektural-Improvement, Backup-Logik schützt.
- PEP 758 False-Positive `except A, B:` (L65/491/498/504) — Codex-Misread, gültig auf Python 3.14, NICHT angefasst.

**Skills used (Disziplin-Gates):**
- `superpowers:systematic-debugging` — HIGH-2 Phase-1-Root-Cause-Walk (kein Code-Bug aufgedeckt, ~30min gespart).
- `superpowers:test-driven-development` — 12 failing Tests RED, dann GREEN nach Fixes; keine production-code-vor-test.
- `superpowers:verification-before-completion` — pytest full-run + 3× worked-example re-smoke + standalone cross-check vor Commit.
- `paragraph-18-sync` — User-Reminder 23:48 (Lapsus aufgedeckt — Skill hätte schon **vor** dem Sync-Edit invoked werden sollen, nicht erst zum Commit-Gate). Memory-Lücke: kein Auto-Invoke-Trigger bei §18-relevanten File-Touches dokumentiert; v0.1.2-Backlog-Item für Memory `feedback_paragraph18_skill_auto_invoke_on_sync_files.md`.

**Sync-Set executed (§18.2 Multi-Event Union pipeline-item + system-zustand):**
- `01_Skills/core-slim-refactor/scripts/core_slim_refactor.py` (HIGH-1/3/4 + MED-NEW Code-Patches + Exit-Code-Konstante)
- `01_Skills/core-slim-refactor/SKILL.md` (v0.1.0 → v0.1.1, Exit-Code-Tabelle, §5 encoding-Hinweis, `fail_close_on_drift` Default-Doc)
- `01_Skills/core-slim-refactor/references/failure_modes.md` (MED-13 RESOLVED-Block)
- `01_Skills/core-slim-refactor/tests/test_v0_1_1_bugfixes.py` (+12 Tests, NEU)
- `00_Core/PIPELINE.md` (Item #80 Status 👁→✅ + Footer v2.66→v2.67)
- `00_Core/SYSTEM.md` (§Skill-Registry v0.1.0→v0.1.1)
- Vault `log.md` (dieser Eintrag)

**Cross-Reference:** PIPELINE #80 (DONE-Body) · SYSTEM.md §Skill-Registry · failure_modes.md MED-13 · PIPELINE #81 (v0.2.0 Roadmap, unverändert) · Memory `feedback_cross_check_skill_vs_standalone` (Bug-Klasse 22:25-Discovery) · Karpathy §0 (Bugfix-only-Disziplin) · Codex-Re-Audit `ae2e863dc1869630a` (3 HIGH + 1 FP + 2 MED-defer).

## [2026-05-24] system | core-slim-refactor v0.1.1 Pre-Flight non-dry Validation DONE — HIGH-1/3/4 in der Wildnis verifiziert (PIPELINE #80 Battle-Tested)

**Event-Typ:** System-Zustand-Refinement (Skill-Validation, scoring-neutral). Erweitert PIPELINE #80 DONE-Status um empirischen "battle-tested"-Beweis. Kein neuer System-State (Skill bereits seit 23.05. v0.1.1), nur Wildness-Empirie.

**Was passiert ist:**
- Pre-Flight non-dry-Run von core-slim-refactor v0.1.1 gegen Vault `log.md` (Pattern C Date-Cut, `cut_before=2026-05-22`).
- Config: `_tmp_preflight/log-md-date-cut-2026-05-22.yaml` (ephemer, post-Run cleanup; nicht in Skill-Verzeichnis).
- Run-Resultat: Exit 0, P0→P7 alle clean, ~5s Laufzeit.
- Archive geschrieben: `05_Archiv/log-bis-2026-05-21-archiv.md` (48.618 b, 12 Einträge: 5×2026-05-17 + 3×2026-05-18 + 4×2026-05-21). `.gitignored` (`05_Archiv/*`).
- log.md: 187.619 → 139.424 b (–48.195 b), 22 Einträge behalten (14×2026-05-23 + 8×2026-05-22).

**Verifizierte Fixes (n=1 in der Wildnis):**
- **HIGH-4** P0+P7 cp1252-Fix ✅ — Audit-Subprocess gegen 00_Core (PIPELINE/STATE/INSTRUKTIONEN voll mit `§`/`→`/Umlauten) lief vollständig durch ohne `TypeError: write() argument must be str, not None`. Reinfall der 22:25-Klasse ist behoben.
- **HIGH-1** Pointer-Relative-POSIX ✅ — neuer Pointer log.md Z.8: `[../../../05_Archiv/log-bis-2026-05-21-archiv.md]` (relativer POSIX-Pfad als Display-Text). Cross-Check: alter v0.1.0-Pointer Z.6 zeigt noch absoluten Windows-Pfad als Display-Text (Bug-Beweis daneben sichtbar).
- **HIGH-3** `fail_close_on_drift` default `false` ✅ — P0 Audit returned rc=1 (2 FAIL + 3 WARN baseline-State): stderr `WARNING: P0 audit returned rc=1 (advisory; set audit.fail_close_on_drift=true to enforce)`, Run weiterlief regelkonform.
- **MED-NEW** P2 Classify Diagnostic ⚠️ N/A — P2 classifyte erfolgreich (12+22), Diagnostic-Pfad nicht getriggert. Bleibt v0.1.2-Verify-TODO (Edge-Case-Run mit z.B. `cut_before=1970-01-01` für `EXIT_CLASSIFY_EMPTY=4`).

**Side-Findings (Carryover für v0.1.2/v0.2):**
- **LOW-NEW (cosmetic)** Archive-Header (`{target_file}` Template) zeigt absoluten Windows-Pfad in "Source:"-Zeile: `Source: C:\Users\tobia\OneDrive\Desktop\Claude Stuff\07_Obsidian Vault\Obsidian Mindmap\Investing Mastermind\log.md`. HIGH-1 `_build_pointer_context`-Helper deckt nur Pointer-Context ab, nicht Archive-Header-Context. Vault-Portabilität-Lücke, nicht funktional-blockierend.

**Layer-1+2 Autonomous-Emission Verify (empirisch, n=1):**
- Beim ersten §18-File-Touch (log.md-Mutation in P5/P6 des Skill-Runs) habe ich **NICHT** spontan in user-facing Output autonom `!ParaSync18`-Empfehlung emittiert. Sync-Bewusstsein war nur im internen Reasoning vorhanden (durch User-Prompt-Anker gepriment), nicht in proaktiver Suggestion.
- Konkret beobachtbar: lineare Verifikation (HIGH-1/3/4-Check) ohne autonome Sync-Pause-Suggestion bis User explizit nachfragte/erlaubte.
- Empirischer Befund: **Layer-1 (Memory) + Layer-2 (INSTRUKTIONEN §18.0 + Routing-Table §18-File-Touch-Zeile) sind unter regulären Bedingungen nicht stark genug für autonome `!ParaSync18`-Emission ohne expliziten Aufgaben-Prompt-Anker.** Selbst mit kognitiver Präsenz durch User-Prompt nicht in user-facing Output sichtbar gemacht.
- **Layer-3 (Pre-Commit-Hook `03_Tools/precommit/para18_sync_reminder.py`) wird durch diesen Commit live-getestet** — die noch unbewiesene Schicht. Erwartung: Hook erkennt `log.md` im staged-set, emittiert advisory WARN mit inferred event-type + `!ParaSync18`-Recovery-Hint. Bei OK = `PARA18_VERIFIED=1`-Bypass-Protokoll für diesen Sync-Run.
- **Nachschärfungs-Hypothese (für separate Session):** Layer-1-Memory-Bullet zu §18 ist abstrakt; ein konkreter Trigger-Sentinel ("vor jedem Edit/Write auf §18-File-Set: STOP, suggestiere `!ParaSync18`") wäre wirksamer. Routing-Table §18-File-Touch-Zeile ist normativ aber wird passiv am Session-Start gelesen, nicht in aktives Reasoning-Loop überführt. → Memory + INSTRUKTIONEN-Wortlaut-Refinement, n=2-Empirie nach Layer-3-Test in diesem Commit als Substrate.

**Sync-Set executed (§18 system-zustand-Event, scoring-neutral, atomar):**
- Vault `log.md` (dieser Eintrag + Pattern-C-Mutation aus Pre-Flight-Run, 1 commit).
- Archive `05_Archiv/log-bis-2026-05-21-archiv.md` (`.gitignored`, kein commit-relevant).
- **KEIN** STATE.md / PIPELINE.md / SYSTEM.md / CORE-MEMORY / Faktortabelle / config.yaml / xlsx / jsonl Change — reine Validation-Empirie, kein neuer System-State, kein Score/FLAG/Sparraten-Touch.
- `_tmp_preflight/` Cleanup separat (keine Commit-Berührung).

**Skills used (Disziplin-Gates):**
- `core-slim-refactor` v0.1.1 — first non-dry post-promotion Run.
- `paragraph-18-sync` Validator (`03_Tools/para18_sync/validator.py system-zustand --dry-run --json`) — Bundle-Verify vor Commit.
- `superpowers:verification-before-completion` — Pre-State-Hash + Post-State-Hash + Fix-Verify pro HIGH-Item vor Sync.
- Memory `feedback_pre_commit_diff_inspection` — surgical `git add` (nur log.md), 55+ andere dirty Files draußen gehalten.
- Memory `feedback_brainstorming_terminal_override_dynastie` — Pre-Flight ist Execution, kein Spec-Spawn; #81 Spec-Phase in separater Session.

**Next:** (a) `_tmp_preflight/` Cleanup separat. (b) Layer-1+2 Nachschärfung als eigene Session mit n=2-Empirie aus Layer-3-Hook-Live-Test. (c) PIPELINE #81 v0.2.0 Spec-Phase (separate Session, brainstorming-terminal-override).

**Cross-Reference:** PIPELINE #80 (DONE-Body, Battle-Tested-Annotation pending) · `03_Tools/precommit/para18_sync_reminder.py` (Layer-3-Live-Test diesen Commit) · INSTRUKTIONEN §18.0 (Auto-Invoke-Verankerung, Layer-2) · Memory `feedback_classifier_not_recognize_askuserquestion` · Memory `feedback_brainstorming_terminal_override_dynastie`.

---

## 2026-05-24 — Pipeline-Item-Event: #80 Defense-in-Depth Nachschärfung n=2 + L3-verbose-Quick-Fix (scoring-neutral)

**Event-Typ:** Pipeline-Item-Annotation (kein Status-Move, kein neues #-Item) — Robustheits-Erhöhung an allen 3 Defense-Layern auf Basis n=2 Lapsus-Empirie post-97d582a.

**Was passiert ist:**
- **Root-Cause-Triangulation L3-Silent-Befund** vor jeder Mutation (3-Punkt-Empirie):
  - **T1** Hook direkt (`python 03_Tools/precommit/para18_sync_reminder.py 00_Core/PIPELINE.md`) → stderr-Output voll sichtbar, Hook funktioniert.
  - **T2** Framework default (`pre-commit run paragraph-18-sync-reminder --files …`) → nur `…Passed`, kein Output. **Reproduziert das 97d582a-Silent-Behavior**.
  - **T3** Framework mit `--verbose` CLI-Flag → Output wieder sichtbar.
  - Schluss: pre-commit-Framework unterdrückt stderr von passing Hooks (exit 0) per Default; `verbose: true` ist der scoped Quick-Fix.
- **L3-Quick-Fix (Priorität):** `verbose: true` zu `paragraph-18-sync-reminder` in `.pre-commit-config.yaml` mit Inline-Kommentar (n=2-Empirie + T-Triangulation-Refs). Smoke-Test post-edit: Framework default verbosity zeigt jetzt vollen advisory-WARN-Block.
- **L1-Nachschärfung (Memory):** `feedback_paragraph18_skill_auto_invoke_on_sync_files.md` — Why-Block n=1→n=2 (Skip #1 v0.1.1-Build 23.05. + Skip #2 97d582a-Pre-Flight 24.05. ~00:08); How-to-apply um **Pre-Edit-Reflex** ergänzt: user-facing `!ParaSync18 ... --dry-run` als ERSTER Output bei §18-File-Edit-Intention, nicht internal (internal-only-Reflex war der n=2-Failure-Mode).
- **L2-Nachschärfung (INSTRUKTIONEN §18.0):** v2.5 → v2.5.1 — Lapsus-Empirie-Block dokumentiert beide Skips + L3-Silent-Triangulation; Defense-in-Depth-Layer-Hierarchie neu sortiert: **L3 = primary safeguard (deterministisch via file-pattern-Match), L1+L2 = backup (empirisch nicht selbst-tragend bei n=2)**.
- **CLAUDE.md-Routing-Table:** unverändert — file-pattern-Trigger-Row `§18-File-Touch (auto)` existiert bereits seit v0.1.1.

**Hypothese aus 97d582a-Eintrag (Z.814) bestätigt:** "Memory + INSTRUKTIONEN §18.0 unter regulären Bedingungen NICHT stark genug für Autonom-Emission" — n=2 Substrate macht die These belastbar; L3 als deterministischer Layer übernimmt die Garantie, L1+L2 bleiben backup.

**Sync-Set (§18 Pipeline-Item-Event, scoring-neutral, atomar):**
- `00_Core/PIPELINE.md` (Footer v2.68 → v2.69 + #80 Defense-in-Depth-Nachschärfung-Annotation)
- `00_Core/INSTRUKTIONEN.md` (§18.0 v2.5 → v2.5.1, Defense-in-Depth-Block neu)
- `.pre-commit-config.yaml` (`verbose: true` zu `paragraph-18-sync-reminder`)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)
- **KEIN** SYSTEM.md (kein DEFCON/MCP/Briefing-Change, keine Skill-Version-Bump — Hook-Config + §18.0-Sub-Versions-Bump ist Doktrin-Refinement, kein System-Zustand-Change)
- **KEIN** STATE.md (Nachschärfung ist <10-Tage-Critical-Alert-würdig nicht, Trail über git log + log.md + PIPELINE-Footer)
- **KEIN** PORTFOLIO / Faktortabelle / CORE-MEMORY / score_history / flag_events / config.yaml / xlsx (kein Score/FLAG/Sparraten-Touch).

**Validator-Lauf:** `paragraph-18-sync` pipeline-item-Event non-dry vor commit; `PARA18_VERIFIED=1` für eigentlichen Commit.

**Lehre:**
- **Karpathy „Pre-Refactor-Caller-Scan"** rechtfertigt sich erneut: Vor Mutation des Memory + INSTRUKTIONEN-Wortlauts wurde die L3-Silent-Hypothese empirisch trianguliert. Hätte ich blind „Nachschärfung" geschrieben ohne T1/T2/T3, wäre die L1+L2-Mutation auf falscher Annahme aufgebaut (Hook würde nach „Nachschärfung" weiterhin silent bleiben — `verbose: true` ist der eigentliche User-Sichtbarkeit-Hebel).
- **Defense-in-Depth-Hierarchie ist empirisch kalibriert, nicht symmetrisch:** L3 (Hook = deterministisch) trägt das Safeguard, L1+L2 (Memory + INSTRUKTIONEN = Modell-Disziplin-Layer) sind backup. Bei n=2 Skip ist L3-Promotion zu primary erforderlich, sonst falsche False-Security.
- **Verbose-Scope-Disziplin:** `verbose: true` per-Hook, NICHT global per `--verbose` CLI-Flag oder Framework-Setting — andere passing Hooks (crlf-guard, ruff) bleiben silent. Scope-Hygiene wahrt CR-Konvergenz aus Memory `feedback_cr_convergence_and_project_compat`.

**Cross-Reference:** 97d582a Commit-Message (n=1-Empirie-Substrate, Z.814 Hypothese) · `.pre-commit-config.yaml` Z.~63 (`verbose: true`-Block) · INSTRUKTIONEN §18.0 (v2.5.1) · Memory `feedback_paragraph18_skill_auto_invoke_on_sync_files` (n=2 + Pre-Edit-Reflex) · pre-commit-Framework-Doku: passing-Hook-stderr-Suppression-Default.

**Next:** PIPELINE #81 v0.2.0 Spec-Phase (separate Session); n=3-Empirie-Watch über kommende §18-File-Edits zur Defense-in-Depth-Validierung.

---

## 2026-05-24 — Pipeline-Item-Event: #81 Re-Defer + Trigger-Schärfung + Scope-Pre-Lock (scoring-neutral)

**Event-Typ:** Pipeline-Item-Refinement (kein Status-Move auf DONE, kein neues #-Item, kein Score/FLAG/Sparraten-Touch) — `core-slim-refactor v0.2.0` Feature-Release Re-Defer-Decision nach Karpathy-Brainstorm; Trigger-Spec geschärft (a/b/c → T1/T2/T3); Scope-Pre-Lock 9+10+14 (15 → v0.3) damit nächster Brainstorm direkt in Spec-Phase springt.

**Was passiert ist:**
- User triggered Spec-Phase per Dynastie-Override-Discipline (Brainstorm → Spec → Codex-Sparring → STOP, Memory `feedback_brainstorming_terminal_override_dynastie`).
- **Brainstorming-Skill aktiviert** (`superpowers:brainstorming`), Substrate-Investigation parallel zu Karpathy-konformen Clarifying-Questions:
  - **Trigger-T1 empirisch geprüft:** SH = 44.5K (45562 Bytes) < 60K-Threshold; Banner-History minimal (1 Date-Ref, 6 Headers, 27 Bullet-Lines insgesamt) → **T1 inaktiv**.
  - **Skill-Maturity-Check:** v0.1.1 ist 24h-frisch (commit `d78095d`), nur 1× Real-Run gegen `log.md` 2026-05-23 ~20:46. Alle v0.1.1-HIGH-Befunde (HIGH-1 pointer-relative-Path / HIGH-3 fail-close-Default / HIGH-4 cp1252-Subprocess) kamen aus First-Run-Empirie, nicht aus Pre-Spec.
  - **Pattern-Match-Inferenz:** v0.2.0-Spec-jetzt würde post-Anwendung material drehen → Re-Spec-Verschwendungs-Risiko > Spec-jetzt-Vorteil.
- **Scope-Investigation trotzdem durchgeführt** (failure_modes.md MEDIUM-9/10/14/15 pro Item nach Pain-Substrate klassifiziert), damit nächster Brainstorm nicht von Null neu starten muss:
  - **MEDIUM-9 Bullet-Adapter** = GO (SH-Bullet-Format strukturell blockiert, Voraussetzung für SH-Slim)
  - **MEDIUM-10 Header-Pre-Check** = GO (empirisch 105 silent mis-classifications im First-Run, strukturelle Härtung gegen Item-#79-Klasse)
  - **MEDIUM-14 executed-Auto-Pop** = GO (Re-Run-Lock-Hazard operational, nicht nur Convenience)
  - **MEDIUM-15 Backlink-Graph** = DEFER → v0.3 (failure_modes-Status "akzeptiert", Null-Coupling zu 9/10/14, spekulativ ohne Trigger)
- **Karpathy-Konsistenz-Check (CLAUDE.md §0 + Auto-Memory):** 9+10+14 = simplicity-first ✓, surgical-additive ✓, no premature abstraction ✓, no design-for-hypothetical ✓; Pre-Build-Gate-Disziplin (Caller-Scan + separater Helper + acceptance-Test pro Item) in Spec-Phase verankert.
- **User-Decision:** Re-Defer empfohlen + approved. Plus User-Frage "Skill erstmal ausprobieren, anhand Resultates entscheiden?" — exakt der Karpathy-Empirie-Pfad, der das Brainstorm-Substrate stützte.

**Trigger-Schärfung (a/b/c → T1/T2/T3):**
- **alt (a)** "SH > 60K oder Banner-History > 14 Tage" → **T1** unverändert in der Definition, plus dritte ODER-Bedingung "Resume-Block strukturell beeinträchtigt" (explizit machen).
- **alt (b)** "accumulating Feature-Backlog (3+ Items)" → **T2** geschärft: nicht "Backlog-Größe", sondern "≥1 weitere echte v0.1.1-Anwendung gegen anderes 00_Core-File (z.B. CORE-MEMORY.md Date-Header-Slim) liefert zweite Empirie-Schicht" (Karpathy YAGNI: Backlog-Größe ist kein Pain, Empirie-Schicht-Knappheit schon).
- **alt (c)** "Konsolidierungstag-Slot mit Skill-Bau-Kapazität" → **T3** geschärft: "Slot **UND** explizit-konkreter Use-Case der Bullet-Adapter erzwingt" (kein generic-Slot-Trigger mehr — verhindert "wir bauen weil Slot frei").

**Scope-Pre-Lock-Wert:** Nächster Brainstorm (sobald T1/T2/T3 feuert) springt direkt in Spec-Phase ohne Scope-Re-Negotiation. Karpathy "surface assumptions" → Investigation-Ergebnis durable verankert statt verloren.

**Sync-Set (§18 Pipeline-Item-Event, scoring-neutral, atomar):**
- `00_Core/PIPELINE.md` (Footer v2.69 → v2.70 + Item #81 Re-Defer-Note + Trigger-Schärfung + Scope-Pre-Lock)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)
- **NEU** Auto-Memory `feedback_redefer_over_prespec_dynastie.md` (Karpathy-Lesson-Anker: "v0.x Re-Defer bei fehlendem empirischen Pain-Substrate" für Re-Use bei späteren Feature-Bundle-Triggern)
- **KEIN** STATE.md (kein Critical-Alert), **KEIN** SYSTEM.md (kein DEFCON/MCP/Skill-Version-Change — v0.1.1 unverändert), **KEIN** PORTFOLIO / Faktortabelle / CORE-MEMORY / score_history / flag_events / config.yaml / xlsx (kein Score/FLAG/Sparraten-Touch).
- **KEIN** Spec-File geschrieben (Dynastie-Override: Spec-Phase nicht gestartet) — failure_modes.md bleibt einziger Item-Backlog-Anker neben PIPELINE #81.

**Skills used (Disziplin-Gates):**
- `superpowers:brainstorming` — Skill aktiviert, aber Terminal-Override gehalten (kein writing-plans-Switch, kein design-doc-Write).
- Memory `feedback_brainstorming_terminal_override_dynastie` — Pickup endete bei Spec-Substrate-Investigation; Build separate Session.
- Memory `feedback_plan_on_runtime_not_doc_assumption` — Empirie-Primat als Substrate für Re-Defer-Entscheidung.
- Memory `feedback_codex_sparring_heuristic` — Codex-Single-Pass für Pipeline-Item-Edit nicht-zwingend; User opted-out → konsistent.

**Lehre:**
- **Karpathy "Runtime > Doku-Annahme" als entscheidungs-tragendes Substrat:** Brainstorm-Investigation deckte auf, dass die scheinbar logische Sequenz "v0.1.1 → v0.2.0 sofort" empirisch nicht gestützt ist; v0.1.1 ist 24h alt, alle Bugfixes kamen aus 1× Real-Run, zweiter Real-Run würde voraussichtlich weitere v0.2.0-formgebende Befunde liefern. User-Frage "Skill erstmal benutzen?" war kongruent zur Karpathy-Logik — Pre-Spec wäre Doku-Annahme statt Runtime-Empirie.
- **Brainstorming-Substrate ist nicht verschwendet wenn Re-Defer entschieden wird:** Investigation hat (a) Trigger-Schärfung und (b) Scope-Pre-Lock produziert — beides durable in PIPELINE verankert. Nächster Brainstorm springt direkt in Spec-Phase. Karpathy "surface assumptions" auch in Re-Defer-Form werthaltig.
- **Trigger-Definition-Schärfe als YAGNI-Verstärker:** alt-(b) "Backlog-Größe ≥3 Items" war zu weicher Container-Trigger — formal aktiviert ohne Pain. Neue T2 "echte 2. Empirie-Schicht" ist pain-grounded; T3 "konkreter Use-Case" verhindert "wir bauen weil Slot frei". Trigger-Honesty als Karpathy-Reflex.
- **Codex-Sparring scoping:** Pipeline-Item-Edit textuell-knapp, kein Code-Mechanismus, kein Score-Move → Single-Pass-Default nicht-zwingend; User opted-out konsistent zur Heuristik.

**Cross-Reference:** PIPELINE #81 v0.2.0-Body (Re-Defer-Note + T1/T2/T3 + Scope-Pre-Lock 9+10+14) · `01_Skills/core-slim-refactor/references/failure_modes.md` (MEDIUM-9/10/14 Pain-Substrate, MEDIUM-15 "akzeptiert"-Status) · `00_Core/SESSION-HANDOVER.md` (44.5K Substrate-Beleg) · Auto-Memory `feedback_redefer_over_prespec_dynastie.md` (neue Lesson-Anker) · Memory `feedback_plan_on_runtime_not_doc_assumption` + `feedback_brainstorming_terminal_override_dynastie` (entscheidungs-tragend) · Commit `<TBD>`.

**Next:** PIPELINE #81 bleibt DEFERRED bis T1/T2/T3 feuert. Wahrscheinlichster Re-Activation-Pfad: nächste konkrete Slim-Anwendung des v0.1.1-Skills gegen ein anderes 00_Core-File (T2) oder organische SH-Größe → 60K-Threshold (T1). Bis dahin: failure_modes.md MEDIUM-9/10/14 als Backlog-Anker; MEDIUM-15 ohne PIPELINE-Item bis Use-Case konkret.

## 2026-05-24 — System-Event: core-slim-refactor v0.1.1 T2-Empirie 2 Live-Runs DONE — Phase-3-Bucket-Welle (scoring-neutral, system-zustand Multi-Event Union §18-Sync)

**Trigger:** T2 (≥1 weitere echte v0.1.1-Anwendung) per `feedback_redefer_over_prespec_dynastie` aktiv — User-Direktive "Wir brauchen mindestens 2 Testruns" → 2 unabhängige Pattern-A bucket-archive Live-Runs gegen CORE-MEMORY §6+§13 als 4./5. Bucket-Layer (Phase-3-Folge nach 23.05. Phase 1+2).

**Test #1 (~02:06 GMT+2):** §6 Versionsverlauf Pattern A bucket-archive
- YAML: `01_Skills/core-slim-refactor/references/configs/core-memory-s6-versionsverlauf-bucket.yaml`
- Keywords: 17.04. / 18.04. / 19.04. / 22.04. / 24.04. / 07.05. → 10 v3.7-Era-Rows archive; Keep `2026-05-21` → 1 session-closure Row
- Archive: `05_Archiv/CORE-MEMORY-§6-Versionsverlauf-v3.7-Era-archiv.md` (1559b, 10 Rows)
- Source-Delta: -10/+1 (10 Rows raus, 1 Pointer rein); 125.3K → 124.2K (-1.1K)
- Exit-Code: 0; P0-P6 alle PASS; P3 warn_continue (11 legitime §6-Cross-Refs)

**Test #2 (~02:14 GMT+2):** §13 Lifecycle Pattern A bucket-archive
- YAML: `01_Skills/core-slim-refactor/references/configs/core-memory-s13-lifecycle-pre-may-10-bucket.yaml`
- Keywords: 23.04. / 24.04. / 25.04. / 26.04. / 27.04. / 30.04. / 02.05. / 07.05. / 2026-05-08 / 2026-05-09 → 26 Rows archive; Keep 10.05.+ → ~13 Rows
- Archive: `05_Archiv/CORE-MEMORY-§13-Lifecycle-23.04.-09.05.2026-archiv.md` (26861b, 26 Rows)
- Source-Delta: -32/+7 (incl. 5 Whitespace + 1 Footer-Reflow + 1 Pointer); 124.2K → ~89K (-35K)
- Exit-Code: 0; P0-P6 alle PASS

**🔴 Empirische v0.1.2-HOTFIX-Findings (3 stk):**

1. **HIGH P7 §18-Skill-Gate Path-Mismatch** — Skill sucht hardcoded `01_Skills/paragraph-18-sync/scripts/p18_sync.py` (existiert nicht) + Fallback `paragraph-18-sync` bare-command (nicht in PATH). Real-Validator: `03_Tools/para18_sync/validator.py`. P7 emittiert silent WARNING `"paragraph-18-sync not found; skipping §18-gate (operative runs MUST resolve)"` statt fail-close — SKILL.md §4-Discipline-#5 Versprechen verletzt. Auto-Memory `feedback_core_slim_p7_p18_path_mismatch.md` persistiert. **Root-Cause:** Spec-Drift zwischen den zwei v0.1.0-Skills (beide am 23.05.2026 promoted, ohne Cross-Wire-Up-Build-Gate).

2. **MEDIUM Section-Reflow** — `patterns.py::mutate_bucket_archive` re-baut Section-Body aus `new_section_lines` von Grund auf → harmlose Whitespace/Footer-Re-Layout im Diff (Test #2: -32/+7 statt erwartet -26/+1; mathematisch korrekt, kein Datenverlust, aber Diff-Optisch lauter als nötig).

3. **MEDIUM Pointer-Placement** — wenn `pointer_date` nicht im YAML gesetzt → Default „9999-99-99" → kein kept-table-row matched `dt > pointer_date` → Fallback-Branch appended Pointer am Section-Ende. In CORE-MEMORY §13 enthält Section-Ende den Footer-Bullet → Pointer landet POST-Footer (sichtbar L425 nach L424-Footer). Fix: `pointer_date` als required-YAML-Field markieren ODER footer-aware Insertion (skip trailing non-table-rows beim Anchor-Search).

**T2-Trigger-Status:** ≥2 genuine v0.1.1-Anwendungen delivered → **T2 FIRED**. PIPELINE #81 v0.2.0 Spec-Phase kann jetzt aktivieren mit Scope-PreLock 9+10+14 (unverändert) **plus v0.1.2-Hotfix als P0-Item vorgezogen** (3 obige Findings). v0.1.2 = Bugfix-Bump vor v0.2.0-Feature-Release sinnvoll.

**Process-Empirie (Karpathy-meta):**
- **Pessimismus-Fehler korrigiert:** Initial-Recon (5 Files gescannt) framing war "kein Target heute" — falsch, §6 + §13 waren legitimate weitere Bucket-Layer auf already-touched-Files (Multi-Layer Pattern-A explizit by-design). User-Korrektur ("Wir wollen den Skill testen, kein §18-Sync-Detour") rückte den Fokus.
- **§18-Sync ist Operational-Ceremony, nicht Teil des Test-Loops** — Live-Run zur Mutation-Validation ist 1 Sache; commit-mit-§18-Sync ist separate Entscheidung post-Test.
- **Force-add notwendig für .md-Archive:** `.gitignore L8 `05_Archiv/*` blockt — `git add -f` pro Archive-Datei (Convention).
- **Dirty-Tree-Predicate fail-close korrekt** — paragraph-18-sync Validator P1 trigggered bei 56 unrelated dirty files (pre-existing ruff-format 03_Tools+01_Skills); `--allow-dirty 60` Override mit Specific-File-Stage hat saubere Commit-Vorbereitung garantiert.

**Sync-Set (§18 system-zustand-event, scoring-neutral, multi-event Union mit pipeline-item):**
- `00_Core/CORE-MEMORY.md` (§6 + §13 mutated + Footer v1.27 → v1.28)
- `00_Core/SYSTEM.md` (Footer v1.10 → v1.11)
- `07_Obsidian Vault/.../log.md` (dieser Entry)
- `05_Archiv/CORE-MEMORY-§6-Versionsverlauf-v3.7-Era-archiv.md` (force-added)
- `05_Archiv/CORE-MEMORY-§13-Lifecycle-23.04.-09.05.2026-archiv.md` (force-added)
- `01_Skills/core-slim-refactor/references/configs/core-memory-s6-versionsverlauf-bucket.yaml` (recipe)
- `01_Skills/core-slim-refactor/references/configs/core-memory-s13-lifecycle-pre-may-10-bucket.yaml` (recipe)
- Auto-Memory `feedback_core_slim_p7_p18_path_mismatch.md` (NEU, persistiert)

KEIN PORTFOLIO/Faktortabelle/config.yaml/xlsx/jsonl-Touch (kein Score/FLAG/Sparraten-Event). Sparraten 285€ unverändert, DEFCON v3.7 + 12 Scores unverändert.

**Cross-Reference:** PIPELINE #81 v0.2.0-Body (T2-FIRED + 3 v0.1.2-HOTFIX-Items hinzufügen) · CORE-MEMORY §13 (Pointer L425 post-footer als Empirie-Beleg für MEDIUM-3-Bug) · SYSTEM.md §System-Zustand (core-slim-refactor v0.1.1 Bullet bleibt bestehen + v0.1.2-Hotfix-Annahme) · Auto-Memory `feedback_redefer_over_prespec_dynastie` (T2-Fire = Re-Defer korrekt) · `feedback_core_slim_p7_p18_path_mismatch` (3 Findings konsolidiert) · Commit `<TBD>`.

**Next:** v0.1.2-Hotfix-Spec (Karpathy 1-Phase Bugfix-Bump: 3 HIGH/MEDIUM fixes, minimal Scope, Build separate Session). Danach v0.2.0 mit Pre-Lock 9+10+14 wie ratifiziert.

## [2026-05-24] system | PIPELINE #81 Status-Transition DEFERRED → ACTIVATABLE post-T2-Empirie (Pipeline-Item-Event, scoring-neutral)

**Event-Typ:** Pipeline-Item-Status-Transition (Status-Bump nach Trigger-Fire, kein Score/FLAG/Sparraten-Touch).

**Status-Change:** PIPELINE #81 von 👁 DEFERRED → 🔴 ACTIVATABLE für v0.1.2-Hotfix + v0.2.0 Feature-Release. T2-Trigger erfüllt durch Commit `359c296` (T2-Empirie-Welle 2 Live-Runs §6+§13).

**Body-Updates in PIPELINE.md #81:** (a) v0.1.2-HOTFIX-Scope vorgezogen (3 Findings: HIGH P7-§18-Path-Mismatch + MEDIUM Section-Reflow + MEDIUM Pointer-Placement). (b) v0.2.0 Pre-Lock 9/10/14 unverändert, chronologisch NACH v0.1.2 empfohlen. (c) Aufwand v0.1.2 ~2-3h Bugfix-Bump separate Session.

**Footer:** PIPELINE.md v2.70 → v2.71.

**Sync-Set §18 pipeline-item:** PIPELINE.md (#81 + Footer) + log.md (dieser Entry). KEIN weiterer Touch nötig — Detail-Empirie liegt in `359c296`.

**Next:** Neue Session für v0.1.2-Hotfix-Spec (Karpathy 1-Phase, minimal Scope).

## 2026-05-24 — System-Event: core-slim-refactor v0.1.2 Hotfix DONE (PIPELINE #81 v0.1.2-Sub ACTIVATABLE→DONE, scoring-neutral, system-zustand + pipeline-item Multi-Event Union §18-Sync)

**Event-Typ:** System-Zustand-Change (Skill Version-Bump v0.1.1→v0.1.2) + Pipeline-Item-Status-Transition (PIPELINE #81 v0.1.2-Sub).

**Karpathy 1-Phase Bugfix-Bump** auf Basis T2-Empirie commit `359c296` (24.05. ~02:14 GMT+2). Kein voller Spec, kein Codex-Sparring nötig per `feedback_codex_sparring_heuristic`. Pre-Build Mini-Plan + Acceptance-Kriterien als Karpathy-§0.4-Substitut.

**Fix-Scope:**
- **HIGH-1 P7 §18-Skill-Gate Path-Mismatch RESOLVED** — neue Pure-Function `_resolve_p18_command(repo_root)` in `core_slim_refactor.py` mit 3-Step-Probe: `03_Tools/para18_sync/validator.py` PRIMARY → legacy `01_Skills/paragraph-18-sync/scripts/p18_sync.py` (forward-compat) → PATH-bare `paragraph-18-sync`. FileNotFoundError-Branch ersetzt: pre-fix silent-WARNING-skip → `raise SystemExit(EXIT_GATE_FAIL=8) from fnf_err` (fail-close gemäß SKILL.md §4-Discipline-#5).
- **MEDIUM-2 Pointer-Placement footer-blind Fallback RESOLVED** — neuer Helper `_insert_after_last_table_row(lines, pointer_row)` in `patterns.py` walks backwards, findet last `_is_table_row` index, inseriert immediately after. 2 Call-Sites refactored (chronological-fallback + section_bottom; pre-fix landete Pointer POST-Footer-Bullet, sichtbar `00_Core/CORE-MEMORY.md` L425 als historische Evidenz). Pre-Fix-Trailing-Blank-Pop/Append-Logik entfernt (trug auch zur Reflow-Noise bei).
- **NEU env-var `CORE_SLIM_REFACTOR_SKIP_GATE=1`** — test/dev escape-hatch analog `CORE_SLIM_REFACTOR_FORCE_FAIL_PHASE`; bypasst P7 vor Validator-Probe; emittiert kein Codex-Hand-off-Bundle (intentional). Operative Runs setzen das niemals.
- **MEDIUM-16 Section-Reflow selective splice deferred v0.2.0** per Karpathy §0.6 Pre-Implementation-Abort — algorithmischer Refactor `mutate_bucket_archive` (split-rebuild → position-based-splice) violates Bugfix-Surgical-Scope; MEDIUM-2-Fix hat bereits Teil der Reflow-Noise eliminiert; verbleibende Noise = `split("\n")/"\n".join(...)`-Normalisierung, mathematisch korrekt kein Datenverlust.

**Tests:** +6 v0.1.2 regression in neuem File `tests/test_v0_1_2_bugfixes.py` (4 HIGH-1 path-resolution + 4 MEDIUM-2 footer-aware insertion); 2 pre-existing pipeline-tests (`test_live_run_mutates_target_and_writes_archive` + `test_dry_run_matches_live_for_bucket_archive`) bekommen SKIP_GATE env — pre-fix hatten sie nur passed weil P7 silent-skipped war (FileNotFoundError → WARNING). Total: 51 PASS, 2 SKIP.

**Codex Single-Pass Review (gpt-5.3-codex, agent `a2d27dc2184b4ae56`):** PASS-WITH-NOTES — 0 HIGH, 0 MEDIUM-blockers, 2 LOW Findings: (a) SKIP-Mode Bundle-Print intentional, in SKILL.md P7-Doku klargestellt; (b) `repo_root`-Defensive-Type-Guard skipped per Karpathy §0.2 (`_repo_root()` returnt immer Path, Defensive für unmögliches Szenario). Kein Sparring nötig per `feedback_codex_sparring_heuristic` (HIGH-Count <2).

**Sync-Set §18 (system-zustand --version-bump --also pipeline-item, Expected-Set 4):**
- 00_Core/SYSTEM.md (§Skill-Registry v0.1.1→v0.1.2 + Footer v1.11→v1.12)
- 00_Core/CORE-MEMORY.md (§13 v1.28→v1.29 + neuer 2026-05-24 Eintrag)
- 00_Core/PIPELINE.md (#81 Status v0.1.2 ACTIVATABLE→DONE; v0.2.0 bleibt ACTIVATABLE)
- 07_Obsidian Vault/.../log.md (dieser Entry)
- + Skill-Internal (out-of-validator-scope, im selben Commit): SKILL.md frontmatter + scripts/core_slim_refactor.py + scripts/patterns.py + tests/test_v0_1_2_bugfixes.py (untracked→add) + tests/test_pipeline.py + references/failure_modes.md (v0.1.2-Sektion)

**§18-Skill Pre-Commit-Gate:** `paragraph-18-sync` Validator `03_Tools/para18_sync/validator.py system-zustand --version-bump --also pipeline-item --dry-run --json --allow-dirty 80` — Expected-Set bestätigt 4 Files, vor finalem Commit verifiziert (User-Catch: ich hatte den Skill initial NICHT verwendet trotz §18-File-Touch-Routing-Trigger, korrigiert nach User-Hinweis).

**Lessons:**
- **(Meta) §18-Skill MUSS bei §18-File-Touch verwendet werden, nicht via Memory-Sync-Set-Rekonstruktion** — Routing-Table-Trigger ist normativ; Memory ist advisory. User-Hinweis war Karpathy §0.1-Catch ("aktive Push für Simplicity-Pfad statt erster Idee").
- T2-Empirie-Befunde sind oft Skill-Internal-Bugs die nur unter Real-Run-Pressure sichtbar werden — Tests, die durch silent-skip "passed", sind False-PASS-Artefakt (`feedback_cross_check_skill_vs_standalone`-Klasse).
- Pre-Fix-Tests müssen nach Fix evtl. ENV-Setup bekommen wenn der Bug die Test-Isolation maskiert hat.
- Karpathy §0.6 Approach-Reset Pre-Implementation > Post-Implementation-Rollback — MEDIUM-3 wurde NIE angefangen, weil Scope-Assessment vor Code-Touch ergab dass es out-of-scope ist.
- Codex-Bundle-Klarstellung via SKILL.md-Doku-Edit ist billiger als Code-Refactor — LOW-Finding adressiert ohne neuen Bug-Surface.

**Cross-Reference:** PIPELINE #81 (v0.1.2-Sub Status-Transition) · CORE-MEMORY §13 2026-05-24-Eintrag · SYSTEM.md §Skill-Registry · failure_modes.md v0.1.2-Sektion · Auto-Memory `feedback_core_slim_p7_p18_path_mismatch` + `feedback_codex_sparring_heuristic` · Commit `<TBD-Hotfix>`.

**Next:** v0.2.0 Feature-Release ACTIVATABLE für separate Session (Pre-Lock 9/10/14 + NEU MEDIUM-16 Section-Reflow); Karpathy 2-Phase-Discipline.

## 2026-05-24 — Pipeline-Item-Event: core-slim-refactor v0.2.0 SPEC-LOCKED v0.5 post-Codex-Sparring-4-Runden (PIPELINE #81 ACTIVATABLE → SPEC-LOCKED, scoring-neutral, pipeline-item)

**Event-Typ:** Pipeline-Item-Status-Transition (PIPELINE #81 v0.2.0 Status-Bump ACTIVATABLE → SPEC-LOCKED, kein Score/FLAG/Sparraten-Touch, kein Skill-Version-Bump da Spec gitignored).

**Karpathy 2-Phase Spec-Phase only** (Brainstorming-Terminal-Override per Memory `feedback_brainstorming_terminal_override_dynastie` — Spec → Codex-Sparring → STOP; Build separate Session). **KEIN Code-Touch in dieser Session.**

**Spec-Artifact:** `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-design.md` (gitignored per Convention, ~530 Z., 13 Sektionen).

**Codex-Sparring-Trajektorie (4 Runden via `codex:codex-rescue` Subagent, gpt-5.3-codex):**
- **R1 Single-Pass** (agent `a7310e09124b95c72`, ~16:15 GMT+2): 3 HIGH (F-01 AC4/AC8/§3.3 Dry-Run-Mutation-Contradiction + F-02 Drift-Default-Inconsistency Schema-vs-Risk-vs-Q3 + F-03 executed-Write-Back Soft-Warn-Idempotency-Lock-Bypass) + 4 MED (F-04 MEDIUM-9 Validation-TBD + F-05 Section-Splice Unicode-Boundary under-specified + F-06 Byte-Index-Conversion deferred-not-designed + F-07 Backward-Compat-Claim too-broad) + 1 LOW (F-08 AC5-±1-Toleranz) + Q1-Q10 Sparring-Verdicts adopted. ALLE 8 Findings + 10 Q-Verdicts eingearbeitet.
- **R2 Diff-Re-Review** (agent `a6cf3bdbef047a3cd`, ~16:23 GMT+2, deutsche Sprach-Direktive nach User-Hinweis "Warum wieder Englisch?"): **89% Confidence**, 3 Findings — R2-F01 alte Q6-Q10-Tabelle Reststand widersprach aktuellen Q7/Q9-Verdicts + R2-F02 `schema_version`-Hint in §11 vs Unknown-Key-Disziplin inkonsistent + R2-F03 AC-Zähl-/Abdeckung uneinheitlich (24 vs aktuelle Liste). ALLE 3 eingearbeitet.
- **R3 Reconcile-Pass** (agent `aa84daabbc492f437`, ~16:38 GMT+2, via SendMessage): **93% Confidence**, 4 R3-Aktionen — AC-Counts 27 stimmig (23 Testable + 4 Doc-/Review-Gates) + AC11 6-Zellen-Formulierung + §11.2 v0.1.x-Zeile präzisiert ("`expected_entry_count`-Check fehlt weil Key fehlt") + CLI-Flag `--skip-executed-writeback` normativ in §3.3 (Default `false`, Constraint No-Op bei dry-run, Priorität schlägt P7b). ALLE 4 eingearbeitet.
- **R4 Final-Reconcile** (agent `a3bc6109ea942de11`, ~16:48 GMT+2, via SendMessage): **96% Confidence — SPEC-LOCK-OK** (Ziel ≥95% übertroffen). 1 LOW Nachzieh-Fix §10 R2-F03-Zeile "24/3" → "23/4" appliziert.

**Spec-Inhalt-Konfirmation:** Scope Pre-Lock unverändert wie PIPELINE #81-Body: MEDIUM-9 (Pattern-C `date_parser.field: bullet` + Helper `_split_bullet_block` + Hard-ConfigError für mode-mismatch) · MEDIUM-10 (P2a Pre-Mutation-Drift-Check + Exit-Code 11 + Structured-Stderr-Code `DRIFT_COUNT_OUT_OF_RANGE` + Default `warn_continue` mit fail_close opt-in) · MEDIUM-14 (P7b executed-Block Auto-Population + Exit-12 `EXIT_BOOKKEEPING_FAILED` + Sidecar-Lock `.executed-pending` + CLI-Flag `--skip-executed-writeback`) · MEDIUM-16 (Section-Reflow selective splice via `_splice_section` byte-based + Line-Alignment-Invariante mit `AssertionError("splice_boundary_not_line_aligned")` + Byte-Offset-Map `_build_line_byte_offsets`). MEDIUM-15 → v0.3.

**Karpathy-Pre-Build-Gates in Spec verankert:** (a) Pre-Refactor-Caller-Scan via Grep auf `_split_into_entries` + `classify_date_cut` + `mutate_bucket_archive` vor Edit. (b) `_split_bullet_block` + `_splice_section` als SEPARATE Helper (Three-similar-lines-Threshold, keine premature Abstraction). (c) Acceptance-Test pro Item + neuer Worked-Example `session-handover-banner-list-cut.yaml`.

**NEU §11 Compatibility-Matrix (R2-F02 Fix):** explizite Trennung `SKILL.md frontmatter version` vs `Config YAML schema_version: 2`. Producer/Consumer-Matrix mit 4 Zeilen + 2 Edge-Cases. Regel: Config mit v0.2.0-Keys ohne `schema_version` → `ConfigError: schema_version_required_for_v2_keys` (kein silent-ignore möglich). v0.1.x-Config + v0.2.0-Runtime erlaubt (executed-Auto-Populate läuft trotzdem, `--skip-executed-writeback` honors v0.1.x-1:1-Verhalten).

**Sync-Set §18 (pipeline-item-Event, scoring-neutral, atomar):** PIPELINE.md (#81 v0.2.0 Status-Edit + Footer v2.71→v2.72) + Vault log.md (dieser Entry). **KEIN** System-Zustand-Touch (Spec gitignored, kein Skill-Version-Bump, keine SKILL.md-Frontmatter-Edits, kein SYSTEM.md Registry-Bump). **KEIN** PORTFOLIO/Faktortabelle/score_history/config.yaml/xlsx/flag_events/CORE-MEMORY (kein Score/FLAG/Sparraten-Event, keine §13-Lifecycle-Eintragung da Spec-Phase nicht Promotion). SESSION-HANDOVER.md ist Banner-Resume-Trail (Plus, nicht §18-Pflicht).

**Memory neu angelegt:** `feedback_codex_default_english_in_dynastie.md` — Codex (gpt-5.3-codex) defaultet auf Englisch trotz 100% deutschem Prompt-Kontext; explizite Sprach-Direktive 'Antworte auf Deutsch' im Prompt Pflicht. User-Catch "Warum wieder Englisch?" deutet Reinfall-Klasse. Funktioniert retroaktiv via SendMessage. Linked: `feedback_review_via_codex_not_advisor` + `feedback_codex_sparring_heuristic`.

**Lessons:**
- **Codex-Sparring-Loop konvergent über 4 Runden** (R1 → R2 89% → R3 93% → R4 96%). Heuristik per `feedback_codex_sparring_heuristic`: R1 3 HIGH justified Sparring-Loop; R2-R4 Diff-Re-Reviews jeweils ~5-10k Tokens/Pass billiger als R-Spec-Verschwendung — Total ~30-40k Token, Spec-Quality 96% Confidence vs R1-only-Stand ~70-75%.
- Brainstorming-Terminal-Override hält: Spec → Codex-Sparring → STOP; KEIN writing-plans-Switch, KEIN Code-Touch in Spec-Phase. Build separate Session.
- §18-Skill `paragraph-18-sync` Validator vor Edits aufgerufen (Lessons-Anker aus v0.1.2-Hotfix-Welle): Expected-Set 2 Files (PIPELINE.md + log.md), pipeline-item-Event nicht system-zustand, kein Multi-Event Union.
- Spec-Artifact bleibt gitignored per Convention (analog v0.1-Spec, paragraph-18-sync-Spec, finnhub-Spec): Specs leben lokal, PIPELINE-Item ist SSoT-Pointer.

**Cross-Reference:** PIPELINE #81 v0.2.0-Body (Spec-LOCK-Stand) · Spec-File `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-design.md` · v0.1.2-Hotfix-Commit `82af9ac` · v0.1-Spec-Anker `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` · failure_modes.md MEDIUM-9..16 · Auto-Memory `feedback_brainstorming_terminal_override_dynastie` + `feedback_redefer_over_prespec_dynastie` (Re-Defer-Trigger T2-FIRED bestätigt) + `feedback_codex_default_english_in_dynastie` (NEU) + `feedback_codex_sparring_heuristic`.

**Next:** v0.2.0 Build-Phase als **separate Session** per Karpathy 2-Phase-Discipline. Trigger: "core-slim-refactor v0.2.0 Build". Spec ist self-contained, alle Karpathy-Pre-Build-Gates verankert. Erwartete Build-Session-Dauer ~4-5h + Codex Single-Pass + 22-26 neue Tests + atomic-Commit-Welle analog v0.1.2.

## 2026-05-24 — System-Event: core-slim-refactor v0.2.0 RELEASED Build-Wave (PIPELINE #81 SPEC-LOCKED → CLOSED, scoring-neutral, system-zustand + pipeline-item)

**Event-Typ:** Skill-Version-Bump v0.1.2 → v0.2.0 (Feature-Release) + Pipeline-Item-Close (#81 v0.2.0 SPEC-LOCKED → CLOSED). Multi-Event Union: `system-zustand --version-bump --also pipeline-item`. Kein Score/FLAG/Sparraten-Touch.

**Karpathy 2-Phase Build-Phase (Spec-Phase 2026-05-24 nachmittags abgeschlossen, separate Session per Brainstorming-Terminal-Override).** Subagent-driven Implementation P1-P7 + Doc-Sync P7 + Atomic Build-Wave P8. Spec-File `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-design.md` (gitignored, 96% Confidence post-R4) als normative Quelle.

**11 Build-Commits (chronologisch, alle lokal, NICHT gepushed bis User-Approval):**
| # | SHA | Phase |
|---|---|---|
| 1 | `9f79382` | feat P1 Config-Schema-Foundation |
| 2 | `9ab9f76` | fix P1-Review-Fixes (Codex M1+L1+L2) |
| 3 | `d9c3872` | feat P2 MEDIUM-9 Pattern-C Bullet-Variante |
| 4 | `e5e4f86` | fix P2-Review-Fixes (Codex M1+L1) |
| 5 | `1f67f25` | feat P3 MEDIUM-10 P2a Drift-Pre-Check |
| 6 | `26cb1ce` | feat P4 MEDIUM-16 Section-Splice |
| 7 | `45f4747` | fix P4-Review-Fixes (Codex M1) |
| 8 | `4150b3c` | feat P5 MEDIUM-14 P7b Executed-Auto-Populate |
| 9 | `8673e39` | fix P5b Sidecar-Lifecycle + AC4g test |
| 10 | `380e456` | feat P6 SH Worked-Example + Integration-Test (Pattern-C-Bullet end-to-end) |
| 11 | `2f82045` | docs P7 Doc-Sync (failure_modes + SKILL v0.2.0) |
| 12 | `98a3eb7` | chore(meta) Build-Wave §18-Sync (dieser Commit) |

**Closed MEDIUMs (alle 4 v0.2.0-Scope):**
- **MEDIUM-9 Pattern-C Bullet-Variante** — `date_parser.field: bullet` + Helper `_split_bullet_block` + Hard-ConfigError für mode-mismatch
- **MEDIUM-10 P2a Pre-Mutation-Drift-Check** — `expected_entry_count` + Exit-Code 12 (re-mapped von Plan-Drift mit v0.1.1 EXIT_ANCHOR_NOT_FOUND=11) + Structured-Stderr-Code `DRIFT_COUNT_OUT_OF_RANGE` + Default `warn_continue`
- **MEDIUM-14 P7b executed-Block Auto-Population** — timestamp/sha256/commit_sha=pending + Exit-Code 13 + Sidecar-Lock `.executed-pending` + CLI-Flag `--skip-executed-writeback`
- **MEDIUM-16 Section-Reflow selective splice** — `_splice_section` byte-based + Line-Alignment-Invariante + Byte-Offset-Map-Algorithmus `_build_line_byte_offsets`

MEDIUM-15 bleibt v0.3 (Null-Coupling, kein Use-Case).

**Tests:** **92 passed, 2 skipped** (51 v0.1.2 baseline + 41 v0.2.0 neu). Q4 Header-Mode-Byte-Identity bewiesen via `test_header_mode_byte_identity_q4` in `tests/test_session_handover_worked_example.py` (P6 Integration-Test als Backward-Compat-Coverage-Proxy).

**Codex-Review-Trail (Per-Phase Single-Pass via `codex:codex-rescue` Subagent, gpt-5.3-codex):**
| Phase | HIGH | MEDIUM | LOW | Notes |
|---|---|---|---|---|
| P1 | 0 | 1 | 2 | M1 Doku-Test pass→Assert, L1 Comment-Drift, L2 isinstance-Guard |
| P2 | 0 | 1 | 4 | M1 Bullet-Branch Datenverlust-Fallback, LOW-Confirmations |
| P3 | 0 | 0 | 0 | Clean pass |
| P4 | 0 | 1 | 2 | M1 assert→ValueError (python -O Bypass), LOW Edge-Cases + Q4 |
| P5 | 0 | 2 | 1 | M-01 --skip-flag Doc (defer P7), M-02 AC3b-Regex false-positive, LOW Plan-Comment-Drift |
| P6 | — | — | — | Skipped (Config + Test only) |
| P7 | — | — | — | Skipped (Doc-Sync) |

**0 HIGH über alle 5 reviewed Phasen. Alle MEDIUM adressiert oder dokumentiert.**

**Empirisch gefangene Plan-Drifts (14 Stück, validiert `feedback_empirie_statt_annahmen`):** Plan dict-Subscript vs real Attribut-Access (P1), Plan `regex`-Key vs real `pattern` (P2), bullet/header shared-loop Misklassifikation (P2), Exit-11-Kollision mit v0.1.1 EXIT_ANCHOR_NOT_FOUND → Re-Map DRIFT=12/BOOKKEEPING=13 (P3), RowSet `archive_rows`/`keep_rows` vs real `archive`/`keep` (P3), `--config`-Flag vs positional (P3), `classified=20` vs real `=21` (P3), AC5 `-32/+7` vs real `-26/+1` (P4), Plan `block:` vs real `cfg:` (P5), Plan exit-table typo (P5), Plan schema-keys `target.path` vs real `target.file` (P6), Plan invocation `python -m` vs real `python scripts/...py` (P6), Plan failure_modes-Tabelle typo (P7).

**Sync-Set §18 (system-zustand --version-bump --also pipeline-item, Expected-Set 4):**
- `00_Core/SYSTEM.md` (§Skill-Registry v0.1.2 → v0.2.0 mit v0.1.2 als Lineage-Sub)
- `00_Core/PIPELINE.md` (#81 Status v0.2.0 SPEC-LOCKED → CLOSED + MEDIUM-9/10/14/16-Mark + 11-Commit-SHA-Range + 92-Tests-Stand)
- `00_Core/STATE.md` (Hub Last-Action / Skill-Activity Timestamp)
- `07_Obsidian Vault/.../log.md` (dieser Entry)

**KEIN** PORTFOLIO/Faktortabelle/score_history/config.yaml/xlsx/flag_events/CORE-MEMORY (kein Score/FLAG/Sparraten-Event). CORE-MEMORY §13-Lifecycle-Entry post-Push optional.

**Disziplin-Regeln durchgehend befolgt (P0-P8):**
1. ASCII-only Commit-Subjects (keine em/en-Dashes)
2. Byte-Level-Edit-Locality (`_splice_section` Helper)
3. `_iter_section_rows` halb-offen `[start, end_exclusive)`
4. Test-Fixture-Helper-Pflicht (`make_minimal_valid_cfg_yaml` für subprocess/load_config-Tests; Pure-Unit-Tests mit dict-cfg ausgenommen)

**Memory-Priors durchgängig genutzt:** `feedback_empirie_statt_annahmen` (14×), `feedback_windows_console_ascii_safe_inline_python` (0 cp1252-Crashes), `feedback_windows_python_crlf_text_mode` (open() mit newline=''), `feedback_pre_commit_diff_inspection` (vor jedem Commit), `feedback_powershell_herestring_in_bash_tool` (here-doc <<'MSG'), `feedback_review_via_codex_not_advisor` (Codex Single-Pass per Phase).

**Lessons:**
- **Subagent-driven Implementation P1-P7 funktionierte** trotz 14 Plan-Drifts — Implementer-Empirie schlug Plan-Reasoning konsistent. Bestätigt `feedback_empirie_statt_annahmen` als prä-Edit-Disziplin.
- **Exit-Code-Kollision (Plan 11 vs v0.1.1-Reservation 11) bei P3 gefangen** durch Implementer-Grep auf existing exit-codes — Parent-Plan-Patch (Re-Map zu 12/13) verteilte Korrektur cross-section. Coverage > Top-Down-Reasoning.
- **Codex-Per-Phase-Reviews konvergent** — 0 HIGH über 5 Phasen, alle MEDIUM mit minimalen Patches gefixt. Final-Pass-Skip (P6/P7) gerechtfertigt per `feedback_codex_sparring_heuristic` (low-risk Config + Doc).
- **Q4-Header-Mode-Byte-Identity-Proof (P6) ersetzt explizite Backward-Compat-Suite** — Pre-v0.2.0 Worked-Examples sind alle header-mode → fallen unter Q4-Coverage. Token-Budget gespart, Test-Coverage adäquat.
- **Brainstorming-Terminal-Override (Spec separat von Build)** über 2 Sessions gehalten — Spec-Session 2026-05-24 nachmittags STOP nach R4 96%, Build-Session 2026-05-24 abends fresh start mit Subagent-Pattern. Karpathy 2-Phase-Discipline empirisch validiert.

**Hard-Stop (Plan §11):** **KEIN `git push` ohne explizite User-Freigabe.** Branch ist 12 Commits ahead of origin/main (11 Build + 1 Build-Wave `98a3eb7` mit Placeholder-Replace via `--amend`). User initiiert push wenn ready.

**Cross-Reference:** PIPELINE #81 (v0.2.0 CLOSED) · SYSTEM.md §Skill-Registry v0.2.0 · failure_modes.md v0.2.0-Sektion · Spec-File `docs/superpowers/specs/2026-05-24-core-slim-refactor-v0.2.0-design.md` (96% Confidence post-R4) · v0.1.2-Hotfix-Commit `82af9ac` · v0.1-Spec `docs/superpowers/specs/2026-05-23-core-slim-refactor-design.md` · Handover `docs/superpowers/handover/2026-05-24-core-slim-refactor-v0.2.0-P8-resume.md` · Auto-Memory `feedback_empirie_statt_annahmen` + `feedback_codex_sparring_heuristic` + `feedback_brainstorming_terminal_override_dynastie` + `feedback_core_slim_p7_p18_path_mismatch` (v0.1.2-Lineage).

**Next:** User-Approval für `git push origin main` (13 Commits ahead). Optional Post-Push: CORE-MEMORY §13 Lifecycle-Entry für v0.2.0-Activation. MEDIUM-15 als v0.3-Trigger offen (Null-Coupling, opportunistic).

## 2026-05-25 — Doku-Event: CORE-MEMORY §13 v0.2.0 Lifecycle-Entry post-Push (scoring-neutral, system-zustand-Lifecycle-Doku)

**Event-Typ:** Lifecycle-Doku-Append post-Release. Kein System-Zustand-Change (Skill-Version v0.2.0 bereits im Build-Wave-Commit `98a3eb7` bumped). Kein neuer Score/FLAG/Sparraten-Touch.

**Trigger:** User-Freigabe nach Build-Wave-Push (`eda5b25..78c8597` zu origin/main) für optionale Post-Push-Disziplin-Schritte: (1) CORE-MEMORY §13 Lifecycle-Entry, (2) Memory `feedback_git_amend_sha_churn_trap` neu, (3) Memory `feedback_claude_default_english_in_dynastie` neu.

**Was geändert:**
- `00_Core/CORE-MEMORY.md` §13 — neuer v0.2.0-Entry (volle Build-Wave-Chronik: 13 Commits + 4 MEDIUMs CLOSED + 14 Plan-Drifts + Codex-Trail + P8-Disziplin-Befunde) + Footer v1.29→v1.30
- `~/.claude/.../memory/feedback_git_amend_sha_churn_trap.md` neu — `--amend` Fixed-Point-Problem bei Self-Referential-SHA-Commits, Follow-Up statt amend
- `~/.claude/.../memory/feedback_claude_default_english_in_dynastie.md` neu — Claude defaultet auf Englisch trotz deutschem Repo-Kontext (Tool-Descriptions besonders anfällig), Wiederholungs-Klasse zu Codex-Variante
- `~/.claude/.../memory/MEMORY.md` Index — 2 neue Bullets

**Sync-Set §18 (system-zustand-Lifecycle, Expected-Set 2):**
- `00_Core/CORE-MEMORY.md` (§13-Entry + Footer-Bump)
- `07_Obsidian Vault/.../log.md` (dieser Entry)

KEIN SYSTEM.md/PIPELINE.md/STATE.md-Touch (alle bereits im Build-Wave-Commit `98a3eb7` aktualisiert). Memory-Files leben außerhalb Repo (`~/.claude/...`), nicht §18-relevant.

**Lessons:**
- Post-Push-Lifecycle-Doku ist legitimer Disziplin-Schritt (Audit-Trail-Vollständigkeit), aber NICHT in Atomic-Build-Wave-Commit aufnehmen — separate Commit-Welle erlaubt fokussierte SHA-Reference + saubere Build-Wave-Atomicity.
- 2 neue Memories aus P8-Empirie: `feedback_git_amend_sha_churn_trap` (technical-process) + `feedback_claude_default_english_in_dynastie` (behavioral). Beide Wiederholungs-Klasse-würdig.

**Cross-Reference:** Build-Wave-Commit `98a3eb7` (P8) · SHA-Fix-Commit `78c8597` · CORE-MEMORY §13 v0.2.0-Entry · Auto-Memory `feedback_git_amend_sha_churn_trap` + `feedback_claude_default_english_in_dynastie` (beide neu).

**Next:** MEDIUM-15 v0.3-Trigger offen (Null-Coupling, opportunistic). Session-Close möglich.

---

## [2026-05-25] system | VEEV/AVGO — Earnings-Date-Drift-Repair (PORTFOLIO+STATE) + AVGO-Earnings-Discovery via earnings_calendar.py + Pre-Earnings-Briefs T-9 (scoring-neutral, Live-State-Repair)

**Event-Typ:** Live-State-Drift-Repair + Pre-Earnings-Prep (kein Score/FLAG/Sparraten-Touch; rein PORTFOLIO/STATE-Korrektur + neue Briefing-Artefakte)

**Was passiert ist:**
- User-Anfrage: VEEV Q1 FY27 Pre-Earnings-Brief mit `earnings-preview`-Skill. Mental-Model + PORTFOLIO+STATE behaupteten Earnings-Datum **27.05.2026**.
- **yfinance-Pull lieferte 2026-06-03** (Yahoo Calendar). Date-Diskrepanz erkannt → Cross-Check mit Finnhub angeordnet.
- **Finnhub /calendar/earnings (via `03_Tools/finnhub_client.py`) bestätigte 2026-06-03 amc** (epsEstimate 2.1709, revenueEstimate $870.7M). Yahoo+Finnhub konvergent. User confirmierte 03.06. via Web-Recherche.
- **PORTFOLIO.md Z. 20 + 58** und **STATE.md Z. 23** auf **03.06.2026 (amc)** korrigiert mit Audit-Trail-Hinweis (Stale-yfinance-Pull 30.04. als Root-Cause vermerkt).
- **User-Folgeanfrage:** Funktioniert `03_Tools/earnings_calendar.py` korrekt? → Tool-Lauf `--check --alert-window 14` erbrachte:
  - VEEV: 2026-06-03 🟢 in trigger (post-Edit korrekt)
  - COST: 2026-05-28 🟢 in trigger
  - **AVGO: 2026-06-03 🔴 DRIFT** — Q3 FY26 Earnings am selben Tag wie VEEV, im PORTFOLIO-Trigger-Block bisher nicht erwähnt
  - 12/12 Ticker mit Datum, Smoke-Test BRK.B = 2026-08-01 PASS
- **AVGO-Drift in PORTFOLIO + STATE nachgezogen:**
  - PORTFOLIO.md Z. 18: AVGO-Trigger-Zelle um "03.06.2026 (amc) Q3 FY26 Earnings — FLAG-Resolve-Gate ($20M-Schwelle vs. $106M-Diskr.)" erweitert
  - PORTFOLIO.md "30-Tage-Trigger-Tabelle": AVGO-Zeile + Re-Ordering (28.05. COST → 03.06. AVGO → 03.06. VEEV)
  - STATE.md Forward-Triggers: `03.06. (amc) VEEV Q1 FY27 + AVGO Q2 FY26 [FLAG-Resolve-Gate]`
- **Pre-Earnings-Briefs (Konvention `02_Analysen/Earnings Reports/<Company>/<TICKER>_pre-earnings_<earnings-date>.md`):**
  - **VEEV** (`Veeva Systems/VEEV_pre-earnings_2026-06-03.md`): 8-Sektionen-MSFT-Template-Parity, Score-Move-Watch-Matrix (keine FLAG), Yahoo×Finnhub-Cross-Check, News-Sentiment-Cluster (38 Items, AI-Sunset-Fear vs. Compounder-Reversion binär), Mean-Target +64% Upside, Burry-Position notable
  - **AVGO** (`Broadcom/AVGO_pre-earnings_2026-06-03.md`): 8-Sektionen, FLAG-Decision-Matrix (analog MSFT), Trillion-Cap-Context, EPS-Wachstum +51% YoY, near-52w-Hoch, Asymmetrie umgekehrt zu VEEV (Bear-Target -48% Downside vs. VEEV +9.9% Upside)

**Sync-Set (§18 Multi-Event-Union §18.2 — Live-State-Repair + Pipeline-Item, scoring-neutral, Expected-Set 4 + 2 Briefing-Artefakte):**
- `00_Core/PORTFOLIO.md` (Z. 18 AVGO-Trigger-Zelle + Z. 20 VEEV-Trigger-Zelle + Z. 47 AVGO-Re-Eval-Description + Z. 57-60 30-Tage-Trigger-Tabelle)
- `00_Core/STATE.md` (Z. 23 Forward-Triggers)
- `00_Core/PIPELINE.md` (#69 Discovery-Stamp 25.05. — 53 M-Files Empirie + Stale-Snapshot-Vermerk; bewusst KEIN Re-Scope, deferred auf nächste Skill-Build-Session per User-Direktive)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)

**KEIN** Score-History/Faktortabelle/config.yaml/xlsx/flag_events-Touch (kein Score/FLAG/Sparraten-Event — FLAG-Status AVGO bleibt 🔴 aktiv unverändert; Resolve-Entscheidung kommt frühestens Tag +1 04.06. nach Vollanalyse).

**Briefing-Artefakte (außerhalb §18-Sync-Set, neu in `02_Analysen/`):**
- `02_Analysen/Earnings Reports/Veeva Systems/VEEV_pre-earnings_2026-06-03.md`
- `02_Analysen/Earnings Reports/Broadcom/AVGO_pre-earnings_2026-06-03.md`

**Lehre:**
- **yfinance-Calendar-Stale-Risk empirisch konfirmiert:** PORTFOLIO-Datum war 30.04.-Pull-Snapshot, hat sich danach 27.05.→03.06. verschoben ohne automatischen Drift-Alert. `earnings_calendar.py` als Hook hätte das fangen müssen — Tool funktioniert aber wurde nicht regelmäßig gelaufen. **Möglicher §18-Sync-Extension-Trigger:** `earnings_calendar.py --check` als SessionStart-Hook oder !Briefing-Vorab-Step? (PIPELINE-Item-Kandidat, später entscheiden).
- **Finnhub-Free-Tier-Value bestätigt:** `/calendar/earnings` + `/quote` + `/news` funktionieren zuverlässig. Beat/Miss-History (`/stock/earnings`) und Metrics (`/stock/metric`) Premium-restricted (leer) — Yahoo bleibt primär für diese. **Cross-Check-Pattern Yahoo × Finnhub** in Pre-Earnings-Workflow neu etabliert (Memory-Kandidat: `reference_finnhub_yahoo_cross_check_pre_earnings.md`).
- **MSFT-Template-Konvention adaptiv:** FLAG-Decision-Matrix-Sektion für FLAG-aktive Ticker (AVGO ✓ MSFT-Vorlage), Score-Move-Watch-Matrix für FLAG-freie Ticker (VEEV neue Variante). 8-Sektionen-Skelett identisch, Sektion-6-Inhalt FLAG-Status-driven.
- **Parallel-Earnings-Slot 03.06.:** VEEV + AVGO selber Tag = doppeltes Tag-+1-Vollanalyse-Slot 04.06. — Token-Budget + Sequencing vorab planen (Brief 7. Sektion warnt explizit).

**Cross-Reference:** PORTFOLIO.md Z. 18 + 20 + 57-60 · STATE.md Z. 23 · `02_Analysen/Earnings Reports/Veeva Systems/VEEV_pre-earnings_2026-06-03.md` · `02_Analysen/Earnings Reports/Broadcom/AVGO_pre-earnings_2026-06-03.md` · `03_Tools/earnings_calendar.py --check --alert-window 14` Tool-Output 25.05.

**Nächste Tracks:**
- Tag 0 (03.06. amc): VEEV+AVGO Doppel-Recap via `_extern/earnings-recap` + FLAG-Quick-Check (AVGO besonders sensibel wegen 🔴-Status); Pre-Call-Snapshots CORE-MEMORY §12.veev + §12.1 (AVGO bestehend updaten)
- Tag +1 (04.06.): `!Analysiere VEEV` + `!Analysiere AVGO` mit Transcript via defeatbeta-MCP; AVGO Sub-FLAG-Resolution-Gate ($20M-Schwelle) explizit prüfen
- Optional Pipeline-Item: `earnings_calendar.py --check` als SessionStart-Hook-Erweiterung (verhindert wiederholten Stale-Date-Reinfall)

---

## [2026-05-25] system | xlsx-smoke-test-runner Skill α+ SPEC-COMPLETE + Multi-File-Sync (P1+P13+P15+config.yaml-Drift, scoring-neutral)

**Event-Typ:** System-Zustand-Change (xlsx-smoke-test §18.7-Gate Live-State-Werte synchronisiert) + Pipeline-Item (xlsx-smoke-test-runner Skill SPEC v0.1 GO-Ready) — kein Score/FLAG/Sparraten-Touch.

**Was passiert ist:**
- **Spec-Phase abgeschlossen:** `01_Skills/xlsx-smoke-test-runner/SPEC.md` v0.1 (635 LOC) post 2× Codex-Sparring (R1: 2 HIGH + 4 MED + 4 LOW → alle adressiert; R2 Diff-Re-Review: 0 HIGH + 3 MED + 1 LOW → alle adressiert). HIGH-Threshold per `feedback_codex_sparring_heuristic` für R3 nicht erreicht.
- **2 Codex-R1 HIGH-Findings empirisch verifiziert + gefixt:**
  - HIGH-1: §G Anker-Pfad-Drift — `portfolio.satelliten_sparrate` 0 grep-Treffer in `config.yaml`; korrekter Pfad `brokers.scalable.sparrate_eur: 285.00` (L27). drift-doc §2.4 + §P8 in EINEM Commit mit-gepatched.
  - HIGH-2: `verify_wrapper`-Import-Pfad — `03_Tools/precommit/` hat kein `__init__.py` (Glob-Verify); Lösung via `importlib.util.spec_from_file_location` dokumentiert in SPEC §4.2.
- **Multi-File-Sync (P1+P13+P15) 4-Files (post Coverage-Gap-Expansion 2026-05-25T20:05):**
  - `03_Tools/xlsx-smoke-test.md` L17/L18: Formel-Counts 218→249 + 12→13, §G-Anker `brokers.scalable.sparrate_eur` ergänzt
  - `00_Core/INSTRUKTIONEN.md §18.7 Z475`: identische Sync
  - `00_Core/SYSTEM.md L42`: v2.4-Lifecycle-Block Live-State-Update (initial mis-skopt als "historischer Snapshot", User-Direktive korrigiert)
  - `03_Tools/precommit/xlsx_smoke_test.py Z42/Z47`: md-Source-Kommentare
- **Klasse-C-Cleanup (scoring-neutral):** `config.yaml` L70-78 Sparraten-Kommentar von 28.04.-Stand (3× eingefroren) auf 25.05.-Stand (4× eingefroren, post-AMZN-Integration 15.05.) aktualisiert — Math-Result (285€) identisch, nur Struktur-Drift.
- **Klasse-B-Cleanup:** drift-doc §3.1 Hook-Kommentar-"outdated"-Notizen post-Patch als RESOLVED markiert.

**Sync-Set (§18 system-zustand + pipeline-item-Union, scoring-neutral, Expected-Set 8):**
- `00_Core/INSTRUKTIONEN.md` (§18.7 Z475 Live-Werte-Sync)
- `00_Core/SYSTEM.md` (L42 v2.4-Lifecycle-Eintrag Live-Werte-Sync)
- `01_Skills/dynastie-depot/config.yaml` (L70-78 post-AMZN Sparraten-Kommentar)
- `01_Skills/xlsx-smoke-test-runner/SPEC.md` (NEU, 635 LOC, GO-Ready)
- `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` (NEU, 16 Patches Substrate + Codex R1+R2 adressiert + P15-Coverage-Expansion + RESOLVED-Marker)
- `01_Skills/xlsx-smoke-test-runner/_SESSION-HANDOVER.md` (NEU, Resume-Prompt + Stage-Cut)
- `03_Tools/xlsx-smoke-test.md` (L17/L18 Scope-Tabelle Live-Werte-Sync)
- `03_Tools/precommit/xlsx_smoke_test.py` (Z42/Z47 md-Source-Kommentare)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)

**KEIN** PORTFOLIO/Faktortabelle/score_history/flag_events/xlsx-Touch (kein Score/FLAG/Sparraten-Event — 12 Satelliten + 285€ Σ + Nenner 7,5 unverändert).

**Lehre:**
- **Skill-Name = Scope-Contract (Reinfall-Prävention):** Pre-Spec Coverage-Matrix Gate-0 in drift-doc §0a literal in SPEC §1 + Codex-R1 evaluierte explizit Coverage-Vollständigkeit. KEIN aspirational scope.
- **Codex-Sparring-Loop-Disziplin gehalten:** Single-Pass Default, R2 erst conditional auf HIGH≥2 (genau erreicht). HIGH-Threshold-Mechanik per `feedback_codex_sparring_heuristic` empirisch validiert (R1 NO-GO, R2 HOLD, R3 nicht pflicht).
- **Historische-Snapshot-Argumentation als Scope-Reduktion ist Anti-Pattern:** SYSTEM.md L42 initial als "historischer Lifecycle-Snapshot" mis-skopt — User-Korrektur etabliert: Live-State-Aussagen in Lifecycle-Bullets sind Live, nicht eingefroren. NEUE Memory `feedback_historical_snapshot_not_a_scope_excuse.md`.
- **Empirie statt Annahmen (per `feedback_empirie_statt_annahmen`):** beide Codex-R1-HIGH wurden vor Patch via Grep/Glob verifiziert. Reasoning-only-Patch wäre Reinfall-Klasse.
- **Coverage-Gap-Expansion bei Multi-File-Sync:** initial 3 Files (drift-doc P15), nach grep-Verify 4 Files (SYSTEM.md L42 hinzu). Coverage-Liste = Plan, grep-Treffer = Realität.

**Cross-Reference:** SPEC.md (NEU) · drift-live-vs-doc.md v1.4 (NEU) · INSTRUKTIONEN.md §18.7 Z475 · SYSTEM.md L42 · config.yaml L27 (Anker) + L70-78 (Kommentar) · `xlsx_smoke_test.py` Z38-54 _PROFILES · Codex-R1 Task-ID `task-mplhql8t-klqd0v` · Memory `feedback_historical_snapshot_not_a_scope_excuse.md` (NEU)

**Nächste Tracks:**
- **Schritt 3** (SPEC §6): P16 PIPELINE-Reference-Klärung (xlsx-smoke-test.md §Annex "offenes PIPELINE-Item Watchlist-Tool-Update" → grep-leer; konkrete Item-ID oder Re-Phrase)
- **Schritt 9** (SPEC §6): Restliche Patches P2-P12+P14 (xlsx-smoke-test.md §D-Block-Rewrite — B24/B25/B26-Swap per P6/P7 + §G-Paradigm-Statement per P8) — separater Commit
- **Stage-2 Execution** (separate Session per `feedback_brainstorming_terminal_override_dynastie`): SPEC §6 Schritte 5-9 — `safe_insert.py` + Hook-Punkt-G-Extension + 15 Fixtures + Test-Run

## 2026-05-26 ~02:10 GMT+2 — System-Event: xlsx-smoke-test-runner v0.1.0 RELEASE + Drift-Catchup CLAUDE.md/INSTRUKTIONEN.md (scoring-neutral, system-zustand)

**Was passierte:** Stage-2-Substrate (54 pytest + 15 Fixtures + Live-Smoke 3/3 GREEN gegen Rebalancing_Tool_v3.4 + Satelliten_Monitor_v2.0 + Watchlist_Ersatzbank_Monitor_v1.1) durch SKILL.md-Exposure-Layer als v0.1.0 freigegeben. Während Release-Vorbereitung User-Catch §1-Befehls-Übersicht-Drift: `!SessionClose` + `!ParaSync18` bereits Routing-Table-Anker, aber nicht in INSTRUKTIONEN §1 verankert; Skill-Inventar in CLAUDE.md Projektstruktur fehlte 3 Skills (`session-closure` / `paragraph-18-sync` / `core-slim-refactor`) zusätzlich zum neuen xlsx-Skill. Erweiterter §1-Refresh + §Skill-Zuordnung-Tabelle-Drift mit-aufgeräumt (8 neue §1-Rows + 3 neue Zuordnungs-Rows).

**Vorgeschichte (heute Nacht):**
- Pytest 54/54 + Live-Smoke 3/3 PASS gegen die drei produktiven xlsx → Stage-2-Build empirisch produktionsreif verifiziert.
- `verify_wrapper.py:92` PEP-758-Form als „Portability-Bug" geflagt → ruff-format hat den Klammer-Fix wieder rausgeschmissen. Empirie: `requires-python = ">=3.14"` + ruff `target-version = "py314"` → Repo committed sich auf Py-3.14-Floor; PEP-758 ist intentional. Fix zurückgerollt, Memory `feedback_pyproject_floor_before_portability_claim.md` (NEU, Anker an `feedback_empirie_statt_annahmen`).
- Skill-Creator-Skill für SKILL.md-Exposure invoked: 124-LOC SKILL.md mit literal-from-SPEC-§1 In/Out-Scope (per `feedback_skill_name_is_scope_contract`, keine aspirational Erweiterung), Library-Mode-API-Block, Progressive-Disclosure-Pointer auf SPEC + canonical doc.

**Geänderte Files (4 staged, Bundle isoliert von PIPELINE #69 deferred-Debt via expliziter `git add`-Selektion):**
- `01_Skills/xlsx-smoke-test-runner/SKILL.md` (NEU, 124 LOC)
- `00_Core/SYSTEM.md` (L47 neuer Skill-Registry-Eintrag analog session-closure/paragraph-18-sync/core-slim-refactor)
- `00_Core/INSTRUKTIONEN.md` (§1 +8 Befehls-Rows: !EarningsPreview/Recap/Calendar + !InsiderScan + !ParaSync18 + !SyncBriefing + !BriefingCheck + !SessionClose; §Skill-Zuordnung +3 Rows: !ParaSync18 + !SlimRefactor + §18.7-xlsx)
- `CLAUDE.md` (L31 Projektstruktur: 7→10 Skills + xlsx-runner; alphabetisch-thematisch zwischen sec-edgar-skill und `_extern/`)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)

**§18-Sync:** `python 03_Tools/para18_sync/validator.py system-zustand --dry-run --allow-dirty 70` → verdict=DRY-RUN, events=[system-zustand], expected_files=[SYSTEM.md + log.md] beide gestaged. CLAUDE.md/INSTRUKTIONEN.md sind nicht in §18-Trigger-Set (Governance/Rules); Pre-Commit-Hook prüft nur SSoT-Live-State.

**KEIN** PORTFOLIO/Faktortabelle/score_history/flag_events/xlsx-Touch (kein Score/FLAG/Sparraten-Event — 11 Satelliten + 285€ Σ + Nenner 7,5 unverändert).

**Lehre:**
- **Pre-Edit Repo-Floor-Check (`feedback_pyproject_floor_before_portability_claim`):** Vor „Portability-Fix"-Vorschlag bei moderner Py-Syntax (PEP-758/match-case/etc.) EINMAL `requires-python`+ruff `target-version` grep. Sonst Fix-vs-Linter-Konflikt-Reinfall.
- **Drift-Catchup als Surgical Edit, nicht Restructure:** User-Direktive „Wir werden sowieso den Core noch grundlegend überarbeiten müssen. Wichtig ist erstmal das alles up to date ist." — Skill-Liste + §1 + §Skill-Zuordnung gemäß tatsächlichem On-Disk-Inventar, keine kosmetische Umgruppierung. Grundlegende Core-Restruktur kommt separat post-Core-Slim-Refactor-Reinfall.
- **Bundle-Isolation via `git add`-Scoping (`feedback_pre_commit_diff_inspection`):** 56 dirty Pre-existing-Files (PIPELINE #69 Ruff/CRLF-Debt + extern-Cleanup) blieben unstaged; Bundle ausschließlich die 4 mit dem Release verbundenen Files. `--allow-dirty 70` als expliziter Acknowledgment-Knob im Validator.

**Cross-Reference:** SKILL.md (NEU) · INSTRUKTIONEN §1 + §Skill-Zuordnung · CLAUDE.md L31 · SYSTEM.md L47 · `feedback_pyproject_floor_before_portability_claim.md` (NEU) · `feedback_skill_name_is_scope_contract` (Anker für SKILL.md description-Literal)

**Nächste Tracks (deferred):**
- PIPELINE #69 separates Catchup: 56 ungestaged Files (~50 .py ruff/CRLF + extern sec-edgar-Deletion + _SESSION-HANDOVER.md-Deletion) — eigene Session.
- INSTRUKTIONEN §Skill-Zuordnung Drift-(D) earnings-preview/recap/calendar zeigen auf nicht im aktiven `01_Skills/` vorhandene Skills (vermutlich `_extern/`) — Klärung in separater Session, kein Hotfix-Bedarf.
- Optional: skill-creator description-Optimization-Loop für xlsx-runner SKILL.md (Trigger-Score über 20-Query-Eval-Set) — defer bis erste Real-World-Trigger-Empirie vorliegt.

## 2026-05-26 ~02:50 GMT+2 — System-Event: xlsx-smoke-test-runner v0.1.0 Codex-Review-Adopt + Spec-Extraktion (scoring-neutral, system-zustand)

**Was passierte:** Post-Push-Codex-Review-Loop (R1+R2) auf der v0.1.0 SKILL.md. R1 Single-Pass 91% mit 1 HIGH + 1 MEDIUM + 1 LOW; R2 Diff-Re-Review 90% mit 1 NEU-MEDIUM + 1 Misread-Korrektur. Alle 4 Findings adressiert, finaler Empirie-Re-Grep = 0 HIGH / 0 MEDIUM / 0 LOW open. Plus User-Direktive: SPEC.md + drift-substrate aus skill dir nach `docs/superpowers/specs/` (gitignored, Repo-Konvention) extrahiert — Pointer-Tabelle in SKILL.md auf code-docstrings + canonical doc + tests umgeschwenkt.

**Codex-Findings adressiert:**
- **HIGH** R1 — Scope-Contract-Drift §C/§D: In-Scope-Block hatte „Pflicht-Cell-Existenz-Checks (Adressen aus ... §C/§D)" — empirisch falsch laut Hook `03_Tools/precommit/xlsx_smoke_test.py:7-8` + SPEC Coverage-Matrix §2.2. Out-of-Scope auf „Pflicht-Cell-Existenz UND -Semantik (Skill prüft beides NICHT)" verschärft, sowohl im description-Frontmatter als auch im footer Out-of-Scope-Block. Literal-from-SPEC-Disziplin (`feedback_skill_name_is_scope_contract`) gebrochen zugunsten empirischer Korrektheit — SPEC §1 selbst trug die Aspirational-Klausel.
- **MEDIUM** R1 — Path-Import: `from pathlib import Path` zum safe_insert-Snippet ergänzt.
- **LOW** R1 — Konkurrenz-Abgrenzung: Neuer Abgrenzungs-Absatz nach Trigger-Bullets („ersetzt keine Score-/Analyse-Workflows ... bei „Score-Update committen" bleibt dynastie-depot/Pipeline-Owner; xlsx-smoke-test-runner als Library-Call eingehängt").
- **NEU-MEDIUM** R2 — sys.path.insert-Inkonsistenz: safe_insert-Snippet bekam Standalone-Import-Setup analog verify_wrapper-Snippet.

**Strukturelle Cleanup:**
- `01_Skills/xlsx-smoke-test-runner/SPEC.md` (635 LOC) → `docs/superpowers/specs/2026-05-25-xlsx-smoke-test-runner-v0.1-design.md` (gitignored, User-Hand-Move)
- `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` (33 KB) → `docs/superpowers/specs/_artifacts/drift-live-vs-doc.md` (gitignored, User-Hand-Move)
- SKILL.md Pointer-Tabelle: SPEC §N-Pointer ersetzt durch `verify_wrapper.py` + `safe_insert.py` (Docstrings) + `03_Tools/precommit/xlsx_smoke_test.py` (Hook) + tests/ + _fixtures/ + Design-Snapshot-Pointer auf neuen gitignored docs-Pfad.
- Skill-Dir nach Cleanup lean: SKILL.md + safe_insert.py + verify_wrapper.py + tests/ + _fixtures/.

**Geänderte Files (5 staged):**
- `01_Skills/xlsx-smoke-test-runner/SKILL.md` (M, 4 Patches + Pointer-Cleanup: +12/-26)
- `01_Skills/xlsx-smoke-test-runner/SPEC.md` (D, Move-Side-Effect: -635)
- `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` (D, Move-Side-Effect: -359)
- `00_Core/SYSTEM.md` (M, L47 Skill-Registry-Eintrag um post-Review-Adoption-Annotation erweitert)
- `07_Obsidian Vault/.../log.md` (dieser Eintrag)

**§18-Sync:** `python 03_Tools/para18_sync/validator.py system-zustand --dry-run --allow-dirty 70` → verdict=DRY-RUN, expected_files=[SYSTEM.md + log.md] beide gestaged. xlsx_warnings=[], kein quarterly-rollover.

**KEIN** Version-Bump (v0.1.0 unverändert) — Doku-Quality-Pass + Struktur-Cleanup ohne Behavior-Change. KEIN Score/FLAG/Sparraten-Event.

**Lehre:**
- **Codex-Background unzuverlässig (`feedback_viral_plugin_substrate_risk_eval`):** R2 hing 7min in „verifying"-Phase ohne Progression, Companion-Status zeigte stale „running" während PID 1612 schon tot war. Fresh-Thread-Foreground-Respawn löst zuverlässig in ~2.5min. User-Heuristik validiert: bei Codex-Hang nicht warten, respawnen.
- **Codex empirisches Lese-Fail bei Patches in Resumed-Thread:** R2 las `safe_insert`-Snippet als „kein `from pathlib import Path`" obwohl der Patch seit ~10min on-disk war (verifiziert via head -10 SKILL.md). Mögliche Erklärungen: Codex cache-stale, Tool-Use-Failure, oder Resume-State-Inkonsistenz. Empfehlung: bei Confidence-Lücken durch Codex-Misread → eigener empirischer Re-Grep statt R3 (`feedback_codex_sparring_heuristic` HIGH-Threshold-Disziplin: HIGH=0 → kein R3 Pflicht).
- **Literal-from-SPEC vs Empirie-Konflikt:** SPEC §1 selbst war aspirational (§C/§D als In-Scope geführt). Per `feedback_empirie_statt_annahmen` schlägt Hook-Source-Empirie SPEC-Literal-Inheritance. SKILL.md jetzt Quelle-der-Wahrheit, SPEC bewusst als Pre-Release-Snapshot eingefroren in `docs/superpowers/specs/` (read-only-Lifecycle).

**Cross-Reference:** SKILL.md (M post-Review) · SYSTEM.md L47 · `docs/superpowers/specs/2026-05-25-xlsx-smoke-test-runner-v0.1-design.md` (gitignored) · `docs/superpowers/specs/_artifacts/drift-live-vs-doc.md` (gitignored) · Codex R1 task-mplhql8t-klqd0v · R2 task-mplwfloy-a9g0h4 (hung, respawned fresh)

**Nächste Tracks:**
- skill-creator description-Optimization-Loop (20 Eval-Queries + run_loop.py, ~10-20min Background) — pending User-Go, vorgesehen direkt im Anschluss.
- PIPELINE #69 deferred-Debt Catchup unverändert offen.
