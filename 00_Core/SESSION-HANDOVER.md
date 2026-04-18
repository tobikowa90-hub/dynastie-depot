# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 18.04.2026 (Abend) | **Für:** Nächste Session

---

## ▶️ TRIGGER

```
Session starten
```

Claude liest automatisch `00_Core/STATE.md` (Single-Entry-Point).

---

## ✅ LETZTE SESSION (18.04.2026) — ERLEDIGT

**8 Commits, systemischer Konsistenz-Sprung.** Erste zwei Forward-Records im Archiv (V + TMO), Schema-SKILL-Alignment, komplette Propagation auf alle Layer (00_Core + Skill-SSOT + Vault + Excel-Tools), Applied-Learning auf Kern-Prinzipien verschlankt.

### Kernereignisse

**1. V Pre-Earnings Q2 FY26 — Forward-Vollanalyse + Rescoring** (Commit `a0aeb6e`)
- Earnings-Preview + Vollanalyse (Score 72) → Advisor-Review → 3 Sub-Score-Korrekturen → Rescoring 63
- Algebra-Projektion 86 (v3.5→v3.7) empirisch nicht haltbar (-23 Pt.)
- Korrekturen: (a) Moat Pricing-Power ohne Transcript-Beleg entfernt; (b) Insider Ownership Threshold statt Gradient; (c) ROIC Regel-4-Gating greift nicht (GW/Assets 19,95% <30%), GAAP 9,89% < WACC 10,48% → 1/8
- **Record:** `2026-04-18_V_vollanalyse` (72) + `2026-04-18_V_rescoring` (63, erstes Rescoring im Archiv)

**2. γ-Fix: Schema-SKILL DEFCON-Threshold-Drift** (Commit `a0aeb6e`)
- `schemas.py` nutzte alte Thresholds 70/60/50, SKILL.md arbeitet seit v3.x mit 80/65/50
- Fix: `_check_defcon_level` + Smoke-Tests auf SKILL-Alignment
- **5 Tickers Label-Drift:** BRK.B/VEEV/SU/COST/RMS D4→D3 (Sparrate unverändert bei D3/D4-Übergang)
- **APH D3→D2** (FLAG überschreibt Sparrate weiterhin)
- **Nenner 8.5 → 8.0**, volle Rate 33,53€ → 35,63€, D2-Rate 16,76€ → 17,81€

**3. TMO Q1 FY26 — Forward-Vollanalyse + struktureller FLAG-Disclosure** (Commit `4e1440c`)
- Score 63 → 64 (Algebra ±1 empirisch bestätigt, dritter Verifikationsfall)
- **ROIC-Regel-4-Gating greift:** GW/Assets 44,74% ≥30% → IC bereinigt 43,430M → ROIC bereinigt **17,18% vs WACC 10,44% = +6,74pp Spread**
- **fcf_trend_neg Option B (Advisor-Entscheidung):** schema-getriggert (FY25 FCF -13,4% YoY, CapEx +8,9%) aber NICHT aktiviert — (a) WC-Delta -$1,766M > FCF-Delta -$974M = WC-Noise; (b) 4J-Plateau $6,9→6,9→7,3→6,3B; (c) OpInc +5,1% YoY
- **Record:** `2026-04-18_TMO_vollanalyse` mit `flags.aktiv_ids=[]` + strukturellem Disclosure in `notizen`
- **Resolve-Gate Q1 23.04.2026** — WC-Unwind + FCF-Recovery bestätigt → Disclosure bleibt; fehlende Reversibilität → FLAG nachtragen

**4. Multi-Layer-Sync-Kaskade** (Commits `5364d06` + `2795d92`)
- `config.yaml` (Skill-SSOT): Sparplan-Beispiel + V + TMO + APH + 5 Label-Fixes + Meta-Header
- Vault-Satelliten (8 Pages): V.md komplett neu, TMO.md erweitert, BRK.B/VEEV/SU/COST/RMS/APH Tag-Updates
- Rebalancing-Tool + Satelliten-Monitor (statische DEFCON-Labels, Sparrate-Werte, Legenden)

**5. Excel-Tool-Hygiene** (Commits `5832e17` + `20ef297` + `5d3a005`)
- Excel-COM-Recalc via `win32com.client` → openpyxl-Save räumt cached values; Recalc populiert sie
- Metric-Columns im Satelliten-Monitor reconciled (V ROIC `~45%[~]` → `9.89% GAAP`, TMO ROIC `~9%[V]` → `17.18% bereinigt (Regel-4)`)
- Conditional-Formatting harmonisiert (Dynasty-Palette: D4 grün / D3 gelb / D2 orange / D1/FLAG rot) in beiden Tools
- Emoji-Bug: `LEFT(O,2)="🔴"` → `LEFT(O,1)="🔴"` (Excel 365+ codepoint-basiert), APH Rot-Färbung wiederhergestellt

**6. Applied Learning Evakuierung** (Commit `5f15405`)
- CLAUDE.md 19/20 → **9/20** (11 Slots Puffer)
- 6 Tool-Refs evakuiert → Auto-Memory (war bereits dort)
- 4 systemische Regeln promotet → **INSTRUKTIONEN §27 Scoring-Hygiene & Daten-Integrität** neu
- §27.1 Double-Counting-Vermeidung / §27.2 Bonus-Cap-Check / §27.3 Projection-Layer ≠ Wahrheitsquelle / §27.4 Multi-Source-Drift-Check
- **Neue Disziplin:** Proaktiver Monats-Scan (5 Min, Tool-Refs identifizieren) statt reaktive Überlauf-Sanierung
- **Neuer Kern-Bullet:** "Option B vor mechanischem FLAG-Trigger" (aus TMO 18.04.)

### Was entstanden ist

**Archive** (`05_Archiv/score_history.jsonl`):
- **27 Records** (24 Backfill + 3 Forward: V_vollanalyse 72 / V_rescoring 63 / TMO_vollanalyse 64)

**Doku-Updates:**
- `STATE.md` — Portfolio-Tabelle + Trigger + Watches (Nenner 8.0, volle Rate 35,63€, D2-Rate 17,81€)
- `CORE-MEMORY.md §11` — 4 Befunde (Delta-Pattern, Schema-Drift, V-Rescoring, TMO Option B)
- `Faktortabelle.md` — V/TMO Zeilen + 5 D4→D3 Label-Fixes + APH D3→D2
- `INSTRUKTIONEN.md v1.7 → v1.8` — §27 neu
- `schemas.py` + `archive_score.py` — Thresholds auf 80/65/50 + Smoke-Tests
- `SKILL.md` — Schritt 0 Rewrite (Trigger-first), Schritt 7 Exit-2 mit sed-Recovery
- `CLAUDE.md` — Applied-Learning auf 9 Bullets + Monatsscan-Regel
- 8 Vault-Satelliten-Pages (V komplett neu, TMO erweitert, 6 Tag-Updates)
- Rebalancing-Tool + Satelliten-Monitor (CF harmonisiert, Metrics reconciled)

### Portfolio-Änderungen

| Ticker | Vorher (17.04.) | Nachher (18.04.) | Grund |
|---|---|---|---|
| V | 86/D4/35,63€ | **63/D2/17,81€** | Forward-Vollanalyse (-23 Pt. nach Advisor-Review) |
| TMO | 63/D2/16,76€ | **64/D2/17,81€** | Forward-Vollanalyse (+1, D2 bleibt, struktureller fcf_trend_neg Disclosure) |
| BRK.B/VEEV/SU/COST/RMS | D4/33,53€ | **D3/35,63€** | Label-Fix Schema-SKILL-Alignment (Score unverändert, Rate steigt durch Nenner 8.5→8.0) |
| APH | D3/0€ | **D2/0€** | Label-Fix (FLAG-Sparrate-Override unverändert) |
| ASML | D3/33,53€ | D3/**35,63€** | Rate-Anstieg durch Nenner-Shrink |
| AVGO | D4/33,53€ | D4/**35,63€** | Rate-Anstieg durch Nenner-Shrink |
| MSFT | D2-FLAG/0€ | D2-FLAG/0€ | Unverändert |

**Sparrate-Check:** 7×35,63 + 2×17,81 + 2×0 = 285€ ✓

---

## 🎯 NÄCHSTER FOKUS: Earnings-Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|---|---|---|---|
| **23.04.** | **TMO** | **B** | **Q1 FY26 — D2-Entscheidung + fcf_trend_neg Resolve-Gate (WC-Unwind?)** |
| **28.04.** | **V** | **B** | **Q2 FY26 — D2-Entscheidung (Technicals-Reversal bei Beat + Guidance?)** |
| 28.04. | SNPS / SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — CapEx/OCF FLAG-Review (bereinigt <60% = Auflösung)** |
| Mai | BRK.B / ZTS / PEGA | B | Q-Earnings + Slot-16 |

**Archiv-Disziplin bei jeder `!Analysiere`:**
- SKILL.md Schritt 6b: FLAG-Resolution-Check vor Archiv-Write
- SKILL.md Schritt 7: `archive_score.py --file <tempfile.json>`
- §18 Sync-Pflicht: 6 Dateien im gleichen git-Commit

---

## 🧭 START-PROTOKOLL NÄCHSTE SESSION

1. `Session starten` → `STATE.md` wird gelesen (Nenner 8.0, 35,63€/17,81€)
2. Backtest-Ready-Status: **27 Records** (24 Backfill + 3 Forward)
3. Earnings-Trigger checken (TMO 23.04., V 28.04., MSFT 29.04.)
4. Bei `!Analysiere`: Schritt 0 Trigger-Check → Vollanalyse → Schritt 6b → Schritt 7

---

## 🚫 WAS NICHT ZU TUN

- **Kein** Narrative-Layer (log.md / CORE-MEMORY.md) als Backtest-Primärquelle zitieren — Point-in-Time-Integrität nur im History-Layer (JSONL-Archive)
- **Kein** manuelles Editieren von `05_Archiv/*.jsonl` — append-only, Korrekturen nur via neuen Record mit Cross-Reference in `notizen` (Präzedenz: V-Rescoring 18.04.)
- **Kein** Commit von JSONL-Archiven ohne die begleitenden Narrative/State/Projection-Dateien (§18 Sync-Pflicht — alle sechs, immer)
- **Kein** mechanisches FLAG-Triggern ohne strukturellen Review — WC-Noise / Multi-Year-Trend / OpInc-Parallelität prüfen (Präzedenz: TMO fcf_trend_neg Option B)
- **Kein** Algebra-Projektion als Scoring-Endergebnis akzeptieren — bei Trigger immer Forward-Lauf (Präzedenz: V Algebra 86 vs Forward 63)

---

## 📂 KRITISCHE DATEIEN (Navigation)

- **Entry:** `00_Core/STATE.md` — Portfolio + Watches + Trigger
- **Gedächtnis:** `00_Core/CORE-MEMORY.md` §11 — 4 Befunde (Backtest-Ready + Drift + V + TMO Option B)
- **Regeln:** `00_Core/INSTRUKTIONEN.md v1.8` — §18 Sync-Pflicht, §22 Sparplan-Formel, §26 Archiv-Sync, **§27 Scoring-Hygiene (neu)**
- **Architektur:** `00_Core/KONTEXT.md` §11 — 4-Layer-Architektur (State/Narrative/History/Projection)
- **Tools:** `03_Tools/backtest-ready/README.md` — CLI-Usage
- **Archive:** `05_Archiv/score_history.jsonl` (27) + `flag_events.jsonl` (2)
- **Skill:** `01_Skills/dynastie-depot/SKILL.md v3.7.1` + `config.yaml` (aktualisiert 18.04.)

---

## 🔬 System-Reife-Tracker

- v3.5 (16.04.): 85%
- v3.7 (17.04. Morgen): ~92%
- Backtest-Ready (17.04. Abend): ~95%
- **Schema-SKILL-Aligned + Forward-Pipeline-bewährt (18.04.): ~96%** — 3 Forward-Records, §27 Scoring-Hygiene formalisiert, Applied Learning konsolidiert
- Weitere Hebel: Verhaltens-Layer (Execution Discipline), Makro-Overlay, Position-Sizing-Regel, FLAG-Historie-Volumen für 2028-Review
