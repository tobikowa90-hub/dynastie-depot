# TMO Q1 FY26 — Pre-Earnings-Briefing

**Erstellt:** 2026-04-22 Spät-Nacht (Vortag der Earnings)
**Earnings-Release:** Donnerstag 23.04.2026 **14:30 CEST** (8:30 AM ET, pre-market + CC)
**Quelle:** yfinance v1.3.0 via `earnings-preview`-Skill (Single-Pass-Fetch)
**Zweck:** Entscheidungs-Basis für morgige `!Analysiere TMO` — D2-Entscheidung + `fcf_trend_neg` Resolve-Gate

---

## 1. Key Info (Stand 22.04. Close)

| Feld | Wert |
|------|------|
| Sektor / Industrie | Healthcare / Diagnostics & Research |
| Marktkapitalisierung | $194,94 Mrd |
| Aktueller Kurs | **$524,57** (Previous Close $526,02) |
| 52W-Range | $385,46 — $643,99 (aktuell 59% der Spanne) |
| Trailing P/E | 29,6 |
| Forward P/E | **19,3** (deutlich günstiger → Growth erwartet) |
| Dividendenrendite | 0,34% |
| 1M-Performance | **+9,72%** (Erholung von Jahres-Tief) |
| 5d-Performance | −1,34% (Pre-Earnings-Soft) |

---

## 2. Consensus-Schätzungen Q1 FY26

| Metrik | Konsens | Low | High | Analysten | Year-Ago | YoY-Growth |
|--------|---------|-----|------|-----------|----------|-----------|
| **EPS** | **$5,24** | $5,02 | $5,34 | 19 | $5,15 | **+1,8%** |
| **Revenue** | **$10,86 Mrd** | $10,42B | $11,04B | — | $10,36B | **+4,8%** |

- **EPS-Range-Spread:** ($5,34 − $5,02)/$5,24 = **6,1%** → enger Konsens, geringe Analysten-Unsicherheit
- **FY26-Gesamtjahr-Erwartung:** EPS $24,80 (+8,4% YoY), Revenue $47,7B (+7,1% YoY) → **Beschleunigung in H2 eingepreist**

---

## 3. Beat/Miss-Track-Record (letzte 4 Quartale)

| Quartal | EPS Est | EPS Actual | Surprise | Urteil |
|---------|---------|------------|----------|--------|
| Q1 2025 | $5,10 | $5,15 | +0,94% | Beat (knapp) |
| Q2 2025 | $5,23 | $5,36 | +2,55% | Beat |
| Q3 2025 | $5,50 | $5,79 | **+5,32%** | Beat |
| Q4 2025 | $6,45 | $6,57 | +1,87% | Beat |

**4/4 Beats · Ø-Surprise +2,67% · Trend verstärkend bis Q3, dann normalisiert Q4.** Q1-Konsens wurde historisch konservativ gesetzt → **niedrige Hürde**.

---

## 4. Analysten-Sentiment

| Empfehlung | Anzahl (letzte 26 Analysten) |
|------------|------------------------------|
| Strong Buy | 5 |
| Buy | 19 |
| Hold | 2 |
| Sell / Strong Sell | 0 / 0 |

→ **92% Buy-Side-Bias, durchgehend bullish, keine Verschlechterung über letzte 3 Monate.**

**Kursziele:**
- Current: **$524,57**
- Mean: **$647,38 (+23,4% Upside)**
- Median: $640
- Range: $520 — $750 (niedrigster Analyst praktisch auf aktuellem Kurs → **kein Analyst sieht downside**)

---

## 5. Key Metrics to Watch — Dynasty-Depot-spezifisch

### 🔴 Kritischer Punkt: `fcf_trend_neg` Resolve-Gate

Aus STATE.md Watch: FY25 FCF −13,4% YoY war **schema-getriggert aber nicht aktiviert** (WC-Delta −1766M erklärte FCF-Rückgang vollständig, 4J-Trajektorie $6,9B→$6,9B→$7,3B→$6,3B = Plateau, OpInc +5,1%). Q1 FY26 = natürlicher Resolve-Gate.

**Quartals-Trajektorie aus yfinance (letzte 4 Quartale):**

| Metrik | Q1'25 | Q2'25 | Q3'25 | Q4'25 |
|--------|-------|-------|-------|-------|
| Operating CF | $723M | $1.399M | $2.239M | $3.457M |
| CapEx | −$362M | −$294M | −$404M | −$465M |
| **FCF** | **$361M** | $1.105M | $1.835M | **$2.992M** |
| **ΔWorking Capital** | **−$1.425M** | −$726M | −$104M | +$489M |
| Operating Income | $1.815M | $1.916M | $2.075M | $2.303M |
| Revenue (YoY est.) | ~+0% | ~+4,5% | ~+7,5% | ~+7,2% |

### Was morgen entscheidet

1. **WC-Unwind bestätigt?**
   Q1'25 hatte −$1,43 Mrd ΔWC als Drag. Wenn **Q1'26 ΔWC deutlich besser** (>−$500M oder positiv) → **WC-Noise-These bestätigt**, `fcf_trend_neg` bleibt deaktiviert.

2. **FCF-Recovery?**
   - Q1'26 FCF **>$700M** = klare Recovery-Bestätigung
   - Q1'26 FCF **<$361M** = strukturelles FCF-Problem → **Trigger nachtragen + ZTS-Ersatz-Welle**
   - Zwischenwerte ($361M–$700M) = WC-noch-nicht-vollständig-unwound, Kontext-abhängig bewerten

3. **Revenue-Akzeleration?**
   YoY-Trajektorie Q1→Q4'25 war +0 → +4,5 → +7,5 → +7,2%. Consensus Q1'26 +4,8% = leichte Deceleration.
   - **Beat >+5,5% YoY** = Re-Akzeleration (bullish)
   - **Miss <+4,0% YoY** = Stagnationssignal

4. **Operating Margin:**
   Q4'25 war 18,9% (Jahresspitze). Q1 saisonal schwächer, aber **>17,5%** (Q1'25-Niveau) = Margin-Hold.

5. **FY26-Guidance-Bestätigung:**
   Consensus $24,80 EPS / $47,7B Revenue.
   - **Raise** = klares Bull-Signal
   - **Unchanged** = neutral
   - **Cut** = FLAG-Verschärfung (selbst bei Q1-Beat)

---

## Entscheidungs-Matrix für morgige `!Analysiere TMO`

| Szenario | Trigger | FLAG-Konsequenz | Sparrate |
|----------|---------|-----------------|----------|
| **Miss** | EPS <$5,10 ODER FCF <$700M + ΔWC weiter stark negativ | `fcf_trend_neg` **nachtragen** via `archive_flag.py trigger`, **TMO-FLAG aktiv**, ZTS-Ersatz-Welle starten | **17,81€ → 0€** |
| **In-Line** | EPS $5,15–$5,35 + FCF $700M–$1,1B + ΔWC verbessert | FLAG-Resolve bestätigt, `fcf_trend_neg` bleibt deaktiviert, D2 hält (kein Upshift mangels Technicals) | **17,81€ hält** |
| **Beat + Guidance-Raise** | EPS >$5,35 + FY26 Guide nach oben | D2→D3-Kandidat, Sparrate-Upshift-Prüfung bei Vollanalyse | **Re-evaluieren** (17,81€ → ggf. 35,63€) |

---

## Workflow-Hinweise für morgen

- **Pfad-2 Old-Pipeline** (Weekly-Limit, Reset erst 22:00 CEST) — TMO-Record im Old-Format archivieren, **Retro-Migration post-Reset**
- **Token-Minimal:** Single-Pass-Analyse, keine Subagent-Exploration, keine Codex/CodeRabbit-Pässe (keine Code-Änderung)
- **Sync-Welle nach Urteil:** `log.md` + `CORE-MEMORY §4` + `Faktortabelle.md` + `STATE.md` + `score_history.jsonl` (+ `flag_events.jsonl` bei FLAG-Trigger)
- **SKILL.md Schritt 7:** Forward-Run via `backtest-ready-forward-verify`-Skill (Draft → Freshness → Tripwire → §28.2 Δ-Gate → Dry-Run → Append → git add)

## Caveats

- yfinance-Consensus kann mehrere Stunden lagen — Release-Consensus morgen kann minimal abweichen
- Historische Beats ≠ Garantie für Q1'26-Beat
- WC-Unwind-Hypothese hängt von Management-Commentary zum Inventory-Build-Down ab (Q1'25-Aufbau vs. Q1'26-Abbau muss im 10-Q explizit bestätigt werden)
- Nicht-Finanzberatung — Research-/Dokumentations-Zweck

---

**Referenz-Commits:** Session-State 22.04. Spät-Nacht (`c4d53ba` handover + `57bee6b` Phase-E-DONE).
**Skill-Nachweis:** `earnings-preview` aus `06_Skills-Pakete/earnings-preview.zip` (Single-Pass yfinance-Fetch, deterministisch reproduzierbar).
