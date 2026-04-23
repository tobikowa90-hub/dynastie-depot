---
tags: [synthese, depot-state, monatlich]
stand: 2026-04-10
version: April-2026
updated: 2026-04-20
aliases:
  - "depot-state-april-2026"

---

# Depot-State — April 2026

> ⚠️ **Historischer Snapshot-Zeitstand: 10.04.2026 (pre-v3.7).** Live-Stand (Nenner **8.0**, Rate **35,63€/17,81€/0€**, 11 Satelliten, DEFCON v3.7, 6-Paper-Ingest SSoT aktiv) → `00_Core/STATE.md`. Dieser Snapshot bleibt als April-Monatsarchiv erhalten.
> Monatlicher Snapshot. Nach jeder !Analysiere-Session aktualisieren.
> Nächste Vollaktualisierung: Mai 2026 (nach TMO + MSFT Earnings)

## Post-Snapshot-Events (11.-20.04.2026)

Chronologischer Abriss der zwischen 10.04. und Monats-Cutoff erfolgten System-Events — keine Änderung am 10.04.-Snapshot, nur Drift-Dokumentation:

- **17.04.2026** — DEFCON v3.7 System-Gap-Release: 4 strukturelle Fixes (Quality-Trap-Interaktionsterm, OpM-TTM, Analyst-Bias-Kalibrierung, Fundamentals-Cap 50). Siehe [[DEFCON-System]].
- **18.04.2026** — V-Forward-Vollanalyse 86→63 (D2), Schema-Threshold-Drift-Fix auf SKILL.md aligned: **Nenner 9.0→8.0, Rate 31,67€/15,83€ → 35,63€/17,81€**. TMO D2 (64, fcf_trend_neg nicht aktiviert). Ersatzbank-Scope auf 5 Titel (MKL/SNPS/SPGI/RACE/ZTS).
- **19.04.2026** — Backtest-Ready Skill-Orchestrator v3.7.2 (programmatische Forward-Verify-Pipeline), R5 Portfolio-Return-Persistenz aktiv (`portfolio_returns.jsonl`), §30 Live-Monitoring pflicht für MSFT CapEx-FLAG (Flint-Vermaak B17 Half-Life ~1M).
- **20.04.2026 Mittag/Abend/Nacht** — v3.0.3 Probe-Trigger T1/T3/T4 PASS (262s OBSERVE-Band); 6-Paper-Ingest Phase 1a+1b (Befunde B19-B24) + Phase 2 Hybrid A+B+C formal abgeschlossen (Commits `89275e2`+`5f6dc62`). **Status-Matrix** in [[Wissenschaftliche-Fundierung-DEFCON]] = kanonische SSoT. [[Knowledge-Graph-Architektur-Roadmap]] v0.1 `draft-frozen` (Codex Option D). DEFCON v3.7 unverändert — ZERO Scoring-Impact des gesamten Ingest-Projekts.
- **20.04.2026 Nacht-Spät** — Morning-Briefing Prod-Trigger v2.1→**v3.0.3 deployed** (`trig_01PyAVAxFpjbPkvXq7UrS2uG`), Gate-A-Start 21.04. 10:00 MESZ (3-Tage-Korrektheits-Check, kein Auto-Rollback aus Runtime).

## Allokation

| Block | Ziel | Betrag/Monat | Broker |
|-------|------|-------------|--------|
| ETF-Core | 65% | 617.50 € | ING |
| Satelliten | 30% | 285.00 € | Scalable Capital |
| Gold | 5% | 47.50 € | Scalable Capital |

**US-Hard-Cap:** max. 63% | Ist: ~46.41% | Ziel: ~49.51%

## Aktuelle Sparplan-Verteilung (10.04.2026)

Stand: 8× DEFCON 4, 2× DEFCON 3, 1× FLAG

- **Nenner:** (8 × 1.0) + (2 × 0.5) + 0 = 9.0
- **D4-Rate:** 31.67 €/Position
- **D3-Rate (ASML, TMO):** 15.83 €/Position
- **FLAG (MSFT):** 0 €

## Score-Register (Stand: 10.04.2026)

| Ticker | Score | DEFCON | FLAG | Sparrate | Nächste Aktion |
|--------|-------|--------|------|----------|----------------|
| [[AVGO]] | 86 | 🟢 4 | — | 31.67€ | Q3 FY26 Earnings |
| [[BRKB|BRK.B]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 7) |
| [[VEEV]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 8) |
| [[RMS]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 9) |
| [[SU]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 10) |
| [[COST]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 4) |
| [[V]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 5) |
| [[APH]] | ~80 | 🟢 4 | — | 31.67€ | Tariff-Check (Prio 6) |
| [[ASML]] | 68 | 🟡 3 | — | 15.83€ | Q1 Earnings (High-NA-Ramp) |
| [[TMO]] | 67 | 🟡 3 | — | 15.83€ | **23.04. Q1 Earnings 🔴** |
| [[MSFT]] | 60 | 🟠 2 | 🔴 CapEx | 0€ | **29.04. Q3 Earnings 🔴** |

## Offene Entscheidungen

| Datum | Ticker | Entscheidung |
|-------|--------|-------------|
| **23.04.2026** | TMO | FCF >$7.3B → DEFCON 4 / sonst ZTS-Aktivierung |
| **28.04.2026** | SPGI | Earnings → Re-Analyse Katalysator |
| **29.04.2026** | MSFT | FLAG-Auflösung wenn bereinigtes CapEx/OCF <60% |
| **Mai 2026** | PEGA | Slot-16-Entscheidung nach Earnings |
| **Juni 2026** | — | Sparplan-Booster: 9.500€ Bausparer + 2.000€ Steuererstattung |

## Liberation-Day Triage (ausstehend)

Tariff-Check für alle 11 Satelliten. Reihenfolge nach Priorität:
1. 🔴 TMO — 23.04. Earnings
2. 🔴 MSFT — 29.04. Earnings
3. 🟡 AVGO — Tariff-Exposure MY/TH ~35%
4. 🟡 COST → 5. V → 6. APH → 7. BRK.B → 8. VEEV → 9. RMS → 10. SU → 11. ASML

## Verlinkungen

- [[DEFCON-System]] — Scoring-Logik
- [[Analyse-Pipeline]] — Workflow
- [[CapEx-FLAG]] — FLAG-Regeln
