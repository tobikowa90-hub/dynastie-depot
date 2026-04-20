# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-20 **Nacht-Spät POST-INCIDENT** (v3.0.3 Prod-Deploy SHORT-LIVED: 14:36 UTC deployed → Manual-Run FAIL mit Halluzination → **Rollback v2.1 15:13 UTC**. Prod-Cron läuft stable seit 14.04.; Gate A ausgesetzt; v3.0.4-Hotfix-Plan in `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` geschrieben) | **Für:** Nächste Session — **v3.0.4-Hotfix-Execution** (Primär-Track, ~90 Min fokussierte Session), danach Gate-A-Re-Start, danach Track 5a/5b, Track 4 weiter ausstehend

## 🔴 POST-INCIDENT: v3.0.3 Rollback auf v2.1 (2026-04-20 15:13 UTC)

**Commits:** `4cfa421` (incident+rollback), `b466f2e` (Applied-Learning 11/20)

**Was passierte:** Manual-Run auf Prod (20.04. nachmittags) ~720s Runtime, Output meldete für 7 US-Ticker massive Intraday-Deltas (AVGO -21,8%, APH -16,1%, MSFT -9,7%, TMO -9,9%). Broker-Verify durch User: AVGO real -2,26%. **Phantom-Kurse — Halluzination.**

**Root Cause:** Shibui-EOD-Query gab 17.04. als `latest_date` (korrekt: Karfreitag + Osterwochenende + Montag-before-EOD). Agent interpretierte das als "stale data" und improvisierte unautorisierten Yahoo-Intraday-Fallback-Pfad via Tavily. Spec §3 hatte keinen expliziten Guard gegen alternative Datenpfade.

**Was korrekt funktionierte:** Yahoo-n.v.-deterministic für BRK-B/RMS/SU (§3c), Material-Filter Slot-Struktur, 8/8 Sektionen, FLAGS/WATCHES/Trigger-Alignment. **T1/T3/T4-Happy-Path-Tests hatten diesen Edge-Case nie getriggert** (immer fresh Shibui-EOD).

**Rollback-Execution:** RemoteTrigger.update mit v2.1-Content aus `03_Tools/morning-briefing-prompt-v2.md`, allowed_tools zurück auf `[Bash,Read,Glob,Grep]` (Tavily raus, MCP-Connector bleibt attached aber ungenutzt). Prod läuft wieder v2.1 stable.

**v3.0.4-Hotfix-Plan:** `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md` (13 Tasks, T5 Adversarial-Stale-Shibui-Test neu, ~90 Min geschätzt).

## 🚀 NÄCHSTE SESSION — PRIMÄR-TRACK: v3.0.4 HOTFIX

### Schritt-für-Schritt

1. **Session starten** → STATE.md lesen → hierher wechseln
2. **Hotfix-Plan lesen:** `docs/superpowers/plans/2026-04-20-briefing-v3.0.4-hotfix.md`
3. **Spec-Update** (Task 1): Revision-Log v3.0.4 + §3a `AUTORITATIVE-DATA-QUELLE-REGEL` + `VERBOTENE-FALLBACK-PFADE` + Critical Guards erweitert
4. **Prompt-Update** (Task 2): `03_Tools/morning-briefing-prompt-v3.md` §3a-Wording + erweiterte Guards
5. **Probe-Trigger Update + Verify** (Task 3-4): `RemoteTrigger update` mit v3.0.4-Content, assert Keywords
6. **T5 Test schreiben + Run** (Task 5-6): Adversarial-Stale-Shibui, assert keine Fallback-Improvisation
7. **T1/T3/T4 Retest** (Task 7-9): auf v3.0.4, kein Regression
8. **Gate-A-Re-Start-Kriterien prüfen** (Task 10): alle 4 Tests PASS
9. **Prod-Deploy v3.0.4** (Task 11): `RemoteTrigger update` mit v3.0.4-Content
10. **Manual-Run auf Prod als finale Verifikation** (Task 12) — dieses Mal MUSS korrekt sein
11. **Gate A Tag 1 starten** (Task 13): naechster Werktag 10:00 MESZ Cron
12. **Bei v3.0.4 FAIL:** Rollback-Pfad auf v2.1 bleibt aktiv, keine Production-Regression

### Gate A Definition (unverändert)
"Stabil" = funktionale Korrektheit (8/8 Sektionen, Yahoo-n.v.-deterministisch, Material-Filter, Slot-Struktur, KEINE Phantom-Kurse). **NICHT Laufzeit.** Laufzeit-Regressionen >400s triggern manuellen Review, nicht Rollback.

---

## 🧠 KEY LESSONS LEARNED (für v3.0.4-Arbeit)

1. **Anti-Hallucination-Guards müssen zweigleisig sein** (Applied Learning 11/20):
   - (a) "KEINE Gründe erfinden" — gegen fabrizierte Narrativen
   - (b) "KEINE unautorisierten Datenquellen" — gegen improvisierte Datenpfade
2. **Edge-Case-Definitionen explizit:** "stale" vs "Wochenend-Lag" vs "Feiertags-Lag" dürfen nicht Agent-Interpretation überlassen werden.
3. **Autoritative Datenquellen als Sprach-Anker:** "Shibui-latest_date ist per Definition autoritativ" schließt Improvisationen aus.
4. **Probe-Tests müssen Adversarial-Scenarios abdecken:** T1 Happy + T3 Homonym + T4 Fail-Open ist nicht ausreichend. T5 Stale-Source wird nach diesem Incident permanent Teil des Test-Gates.

---

## ~~ALTE HANDOVER-SECTION~~ (historisch, pre-Incident Kontext)

> Die folgenden Sections (KG-Roadmap Option D, 6-Paper-Ingest-Closure, Gate-A-Definition, alte Deploy-Schritte etc.) bleiben für Kontext erhalten, sind aber **nicht mehr aktive Handlungsanweisung**. Der Primär-Track hat sich verschoben auf v3.0.4-Hotfix.

## ✅ POST-GATE: KG-Roadmap v0.1 als `draft-frozen` markiert (2026-04-20 Nacht-Spät)

**Commit:** `f13701a` docs(phase2-postgate): KG-Roadmap v0.1 als draft-frozen markiert (Codex Option D)

**Auslöser:** Nach Closure des 6-Paper-Ingest-Projekts ergab User-Frage „macht KG-Roadmap-Ratifikation vor Track 5a/5b Re-Validation mehr Sinn?" eine Pre-Track-5-Architektur-Entscheidung. Codex-Review (Opus 4.7 + Codex Combined) verglich 3 Optionen (A Ratifikation v0.1→v1.0 / B Q1-Q3-Klärung / C beides) und empfahl **Option D** (`draft-frozen` belassen, Inhalte faktisch geltend, Re-Review-Trigger explizit dokumentiert).

**Begründung:** Szenario 2 (10-K-KG) ist genuine `future-arch` ohne Usage-Evidence; v1.0 würde Konsens-Lock-in suggerieren. Q1-Q3 (Dataset-Größe / Lizenz-Legal / Score-Archiv-Integration) heute spekulativ beantwortbar, nicht release-blockierend, aber Q3-Design-Klarheit Pflicht **vor** operativer KG-Adoption.

**Faktische Inhalte (gelten ab 20.04.2026 Nacht-Spät trotz `draft-frozen`):**
- Form-4 Insider bleibt XML-Parsing (Szenario 1 REJECT bestätigt)
- 10-K-KG bleibt `future-arch`, frühestens 2027+ (Szenario 2 DEFER)
- Bayesian-RAG-Briefing-Rewrite verworfen wegen Tavily-API-MC-Dropout-Limitation (Szenario 3 DEFER)

**Re-Review-Trigger:** konkreter Cross-Entity-/10-K-Narrativ-Bedarf ODER Score-Archiv-Interim-Gate **2026-10-17** (whichever first).

**Scoring-Impact:** ZERO. DEFCON v3.7 unverändert, config.yaml unberührt, Skill bleibt v3.7.2, §28.3 Nicht-Migration-Trigger weiterhin gültig.

**Track 5a/5b Re-Validation = trivial closed:** Roadmap-Verdikt ist die Referenz-Antwort — beide Pläne haben bereits passende Phase-1b/Phase-2-Header-Notices, brauchen körperlich keine Änderung.

**Details:** log.md [2026-04-20] post-gate-d | CORE-MEMORY §1 Meilenstein 20.04.2026 Nacht-Spät | STATE.md System-Zustand-Eintrag KG-Roadmap | Synthesis-Frontmatter `status: draft-frozen` + Status-Banner.

---

## ✅ ABGESCHLOSSEN: 6-Paper-Ingest-Projekt (2026-04-20 Nacht)

**Commits:**
- `89275e2` Phase 2 Hybrid A+B+C — Status-Matrix + §4 Router + §33 Skill-Self-Audit + SKILL.md-Output-Block (10 Dateien, +275/-27)
- `5f6dc62` Final-Discoverability — CLAUDE.md-Pointer + insider-intelligence §33-Note + backtest-ready-forward-verify GT-Score-Pointer + log.md Closure-Entry (4 Dateien, +18)

**Wissenschaftliche Fundierung aktiv in:** !Analysiere (§4 Router + §2 Pipeline + SKILL.md Schritt 2.5 + Output-Block) + §28 Migration + §29 Retrospective (ab 2028) + §33 Skill-Self-Audit. Bewusst passiv in !QuickCheck/!Rebalancing/Screener (mechanische Workflows).

**Scoring-Impact gesamt:** ZERO. DEFCON v3.7 unverändert, alle 11 Satelliten-Scores/Sparraten/FLAGs unverändert, config.yaml unberührt. §28.3 Nicht-Migration-Trigger über gesamtes Projekt bestätigt. Skill bleibt v3.7.2.

**Smoke-Test AVGO (2026-04-20 Nacht):** Schritt 2.5 + Output-Template funktionieren — Befunde-Labels ticker-spezifisch (B6 Quality-Trap-Nicht-Aktivierung sauber ausgewiesen), traceable, kompakt. Erster Live-Test natürlich bei TMO Q1 23.04.2026.

**Details:** log.md [2026-04-20] phase2 + [2026-04-20] projekt-abschluss | CORE-MEMORY §5 "Phase-2-System-Konsequenzen" | Synthesis §Status-Matrix.

---

---

## 🆕 HAUPT-TRACK: 6-Paper-Ingest Phase 1 KOMPLETT (2026-04-20 Abend-Spät)

**Scope-Entscheidung Mittag→Abend→Abend-Spät:** User hatte 6 neue Finance/AI-Papers in `07_Obsidian Vault/.../raw/` hinzugefügt (3 PDFs + 3 .md). Nach 2 Codex-Review-Runden (Triage + Skill-Cross-Check) wurde entschieden: Track 5a/5b/Briefing-v3.1 **pausieren**, Paper-Ingest mit Palomar-Standard durchführen. v3.0.3 Prod-Deploy läuft **parallel** (nicht blockiert). **Phase 1a + Phase 1b in derselben Tages-Session abgeschlossen** — User-Entscheidung zugunsten Codex-Combined-Review statt sequentieller Gate-Review-Runden.

**Phase 1a abgeschlossen (Severity-🔴-Cluster, Commit 7ec7b86):**
- 2 Sources: [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] (KDD '26, B19), [[Sheppert-2026-GT-Score]] (JRFM 2026, B20)
- 3 Concepts: [[LLM-Investing-Bias-Audit]], [[Regime-Aware-LLM-Failure-Modes]], [[Composite-Anti-Overfitting-Objective]]
- 5 Author-Entities: Weixian Waylon Li, Hyeonjun Kim, Mihai Cucuringu, Tiejun Ma, Alexander Pearson Sheppert
- Updates: `Wissenschaftliche-Fundierung-DEFCON` (B19+B20), `Backtest-Methodik-Roadmap` v2.0→v2.1, `index.md`, `log.md`

**Phase 1b abgeschlossen (Severity-🟡-Cluster, Commit folgt gleich nach diesem Edit):**
- 4 Sources: [[Arun-et-al-2025-FinReflectKG]] (Domyn/arxiv 2508.17906, B21), [[Labre-2025-FinReflectKG-Companion]] (Towards AI, B22), [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] (Frontiers AI, B23), [[Iacovides-Zhou-Mandic-2025-FinDPO]] (Imperial/arxiv 2507.18417, B24)
- 6 Concepts: [[Knowledge-Graph-Finance-Architecture]], [[Agentic-Reflection-Pattern]], [[LLM-as-a-Judge-Evaluation]], [[RAG-Uncertainty-Quantification]], [[LLM-Preference-Optimization-Finance]], [[Sentiment-Strength-Logit-Extraction]]
- 12 Author-Entities: Abhinav Arun, Fabrizio Dimino, Tejas Prakash Agarwal, Bhaskarjit Sarmah, Stefano Pasquali, Marcelo Labre, Lebede Ngartera, Saralees Nadarajah, Rodoumta Koina, Giorgos Iacovides, Wuyang Zhou, Danilo Mandic
- 1 neue Synthesis: [[Knowledge-Graph-Architektur-Roadmap]] v0.1 (Entscheidungsvorlage KG vs. XML-Direkt-Parsing vs. Bayesian RAG; 3 Qualitäts-Gates; 3 konkrete Szenarien; Codex-Gate 2.5 eingeplant)
- Updates: `Wissenschaftliche-Fundierung-DEFCON` (B21-B24, 20 Quellen / 24 Befunde), `index.md` (107→130 Notes), `log.md` — Phase 1b-Eintrag

**Codex Combined Gate 2 Ergebnis (post-commit 40fbcdd + Fix-Commit 3f11b63):**
- Cross-Links, B-Mapping, Architektur-Roadmap, Instruktion-Alignment → **PASS**
- Akkuratesse → CONDITIONAL (B23 ECE-Baseline unklar) → **behoben** in `3f11b63` (Ebene 1/2/3 Baselines explizit getrennt)
- Showstopper-Risk → CONDITIONAL (B24 "Vor operativer Adoption"-Formulierung) → **behoben** in `3f11b63` (als hypothetisch markiert)
- **Phase-2-Ready: JA**

**Plus späte Obsidian-Graph-Lesson** (`addc33b` + `1590816`): Raw-Backlinks brauchen Datei-Stem-Link im Body (Frontmatter-`raw:`-String ist kein Graph-Edge). Lesson in memory `feedback_raw_backlink_pflicht.md`.

**Nächste Session — Reihenfolge:**
1. **Phase 2: System-Konsequenzen** — §29-Sub-Klausel-Mapping erweitern (29.1+29.2+29.5+29.6) + ggf. neue §33 Skill-Self-Audit + Plan-Diffs (Track 5a/5b/v3.1) + Entscheidung zu [[Knowledge-Graph-Architektur-Roadmap]]-Szenarien
2. **Phase 2.5 Codex-Skill-Audit-Gate** (kritisch — Anti-Creep-Mechanismus): trennt Audit-Methodik von Skill-Code-Change
3. **Parallel: Prod-Deploy v3.0.3 + Gate-A-Start** — unverändert (siehe Section unten)

**Showstopper-Risk** (Codex Round 2): Vermischung Audit-Layer ↔ Produktions-Skill-Logik. Phase 2.5-Gate adressiert das explizit.

---

---

## 📊 AKTUELLER PROJEKT-STAND (20.04.2026, Ende Mittags-Session)

### Portfolio
- 11 Satelliten, DEFCON v3.7, Sparraten 35,63€ / 17,81€ / 0€, Summe **285€** ✓ (Nenner 8.0)
- Scores stabil seit 18.04.: V 63/D2, TMO 64/D2 (fcf_trend_neg schema-trigger nicht aktiviert), APH 63/D2 FLAG, MSFT 59/D2 FLAG
- Keine Score-Änderungen in dieser Session

### Morning-Briefing (Infrastruktur)
- **v3.0.3 auf Probe-Trigger** `trig_01XYuQ5mugsvZGZD4K52rjXh` deployed + T1-Baseline-Content zurückgesetzt (clean, post-T3 aufgeräumt)
- **Alle 3 Pre-Prod-Tests PASS:** T1 Happy-Path 262s, T4 Fail-Open ~10s (HTTP 422 gefangen), T3 Adversarial-Trap ~270s (dreifache Homonym-Absicherung verifiziert)
- **Prod-Trigger** `trig_01PyAVAxFpjbPkvXq7UrS2uG` läuft noch v2.1 — **Deploy pending in nächster Session**
- Korrektheits-Prinzip verankert: Spec §6(E)/§8/§11-13 auf Soft-Alert-Schema rebased (<180s healthy / 180-400s observe / >400s alert, KEIN Auto-Rollback aus Runtime)
- v3.1 Deferred-Plan geschrieben: `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md` (2-Stage-Tavily-Cache, nur wenn 262s im Alltag stört)

### Gate A Definition (Codex-aligned)
"Stabil" = funktionale Korrektheit (8/8 Sektionen, Yahoo-n.v.-deterministisch, Material-Filter korrekt, Slot-Struktur korrekt). **NICHT Laufzeit.** Laufzeit-Regressionen >400s triggern manuellen Review, nicht Rollback.

---

## 🚀 NÄCHSTE SESSION — PRIMÄR-TRACK: PROD-DEPLOY

### Schritt-für-Schritt

1. **Session starten** → STATE.md lesen → hierher wechseln
2. **Prod-Trigger aktualisieren:**
   ```
   RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG
   ```
   (Baseline-Config zur Sicherheit speichern für potentiellen Rollback)
3. **RemoteTrigger update** mit v3.0.3-Content (exakt der Probe-T1-Baseline-Prompt — bereits auf Probe-Trigger als Referenz-Implementierung):
   - `environment_id`: `env_01Ek3HiKjymFoWzrQoyvMTEk` (unverändert)
   - `allowed_tools`: `["Bash","Read","Glob","Grep","mcp__tavily__tavily_search"]`
   - `events[0].data.message.content`: v3.0.3-Prompt aus `03_Tools/morning-briefing-prompt-v3.md` (Zeilen 60-338, innerhalb ``` ```)
   - `session_context.model`: `claude-sonnet-4-6`
   - `sources`: github `tobikowa90-hub/dynastie-depot`
   - **mcp_connections NICHT im ccr-Pfad senden** — werden automatisch erhalten (Shibui + Tavily bleiben attached)
4. **Post-Update-Verify (Spec §10):**
   - `RemoteTrigger get trig_01PyAVAxFpjbPkvXq7UrS2uG`
   - Assert content enthält `SCHRITT 4.5`, `v3.0.3`, `n.v. [Yahoo 403 known]`, `Runtime-Hinweis (v3.0.3)`
   - Assert content enthält NICHT `Keine News-Suche` (v2.2-Reste)
5. **Manual-Run-Verification auf Prod** (einmalig via Desktop-App "Jetzt ausführen" auf **Prod**-Trigger, nicht Probe): bestätigen dass Prod identische Output-Struktur wie T1-Baseline liefert.
6. **Gate A startet** mit morgigem (21.04.) 10:00-MESZ-Cron-Run. 3 konsekutive Werktage (21./22./23.04.) mit Korrektheits-Check (nicht Laufzeit):
   - Di 21.04. Cron-Run → Output checken auf 8/8 Sektionen + Yahoo-n.v. + Material-Filter
   - Mi 22.04. Cron-Run → gleiche Checks
   - Do 23.04. Cron-Run → gleiche Checks (zusätzlich: TMO Q1 Earnings-Event = Cohort/Per-Ticker-Load)
7. **Post-Deploy Housekeeping** (in derselben Session commitbar): `memory/morning-briefing-config.md` ✓ bereits gemacht; zusätzlich Commit-Log-Entry in CORE-MEMORY §1 ergänzen nach Prod-PASS.
8. Bei Prod-Regression in den 3 Tagen: **Rollback-Runbook** aus Spec §11 — `RemoteTrigger update` mit v2.1-Content aus `03_Tools/morning-briefing-prompt-v2.md`.

### Deployment-Pipeline-Dokumentation
Siehe memory `morning-briefing-config.md` für das wiederverwendbare 7-Schritt-Pattern (Edit → Commit → Push → Update → Verify → Manual-Run → Result-Doc).

---

## 📅 NACH GATE-A-PASS (ab ~24.04.)

### Track 5a — SEC EDGAR Skill-Promotion
Plan ready: `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks, Codex-reviewed). Pre-Implementation-Gate A (Tavily-Stabilität 3-Tage) = jetzt am morgigen Prod-Deploy-Tag startend, frühester Start ~24.04.

### Track 5b — FRED Macro-Regime-Filter
Plan ready: `docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md` (15 Tasks, Codex-reviewed). Vor Task 1.3: **User-Aktion** — FRED-API-Key registrieren (~5 Min: https://fred.stlouisfed.org/docs/api/api_key.html).

### Track 4 — Portfolio-Risk ETF+Gold-Erweiterung
**Blockiert auf User-Input:**
- ETF-Core-Ticker? (IWDA.AS / SWDA.L / EUNL.DE / …?)
- Gold-Ticker? (SGLD.DE / 4GLD.DE / GC=F / …?)

Nach Input: `03_Tools/portfolio_risk.py` um ETF+Gold erweitern, in `--persist daily`-Schema einbetten.

---

## 📆 PORTFOLIO-TRIGGER (30 TAGE)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| **21.04.** | RMS.PA | — | **Ex-Dividend EUR 13,00** (automatische Gutschrift im aktiven Depot, kein Handlungsdruck) |
| **23.04.** | **TMO** | **B** | **Q1 — D2-Entscheidung + fcf_trend_neg Resolve-Gate (WC-Unwind + FCF >$7,3B?)** |
| **28.04.** | **V** | **B** | **Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)** |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review CapEx/OCF <60%** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

### Aktive Watches
- **V D2-Kritik:** 6M RelStärke -14pp vs SPY. Q2 28.04. = Beat+Guidance → D3-Reversal, Miss → D1-Richtung.
- **ASML Fwd P/E FY27 = 30,30:** Grenzfall, bei <30 Fix-1-Fwd-Zweig deaktiviert → Score +1/+2 (D3→D4-Kandidat).
- **AVGO Insider $123M:** wahrscheinlich Post-Vesting. Vor FLAG: OpenInsider manuell prüfen.
- **TMO Resolve-Gate:** Q1 23.04. — WC-Unwind + FCF-Recovery bestätigt → kein FLAG; fehlt → fcf_trend_neg nachtragen + Ersatz-ZTS-Vorbereitung eskalieren.
- **MSFT FLAG-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance-Lease $19,5B raus) = Auflösung.
- **RMS.PA Q1-Slowdown (NEU 20.04.):** Middle-East-Druck + Tourismus schwächer, Q1 Revenue-Miss vs. Erwartung. Watch-Notiz, kein Klasse-C-Event. H1-Trigger (Juli/Aug) möglich vorzuziehen falls Q2 bestätigt.

---

## ⚠️ OPEN RISKS / REMINDERS

1. **Tavily Dev-Key Rotation** innerhalb 7 Tagen nach Prod-Go-Live (`tvly-dev-4PYXp...`)
2. **Prod-Deploy-Rollback-Pfad:** `03_Tools/morning-briefing-prompt-v2.md` unverändert im Repo, Runbook in Spec §11
3. **Codex-Plugin Review-Gate** NICHT aktiviert (User-Entscheidung 19.04.) — Codex nur on-demand via `codex:codex-rescue`
4. **Track 5b FRED** ist strategische Greenfield-Entscheidung (Macro-Dimension in DEFCON?) — vor Execution klären
5. **v3.1 Cache-Refactor** nur bei Bedarf — trigger: "262s zu lang im Alltag" oder ">400s-Alert-Schwelle wiederholt erreicht"
6. **Korrektheits-Prinzip systemweit verankert** (memory `feedback_correctness_over_runtime.md`) — gilt auch für zukünftige Pipeline-Änderungen (Scoring, FLAG-Checks, Score-Archive). Runtime-Optimierungen nie auf Kosten von Recall.

---

## 🗂 ARTEFAKTE DIESER SESSION (20.04.2026 Mittags)

### Dateien
- `03_Tools/morning-briefing-prompt-v3.md` (v3.0.3)
- `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` (Revision-Log v3.0.3)
- `03_Tools/tests/tavily-probe-prompts/results/T1-2026-04-20-v3.0.3.md`
- `03_Tools/tests/tavily-probe-prompts/results/T4-2026-04-20-v3.0.3.md`
- `03_Tools/tests/tavily-probe-prompts/results/T3-2026-04-20-v3.0.3.md`
- `docs/superpowers/plans/2026-04-20-briefing-v3.1-cache-refactor.md` (deferred)
- Memory: `feedback_correctness_over_runtime.md` (neu), `data-source-coverage.md` (SU.PA-Schärfung), `morning-briefing-config.md` (v3.0.3-Status)

### Commits (chronologisch)
- `30b1867` v3.0.3 prompt + spec rebase (Lever 1 + Soft-Alert)
- `e5ba317` T1-Result + STATE + Handover
- `42a82f4` v3.1 deferred cache-refactor plan
- `c7c0c11` Gate-A-Korrektheits-Definition
- `29d9cb0` T4 Fail-Open PASS
- `7cafc78` T3 Adversarial-Trap PASS

### Remote-Trigger-State
- Probe `trig_01XYuQ5mugsvZGZD4K52rjXh`: clean v3.0.3 T1-Baseline-Content (post-T3-Reset), allowed_tools full, Shibui+Tavily MCPs attached
- Prod `trig_01PyAVAxFpjbPkvXq7UrS2uG`: v2.1 (unverändert, Deploy pending)

---

## ▶️ TRIGGER NÄCHSTE SESSION

```
Session starten
```

1. Claude liest `STATE.md`
2. Wechsel hierher
3. **Primär-Track: Prod-Deploy v3.0.3** (Schritte 2-6 oben)
4. Bei abweichender User-Priorität: Track 4 (ETF/Gold-Input), oder Track 5a/5b (falls Gate A bereits abgeschlossen), oder Scoring-Session bei Marktbewegungen

---

*Archiv-Verweis: Historische Session-Details (frühe 20.04.-Session Track-5-Plan-Writing, 00:13-MESZ-Session Tavily-Probe-Setup v3.0.1/v3.0.2, Tool-Evaluation-Runde) in `git log` ab `dd0cd62` sichtbar. Milestone-Chronik in `CORE-MEMORY.md §1`.*
