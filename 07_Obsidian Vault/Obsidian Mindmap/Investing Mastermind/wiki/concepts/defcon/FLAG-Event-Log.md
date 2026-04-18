---
title: "FLAG-Event-Log"
type: concept
tags: [defcon, flag, infrastructure, history, backtest-ready]
created: 2026-04-17
updated: 2026-04-19
version: v3.7.2
sources: []
related: [CapEx-FLAG, Tariff-Exposure-Regel, DEFCON-System, Score-Archiv, Backtest-Ready-Infrastructure]
wissenschaftlicher_anker: "Operative Trigger/Resolution-Historie für FLAG-Event-Study-Methodik"
konfidenzstufe: operativ
---

# FLAG-Event-Log

> **Append-only Trigger- und Resolution-Paare aller FLAG-Ereignisse. Quelle für deskriptive Event-Studies.**

## Zweck

`05_Archiv/flag_events.jsonl` hält pro FLAG **genau zwei Records** über Lebenszyklus: einen Trigger-Record (Regel verletzt) und einen Resolution-Record (Regel wieder eingehalten). Gepaart über gemeinsame `flag_id` (`TICKER_FLAGTYP_YYYY-MM-DD`).

## Vier FLAG-Typen (enum `flag_typ`)

| Typ | Schwelle | Verletzung | Definition |
|-----|----------|------------|------------|
| `capex_ocf` | 60 | `>` | CapEx/OCF > 60% (laufendes oder kommendes GJ) |
| `fcf_trend_neg` | 0 | `<` | FCF YoY negativ in ≥3 von 4 letzten Quartalen UND CapEx YoY positiv — **deterministische Definition** |
| `insider_selling_20m` | 20_000_000 | `>` | Diskretionäres Selling > $20M in 90d (Code S, kein M+S Cashless-Exercise) |
| `tariff_exposure` | 35 | `>` | Revenue-Anteil aus tarifbetroffenen Märkten > 35% |

Schwellen sind hardcoded in `03_Tools/backtest-ready/schemas.py` → `FLAG_RULES`. Schwellen-Änderung erfordert `schema_version`-Bump.

## Event-Format

**Trigger:**
```bash
python 03_Tools/backtest-ready/archive_flag.py trigger \
  --ticker GOOGL --flag-typ capex_ocf --datum 2026-03-15 \
  --metrik-wert 78 --metrik-definition "fy26_guidance" \
  --kurs 305.56 --waehrung USD --kurs-quelle yahoo_eod
```

**Resolution** (gleicher `flag_id`):
```bash
python 03_Tools/backtest-ready/archive_flag.py resolve \
  --flag-id GOOGL_capex_ocf_2026-03-15 \
  --datum 2027-02-15 --metrik-wert 54 ...
```

## Integration in SKILL.md

**Schritt 6b (Pre-Archive-Write):** FLAG-Resolution-Check — aktive FLAGs des analysierten Tickers prüfen, resolven wenn Metrik normalisiert. Neue Triggers im gleichen Lauf aufnehmen. Bleibt CLI-direkt (`archive_flag.py trigger/resolve/list`), nicht Teil der v3.7.2-Skill-Orchestrierung.

**Schritt 7:** Archiv-Write des Score-Records via Skill [`backtest-ready-forward-verify`](../../../../../01_Skills/backtest-ready-forward-verify/SKILL.md) (seit 19.04.2026, v3.7.2); `flags.aktiv_ids` referenziert zum Zeitpunkt der Analyse aktive Flags. Der Skill konsumiert nur Score-Drafts — FLAG-Events bleiben ausserhalb seines Scopes.

## Validation

`FlagEvent._check_metrik_direction` greift hart:
- Trigger MUSS Schwelle verletzen (Direction aus `FLAG_RULES`)
- Resolution MUSS Schwelle einhalten
- `metrik.wert = null` überspringt Check (Backfill-Tolerant)

## Event-Study

Deskriptive Auswertung: siehe [[Backtest-Methodik-Roadmap]] + `02_Analysen/flag_event_study_2026-04-17.md` (Einmal-Report n=2 Infrastruktur-Validation, Disclaimer: nicht statistisch belastbar).
