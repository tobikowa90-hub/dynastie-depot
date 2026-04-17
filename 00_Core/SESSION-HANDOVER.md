# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 17.04.2026 nach v3.7-Deployment | **Für:** Nächste Session (Claude Code empfohlen)

---

## ▶️ TRIGGER

```
Session starten
```

Danach: freie Agenda (siehe Offene Punkte unten) oder Earnings-Trigger.

---

## ✅ LETZTE SESSION (17.04.2026) — ERLEDIGT

**DEFCON v3.7 „System-Gap-Release" deployed.** Commit `d890d57`, 14 Dateien.

### Was geändert wurde
- **Fix 1 Quality-Trap als Interaktionsterm** (nicht additiver Moat-Malus): Wide Moat + Fwd P/E >30 → Fwd-P/E-Subscore hart 0; Wide Moat + P/FCF >35 → P/FCF-Subscore hart 0; 22–30/22–35 → Subscore max 1. Grund: Applied Learning 17.04. verbietet Double-Counting.
- **Fix 2 Operating Margin** (max 2 Pt.; >30%→2, 15–30%→1, <15%→0). Exceptions COST+BRK.B. Fundamentals-Block-Cap hart bei 50.
- **Fix 3 Analyst-Bias-Kalibrierung:** Strong-Buy >60% → 1 (Crowd-Malus); Sell-Ratio <3%→1 (Warning), 3–10%→3 (Healthy), >10%→0.
- **v3.6 (F-Score/GP-TA/Accrual-Bonus) verworfen** wegen Double-Counting mit dekomponierten Sub-Signalen.

### Backtest-Impact (keine DEFCON-Shifts) + Live-Verify-Status
| Ticker | v3.5 → v3.7 | DEFCON | Rate | Live-Verify |
|--------|-------------|--------|------|-------------|
| ASML | 68 → 66 → **68** | 🟡 3 | 33,53€ | ✅ 17.04. (±2 → Post-Q1 Vollanalyse: 68 bestätigt). **Watch Fwd P/E FY27 30,30 → D4-Upside bei <30** |
| AVGO | 85 → 84 | 🟢 4 | 33,53€ (Insider-Review) | ⏳ offen (Q3 FY26 Earnings) |
| MSFT | 60 → 59 | 🟠 2 | 0€ (🔴 CapEx/OCF) | ⏳ offen (29.04.) |
| TMO | 62 → 63 | 🟠 2 | **16,76€** (D2 aus v3.5 Audit) | ✅ 17.04. (±1) — nur P/FCF-Zweig Fix-1 |
| RMS | 69 → 68 | 🟢 4 | 33,53€ | ✅ 17.04. (±2) — beide Fix-1 + Screener-Exception |
| VEEV | 74 → 74 | 🟢 4 | 33,53€ | ⏳ offen |
| SU | 71 → 69 | 🟢 4 | 33,53€ | ⏳ offen (H1 Report Juli/Aug) |
| BRK.B | 75 → 75 | 🟢 4 | 33,53€ | ⏳ offen (Q-Earnings Mai) |
| V | 86 → 86 | 🟢 4 | 33,53€ | ⏳ offen (~22.04.) |
| APH | 61 → 63 | 🟡 3 | 0€ (🔴 Score-basiert) | ⏳ offen (23.07.) |
| COST | 69 → 69 | 🟢 4 | 33,53€ | ⏳ offen (Q1 FY27 ~Dez) |

**Sparraten-Nenner:** 8×1.0 (D4/D3) + 1×0.5 (TMO D2) = **8.5** → 285€ / 8.5 = 33,53€ volle, 16,76€ D2.

### Live-Verify-Fortschritt (Schritt-2 Backtest-Plan)
**3/11 verifiziert (17.04.2026) — alle Approximationen innerhalb ±2 Toleranz bestätigt.** Commit `e13cfd3`.

- **Kritische Fix-1-Kandidaten abgearbeitet:** ASML, RMS (beide Wide Moat + Fwd P/E >30 + P/FCF >35 → beide Zweige hart 0).
- **Differenzierungs-Case validiert:** TMO (nur P/FCF-Zweig, Fwd P/E 20,80 unter Schwelle) — beweist: Fix-1 ist echter Interaktionsterm, kein Pauschal-Malus.
- **Rest-Tickers (8) bei regulärem Earnings-Trigger** verifizieren (keine Einzel-Pushes nötig — Morning-Briefing erfasst).

### Skill-Deployment
- `01_Skills/dynastie-depot/SKILL.md` (Source, v3.7 inhaltlich)
- `06_Skills-Pakete/dynastie-depot_v3.7.zip` (mit `SKILL.md` Rename für Desktop-App) — manuell installiert, ersetzt v3.5.

### Noch offen (User-Pending)
- Keine offenen Tool-/Doku-Sync-Punkte. Rebalancing_Tool + Satelliten_Monitor + alle 00_Core/-Dateien + Vault sind 17.04.2026 auf v3.7 / ASML 68 synchronisiert.

---

## 📅 NÄCHSTE TRIGGER (nach Datum)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| ~2026-04-22 | V | B | Q2 FY26 Earnings — QuickCheck + Sparplan bestätigen |
| 2026-04-23 | TMO | B | Q1 Earnings — **FCF >$7.3B nötig** für FCF-Yield >4%. D2-Kritik-Trigger. |
| 2026-04-28 | SNPS | B | Q1 Earnings — Watchlist (Score 79 Ersatz ASML) |
| 2026-04-28 | SPGI | B | Q1 Earnings — Watchlist (Score 77) |
| **2026-04-29** | **MSFT** | **C** | **Q3 FY26 Earnings — CapEx-FLAG-Review: bereinigt <60% = Auflösung.** |
| Mai 2026 | BRK.B / CPRT / ZTS / PEGA | B | Q-Earnings + Watchlist |
| Juni 2026 | — | — | Bausparvertrag 9.500€ + Steuererstattung ~2.000€ → Slot-Entscheidung |
| Juli/Aug 2026 | RMS + SU | — | H1 Reports → Re-Check D4-Exceptions |
| 2026-07-23 | APH | C | Q2 Earnings — FLAG-Review + Tariff-Impact |
| Q2 2026 | GOOGL | C | FLAG-Review |
| Q3 FY26 | AVGO | C | Insider-FLAG-Review — erneuter OpenInsider-Check |

---

## 🧭 START-PROTOKOLL FÜR NÄCHSTE SESSION

1. `Session starten` — Claude liest automatisch **nur `00_Core/STATE.md`** (seit 17.04.2026). Andere 00_Core-Dateien on-demand.
2. Kompakte Lage-Zusammenfassung (max. 10 Zeilen).
3. `dynastie-depot`-Skill aktiv (v3.7 Desktop-installiert).
4. Falls Earnings-Tag: `!QuickCheck <TICKER>` oder `!Analysiere <TICKER>`.

---

## 🚫 WAS NICHT ZU TUN

- **Keine** Rückkehr zu v3.6 (F-Score/GP-TA/Accrual-Bonus) — verworfen.
- **Kein** additiver Moat-Malus für Quality-Trap — Interaktionsterm bleibt (Anti-Double-Counting).
- **Keine** Sparraten-Diskussion — 8.5-Nenner / 33,53€ / 16,76€ fix bis nächster DEFCON-Shift.

---

## 📂 KRITISCHE DATEIEN

- `00_Core/CORE-MEMORY.md` (v1.7) — institutionelles Gedächtnis
- `00_Core/INSTRUKTIONEN.md` (v1.4) — §5 Scoring + §5a Sentiment + §22 Sparplan
- `00_Core/Faktortabelle.md` (v3.7) — Score-State
- `01_Skills/dynastie-depot/SKILL.md` + `config.yaml` (v3.7)
- `07_Obsidian Vault/.../synthesis/Wissenschaftliche-Fundierung-DEFCON.md` (v3.7 Änderungsprotokoll)

---

## 🔬 System-Reife-Tracker

- v3.5 (16.04.): 85%
- **v3.7 (17.04.): ~92%** — 3 operative Gaps geschlossen
- Weitere Hebel (nicht akut): Verhaltens-Layer (Execution Discipline), Makro-Overlay, Position-Sizing-Regel
