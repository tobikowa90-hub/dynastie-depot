# 🔗 Quellen-Referenz – Dynastie-Depot v3.7

**Stand:** 17.04.2026 | **Version:** 3.0 | **Zweck:** Verbindliche Quellenmatrix für alle DEFCON-Analysen

Lies diese Datei bei jeder `!Analysiere`- und `!CAPEX-FCF-ANALYSIS`-Analyse. Die Quellen-Reihenfolge entspricht dem DEFCON v3.7 Workflow.

---

## ⚠️ Architektur-Änderungen v3.0 (gegenüber v2.7)

- **MCP-First:** Shibui Finance SQL (Technicals) + defeatbeta MCP (Fundamentals) sind Primärquelle bei US-Tickern, nicht mehr GuruFocus/Macrotrends.
- **Automatisierte Insider:** `insider_intel.py` (US, SEC EDGAR Form 4) und `eodhd_intel.py` (Non-US, yfinance) ersetzen manuelle OpenInsider/GuruFocus-Checks als Pflicht-Primärquelle.
- **GuruFocus:** bleibt für Moat-Score + term-basierte Fallbacks. Pflicht-Batch unverändert.
- **Entfernt:** Simply Wall St (paywall + unscharf), Stock3 (redundant), Fintel (Paywall), CB Insights (nicht DEFCON-relevant), Morningstar-Eintrag ohne User-Zugang.
- **GuruFocus `/stock/[TICKER]/summary`** bleibt gesperrt (JS-gerendert). Nur `/term/[METRIK]/[TICKER]` verwenden.

---

## 🎯 Primärquellen (MCP / SQL / Scripts — Top-Tier)

### US-Ticker (NYSE/NASDAQ)

| Quelle | Zugriff | Liefert |
| :---- | :---- | :---- |
| **Shibui Finance SQL** | `mcp__claude_ai_Shibui_Finance__stock_data_query` | Technicals (RSI, MACD, MA, Rel. Stärke), Quarterly Cash Flow, Balance Sheet |
| **defeatbeta MCP** | defeatbeta MCP Tools | Fundamentals (ROIC, FCF Yield, P/FCF annual, Revenue-Wachstum), EPS-Historie |
| **insider_intel.py** | `python insider_intel.py [TICKER]` | SEC EDGAR Form 4 — automatisiert, inkl. 10b5-1-FLAG-Auswertung |

### Non-US-Ticker (ASML, RMS, SU)

| Quelle | Zugriff | Liefert |
| :---- | :---- | :---- |
| **eodhd_intel.py** | `python eodhd_intel.py detail [TICKER]` | yfinance-basiert, vollständiger DEFCON-Block (Fundamentals + Technicals + Insider-Proxy) |
| **AFM-Register** | [afm.nl](https://afm.nl) | ASML-Insider (Niederlande) — manuell |
| **AMF-Register** | [amf-france.org](https://amf-france.org) | RMS/SU-Insider (Frankreich) — manuell |
| **IFRS-PDF (10-K/20-F)** | IR-Seite des Unternehmens | Primärquelle bei IFRS-Abweichung gegen yfinance (ROU/Leasing) |

**Hinweis:** Bei Non-US keine Form-4-Pflicht — AFM/AMF als manuelle Fundstelle, keine automatische Auswertung.

---

## 🔬 Web-Sekundärquellen (Fallback/Verifikation)

| Quelle | URL | Wofür |
| :---- | :---- | :---- |
| **GuruFocus** | [gurufocus.com](https://gurufocus.com) | Moat-Score (Primär für Moat-Block!), term-Pages für Verifikation |
| **AlphaSpread** | [alphaspread.com](https://alphaspread.com) | DCF Fair Value, Relative Valuation, Fwd PE/FCF — Non-US mit Börsen-Prefix |
| **StockAnalysis** | [stockanalysis.com](https://stockanalysis.com) | Quarterly Cash Flow als Cross-Check zu Shibui |
| **Macrotrends** | [macrotrends.net](https://macrotrends.net) | 10-Jahres-Historie FCF/CapEx/OCF für Trend-Analyse |
| **Yahoo Finance** | [finance.yahoo.com](https://finance.yahoo.com) | Live-Kurs, USD/EUR-Rate, Earnings Calendar |
| **Finviz** | [finviz.com](https://finviz.com) | Screener, PE/FCF-Übersicht (Fallback wenn Shibui down) |
| **Zacks** | [zacks.com](https://zacks.com) | EPS-Revisionen, Analyst-Ratings |
| **TradingView** | [tradingview.com](https://tradingview.com) | Chart-Analyse (Fallback) |

---

## 🚀 GuruFocus Pflicht-Batch (bei `!Analysiere` Start)

Diese 4 URLs werden **gleichzeitig** abgerufen. Sie decken den Moat-Block plus Fallback-Fundamentals ab, falls defeatbeta lückenhaft ist.

| Metrik | URL-Muster | Liefert |
| :---- | :---- | :---- |
| **Moat Score** | `gurufocus.com/term/moat-score/[TICKER]` | 0–10 Skala + Wide/Narrow/None |
| **P/FCF (TTM)** | `gurufocus.com/term/price-to-free-cash-flow/[TICKER]` | Price-to-FCF TTM |
| **ROIC** | `gurufocus.com/term/roic/[TICKER]` | ROIC % TTM |
| **FCF Yield** | `gurufocus.com/term/fcf-yield/[TICKER]` | FCF Yield % |

**Erweiterter GuruFocus-Batch (bei Bedarf):**

| Metrik | URL-Muster | Liefert |
| :---- | :---- | :---- |
| **Gross Margin** | `gurufocus.com/term/gross-margin/[TICKER]` | GM % TTM |
| **Debt/EBITDA** | `gurufocus.com/term/debt-to-ebitda/[TICKER]` | Net Debt/EBITDA |
| **Revenue CAGR 3Y** | `gurufocus.com/term/revenue-growth-3y/[TICKER]` | Umsatzwachstum 3J |
| **Insider (Fallback)** | `gurufocus.com/insiders/[TICKER]` | Buy/Sell-Saldo, nur wenn insider_intel.py down |

---

## 🦅 Insider & Institutional

| Quelle | Zugriff | Wofür | Priorität |
| :---- | :---- | :---- | :---- |
| **insider_intel.py** | `python insider_intel.py [TICKER]` | US-Form-4 automatisiert inkl. 10b5-1-FLAG | ✅ Primär (US) |
| **eodhd_intel.py** | `python eodhd_intel.py detail [TICKER]` | Non-US Insider-Proxy (Institutional Holders) | ✅ Primär (Non-US) |
| **AFM / AMF** | Register-Seiten | Non-US Form-4-Äquivalent, manuell | ✅ Primär (Non-US) |
| **SEC EDGAR Form 4** | sec.gov/cgi-bin/browse-edgar | Rohdaten für forensische Verifikation | Sekundär |
| **OpenInsider** | [openinsider.com](https://openinsider.com)/[TICKER] | Triage-Check bei Unklarheit (Spalte X) | Sekundär |
| **GuruFocus Insider** | gurufocus.com/insiders/[TICKER] | Ownership %, Buy/Sell 90 Tage | Sekundär |

### 🚨 10b5-1 FLAG-Prüflogik

Pflicht bei jedem Insider-Verkauf >$20M in den letzten 90 Tagen. `insider_intel.py` prüft automatisch; bei Web-Check:

| Spalte "X" / "M" | Bedeutung | FLAG? |
| :---- | :---- | :---- |
| **M** angezeigt | ✅ 10b5-1-Plan vorhanden (automatischer Plan-Verkauf) | 🟢 Kein FLAG |
| **Leer** | 🔴 Diskretionärer Verkauf ohne Plan | 🚨 FLAG aktiv |

**Regel:** Verkauf >$20M + kein "M" + innerhalb 90-Tage-Fenster = **FLAG aktiv**, Sparrate einfrieren, unabhängig vom Score.

### 🔍 Form 4 Transaktions-Code Cheatsheet (SEC EDGAR)

Die 10b5-1-Prüfung gilt **ausschließlich bei echten Verkäufen**. Zuerst Code prüfen, dann 10b5-1-Box auswerten:

| Code | Bedeutung | 10b5-1 prüfen? | FLAG möglich? |
| ----- | ----- | ----- | ----- |
| **S** | Open-Market-Verkauf | ✅ Ja — Box prüfen | 🚨 Ja |
| **D** | Disposal (sonstige Übertragung) | ✅ Ja — Box prüfen | 🚨 Ja |
| **M** + **S** gleicher Tag + Option nahe Expiry | Cashless Exercise (erzwungen) | ❌ Nein | 🟢 Kein FLAG |
| **M** + Preis $0.00 | RSU-Vesting | ❌ Nein | 🟢 Kein FLAG |
| **A** | Acquisition (Grant, RSU, Zuteilung) | ❌ Nein | 🟢 Kein FLAG |
| **M** allein (Option Exercise, kein S) | Option ausgeübt, Aktien behalten | ❌ Nein | 🟢 Kein FLAG |

**Cashless Exercise erkennen:** Code M + Code S am gleichen Tag + Options-Expiry ≤ 30 Tage = erzwungener Verkauf, kein Timing-Signal. Transaktionsvolumen trotzdem prüfen — bei >$20M und kein 10b5-1-Plan → FLAG.

### 🔍 OpenInsider Spalten-Cheatsheet (Triage-Fallback)

| Spalte | Inhalt | Relevanz |
| ----- | ----- | ----- |
| **X** | 10b5-1-Plan vorhanden | ✅ Kernprüfung — leer = FLAG-Kandidat |
| **Trade Type** | P = Purchase, S = Sale, S-Auto = 10b5-1-Sale | S ohne X = 🚨 |
| **Value** | Transaktionswert in USD | >$20M = FLAG-Schwelle |
| **#Shares** | Anzahl gehandelter Aktien | Kontext |
| **Own** | Ownership nach Trade (D/I) | D = Direct = stärker gewichtet |

**Automatische Entlastung (kein FLAG trotz leerem X):**
- Trade Type **"S-Auto"** = automatischer 10b5-1-Verkauf → 🟢 Kein FLAG
- Trade Type **"Option Ex."** + gleicher Tag S = Cashless Exercise → 🟢 Kein FLAG
- Value **< $20M** = unter FLAG-Schwelle → ⚠️ Negatives Signal, kein FLAG

---

## 🏰 Moat & Qualität

| Quelle | Zugriff | Wofür | Priorität |
| :---- | :---- | :---- | :---- |
| **GuruFocus Moat** | `gurufocus.com/term/moat-score/[TICKER]` | Moat Score 0–10 + Wide/Narrow/None | ✅ Primär |
| **defeatbeta MCP** | MCP | Gross Margin-Stabilität, ROIC-Persistenz als Moat-Proxy | Sekundär |
| **Morningstar** | [morningstar.com](https://morningstar.com) | Wide/Narrow/None (Paywall) | Nur bei User-Zugang |

---

## 📋 Primärquellen (Pflicht für CapEx-FCF)

| Quelle | URL | Wofür |
| :---- | :---- | :---- |
| **SEC EDGAR** | sec.gov/cgi-bin/browse-edgar | 10-K, 10-Q direkt (US-Pflicht) |
| **IFRS-PDF (20-F / Annual)** | IR-Seite | ASML/RMS/SU — ROU-Leasing-Korrektur |
| **Investor Relations** | `[TICKER] investor relations` (Google) | Press Releases, Earnings PDFs |
| **Yahoo Finance FX** | finance.yahoo.com/quote/USDEUR=X | Aktuelle USD/EUR-Rate |
| **EZB Referenzkurs** | ecb.europa.eu | Offizieller Referenzkurs (Audit) |

---

## ⚡ Quick-Lookup nach Analyse-Schritt

Primär zuerst abfragen. Sekundär nur bei fehlenden/widersprüchlichen Daten.

| **Schritt** | **Primär** | **Sekundär** |
| :---- | :---- | :---- |
| **Live-Kurs + Marktdaten** | Shibui `stock_data_query` (Technicals) | Yahoo Finance |
| **Fwd PE / DCF** | AlphaSpread | Yahoo /analysis |
| **P/FCF (TTM)** | defeatbeta `annual_cash_flow` | GuruFocus term/price-to-free-cash-flow |
| **ROIC** | defeatbeta `quarterly_roic` | GuruFocus term/roic |
| **FCF Yield** | defeatbeta `annual_cash_flow` / Marktcap | GuruFocus term/fcf-yield |
| **Bilanz (Debt/EBITDA)** | defeatbeta `balance_sheet` | GuruFocus term/debt-to-ebitda |
| **Gross Margin** | defeatbeta `income_statement` | GuruFocus term/gross-margin |
| **Moat-Check** | GuruFocus term/moat-score | defeatbeta (Margin-/ROIC-Persistenz) |
| **Insider-Check (FLAG)** | `insider_intel.py` (US) / `eodhd_intel.py` + AFM/AMF (Non-US) | OpenInsider / SEC EDGAR Form 4 |
| **Analyst-Konsensus + PTs** | Zacks | Yahoo Finance analysis |
| **CapEx / OCF quarterly** | Shibui `cash_flow_quarterly` | StockAnalysis cash-flow-statement |
| **CapEx / OCF 5J-Historie** | defeatbeta `annual_cash_flow` | Macrotrends |
| **10-K Primärquelle** | SEC EDGAR | IR-Website direkt |
| **USD/EUR Umrechnung** | Yahoo Finance (Echtzeit) | EZB (offiziell) |
| **SBC/Revenue** | defeatbeta `annual_cash_flow` (SBC-Zeile) | GuruFocus term/sbc-to-revenue |
| **Accruals Ratio** | defeatbeta (NI-OCF/Assets berechnet) | StockAnalysis balance+cash-flow |
| **GM-Trend 3J** | defeatbeta `income_statement` (5J) | Macrotrends gross-profit-margin |
| **Pricing Power** | Quartr TICKER (Transcript) | IR-Website Earnings Call |
| **Rel. Stärke 6M** | Shibui `technical_indicators` | Finviz quote.ashx |
| **EPS Revisionen** | Zacks TICKER → Consensus EPS Revisions | Yahoo Finance analysis |
| **Tariff Exposure** | SEC EDGAR 10-K → "Geographic Revenue" | Quartr (Management Commentary) |

---

## ⚠️ Scoring-Protokoll: Kritische Datenanpassungen

#### 1. TTM-Verzerrung bei Kurscrash (>30% vom ATH)

* **Problem:** Wenn der Kurs >30% unter dem All-Time High (ATH) liegt, sind TTM-Multiples (PFCF, FCF Yield, PE) künstlich billig und verzerren den Score nach oben.
* **Regel:** **Forward-Metriken** (Fwd PE, Fwd P/FCF) sind die primäre Scoring-Basis.
* **TTM-Werte:** Nur als Kontextreferenz dokumentieren, nicht zur Score-Berechnung verwenden.
* **Quelle Forward-PFCF:** AlphaSpread (P/FCFE Forward) → GuruFocus (Fwd-Sektion).

#### 2. GAAP vs. Non-GAAP Protokoll

* **Standard:** **GAAP-Metriken** für alle Score-Berechnungen (konservativ).
* **Non-GAAP:** Nur als Kontextinformation in Klammern dokumentieren.
* **Ausnahme:** Wenn die Non-GAAP-Differenz *ausschließlich* aus Amortisierung von Akquisitions-Goodwill besteht (z.B. AVGO nach VMware), kann Non-GAAP als Hauptmetrik mit explizitem Vermerk verwendet werden.
* **Begründung:** Stock-Based Compensation (SBC) ist ein realer Kostenfaktor und darf *niemals* herausgerechnet werden. Amortisierung ist buchhalterisch, kein Cash-Abfluss.

#### 3. Non-US Ticker Quellenregel

* **US-Ticker (NYSE/NASDAQ):**
  * **Primär:** Shibui Finance SQL (Technicals) + defeatbeta MCP (Fundamentals)
  * **Insider:** insider_intel.py (SEC EDGAR Form 4 — automatisiert)
  * **Fallback:** GuruFocus/Macrotrends
* **Non-US-Ticker (ASML, RMS, SU):**
  * **Primär:** `eodhd_intel.py` (yfinance, EUR-Ticker) — vollständiger DEFCON-Block automatisiert
  * **Befehl:** `python eodhd_intel.py detail [TICKER]`
  * **Insider:** AFM (ASML) / AMF (RMS, SU) — manuell, keine Form-4-Pflicht
  * **Verifikation Valuation:** AlphaSpread `/par/[TICKER]` (Paris) oder `/ams/[TICKER]` (Amsterdam)
  * **Verifikation ROIC:** GuruFocus `term/roic/[TICKER]` (yfinance liefert nur Proxy)
  * **IFRS-Abweichung:** Bei CapEx/OCF-Diff >15% zwischen yfinance und IFRS-PDF → IFRS-Werte als Master (ROU-Leasing rausrechnen).
* **Hinweis AlphaSpread:** Börsen-Prefix beachten: `/par` (Paris), `/ams` (Amsterdam), `/xet` (Xetra), `/nasdaq`, `/nyse`.

#### 4. Insider Ownership Bewertungsskala

| Direct Ownership | Punkte | Bewertung |
| ----- | ----- | ----- |
| **>5%** | 3/3 | CEO/Gründer-Alignment |
| **1% – 5%** | 2/3 | Signifikant |
| **0.1% – 1%** | 1/3 | Minimal |
| **<0.1%** | 0/3 | Faktisch kein Skin in the Game |

* **Zählweise:** Nur **Direct (D)** Ownership zählt. Indirect (I) gibt max. 1/3 Punkt.

#### 5. Fwd PE Quellen-Hierarchie bei Widerspruch

1. **AlphaSpread** (Relative Valuation Tab) — **Primär**
2. **Yahoo Finance** (/analysis: Consensus EPS × aktueller Kurs) — **Sekundär**
3. **Finviz** (Forward PE Zeile) — **Tertiär**
* **Abweichung:** Bei >15% Abweichung den konservativsten Wert verwenden + Abweichung dokumentieren.

#### 6. Quarterly vs. Annual Daten

| Metrik / Zweck | Frequenz / Zeitraum | Quelle |
| ----- | ----- | ----- |
| **CapEx/OCF** für CapEx-FLAG-Prüfung | Quarterly (letzte 4Q annualisiert) | Shibui `cash_flow_quarterly` |
| **CapEx/OCF** für historischen Trend | Annual (5–10 Jahre) | defeatbeta / Macrotrends |
| **FCF** für DEFCON-Score | TTM Annual | defeatbeta / GuruFocus |
| **FCF** für Forward-Bewertung | Nächstes volles Fiskaljahr | AlphaSpread / Konsensus |

---

## 🔑 Goldene Regel (gilt immer, überall)

Bei widersprüchlichen Daten zwischen Quellen: **konservativsten Wert verwenden** und Abweichung explizit in der Analyse dokumentieren.

**Hierarchie:** SEC EDGAR / IFRS-PDF > Shibui + defeatbeta MCP > GuruFocus term > AlphaSpread > Web-Drittanbieter.

---

## 🔍 URL-Muster für Ticker-spezifische Abfragen

Ersetze `[TICKER]` durch das jeweilige Kürzel (z.B. COST, AVGO, MSFT).

**GuruFocus Term-Seiten (fetchbar, kein Login)**

| Bezeichnung | Link-Vorlage |
| :---: | :---: |
| Moat | `https://www.gurufocus.com/term/moat-score/[TICKER]` |
| P/FCF | `https://www.gurufocus.com/term/price-to-free-cash-flow/[TICKER]` |
| ROIC | `https://www.gurufocus.com/term/roic/[TICKER]` |
| FCF Yield | `https://www.gurufocus.com/term/fcf-yield/[TICKER]` |
| Gross Margin (GM) | `https://www.gurufocus.com/term/gross-margin/[TICKER]` |
| Debt to EBITDA | `https://www.gurufocus.com/term/debt-to-ebitda/[TICKER]` |
| Revenue Growth 3Y (CAGR) | `https://www.gurufocus.com/term/revenue-growth-3y/[TICKER]` |
| Insider Trades | `https://www.gurufocus.com/insiders/[TICKER]` |

**❌ NICHT verwenden (JS-gerendert, nicht fetchbar):** `https://www.gurufocus.com/stock/[TICKER]/summary`

**AlphaSpread (Börsen-Prefix beachten)**

| Bezeichnung | Link-Vorlage |
| ----- | :---: |
| US NASDAQ | `https://alphaspread.com/security/nasdaq/[TICKER]` |
| US NYSE | `https://alphaspread.com/security/nyse/[TICKER]` |
| EU Paris (z.B. SU, RMS) | `https://alphaspread.com/security/par/[TICKER]` |
| EU Amsterdam (ASML) | `https://alphaspread.com/security/ams/[TICKER]` |
| EU Xetra | `https://alphaspread.com/security/xet/[TICKER]` |

**Weitere Quellen**

| Bezeichnung | Link-Vorlage |
| ----- | ----- |
| StockAnalysis (Cash Flow Quarterly) | `https://stockanalysis.com/stocks/[ticker]/financials/cash-flow-statement/?p=quarterly` |
| StockAnalysis (Statistics) | `https://stockanalysis.com/stocks/[ticker]/statistics/` |
| Macrotrends (Charts) | `https://macrotrends.net/stocks/charts/[TICKER]/` |
| Yahoo Finance (Quote) | `https://finance.yahoo.com/quote/[TICKER]/` |
| Yahoo Analysis | `https://finance.yahoo.com/quote/[TICKER]/analysis` |
| Finviz | `https://finviz.com/quote.ashx?t=[TICKER]` |
| SEC EDGAR (10-K) | `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-K` |
| OpenInsider | `https://openinsider.com/[TICKER]` |

---

*🦅 Bei widersprüchlichen Daten zwischen Quellen: konservativsten Wert verwenden und Abweichung dokumentieren.*
*Version 3.0 – 17.04.2026 | MCP-first: Shibui + defeatbeta als Primärquelle. Scripts insider_intel.py (US) / eodhd_intel.py (Non-US) als automatisierte Insider-Primärquelle. GuruFocus Moat + term als Fallback/Moat. OpenInsider + SEC EDGAR Form 4 = Triage/Forensik.*
