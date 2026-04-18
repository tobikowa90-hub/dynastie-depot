# 🎯 STATE.md — Dynasty-Depot Live-Status
**Single Entry Point für Session-Start** | Stand: 18.04.2026 (TMO Forward-Vollanalyse) | System: DEFCON v3.7 (Schema-SKILL-Threshold-Alignment)

> **Prinzip:** Diese Datei genügt für 90% der Sessions. Tiefere Quellen on-demand:
> - Lektionen/Historie → `CORE-MEMORY.md`
> - Workflows/Scoring-Skalen → `INSTRUKTIONEN.md`
> - Strategie/Allokation → `KONTEXT.md`
> - Score-Detail → `Faktortabelle.md`
> - Last-Session-Handover → `SESSION-HANDOVER.md`

---

## Portfolio-State (11 Satelliten)

| Ticker | Score | DEFCON | Rate | FLAG | Nächster Trigger |
|--------|-------|--------|------|------|------------------|
| AVGO | 84 | 🟢 4 | 35,63€ | ⚠️ Insider-Review (OpenInsider!) | Q3 FY26 |
| BRK.B | 75 | 🟡 3 | 35,63€ | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | 35,63€ | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | 35,63€ | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | 35,63€ | ✅ Screener-Exception | Q1 FY27 ~Dez |
| RMS | 68 | 🟡 3 | 35,63€ | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | 35,63€ | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| V | **63** | **🟠 2** | **17,81€** | ✅ | **28.04. Q2 FY26 — D2-Entscheidung** |
| TMO | **64** | 🟠 2 | 17,81€ | ✅ (fcf_trend_neg schema-trigger, WC-Noise → **nicht aktiviert**) | **23.04. Q1 — FLAG-Resolve-Gate** |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |

**Sparraten-Nenner:** 7×1.0 + 2×0.5 + 2×0 = **8.0** → 35,63€ volle / 17,81€ D2 / 0€ FLAG. **Summe 285€** ✓

> **18.04.2026 Änderung:** V-Forward-Vollanalyse (63, D2) ersetzt 17.04.-Backfill-Projektion (86, D4) — siehe CORE-MEMORY §11. Gleichzeitig Schema-SKILL-Threshold-Drift gefixt: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 (Label-Fix, Sparrate unverändert), APH D3→D2 (FLAG überschreibt Sparrate weiterhin). Nenner schrumpft von 8.5 auf 8.0, volle Rate steigt 33,53€ → 35,63€.

---

## Aktive Watches

- **V D2-Kritik (NEU 18.04.):** 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA, Crowd-Sell-Ratio 0%. Q2 FY26 am 28.04. entscheidet: Beat + Guidance-Bestätigung → Technicals-Reversal möglich (zurück Richtung D3). Miss → weiterer Downshift Richtung D1.
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- **AVGO Insider $123M (90d)** — wahrscheinlich Post-Vesting (Broadcom-Muster Tan/Brazeal/Spears). Vor FLAG-Aktivierung OpenInsider manuell prüfen.
- **TMO D2-Kritik + FLAG-Resolve-Gate (NEU 18.04.):** Score 64 (Forward), fcf_trend_neg schema-getriggert (FY25 FCF -13,4% YoY, CapEx +8,9%) aber **nicht aktiviert** — WC-Delta FY25 -1766M erklärt FCF-Rückgang vollständig (>Δ FCF -974M), 4J-Trajektorie FY22-25 $6,9→6,9→7,3→6,3B zeigt Plateau, OpInc +5,1%. Q1 23.04. = natürlicher Resolve-Gate: WC-Unwind + FCF-Recovery bestätigt → kein FLAG; fehlende Reversibilität → fcf_trend_neg-Trigger nachtragen. Ersatz-Vorbereitung ZTS aktiv.
- **MSFT FLAG-Auflösungs-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance Lease $19.5B raus) = Auflösung. Darüber = Veto-Verschärfung.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| **23.04.** | **TMO** | **B** | **Q1 — D2-Entscheidung + fcf_trend_neg Resolve-Gate (WC-Unwind?)** |
| **28.04.** | **V** | **B** | **Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)** |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

---

## System-Zustand

- **Scoring:** DEFCON v3.7 — Quality-Trap-Interaktionsterm (kein additiver Moat-Malus), OpM max 2Pt., Analyst-Bias-Kalibrierung, Fundamentals-Cap 50. Schema-Thresholds 18.04. auf SKILL.md aligned (≥80 D4 / 65-79 D3 / 50-64 D2 / <50 D1). **INSTRUKTIONEN §27 Scoring-Hygiene neu (18.04.):** Double-Counting-Vermeidung + Bonus-Cap-Check + Projection-Layer-Regel + Multi-Source-Drift-Check. System-Reife ~96%.
- **Live-Verify v3.7:** 5/11 bestätigt — V (18.04. Forward 72→63 nach Advisor-Review), **TMO (18.04. Forward 63→64, fcf_trend_neg struktureller Disclosure)**, ASML ±2, RMS ±2. Rest bei Earnings-Trigger.
- **Allokation:** 65/30/5 (ETF 617,50€ / Satelliten 285€ / Gold 47,50€), US-Cap 63% / Ist ~46%.
- **MCP-Status:** defeatbeta (WSL2 Ubuntu-24.04), Shibui, WebSearch — alle live. Non-US via yfinance.
- **Morning Briefing:** Trigger v2.1 täglich 10:00 MESZ (16 Symbole, Yahoo-Gap BRK.B/RMS/SU).
- **Backtest-Ready:** aktiv seit 17.04.2026 — **27 Score-Records** (24 Backfill + 3 Forward: V_vollanalyse 72 + V_rescoring 63 + **TMO_vollanalyse 64**) + 2 FLAG-Events. SKILL.md Schritt 7 Write-Pflicht. Review 2028-04-01, Interim-Gates 2026-10-17.

---

## Navigation (on-demand)

| Wenn du brauchst… | Lies… |
|-------------------|-------|
| Aktuellen Stand, Trigger, Sparraten | **Diese Datei** |
| Letzte Session-Details, v3.7 Deployment | `SESSION-HANDOVER.md` |
| Scoring-Regeln, Sparplan-Formel, Workflows | `INSTRUKTIONEN.md` |
| Strategie, Allokation, Satelliten-Struktur | `KONTEXT.md` |
| Scoring-Lektionen, Positions-Entscheidungen, Audit-Log | `CORE-MEMORY.md` (Sections 2–10) |
| Meilenstein-Chronik vor 15.04.2026 | `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` |
| Score-Detail pro Ticker | `Faktortabelle.md` |

**Sync-Pflicht bei Score/FLAG/Sparraten-Änderung:** log.md + CORE-MEMORY.md + Faktortabelle.md + **STATE.md** + **score_history.jsonl** (+ ggf. **flag_events.jsonl**) (§18 INSTRUKTIONEN — alle sechs, immer).
**Briefing-Sync:** `!SyncBriefing` vor Session-Ende, wenn 00_Core/ geändert wurde (§25).

---
*🦅 STATE.md v1.0 | Dynasty-Depot | Entry-Point statt 1.200-Zeilen-Auto-Read*
