---
name: cross-source-verify
description: >
  Selbst-verifizierender Fundamentaldaten-Skill für das Dynastie-Depot. Liefert
  EINE Finanzkennzahl/abgeleitete Antwort (FCF-Marge, ROIC, Revenue-YoY, P/FCF,
  EPS, Net-Margin, Net-Debt/EBITDA, Shares-out, Dividende, …) für einen Ticker
  UND verifiziert sie im selben Lauf gegen ≥2 unabhängige Quellen + Primärquelle,
  bevor sie ausgegeben wird. Ersetzt den manuellen Cross-Source-Drift-Check, den
  du sonst nach jeder KI-Zahl per Hand machst (Aggregator gegen 2. Quelle, gegen
  SEC/IR-Filing ankern, Währung/Periode/Basis prüfen, Δ bewerten). Fail-close:
  Verdikt VERIFIED nur bei Quellen-Konsens; sonst DISCREPANCY (beide Werte +
  wahrscheinliche Ursache) oder UNVERIFIED (nur 1 Quelle erreichbar). Trigger:
  `!Verify <TICKER> <metric>`, "verifizier die Zahl", "stimmt der FCF/ROIC?",
  "cross-check <metric> für <Ticker>", "gegenprüfen", "welche Quelle hat recht?",
  oder unmittelbar nachdem eine KI-Ausgabe eine zu persistierende Kennzahl nennt.
  KEIN Score-Workflow-Ersatz (dynastie-depot bleibt Owner) — dies ist der
  Daten-Verifikations-Layer, der dort als Vorstufe/Gate eingehängt wird.
---

# cross-source-verify

**Zweck:** Eine Finanzkennzahl generieren **und sie im selben Lauf selbst
gegenprüfen**, sodass der manuelle Multi-Source-Drift-Check entfällt. Output ist
nie nur eine Zahl, sondern Zahl **+ Verifikations-Block + Verdikt**.

Leitlinie (normativ): **Korrektheit > Laufzeit** (`feedback_correctness_over_runtime`).
False-Negative-Risiko schlägt jede Token-Ersparnis. Snapshot-First:
PORTFOLIO.md + Faktortabelle-Wert lesen, BEVOR externe Calls laufen.

---

## Auslösezeitpunkt (Trigger-Beispiele)

| Situation | Beispiel-Eingabe |
|-----------|------------------|
| Explizit, strikt | `!Verify KYCCF fcf_margin` · `!Verify ASML roic` |
| Eine KI-Zahl plausibilisieren | „Stimmt die FCF-Marge von 22 % für 6861.T?" |
| Drift-Verdacht zwischen Quellen | „defeatbeta sagt X, Yahoo sagt Y — welche stimmt?" |
| Vor Persistenz eines Score-Inputs | „Bevor ich das ins Faktortabelle schreibe: gegenprüfen" |
| Cross-Check generisch | „cross-check revenue_yoy für SU" · „gegenprüfen NOW net_margin" |
| Als Gate aus `dynastie-depot` | Schritt-3-Datenblock liefert Rohzahl → dieser Skill verifiziert vor Scoring |

**Kein Trigger:** voller `!Analysiere`-Lauf (das ist `dynastie-depot`; dieser Skill
wird darin als Daten-Gate aufgerufen, konkurriert nicht). Reiner Kursabruf ohne
Verifikationsbedarf.

---

## Ablauf

### Phase 1 — GENERATE (die Antwort)
1. **Snapshot-First:** zuletzt persistierten Wert aus PORTFOLIO.md / Faktortabelle lesen (Referenzanker, Token-frei).
2. **Primärquelle nach Source-Hierarchie:**
   - US-Ticker → `defeatbeta-api` MCP (`get_stock_quarterly_fcf_margin`, `…_roic`, `…_net_margin`, `get_stock_quarterly_revenue_yoy_growth`, …).
   - Non-US (ASML/RMS/SU/KYCCF) → Skill `non-us-fundamentals` (yfinance, Datensymbol z. B. `6861.T`).
3. Kennzahl berechnen/extrahieren. **Basis festhalten:** TTM vs. annual vs. quarterly, diluted vs. basic, Währung (USD/EUR/JPY), Stichtag/Periode.

### Phase 2 — VERIFY (der Verifizierungsschritt — Kern des Skills)
Jeder Schritt ist fail-close; ein nicht-erreichbarer Schritt downgraded das Verdikt, fabriziert nie einen Wert.

1. **Unabhängige 2. Quelle (anderer Code-Pfad):**
   - `mcp__claude_ai_Shibui_Finance__stock_data_query` ODER yfinance-Gegenpfad ODER `Tavily` (Konsens/Analystenwert, IR-Press-Release) ODER FinnHub (`03_Tools/finnhub_*.py`, Real-Time-Quote/Calendar/Estimates/News).
   - **FinnHub-Guardrail:** zählt als unabhängige Bestätigung + Drift-Flag, liefert aber **nie** den kanonischen/persistierten Wert (`_meta.for_scoring=False`, V-Q2-Methodology-Drift-Schutz). Free-Tier-Endpoint-Lücken (`/stock/earnings` leer) → fehlend = downgrade, nicht raten.
2. **Toleranz-Gate (in `ctx_execute`, raw bleibt in Sandbox):**
   - Roh-Absolutwerte: |Δ| ≤ 2 %.
   - Margen/Quoten: |Δ| ≤ 0,5 pp.
   - Δ über Band → Schritt 3 erzwingen (nicht raten).
3. **Primärquellen-Anker (Pflicht für score-treibende Zahlen):**
   - US → `get_stock_sec_filings` / SEC-EDGAR (10-K/10-Q) — Zahl gegen Original-Filing.
   - Non-US → IR-/Geschäftsbericht-PDF via `ctx_fetch_and_index` (JGAAP/IFRS-Primärquelle, wie KYCCF JGAAP).
4. **Konsistenz-Checks:** Währung normalisiert? Periode aligned (Q vs. annual vs. TTM)? Share-Basis (diluted) konsistent? Einheit (k/M/B)?
5. **Recency-Check:** `get_latest_data_update_date` — Aggregator stale? Datenstand < Earnings-Datum → flag.
6. **Drift-vs-persistiert:** Neuwert gegen Snapshot aus Phase 1.1 — unerklärter Sprung = eigenständiger Flag.

### Phase 3 — VERDIKT (Ausgabe)
```
Antwort:    <metric> = <Wert> (<Basis>, <Währung>, <Periode>)
Quelle 1:   <name> = <Wert>   (Stand: <datum>)
Quelle 2:   <name> = <Wert>
Primär:     <SEC/IR-Filing> = <Wert>   [oder: nicht erreichbar]
Δ:          <wert> (Toleranz <band>)
Recency:    <datenstand> vs. Earnings <datum>
Verdikt:    VERIFIED | DISCREPANCY | UNVERIFIED
Konfidenz:  hoch | mittel | niedrig
Hinweis:    <bei DISCREPANCY: beide Werte + wahrscheinliche Ursache>
```
- **VERIFIED:** ≥2 unabhängige Quellen im Toleranzband + Primärquelle bestätigt (oder nicht widersprochen).
- **DISCREPANCY:** Δ über Band → **niemals** eine der Zahlen still wählen; beide ausgeben, Ursache benennen (Basis/Periode/Währung/Stale), Primärquelle entscheidet.
- **UNVERIFIED:** nur 1 Quelle erreichbar → explizit als unbestätigt markieren, **nie** als Score-Input freigeben.

---

## Benötigte Tools

| Tool | Rolle in diesem Skill |
|------|----------------------|
| `mcp__defeatbeta-api__*` (`get_stock_quarterly_*`, `get_stock_sec_filings`, `get_stock_dcf_analysis`, `get_stock_wacc`) | Primärquelle US-Fundamentals + SEC-Filing-Liste |
| `mcp__defeatbeta-api__get_latest_data_update_date` | Recency-/Stale-Check (Phase 2.5) |
| Skill `non-us-fundamentals` (yfinance) | Primär-/Gegenquelle ASML/RMS/SU/KYCCF, EUR/JPY |
| `mcp__claude_ai_Shibui_Finance__stock_data_query` | Unabhängige 2. Quelle (anderer Code-Pfad) |
| `mcp__tavily__tavily_search` / `tavily_extract` | Konsens-/Analystenwert, IR-Press-Release als 3. Anker |
| FinnHub-Scripts `03_Tools/finnhub_*.py` (v0.1, Free-Tier) | Real-Time-Cross-Check (Quote/Calendar/Estimates/News). **Nur Bestätigung/Drift-Flag — nie kanonischer Wert** (`for_scoring=False`); STALLED/#75 + Endpoint-Lücken beachten |
| Skill `insider-intelligence` / `sec-edgar-skill` | SEC-EDGAR-Primärquellen-Anker (US) |
| `ctx_fetch_and_index` + `ctx_search` | IR-/Geschäftsbericht-PDF (Non-US Primärquelle) ohne Kontext-Bloat |
| `ctx_execute` | Δ-/Toleranz-Berechnung, Währungs-Normalisierung — raw bleibt in Sandbox |
| `Read` (PORTFOLIO.md, Faktortabelle.md) | Snapshot-First-Anker + Drift-vs-persistiert |

**Optional/Eskalation:** `WebFetch` (IR-Seite ohne Index-Bedarf), `mcp__claude_ai_Shibui_Finance__export_to_excel` (Audit-Trail), Codex (`codex:rescue`) bei strittigem DISCREPANCY statt `advisor()` — `feedback_review_via_codex_not_advisor`.

---

## Grenzen & Registrierung
- Ersetzt **keinen** Score-/Analyse-Workflow; Owner bleibt `dynastie-depot`, hier nur als Daten-Gate eingehängt.
- DISCREPANCY ohne erreichbare Primärquelle → an User eskalieren, nicht selbst entscheiden.
- **Noch offen vor Live-Nutzung:** Junction in `.claude/skills/` (`mklink /J`), CLAUDE.md-Projektstruktur-Inventar ergänzen, ggf. §18-Sync-Relevanz prüfen.
