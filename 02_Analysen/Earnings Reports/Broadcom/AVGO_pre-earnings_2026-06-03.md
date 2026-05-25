# Broadcom (AVGO) — Pre-Earnings Brief Q2 FY26

**Report-Datum:** Mittwoch, 03.06.2026, after market close (amc)
**Quarter ending:** ~03.05.2026 (Fiskal-Q2 FY26, Periode Feb–Apr/Mai 2026)
**Brief-Erstellt:** 25.05.2026 (T-9)
**Datenquellen:** Yahoo Finance via yfinance 1.3.0 (primär) · Finnhub Free-Tier (Cross-Check: Date / Quote / Estimates / News-Stream)
**Aktueller Score (PORTFOLIO.md):** 53 · DEFCON 🟠 2 · Sparrate **0€ (FLAG-Override)** · 🔴 FLAG Insider-Selling 90d **$106M+** (seit 27.04.) · **FLAG-Resolve-Gate <$20M Diskr.**

> **⚠️ Pre-Append-Audit (Provenance-Gate-Hardening 28.04.2026, dynastie-depot v3.7.4):**
> Vor Schritt 7 (Archiv-Write der Tag-+1-Vollanalyse 04.06.) **manuell** pro Block (fundamentals/moat/technicals/insider/sentiment) prüfen:
> - Wenn ein Sub-Score `!= 0` → korrespondierender Rohwert in `metriken_roh` darf nicht null sein, ODER `quellen.<block>` enthält legitimes `*_carryover`-Suffix (Whitelist analog `provenance_gate.py`).
> - Bei Verstoß → Sub-Score auf 0 setzen ODER Rohwert nachtragen ODER `quellen` mit `_carryover`-Markierung versehen.
> - **Insider-Block besonders kritisch:** FLAG-Resolve-Entscheidung hängt direkt am 90d-Aggregat — Quelle muss SEC EDGAR Form 4 sein (via `insider-intelligence`-Skill), nicht Yahoo-Sekundär.

> **📅 Date-Discovery-Log (25.05.2026, T-9):**
> AVGO Q2 FY26 Earnings am 03.06.2026 (amc) war im PORTFOLIO **bisher nicht als Trigger gelistet** — erkannt durch Drift-Lauf von `03_Tools/earnings_calendar.py --check --alert-window 14`. Yahoo Calendar + Finnhub `/calendar/earnings` konvergent auf 03.06.2026 amc (Finnhub: `epsEstimate 2.4645`, `revenueEstimate $22.91B`, `quarter 2`, `year 2026`). PORTFOLIO.md Z. 18 + 30-Tage-Trigger-Tabelle + STATE.md Z. 23 nachgezogen. **Parallel-Slot mit VEEV** — beide reporten 03.06. amc.

---

## 1. Setup (Stand 25.05.2026)

| Feld | Wert |
|------|------|
| Sektor / Industry | Technology / Semiconductors |
| Marktkapitalisierung | **$1.961 Mrd** (Trillion-Cap) |
| Aktueller Kurs | $414,14 |
| 52W Range | $231,13 – $442,36 (**−6,4 %** vom Hoch, **+79,2 %** vom Tief) |
| 1W / 1M Performance | −2,60 % / −1,38 % (leichte Konsolidierung nahe Hoch, **kein Pre-Earnings-Crash**) |
| Day-Range (25.05.) | $410,21 – $419,99, Schluss −0,10 % (−$0,43) |
| Trailing / Forward P/E | **80,57 / 22,68** (extreme Multiple-Compression eingepreist) |
| Dividend Yield | 0,63 % |
| Currency | USD |

**Technische Lage:** Diametraler Gegensatz zu VEEV-Parallel-Slot — AVGO **near 52w-Hoch** nach +79 % Rally vom Tief, leichte Konsolidierung in den letzten Wochen aber keine Schwäche. Markt preist **Beat-and-Raise bereits ein**; Korrektur-Anfälligkeit bei Disappointment hoch.

**Multiple-Spread Trailing vs. Forward (80,6 → 22,7):** Massive EPS-Akzeleration eingepreist (Konsens-FY26-EPS-Growth +66,6 % YoY). Forward-Multiple bei 22,7 ist nicht-billig, aber relativ zum Wachstum gerechtfertigt **wenn AI-Akzeleration nachhaltig**.

---

## 2. Consensus Estimates (Q2 FY26) — Cross-Check Yahoo × Finnhub

| Metrik | Yahoo Consensus | Finnhub | Δ | Verdict |
|--------|-----------------|---------|---|---------|
| **EPS** | **$2,391** (Range $2,36 – $2,50, 36 Analysten) | **$2,465** | +3,1 % | ✅ AGREE (innerhalb Yahoo-Hi/Lo) |
| **Revenue** | **$22,08 Mrd** (Range $21,88 – $22,40 Mrd, 35 Analysten) | **$22,91 Mrd** | +3,7 % | 🟡 AGREE knapp (Finnhub-Wert über Yahoo-High) |

**YoY-Wachstum (Yahoo-Basis):**
- EPS: **+51,3 %** (vs. $1,58 Q2 FY25)
- Revenue: **+47,2 %** (vs. $15,00 Mrd Q2 FY25) — **Massives Wachstum**, dominiert durch AI-Custom-ASIC + VMware-Integration-Cycling

**EPS-Range Spread:** 5,9 % vom Consensus → **moderat** (etwas weiter als VEEV's 4,0 %), aber kein "high uncertainty".
**Revenue-Range Spread:** 2,4 % vom Consensus → **eng**, klassisches Wachstums-Anker-Signal.

**Forward (Q3 FY26):** EPS **$3,207** (+89,8 % YoY vs. $1,69), Revenue **$28,69 Mrd** (+79,9 % YoY vs. $15,95 Mrd).
**⚠️ Range-Spread Q3-EPS: 49 % (von $2,69 – $4,26).** **Maximale Analysten-Disagreement zur AI-Acceleration-Sustainability** — das ist der eigentliche Bull/Bear-Battle-Ground im Q2-Call.

**Full-Year FY26:** EPS $11,36 (+66,6 % YoY), Revenue $103,27 Mrd (+61,7 %). Range Rev $85,6 – $119,2 Mrd (Spread 32 %).
**Full-Year FY27:** EPS $18,26 (+60,8 %), Revenue $158,86 Mrd (+53,8 %). Range Rev $90,7 – $197,4 Mrd (**Spread 104 %!**) — beispiellose FY27-Unsicherheit.

---

## 3. Beat/Miss Track Record (letzte 4 Q — alle Beats, aber knapp)

| Quartal | Reporting | EPS Est | EPS Actual | Surprise % | Beat / Miss |
|---------|-----------|---------|------------|------------|-------------|
| Q2 FY25 | 30.04.2025 | $1,571 | $1,58 | +0,59 % | ✅ Beat (knapp) |
| Q3 FY25 | 31.07.2025 | $1,663 | $1,69 | +1,60 % | ✅ Beat (knapp) |
| Q4 FY25 | 31.10.2025 | $1,868 | $1,95 | +4,38 % | ✅ Beat |
| Q1 FY26 | 31.01.2026 | $2,023 | $2,05 | +1,32 % | ✅ Beat (knapp) |

**Bilanz:** **4 / 4 Beats**, Ø Surprise **+1,97 %**, Bandbreite +0,59 % bis +4,38 %.

**Kontrast zu VEEV-Parallel-Slot:** AVGO beat-Surprises sind **deutlich knapper** (Ø +2 % vs. VEEV +7,2 %). Konsensus ist bei AVGO sehr nahe am Tatsächlichen — Analysten haben das Wachstum gut modelliert. **Sub-Consensus wäre erstmaliger Miss in vier Quartalen** und würde wegen knapper Beat-Margen-Historie als seltenes Negativ-Signal interpretiert.

**Hist.-Norm-Implikation:** Konsens-Beat um +2 % → Actual-EPS ~$2,44 (Yahoo) / ~$2,51 (Finnhub). Beat >5 % wäre über historischer Norm und positiver Catalyst.

**Finnhub-Endpoint-Note:** `/stock/earnings` (Beat/Miss-Hist) Free-Tier-restricted → leer. Cross-Check via Yahoo. Für Tag +1 ggf. defeatbeta-MCP konsultieren.

---

## 4. Street Sentiment

### 4.1 Analyst Recommendations (Stand 25.05.)

| Bucket | now | -1m | -2m | -3m |
|--------|-----|-----|-----|-----|
| Strong Buy | 8 | 7 | 7 | 8 |
| Buy | 36 | 36 | 40 | 40 |
| Hold | 3 | 3 | 2 | 2 |
| Sell | 0 | 0 | 0 | 0 |
| Strong Sell | 0 | 0 | 0 | 0 |
| **Total** | **47** | 46 | 49 | 50 |

**Mix:** 44 / 47 positiv = **93,6 % Positiv-Skew** (vs. VEEV 73 %). **Quasi-Unanimer Bullish-Konsens** — kein einziger Sell oder Strong Sell. Über 3M leichter Drift Buy 40 → 36, Hold 2 → 3 — **mild weicher**, aber kein Strong-Buy-Verlust.

### 4.2 Price Targets

| Target | Wert | Implied vs. $414,14 |
|--------|------|---------------------|
| Mean | **$480,49** | **+16,0 %** |
| Median | $495,00 | +19,5 % |
| Low | **$215,88** | **−47,9 %** |
| High | $630,00 | +52,1 % |

**⚠️ Asymmetrie umgekehrt zu VEEV:** Bei VEEV liegt selbst der Bear-Target +10 % über Spot (Markt sieht limitiertes Downside). Bei AVGO ist Bear-Target **−48 % unter Spot** — Bear-Case impliziert "Aktie kann sich halbieren". Mean-Upside nur +16 % bedeutet **moderater Bullish-Anchor**. **Risk/Reward damit asymmetrisch nach unten** bei einem Disappointment-Szenario.

### 4.3 News-Sentiment-Cluster (Finnhub-Stream, letzte 14 Tage, **247 Items**)

Sehr hohes News-Volumen (vs. VEEV 38 Items) — AVGO ist im aktuellen Markt-Narrativ zentral positioniert.

**Bullish / AI-Infrastruktur-Tailwind:**
- **"Citi names Broadcom stock top semiconductor pick for 2026"** (Yahoo) — Analyst-Conviction-Signal
- **"Broadcom's AI Packaging Bet Gets Bigger. Wall Street Is Betting on More Upside"** (Yahoo)
- **"Druckenmiller Dumped Nvidia but Loaded Up on These 3 AI Infrastructure Stocks"** (Yahoo) — AVGO in den 3, Big-Hedge-Fund-Rotation-Signal
- "Meta, Broadcom Launch $125M UCLA AI Chip Hub" — Strategischer Customer-Tie-Signal
- "This Tech Stock Pays a Growing Dividend and Rides Every AI Tailwind" (Yahoo)

**Bearish / Valuation-Skepsis:**
- **"The Broadcom Stock Paradox: Why a $2 Trillion Valuation Ignores the Base Economics of Custom Chips"** (Yahoo) — Multiple-Skepsis-Narrativ
- "Nvidia's Hidden $60 Billion Business Is About to Overtake Broadcom" (Yahoo) — Competitive-Pressure-Story
- "This AI Stock Will Beat Nvidia, AMD, Broadcom, Intel to Become Biggest Winner in AI Inference" (Yahoo)
- **"Presidential Trading Puts Broadcom Valuation And Policy Risks In Focus"** (Yahoo) — Politik-Risk-Schwelle

**Lesart:** Markt-Narrativ ist **bipolar** — AI-Infrastruktur-Tailwind vs. Valuation-Concern / Competitive-Squeeze. Call-Question-Priorities:
1. AI-Custom-ASIC-Revenue-Akzeleration (Google TPU, Meta-Custom-Chips, OpenAI-Speculation)
2. FY27-Guidance-Specifics (Range $90,7–197,4 Mrd Rev signalisiert Analysten-Maximalkonfusion)
3. Insider-Selling-90d-Update (FLAG-Resolve-Gate)

---

## 5. Key Metrics to Watch (DEFCON-relevant — FLAG-Resolve-Gate-Fokus)

Da AVGO 🔴 FLAG aktiv hat (Insider-Selling 90d $106M+ seit 27.04., Score 53 D2), ist Tag-+1-Transcript-Fokus **dual**: FLAG-Resolution + Score-Re-Eval-Trigger.

1. **🔴 FLAG-Resolution-Metrik #1: Insider-Selling 90d-Update** — Nicht im Earnings-Print enthalten, aber via SEC EDGAR Form-4 (Skill `insider-intelligence`) am Tag 0 + Tag +1 frische 90d-Aggregat ziehen. **Resolve-Trigger: <$20M Q-to-Q-Netto-Selling.** Bei Beibehaltung >$50M = FLAG-stable. Bei Beschleunigung >$150M = FLAG-Vertiefung → potentieller DEFCON-Drop 🟠2 → 🔴1.
2. **AI / Custom-ASIC-Revenue-Akzeleration** — Bookings-Trajektorie Google TPU + Meta-Custom-Chips + OpenAI-Spekulation. Konsens für FY26 Rev $103 Mrd (+62 % YoY) basiert primär auf AI-Wachstums-Annahme. Concrete Customer-Color = Reaction-Driver.
3. **VMware-Integration-Revenue + Margin** — VMware-Integration-Cycle vollständig in Year-Over-Year-Vergleich (Q2 FY25 hatte teilweisen VMware-Beitrag). Op-Margin-Trajektorie und FCF-Conversion müssen Integrations-Synergien zeigen.
4. **FY26 Full-Year Guidance** — Reaffirm / Raise / Cut Revenue ($103 Mrd Konsens) + EPS ($11,36) + Op-Margin. **Wichtigster Single-Reaction-Driver** nach FLAG-Resolution.
5. **Customer-Concentration-Risk** — Top-3-Customer-Mix (Apple ~20 %, Google + Meta steigend). Konzentration-Increase = Sub-Score-Watch (Moat-Block).
6. **FCF-Margin & Capital-Return-Trajectory** — Dividende ist im FLAG-Override 0€-Sparrate-Modus für uns nicht direkt relevant, aber FCF-Stability ist Score-53-Anker.

**Yahoo-quarterly-Data-Hygiene-Note:** Analog VEEV-Brief — bei Tag-+1-Vollanalyse Q-Numbers via defeatbeta-MCP frisch ziehen, nicht yfinance-quarterly-stmt verwenden (Endpoint-Quirk).

---

## 6. FLAG-Decision-Matrix (analog MSFT-Template; AVGO 🔴 FLAG aktiv)

| Szenario | FLAG-Status | Score-Implikation | DEFCON / Sparrate | Tag-+1-Aktion |
|----------|-------------|-------------------|---------------------|----------------|
| **Insider-Selling 90d <$20M + Beat-and-Raise** | 🟢 **RESOLVED** | Score-Re-Eval erwartbar (53 → 60+); DEFCON-Lift möglich | 🟠 2 → 🟡 3, Sparrate 0€ → 19€ oder 38€ | FLAG-Resolve-Append (`archive_flag.py`) + Vollanalyse + 8-File-Sync |
| **Insider-Selling 90d $20–50M + Beat-Inline** | 🟡 **STABLE-IMPROVING** | Score 53 stable mit positivem Bias | 🟠 2, 0€ | Vollanalyse + FLAG-Watch; nächster Re-Eval bei Q3 FY26 Print (~Sept) |
| **Insider-Selling 90d $50–106M + Beat-Inline** | 🟡 **STABLE** | Score 53 stable | 🟠 2, 0€ | Vollanalyse routine; FLAG bleibt aktiv |
| **Insider-Selling >$150M (Beschleunigung) ODER Bookings-Crash** | 🔴 **VERTIEFT** | Score 53 → Sub-50-Risk (möglicher Move 53 → 45–48) | 🟠 2 → potentiell 🔴 1, 0€ stable | Vollanalyse + Sub-Score-Re-Eval kompakt; PIPELINE-Item-Append |
| **Miss + Guide-Cut + Insider-stabil** | 🔴 **STABLE-aber-Earnings-Schwäche** | Score 53 → 47–50 (Sub-Score Fundamentals -1, Sentiment-Sub-Score -1) | 🟠 2 → 🔴 1 möglich, 0€ stable | Vollanalyse + Sub-Score-Recompute + FLAG-Compound-Watch |
| **Customer-Concentration-Increase >5 pp Top-3** | unabhängig | Sub-Score Moat -1 → 53 → 52 | unverändert (FLAG dominiert) | Vollanalyse + Moat-Block-Refresh |

**FLAG-Resolve-Pfad-Wahrscheinlichkeit-Estimate:** Niedrig–Moderat. Insider-Selling-90d ist von Natur aus stabil bis Insider-Activity-Pattern-Wechsel; $106M+ → <$20M in einem Quartal erfordert entweder massiven Buy-Side-Insider-Move ODER deutlich rückläufige Sell-Side-Aktivität. Ohne harten Katalysator unwahrscheinlich.

---

## 7. Tag-0 / Tag-+1 Workflow (§19.1 + FLAG-Resolve-Pfad)

### Tag 0 — Mittwoch 03.06.2026 nach Close
- **Skills:** `_extern/earnings-recap` für Press-Release-Recap + `insider-intelligence` für 90d-Form-4-Aggregat-Update
- **FLAG-Quick-Check:** `03_Tools/backtest-ready/archive_flag.py` bei Auslöser-Szenario (Miss, Guide-Cut, Insider-Acceleration → FLAG-Vertiefung; <$20M-Resolution → FLAG-Resolved-Trigger; sonst FLAG bleibt aktiv ohne Event)
- **Pre-Call-Snapshot:** CORE-MEMORY §12.1 (AVGO bestehend) updaten mit Q2-Werten + Insider-90d-Aggregat + Setup-Lesart aus diesem Brief
- **Score-Move:** ❌ NICHT am Tag 0 — selbst bei Outlier nur FLAG-Event möglich, kein Score-Move ohne Transcript

### Tag +1 — Donnerstag 04.06.2026 morgens
- **Trigger:** `!Analysiere AVGO`
- **Skills:** `dynastie-depot` (Klasse-B-Vollanalyse mit FLAG-Resolve-Gate-Evaluation explizit) + `backtest-ready-forward-verify` (Schritt 7 programmatisch) + `insider-intelligence` (frischer 90d-Pull post-Earnings)
- **Daten:** Transcript via defeatbeta-MCP (`get_stock_earning_call_transcript`); Q-Numbers via `get_stock_quarterly_income_statement` + `get_stock_quarterly_cash_flow`; Insider via SEC EDGAR Form 4
- **FLAG-Resolve-Decision-Logic:** Strict gegen $20M-Schwelle (Score 84→53-Setup vom 30.04. dokumentiert in §12.1). Resolve = `archive_flag.py archive --resolve` + Score-Re-Eval + Sub-Score-Recompute. Stable = keine FLAG-Event-Mutation, nur Score-Update wenn Sub-Scores moved.
- **8-File-§18-Sync** bei Score/FLAG/Sparrate-Bewegung: log.md + CORE-MEMORY + Faktortabelle + PORTFOLIO + score_history.jsonl + config.yaml + Rebalancing_Tool + Satelliten_Monitor (+ flag_events.jsonl bei FLAG-Event + Watchlist falls §6-Drift)
- **xlsx-Post-Write-Smoke-Test** (§18.7) Pflicht via `03_Tools/xlsx-smoke-test.md`

### Parallel-Slot-Warnung — Doppel-Belastung 04.06.
**VEEV reportet ebenfalls am 03.06. amc.** Tag-+1-Slot 04.06. wird **doppelt belegt** (VEEV + AVGO Vollanalysen, beide Klasse B). Empfehlung:
- **AVGO zuerst** (FLAG-Resolve-Gate hat höhere Score-Implikations-Sensitivität als VEEV-Score-Stability)
- VEEV danach am Tag (oder Tag +2 wenn AVGO-Komplexität explodiert)
- Token-Budget realistisch einschätzen — AVGO-Vollanalyse mit FLAG-Logic + Insider-Re-Pull ist ~30–50 % schwerer als VEEV-Standard-Vollanalyse

---

## 8. Synthesis (T-9)

**Setup:** Trillion-Cap-Position nahe 52w-Hoch nach +79 % Rally vom Tief, P/E-Multiple-Re-Rating eingepreist (Forward 22,7 bei +66 % EPS-Wachstum FY26). Beat-Historie 4/4 aber **knapp** (Ø +2,0 %), Analysten-Sentiment quasi-unanim bullish (44/47 positiv), aber **Bear-Target signalisiert −48 % Tail-Risk**.

**Erwartungs-Bar:** $2,39 EPS / $22,08 Mrd Revenue, Hist.-Norm-Beat impliziert nur ~$2,44 EPS. **Wichtigster Watch: FY26-Guidance + Q3-Forward-Range-Width 49 %** (Spread $2,69–$4,26 EPS) = maximale Analysten-Disagreement zur AI-Acceleration-Sustainability.

**FLAG-Dimension dominiert:** $106M-Insider-Selling-FLAG aktiv seit 27.04. Resolve-Pfad (<$20M) niedrig wahrscheinlich ohne harten Katalysator. **Wahrscheinlichster Tag-+1-Output: FLAG-stable, Score 53 stable, kein DEFCON-Move** — Außer Sub-Consensus-Miss + Guide-Cut, was Score → Sub-50-Risk eröffnet.

**Asymmetrie:** Risk/Reward klar nach unten asymmetrisch (Bear-Target −48 %, Bull-Target nur +16 % Mean). Kombiniert mit FLAG-Override-Sparrate 0€ ist AVGO-Position bereits maximal de-risked aus Depot-Sicht — keine Sparraten-Action erwartbar unabhängig vom Outcome.

---

**Brief-Status:** T-9 (Pre-Call-Prep). Erweiterung um AVGO-IR-Tag-0-Press-Release + Insider-Form-4-Pull am 03.06. nach Close.
**Brief-Persistenz:** `02_Analysen/Earnings Reports/Broadcom/AVGO_pre-earnings_2026-06-03.md`
**Verwandte Files:** PORTFOLIO.md Z. 18 + 47 (Q3-FY26-Re-Eval-Description, optional-update später) + Z. 59 (30-Tage-Trigger) · STATE.md Z. 23 · CORE-MEMORY §12.1 (Bestand) · `03_Tools/earnings_calendar.py --check --alert-window 14` Tool-Output 25.05.
**Parallel-Brief:** `02_Analysen/Earnings Reports/Veeva Systems/VEEV_pre-earnings_2026-06-03.md`
