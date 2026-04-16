# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 16.04.2026 | **Für:** Neue Cowork-Session

---

## ▶️ TRIGGER

```
Session starten
```

---

## 📋 Übergabe-Kontext

Bitte lies zuerst die vier Core-Dateien wie gewohnt (CORE-MEMORY, KONTEXT, INSTRUKTIONEN, Faktortabelle).
Danach gilt folgender Kontext aus der letzten Session:

---

## ✅ PRIO 1 ERLEDIGT — DEFCON v3.5 implementiert (16.04.2026)

Das Scoring-System-Audit ist abgeschlossen. DEFCON v3.5 ist live.

**Audit-Ergebnis:** 5×A, 1×B (PT-Upside Double-Counting — gefixt), 1×C (Gewichtsanpassung zurückgestellt auf 6 Monate)
**v3.5-Fix:** PT-Upside aus Technicals entfernt, Relative Stärke vs S&P500 als 0-3 Scored Metric (war: ±1 Tiebreaker)
**Anker-Shifts:** AVGO 86→85, SNPS 79→76, TMO 65→62 (⚠️ D3→D2), FICO 70→67, SPGI 77→74, MKL 82 (unverändert)

👉 **Die Satelliten-Queue ist jetzt entsperrt.** Alle Re-Analysen laufen unter v3.5.

---

## 🚀 Offene Analyse-Queue (v3.5 live — ENTSPERRT)

| Priorität | Aufgabe | Kontext |
|-----------|---------|---------|
| 🔴 1 | **!Analysiere MSFT** | Earnings 29.04. — FLAG-Review CapEx/OCF (zuletzt 65.3%). Bei <60% → FLAG auflösen, D3 volle Rate aktivieren |
| 🔴 2 | **!Analysiere AVGO** | Tariff-Exposure MY/TH ~35% Grenzfall. Insider-FLAG-Pflichtcheck: OpenInsider-Spalte „X"/„M" manuell verifizieren (Post-Vesting wahrscheinlich, aber nicht voreilig auflösen) |
| 🟡 3 | **!Analysiere COST** | Retail, US-lastig, Tariff-Ketteneffekte |
| 🟡 4 | **!Analysiere V** | Kein Tariff-Risiko, Konsumrückgang-Check |
| 🟡 5 | **!Analysiere APH** | Produktion CN/MY — Tariff-Exposure prüfen |
| 🟢 6 | **!Analysiere BRK.B** | Holding, defensiv |
| 🟢 7 | **!Analysiere VEEV** | SaaS, kein Tariff-Risiko |
| 🟢 8 | **!Analysiere RMS** | Luxury, EUR, Preismacht |
| 🟢 9 | **!Analysiere SU** | Industrie, EUR |

**Hinweis Liberation Day:** Bei jedem Satelliten Tariff-Exposure prüfen (CN/TW/MY/TH/VN >35% = FLAG). Kurse seit 02.04. teilweise -10–20% → Forward-Metriken als Primärbasis.

---

## 📅 Kritische Termine

| Datum | Ereignis | Aktion |
|-------|----------|--------|
| **23.04.2026** | TMO Q1 Earnings | FCF >$7.3B → DEFCON 4 / sonst ZTS-Aktivierung prüfen (TMO v3.5 Score 62, D🟠2 — Sparrate 50%) |
| **28.04.2026** | SPGI Earnings | QuickCheck SPGI (Score 74, Watchlist) |
| **29.04.2026** | MSFT Q3 Earnings | FLAG-Auflösung wenn CapEx/OCF <60% |
| **Mai 2026** | PEGA Earnings | Slot-16-Entscheidung |
| **01.05.2026** | Sparplan | !Rebalancing live testen (erster echter Lauf, noch nie gelaufen) |
| **Juni 2026** | Sparplan-Booster | 9.500€ Bausparvertrag + 2.000€ Steuererstattung |

---

## ⚙️ System-Status

| Komponente | Status |
|-----------|--------|
| defeatbeta MCP | ✅ WSL2 Ubuntu-24.04 — produktiv (Daten bis 03.04.2026) |
| Shibui Finance SQL | ✅ Primärquelle Technicals + FLAG-Historie |
| insider_intel.py | ✅ Form-4-Scanner 8 US-Satelliten |
| eodhd_intel.py / yfinance | ✅ Non-US Fundamentals (Cowork-Session: Web-Fallback) |
| SKILL.md | ✅ v3.5 — PT-Upside-Fix, Relative Stärke als Scored Metric |
| Briefing-Sync | ✅ Dreifach abgesichert (SessionStart/End-Hook + Claude-App-Push + Scheduled Task 09:54). Shortcuts: `!BriefingCheck`, `!SyncBriefing` (INSTRUKTIONEN.md §25) |
| Shibui SQL column | ⚠️ `code` nicht `ticker` — immer `WHERE code = 'TICKER'` |

---

## 📋 Backtest-Ready-Infrastruktur (NÄCHSTES PROJEKT — nach Satelliten-Queue)

**Status:** Audit ✅ abgeschlossen (16.04.2026), DEFCON v3.5 live — Spec v1.0 liegt bereit, v1.1 ausstehend  
**Spec:** `docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md`

### Wiedereinstieg

```
Lies docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md
→ Spec v1.1 updaten (10 bekannte Fehler unten) → writing-plans-Skill → Phase 1 bauen
```

Die 11 v3.5-Re-Analysen (Queue oben) werden die ersten Forward-Records im Archiv.

### Bekannte Fehler im Spec v1.0 (für v1.1 — nicht nochmal suchen)

**Kritisch:**
1. Arithmetik AVGO-Record §4.1: `eps_revisions_up_90d: 4` → `sentiment.gesamt` müsste 10, `score_gesamt` 87 statt 86. Fix: Rohwert auf 2.
2. Moat-Schema fehlt `rating_base_score: int` (0-20).
3. Malus-Konvention ambig — Empfehlung: **negative Zahlen** für einfache Summe.
4. `metriken_roh` unvollständig (fehlen u.a. `ath_distanz_pct`, `pt_upside_consensus_pct`, `konsensus_rating`, `sell_ratio_pct`, `ownership_pct`, `net_buy_6m_usd`, `max_single_sale_90d_usd`, `trend_200ma_richtung`).
5. Widerspruch §4.1↔§9.2: "unique" vs. "Sub-Record" → Duplikate verwerfen in `_parser_errors.log`.
6. `analyse_typ: "rescoring"` undefiniert → Enum: `["vollanalyse", "delta"]`.

**Klarheit:**
7. §12 Phase-Abhängigkeit: Phase 3 ← Phase 2. Phase 4 parallel zu 2+3.
8. §10.4 Benchmark-Liste: regelbasiert ("primärer Heimatindex") statt Enumeration.
9. §6.5: "Shibui primär, yfinance Fallback".
10. Datums-Placeholder vereinheitlichen auf `[YYYY-MM-DD]`.

### Spec-Entscheidungen (versionsunabhängig — nicht neu diskutieren)
- ✅ Zwei JSONL: `score_history.jsonl` + `flag_events.jsonl` (append-only, niemals UPDATE)
- ✅ Point-in-Time-Backfill via `git show <sha>:pfad`, nie Working Tree
- ✅ FLAG-Events paired (`flag_id` = `TICKER_FLAGTYP_YYYY-MM-DD`)
- ✅ `fcf_trend_neg` deterministisch: FCF YoY neg. in ≥3/4 Quartalen UND CapEx YoY positiv
- ✅ 4 Implementation-Phasen + Review 2028-04-01
- ✅ YAGNI: kein formaler Backtest, kein Dashboard, kein SQL

---

*🦅 SESSION-HANDOVER.md v1.5 | Dynastie-Depot | Bereinigt 17.04.2026 — DEFCON v3.5 live | Backtest-Ready nach Queue*
