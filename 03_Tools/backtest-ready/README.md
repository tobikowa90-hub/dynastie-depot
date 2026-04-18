# Backtest-Ready Archive Tools

**Aktiviert:** 2026-04-17 | **System:** DEFCON v3.7 | **Review-Termin:** 2028-04-01

Append-only JSONL-Archive für das Dynastie-Depot-Scoring-System. Jede `!Analysiere`-Ausgabe und jedes FLAG-Event wird maschinenlesbar persistiert, damit ab 2028+ ein formaler Backtest methodisch möglich wird.

**Prinzip:** *"Jeder Monat ohne Archiv-Infrastruktur ist verlorene Historie."*

---

## Dateien

| Datei | Zweck |
|-------|-------|
| `schemas.py` | Pydantic-Modelle (Score-Record, FLAG-Event, Kurs, 14 Modelle insgesamt). Alle Validators — Arithmetik, DEFCON-Konsistenz, Quality-Trap-Interaktion (v3.7), FLAG-Direction. |
| `archive_score.py` | CLI: Score-Record anhängen. Liest JSON via `--file` oder `--stdin`. Validiert, prüft `record_id`-Uniqueness + Forward-Datum-Window (≤3 Tage). Append-only an `../../05_Archiv/score_history.jsonl`. |
| `archive_flag.py` | CLI: FLAG-Events — Subcommands `trigger`, `resolve`, `list`. Schwellen hardcoded via `FLAG_RULES` in `schemas.py`. Uniqueness-Check (kein Doppel-Trigger), Resolve-Präconditions (Trigger existiert + nicht bereits resolved). |
| `README.md` | Diese Datei. |

**Archive:** `../../05_Archiv/score_history.jsonl` + `../../05_Archiv/flag_events.jsonl` — git-tracked via `.gitignore`-Whitelist (Pattern `05_Archiv/*` + Exceptions).

---

## Usage

### Score archivieren (nach jeder !Analysiere)

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
python 03_Tools/backtest-ready/schemas.py        # 6 cases
python 03_Tools/backtest-ready/archive_score.py  # 5 cases (ohne CLI-Args)
python 03_Tools/backtest-ready/archive_flag.py --smoke-test  # 7 cases
```

Alle Smoke-Tests nutzen Temp-Files — echte Archive bleiben unangetastet.

---

## Sync-Pflicht (§18 INSTRUKTIONEN)

Nach jeder `!Analysiere`: **6 Dateien** in einem git-Commit aktualisieren:
1. `log.md` (Vault)
2. `CORE-MEMORY.md` (00_Core)
3. `Faktortabelle.md`
4. `STATE.md`
5. `score_history.jsonl` ← dieser Append
6. `flag_events.jsonl` (nur bei FLAG-Trigger/Resolution)

**SKILL.md Schritt 7** ist die kanonische Trigger-Stelle für den `archive_score.py`-Aufruf.

---

## 2028-Review

Am **2028-04-01** entscheiden:
- Hat die Forward-Historie (+2 Jahre seit 2026-04) genug Sample-Size für Return-Prediction oder Threshold-Kalibrierung?
- Welcher der 4 DEFCON-Fundierungs-Paper (arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha) ist als Benchmark anlegbar?
- Haben Scoring-Version-Sprünge Regime-Wechsel produziert, die Backtest-Vergleiche invalidieren?

Entscheidungsmatrix: `07_Obsidian Vault/.../synthesis/Backtest-Methodik-Roadmap.md` (wird in Phase 4 angelegt).
