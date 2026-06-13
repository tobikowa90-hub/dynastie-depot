# Gate-0 Coverage-Matrix — cross-source-verify

**Stand:** 2026-06-13 | **Zweck:** Empirisch belegte Quellen-Coverage VOR Spec (Scope-Contract-Gate, `feedback_skill_name_is_scope_contract`).
**Methode:** Live-Probe je Quelle × Ticker-Klasse. Jede Zeile „verified via:"-annotiert (`feedback_empirie_statt_annahmen`).

## Quellen-Probe (empirisch, 2026-06-13)

| Quelle | US-Listed (inkl. US-ADR) | Non-US EUR (kein US-Listing) | JP-OTC | verified via |
|--------|--------------------------|------------------------------|--------|--------------|
| **defeatbeta MCP** | ✅ direkt: fcf/net_margin, ROIC (dekomponiert, **quartals-basiert**), revenue_yoy, EPS, Bilanz, ttm_pe, DCF, WACC | ⚠️ **nur via US-ADR-Symbol** (`ASML`✅) — `ASML.AS`/`.PA`=leer | ❌ `6861.T` → `{}` | `get_stock_profile('6861.T'/'ASML.AS')={}` vs `('ASML')=full`; `roic('NOW')`=11Q |
| **Shibui MCP** | ✅ US-only; claimt margins/valuation/cashflow/dividends (SQL) — **Tiefe SPEC-CONFIRM-PENDING** | ❌ US-only | ❌ | Schema-Desc „US-exchange-listed"; Spalten-Tiefe noch nicht SQL-geprüft |
| **yfinance** (non-us-fundamentals) | ✅ (nicht primär) | ✅ **Primär** (ASML.AS/RMS.PA/SU.PA); ROIC=**Proxy**; RMS CapEx **IFRS-buggy** | ✅ `6861.T` (JPY) | SKILL v1.2 + 6861.T-Verifikation 2026-06-13 |
| **Finnhub** (v0.1, STALLED #75) | ✅ US-only: quote/estimates/news/profile2 + 11 metrics, `for_scoring=False` | ❌ **403 Premium** | ❌ | `finnhub_health.json` (EU rms/su=403) |
| **Tavily** | ✅ AlphaSpread/simplywall/GuruFocus | ✅ (web) | ✅ (web) | Live-Probe „Keyence FCF margin" → AlphaSpread 34,4 % |
| **SEC EDGAR / IR-Primär** | ✅ 10-K/10-Q | ✅ IR/Annual-Report (IFRS) | ✅ IR/Annual (JGAAP) | KYCCF-O3 JGAAP-Anchor 2026-06-13 |
| **EODHD Free (eigener Key)** | ❌ Fund=403; EOD=200 **aber ~1J stale**; RT=200 | ❌ Fund=403; EOD=200 ~1J stale | ❌ Fund=403; EOD=404 (JP nicht abgedeckt) | Live-Probe Key 2026-06-13: fundamentals/{6861.T,RMS.PA,AAPL.US}=403; eod/AAPL.US,RMS.PA last=2025-06-13; eod/6861.TSE=404 |

**EODHD-Verdikt: REJECT.** Free-Tier liefert keine Fundamentals (403 überall) → schließt die Tier-2-Lücke nicht. EOD-Price ~1 Jahr veraltet → als Valuations-Denominator unbrauchbar; JP gar nicht abgedeckt. Einziger Mehrwert = US-Real-Time-Quote, redundant zu Finnhub. Deckt sich mit `non-us-fundamentals`-Doku „warum nicht EODHD", jetzt mit eigenem Key frisch belegt (+ neuer Fund: 1-J-EOD-Lag).

| **Alpha Vantage Free (eigener Key)** | ✅ OVERVIEW US voll (55 Felder, USD) | ❌ RMS.PAR=leer | ❌ 6861/Tokio nicht indexiert; KYCCF(OTC)=leer | Live-Probe Key 2026-06-13: OVERVIEW AAPL OK; RMS.PAR/KYCCF={}; SYMBOL_SEARCH Keyence → nur KEE.FRK(Frankfurt)+KYCCF(OTC), kein 6861.T; Rate-Limit 25/Tag + ~5/min-Burst |

**Alpha-Vantage-Verdikt: REJECT für Tier-2; OPTIONAL als tertiäre US-Quelle.** Nur US-Fundamentals — auf Primärbörsen Paris/Tokio nichts; dupliziert defeatbeta/Shibui/Finnhub. 1 OVERVIEW-Call = viele US-Metriken (token-effizient), aber 25/Tag-Limit untauglich für Routine. **Strukturfazit:** EODHD UND Alpha Vantage scheitern beide an Non-US-Fundamentals → Tier-2-Lücke ist strukturell für Free-Tier, nicht wegspezifizierbar; gestufter Scope bestätigt.

## Scope-Tiers (folgt aus der Probe — MUSS literal in SKILL.md `description`)

- **Tier-1 „Structured-Dual"** = US-Ticker + US-ADR-Non-US (**ASML**): ≥2 unabhängige strukturierte Quellen (defeatbeta + Shibui/yfinance) → echtes VERIFIED möglich.
- **Tier-2 „Web+Primary"** = **RMS / SU / KYCCF** (kein US-Listing): **keine** 2. strukturierte API. Verifikation = yfinance-Primär + Tavily/AlphaSpread-Korroboration + IR-Primär-Anchor. **Nie** als „Structured-Dual" labeln; eigenes, niedrigeres Konfidenz-Tier. JGAAP/IFRS-Basis.
- **FX/ADR-Caveat:** ASML defeatbeta(USD-ADR) vs yfinance(EUR) → **Währungs-Normalisierung Pflicht** vor Δ.

## Metrik-Querschnitt-Gaps (in Verify-Logik abfangen)

- **ROIC:** defeatbeta=quartalsbasiert, yfinance=TTM-Proxy, AlphaSpread=eigene Basis → **Basis-Normalisierung Pflicht**, sonst False-DISCREPANCY. Non-US = nur Proxy, kein authoritatives 2. Struktur-Signal. **Banken (BRK.B): ROIC N/A** (defeatbeta-Warnung).
- **Derived Ratios** (P/FCF, EV/EBITDA, Net-Debt/EBITDA, FCF-Yield): kein Single-Field → aus Komponenten **rekomputieren**; Cross-Check = Komponenten-Ebene, größere Fehlerfläche.
- **Dividend-per-Share:** defeatbeta kein direkter Endpoint (CONFIRM); yfinance ja.
- **RMS CapEx/FCF:** Primärquelle selbst unzuverlässig (yfinance FCF==OCF) → P/FCF & FCF-Marge für RMS schon an der Quelle Low-Confidence.

## Self-Consistency-Gate (yfinance, gratis — neuer Tier)

yfinance = Wrapper um **ein** Backend (Yahoo) → kein unabhängiger Cross-Check, ABER interner Konsistenz-Gate gratis: Kennzahl aus Rohzeilen (`.cashflow`/`.financials`/`.balance_sheet`) selbst rechnen vs. Yahoos vorberechnete `.info`-Ratio. Fängt Extraktions-/Rechenfehler, NICHT Yahoo-Quellfehler.

**Empirie RMS.PA GJ2025 (2026-06-13, yfinance 1.3.0):**
- recompute FCF = OCF(5,374Mrd)+CapEx(−1,161Mrd) = **4,213Mrd** == cashflow-FCF-Zeile 4,213Mrd → Gate **PASS**.
- **Doku-Stale-Catch:** „FCF==OCF"-Bug (SKILL.md non-us-fundamentals) für GJ2025 **nicht** vorhanden → Skill muss Self-Consistency live testen, Bug nicht hardcoden (`feedback_plan_on_runtime_not_doc_assumption`). Ältere Jahrgänge in Spec spot-checken.
- **Basis-Trap belegt:** annual-FCF-Marge 26,3 % vs `.info`-TTM 25,2 % = 1,1pp = **Basis-Differenz (GJ vs TTM), kein Fehler**. Naiver Cross-Check → False-DISCREPANCY. → Basis-Normalisierung Pflicht (verify-Phase 2.2).

→ Verdikt-Tiers final: **VERIFIED** (≥2 unabh. strukturierte Quellen, Tier-1) · **CORROBORATED** (Self-Consistency-PASS + Web/IR-Primär, Tier-2) · **DISCREPANCY** · **UNVERIFIED**.

## Confidence nach Gate-0

| Achse | vor Gate-0 | nach Gate-0 | Rest-Gap |
|-------|-----------|-------------|----------|
| Quellen-Coverage | ~40 % | **~85 %** (feasible, aber **gestuft** nötig) | Shibui-Tiefe + Dividend/Derived-Komponenten |
| Design-Logik | ~70 % | ~70 % | grill-with-docs (Toleranz, Basis-Norm, Tier-Verdikt-Statemachine) |
| API-Korrektheit | ungeprüft | defeatbeta/Finnhub/yfinance ✅ | context7 (Funktions-Surface final) |

**→ Noch <95 % bis:** (1) Shibui-Fundamental-Tiefe SQL-bestätigt, (2) grill-with-docs lockt Toleranz/Basis-Norm/Tier-Verdikt, (3) context7-Validation. Dann Spec(frozen) → Codex-Sparring (Coverage-Matrix-Completeness = HIGH-Gate).
