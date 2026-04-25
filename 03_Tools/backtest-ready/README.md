# Backtest-Ready Archive Tools

**Aktiviert:** 2026-04-17 | **System:** DEFCON v3.7 | **Skill-Orchestrator aktiv seit:** 2026-04-19 (v3.7.2) | **Review-Termin:** 2028-04-01

> **Wissenschaftlicher Kontext (19.04.2026):** Diese Infrastruktur operationalisiert die Retrospective-Validation-Gates aus INSTRUKTIONEN.md §29. Relevante Papers: Bailey 2015 (PBO/CSCV), Aghassi 2023 (AQR-Benchmark), Flint-Vermaak 2021 (Half-Life), Palomar 2025 (Seven Sins + Risk-Metrics). Review 2028-04-01.

Append-only JSONL-Archive für das Dynastie-Depot-Scoring-System. Jede `!Analysiere`-Ausgabe und jedes FLAG-Event wird maschinenlesbar persistiert, damit ab 2028+ ein formaler Backtest methodisch möglich wird.

**Prinzip:** *"Jeder Monat ohne Archiv-Infrastruktur ist verlorene Historie."*

---

## Dateien

| Datei | Zweck |
|-------|-------|
| `schemas.py` | Pydantic-Modelle (Score-Record, FLAG-Event, Kurs, MigrationEvent, 15 Modelle insgesamt). Validators (v3.7.2, 6 Stück): Arithmetik, DEFCON-Konsistenz, Quality-Trap-Interaktion (v3.7), FLAG-Direction, MigrationEvent-Delta-Arithmetik, §28.2-Outcome-Bucket. |
| `archive_score.py` | CLI: Score-Record anhängen. Liest JSON via `--file` oder `--stdin`. Validiert, prüft `record_id`-Uniqueness + Forward-Datum-Window (≤3 Tage). Append-only an `../../05_Archiv/score_history.jsonl`. Seit 19.04.2026 orchestriert durch Skill (siehe unten); direkter CLI-Aufruf bleibt für Backfill und manuelle Recovery. |
| `archive_flag.py` | CLI: FLAG-Events — Subcommands `trigger`, `resolve`, `list`. Schwellen hardcoded via `FLAG_RULES` in `schemas.py`. Uniqueness-Check (kein Doppel-Trigger), Resolve-Präconditions (Trigger existiert + nicht bereits resolved). Bleibt CLI-direkt (nicht Teil der v3.7.2-Skill-Orchestrierung). |
| `_forward_verify_helpers.py` | Deterministische Primitives (Python): `parse_wrapper`, `parse_state_row` (PORTFOLIO.md-Tripwire; Funktions-Signatur aus Backwards-Compat unverändert), `build_migration_event` (§28.2-Bucketing + STOP-Signal), `check_freshness` (git-status gegen 3 Required-Touch-Files). Aufgerufen vom Skill `backtest-ready-forward-verify`. |
| `backfill_scores.py` / `backfill_flags.py` | Einmalige Backfill-CLIs aus CORE-MEMORY §4. Nicht Teil des laufenden Betriebs. |
| `flag_event_study.py` | Phase-3-Analyse-CLI (Event-Study über FLAG-Trigger/Resolution-Paare). Einmalige Auswertung, kein Teil der Orchestrierung. |
| `README.md` | Diese Datei. |

**Archive:** `../../05_Archiv/score_history.jsonl` + `../../05_Archiv/flag_events.jsonl` — git-tracked via `.gitignore`-Whitelist (Pattern `05_Archiv/*` + Exceptions).

---

## Usage

### Score archivieren — Forward-Run (kanonisch, seit 19.04.2026 v3.7.2)

Aus dynastie-depot Schritt 7: Draft-Wrapper nach `_drafts/<TICKER>_<YYYYMMDD-HHMM>.json` schreiben, dann Skill invoken:

```
Skill(skill="backtest-ready-forward-verify", args="<pfad-zum-draft>")
```

Skill orchestriert P1-P6 (Parse → Freshness + PORTFOLIO.md-Tripwire → §28.2 Δ-Gate → Dry-Run → Append → git add). Stdout-Report: 6 Fälle (OK / freshness / PFLICHT / STOP / duplicate / FAIL). Siehe `01_Skills/backtest-ready-forward-verify/SKILL.md`.

### Score archivieren — CLI-direkt (Backfill / manuelle Recovery)

```bash
# Dry-run zuerst zur Validation
python 03_Tools/backtest-ready/archive_score.py --file record.json --dry-run

# Echter Append
python 03_Tools/backtest-ready/archive_score.py --file record.json

# Oder via stdin
cat record.json | python 03_Tools/backtest-ready/archive_score.py --stdin
```

### FLAG triggern

```bash
python 03_Tools/backtest-ready/archive_flag.py trigger \
  --ticker GOOGL \
  --flag-typ capex_ocf \
  --datum 2026-04-17 \
  --metrik-wert 78 \
  --metrik-definition "annual_cash_flow_fy26_guidance" \
  --kurs 142.30 --waehrung USD --kurs-quelle yahoo_eod \
  --related-score-record-id 2026-04-17_GOOGL_vollanalyse
```

### FLAG resolven

```bash
python 03_Tools/backtest-ready/archive_flag.py resolve \
  --flag-id GOOGL_capex_ocf_2026-04-17 \
  --datum 2027-02-15 \
  --metrik-wert 54 \
  --metrik-definition "annual_cash_flow_fy27" \
  --kurs 168.90 --waehrung USD --kurs-quelle yahoo_eod
```

### Aktive FLAGs abfragen

```bash
python 03_Tools/backtest-ready/archive_flag.py list --aktiv
python 03_Tools/backtest-ready/archive_flag.py list --ticker MSFT
python 03_Tools/backtest-ready/archive_flag.py list --flag-typ capex_ocf
```

---

## FLAG-Typen (enum `flag_typ`)

| Typ | Schwelle | Verletzung | Definition |
|-----|----------|------------|------------|
| `capex_ocf` | 60 | `>` | CapEx/OCF > 60% (laufendes oder kommendes GJ) |
| `fcf_trend_neg` | 0 | `<` | FCF YoY negativ in ≥3 von 4 letzten Quartalen UND CapEx YoY positiv |
| `insider_selling_20m` | 20000000 | `>` | Diskretionäres Selling > $20M in 90d (Code S, kein M) |
| `tariff_exposure` | 35 | `>` | Revenue-Anteil aus tarifbetroffenen Märkten > 35% |

---

## Exit-Codes

- `0`: Success (append oder dry-run validiert)
- `1`: Validation-Error (Schema, Uniqueness, Direction-Check, Forward-Window)
- `2`: IO-Error (Archiv nicht lesbar, korrupt, Schreibfehler)

---

## Smoke-Tests

```bash
python 03_Tools/backtest-ready/schemas.py        # 7 cases (inkl. MigrationEvent)
python 03_Tools/backtest-ready/archive_score.py  # 5 cases (ohne CLI-Args)
python 03_Tools/backtest-ready/archive_flag.py --smoke-test  # 7 cases
python 01_Skills/backtest-ready-forward-verify/_smoke_test.py  # 6 cases (Skill-Helpers)
```

Alle Smoke-Tests nutzen Temp-Files — echte Archive bleiben unangetastet.

---

## Sync-Pflicht (§18 INSTRUKTIONEN v1.7)

Nach jeder `!Analysiere`: **6 Dateien** in einem git-Commit aktualisieren:
1. `log.md` (Vault)
2. `CORE-MEMORY.md` (00_Core)
3. `Faktortabelle.md`
4. `PORTFOLIO.md` (seit 00_Core Hub-Split, vorher `STATE.md`)
5. `score_history.jsonl` ← dieser Append (seit v3.7.2 via Skill orchestriert)
6. `flag_events.jsonl` (nur bei FLAG-Trigger/Resolution, CLI-direkt)

**SKILL.md Schritt 7 (dynastie-depot v3.7.2)** ist die kanonische Trigger-Stelle: Draft → `Skill(skill="backtest-ready-forward-verify", args=<pfad>)` → 6-Fall-Stdout-Report.

---

## 2028-Review

Am **2028-04-01** entscheiden:
- Hat die Forward-Historie (+2 Jahre seit 2026-04) genug Sample-Size für Return-Prediction oder Threshold-Kalibrierung?
- Welcher der 4 DEFCON-Fundierungs-Paper (arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha) ist als Benchmark anlegbar?
- Haben Scoring-Version-Sprünge Regime-Wechsel produziert, die Backtest-Vergleiche invalidieren?

Entscheidungsmatrix: `07_Obsidian Vault/.../synthesis/Backtest-Methodik-Roadmap.md` (wird in Phase 4 angelegt).
