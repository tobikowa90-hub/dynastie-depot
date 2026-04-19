# Design: Paper-Integration systemweit (Track 3)

**Stand:** 19.04.2026 | **System:** Dynasty-Depot DEFCON v3.7.2 | **Status:** APPROVED (pending user final review)

**Vorgänger:** Paper-Ingest & §29 Retrospective-Gate (commit `f915e5f`, Track 2 abgeschlossen).

**Scope-Trigger:** SESSION-HANDOVER.md vom 19.04. Mittag — Track 3 "Paper-Integration systemweit" pending seit 18./19.04. Nacht-Session (4 Papers in Vault ingested + §29 eingeführt, operative Ausstrahlung noch offen).

---

## 1. Context & Motivation

Am 18./19.04.2026 wurden 4 wissenschaftliche Papers ingested:

1. **Bailey et al. 2015** — Probability of Backtest Overfitting (PBO/CSCV)
2. **Aghassi et al. 2023** — Fact, Fiction, and Factor Investing (AQR)
3. **Flint & Vermaak 2021** — Factor Information Decay (Half-Life-Konzept)
4. **Palomar 2025** — Portfolio Optimization (Ch 6 Risk-Metrics, Ch 8.2 Seven Sins)

Daraus entstanden:
- **§29 Retrospective-Analyse-Gate** (6 Sub-Gates; §29.4 + §29.5 sofort aktiv, Rest Review 2028-04-01)
- **9 neue Vault-Seiten** (4 Source + 5 Concept)
- **2 modifizierte Synthesen** (Backtest-Methodik-Roadmap, Wissenschaftliche-Fundierung-DEFCON)
- **CORE-MEMORY §5 Lektion** "4-Paper-Triage"
- **Skill-Bullets** in dynastie-depot + backtest-ready-forward-verify

**Lücke (dieser Spec):** Die darüber hinausgehende operative Integration — Vault-Cross-Links zu 11 Satelliten-Pages + 6 defcon-Concepts + ~10 bestehenden Concepts, Skill-Verankerung, INSTRUKTIONEN-Querverweise, taktisch ableitbare operative Regeln (Monthly-Refresh für Investment-FLAGs, Portfolio-Return-Persistenz) — steht aus.

**User-Anforderung (19.04. Mittag):** "Maximum Nutzen aus Papers ziehen. Applied-Learning-Regel ist sinnvoll aber hier zu streng. Wenn sich taktisch gute und verbesserte operative Regeln ableiten lassen, nicht vernachlässigen."

**Applied-Learning-Regel (CLAUDE.md, 3× bestätigt):** *"Paper-Ingest ≠ System-Update: Wissenschaft validiert Regeln, erzwingt keine neuen — Redundanz-Check vor jeder Scoring-Erweiterung."*

**Spannung auflösen:** Leseart "prozedural" — Paper-Ingest allein reicht nicht, aber *nach Triage mit Evidence-Bedarfs-Nachweis* können Regeln entstehen. §29 selbst ist bereits so entstanden. Dieser Spec folgt derselben Disziplin.

---

## 2. Architektur — 4-Layer-Trennung

Jede Paper-getriebene Ergänzung wird einem Layer zugeordnet. **Cross-Layer-Spillover ist explizit verboten** (Guardrail):

| Layer | Inhalt | Paper-Einfluss |
|-------|--------|----------------|
| **Scoring-Kern** | DEFCON-Gewichte, FLAG-Typen, Columns, Thresholds | ❌ Keiner (Applied-Learning strikt) |
| **Monitoring** | Cadence-Regeln (wann Refresh? wann Snapshot?) | ✅ R1 (Flint-Vermaak) |
| **Dokumentation** | Vault-Seiten, Skill-Texte, INSTRUKTIONEN-Querverweise, Ticker-Pages | ✅ A+B+C+R4 |
| **Validation/Retrospective** | PBO, Walk-Forward, Seven-Sins, Portfolio-Metriken | ✅ §29 (bereits) + R5-Infrastruktur |

**Guardrail:** Walk-forward/k-fold/randomized Backtests (Palomar Ch 8.4) **nur im Validation-Layer**, nie im Live-Analyse-Workflow.

**Guardrail (Codex-ergänzt):** **Keine versteckten Workflow-/Trigger-Änderungen in Skills/Tools.** Keine neuen automatischen Trigger, keine zusätzlichen Pflichtschritte in `!Analysiere`/`!QuickCheck`/Archiv-Pipeline außer den ausdrücklich in Phase 2/3/4 spezifizierten.

---

## 3. Scope-Items

### A — Vault-Cross-Links (Layer: Dokumentation)

- **11 Satelliten-Entity-Pages** (ASML, AVGO, MSFT, V, TMO, VEEV, SU, BRKB, COST, RMS, APH): thematisch passende Paper-/Concept-Verweise
- **6 defcon-Concepts** (DEFCON-System, Score-Archiv, Backtest-Ready-Infrastructure, CapEx-FLAG, FLAG-Event-Log, Analyse-Pipeline): §29-Rückverweis + Paper-Anker
- **~10 bestehende Konzept-Pages** (Moat-Taxonomie-Morningstar, QMJ-Faktor, Buffett-Faktorlogik, FCF-Primacy, Update-Klassen-DEFCON, F-Score-Quality-Signal, Gross-Profitability-Premium, Accruals-Anomalie-Sloan): "Wissenschaftliche Fundierung"-Abschnitt mit Aghassi/Palomar-Zitat

### B — Skill-Verankerung (Layer: Dokumentation)

- `01_Skills/dynastie-depot/SKILL.md` — Paper-Zitate an Workflow-Schritten (Fundamentals-Review → Aghassi; Moat-Validation → Palomar-QMJ)
- `01_Skills/backtest-ready-forward-verify/SKILL.md` — §29-Querverweis an Schritt 7 + Seven-Sins-Anker
- `03_Tools/backtest-ready/README.md` — Paper-Kontext-Header (PBO/§29)
- `03_Tools/portfolio_risk.py` + `03_Tools/briefing-sync-check.ps1` + `03_Tools/morning-briefing-prompt-v2.md` — inline-Kommentare mit Paper-Anker wo relevant (Excel-Tools bleiben unangetastet)

### C — INSTRUKTIONEN-Querverweise (Layer: Dokumentation)

- §18 Sync-Pflicht → Anker zu §29.5 Sin #2 (Look-Ahead)
- §27 Scoring-Hygiene → Anker zu §29.4 (t-Hurdle)
- §28 Migration → Anker zu §29.1 (PBO), §29.5 (Seven-Sins)
- §29 → Rückverweise-Liste + Paper-Anker präzisieren

### R1 — Monthly-Refresh für aktive Investment-FLAGs (Layer: Monitoring)

**Platzierung:** Neue **§30 Live-Monitoring & Cadence** (nicht §29, weil §29 Retrospective-Gate ist).

**Begründung:** Flint-Vermaak 2021 — Investment-Faktor-Half-Life ≈ 1 Monat. Earnings-Trigger-Cadence (~3M) ist zu träge für aktive Investment-FLAGs.

**Constraints (Codex-verschärft):**
- Nur **aktiver FLAG** = binär ausgelöst in `flag_events.jsonl` ohne Resolution → R1 pflicht
- **Schema-Watch (nicht FLAG-aktiv)** (neu) = schema-getriggert, aber bewusst nicht aktiviert (wie TMO fcf_trend_neg 18.04. WC-Noise) → R1 **nicht** automatisch pflicht
- Aktueller Live-Scope: **MSFT CapEx/OCF 83.6%** (FLAG aktiv) → Monthly-Refresh pflicht
- TMO fcf_trend_neg: Schema-Watch, **nicht** automatisch Monthly-Refresh (23.04. Q1 = natürliches Resolve-Gate)
- **Keine Auto-Rescore** — nur Prüfung bestehender Trigger, keine neue Punkte-Logik

**Applied-Learning-Wächter:** §30-Cadence-Ausweitung auf weitere Faktor-Klassen (z.B. Quality, falls Half-Life <4M beobachtet) erfordert Applied-Learning-Re-Review — keine stille Erweiterung.

### R4 — Factor-Exposure-Block pro Satelliten-Page (Layer: Dokumentation)

**Struktur (Codex-spezifiziert):** Feste 5-Zeilen-Struktur pro Satellit, Werte `stark / moderat / schwach / n.a.` (letzteres nur wenn konzeptionell nicht ableitbar).

**Template (Muster, pro Ticker mit konkreten Werten + Begründung zu füllen):**

```markdown
## Factor-Exposure (Aghassi 2023)
- **Value:** {stark|moderat|schwach|n.a.} — {1-Satz Begründung, z.B. "Fwd P/E 28 über 5J-Median 22"}
- **Quality:** {stark|moderat|schwach|n.a.} — {z.B. "ROIC ~30% > WACC 9%, Moat wide"}
- **Momentum:** {stark|moderat|schwach|n.a.} — {z.B. "6M RelStärke +8pp vs SPY"}
- **Defensive:** {stark|moderat|schwach|n.a.} — {z.B. "Beta 0,8; stabile Cashflows"}
- **Investment:** {stark|moderat|schwach|n.a.} — {z.B. "CapEx/OCF ~25% stabil, kein Overspending-Signal"}
```

**Scope:** Nur 11 Satelliten. Ersatzbank (7 Pages: GOOGL, ZTS, PEGA, MKL, NVDA, SNPS, RACE, DE, SPGI) ausgenommen — kein Live-STATE-Bezug.

**Strikt dokumentativ — keine Score-Wirkung.** Kein Mapping von Factor-Stärke zu DEFCON-Punkten (verdeckter Scoring-Change).

### R5 — Portfolio-Return-Persistenz (Layer: Infrastruktur)

**Begründung:** Palomar Ch 6 + CORE-MEMORY §5 "Sin #2 Look-Ahead proaktiv vermeiden". Jeder nicht gespeicherte Monat ist irreversibel verloren — deshalb **vor R1 starten** (Zeitwert).

**Dateien:**
- `05_Archiv/portfolio_returns.jsonl` (neu)
- `05_Archiv/benchmark-series.jsonl` (neu — eigene Benchmark-Zeitreihe, nicht retrospektiv aus SPY rekonstruiert)
- `03_Tools/portfolio_risk.py` — neuer `--persist daily`-Modus

**Granularität:** **Daily** (nicht Weekly) — Sortino/Calmar/Max-DD/IR verlieren bei Weekly Drawdown- und Pfad-Information.

**Schema (pro Record, Codex-spezifiziert):**

```json
{
  "schema_version": "1.0",
  "date": "YYYY-MM-DD",
  "portfolio_value_gross": 1234.56,
  "cashflow_net": 285.00,
  "portfolio_return": 0.0023,
  "benchmark_value": 5678.90,
  "benchmark_return": 0.0015,
  "positions": [
    {"ticker": "AVGO", "weight_eod": 0.12, "price_eod": 234.56, "value_eod": 148.27},
    {"ticker": "MSFT", "weight_eod": 0.08, "price_eod": 412.34, "value_eod": 98.96}
  ]
}
```

**Cashflow-Trennung** kritisch — sonst Return-Rekonstruktion bei Sparraten-Einzahlungen fehleranfällig.

---

## 4. Execution-Phasen

**Batching-Strategie B1.5** — Risiko-Gradient + Codex-präzisiertes Vorziehen von R5 (Zeitwert):

### Phase 1a — Satelliten + R4 Factor-Exposure-Blocks

**Dateien:** 11 Satelliten-Pages (ASML, AVGO, MSFT, V, TMO, VEEV, SU, BRKB, COST, RMS, APH)

**Acceptance (gehärtet):**
- Pro Satelliten-Page: genau 1 standardisierter 5-Zeilen-Factor-Exposure-Block
- Pro Satelliten-Page: min. 1 expliziter Link auf neues Paper oder neue Synthese
- Format-Gleichheit aller 11 Blöcke (identischer Header, identische Reihenfolge der 5 Faktoren)

**Review:** User-Review (Stichprobe 3 Ticker)

**Commit:** `feat(vault): paper-integration phase 1a — satellites + factor-exposure blocks`

### Phase 1b — Concept-Cross-Links + Index/Log

**Dateien:** 6 defcon-Concepts + ~10 bestehende Concepts + index.md + log.md

**Acceptance:**
- Pro defcon-Concept: min. 1 §29-Rückverweis + 1 Paper-Anker
- Pro bestehendem Concept: "Wissenschaftliche Fundierung"-Abschnitt mit Paper-Zitat
- index.md aktualisiert
- log.md aktualisiert

**Review:** User-Review + **kurzer Codex-Konsistenz-Pass** (rg-basiert: Backlink-Vollständigkeit, Orphan-Detection, Format-Gleichheit)

**Commit:** `feat(vault): paper-integration phase 1b — concept cross-links + index/log`

### Phase 2 — Skill-Verankerung + INSTRUKTIONEN-Querverweise

**Dateien:** 2 Skills + ggf. 2 Tool-READMEs + INSTRUKTIONEN §§18/27/28/29

**Acceptance:**
- Beide Skills zitieren relevante Papers an Workflow-Schritten
- Tool-READMEs haben Paper-Kontext-Header (wo anwendbar)
- §§18/27/28 haben "→ §29 / [[Paper]]"-Anker wo thematisch passt
- §29 hat Rückverweise-Liste

**Review:** User-Review (kein Codex)

**Commit:** `feat(skills+instruktionen): paper-integration phase 2 — skill anchors + cross-refs`

### Phase 3 — R5 Portfolio-Return-Persistenz

**Dateien:**
- `05_Archiv/portfolio_returns.jsonl` (neu, mit Daily-Schema inkl. `schema_version: "1.0"` pro Record)
- `05_Archiv/benchmark-series.jsonl` (neu)
- `03_Tools/portfolio_risk.py` (neuer `--persist daily`-Modus)
- CORE-MEMORY §5 (Lektion "R5 aktiviert YYYY-MM-DD")
- STATE.md (Interim-Gate-Bullet aktualisiert)

**Acceptance:**
- Daily-Schema wie spezifiziert (portfolio_value_gross, cashflow_net, return, benchmark, positions[])
- `schema_version: "1.0"` pro Record (konsistent mit `score_history.jsonl` §18)
- Erster Live-Snapshot läuft durch + verifiziert (Cashflow-Trennung, Benchmark-Parallelität)
- Benchmark-Zeitreihe täglich gemeinsam mit Portfolio persistiert (nicht retrospektiv rekonstruiert)

**Review:** **Codex-Review pflicht** — Code + Schema-Sanity + Look-Ahead-Check + Cashflow-Handling

**Commit:** `feat(infra): paper-integration phase 3 — portfolio-return persistence (daily snapshot)`

### Phase 4 — R1 Monthly-Refresh via §30

**Dateien:**
- `00_Core/INSTRUKTIONEN.md` (neue **§30 Live-Monitoring & Cadence**)
- `00_Core/CORE-MEMORY.md` (§5 Lektion R1)
- `01_Skills/dynastie-depot/SKILL.md` (Monatsrefresh-Trigger, falls Monthly-Refresh Workflow-Seite benötigt)

**§30-Skelett:**

```markdown
## 30. Live-Monitoring & Cadence

**Scope:** Monatliche Refresh-Pflicht für aktive Investment-FLAGs. Nicht: Scoring-Change, Auto-Rescore, neue Punkte.

**Trigger-Definition:**
- **Aktiver FLAG** = binär ausgelöst in flag_events.jsonl ohne Resolution → §30 pflicht
- **Schema-Watch (nicht FLAG-aktiv)** = schema-getriggert, bewusst nicht aktiviert → §30 nicht automatisch

**Aktuelle Scope (Stand 19.04.2026):**
- MSFT: CapEx/OCF 83.6% FLAG aktiv → Monthly-Refresh pflicht
- TMO: fcf_trend_neg Schema-Watch (WC-Noise 18.04.) → kein Monthly-Refresh

**Wissenschaftliche Basis:** Flint-Vermaak 2021 (Investment-Faktor-Half-Life ≈ 1M). → siehe §29.3.

**Ausweitung auf andere Faktor-Klassen** (z.B. Quality bei Half-Life <4M) erfordert Applied-Learning-Re-Review.
```

**Acceptance:**
- §30 präzise formuliert (nur aktive Investment-FLAGs, keine Auto-Rescore, nur Trigger-Prüfung)
- Schema-Watch-Kategorie klar abgegrenzt gegen STATE.md "Aktive Watches"
- Aktuelle Scope (MSFT + TMO mit Unterscheidung) dokumentiert
- Rückverweis auf §29.3 (Flint-Vermaak-Anker)
- Optionaler Testlauf: MSFT-Monatsrefresh simulieren

**Review:** **Codex-Review pflicht** — §30-Formulierung auf verdeckte Scoring-Change-Anker prüfen; Schema-Watch-Disambiguierung

**Commit:** `feat(instruktionen): §30 Live-Monitoring — Monthly-Refresh for active Investment-FLAGs (R1)`

---

## 5. Nicht-Ziele (Guardrails)

- **Keine Scoring-Kern-Änderungen:** Keine neuen DEFCON-Columns, keine Gewichts-Shifts, keine neuen FLAG-Typen, keine t-Score-Kalibrierung. Applied-Learning strikt.
- **Keine versteckten Workflow-/Trigger-Änderungen in Skills/Tools:** Keine neuen automatischen Trigger, keine zusätzlichen Pflichtschritte in `!Analysiere`/`!QuickCheck`/Archiv-Pipeline außer in Phase 2/3/4 ausdrücklich spezifiziert.
- **Keine retroaktive Altbestands-Anfassung:** Source-Pages Buffetts-Alpha, Morningstar-Wide-Moat, Gu-Kelly-Xiu-2020, Jadhav-Mirza-2025, Piotroski, Novy-Marx, Sloan, Wolff-Echterling bleiben unangetastet. Eigener Cleanup-Batch falls später gewünscht.
- **Keine Walk-forward/k-fold/randomized Backtests im Live-Workflow** (Palomar Ch 8.4 Guardrail) — nur Retrospective/Migration via §29.
- **Kein Scope-Creep in Ersatzbank:** 7 Ersatzbank-Pages (GOOGL, ZTS, PEGA, MKL, NVDA, SNPS, RACE, DE, SPGI) ohne R4-Factor-Exposure-Block.
- **Kein Valuation-Z-Score als Metric** — verworfen Session 2 (Evidence-Mismatch: AQR-Value-Spread Long-Short-Cross-Section, nicht Single-Ticker). !Analysiere-Checklist statt.
- **§30-Cadence-Ausweitung** auf weitere Faktor-Klassen nur nach Applied-Learning-Re-Review.

---

## 6. Backlog & Gates

### Interim-Gate 2027-10-19 (18-Monate-Dry-Run)

- `risk-metrics-calculation`-Skill Dry-Run auf `portfolio_returns.jsonl` (Phase-3-Output, dann 18 Monate akkumuliert)
- **PBO/CSCV-Smoke-Test** (Codex-ergänzt) als technischer Dry-Run — Implementation, Input-Format, Mindestanforderungen (N, T, Forward-only-Filter) vor 2028 entstressen. **Ohne Entscheidungswirkung.**
- Data-Quality-Check auf `portfolio_returns.jsonl` (Lücken, Cashflow-Konsistenz)

### Review-Gate 2028-04-01 (Volle Aktivierung §29)

- **R2 — Cumulative-Version-Bump-Tripwire** (Bailey PBO-Logik): Erst nach mehr Forward-Historie. §28 deckt heute ab.
- **R3 — Seven-Sins in Live-!Analysiere-Workflow:** Retrospective-Gate §29.5 nicht mit Live-Prozess verwischen.
- **§29.1-3 + §29.6 Vollaktivierung:** PBO/CSCV-Rechnung, AQR-Benchmark-Gate, Half-Life-Konsistenz-Check, Portfolio-Return-Metrik-Layer — benötigen 24+ Monate saubere Return-Serie.
- **Walk-forward + k-fold** als Cross-Checks zu §29.1 einführen.
- **Ersatzbank-Harmonisierung:** Factor-Exposure-Blöcke retroaktiv für 7 Ersatzbank-Pages, falls Slot-16-Promotion.
- **Skill `risk-metrics-calculation`-Aktivierung** (Sortino, Calmar, Max-DD, CVaR, IR) nach 24+ Monaten portfolio_returns.jsonl-Historie.
- **Eventuelle §30-Erweiterung** um Quality-Klasse-Monthly-Refresh (nach Applied-Learning-Re-Review).

---

## 7. Review-Gate-Übersicht

| Phase | User-Review | Codex-Review | Commit |
|-------|-------------|--------------|--------|
| 1a — Satelliten + R4 | ✅ Stichprobe 3 Ticker | — | `phase 1a` |
| 1b — Concepts + Index/Log | ✅ Stichprobe 2 Concepts | ✅ Konsistenz-Pass (rg-basiert) | `phase 1b` |
| 2 — Skills + INSTRUKTIONEN | ✅ | — | `phase 2` |
| 3 — R5 Portfolio-Persistenz | ✅ | ✅ **Pflicht** (Code + Schema + Look-Ahead) | `phase 3` |
| 4 — R1 §30 Live-Monitoring | ✅ | ✅ **Pflicht** (§30-Formulierung + Schema-Watch) | `phase 4` |

---

## 8. Approvals-Trail

| Datum | Review | Verdikt | Dokumentiert |
|-------|--------|---------|--------------|
| 19.04.2026 | Codex Scope-Review (C+ vs Applied-Learning) | GO mit R5 ergänzt (Blind Spot: Portfolio-Return-Persistenz-Zeitwert) | Sektion 3 |
| 19.04.2026 | Codex Batching-Review (B1/B2/B3) | B1.5 — R5 vor R1 (Zeitwert) | Sektion 4 |
| 19.04.2026 | Codex Scope-Items + Datei-Impact | GO mit 3 Änderungen: R1→§30, Daily-Schema, R4-5-Zeilen-Struktur | Sektion 3 |
| 19.04.2026 | Codex Execution-Phasen + Acceptance | GO mit 6 Änderungen: Phase-1-Sub-Commits, Acceptance-Härte, schema_version, Benchmark-Serie, FLAG-Semantik, Konsistenz-Pass | Sektion 4 |
| 19.04.2026 | Codex Guardrails + Backlog | GO mit 4 Änderungen: Workflow-Guardrail, PBO-Smoke-Test, §30-Re-Review, Schema-Watch-Rename | Sektion 4 |

---

## 9. Nächste Schritte

Nach User-Approval dieses Specs:
1. Transition zu `writing-plans`-Skill → Implementation-Plan `docs/superpowers/plans/2026-04-19-paper-integration.md`
2. Plan-Granularität: eine Task pro Phase (1a/1b/2/3/4), mit konkreten Datei-Edits und Codex-Checkpoints als eigene Tasks
3. Execution inline (keine Subagents — CLAUDE.md Applied-Learning #1: "Markdown/YAML-Edits direkt editieren")

---

*🦅 Dynasty-Depot Track 3 | Paper-Integration systemweit | Spec v1.0 — 19.04.2026*
