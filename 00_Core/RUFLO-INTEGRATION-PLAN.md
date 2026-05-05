# Ruflo-Integration-Plan v1.2 — Coexistence-Roadmap

**Status:** **v1.2** — Spec-approved Coexistence-Roadmap (ersetzt v1.1; Phase 1.1 + Welle 0 + Phase 1.2-1.7 ✅ DONE; Welle 3 = 1.8 + 1.9-Replace PENDING 05.-12.05.2026 post-BRK.B-Tag-+1; Phase 2 = 2a/2b deferred ab ~13.05.; Phase 3-4 = ASTRONAUT-ARCH unter Adoption-Gates).
**Erstellt:** 2026-04-28 (v1.0) / **v1.1:** 2026-05-02 (Bridge-Coherence-Welle, Patches P1/P2/P3/P5/P6/P10 als „operational implementiert" verzeichnet) / **v1.2:** 2026-05-05 (Spec-Approval `docs/superpowers/specs/2026-05-05-ruflo-superpowers-coexistence-design.md` USER-APPROVED; Coexistence-Modell Variante D normativ verankert; alle PIPELINE-#42-Pflicht-Inhalte (a)–(h) integriert).
**Spec-Quelle (USER-APPROVED 05.05.):** `docs/superpowers/specs/2026-05-05-ruflo-superpowers-coexistence-design.md` (v1.0 Final-R2 closed; HIGH-1 + HIGH-2 spec-intern closed via M1 Named-Trigger-Pflicht + G3 3-Felder-Konsistenz + C2.1 `CLAUDE.md`-Sync-Set; MED-2 closed via W3 Feld-Typen-Tabelle).
**Architektur-Modell:** Variante D — Capability-Layered Hybrid With Explicit Adoption Gates.
**Default-Workflow-Layer:** Superpowers (Authority via `CLAUDE.md` Override-Block).
**Substrat-Layer:** Ruflo (Memory-Bridge / AttestationLog / Doctor-Periodic / AIDefence / Tool-Mode `dynastie` / Context Autopilot / Statusline).
**M4-Rollentrennung:** `CLAUDE.md` = Authority („was darf controllen"). `SYSTEM.md §Ruflo-Status` = Attestierung („was läuft gerade"). Diese Datei = Roadmap („was ist als nächstes geplant"). KONTEXT/APPLIED-LEARNING/CORE-MEMORY informieren, halten aber keine Control-Authority (Spec M4 Exclusion-Note).

**Plan-Patches-Status:** P1 ✅ (path-scoped Import operational) · P2 ✅ (CLI-Flag-Bug umgangen via cwd-Default-Akzeptanz) · P3 ✅ (IDE-Pre-Flight in Welle 0) · P5 ✅ (Phase-1.9-Defer + Replace dokumentiert in §1.9-Replace) · P6 ✅ (`SYSTEM.md §Ruflo-Status` angelegt 30.04.) · P10 ✅ (Codex-Nits im 1.2-1.7-Commit nachgefixt) · **P4 / P7 / P8 / P9 jetzt in v1.2 verankert** (siehe §Meta-Review-Patches-Closure).

---

## Versions-Verlauf

| Version | Datum | Änderung |
|---------|-------|----------|
| v1.0 | 2026-04-28 | Initial — Phase-1-bis-4-Roadmap, USERGUIDE-v3.5-basiert, „User will Ruflo statt Superpowers nutzen"-Annahme |
| v1.1 | 2026-05-02 | Bridge-Coherence-Welle: Patches P1/P2/P3/P5/P6/P10 operational implementiert in Welle 0 + Phase 1.2-1.7 (Commits `c9a3ed5` / `7b3c7d1` / `e983102`); Welle 3 (1.8/1.9) deferred 05.-12.05. post-BRK.B-Tag-+1 |
| **v1.2** | **2026-05-05** | **Spec-Approval Coexistence-Variante D normativ verankert. Bisherige „Ruflo statt Superpowers"-Prämisse explizit ersetzt durch Coexistence-Modell mit Authority-Trennung. 1.9-Replace (audit-trace-lite Pilot) ersetzt Voll-Trajectory-Recording. P4/P7/P8/P9 inkorporiert. Phase 2 in 2a (Memory-Controllers + Workers) und 2b (Skill-Refactor Stream-Chain) gesplittet. Stream-Chain + Hive-Mind unter Adoption-Gates re-basiert. ONNX-ROI-Gate als Phase-2-Eval-Slot mit 5 Schwellen-Metriken etabliert. Cleanup-Track für 131 broken Refs. C5-Reststeller R2-1 + R2-2 closed. Final-R1 MED/Gaps closed. 00_Core-Cleanup-Disziplin: META-REVIEW.md → `05_Archiv/` als Folge-Commit.** |

---

## Executive Summary (revidiert post-Spec)

Diese Roadmap operationalisiert die **Coexistence-Spec v1.0** (USER-APPROVED 05.05.). Die ursprüngliche v1.0-Prämisse („User will Ruflo statt Superpowers nutzen") ist normativ ersetzt durch das **Capability-Layered Hybrid With Explicit Adoption Gates**-Modell:

- **Superpowers-Reaktivierung war kein Architektur-Eingriff**, sondern Schließung einer akuten Workflow-Lücke (Codex-R1-Befund: Ruflo hat null funktionales Brainstorming-Äquivalent, kein erstklassiger Plan-Skill, SPARC nur als Tabellen-Eintrag, Spec-Driven-Development ADR/DDD-geprägt — nicht passend für Investing-Workflows).
- **Ruflo bleibt für Memory/Audit/Hygiene wertvoll** als Substrat-Layer.
- **Workflow-Layer-Erweiterungen erfordern explizite Adoption-Gates** mit empirischer Evidenz und Plan-Update — Default = BLOCK.
- **3-Felder-Konsistenz** für jede aktive Workflow-Approval: Listen-Eintrag (`CLAUDE.md` M1-Registry) + Gate-Ref (Plan-Definition) + Named-Trigger (Routing-Table). Fehlt eines → NICHT autorisiert.

**Größter aktueller Hebel (Substrat):** Memory-Bridge (path-scoped, `allProjects=false`) + AttestationLog + Tool-Mode `dynastie` → Token-Save + Audit-Trail.
**Größtes aktuelles Risiko:** Doppel-SSoT zwischen `dynastie-depot` SKILL.md und Stream-Chain/Hive-Mind-Workflow-Owner — daher beide unter Adoption-Gate.

---

## Spec-Bezug & Architektur-Modell

### Variante D — Kern-Prinzip

Superpowers ist die Default-Workflow-Layer für Investing-Operationen. Ruflo ist die Substrat-Layer für Memory/Audit/Hygiene. Jede Erweiterung von Ruflo in die Workflow-Layer erfordert ein explizites, fail-closed Adoption-Gate mit empirischer Evidenz und Plan-Update.

**Drei normative Grundsätze:**

1. **Substrat ≠ Workflow.** Substrat-Layer-Erweiterungen sind additiv und jederzeit erlaubt. Workflow-Layer-Erweiterungen sind per Default BLOCKED.
2. **Authority vs. Attestierung getrennt.** `CLAUDE.md` Override-Block ist die einzige authoritative Quelle dafür, welche Workflow-Skills aktiv sind („Aktuelle Positivliste"). `SYSTEM.md §Ruflo-Status` dokumentiert nur den Runtime-Zustand, hat aber keine Decision-Authority.
3. **Default = BLOCK.** Bei jedem unklaren Status fällt das System auf „nicht aktivieren" zurück.

### Control-Plane-Disziplin (Spec Sektion 2 — 5 Mechanismen)

| ID | Was | Wo | Bezug zu v1.2 |
|----|-----|-----|---------------|
| **M1** | Authoritative Workflow-Registry (`default-workflow-layer = superpowers` + `ruflo-workflow-exceptions: []`) — Promotion erst wirksam mit Named-Trigger in Routing-Table | `CLAUDE.md` Override-Block | Wird in Plan-v1.2-Commit angelegt (Task 19) |
| **M2** | Lifecycle-Hook-Owner-Regel — pro Event-Familie genau ein aktiver Owner; alle anderen passive (read-only, kein State-Write, kein downstream-Workflow-Trigger) | `CLAUDE.md` Override-Block (Regel) + `SYSTEM.md §Ruflo-Status` (Belegung) | Aktueller Owner: `briefing-sync-check.ps1` für SessionStart/SessionEnd; Ruflo-Hooks in `settings.json` sind passive Intent-Dokumentation |
| **M3** | Skill-Annotation `control-plane:` in Routing-Table (Werte: `dynastie-primary`, `superpowers-workflow`, `ruflo-substrate-only`, `tools-engineering`); Supporting-Tools wie `cc-gemini-plugin`, `codex-rescue`, `coderabbit-review`, `watch` exempt | `CLAUDE.md` Routing-Table | Wird in Plan-v1.2-Commit angelegt (Task 21) |
| **M4** | Authority (`CLAUDE.md`) vs. Attestierung (`SYSTEM.md`) vs. Roadmap (diese Datei) — strikt getrennt; KONTEXT/APPLIED-LEARNING/CORE-MEMORY informieren, halten aber keine Control-Authority | drei genannte Files | normativ verankert |
| **M5** | `.claude/settings.json` + `settings.local.json` sind Implementation/Intent-Dokumentation, nicht Policy — können keine Workflow-Layer aktivieren, die nicht in `CLAUDE.md` autorisiert sind | settings-Files | Bestätigung im SYSTEM.md §Ruflo-Status |

### Spec-Pfad

Vollständige Spec-Definition (Mechanismen, Klassifikationen, Adoption-Gates G1-G5, ONNX-ROI-Gate, audit-trace-lite-Schema): `docs/superpowers/specs/2026-05-05-ruflo-superpowers-coexistence-design.md`. **Diese Roadmap setzt die Spec voraus** und definiert die operative Sequenz, nicht die Mechanismen selbst.

---

## Phase-Overview (Status-Tabelle)

| Phase | Inhalt | Status | Trigger / Datum |
|-------|--------|--------|-----------------|
| 1.1 | Override-Block in `CLAUDE.md` | ✅ DONE | 28.04.2026 (Codex-Round-2 PASS WITH NITS) |
| 1.2 | ADR-048 Auto Memory Bridge (path-scoped, NICHT `allProjects=true`) + Backend-Pfad WSL `/home/tobia/.local/share/ruflo/memory` | ✅ DONE | 30.04.2026 (Welle 0 WSL-Foundation + Phase-1.2-1.7-atomar-Commit `e983102`) |
| 1.3 | ADR-050 Intelligence Loop Top-K=3 | ✅ DONE | 30.04.2026 (Bestandteil 1.2-1.7-Commit) |
| 1.4 | ADR-051 Context Autopilot | ✅ DONE | 30.04.2026 |
| 1.5 | Custom Tool-Mode `dynastie` (env `CLAUDE_FLOW_TOOL_GROUPS=memory,monitor`) | ✅ DONE | 30.04.2026 |
| 1.6 | Statusline (DDD-Bar disabled) | ✅ DONE | 30.04.2026 |
| 1.7 | 6-Hook-Subset (Rest 21 explizit `enabled: false`) | ✅ DONE | 30.04.2026 |
| **1.8** | **Doctor-Periodic-Cadence** | 📅 PENDING Welle 3a | **1.8-Fenster: 05.-12.05.2026** (post-BRK.B-Tag-+1; Cadence-Definition siehe §Phase-1.8 unten) |
| **1.9-Replace** | **audit-trace-lite Pilot (2-3 Vollanalysen)** ersetzt Voll-Trajectory-Recording | 📅 PENDING Welle 3b | **1.9-Pilot-Fenster: ab 27.05.2026** (frühestens an VEEV Q1 FY27, abhängig von Earnings-Trigger; Schema-Erstellung in `05_Archiv/audit_trace_lite.jsonl` kann VOR 1.9-Pilot-Start als reine Schema-Datei erfolgen — separater §18-Sync-Trigger gem. Spec W6) |
| 2a | Memory-Controllers (HierarchicalMemory, AttestationLog, ExplainableRecall, CausalRecall) + Worker-Manager (5 relevante: patterns, adr, consolidate, predict, learning — `adr` initial warn-only) | 📅 deferred ab ~13.05.2026 | post-Welle-3-Stabilität |
| 2b | Skill-Refactor Stream-Chain (Pipeline-Definition für `dynastie-depot`) — **kein Eval, sondern Architektur-Eingriff** | ⛔ ASTRONAUT-ARCH (Adoption-Gate-pflichtig) | siehe §Adoption-Gates Stream-Chain |
| 2.3 | Codex Dual-Mode auf §28.1 (Paper-Befund-Auswahl + ExplainableRecall-Trace + §29.7 M&P-Trigger) — **NICHT §28.2 Algebra** (P4-Repositioning) | 📅 deferred (Phase 2a-Slot) | nach Worker-Stabilität ≥2 Wochen |
| 2.4 | AIDefence pre-agent-input für Tavily | 📅 deferred ab ~13.05.2026 | Bestandteil Phase 2a |
| 2.6 | Hyperbolic Embeddings für Sektor-Taxonomie | ⛔ CONDITIONAL (ONNX-Pre-Condition) | nach ONNX-ROI-Pass (siehe §ONNX-ROI-Gate) |
| 2.7 | Drift-Detection Baseline | 📅 deferred (Phase 2a-Slot) | nach HierarchicalMemory-Stabilität |
| 3.1 | Hive-Mind für `!BatchScan`-Trigger | ⛔ ASTRONAUT-ARCH (Adoption-Gate-pflichtig) | siehe §Adoption-Gates Hive-Mind |
| 3.2-3.5 | Claims-System / Multi-Agent-Consensus / Browser-Automation / MCP-Multi-Client | ⛔ Use-Case-getrieben, keine Default-Aktivierung | per Adoption-Gate je Item |
| 4.x | plugin-prime-radiant / plugin-cognitive-kernel / plugin-hyperbolic-reasoning / Granger-Causality / Guidance-Library / Pattern-Export / Helper-Scripts-Eval | ⛔ HOCH (alle alpha/experimentell) | Default-Tendenz: SKIP wenn unklar |

**Status-Legende:** ✅ DONE · 📅 PENDING/deferred mit definitivem Slot · ⛔ ASTRONAUT-ARCH/CONDITIONAL — Adoption-Gate-pflichtig · 🔵 Use-Case-getrieben.

---

## §Phase-1.8 Welle-3 — Doctor-Periodic-Cadence

**Begründung:** Embedding-unabhängig, additive Audit-Layer, niedrig-risk (Spec Sektion 6 W1). Doctor-Lauf als *supporting evidence only* — bestätigt Runtime-Health, kann aber keine Architektur-Entscheidung autorisieren (Spec G5).

**Cadence-Definition:**

| Cadence | Trigger | Befehl | Persistenz |
|---------|---------|--------|------------|
| **Wöchentlich** (Standard) | manuell jeden Montag morgen vor erstem Trigger | `wsl -d Ubuntu-24.04 -u root -e bash -lc 'ruflo doctor --verbose'` | Snapshot in `05_Archiv/ruflo-doctor-history/YYYY-MM-DD.txt` |
| **Pre-Phase-Gate** | vor jedem Phase-Sprung (1.9 → 2a, 2a → 2b, etc.) | siehe oben | gleicher Pfad |
| **Post-§18-Sync-Welle** (Optional) | nach atomarem Multi-File-Sync mit AgentDB-Touch | siehe oben | gleicher Pfad |
| **Ad-hoc** (Drift-Verdacht) | Operator-Initiative bei Auffälligkeit | siehe oben | gleicher Pfad |

**§18-Sync-Trigger für 1.8-Aktivierung (System-Zustand-Change):** `SYSTEM.md §Ruflo-Status` (Cadence-Schedule + erste Snapshot-Pfad-Pattern) + `00_Core/log.md` + `STATE.md` Last-Audit + `PIPELINE.md` (Cadence-Item NEU).

**Kill-Criterion (P8) — numerisch operationalisiert (Codex-R1 MED-3 Fix):** Doctor-Run >120s in **≥2 aufeinanderfolgenden Runs** (Performance-Drift) **ODER** ≥3 FAIL-Runs in 4 Wochen (Health-Regression) **ODER** zwei aufeinanderfolgende Wochen Cadence komplett ausgefallen wegen Operator-Friction → Cadence pausieren, Root-Cause-Analyse, dann re-aktivieren oder skippen. Reine WARN sind erwartbar (Default-Setup-State).

**Erfolgskriterium:** ≥4 Wochen wöchentliche Snapshots ohne unerklärten FAIL-Drift; Snapshots im `05_Archiv/ruflo-doctor-history/` als zeitliche Health-Trend-Dokumentation auditierbar.

**Rollback:** Cadence pausieren = `SYSTEM.md §Ruflo-Status` umstellen, kein Code-Eingriff.

---

## §Phase-1.9-Replace — audit-trace-lite Pilot

**Begründung Replace (Spec Sektion 6 W1):** Original 1.9 Voll-Trajectory-Recording auf `dynastie-depot`-Skill ist **timing-falsch vor Skill-Stabilität** (Beispiele.md-Refactor Item #17 noch pending; ONNX-Embeddings sind Mock → RL-Trainings-Daten anti-produktiv; Spec-Klassifizierung Trajectory = PARTIAL embedding-sensitive). Promotion zu Voll-1.9 erfordert UND-verknüpft: (a) ONNX-Aktivierung (siehe §ONNX-ROI-Gate) **UND** (b) Skill-Workflow stable über mind. 3 vergleichbare Vollanalysen **UND** (c) ≥2-3 audit-trace-lite-Iterationen ohne Schema-Churn.

### Pilot-Definition

**Was:** Manueller (oder semi-manueller) Trace pro DEFCON-Vollanalyse, der **causal explainability des Analyse-Pfades** festhält — nicht das Outcome (das ist `score_history.jsonl`), sondern den **Reasoning-Path und Decision-Checkpoints**.

**Pfad:** `05_Archiv/audit_trace_lite.jsonl` (append-only, NEU).

**Pilot-Cadence:** **2-3 Vollanalysen**, danach Reassess gegen GO/NOGO-Kriterien (siehe Pilot-Exit unten).

**Pilot-Kandidaten (chronologische Auswahl, abhängig von Earnings-Kalender):**
1. **VEEV Q1 FY27 — 27.05.2026** (Standard-Klasse-B-Vollanalyse, mittlere Komplexität)
2. **COST Q3 FY26 — 28.05.2026** (Screener-Exception, Membership-Yield-Watch)
3. **TMO Q2 FY26 ~Ende Juli 2026** (Organic-Akzeleration + Clario-Integration-Check) — **falls Pilot 1+2 keine Schema-Churn auslösen, sonst skippen und nach Schema-Stabilisierung neu**

### Schema (10 Felder, Spec Sektion 6 W3)

```jsonl
{
  "timestamp": "2026-05-12T09:42:00+02:00",
  "ticker": "VEEV",
  "analysis_type": "vollanalyse",
  "source_bundle": ["defeatbeta-mcp:VEEV-FY27Q1-transcript", "sec-edgar:VEEV-10-Q-FY27Q1", "wiki:Investing-Mastermind/VEEV"],
  "critical_evidence_refs": ["00_Core/INSTRUKTIONEN.md§19.1", "02_Analysen/VEEV-DEFCON-FY27Q1.xlsx#Methodology-Tab"],
  "decision_checkpoints": {
    "quality_trap_invoked": true,
    "earnings_wait_honored": true,
    "skip_window_carryover_applied": false
  },
  "score_change_summary": "74→XX Δ-Y",
  "operator_notes_short": "Methodology-Watch X carried forward",
  "skill_meta": {
    "dynastie_depot_version": "v3.7.6",
    "workflow_shape_changed_since_last_trace": false
  },
  "trace_quality": "complete"
}
```

**Feld-Typen-Tabelle (verbindlich, Spec W3 MED-2-Closure):**

| Feld | Typ | Format / Enum |
|------|-----|---------------|
| `timestamp` | string | ISO 8601 mit Timezone-Offset (`YYYY-MM-DDTHH:MM:SS±HH:MM`). Datum allein ist invalid — Pilot-Records ohne Uhrzeit/Offset sind als `trace_quality: partial` zu markieren |
| `ticker` | string | Großbuchstaben-Ticker (`VEEV`, `BRK.B`, `RMS.PA`); Non-US mit Suffix-Konvention der Quelle |
| `analysis_type` | string | Enum: `vollanalyse`, `quickcheck`, `flag-event`, `methodology-watch-resolution` |
| `source_bundle` | array&lt;string&gt; | Item-Form: `<source-type>:<identifier>`. Erlaubte source-types: `defeatbeta-mcp`, `sec-edgar`, `yfinance`, `wiki`, `web-fetch`, `manual-research`, `tavily` |
| `critical_evidence_refs` | array&lt;string&gt; | Item-Form: `<repo-relative-pfad><anchor>`. Anchor-Konvention: `§<paragraph-id>` für MD, `#<sheet-or-named-range>` für xlsx, `:<line-number>` für Code/JSONL, leerer Anchor erlaubt für ganze Datei |
| `decision_checkpoints` | object | Verschachtelt; nur Bool-Keys. Erweiterbar; minimal-Set: `quality_trap_invoked`, `earnings_wait_honored`, `skip_window_carryover_applied` |
| `score_change_summary` | string | Format: `<old>→<new> Δ<signed-int>` oder `unchanged` |
| `operator_notes_short` | string | ≤ 200 Zeichen, freie Notation |
| `skill_meta` | object | Verschachtelt; minimal-Set: `dynastie_depot_version` (string, semver `vX.Y.Z`), `workflow_shape_changed_since_last_trace` (bool) |
| `trace_quality` | string | Enum: `complete` · `partial` (Pilot-Lücken) · `draft` (pre-commit) |

### §18-Sync-Trigger (Spec W6)

1. **Schema-Erstellung** = System-Zustand-Change → Sync-Set: `SYSTEM.md` + `00_Core/log.md` + `STATE.md` Last-Audit + `PIPELINE.md`. *(Erfolgt beim ersten Pilot-Run, nicht im Plan-v1.2-Commit selbst — Spec C4.)*
2. **Erster Per-Analyse-Append (Pilot-Start-Event)** = einmaliger Sync-Trigger → gleiches Sync-Set.
3. **Nachfolgende Per-Analyse-Appends** = NICHT in §18-Sync (analog `score_history.jsonl`, gehört zur Vollanalyse-Sequenz).

### Pilot-Exit-Kriterien GO/NOGO (Final-R1 Gap 1 Closure)

Nach 2-3 Pilot-Iterationen Owner-Review gegen folgende Kriterien — alle vier müssen positiv beantwortbar sein für **GO** (Promotion-Trigger-Vorbereitung); ein FAIL = **NOGO** (Pilot verlängern oder zurückrollen):

| # | Kriterium | Messverfahren | Schwelle GO | Bei NOGO |
|---|-----------|---------------|-------------|----------|
| **K1** | **Vollständigkeit** — sind alle 10 Felder bei jedem Pilot-Append valid gefüllt (keine `partial`/`draft` mehr)? | manueller Read jedes Pilot-Records + Feld-Typen-Check | 100% `complete` über letzte 2 Records | Schema-Lücke identifizieren, Feld-Definition schärfen, weiter piloten |
| **K2** | **Querybarkeit** — beantworten 3 Test-Queries die Question stellbar sind: (a) „welche Vollanalysen haben `quality_trap_invoked=true` UND `earnings_wait_honored=false`?" (b) „welche Source-Types kommen wie oft in `source_bundle` vor?" (c) „welche Vollanalysen haben `workflow_shape_changed_since_last_trace=true`?" | `jq`-Queries gegen `audit_trace_lite.jsonl` | alle 3 Queries liefern in ≤30s ein verwertbares Ergebnis | Schema-Verschachtelung anpassen, ggf. Top-Level-Felder nachziehen |
| **K3** | **Pflegeaufwand** — Operator-Aufwand pro Append vs. Mehrwert | Stoppuhr pro Pilot-Append + Operator-Selbsteinschätzung | ≤ 5 Min Append-Aufwand UND Operator bewertet „würde ich wiederholen" mit ja | Schema vereinfachen, Bool-Keys reduzieren |
| **K4** | **Reviewer-Nutzen** — kann ein späterer Reviewer aus dem Trace-Record allein rekonstruieren, welche Evidence-Family den Score-Change drove? | manuell: 1 historischer Trace + Reviewer-Try ohne Zugriff auf CORE-MEMORY/log.md | „ja, rekonstruierbar" für ≥ 2 von 3 Pilot-Records | `critical_evidence_refs` schärfen oder `operator_notes_short`-Konvention |

### Promotion-Trigger zu Voll-1.9 (Spec W5)

UND-verknüpft (alle drei müssen erfüllt sein):

1. **Empirisch:** ONNX-Aktivierung gemäß §ONNX-ROI-Gate (mind. 3/5 Schwellen, davon 2 objektiv)
2. **Iterativ:** ≥ 2-3 audit-trace-lite-Iterationen abgeschlossen ohne Schema-Churn
3. **Skill-Stabilität:** `dynastie-depot`-Skill stable über mind. 3 vergleichbare Vollanalysen ohne strukturellen Refactor (Beispiele.md-Refactor Item #17 closed)

Ist nur eine Bedingung erfüllt → Voll-1.9 bleibt blocked. **Hohes Audit-Interesse allein überschreibt weder den Stabilitäts-Gate noch den ROI-Gate.**

### Kill-Criterion (P8)

- Pilot-Pflegeaufwand >15 Min pro Append konstant über 2 Pilots → Schema zu schwer, Pilot pausieren, Schema redesignen oder Pilot abbrechen.
- Schema-Churn ≥3 nicht-rückwärtskompatible Änderungen während Pilot-Phase → Idee „lite" gescheitert, zurück zu pre-Pilot-State (Pilot-Records zu Backup, Sektion „abgeschlossen ohne Promotion" markieren).

### Rollback

audit-trace-lite ist additiv (append-only JSONL), Rollback = Schema-Sektion in v1.2 als „Pilot-abgeschlossen-ohne-Promotion" markieren + Pilot-Records optional nach `05_Archiv/audit-trace-lite-pilot-frozen/` verschieben. Kein Code-Eingriff.

---

## §C5-Closures — Cross-File-Reststeller R2-1 + R2-2 (PIPELINE-#42-Block (b))

Beide Reststeller sind **nicht-optional** und blocking für die Workflow-Promotion-Phase (Spec C5).

### R2-1 PIPELINE-#42-Sync-Set-Patch — Closure

**Closure-Test (Spec C5):** PIPELINE-Item #42 zitiert das C2.1-Sync-Set wörtlich oder per Anker-Verweis und benennt `CLAUDE.md` als Authority-Datei.

**Closure-Status:** ✅ Pre-Plan-v1.2-Commit bereits erfüllt — PIPELINE.md Item #42 enthält bereits den Sync-Set-Block (Z. 94 PIPELINE.md):

> *„Sync-Set bei Plan-v1.2-Commit (atomar, ein Commit) — Closure-Test für R2-1: `RUFLO-INTEGRATION-PLAN.md` v1.1→v1.2 (in-place, Versions-Bump) + `CLAUDE.md` Override-Block (Authority — gemäß Spec C2.1 Pflicht-Bestandteil) + `00_Core/SYSTEM.md §Ruflo-Status` (Attestierung) + `00_Core/log.md` (Vault) + `00_Core/STATE.md` Last-Audit + `00_Core/PIPELINE.md` (dieses Item DONE)."*

**Verifikations-Pflicht beim Plan-v1.2-Commit (Task 26):** Pre-Commit-Step bestätigt, dass dieser Sync-Set-Eintrag in PIPELINE-#42 unverändert vorhanden ist und der tatsächlich gestagete Commit-Inhalt **diesem Sync-Set wörtlich entspricht** (kein File extra, kein File fehlt). Bei Diskrepanz → Commit zurückrollen, Sync-Set neu auslegen.

### R2-2 `CLAUDE.md` Z.124 Wortlaut-Harmonisierung — Closure

**Closure-Test (Spec C5):** `CLAUDE.md` Z.124 enthält keine Formulierung mehr, die ad-hoc-Aktivierung ohne benannten Trigger erlaubt.

**Pre-State (v1.1, derzeitige Z.124):**

> *„Reviews/Second-Opinions: Codex bleibt Primary (Memory `feedback_review_via_codex_not_advisor.md`). Ruflo-Swarms ausschließlich bei explizitem User-Auftrag oder definierten Triggern."*

Konflikt: „expliziter User-Auftrag" ist offen genug, dass Hard-Conflict #5 (Z. 97, 122–125) und die spec-neue Named-Trigger-Pflicht (M1 + G3) ad-hoc-Sätze („spawn mal nen Swarm", „lass das via Hive-Mind laufen") als Aktivierungs-Pfad missdeutbar werden.

**Post-State (v1.2-Commit Edit, im Plan-v1.2-Commit Task 18):**

> *„Reviews/Second-Opinions: Codex bleibt Primary (Memory `feedback_review_via_codex_not_advisor.md`). Ruflo-Swarms / Hive-Mind / Stream-Chain / breit aktivierte Worker-Manager-Pipelines werden **ausschließlich** an benannte Trigger der Routing-Table gebunden (analog `!QuickCheck`, `!Analysiere`, `!Rebalancing`, `!SyncBriefing`). Aktuelle Positivliste an benannten Triggern für Ruflo-Workflow-Layer-Aktivierungen: **leer** (Stand: 2026-05-05). Ad-hoc-User-Sätze („spawn mal nen Swarm", „lass das via Hive-Mind laufen", „nutz mal Stream-Chain dafür") aktivieren **nichts** — auch nicht bei vorhandener Listen-Position oder bestätigtem Adoption-Gate (Spec M1 Named-Trigger-Pflicht + G3 3-Felder-Konsistenz-Regel)."*

**Closure-Verifikation (post-Commit):** Re-Read `CLAUDE.md` an genau dem Block, kein Vorkommen mehr von `bei explizitem User-Auftrag oder definierten Triggern` als alleiniger Aktivierungspfad — stattdessen explizite Named-Trigger-Bindung mit aktuell **leerer** Positivliste.

---

## §Final-R1 MED/Gaps Closures (PIPELINE-#42-Block (c))

### MED-1 — M1-Registry-Format ↔ G3 3-Felder-Konsistenz-Regel Zusammenführung

**Konflikt-Befund (Final-R1):** M1 sagt „Format = zwei Felder (`default-workflow-layer = superpowers` + `ruflo-workflow-exceptions: []`)". G3 sagt „aktive Approval = drei Felder (Listen-Eintrag + Gate-Ref + Named-Trigger)". Format-Doku in M1 listet aber nur das Listen-Format, nicht die zwei zusätzlichen Felder.

**Closure (im Plan-v1.2-Commit Task 19, Override-Block-Erweiterung):** M1-Registry-Format wird in `CLAUDE.md` mit dem expliziten 3-Felder-Schema gepflegt:

```yaml
default-workflow-layer: superpowers
ruflo-workflow-exceptions:
  # Beispiel-Eintrag, nicht aktiv:
  # - skill: ruflo-stream-chain-pipeline
  #   gate-ref: "RUFLO-INTEGRATION-PLAN.md v1.X §Adoption-Gates Stream-Chain (G1-G5)"
  #   named-trigger: "!StreamChain"   # muss zusätzlich in Routing-Table existieren
  []   # aktuell leer
```

**Audit-Pflicht (Doctor / SystemAudit):** Bei Lauf prüfen, dass jede `ruflo-workflow-exceptions[i]` alle drei Felder gesetzt hat **UND** der `named-trigger` in der `CLAUDE.md` Routing-Table tatsächlich existiert. Fehlt eines → Skill gilt als NICHT autorisiert, Audit-Lauf MUSS dies als Failure-Mode listen (Spec G3).

### MED-3 — Plan-v1.2-Strukturwechsel-Pflichtliste

**Befund (Final-R1):** Plan-v1.2 muss strukturell sichtbar Variante D verankern; bloßer Header-Bump reicht nicht.

**Closure (durch diese v1.2-Datei selbst erfüllt):**

| Pflicht-Item | Verankerung |
|--------------|-------------|
| Header/Status-Bump auf v1.2 mit Spec-Quelle | ✅ Header-Block oben |
| Rewrite Z.7-Wording „User will Ruflo statt Superpowers nutzen" | ✅ Executive Summary explizit revidiert: „Superpowers-Reaktivierung war kein Architektur-Eingriff, sondern Schließung einer akuten Workflow-Lücke" |
| 1.9-Replace (kein Voll-Trajectory-Recording) | ✅ Sektion `§Phase-1.9-Replace` |
| Re-Basing Stream-Chain unter Adoption-Gate | ✅ Sektion `§Adoption-Gates` (Stream-Chain-Sub-Sektion); Phase-2.5 Roadmap-Entry markiert ASTRONAUT-ARCH |
| Re-Basing Hive-Mind (Phase 3.1) unter Adoption-Gate | ✅ Sektion `§Adoption-Gates` (Hive-Mind-Sub-Sektion); Phase-3.1 Roadmap-Entry markiert ASTRONAUT-ARCH |
| Trennung Historie vs. Gate-Katalog | ✅ Phasen-Sektionen (1.x / 2.x / 3.x / 4.x) bleiben für Historie-/Roadmap-Status; Adoption-Gates sind in eigener Sektion gebündelt |

### Gap 1 — audit-trace-lite Pilot-Exit-Kriterien GO/NOGO

**Befund (Final-R1):** Spec definiert Pilot, aber keine Exit-Kriterien.

**Closure:** ✅ in `§Phase-1.9-Replace` → Pilot-Exit-Kriterien K1-K4 (Vollständigkeit, Querybarkeit, Pflegeaufwand, Reviewer-Nutzen) mit Schwellen + Fail-Pfaden.

### Gap-Hypothese — Double-Trigger-Präzedenz (Superpowers-Default vs. Ruflo-Exception bei User-Intent-Match)

**Hypothese (Final-R1):** Wenn ein User-Intent gleichzeitig zu einem Superpowers-Default-Trigger UND zu einem Ruflo-Exception-Trigger matcht, gibt es kein Tie-Break.

**Closure-Regel (in v1.2 normativ):**

1. **Superpowers-Default hat Vorrang**, solange `ruflo-workflow-exceptions` leer ist (Stand: 2026-05-05).
2. **Bei nicht-leerer Positivliste:** Wenn beide Trigger explizit benannt matchen → User-Rückfrage (analog Routing-Table-Ambiguity-Edge-Case in `CLAUDE.md` „bare Symbol mit Wort-Ambiguität"). **Default = Superpowers**, weil Variante D Superpowers als Workflow-Default normativ verankert; Ruflo-Exception-Pfad nur bei expliziter User-Confirmation.
3. **Bei nur einem Match:** der eindeutige Trigger gewinnt.
4. **Audit-Pflicht:** Jeder Double-Trigger-Pfad-Wechsel (Superpowers → Ruflo-Exception via User-Confirmation) ist in `00_Core/log.md` mit Trigger-Quelle + Confirmation-Snippet zu dokumentieren — verhindert schleichende Promotion-Drift.

**Re-Eval:** Wenn Positivliste je gefüllt wird (per Adoption-Gate-Pass), wird diese Regel im selben Plan-Commit re-validiert; bei Bedarf in `CLAUDE.md` Routing-Table als expliziter Edge-Case-Eintrag verankern.

---

## §Meta-Review-Patches — P4 / P7 / P8 / P9 Closures (PIPELINE-#42-Block (d))

Quelle: `00_Core/RUFLO-PLAN-META-REVIEW.md` §7 (v1.0-Final, abgelegt nach Plan-v1.2-Commit per (h)-Folge-Commit nach `05_Archiv/`).

### P4 — Phase 2.3 §28.2 → §28.1 Repositioning

**Pre-State (v1.1):** Phase 2.3 Codex Dual-Mode für §28.2 Algebra-Δ-Gate.

**Befund (Meta-Review §3):** §28.2 ist deterministisch (`delta_check.py`), kein Halluzinations-Risiko → Codex-Dual-Mode hier nutzlos. Sinnvoller wäre §28.1 (Paper-Befund-Auswahl + ExplainableRecall-Trace) und §29.7 (M&P-Discount-Trigger).

**Post-State (v1.2):** Phase 2.3 wird auf **§28.1** repositioniert. ExplainableRecall-Trace liefert Zertifikat „warum gerade dieses Paper/Evidence-Item", Codex Dual-Mode validiert Auswahl-Plausibilität gegen Wiss-Fundierung. §29.7 M&P-Discount-Trigger bleibt zweiter Anwendungsfall.

**§28.2-Algebra-Gate bleibt Claude-only deterministisch.** Codex-Sparring-Heuristik unverändert (Single-Pass Default; Sparring-Loop nur bei HIGH-Count ≥2 — Memory `feedback_codex_sparring_heuristic.md`).

**Status:** PENDING (Phase 2a-Slot ab ~13.05.2026, frühester Pilot-Run an einer §28.1-Paper-Auswahl).

### P7 — Pending-Insights-Pflege-Regel

**Befund (Meta-Review §3):** Pending-Insights-Buildup-Risk analog APPLIED-LEARNING-20/20-Cap.

**Post-State (v1.2):** **Monatliche Pending-Insights-Review-Cadence** (1× pro Monat, Konsolidierungstag-aligned):

| Schritt | Aktion |
|---------|--------|
| 1 | `wsl -d Ubuntu-24.04 -u root -e bash -lc 'ruflo memory list --namespace patterns'` — Anzahl Pending-Insights ablesen |
| 2 | Falls Anzahl > 30 (Soft-Schwelle): Konsolidierung manuell triggern (`ruflo memory consolidate`) und Outcome in `00_Core/log.md` festhalten |
| 3 | Falls Konsolidierung wiederholt unwirksam (Pending bleibt > 30 ≥3 Monate): Schwelle in `SYSTEM.md §Ruflo-Status` als Drift-Warning markieren, in nächstem Phase-Review (G5) Owner-Entscheid |

**§18-Sync-Trigger:** Monthly-Review-Eintrag = `00_Core/log.md` (kurz: „Pending-Insights-Review YYYY-MM, Anzahl=N, Action=…"); kein voller Sync-Set, weil monatliche Routine kein State-Change ist (außer bei Drift-Warning).

**Verlinkung:** Diese Regel wird zusätzlich als Bullet in `00_Core/APPLIED-LEARNING.md` (Pflege-Regel-Block) referenziert — aber ohne Tier-2-Promotion: APPLIED-LEARNING dokumentiert die Regel als Pointer auf v1.2 hier. (Schreib-Authority bleibt v1.2-Roadmap; APPLIED-LEARNING-Pointer = Discoverability-Maßnahme, keine Authority-Verdoppelung — M4-Rollentrennung.)

### P8 — Kill-Criteria pro Phase explizit

**Befund (Meta-Review §3):** Plan beschrieb Rollback-Pfade, aber keine Stop-Bedingungen.

**Post-State (v1.2 — vollständige Tabelle in `§Kill-Criteria` weiter unten; hier Verweis):**

| Phase | Kill-Trigger (Kurzform) | Detail-Anker |
|-------|-------------------------|--------------|
| 1.8 | Doctor >120s mehrfach in Folge ODER >3 FAIL in 4 Wochen | `§Phase-1.8` |
| 1.9-Pilot | Pflegeaufwand >15 Min/Append konstant 2× ODER ≥3 nicht-rückwärts-kompatible Schema-Churns | `§Phase-1.9-Replace` |
| 2a Memory-Controllers | CausalRecall verschlechtert Pattern-Empfehlungs-Qualität messbar (FP-Rate >25% in 4 Wochen) ODER `adr`-Worker FP-Rate >30% (legitime §-Erweiterungen blockiert) | `§Kill-Criteria` |
| 2a Worker-Manager | Worker-Stuck >30 Min ohne Recovery in 3 Folgewochen | `§Kill-Criteria` |
| 2.3 Codex Dual-Mode (§28.1) | Match-Rate <80% über 5 Pilot-Runs | `§Kill-Criteria` |
| 2b Stream-Chain | Doppel-SSoT-Konflikt zu `dynastie-depot` SKILL.md (=Skill-Pattern aus Pipeline-YAML divergiert messbar von SKILL.md-Sequenz in 2 aufeinanderfolgenden Live-Runs) | `§Kill-Criteria` + `§Adoption-Gates Stream-Chain` |
| ONNX-Aktivierung | <3/5 Schwellen erfüllt ODER FP-Rate ≥20% in Eval-Slot | `§ONNX-ROI-Gate` |
| 3.1 Hive-Mind `!BatchScan` | FLAG-Konsistenz-Drift >10% vs serieller Run in Validation-Run | `§Adoption-Gates Hive-Mind` |
| Allgemein (jede Phase) | „Diese Phase als Fehlversuch abschließen, kein Re-Try"-Pfad explizit dokumentiert in `00_Core/log.md` mit Owner-Begründung; Audit-Eintrag in `STATE.md` Last-Audit | `§Kill-Criteria` |

### P9 — Phase-2-Split 2a / 2b

**Befund (Meta-Review §3):** Phase 2 ist überladen für Eval-Phase mit Pilot-Use-Case; >2 Hebel parallel macht Attribution unscharf.

**Post-State (v1.2):**

| Sub-Phase | Inhalt | Charakter |
|-----------|--------|-----------|
| **2a — Eval (additiv, niedrig-mittel-Risk)** | AgentDB v3 Controllers (Hierarchical/Attestation/Explainable/Causal — Reihenfolge nach Risiko per `§Phase-2a-Reihenfolge`) + Worker-Manager (5 relevante: patterns/adr/consolidate/predict/learning, `adr` initial warn-only) + AIDefence pre-agent-input für Tavily + Drift-Detection-Baseline + Phase-2.3-§28.1-Codex-Dual-Mode (P4) | Pilot-getrieben, isoliert evaluierbar, Rollback je Item |
| **2b — Architektur-Eingriff (kein Eval, ASTRONAUT-ARCH-Gate-pflichtig)** | Stream-Chain Pipeline-Definition für `dynastie-depot`-Skill (`01_Skills/dynastie-depot/pipeline.yaml`); würde zweite Orchestrierungs-SSoT neben SKILL.md einführen | NUR via Adoption-Gate Stream-Chain (siehe `§Adoption-Gates`) — kein Default-Pfad in Phase 2 |

**Konsequenz für Roadmap:** Phase 2 Eval-Slot ab ~13.05.2026 = 2a only. 2b bleibt Adoption-Gate-pflichtig auch wenn 2a vollständig stable wird. Skill-Refactor vermischt Eval-Befund mit Architektur-Wahl — getrennt halten.

---

## §ONNX-ROI-Gate — Phase-2-Eval-Slot (PIPELINE-#42-Block (e))

**Rahmen:** Memory-Bridge ist GENUINE-VALUE als Substrat; ihr Retrieval-Mehrwert ist embedding-sensitive. Aktueller Stand: Mock-Embeddings semantisch schwach. ONNX-Aktivierung ist ein **bounded retrieval-quality experiment**, kein Platform-Milestone (Spec O3).

### Aufspaltung nach Embedding-Abhängigkeit (Spec O1)

| Feature | Embedding-Abhängigkeit |
|---------|------------------------|
| Memory-Bridge (Existenz/Persistenz) | EMBEDDING-INDEPENDENT |
| Memory-Bridge (Retrieval/Search-Quality) | EMBEDDING-SENSITIVE |
| AttestationLog · Doctor-Periodic · AIDefence · Tool-Mode · Context Autopilot · Statusline | EMBEDDING-INDEPENDENT |
| ExplainableRecall · CausalRecall · Hyperbolic Embeddings | EMBEDDING-SENSITIVE |
| Trajectory-Recording | PARTIAL (Recording embedding-unabhängig, RL-Lernwert embedding-sensitiv) |

**Konsequenz:** 8 von 9 Embedding-INDEPENDENT-Features funktionieren ohne ONNX. ONNX ist **kein Phase-1-Blocker**.

### 5 Schwellen-Metriken (Spec O2)

| # | Metrik | Schwelle | Typ |
|---|--------|----------|-----|
| 1 | Recall@3 auf 10-15 Investing-Prompts vs. Mock-Baseline | **+30 Prozentpunkte** | objektiv (System) |
| 2 | Top-1 Retrieval-Accuracy auf bekannten Investing-Lessons | **≥70%** | objektiv (System) |
| 3 | False-Positive-Rate auf Investing-Prompts | **<20%** | objektiv (System) |
| 4 | Operator-Rating „did retrieved pattern materially help this analysis?" | **≥6/10 in 5 von 8 Sessions** | subjektiv (Operator) |
| 5 | Pattern-Search Hit-Rate für 3 spezifische Queries (`earnings-wait-discipline`, `multi-source-drift`, `quality-trap`) | **≥80% mit relevantem Result in Top-3** | objektiv (System) |

### Aggregations-Regel + Guardrail

- **Mindestens 3 von 5 Schwellen erfüllt** UND
- **Von den 3 erfüllten Schwellen müssen mind. 2 objektive System-Metriken sein** (Operator-Rating allein reicht nicht — Spec O2 Guardrail).

### Posture-Regel (Spec O3)

**ROI-Pass öffnet das Gate-Review-Fenster; er aktiviert ONNX nicht.** Schwellen-Erfüllung ist notwendig, aber **nicht hinreichend** für ONNX-Aktivierung. Finale Aktivierung erfordert weiterhin den Approval-Point gemäß Spec G1 (Gate-Owner) + G3 (3-Felder-Konsistenz) + Plan-Update mit Versions-Stempel.

### Eval-Cadence

| Phase | Aktion |
|-------|--------|
| ~13.05. - ~30.06.2026 | Eval-Slot offen, parallel zu 2a Memory-Controllers + Worker-Manager. 8 Vollanalysen-Sessions als Operator-Rating-Pool (4 von Welle-3-Pilot + 4 nachfolgende). |
| ~01.07. (frühester Review) | Owner-Review der 5 Metriken — gegen Aggregations-Regel + Guardrail prüfen. Outcome dokumentiert in `00_Core/log.md`. |
| Bei PASS | Gate-Review-Fenster eröffnet — separater Plan-Bump (v1.3) mit Aktivierungs-Sequenz, Adoption-Gate-Definition für ONNX, 3-Felder-Eintrag in `CLAUDE.md` Override-Block. |
| Bei FAIL | Mock-Baseline ist akzeptabler Status quo. Re-Eval-Cadence = quartalsweise (~01.10., ~01.01.2027). |

### Kill-Criterion (P8)

Eval-Slot Run-Completion <50% (z.B. <4 von 8 Sessions Operator-Rating gefüllt, weil Memory-Bridge im Alltag nicht hilfreich genug erscheint) → Eval-Slot abbrechen, Mock-Baseline als „akzeptierter Status quo" in `SYSTEM.md §Ruflo-Status` festhalten, ONNX deferred auf 2027 oder bis sich konkrete Recall-Notwendigkeit ergibt.

---

## §Cleanup-Track — 131 broken Pfad-Refs (PIPELINE-#42-Block (f))

**Pre-State (Spec C1):** SystemAudit 04.05.2026 hat 131 broken Refs gemeldet, primär `docs/superpowers/plans/*`-Verweise in PIPELINE.md, SYSTEM.md, SESSION-HANDOVER.md, CORE-MEMORY.md.

**Post-Spec-Approval-Konsequenz:** Superpowers-Plugin ist reaktiviert; das `docs/superpowers/plans/`-Verzeichnis existiert wieder. Status muss empirisch verifiziert werden — nicht aus dem Audit-Snapshot ableiten, sondern Re-Audit fahren.

### Cleanup-Sequenz (Phase 1.x parallel zu Welle 3)

| # | Aktion | Befehl / Verfahren |
|---|--------|--------------------|
| 1 | **Re-Audit nach Plan-v1.2-Commit** (post-Task-27) | `python "03_Tools/system_audit.py" --full --json > "05_Archiv/system-audit-snapshots/2026-05-XX-post-plan-v1.2.json"` (Datum aus Commit) |
| 2 | **Klassifizierung** der dann noch verbleibenden broken Refs | aus dem JSON-Snapshot Liste der broken-ref-Pfade extrahieren; pro Pfad: Live-Check (`test -f`) |
| 3a | **Live-Refs** (Plugin liefert File wieder) | keine Aktion; Audit-Drift dokumentieren |
| 3b | **Tote Refs Klasse A — Plan endgültig weg, Re-Generation sinnvoll** (z.B. Track-5b-FRED-Plan, Briefing-v3.1-Cache-Refactor — `00_Core/PIPELINE.md` Z. 102-106 Deferred-Bereich) | per Item entscheiden: (i) Plan via `superpowers:writing-plans` neu erzeugen wenn Trigger eintritt ODER (ii) Ref entfernen mit `[ARCHIVED — siehe 05_Archiv/]`-Marker |
| 3c | **Tote Refs Klasse B — Plan endgültig weg, kein Re-Bedarf** | Ref entfernen / `[ARCHIVED]`-Marker |
| 3d | **Refs auf bewusst-archivierte Files** (z.B. `RUFLO-PLAN-META-REVIEW.md` post-Folge-Commit) | Pfad auf `05_Archiv/`-Position aktualisieren |
| 4 | **Tracking-Item in PIPELINE.md** anlegen (separates Item, NICHT #42), bis broken-Refs-Count = 0 |

### Erfolgskriterium

- Re-Audit nach Plan-v1.2-Commit + Cleanup-Welle: broken-Refs-Count ≤ 20 (nur noch erwartbare Deferred-Plan-Refs).
- Re-Audit nach 4 Wochen: broken-Refs-Count = 0 (nur erwartbare Deferred-Refs in toleriertem Status, dokumentiert in `SYSTEM.md`).

### §18-Sync für Cleanup-Sub-Welle

Cleanup-Item-Done = Pipeline-Item-Status-Change: `00_Core/PIPELINE.md` (Cleanup-Item DONE) + `00_Core/log.md` (Cleanup-Welle-Eintrag) + `STATE.md` Last-Audit (post-Cleanup-System-Audit-Snapshot). Atomarer Commit pro Cleanup-Welle, NICHT pro einzelner Ref-Korrektur (Token-Effizienz).

### Kill-Criterion (P8)

Cleanup-Welle entdeckt strukturelle Refs-Drift (z.B. >50% der Refs nach `02_Analysen/` zeigen auf nicht-existente DEFCON-Files, was auf einen Sync-Lapse hinweist) → Cleanup pausieren, Root-Cause-Audit fahren, Sync-Pflicht-Verletzung in `00_Core/CORE-MEMORY.md §5` als Lesson aufnehmen, dann re-starten.

---

## §Adoption-Gates für ASTRONAUT-ARCH-Features (PIPELINE-#42-Block (g))

**Rahmen:** Variante D braucht Gate-Mechanik für Promotion eines Ruflo-Workflow-Features aus ASTRONAUT-ARCH/CONDITIONAL in den aktiven Status. Diese Sektion operationalisiert Spec G1-G5 für **Stream-Chain** und **Hive-Mind** als die zwei konkreten ASTRONAUT-ARCH-Kandidaten.

### Gate-Mechanik (Spec G1 — Fünf Pflicht-Komponenten je Gate)

1. **Activation-Trigger** — konkrete Bedingung, ab der das Gate überhaupt geprüft wird
2. **Empirical-Success-Test** — messbare Kriterien
3. **Approval-Point** — manuelle Owner-Entscheidung mit dokumentierter Begründung (kein Auto-Promote)
4. **Gate-Owner** — namentlich identifizierte Person/Rolle
5. **Rollback-Path** — explizite Deaktivierungs-Mechanik

**Default = BLOCK (Spec G2):** Gate-Status undokumentiert / Empirical-Test ambiguous / Approval-Point fehlt / Owner uneinig → BLOCK. Aktivierung ohne Gate-Pass → sofortige Deaktivierung + Audit-Eintrag.

**Emergency-Containment-Exception (Spec G2):** Erlaubt nur für **Deaktivierung oder Einschränkung bestehender Komponenten** aus Runtime-Safety- oder Data-Integrity-Gründen. Verboten für Aktivierung neuer Workflow-Layer. Pflicht-Folge: Sofortiger Post-Hoc-Audit-Eintrag (`log.md` + `SYSTEM.md §Ruflo-Status` + `STATE.md` Last-Audit).

**3-Felder-Konsistenz für aktive Approvals (Spec G3):** Listen-Eintrag (`CLAUDE.md` M1-Registry) + Gate-Ref (Plan-Definition mit Plan-Version/Datum) + Named-Trigger (Routing-Table). Fehlt eines → NICHT autorisiert. Audit-Lauf MUSS dies als Failure-Mode listen.

### Adoption-Gate Stream-Chain (Phase 2b)

| Komponente | Definition |
|------------|------------|
| **Activation-Trigger** | Phase 2a vollständig stabil ≥ 4 Wochen (alle Worker ohne Stuck >30 Min, AgentDB-Controllers FP-Rate <20%) **UND** ≥ 2 Live-Runs mit Worker-Manager DONE ohne Skill-Workflow-Konflikt **UND** Operator-Befund: „Skill-SKILL.md-Sequenz ist heute zu opaque/komplex genug, dass eine externe Pipeline-YAML strukturellen Mehrwert hätte" |
| **Empirical-Success-Test** | Pre-Activation Trockentest: Pipeline-YAML (`01_Skills/dynastie-depot/pipeline.yaml`) wird **parallel** zur SKILL.md-Sequenz gepflegt für 2 Vollanalysen-Pilot. Empirisch: (a) keine Stage-Schritt-Drift zwischen YAML und SKILL.md (jeder SKILL.md-Schritt eindeutig zu einer YAML-Stage zuordbar), (b) YAML-Edit-Aufwand ≤ SKILL.md-Edit-Aufwand bei Skill-Änderung in Pilot-Phase (Stoppuhr), (c) Operator-Rating: „YAML reduziert Skill-Verständlichkeits-Schwelle für Externe" ≥6/10 |
| **Approval-Point** | Owner liest Pilot-Ergebnis + bestätigt schriftlich in `00_Core/log.md` (Eintrag: „Stream-Chain Adoption-Gate APPROVE/REJECT — Begründung … — Datum + Plan-Version") |
| **Gate-Owner** | **User (Tobias)** — keine Delegation an Agent/Codex; Plan-Update mit Versions-Stempel + 3-Felder-Eintrag (`CLAUDE.md` M1-Registry + Gate-Ref + Named-Trigger `!StreamChain` neu) erforderlich |
| **Rollback-Path** | (1) `01_Skills/dynastie-depot/pipeline.yaml` löschen ODER nach `05_Archiv/stream-chain-attempt-YYYY-MM/` verschieben; (2) `CLAUDE.md` M1-Registry-Eintrag entfernen + Routing-Table-Trigger entfernen; (3) §18-Sync-Set für Workflow-Deaktivierung gem. C2.1 (Sync-Set: `RUFLO-INTEGRATION-PLAN.md` v1.X+ + `CLAUDE.md` + `SYSTEM.md` + `log.md` + `STATE.md` Last-Audit + `PIPELINE.md` + verbindlicher Audit-Trail in log.md); (4) SKILL.md bleibt einzige Orchestrierungs-SSoT (M4-Restoration) |

**Doppel-SSoT-Risiko-Note:** Stream-Chain führt eine zweite Orchestrierungs-SSoT neben `dynastie-depot` SKILL.md ein. Adoption-Gate prüft Doppel-SSoT empirisch im Pilot. Bei Drift ≥ 2 Schritte zwischen YAML und SKILL.md = Empirical-Test FAIL.

### Adoption-Gate Hive-Mind (Phase 3.1)

| Komponente | Definition |
|------------|------------|
| **Activation-Trigger** | Anzahl Satelliten-Watches/Re-Score-Bedarfe pro Welle (z.B. monatliches Re-Score-Sweep ≥6 Ticker) erreicht ≥3× im selben Quartal **UND** seriell-sequenzieller Run sprengt ein Token-/Latenz-Budget mehrfach (>30 Min Hands-on pro Sweep, dokumentiert in `log.md`) **UND** Phase 2a stable ≥4 Wochen (Memory-Bridge-Recall hilft Pilot-Run-Konsistenz, sonst BatchScan-Worker beginnen ohne Pattern-Kontext) |
| **Empirical-Success-Test** | Validation-Run: serieller Run vs. parallele Hive-Mind-Run für 2 Sweep-Sessions, **identische 11-Satelliten-FLAG-Outcomes** (Konsistenz-Check); Token/Latenz-Reduktion Ziel ≥ 40% bei gleicher FLAG-Konsistenz; **Cost-Cap $5/BatchScan-Run** — Überschreitung = Hard-Stop + Run-Abort. |
| **Approval-Point** | User-Approval (siehe Stream-Chain) plus Plan-Update mit `!BatchScan`-Trigger als Named-Trigger in Routing-Table; vor Approval: Aktuelle Positivliste in M1-Registry bleibt **leer**, Hive-Mind-Pilot wird in `SYSTEM.md §Ruflo-Status` als „pre-Gate-Validation-Run, not authorized" geführt |
| **Gate-Owner** | **User (Tobias)** |
| **Rollback-Path** | (1) `!BatchScan`-Trigger aus Routing-Table entfernen (serieller Default greift); (2) `CLAUDE.md` M1-Registry-Eintrag entfernen; (3) `01_Skills/dynastie-depot/SKILL.md` BatchScan-Sub-Section entfernen falls hinzugefügt; (4) §18-Sync-Set für Workflow-Deaktivierung (siehe Stream-Chain Rollback-Pfad-Punkt 3); (5) Hive-Mind-Worker-Settings in `.claude/settings.json` zurücksetzen |

**FLAG-Konsistenz-Risiko-Note:** Hive-Mind-Worker scoren isoliert je Ticker — Cross-Ticker-Pattern (z.B. Sektor-FLAG-Cascading, BHE/PacifiCorp-Settlement-Effects auf BRK.B-Sub-Score) gehen verloren. Adoption-Gate Empirical-Test prüft das via Validation-Run; FAIL = Hive-Mind ist für Score-Sweep ungeeignet, nur für *triviale* read-only-Sweeps (z.B. Earnings-Calendar-Drift-Check 11 Ticker) zulässig.

### Phase-Review-Kadenz (Spec G5)

**Manueller Owner-Review** beim nächsten definierten Phase-Review-Slot ODER bei explizitem Trigger-Event. **Cadence:**

| Slot | Cadence | Inhalt |
|------|---------|--------|
| **Welle-3-Closure-Review** | nach 1.8-Cadence ≥4 Wochen + audit-trace-lite-Pilot ≥3 Records | Welle-3-Promotion-Entscheid (zu Phase 2a) |
| **Phase-2a-Eval-Review** | nach 2a stable ≥4 Wochen | Stream-Chain-Adoption-Gate-Trigger-Check (öffnet Gate-Review-Fenster oder nicht) |
| **ONNX-ROI-Eval-Review** | ~01.07.2026 frühester Slot | 5-Schwellen-Aggregations-Check |
| **Hive-Mind-Adoption-Gate-Review** | wenn Activation-Trigger erfüllt (≥3× Sweep-Bedarf in einem Quartal) | gegen Validation-Run-Kriterien |
| **Quartalsweise (~01.10., ~01.01.2027)** | regulär | Kill-Criteria-Check je Phase + Pending-Insights-Cleanup-Check (P7-Verlinkung) |

**Doctor-Lauf** als *supporting evidence only* — bestätigt Runtime-Health, kann **keine** Architektur-Entscheidung autorisieren (Spec G5 normativ).

**Keine automatischen Gate-Aktivierungen** — auch wenn Schwellen algorithmisch erfüllt sind, braucht es den Approval-Point (Spec G5).

---

## §00_Core-Cleanup-Disziplin (PIPELINE-#42-Block (h))

**User-Direktive (05.05.2026 abends, Memory `feedback_core_folder_lean_discipline.md`):** `00_Core/` ist Pflicht-Lese-Pfad. Jeder Plan-/Spec-Commit muss Post-Commit-Cleanup mitdenken. Historische / abgelöste Files sofort nach `05_Archiv/`. Versions-Bumps in-place, nicht parallel.

### Generelle Regel

Bei jedem Plan-/Spec-Commit, der ein File in `00_Core/` als historisch/abgelöst markiert:

| Schritt | Aktion |
|---------|--------|
| 1 | Plan-/Spec-Commit selbst (atomar, mit allen Sync-Set-Files) |
| 2 | Folge-Commit: `git mv 00_Core/<file> 05_Archiv/<file>` + log.md-Eintrag + ggf. PIPELINE.md-Folge-Sub-Item DONE |
| 3 | Refs auf das verschobene File in anderen 00_Core-Dateien prüfen — Cleanup-Track berücksichtigt das |

### META-REVIEW-Move (konkret im Folge-Commit nach Plan-v1.2)

**Pre-State:** `00_Core/RUFLO-PLAN-META-REVIEW.md` ist **selbst-deklariert „historisches Pre-Read-Artefakt"** (Z. 11 der Datei). Alle relevanten Patches P4/P7/P8/P9 sind in dieser v1.2-Roadmap verankert (`§Meta-Review-Patches`).

**Move-Trigger (jetzt erfüllt mit Plan-v1.2):**

- ✅ P4 (Phase 2.3 §28.1-Repositioning) verankert in `§Meta-Review-Patches`
- ✅ P7 (Pending-Insights-Pflege-Regel) verankert in `§Meta-Review-Patches`
- ✅ P8 (Kill-Criteria pro Phase) verankert in `§Kill-Criteria` (vollständige Tabelle)
- ✅ P9 (Phase-2-Split 2a/2b) verankert in `§Meta-Review-Patches`
- ✅ alle offenen Findings aus META-REVIEW §10 + §11 abgearbeitet (P1/P2/P3/P5/P6/P10 bereits operational, P4/P7/P8/P9 jetzt v1.2)

**Reihenfolge (verbindlich, atomar nicht möglich, sequentiell zwingend):**

1. (Plan-v1.2-Commit Task 27) — Plan-v1.2 + alle Sync-Set-Files atomar committed
2. (Folge-Commit Tasks 28-30) — `git mv 00_Core/RUFLO-PLAN-META-REVIEW.md 05_Archiv/RUFLO-PLAN-META-REVIEW.md` + `log.md`-Append + `PIPELINE.md`-Folge-Sub-Item DONE
3. (Folge-Commit gleicher Sequenz) — Re-Check: keine 00_Core-Datei verlinkt mehr auf `00_Core/RUFLO-PLAN-META-REVIEW.md` (alle Refs jetzt auf `05_Archiv/...`)

### Future Plan-/Spec-Commit-Cleanup-Pflicht

Bei jedem zukünftigen Plan-/Spec-Commit in `00_Core/` analog Cleanup-Folge mitdenken:

- Welche bestehenden 00_Core-Files werden durch diesen Commit historisch / abgelöst?
- Nach Commit: Folge-Commit mit Move dieser Files nach `05_Archiv/`.
- Refs in verbleibenden 00_Core-Dateien aktualisieren (`05_Archiv/`-Pfad).

**Audit-Klausel:** SystemAudit prüft (Soft-Check, kein Fail): Files in `00_Core/`, die in den letzten 30 Tagen keinen Read-Touch via Routing-Table-Pfad hatten und im Header „historisch" / „v1.0-Final" / „abgelöst" markiert sind, werden als „archiv-Kandidat" gelistet. Liste in `SYSTEM.md §Ruflo-Status` (Soft-Drift-Block).

---

## §Sync-Pflicht — verschärft per Spec C2.1

`CLAUDE.md` Override-Block ist Authority-Datei für M1-Registry, M2-Lifecycle-Owner-Regel, M3-control-plane-Annotation, G3 3-Felder-Konsistenz. Ohne `CLAUDE.md` im Sync-Set entsteht Authority/Runtime/Roadmap-Drift; M4-Rollentrennung kollabiert. Daher gilt ab Plan v1.2 verbindlich:

| Trigger | Pflicht-Sync-Set (atomar, ein Commit) |
|---------|---------------------------------------|
| **Plan-v1.2-Commit** (Roadmap-Promotion) | `00_Core/RUFLO-INTEGRATION-PLAN.md` (v1.2) + `CLAUDE.md` Override-Block (Authority) + `00_Core/SYSTEM.md §Ruflo-Status` (Attestierung) + `00_Core/log.md` + `00_Core/STATE.md` Last-Audit + `00_Core/PIPELINE.md` |
| **Workflow-Promotion** (Adoption-Gate-Pass: ASTRONAUT-ARCH/CONDITIONAL → ACTIVE) | wie oben + M1-Registry-Update in `CLAUDE.md` + G3-3-Felder-Konsistenz nachweisbar (Listen-Eintrag + Gate-Ref + Named-Trigger) |
| **Workflow-Deaktivierung** (Rollback gem. G1 Rollback-Path oder G2 Emergency-Containment) | wie oben + verbindlicher Audit-Trail-Eintrag in `00_Core/log.md` mit Begründung + Datum + Owner |

**Operative Pflicht (PIPELINE-#42-R2-1-Closure):** PIPELINE-Item-#42 zitiert das Sync-Set wörtlich (Z. 94 PIPELINE.md). Jeder zukünftige Plan-Bump-Commit (v1.3+) MUSS ein analoges Sync-Set in seinem PIPELINE-Item benennen, sonst gilt der Plan-Commit als unvollständig.

### Verhältnis zu §18-Sync (INSTRUKTIONEN.md §18 v2.3)

§18 ist die generelle Sync-Pflicht für Score/FLAG/Sparraten-Changes (`PORTFOLIO.md` + `score_history.jsonl` + `Faktortabelle.md` + `log.md` + `CORE-MEMORY` + xlsx-Tools + `config.yaml`). Diese hier definierte Sync-Pflicht für Plan-Roadmap-Commits **ergänzt §18 für die Roadmap-Domain** und ist nicht-überlappend.

Multi-Event-Aktion (z.B. Plan-Bump-Commit fällt zeitlich zusammen mit einer Score-Move): **Union beider Sync-Sets** (`PORTFOLIO.md` aus §18, `CLAUDE.md` aus dieser Pflicht, etc.) — analog §18-v2.3-Multi-Event-Union-Regel.

---

## §Kill-Criteria pro Phase (P8 vollständig)

Jede Phase / jeder Adoption-Gate hat einen expliziten Stop-Trigger. „Diese Phase als Fehlversuch abschließen, kein Re-Try"-Pfad ist immer dokumentiert in `00_Core/log.md` mit Owner-Begründung; Audit-Eintrag in `STATE.md` Last-Audit.

| Phase / Item | Kill-Trigger | Reaktion |
|--------------|--------------|----------|
| **1.8 Doctor-Periodic-Cadence** | Doctor-Run >120s in **≥2 aufeinanderfolgenden Runs** (Performance-Drift) ODER ≥3 FAIL-Runs in 4 Wochen (Health-Regression) ODER 2 aufeinanderfolgende Wochen Cadence komplett ausgefallen | Cadence pausieren, Root-Cause, dann re-aktivieren oder skippen |
| **1.9-Replace audit-trace-lite-Pilot** | (a) Pflegeaufwand >15 Min/Append konstant über 2 Pilots **ODER** (b) ≥3 nicht-rückwärtskompatible Schema-Churns während Pilot-Phase | (a) Schema redesignen oder Pilot abbrechen / (b) Pilot „abgeschlossen ohne Promotion", Records nach `05_Archiv/audit-trace-lite-pilot-frozen/` |
| **2a Memory-Controllers** | (a) CausalRecall verschlechtert Pattern-Empfehlungs-Qualität messbar (FP-Rate >25% in 4 Wochen) **ODER** (b) AttestationLog-Persistenz korrumpiert in 2 Wochen ein nachweisbares Memory-Op-Logging | (a) zurück auf Pure-Similarity / (b) AttestationLog deaktivieren, Root-Cause Backend-Pfad |
| **2a Worker-Manager** | (a) Worker-Stuck >30 Min ohne Recovery in 3 Folgewochen **ODER** (b) `adr`-Worker FP-Rate >30% (legitime §-Erweiterungen blockiert) | (a) Worker-Manager pausieren, Root-Cause / (b) `adr` permanent auf warn-only |
| **2.3 Codex Dual-Mode (§28.1)** | Match-Rate <80% über 5 Pilot-Runs ODER Codex-Spawn-Latenz >2 Min mehrfach (Operator-Friction) | Worker zurückziehen, §28.1-Workflow nicht formalisiert genug |
| **2a AIDefence pre-agent-input für Tavily** | False-Positive-Block legitimer Tavily-Outputs >2× pro Woche | von blocking auf warn-only |
| **2b Stream-Chain (Adoption-Gate)** | Doppel-SSoT-Konflikt zu `dynastie-depot` SKILL.md (=Skill-Pattern aus Pipeline-YAML divergiert messbar von SKILL.md-Sequenz in 2 aufeinanderfolgenden Live-Runs) | YAML löschen / nach `05_Archiv/`, Adoption-Gate REJECT-Eintrag in log.md |
| **ONNX-Aktivierung** | <3/5 Schwellen erfüllt ODER FP-Rate ≥20% in Eval-Slot ODER Eval-Slot-Run-Completion <50% | ONNX deferred ≥3 Monate, Mock-Baseline akzeptiert |
| **3.1 Hive-Mind `!BatchScan`** | FLAG-Konsistenz-Drift >10% vs serieller Run in Validation-Run ODER Cost-Cap $5/Run in ≥2 von letzten 5 Validation-Runs gerissen | Adoption-Gate REJECT, `!BatchScan`-Trigger nicht aktiviert |
| **Cleanup-Track 131 Refs** | Strukturelle Refs-Drift entdeckt (z.B. >50% der `02_Analysen/`-Refs zeigen auf nicht-existente DEFCON-Files) | Cleanup pausieren, Root-Cause-Audit, Sync-Pflicht-Verletzung als Lesson in CORE-MEMORY §5 |

**Allgemeine Audit-Klausel:** Bei Kill-Trigger-Auslösung **immer**: (1) Audit-Eintrag in `00_Core/log.md` mit Trigger-Beweis (Logs, Numbers, Screenshots), (2) Phase-Status-Update in `SYSTEM.md §Ruflo-Status` auf „killed YYYY-MM-DD" mit Begründung, (3) `STATE.md` Last-Audit dokumentiert den Vorfall in Critical-Alerts (≤10 Tage), (4) Adoption-Gate (falls relevant) bleibt blockiert bis explizite Re-Activation-Begründung in nächstem Plan-Bump.

---

## Phase 1 — Foundation (HISTORISCH, alle DONE)

### Phase-1-Historie-Snapshot

| Schritt | Inhalt | Commit | Datum |
|---------|--------|--------|-------|
| 1.1 | Override-Block in `CLAUDE.md` (Hard-Conflicts 9, Soft-Conflicts 4, Compatible 7) | `c9a3ed5` | 28.04.2026 |
| 1.2 | ADR-048 Auto Memory Bridge (path-scoped, NICHT `allProjects=true`) — WSL-Backend `/home/tobia/.local/share/ruflo/memory` | `e983102` | 30.04.2026 |
| 1.3 | ADR-050 Intelligence Loop Top-K=3 | `e983102` | 30.04.2026 |
| 1.4 | ADR-051 Context Autopilot | `e983102` | 30.04.2026 |
| 1.5 | Custom Tool-Mode `dynastie` (env `CLAUDE_FLOW_TOOL_GROUPS=memory,monitor`) | `e983102` | 30.04.2026 |
| 1.6 | Statusline aktiviert, DDD-Bar disabled | `e983102` | 30.04.2026 |
| 1.7 | 6-Hook-Subset (session-start/end, pre/post-task, pattern-store/search), Rest 21 explizit `enabled: false` | `e983102` | 30.04.2026 |
| Welle 0 | WSL-Foundation (Ubuntu-24.04 + nodejs 20.20.2 + ruflo v3.6.11) | `7b3c7d1` | 30.04.2026 |
| Bridge-Coherence-Welle | 15 Files Code→Dynastie + Index 19→35 | `7733094` | 02.05.2026 |

**Welle 3 (1.8 + 1.9-Replace):** PENDING — siehe §Phase-1.8 + §Phase-1.9-Replace.

**Pre-Conditions Welle 3:** ✅ alle erfüllt (Earnings-Window 28./29.04. abgeschlossen + Phase 1.2-1.7 operational + Spec-Approval erfolgt + Plan-v1.2-Commit erfolgt).

---

## Phase 2 — Eval-Phase (Sub-Split 2a/2b per P9)

### Phase 2a — Eval (additiv, niedrig-mittel-Risk)

Ab ~13.05.2026, parallel zu Welle-3-Stabilisierung.

| Schritt | v1.1-Inhalt | v1.2-Status |
|---------|-------------|-------------|
| 2.1 AgentDB Controllers | HierarchicalMemory → AttestationLog → ExplainableRecall → CausalRecall (Reihenfolge nach Risiko) | DEFER ab ~13.05., Reihenfolge unverändert |
| 2.2 Worker-Manager 5 relevante | patterns, adr (initial warn-only), consolidate, predict, learning | DEFER ab ~13.05., `adr`-Warn-only-Klausel verbindlich |
| 2.3 Codex Dual-Mode | **§28.1 statt §28.2** (P4) | REPOSITION DONE in v1.2; Pilot ab ~13.05. |
| 2.4 AIDefence pre-agent-input für Tavily | unverändert | DEFER ab ~13.05. |
| 2.6 Hyperbolic Embeddings | Sektor-Taxonomie | CONDITIONAL — ONNX-Pre-Condition (siehe §ONNX-ROI-Gate) |
| 2.7 Drift-Detection-Baseline | unverändert | DEFER ab ~13.05. |

### Phase 2b — Architektur-Eingriff (Adoption-Gate-pflichtig)

| Schritt | v1.1-Inhalt | v1.2-Status |
|---------|-------------|-------------|
| 2.5 Stream-Chain Pipeline-YAML | `01_Skills/dynastie-depot/pipeline.yaml` | ASTRONAUT-ARCH — siehe §Adoption-Gates Stream-Chain. NICHT Default-Phase-2-Pfad |

**Erfolgskriterium 2a (Woche 6 Review):** Codex Algebra-Gate-Match-Rate ≥80% über 5 §28.1-Pilot-Runs · AIDefence-Tavily False-Positives <2/Woche · HierarchicalMemory ≥3 Patterns spontan zu Semantic promoted · Worker `patterns` APPLIED-LEARNING-Duplicate-Count rückläufig.

**Rollback Phase 2a:** Jeder Schritt isoliert deaktivierbar. `adr`-Worker zuerst zurückziehen wenn nervig.

**Rollback Phase 2b:** Adoption-Gate REJECT-Pfad (siehe §Adoption-Gates Stream-Chain Rollback-Path).

---

## Phase 3 — Use-Case-getrieben (Adoption-Gate-pflichtig)

Nur wenn Phase 1 + 2a stable ≥4 Wochen UND Use-Case-Trigger empirisch dokumentiert.

| Schritt | Inhalt | v1.2-Status |
|---------|--------|-------------|
| 3.1 Hive-Mind für `!BatchScan` | Hierarchical Topology, Strategic Queen, max 8 Worker, Cost-Cap $5/Run | ASTRONAUT-ARCH — siehe §Adoption-Gates Hive-Mind |
| 3.2 Claims-System für Codex-Sparring | Stuck-Detection >30 Min → STEALABLE | Use-Case-getrieben — eigener Adoption-Gate falls aktiviert (Activation-Trigger: ≥3 Codex-Sessions >5 Min in einem Monat) |
| 3.3 Multi-Agent Security Consensus für Score-Disagreement | 3 Agents (Claude-Strat, Claude-Skeptic, Codex) bewerten | Use-Case-getrieben — kein Default; eigener Adoption-Gate bei FLAG-Edge-Case-Häufung |
| 3.4 Browser-Automation für `annual-*`-Skills | Migration je Skill, Trajectory-Learning | Use-Case-getrieben — eigener Adoption-Gate je Skill |
| 3.5 MCP Multi-Client für Mobile-Workflow | HTTP-Transport, ChatGPT-Mobile-Connector | Use-Case-getrieben — Sicherheits-Implikation bei externem Tunnel; eigener Adoption-Gate |

**Default-Tendenz:** SKIP wenn Activation-Trigger nicht empirisch belegt. Memory `feedback_review_via_codex_not_advisor.md` bleibt unberührt — keine 3.x-Promotion ändert die Codex-als-Primary-Review-Regel.

**v1.1-Operational-Detail-Pointer (Codex-R1 MED-4 Fix):** Detaillierte v1.1-Beschreibung der Phase-3.x-Schritte (Hierarchical Topology + Strategic Queen + Cost-Cap-Mechanik / Stuck-Detection + Visual-Board / 3-Agent-Consensus + calculateSecurityConsensus-API / Browser-Refactor-Aufwandsschätzung / MCP-HTTP-Tunnel-Sicherheit) bleibt im Backup `05_Archiv/ruflo-phase1.2-backups/RUFLO-INTEGRATION-PLAN-v1.1-pre-v1.2-rewrite.md` (Z. 315-368) zugänglich. Wenn ein 3.x-Adoption-Gate aktiviert wird, ist der Backup-Block der Ausgangstext für den dann zu schreibenden Phase-3.x-Detail-Plan.

---

## Phase 4 — Optional & langfristig (HOCH-Risiko, alle Alpha/experimentell)

Default-Tendenz: **SKIP wenn unklar.** Jeder 4.x-Punkt hat eigenen Eval-Zyklus mit Stop-Criterion „Bringt es nachweislich Mehrwert über Phase 1-3 hinaus, oder fügt es nur Komplexität hinzu?"

| Schritt | Inhalt | v1.2-Status |
|---------|--------|-------------|
| 4.1 plugin-prime-radiant | Hallucination-Prevention via Consensus, Causal Inference + Consensus Verification | ASTRONAUT-ARCH; nur evaluieren wenn 1-3 stable + konkreter Use-Case-Beleg |
| 4.2 plugin-cognitive-kernel | Miller's Law (7±2)-Check der 28-Faktor-Bewertung | ASTRONAUT-ARCH |
| 4.3 plugin-hyperbolic-reasoning | Taxonomic Inference | ASTRONAUT-ARCH (ONNX-pre-condition) |
| 4.4 Granger Causality auf `score_history.jsonl` | GraphTransformerService — Faktortabelle-Refactor-Vorschläge | ASTRONAUT-ARCH; Pre-Condition: ≥30 Score-Records (aktueller Stand: ~33; Schwelle erreicht, aber Use-Case-Trigger fehlt) |
| 4.5 Guidance Library (Hard Gates) | INSTRUKTIONEN.md §18 + §28.2 zu PolicyBundle | ASTRONAUT-ARCH; warten auf Alpha-Exit |
| 4.6 Pattern-Export als Backup | Memory + APPLIED-LEARNING als RVF-File | OK-zu-eval (additiv, niedrig-Risk) wenn konkreter Backup-Bedarf entsteht |
| 4.7 Helper-Scripts vs. eigene `03_Tools/` | Eval pro Helper | Use-Case-getrieben, kein Default |

**Risiko: HOCH** — alle alpha/experimentell, plugin uninstall via npm + Guidance via env-flag jederzeit reversibel.

**v1.1-Operational-Detail-Pointer:** Vollständige v1.1-Beschreibung der Phase-4.x-Punkte (6 mathematische Engines plugin-prime-radiant / Miller's-Law-7±2-Mechanik / Granger-Causality-GraphTransformerService / Guidance-PolicyBundle / RVF-Export / Helper-Migration-Eval) bleibt in `05_Archiv/ruflo-phase1.2-backups/RUFLO-INTEGRATION-PLAN-v1.1-pre-v1.2-rewrite.md` (Z. 370-425) verfügbar.

---

## §Audit-Cadence

| Cadence | Was | Trigger / Slot |
|---------|-----|----------------|
| **Pre-Phase-Gate** | Doctor-Lauf vor jedem Phase-Sprung | manuell |
| **Wöchentlich (Welle-3-Phase)** | 1.8 Doctor-Cadence-Snapshot | jeden Montag |
| **Welle-3-Closure-Review** | Promotion-Entscheid 1.8 + 1.9-Pilot zu Phase 2a | nach 1.8 ≥4 Wochen + 2-3 Pilot-Records |
| **Phase-2a-Eval-Review** | Worker-Stabilität, Memory-Controllers-FP, AIDefence-False-Positives | nach 2a stable ≥4 Wochen |
| **ONNX-ROI-Eval-Review** | 5-Schwellen-Aggregation | ~01.07.2026 frühester Slot |
| **Pending-Insights-Review (P7)** | `ruflo memory list --namespace patterns` Anzahl-Check | monatlich, Konsolidierungstag-aligned |
| **Quartalsweise** | Kill-Criteria-Check je Phase + Cleanup-Track-Stand | ~01.10.2026, ~01.01.2027, ... |
| **Adoption-Gate-Trigger-Reviews** | Stream-Chain / Hive-Mind / ONNX bei Activation-Trigger-Match | ad-hoc |

---

## §Resumption-Hinweise

### Bei neuer Session
1. `Session starten` lesen → `STATE.md` + `PORTFOLIO.md` (Routing-Table-Default).
2. Falls Critical-Alert „Plan-v1.2 PENDING/in-progress" → diese Datei als Roadmap-Kontext laden, Welle-3-Status in §Phase-Overview lesen.
3. Phase-Sprung-Pflicht: Pre-Phase-Gate-Doctor-Lauf VOR jeder neuen Welle.

### §18-Sync-Reminder (operational)
- Plan-Bump (v1.2 → v1.3+) = `CLAUDE.md` MUSS im Sync-Set sein (siehe §Sync-Pflicht).
- Adoption-Gate-Pass = M1-Registry-Update in `CLAUDE.md` + G3-3-Felder-Konsistenz.
- Workflow-Deaktivierung = Audit-Trail-Eintrag in `log.md` Pflicht.
- §18 (Score/FLAG/Sparraten) und diese Roadmap-Sync-Pflicht überlappen nicht; bei Multi-Event = Union-Set.

### Quellen
- Spec: `docs/superpowers/specs/2026-05-05-ruflo-superpowers-coexistence-design.md` (USER-APPROVED 05.05.)
- Historisches Pre-Read-Artefakt (Plan-v0/v1.0-Bewertung): `05_Archiv/RUFLO-PLAN-META-REVIEW.md` (verschoben im Folge-Commit nach Plan-v1.2)
- USERGUIDE.md v3.5 lokal: `/c/Users/tobia/Downloads/USERGUIDE.md` (read-only Referenz für Feature-Definitionen)
- Repo: https://github.com/ruvnet/ruflo
- Diese Datei: einzige SSoT für Ruflo-Roadmap. Bei Plan-Änderungen Versions-Stempel oben aktualisieren UND `CLAUDE.md` Override-Block (Authority) — sonst Drift.

---

## Was diese Roadmap NICHT macht

- Keine Migration zu Codex als Primary-Platform (Claude Code bleibt Workflow-Owner)
- Keine Cloud-Skalierung (Single-User stays)
- Keine Wiki/Vault-Auto-Generation aus AgentDB
- Keine Auto-Pflege von INSTRUKTIONEN.md §§ (Tier-3-Regeln bleiben manuell)
- Keine Aktivierung von Patterns/Plugins die Code-Domain sind
- Keine Auto-Promotion eines Ruflo-Workflow-Skills, auch wenn er „besser aussieht" — Adoption-Gate-Pflicht (Spec G1-G5)
- Keine Routing-Table-Erweiterung um Toolset-Spalte (Variante C explizit verworfen in Spec)
- Keine starre Domänen-Trennung (Variante A explizit verworfen)
- Keine freie Per-Use-Case-Auswahl ohne Gates (Variante B explizit verworfen)

---

*Plan-v1.2 Final | 2026-05-05 | Spec-approved Coexistence Variante D | Welle 3 PENDING 05.-12.05.2026 post-BRK.B-Tag-+1 | nächster Phase-Review = Welle-3-Closure-Review nach 1.8-Cadence ≥4 Wochen + audit-trace-lite-Pilot ≥3 Records.*

