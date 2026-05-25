# Veeva Systems (VEEV) — Pre-Earnings Brief Q1 FY27

**Report-Datum:** Mittwoch, 03.06.2026, after market close (amc)
**Quarter ending:** 30.04.2026
**Brief-Erstellt:** 25.05.2026 (T-9)
**Datenquellen:** Yahoo Finance via yfinance 1.3.0 (primär) · Finnhub Free-Tier (Cross-Check: Date / Quote / Estimates / News-Stream)
**Aktueller Score (PORTFOLIO.md):** 74 · DEFCON 🟡 3 · Sparrate 38,00€ · ✅ keine FLAG offen

> **⚠️ Pre-Append-Audit (Provenance-Gate-Hardening 28.04.2026, dynastie-depot v3.7.4):**
> Vor Schritt 7 (Archiv-Write der Tag-+1-Vollanalyse 04.06.) **manuell** pro Block (fundamentals/moat/technicals/insider/sentiment) prüfen:
> - Wenn ein Sub-Score `!= 0` → korrespondierender Rohwert in `metriken_roh` darf nicht null sein, ODER `quellen.<block>` enthält legitimes `*_carryover`-Suffix (Whitelist analog `provenance_gate.py`).
> - Bei Verstoß → Sub-Score auf 0 setzen ODER Rohwert nachtragen ODER `quellen` mit `_carryover`-Markierung versehen.
> - Joint-Confidence-Lift via Pre-Flight-Klausel ab v3.7.4 + Provenance-Gate (P3.5 fail-close, 8 Checks): 92% → 95%+.

> **📅 Date-Correction-Log (25.05.2026, T-9):**
> Vorherige PORTFOLIO/STATE-Einträge nannten 27.05.2026 als Earnings-Datum (Stale-yfinance-Pull 30.04.). Re-Check am 25.05. mit **Finnhub /calendar/earnings + Yahoo Calendar + Web-Recherche** konvergent auf **03.06.2026 amc**. Beide Aggregator-Quellen einig, IR-Bestätigung durch User. PORTFOLIO.md (Z. 20 + 58) und STATE.md (Z. 23) korrigiert. earnings_calendar.py-Tool-Lauf (25.05.) bestätigt 2026-06-03 mit Source `earnings_dates`, in trigger 🟢.

---

## 1. Setup (Stand 25.05.2026)

| Feld | Wert |
|------|------|
| Sektor / Industry | Healthcare / Health Information Services |
| Marktkapitalisierung | $26,14 Mrd |
| Aktueller Kurs | $160,17 |
| 52W Range | $148,05 – $310,50 (**−48,4 %** vom Hoch, **+8,2 %** vom Tief) |
| 1W / 1M Performance | +0,82 % / +2,57 % (Boden-Bildung, **kein Pre-Earnings-Run-Up**) |
| Day-Range (25.05.) | $158,86 – $162,60, Schluss +1,20 % (+$1,90) |
| Trailing / Forward P/E | 29,39 / **16,20** |
| Currency | USD |

**Technische Lage:** Diametraler Gegensatz zu MSFT-Q3-FY26-Setup (Recovery-Modus + Run-Up). VEEV in **prolonged share price weakness**: -48 % vom 52w-Hoch, nur +8 % über 52w-Tief, kein Pre-Earnings-Rally. Markt preist **kein Beat-Premium ein** — Expectations erkennbar de-risked.

**Multiple-Spread Trailing vs. Forward (29,4 → 16,2):** EPS-Re-Rating bereits eingepreist; bedeutet auch: Sub-Consensus oder Guide-Cut wäre brutaler Move, da Aktie keinen Puffer hat.

---

## 2. Consensus Estimates (Q1 FY27) — Cross-Check Yahoo × Finnhub

| Metrik | Yahoo Consensus | Finnhub | Δ | Verdict |
|--------|-----------------|---------|---|---------|
| **EPS** | **$2,135** (Range $2,10 – $2,185, 26 Analysten) | **$2,171** | +1,7 % | ✅ AGREE (innerhalb Yahoo-Hi/Lo) |
| **Revenue** | **$857,7 Mio** (Range $854,5 – $874,4 Mio, 24 Analysten) | **$870,7 Mio** | +1,5 % | ✅ AGREE (innerhalb Yahoo-Hi/Lo) |

**YoY-Wachstum (Yahoo-Basis):**
- EPS: +8,4 % (vs. $1,97 Q1 FY26)
- Revenue: **+13,0 %** (vs. $759,0 Mio Q1 FY26) — **decelleriert leicht** vs. 4Q-Q3 FY26 ($1,99 → $2,04 EPS-Trajektorie)

**EPS-Range Spread:** 4,0 % vom Consensus → **sehr eng**, Analysten konvergent, wenig Disagreement.
**Revenue-Range Spread:** 2,3 % vom Consensus → **noch enger**, klassisches Decel-Phase-Signal (Analysten haben gut gemodelt).

**Forward (Q2 FY27):** EPS $2,185 (+9,8 % YoY), Revenue $887,7 Mio (+12,5 % YoY).

**Full-Year FY27:** EPS $8,85 (+9,3 %), Revenue $3,60 Mrd (+12,7 %).
**Full-Year FY28:** EPS $9,88 (+11,7 %), Revenue $4,04 Mrd (+12,2 %) — **EPS-Akzeleration eingepreist** (während Rev-Wachstum stable), impliziert Margin-Expansion.

---

## 3. Beat/Miss Track Record (FY26 — letzte 4 Q)

| Quartal | Reporting | EPS Est | EPS Actual | Surprise % | Beat / Miss |
|---------|-----------|---------|------------|------------|-------------|
| Q1 FY26 | 30.04.2025 | $1,744 | $1,970 | **+12,98 %** | ✅ Beat (klar) |
| Q2 FY26 | 31.07.2025 | $1,900 | $1,990 | +4,75 % | ✅ Beat |
| Q3 FY26 | 31.10.2025 | $1,951 | $2,040 | +4,55 % | ✅ Beat |
| Q4 FY26 | 31.01.2026 | $1,935 | $2,060 | +6,45 % | ✅ Beat |

**Bilanz:** **4 / 4 Beats**, Ø Surprise **+7,18 %**, Bandbreite +4,55 % bis +12,98 %.
**Hist.-Norm-Implikation:** Konsens-Beat um +7 % → Actual-EPS ~$2,28 (Yahoo-Basis) oder ~$2,32 (Finnhub-Basis). Sub-$2,13 wäre erstmaliger Miss in vier Quartalen.

**Finnhub-Endpoint-Note:** `/stock/earnings` (Beat/Miss-Hist) Free-Tier-restricted → leer. Cross-Check der Hist nur Yahoo. Für Tag +1 ggf. defeatbeta-MCP konsultieren wenn zusätzliche Verifikation gewünscht.

---

## 4. Street Sentiment

### 4.1 Analyst Recommendations (Aktualität 25.05.)

| Bucket | now | -1m | -2m | -3m |
|--------|-----|-----|-----|-----|
| Strong Buy | 8 | 8 | 9 | 9 |
| Buy | 14 | 14 | 14 | 15 |
| Hold | 7 | 7 | 8 | 8 |
| Sell | 1 | 1 | 1 | 1 |
| Strong Sell | 0 | 0 | 0 | 0 |
| **Total** | **30** | 30 | 32 | 33 |

**Mix:** 22 / 30 positiv = **73 % Positiv-Skew**. 1 Sell stabil, kein Strong Sell. Über 3M leichter Drift StrongBuy 9 → 8, Buy 15 → 14 — **mild weicher, aber keine akute Verschlechterung**.

### 4.2 Price Targets

| Target | Wert | Implied vs. $160,17 |
|--------|------|---------------------|
| Mean | **$262,68** | **+64,0 %** |
| Median | $266,00 | +66,1 % |
| Low | $176,00 | +9,9 % |
| High | $350,00 | +118,5 % |

**Asymmetrie:** **Selbst der Bear-Target ($176) liegt über dem aktuellen Preis.** Street sieht Downside als limited; Mean/Median +64–66 % Upside ist außergewöhnlich für einen 🟡3-Compounder. Disconnect Preis-vs-Targets = Markt-Skepsis ODER Target-Update-Lag.

### 4.3 News-Sentiment-Cluster (Finnhub-Stream, letzte 14 Tage, 38 Items)

**Bearisch / Drawdown-Narrativ:**
- "Is It Time To Reassess VEEV After Prolonged Share Price Weakness?" (Yahoo)
- "Sprout Social and VEEV Shares Plummet" (Yahoo)
- "VEEV Stock Slides as Market Rises" (Yahoo)

**AI / CRM-Sunset-Fear-Counter:**
- **"VEEV: AI Fears Look Overdone, The Selloff Creates An Opportunity"** (SeekingAlpha) — Bull-Counter zur Salesforce-Migration-Sorge

**Bullish / Contrarian:**
- **"VEEV: Michael Burry Admires This Software Stock"** (Yahoo) — Burry-Position notable, nicht überdeuten
- "VEEV RTSM Momentum Signals Another Long-Term Growth Driver" (Yahoo) — Vault-Clinical-RTSM-Produkt-Tailwind
- "Is VEEV a Buy as Wall Street Analysts Look Optimistic?" (Yahoo) — bestätigt das +64 % Mean-Target-Upside

**Lesart:** Markt-Narrativ ist **binär** — AI-Sunset-Bear-Case vs. Compounder-Reversion-Bull-Case. Call-Question-Priority #1 = CRM-Migration-Color + AI-Adoption-Metrics.

---

## 5. Key Metrics to Watch (DEFCON-relevant — Score-74-Anker-Watch)

VEEV-Score 74 hängt primär an FCF-Stability + Subscription-Revenue-Decel-Resistance + Vault-Plattform-Wachstum. Folgende 5 Themen sind Tag-+1-Transcript-Fokus:

1. **Subscription-Revenue Growth & Net-Revenue-Retention (NRR)** — Konsens +13 % YoY für Q1 FY27 vs. FY26 mid-teens. Re-Akzeleration = bullish Catalyst; weitere Decel = Score-Watch.
2. **Vault Crossix / Compass / R&D-Vault — Commercial-Cloud-Mix** — Re-Platform-Story muss sichtbar progressieren (Bookings-Color, ARR-pro-Customer, neue Module-Adoption).
3. **AI / Veeva-CRM-Migration vs. Salesforce-Sunset (FY30)** — Concrete Customer-Switches, Bookings-Pipeline, Churn-Risk-Color. **Dominantes Narrativ — höchste Call-Priorität.**
4. **FY27 Full-Year Guidance** — Reaffirm / Raise / Cut für Revenue ($3,60 Mrd Konsens) + EPS ($8,85) + Op-Margin. **Wichtigster Single-Reaction-Driver.**
5. **Operating-Margin & FCF-Conversion** — VEEV-Score-74-Logik hängt an FCF-Stability. Margin-Compression-Signal wäre erster Trigger für Sub-Score-Re-Eval (DEFCON-Fundamentals-Block).

**Yahoo-quarterly-Data-Hygiene-Note:** `quarterly_income_stmt` und `quarterly_cashflow` kamen am 25.05. leer zurück (Yahoo-Endpoint-Quirk). Für Tag-+1-Vollanalyse **frische Q-Numbers via defeatbeta-MCP ziehen** (Memory `reference_defeatbeta_mcp_setup.md`).

---

## 6. Score-Move-Watch-Matrix (VEEV hat keine offene FLAG)

| Szenario | Score-Implikation | Sparraten-Action | Tag-+1-Aktion |
|----------|-------------------|-------------------|----------------|
| **Beat-and-Raise** (Rev+EPS-Beat + FY27 Guide-Raise) | 74 stable, leichter Uptilt möglich (Sub-Score Fundamentals +1) | Keine (Sparrate bleibt 38€) | Vollanalyse routine; ggf. Anker-Aktualisierung |
| **Mixed Beat** (eines Beat / eines Miss-or-Inline, Guide-Reaffirm) | 74 stable | Keine | Vollanalyse routine |
| **Light-Guide** (Beat aber FY27 Guide-Cut <3 %) | Watch — Score 74 → 72-73 möglich | Keine | Vollanalyse + Sub-Score Fundamentals + Margin-Trajectory-Re-Eval |
| **Sub-Consensus oder Guide-Cut >5 %** | Score-Re-Eval erwartbar (möglicher Move 74 → low-70s, in extremis 60s) | Keine sofort, Re-Eval-Output-getrieben | Vollanalyse Pflicht + Sub-Score-Recompute + ggf. FLAG-Eröffnung (Bookings-Decel-Watch) |
| **Margin-Decel-Signal** (Op-Margin-Compression > 100 bps QoQ ohne One-Time) | Sub-Score Fundamentals -1 → Score 74 → 73 | Keine | Vollanalyse + FCF-Conversion-Audit; potentieller FLAG-Open-Trigger wenn FCF-Margin <Threshold |

**No-FLAG-Status hält:** Wenn kein Outlier-Szenario eintritt, bleibt VEEV in 🟡3 / 38€ / ✅ konfiguriert; Score-Move auf Tag +1 isoliert; Pipeline-Item bei Re-Eval anzulegen falls Sub-Score-Move erfolgt.

---

## 7. Tag-0 / Tag-+1 Workflow (§19.1 Earnings-Call-Wait-Discipline)

### Tag 0 — Mittwoch 03.06.2026 nach Close
- **Skill:** `_extern/earnings-recap` für Press-Release-Recap (kein Score-Move)
- **FLAG-Quick-Check:** `archive_flag.py` falls Outlier-Szenario (Margin-Decel, Guide-Cut, Bookings-Crash); sonst nichts
- **Pre-Call-Snapshot:** CORE-MEMORY §12.veev mit aktuellen Werten einfrieren (Score 74 / DEFCON 🟡3 / Sparrate 38€ / Setup-Lesart aus diesem Brief)
- **Score-Move:** ❌ NICHT am Tag 0 — selbst bei Outlier nur FLAG-Event möglich, kein Score-Move ohne Transcript

### Tag +1 — Donnerstag 04.06.2026 morgens
- **Trigger:** `!Analysiere VEEV`
- **Skills:** `dynastie-depot` (Klasse-B-Vollanalyse) + `backtest-ready-forward-verify` (Schritt 7 programmatisch)
- **Daten:** Transcript via defeatbeta-MCP (`get_stock_earning_call_transcript`); Q-Numbers via `get_stock_quarterly_income_statement` + `get_stock_quarterly_cash_flow`
- **8-File-§18-Sync** wenn Score/FLAG/Sparrate sich bewegt: log.md + CORE-MEMORY + Faktortabelle + PORTFOLIO + score_history.jsonl + config.yaml + Rebalancing_Tool + Satelliten_Monitor (+ ggf. flag_events.jsonl + Watchlist falls §6-Drift)
- **xlsx-Post-Write-Smoke-Test** (§18.7) Pflicht via `03_Tools/xlsx-smoke-test.md`

### Parallel-Slot-Warnung
**AVGO meldet ebenfalls am 03.06.2026** (Drift-Erkenntnis aus `earnings_calendar.py --check`, 25.05.). Tag-+1-Slot (04.06.) wird damit potentiell **doppelt belegt** (VEEV Vollanalyse + AVGO Vollanalyse). Beide sind Klasse B. Token-Budget + Sequencing vorab planen — ggf. AVGO später am Tag oder AVGO Tag +2.

---

## 8. Synthesis (T-9)

**Setup:** Battered Compounder bei -48 % vom 52w-Hoch, kein Pre-Earnings-Run-Up, Forward-Multiple bereits aggressiv re-rated (P/E 16,2). Beat-Historie konstant (4/4, Ø +7,2 %), Konsens-Range eng, Analysten-Sentiment positiv (22/30, +64 % Mean-Upside).

**Erwartungs-Bar:** $2,13 EPS / ~$858 Mio Revenue, Hist.-Norm-Beat impliziert ~$2,28 / ~$874 Mio. FY27-Guidance-Reaffirm/Raise ist Reaction-Driver #1.

**Asymmetrie:** Risk/Reward asymmetrisch nach oben (Bear-Target $176 schon über Spot), aber **kein Margin-Of-Safety nach unten** — Sub-Consensus oder Guide-Cut würde brutalen Move triggern. Markt-Narrativ-Battle = AI-Sunset-Fear vs. Compounder-Reversion. Tag +1 Vollanalyse muss CRM-Migration-Color als ersten Prio-Block bringen.

---

**Brief-Status:** T-9 (Pre-Call-Prep). Erweiterung um VEEV-IR-Tag-0-Press-Release am 03.06. nach Close.
**Brief-Persistenz:** `02_Analysen/Earnings Reports/Veeva Systems/VEEV_pre-earnings_2026-06-03.md`
**Verwandte Files:** PORTFOLIO.md Z. 20 + 58 · STATE.md Z. 23 · earnings_calendar.py Tool-Run-Output 25.05.
