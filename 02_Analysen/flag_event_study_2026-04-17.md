# FLAG-Event-Study 2026-04-17 — Deskriptive Auswertung

**Stichprobengröße:** n = 2 Events | **Zeitraum:** 2026-01-15 bis 2026-03-15
**Disclaimer:** *Nicht statistisch belastbar, rein deskriptiv. Infrastruktur-Validierung, keine Scoring-Kalibrierung.*
**Methodik-Referenz:** `docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md` §10

## 1. Event-Tabelle (alle FLAGs)

| flag_id | Ticker | Typ | Trigger-Datum | Alter (Tage) | Kurs@Trigger | Raw +30 | Raw +90 | Raw +180 | Raw +360 | MaxDD-Fenster | Alpha vs S&P500 +30 | Alpha +90 | Resolution? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `MSFT_capex_ocf_2026-01-15` | MSFT | capex_ocf | 2026-01-15 | 92 | 456.66 USD (2026-01-15) | -12.12% | -9.95% | pending (needs 88 more days) | pending (needs 268 more days) | -21.87% (bis 2026-04-17) | -10.56pp | -11.08pp | keine (Backfill-Sample) |
| `GOOGL_capex_ocf_2026-03-15` | GOOGL | capex_ocf | 2026-03-15 | 33 | 305.56 USD (2026-03-16) | +8.95% | pending (needs 57 more days) | pending (needs 147 more days) | pending (needs 327 more days) | -10.49% (bis 2026-04-17) | +4.95pp | pending (57d) | keine (Backfill-Sample) |

> *Für nicht-observierte Horizonte: "pending (needs X more days)". yfinance-Failures werden als "n.a. (data source)" markiert.*

## 2. Aggregation per FLAG-Typ

| FLAG-Typ | Anzahl | Median Raw +30 | Range Raw +30 | Median Raw +90 | Range Raw +90 |
|---|---|---|---|---|---|
| capex_ocf | 2 | -1.58% | [-12.12%, +8.95%] | -9.95% | [-9.95%, -9.95%] |

> *n pro FLAG-Typ zu klein für Mittelwerte oder Signifikanztests — nur Median + Range ausgewiesen. Bei observed=0 steht "–".*

## 3. Einzelfall-Narrativ

### MSFT capex_ocf (Trigger 2026-01-15)

**Hintergrund (CORE-MEMORY §1):** CapEx/OCF Q2 FY26 GAAP 83,6 % (bereinigt um Finance Leases ~63 %), damit über der 60 %-Schwelle. Trigger-Datum 2026-01-15 ist Proxy (Monatsmitte; Earnings-Call ca. 30.01.). **Kurs@Trigger (yfinance EOD 2026-01-15):** 456.66 USD. **+30d:** Raw -12.12%, Benchmark S&P500 -1.56%, Alpha -10.56pp. **+90d:** Raw -9.95%, Benchmark +1.13%, Alpha -11.08pp. **Noch offen:** Horizonte +180d, +360d (observierbar ab späterem Review).

### GOOGL capex_ocf (Trigger 2026-03-15)

**Hintergrund (CORE-MEMORY §3/§4):** FY26-Guidance nennt CapEx ~75 % OCF, FLAG-Record hat `wert=null` (Rohwert nicht eindeutig rekonstruierbar; Direction-Validator bewusst übersprungen). Trigger-Datum 2026-03-15 Proxy (Monatsmitte; Score-Datum im CORE-MEMORY ist 26.03. mit Score 72 / roter FLAG / kein Einstieg). **Kurs@Trigger (yfinance EOD 2026-03-16):** 305.56 USD. **+30d:** Raw +8.95%, Benchmark S&P500 +4.00%, Alpha +4.95pp. **Noch offen:** +90d, +180d, +360d.

## 4. Limitationen & Lehren für 2028-Review

- **n = 2** ist nicht-repräsentativ (Infrastruktur-Sample, keine statistische Power).
- **3 / 8** Horizont-Messpunkte observierbar, **5 / 8** pending (brauchen zusätzliche Marktdaten).
- **GOOGL-FLAG-Record** hat `wert=null` (Backfill-Lücke, CORE-MEMORY §4 hält nur Score-Level fest, nicht exakten CapEx/OCF-Rohwert zum März-Stichtag).
- **Backfill-Limit:** FLAGs vor 2026-04 nutzen Trigger-Datum-Proxies (Monatsmitte), was Event-Study-Präzision bei historischen Records reduziert (±15 Tage Unsicherheit im Stichtag).
- **Ab 2026-04 live Forward-Pipeline** → zum 2028-Review-Zeitpunkt erwartete Sample-Size: **~15–25 Events** (annahme: 1–2 FLAGs/Quartal über ~2 Jahre für 10 aktive Symbole).
- **Nächster Review-Auslöser:** wenn n≥10 UND 2/3 der Events +180d observierbar sind (frühestens Q4-2027 bei aktueller Trigger-Frequenz).

---

*Generiert am 2026-04-17 via `03_Tools/backtest-ready/flag_event_study.py` gegen `05_Archiv/flag_events.jsonl` (n=2). Benchmark: `^GSPC` (S&P 500 Composite, yfinance EOD Close, unadjusted).*
