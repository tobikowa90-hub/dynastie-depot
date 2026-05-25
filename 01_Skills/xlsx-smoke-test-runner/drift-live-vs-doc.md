# Drift-Tabelle: Live-State vs `03_Tools/xlsx-smoke-test.md`

**Zweck**: Empirische Pre-Spec-Verifikation pro α+ Adaption — jede Drift-Behauptung mit `verified via:`-Annotation gegen real-laufende xlsx-Dateien.

**Probe-Timestamp**: 2026-05-25T17:31:25 (post user-update aller 3 xlsx-Files am 25.05.2026)
**Probe-Tool**: `mcp__plugin_context-mode_context-mode__ctx_execute` + `openpyxl.load_workbook(path, data_only=False)`
**Live-State-Hash-Anker**: REBAL mtime=17:12:51, SAT mtime=16:44:58, WATCH mtime=17:07:28

---

## 0a. Skill-Scope-Statement (Pre-Spec, Codex-R2-F5)

Per `feedback_skill_name_is_scope_contract`-Lesson und α+ Adaption: literale Capability-Grenze des kommenden `xlsx-smoke-test-runner` Skills (NICHT aspirational).

**In-Scope (Skill automatisiert)**:
- **§A** Open-Repair (Workbook-Load + Sheet-Existenz aller Profile-Sheets)
- **§B** Error-Token-Scan (`#REF!`/`#NAME?`/`#VALUE!`/`#N/A` in allen Sheets)
- **§E** CF-Rule-Count-Drift-Check pro Profil
- **§G** (NEU per P8-Variante-G) Sparrate-Σ-Sanity: config.yaml-Mapping → Σ-Check gegen Anker (285€) + xlsx-Display-Konsistenz (K3/B3/B26/N19-Text)
- Pflicht-Cell-Existenz-Checks (Adressen aus xlsx-smoke-test.md §C/§D)

**Out-of-Scope (manuell bzw. UI-only)**:
- **§C/§D** Pflicht-Cell-Inhalt-Semantik (z.B. ob `'DEFCON 3 (74)'` semantisch korrekt für VEEV ist — gehört zu §18-Sync, nicht Smoke-Test)
- **§F** Read-only-Close (interaktiv, kein git-gate)
- Cell-Number-Format, CF-Rules-Identität, Defined Names, Pivots, Workbook-Protection, Print-Settings (siehe §5)

**Verbindlichkeit**: Diese Liste ist Capability-Vertrag. SKILL.md `description` muss literal diese Punkte nennen — keine Erweiterung ohne Pre-Spec-Update.

---

## 0. Gesund-Befunde (alle 3 Files)

| File | Open §A | openpyxl-Warnings | #REF/#NAME/#VALUE/#N/A Hits |
|------|---------|-------------------|------------------------------|
| Rebalancing_Tool_v3.4 | ✓ PASS | 0 | 0 |
| Satelliten_Monitor_v2.0 | ✓ PASS | 0 | 0 |
| Watchlist_Ersatzbank_Monitor_v1.1 | ✓ PASS | 0 | 0 |

**Bedeutung**: Alle 3 Files sind strukturell intakt. Drift ist ausschließlich **Doku ↔ Live** (xlsx-smoke-test.md spec ↔ tatsächliche xlsx-Inhalte), nicht Live ↔ Soll.

---

## 1. Rebalancing_Tool_v3.4.xlsx — HAUPTACHSE

### 1.1 Struktur-Drift

| Punkt | Doku xlsx-smoke-test.md | Live-State (Probe 17:31) | Drift | Severity | verified via |
|-------|-------------------------|--------------------------|-------|----------|--------------|
| Total Formeln | 218 (Scope-Tabelle Z17) | **249** (Portfolio 151 + US-Exposure 93 + Parameter 5) | +31 | LOW | `sum(1 for c in row if c.value.startswith('='))` 2026-05-25T17:31 |
| CF-Rules total | 6 (Scope-Tabelle Z17) | 6 (Portfolio 5 + US-Exposure 0 + Parameter 1) | ✓ match | — | `len(ws.conditional_formatting._cf_rules)` 2026-05-25T17:31 |
| Sheet-Liste | nicht spezifiziert | 3 Sheets: `Portfolio & Rebalancing`, `US-Exposure`, `Parameter & Regeln` | Doku-Gap | LOW | `wb.sheetnames` 2026-05-25T17:31 |
| Sheet-Dims | nicht spezifiziert | Portfolio A1:**Q28** (vorher P27 — Spalte Q + Row 28 neu), US-Exposure A1:E27, Parameter A1:C32 | Doku-Gap | LOW | `ws.dimensions` 2026-05-25T17:31 |
| Header-Row | nicht spezifiziert | **R4** (Position, Ticker, Typ, Broker, US-Faktor, Depotwert, Ist%, Ziel%, Zielwert, Fehlbetrag, Abw%, Aktion, Cap-Check, DEFCON, FLAG, Sparrate) | Doku-Gap | MEDIUM | `ws.cell(4, c).value` for c in 1..16 2026-05-25T17:31 |
| Ticker-Daten-Range | **R18-R28** (Soll §C) | **R5-R21** (max 17 Slots per Formel `C5:C21`, davon R5-R9 = 5 ETFs/Gold, R10-R21 = 12 Aktien) | **KRITISCH** | HIGH | `ws.cell(r, *).value` Vollscan + `'Parameter & Regeln'!B13 = COUNTIF('Portfolio & Rebalancing'!C5:C21,"Aktie")` 2026-05-25T17:31 |

### 1.2 Pflicht-Zellen §C Drift

| Doku-Spec | Live-Befund (Probe 17:31) | Drift | verified via |
|-----------|---------------------------|-------|--------------|
| `R2 = 'Stand: YYYY-MM-DD'` (String mit Prefix) | **`R2 = None`**, stattdessen **`A2 = datetime(2026-05-25 00:00:00)`** (Python datetime-Objekt, ohne `Stand:`-Prefix; user-fix 25.05.) | **KRITISCH** — Cell-Adresse R2→A2 + Format String→datetime | `ws["R2"].value` (None) + `ws["A2"].value` (datetime) + Volltext-Suche `"stand"` 2026-05-25T17:31 (0 Treffer in allen 3 Sheets) |
| `N18-N28 = 'DEFCON X (NN)'` per Ticker | Spalte N enthält `'DEFCON X (NN)'`-Strings im Bereich **N10-N21** (12 Aktien — ASML/AVGO/MSFT/COST/RMS/VEEV/SU/BRK.B/V/TMO/APH/AMZN); N22 = COUNTIF-Aggregat; N23 = Label `'⚠️ DEFCON ≤ 3'` | Spalte ✓ / Range R18-R28→R10-R21 HIGH | `ws.cell(r, 14).value` r=10..23 2026-05-25T17:31 (z.B. `N10='DEFCON 3 (68)'` ASML, `N21='DEFCON 1 (42)'` AMZN) |
| `O18-O28 = FLAG-Status-Text` | Spalte O enthält FLAG-Strings im Bereich **O10-O21**; O22 = COUNTIF-Aggregat; O23 = Label `'🚩 Aktive FLAGs'` | Spalte ✓ / Range R18-R28→R10-R21 HIGH | `ws.cell(r, 15).value` r=10..23 2026-05-25T17:31 (z.B. `O11='🔴 FLAG: Insider-Selling 90d $106M+...'`, `O21='🔴 FLAG: CapEx/OCF TTM 99,2%'`) |
| `P18-P28 = Sparrate-Output Formel` | Spalte P enthält Sparrate-Formeln im Bereich **P5-P21** (Pattern `=IF(C5="Aktie",'Parameter & Regeln'!$B$4*...)`); P22 = `=SUMIF(C5:C21,"Aktie",P5:P21)+SUMIF(C5:C21,"<>Aktie",P5:P21)`; P23 = Label `'Check: Sparrate gesamt'` | Spalte ✓ / Range R18-R28→R5-R21 HIGH + Footer-Sum-Pattern (Doku-Gap) | `ws.cell(r, 16).value` r=5..23 2026-05-25T17:31 |

### 1.3 Footer-Aggregate-Layer (Doku-Gap)

| Live-Zelle | Inhalt | Funktion | verified via |
|------------|--------|----------|--------------|
| R22 A | `'📊 GESAMT'` | Footer-Row-Label | live-read 2026-05-25T17:31 |
| R22 F-K | `=SUM(F5:F21)`, `=SUM(G5:G21)`, `=SUM(H5:H21)`, `=SUM(I5:I21)`, `=ROUND(SUM(J5:J21),2)`, `=SUMPRODUCT((C5:C21="Aktie")*ABS(K5...)` | Spalten-Summen + Drift-Aggregate | live-read 2026-05-25T17:31 |
| R22 L | `'Ø Drift Aktien'` | Label | live-read |
| R22 M | `=COUNTIF(M5:M21,"🚨 ÜBER CAP")` | Cap-Violations-Count | live-read |
| R22 N | `=COUNTIF(N5:N21,"DEFCON 1*")+COUNTIF(N5:N21,"DEFCON 2*")+COUNTIF(N5:N21,"DEFCON 3*")` | Count DEFCON ≤ 3 | live-read |
| R22 O | `=COUNTIF(O5:O21,"🚩*")+COUNTIF(O5:O21,"🔴*")` | Count aktive FLAGs | live-read |
| R22 P | `=SUMIF(C5:C21,"Aktie",P5:P21)+SUMIF(C5:C21,"<>Aktie",P5:P21)` | Σ-Check Sparrate total | live-read |
| R23 K-P | Labels: `'Ø ETF/Gold-Drift'`, `'⚠️ DEFCON ≤ 3'`, `'🚩 Aktive FLAGs'`, `'Check: Sparrate gesamt'` | UI-Beschriftung | live-read |
| R24 A/F | `'Scalable Cash (verfügbar)'` / `1297.78` | Cash-Position | live-read |
| R25 A/F | `'📝 Neuinvestition (manuell ei...)'` / `950` | Sparrate-Input | live-read |
| R26 A/F | `'Gesamtwert nach Invest'` / `=F22 + F25` | Berechnung | live-read |
| R27 A/F | `'💸 ING-Überweisung (Sparplan)'` / `=SUMIFS(P5:P21,D5:D21,"ING")` | Broker-Split | live-read |

**Implikation**: Doku §C kennt KEINE Footer-Aggregate-Verifikation für Rebal. Σ-Check Sparrate (P22) existiert als echte Excel-Formel — anders als Satelliten §D wo der Σ-Check nur Text ist (siehe §2.2 unten).

### 1.4 Cross-Sheet-Referenzen

| Doku-Referenz | Live-Status | verified via |
|---------------|-------------|--------------|
| `P-Formel referenziert 'Parameter & Regeln'!$B$4` | `B4 = 950` (Sparrate monatlich €) | `Parameter & Regeln` Sheet read 2026-05-25T17:31 |
| `P-Formel cross-check gegen config.yaml sparrate_eur` | config.yaml `sparrate_eur: 950` (Observer L25 2026-05-25 12:49) — **match** | Observer L25 + Live B4 reconciliation |
| Allokations-Konsistenz (Soll: ETF+Sat+Gold = 100%) | `Parameter & Regeln`!B16 = `=B5+B6+B7` = 0.65+0.30+0.05 = 1.00 ✓ | `Parameter & Regeln` Rows 5-7 + B16 Formel-Read 2026-05-25T17:31 |

> **C4-deferred (Codex-Review 17:43)**: Cross-Sheet-Refs in `P5:P21` sind nur stichprobenartig validiert (B4, B16). Systematische Enumeration aller P-Formel-Targets ist auf v0.2-Iteration vertagt (siehe Task #7).

### 1.5 US-Exposure-Sheet — Sentinel-Set (Hochgestuft LOW → MEDIUM via Codex-Review)

**Codex-Befund**: 93 Formeln außerhalb der dokumentierten Pflichtprüfungen sind kein reiner Kosmetik-Gap → erhöhtes Drift-Risiko. Sentinel-Set definiert minimale Pflicht-Checks.

| Sentinel-Zelle | Inhalt | Cross-Sheet-Anchor | verified via |
|----------------|--------|-------------------|--------------|
| `US-Exposure!R03` | Header-Row: `Position | Ticker | Depotwert € | US-Faktor | US-Anteil €` | — | live-read 2026-05-25T17:31 |
| `US-Exposure!R04 A-D` | `='Portfolio & Rebalancing'!A5/B5/F5/E5` (Erste Ticker-Zeile gespiegelt) | ✓ R4 → Portfolio R5 (EUWAX Gold) | live-read |
| `US-Exposure!R20 A-D` | `='Portfolio & Rebalancing'!A21/B21/F21/E21` (Letzte Ticker-Zeile gespiegelt) | ✓ R20 → Portfolio R21 (AMZN) | live-read |
| `US-Exposure!R21 E` | `=SUM(E4:E20)` (Σ-US-Anteil €) | — | live-read |
| `US-Exposure!R23 B` | `=IF('Portfolio & Rebalancing'!F26=0,0,E21/...)` (US-Anteil Ist %) | ✓ Portfolio R26 = Gesamtwert nach Invest | live-read |
| `US-Exposure!R24 B` | `=SUMPRODUCT('Portfolio & Rebalancing'!$E...)` (US-Anteil Ziel %) | ✓ Portfolio E-Spalte (US-Faktoren) | live-read |
| `US-Exposure!R25 B` | `='Parameter & Regeln'!B11` (US-Hard-Cap-Lookup) | ✓ Parameter!B11 = 0.63 (63%) | live-read + Parameter Sheet-Probe |
| `US-Exposure!R26 B` | `=IF(B23>B25,"⛔ ÜBER CAP","✅ OK")` (Ist-Status) | — | live-read |
| `US-Exposure!R27 B` | `=IF(B24>B25,"⛔ ZIEL ÜBER CAP","✅ Ziel OK...")` (Ziel-Status) | — | live-read |

**Implikation**: US-Exposure ist 1:1-Spiegel-Sheet mit 17 Mirror-Zeilen (R4-R20 = Portfolio R5-R21) + 1 Σ + 5 Aggregate-Zellen. Wenn Portfolio-Ticker-Range sich ändert (z.B. Slot-Erweiterung), bricht das Mirror-Pattern fail-close (#REF!). Sentinel-Pflicht-Check: **R4 + R20 Mirror-Validität** (kein #REF!) + **R21 E Σ-Resolve** (nicht 0).

---

## 2. Satelliten_Monitor_v2.0.xlsx — SEKUNDÄR

### 2.1 Struktur-Drift

| Punkt | Doku xlsx-smoke-test.md | Live-State (Probe 17:31) | Drift | Severity | verified via |
|-------|-------------------------|--------------------------|-------|----------|--------------|
| Total Formeln | 12 (Scope-Tabelle Z18) | 13 (Satelliten Monitor 13 + QuickScreen Ampel 0) | +1 | LOW | `openpyxl` Formel-Count 2026-05-25T17:31 |
| CF-Rules | 5 (Scope-Tabelle Z18) | 5 | ✓ match | — | `len(ws.conditional_formatting._cf_rules)` 2026-05-25T17:31 |
| Sheets | nicht spezifiziert | 2: `Satelliten Monitor` (A1:S26), `QuickScreen Ampel` (A1:I23) | Doku-Gap | LOW | `wb.sheetnames` 2026-05-25T17:31 |
| Merges total | nicht spezifiziert | 21 (14+7) | Doku-Gap | LOW | `len(ws.merged_cells.ranges)` 2026-05-25T17:31 |
| Spalte Q (Datum-Stempel pro Ticker) | nicht spezifiziert | Q7-Q18 = 12 datetime-Cells (z.B. Q14=2026-05-04 BRK.B, Q18=2026-05-15 AMZN) | Doku-Gap | MEDIUM | datetime-Vollscan 2026-05-25T17:31 |
| Ticker-Range | nicht spezifiziert | R7-R18 (12 Slots = 12/12 belegt) + R19 Sparrate-Check + R21+ Legende | Doku-Gap | LOW | `ws.cell(r, 2)` r=4..22 2026-05-25T17:31 |

### 2.2 Pflicht-Zellen §D Drift

| Doku-Spec | Live-Befund (Probe 17:31) | Drift | verified via |
|-----------|---------------------------|-------|--------------|
| `O2 = 'Stand: YYYY-MM-DD ...'` | `O2 = 'Stand: 18.05.2026 (AMZN Neuaufnahme 12. Satellit — Score 42/DEFCON 1, 🔴 CapEx/OCF-FLAG, Sparrate 0€ regelkonform)  \|  Broker: Scalable Capital  \|  Slots: 12/12'` | ✓ Format match (String mit `Stand:`-Prefix) | live-read 2026-05-25T17:31 |
| `B3 = 'D3/D4-Rate: X€ \| D2-Sockelbetrag: Y€ \| Nenner Z'` | `B3 = 'Sparrate Satelliten: 285 €/Monat  \|  D3/D4-Rate: 38,00€  \|  D2-Sockelbetrag: 19,00€ (50%)  \|  Nenner 7.5 (unverändert — ...)'` | ✓ Format match (Live hat zusätzlichen Sparrate-Header-Prefix) | live-read 2026-05-25T17:31 |
| `H3 = Eingefroren-Liste mit Datum` | `H3 = 'Eingefroren: MSFT (● CapEx/OCF >60%, D2) \| APH (● Score-basiert 61, D2) \| AVGO (● Insider-Selling 90d $106M+, ab 27.04.) \| AMZN (● CapEx/OCF 99,2%, D1, ab 15.05.) → Sparrate 0€'` | ✓ Format match (User-Vereinheitlichung: `●` statt 🔴/🟢/🟠 Emojis als Status-Marker — Doku-Erwartung 🔴 noch im alten Format) | live-read 2026-05-25T17:31 |
| `K3 = Ergebnis-Zeile '🟢 N Voll 🟠 M D2 🔴 K Eingefroren (Liste)'` | `K3 = 'Ergebnis: ● 7 Voll  ● 1 D2-Sockelbetrag (V)  ● 4 Eingefroren (MSFT, APH, AVGO, AMZN)'` | Format ✓ / Status-Marker-Drift (●-Vereinheitlichung im Tool) | live-read 2026-05-25T17:31 |
| `L<ticker> = 'NN / DEFCON X'` | L7-L18 enthalten Format `'NN / DEFCON X'` (z.B. `L7='68 / DEFCON 3'` ASML, `L18='42 / DEFCON 1'` AMZN) | ✓ Format match | live-read R7-R18 2026-05-25T17:31 |
| `M<ticker> = Δ vs Vorperiode` | M7-M18 enthalten Δ-Strings (z.B. `M8='Δ-31 30.04. (Quality-Trap)'`, `M16='+3 Q1 FY26 Beat+Raise'`) | ✓ Format match | live-read R7-R18 2026-05-25T17:31 |
| `N<ticker> = Status/FLAG mit Pfad-Note + ggf. Q-Verify/PIPELINE` | N7-N18 enthalten FLAG-Status-Strings mit Pfad-Notes (z.B. `N7='● DEFCON 3 / ✅ Volle Rate 38,00€ (D3=1.0...)'`) | ✓ Format match (User-Vereinheitlichung: `●` als Status-Marker statt 🟡/🟠/🔴 Doku-Erwartung) | live-read R7-R18 2026-05-25T17:31 |
| **`B24 = Footer Eingefroren-Liste komplett mit FLAG-Grund pro Ticker`** | **`B24 = '[~] – Schätzung Wissensbasis (plausibel) \| [V] – Vollanalyse verifiziert \| [TC] – Tariff-Check abgeschlossen 15.04.2026'`** (= LEGENDE der Verifikations-Marker, NICHT Eingefroren-Liste!) | **KRITISCH SWAP** — B24 ist Legende, NICHT Eingefroren-Liste | live-read 2026-05-25T17:31 |
| **`B25 = Footer Volle-Rate-Liste mit Σ-Check-Formel '7×38,00 + 1×19,00 + 3×0 = 285,00€ ✓'`** | **`B25 = '● EINGEFROREN: MSFT (FLAG CapEx/OCF >60%, D2, Score 50) \| APH (FLAG Score-basiert, D2, Score 61) \| AVGO (FLAG Insider-Selling 90d $106M+, D2 Score 53, ab 27.04.) \| AMZN (FLAG CapEx...)'`** (= EINGEFROREN-Liste, NICHT Volle-Rate-Liste mit Σ-Check) | **KRITISCH SWAP** — B25 ist Eingefroren-Liste | live-read 2026-05-25T17:31 |
| **`Σ-Check-Formel im Footer B25 resolvet ohne Fehler`** | Σ-Check existiert NICHT als Excel-Formel — nur als Text-Note in **`N19 = '→ muss = 285,00 €'`** (kein `=`-Prefix, kein Formel-Resolve) | **KRITISCH** — Doku-Erwartung „Formel resolvet" technisch unmöglich | live-read R19 2026-05-25T17:31 |
| **`B26` — Doku kennt B26 nicht** | **`B26 = '● Volle Rate 38,00€ (7 Positionen): ASML/COST/RMS/VEEV/SU/BRK.B/TMO D3  \|  ● D2-Sockelbetrag 19,00€ (1): V  \|  ● Eingefroren 0€ (4): MSFT, APH, AVGO, AMZN  \|  Nenner 7×1,0 + 1×0,5 ...'`** | **NEU** — User hat B26 als „Volle-Rate-Liste + Aufteilung" hinzugefügt (entspricht eigentlich der ursprünglichen Doku-Erwartung für B25, nur eine Zeile drunter) | live-read 2026-05-25T17:31 |

### 2.3 QuickScreen Ampel Sheet (kompletter Doku-Gap)

Doku xlsx-smoke-test.md kennt das `QuickScreen Ampel`-Sheet komplett **nicht** (Scope-Tabelle Z18 erwähnt nur „Satelliten Monitor"-Sheet). User hat das Sheet überarbeitet — Live-Struktur:

| Row | Inhalt | verified via |
|-----|--------|--------------|
| R02 | Header DYNASTIEDEPOT - QUICKSCREEN AMPEL | live-read 2026-05-25T17:31 |
| R03 | Filter-Beschreibung (P/FCF ≤ 35x, ROIC, Moat) | live-read |
| R05 | Spalten-Header: Ticker, Name, P/FCF Filter, ROIC Filter, Moat Filter, FLAG, Gesamt-Ampel, Nächster Schritt | live-read |
| R06-R17 | 12 Ticker (ASML, AVGO, MSFT, COST, RMS, VEEV, SU, BRK.B, V, TMO, APH, AMZN) mit Ampel-Status pro Filter | live-read |
| R19 | LEGENDE-Header | live-read |
| R20-R23 | Ampel-Erklärung (●-Marker semantik HALTEN/PRÜFEN/EINGEFROREN/Exception-Logik) | live-read |

**Implikation**: §D muss um QuickScreen-Ampel-Scope erweitert werden (Pflicht-Cells: R5 Header-Integrität, R6-R17 Ticker-Vollständigkeit gegen Satelliten-Monitor R7-R18 Cross-Check, R19+ Legende-Existenz).

### 2.4 Spec-Patches Satelliten

1. **B24 ↔ B25 Swap** — Doku §D-Tabelle muss B24-Beschreibung mit B25-Beschreibung tauschen (Live: B24=Legende `[~]/[V]/[TC]`, B25=Eingefroren-Liste).
2. **B26 als neue Pflicht-Zelle dokumentieren** — Volle-Rate-Liste + Nenner-Aufteilung.
3. **Σ-Check Variante G entschieden + EMPIRISCH VALIDIERT 2026-05-25T18:30** — config.yaml SSoT + Hook-Logik:

   **Mapping-Regel** (in Hook-Code, Python):
   ```python
   def derive_rate(satellit_cfg):
       if satellit_cfg["flag"] is True:
           return 0
       defcon = satellit_cfg["defcon"]
       if defcon in (3, 4):  return 38
       if defcon == 2:       return 19
       if defcon == 1:       return 0  # nur falls FLAG fehlt aber DEFCON 1
       raise ValueError(f"unmapped defcon={defcon}")
   ```

   **Cross-Checks**:
   1. `sum(derive_rate(s) for s in cfg["satelliten"]) == cfg["brokers"]["scalable"]["sparrate_eur"]` (Pflicht-Anker `285.00`, config.yaml L27 — `portfolio.satelliten_sparrate` existiert NICHT, korrigiert 2026-05-25 post Codex-R1)
   2. xlsx-Display K3-Text muss konsistente Zahlen enthalten (z.B. `'7 Voll'` + `'1 D2-Sockelbetrag'` + `'4 Eingefroren'`)
   3. xlsx B26-Text muss dieselben Ticker-Aufteilungen enthalten
   4. xlsx N19-Text muss literal `'→ muss = 285,00 €'` enthalten (Sanity-Echo)

   **Empirie-Validierung 2026-05-25T18:30** (12 Satelliten aus Live config.yaml):
   - ASML D3 noFLAG=38, AVGO D2 FLAG=0, MSFT D2 FLAG=0, COST D3 noFLAG=38, RMS D3 noFLAG=38, VEEV D3 noFLAG=38, SU D3 noFLAG=38, BRK.B D3 noFLAG=38, V D2 noFLAG=19, TMO D3 noFLAG=38, APH D2 FLAG=0, AMZN D1 FLAG=0
   - **Σ = 7×38 + 1×19 + 4×0 = 285€ ✓ MATCH** mit `cfg.brokers.scalable.sparrate_eur` (config.yaml L27 — Pfad-Korrektur post Codex-R1 HIGH-1, vorher fälschlich `cfg.portfolio.satelliten_sparrate` der nicht existiert)
   - Vorher: Freitext-Mapping-Variante (F) ergab Σ=95€ → 5 Tickers ungemapped weil ihre N-Spalte `'● Halten | D4→D3'` statt `'● Volle Rate 38'` enthält. **Freitext-Inkonsistenz validiert Codex-R2-F2 Warnung literal.**

   **Implementations-Konsequenzen**:
   - xlsx Sat braucht KEINE neue Cell, KEINE Σ-Formel, KEINEN Code-Spalte — Display bleibt wie es ist
   - Hook-Code wird erweitert um „Punkt G — Sparrate-Σ-Sanity" Funktion (~30 LOC Python)
   - `safe_insert.py` Helper-Erst-Use-Case ändert sich: nicht mehr für Sat-Σ-Formel (entfällt), sondern für andere xlsx-Edits (z.B. Pflicht-Cell-Update bei Sparrate-Change in config.yaml → xlsx B3/K3 update via openpyxl) — sicheres openpyxl-Schreiben bleibt scope-relevant
   - **Validierung 100% empirisch** auf Live-config.yaml + Live-Sat-xlsx 2026-05-25T18:30 — keine Annahmen, alle Sub-Komponenten dry-run-getestet
4. **QuickScreen-Ampel-Sheet im Scope ergänzen** — §D oder neuer §D2.

---

## 3. Watchlist_Ersatzbank_Monitor_v1.1.xlsx — HOCHGESTUFT-KANDIDAT

### 3.1 Minimal-Check §Annex (Doku-Aktueller-Stand)

| Punkt | Doku-Erwartung | Live (Probe 17:31) | Status | verified via |
|-------|----------------|--------------------|--------|--------------|
| A. Datei öffnet ohne Repair-Prompt | PASS | `openpyxl.load_workbook` ohne Exception + 0 Warnings | ✓ PASS | execute 2026-05-25T17:31 |
| Existenz + lesbar | PASS | File präsent unter `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx` (20354 bytes, mtime 17:07:28) | ✓ PASS | `os.path.exists` + size + mtime 2026-05-25T17:31 |

### 3.2 Struktur-Cross-Check

| Punkt | Doku | Live | Drift |
|-------|------|------|-------|
| Sheet-Count | 1 | 1 (`Watchlist_Ersatzbank`) | ✓ match |
| Formeln | 0 | 0 | ✓ match |
| CF-Rules | 0 | 0 | ✓ match |
| Merges | nicht spezifiziert | 4 (vorher 14 — User hat reduziert) | Doku-Gap |
| dims | nicht spezifiziert | A1:O39 (vorher max_row=50 — User komprimiert) | Doku-Gap |

### 3.3 Inhaltlicher Live-Stand (Doku-Gap)

Doku §Annex sagt: „Hochstufung in Voll-Smoke-Test sobald Watchlist-Tool-Update PIPELINE-Item resolved (Formeln / Logik hinzugefügt)." Live-Inhalt zeigt **Watchlist ist bereits inhaltlich Voll-Scope**, nur ohne Formeln/CF:

| Row | Inhalt | verified via |
|-----|--------|--------------|
| R01 | `'🦅 DYNASTIEDEPOT – WATCHLISTE / ERSATZBANK'` Header | live-read 2026-05-25T17:31 |
| R02 | Zweck-Beschreibung | live-read |
| R03 | `'Ersatzbank: 11 Ticker'` | live-read |
| R04 | Spalten-Header: Ticker, Name, Kategorie, P/FCF, ROIC%, Gross Margin%, Rev CAGR 3Y%, Moat (GuruFocus), P/B (Excptn.), Exception, Score/DEFCON, Status (Ampel), Hinweis, Datenstand/Quelle | live-read |
| R05-R17 (ca.) | 11 Ticker-Einträge (ADBE, DE, FFH.TO, ..., FICO, IDXX, KLAC, MA, ...) jeweils mit Kategorie (z.B. „Ersatzbank MSFT (NEU 14.05.)"), Filter-Werten + Status-Ampel + Hinweis + Datenstand-Quelle | live-read |
| R27-R39 | Weitere Ticker-Einträge + Sektion (Exception-Notes, REJECTED-Ticker wie TYL, ZTS Grenzfall) | live-read |

**Implikation**: Watchlist ist faktisch Voll-Scope-fähig (12+ Ticker mit DEFCON-Spalte + Status-Ampel). Aber wegen 0 Formeln/0 CF besteht weiterhin **kein** openpyxl-Korruptions-Risiko → Minimal-Annex bleibt korrekt. Was drift gegen Doku ist: die Beschreibung „Hochstufung nach Watchlist-Tool-Update Logik hinzugefügt" — Logik (im Sinne von Status-Ampel-Werten) IST hinzugefügt, nur nicht als Excel-Formeln.

### 3.4 Spec-Patches Watchlist

1. **Doku §Annex Re-Phrase**: Hochstufungs-Trigger präzisieren — „Formeln (`=...`) hinzugefügt" statt „Logik hinzugefügt" (Status-Ampel-Werte sind Logik aber ohne Korruptions-Risiko).
2. **Optional**: Pflicht-Cell-Light einführen (R3 Ersatzbank-Count `'11 Ticker'` vs aktuelle Ticker-Row-Count Konsistenz-Check) — schließt manuelle Drift-Quelle.

---

## 4. Pre-commit-Hook `03_Tools/precommit/xlsx_smoke_test.py` — Reconciliation

**Codex-Befund (C1)**: Der Hook implementiert §18.7 fail-close gegen die alte Doku-Soll-Werte. Bei Doku-Patches (P1-P12) muss der Hook synchron mitgepatched werden, sonst entsteht Spec ↔ Hook ↔ Live Drei-Wege-Drift.

**Hook-Architektur** (read-only, fail-close, 160 LOC):
- Implementiert nur **A** (Open) + **B** (Error-Token-Scan) + **E** (CF-Rule-Count). C/D/F sind manuell (Excel-UI), nicht git-gate-fähig.
- Hardcoded `_PROFILES`-Dict mit Soll-Werten (Sheets-Tupel + CF-Count). SSoT = `xlsx-smoke-test.md`, aber Werte sind im Code dupliziert.

| Profil | Hook-Sheets-Liste (`_PROFILES["...sheets"]`) | Hook-CF-Count | Live-Sheets | Live-CF-Count | Drift |
|--------|---------------------------------------------|---------------|-------------|---------------|-------|
| Rebalancing_Tool | `("Portfolio & Rebalancing",)` | 6 | 3 Sheets (Portfolio & Rebalancing, **US-Exposure**, **Parameter & Regeln**) | 6 (total) | **Hook prüft nur Portfolio-Sheet-Existenz** — US-Exposure + Parameter werden NICHT gegen Sheet-Existenz validiert (würden bei Sheet-Delete/Rename silent durchrutschen); CF-Count match ✓ |
| Satelliten_Monitor | `("Satelliten Monitor",)` | 5 | 2 Sheets (Satelliten Monitor, **QuickScreen Ampel**) | 5 (total) | **Hook prüft nur Satelliten-Monitor-Sheet-Existenz** — QuickScreen Ampel (vom User in dieser Session überarbeitet) wird NICHT validiert; CF-Count match ✓ |
| Watchlist_Ersatzbank_Monitor | `()` (leer, Minimal-Profil) | 0 | 1 Sheet (Watchlist_Ersatzbank) | 0 | ✓ match — Minimal-Profil prüft nur A1-non-empty + Existenz |

**Drift im Hook-Code (Source-Kommentare)**:
- ~~`Rebalancing_Tool` Z42-Kommentar: `# md: "218 Formeln + 6 Conditional Formats"` → outdated, Live ist 249 Formeln~~ **RESOLVED 2026-05-25T20:00** post P1+P13+P15 Multi-File-Sync — Z42-Kommentar jetzt `# md: "249 Formeln + 6 Conditional Formats"`
- ~~`Satelliten_Monitor` Z47-Kommentar: `# md: "12 Formeln + 5 Conditional Formats + Σ-Check"` → outdated, Live ist 13 Formeln + Σ-Check ist Text in N19~~ **RESOLVED 2026-05-25T20:00** post P1+P13+P15 Multi-File-Sync — Z47-Kommentar jetzt `# md: "13 Formeln + 5 Conditional Formats + §G Σ-Check via Hook"`

**Was der Hook NICHT prüft (by-design oder Lücke?)**:
1. Datum-Stempel A2 (datetime-Aktualität) — nicht implementiert, auch nicht in §18.7-Punkten A/B/E
2. Pflicht-Zell-Cross-Checks §C/§D — by-design manuell ("UI-only, nicht git-gate-fähig" laut Hook-Header)
3. Spalten-Drift (Q + R28 Erweiterung in Rebal) — nicht erfasst
4. Sheet-Vollständigkeit über das primäre Sheet hinaus — Lücke

**Spec-Patch-Reconciliation (P13)**:
- Hook-`_PROFILES["sheets"]` muss von `("Portfolio & Rebalancing",)` auf `("Portfolio & Rebalancing", "US-Exposure", "Parameter & Regeln")` erweitert werden (Sheet-Existenz für alle 3 prüfen)
- Analog Satelliten: `("Satelliten Monitor",)` → `("Satelliten Monitor", "QuickScreen Ampel")`
- Hook-Source-Kommentare Z42 + Z47 updaten auf Live-Werte (oder besser: aus Doku-Header parsen statt hardcoded)
- Optional: Hook-CF-Count-Reconciliation prüfen falls P-Patches CF-Counts ändern (aktuell match — kein Update nötig)

---

## Gesamtbilanz Spec-Patches (Pre-Spec-Pflicht)

| # | Section | Patch | Severity |
|---|---------|-------|----------|
| P1 | §1 Rebal Scope | Total-Formel-Count 218 → 249 | LOW |
| P2 | §C Rebal Pflicht | Ticker-Range R18-R28 → R5-R21 (5 ETFs + 12 Aktien Slots) | HIGH |
| P3 | §C Rebal Pflicht | Datum-Stempel R2-String → A2-datetime-Objekt (Smoke-Test-Logic: `isinstance(value, datetime)` statt regex) | HIGH |
| P4 | §C Rebal Pflicht | Footer-Aggregate-Layer ergänzen (R22 SUM/COUNTIF/SUMIF + R23 Labels + R24-R27 Cash/Invest/Gesamtwert/ING-Split) | MEDIUM |
| P5 | §1 Rebal Scope | Spalte Q + Row 28 dokumentieren (max_col 16→17, max_row 27→28) | LOW |
| P6 | §D Satelliten Pflicht | B24 ↔ B25 Swap-Korrektur | HIGH |
| P7 | §D Satelliten Pflicht | B26 als neue Pflicht-Zelle (Volle-Rate-Liste + Nenner-Aufteilung) | MEDIUM |
| P8 | §D Satelliten Pflicht | **✓ ENTSCHIEDEN (Variante G — config.yaml SSoT + Hook-Logik, post-Empirie-Test 2026-05-25T18:30; Anker-Pfad-Fix 2026-05-25 post Codex-R1)** Σ-Check verschiebt sich von Excel zum Hook. Mapping-Logik: `flag=True→0€`, `flag=False+defcon∈{3,4}→38€`, `flag=False+defcon=2→19€`. Cross-Check: Hook-Σ == `config.yaml.brokers.scalable.sparrate_eur` (literal 285.00, L27) + xlsx-Display (K3/B3/B26-Texte) konsistent. **Empirisch validiert**: G-Σ = 7×38+1×19+4×0 = 285€ ✅ (siehe §2.4 unten). | HIGH |
| P9 | §D Satelliten Scope | QuickScreen-Ampel-Sheet aufnehmen (R5 Headers + R6-R17 Ticker-Konsistenz + R19+ Legende) | MEDIUM |
| P10 | §D Satelliten Pflicht | `●`-Status-Marker-Vereinheitlichung dokumentieren (User-Format-Change vs Doku 🟢/🟡/🟠/🔴) | LOW |
| P11 | §Annex Watchlist | Hochstufungs-Trigger Re-Phrase „Formeln (`=...`)" statt „Logik" | LOW |
| P12 | §1 Rebal Scope | Sheet-Liste explizit (Portfolio/US-Exposure/Parameter) dokumentieren | LOW |
| **P13** | §3.1 Pre-commit-Hook | **Hook-`_PROFILES["sheets"]` erweitern** (Rebal +US-Exposure+Parameter, Sat +QuickScreen-Ampel) + Source-Kommentare Z42/Z47 auf Live-Werte updaten (oder aus Doku-Header parsen statt hardcoded). **Non-goal explizit** (Codex-R2-F3): Q-Spalten-Datum-Drift wird NICHT im Hook geprüft (gehört zu manuellen Pflichtchecks §C/§D bzw. P9/P14) — keine falsche Sicherheit erzeugen. | HIGH |
| **P14** | §1.5 Rebal US-Exposure | **US-Exposure-Sentinel-Set in Pflicht-Check aufnehmen** (R4+R20 Mirror-Validität + R21 E Σ-Resolve + R25 B Cross-Ref auf Parameter!B11) | MEDIUM |
| **P15** | `00_Core/INSTRUKTIONEN.md §18.7` Z475 + `00_Core/SYSTEM.md` L42 (v2.4-Lifecycle-Eintrag, post 2026-05-25 Cover-Gap-Expansion) | **Multi-File-Sync mit P1+Hook (4 Files, nicht 3)**: INSTRUKTIONEN.md §18.7 + SYSTEM.md §Plugin-Layer-Lifecycle-Block zitieren beide „Rebalancing v3.4: 218 Formeln + 6 CF; Satelliten-Monitor v2.0: 12 Formeln + 5 CF" — Vier Doku-Files (INSTRUKTIONEN + xlsx-smoke-test.md + Hook-Source-Comments + SYSTEM.md) müssen synchron auf Live-Werte (Rebal 249, Sat 13) gepatched werden. SYSTEM.md L42 wurde initial als „historischer Snapshot" mis-skopt; User-Direktive 2026-05-25T20:05: Live-State-Aussagen über Gate-Scope sind Live, nicht historisch eingefroren. **verified via**: `Grep "218 Formeln"` in `00_Core/` 2026-05-25T20:00 = 2 Treffer (INSTRUKTIONEN + SYSTEM); ferner SPEC §6 Schritt 1 Erweiterung auf 4 Files. | HIGH |
| **P16** | `00_Core/PIPELINE.md` ↔ xlsx-smoke-test.md §Annex-Reference | **Hängende PIPELINE-Referenz**: xlsx-smoke-test.md §Annex zitiert „offenes PIPELINE-Item Watchlist-Tool-Update" — Grep auf PIPELINE.md zeigt **kein** entsprechendes Item (6 andere Watchlist-Treffer #62/#63/#52/#53/#73/#77). Entweder Item resolved/umbenannt/nie angelegt. Verschärft P11: Hochstufungs-Trigger braucht entweder konkrete PIPELINE-Item-ID ODER Re-Phrase ohne PIPELINE-Backing. **verified via**: `Grep Watchlist|Ersatzbank` in PIPELINE.md 2026-05-25T18:15 (109 Zeilen total, 6 Hits, kein Tool-Update-Item) | MEDIUM |

**16 Patches total** — **8 HIGH** + **5 MEDIUM** + **3 LOW** (nach Substrate-Audit-Erweiterung).

### Sequenzierungs-Regel (Pre-Spec, post-Substrate-Audit)

```
P8 (✓ entschieden — β Tool-Patch) → Implementation in Spec-Phase als Erst-Use-Case safe_insert.py
  ↓
P1 + P13 + P15 MULTI-FILE-SYNC (Drei-Wege-Drift-Vermeidung):
  - xlsx-smoke-test.md Scope-Tabelle (Formel-Counts 218→249, 12→13)
  - 00_Core/INSTRUKTIONEN.md §18.7 Z475 (Formel-Counts identisch)
  - 03_Tools/precommit/xlsx_smoke_test.py Z42/Z47 (Kommentare)
  Alle drei in EINEM Commit, sonst entsteht Spec/Hook/Doku Inkonsistenz
  ↓
P13 Hook-Profile-Erweiterung (Sheets-Liste pro Profil)
  ↓
P16 PIPELINE-Reference-Klärung (verschärft P11: konkrete Item-ID oder Re-Phrase)
  ↓
Restliche Patches (P2, P3, P4, P5, P6, P7, P9, P10, P11, P12, P14) können in beliebiger Reihenfolge
```

### Spec-Phase Test-Fixture-Constraint (Audit-A4)

**Pflicht-Adoption** des etablierten Patterns aus `03_Tools/precommit/_fixtures/_generate_fixtures.py`:
- Deterministisch (kein Timestamp/Random)
- Byte-exakt
- Pro Test: 1 valid + 1 invalid Fixture
- **Beschreibende Namen** (NICHT `bad_*`/`good_*` per Memory `feedback_cr_convergence_and_project_compat`)
- xlsx-Fixtures via `openpyxl.Workbook()` mit explizitem Profil-Match (Name-Prefix `Rebalancing_Tool` / `Satelliten_Monitor` / `Watchlist_Ersatzbank_Monitor`)
- Schema-Drift wirft laut (`assert` / `ValueError` statt silent-pass)
- **Voll-Scope-Fixtures fehlen** — aktuell nur Watchlist-Minimal (`*_fixture_clean.xlsx` + `*_fixture_empty_a1.xlsx`). Für Rebal + Sat Voll-Scope-Smoke-Test braucht es zusätzliche Fixtures (Pflicht-Cell-Drift, CF-Count-Drift, Formel-Fehler-Klassen).

### Substrate-Status (Audit-A3)

**`safe_insert.py` Helper hat KEIN existing Substrate** im Repo:
- `Grep` auf `safe_insert|insert_rows|insert_cols|safe_xlsx|openpyxl.*insert|merge.*insert` in allen `.py` Files = 0 Treffer (2026-05-25T18:15)
- → Neubau, kein Duplicate-Code-Risiko, kein Refactor-Konflikt mit existierendem Tool

**P8-Entscheidung pending (User-Input nötig)**:
- Option α (Doku-Patch): §D auf „Σ-Check ist Text-Sanity in N19" umstellen, kein Excel-Formel-Resolve nötig. Niedrigerer Aufwand, schwächere Verifikation.
- Option β (Tool-Patch): Echte `=SUMPRODUCT`-Σ-Formel in B-Spalte ergänzen die `285,00€` literal resolvet. Höherer Aufwand, starke Verifikation.

---

## 5. Out-of-Scope dieser Iteration (Codex-Review C6)

Folgende Drift-Dimensionen sind in dieser v0.1-Drift-Doc **nicht** abgedeckt — explizit dokumentiert um Fehlinterpretation als „vollständige Drift-Abdeckung" zu vermeiden:

| Dimension | Warum out-of-scope v0.1 | Re-Activation-Trigger |
|-----------|-------------------------|-----------------------|
| Cell-Number-Format (z.B. Datum-Anzeige `TT.MM.JJJJ`) | Reine Display-Eigenschaft, kein Daten-Inhalt | Wenn A2-datetime falsch in Excel rendert oder Sparrate als String statt Zahl angezeigt |
| Cell-Color (Conditional-Formatting **Rules-Identität**, nicht nur Count) | Smoke-Test §E ist CF-Count-Check, nicht Rules-Diff | Wenn Live CF-Rules-Count matched aber Färbung falsch wird (silent CF-Rule-Mutation) |
| Defined Names (Workbook-level Named Ranges) | Aktuell keine vermutete Nutzung in den 3 xlsx | Wenn Formeln zu Named-Ranges-Refs migriert werden |
| Pivot-Tables | Keine Pivots in den 3 xlsx (verifiziert via `openpyxl`-Load ohne Pivot-Warnings) | Wenn ein Sheet Pivot-Source bekommt |
| Workbook-Protection-Status (Read-only-Flag, Password) | Aktuell kein Protection-Layer in den 3 xlsx | Wenn versehentliche Protection-Aktivierung Smoke-Test blockiert |
| Print-Settings (Print-Area, Print-Scaling) | Reine Druck-Output-Eigenschaft | Wenn Print-Area falsch und Sparplan-Druck unvollständig |
| Cross-Sheet-Refs **systematisch enumeriert** (C4-deferred) | Stichprobe statt vollständige Parse aller P-Formel-Targets | v0.2-Drift-Doc (Task #7) |
| `verified via:` 4-Felder-Schema (C5-deferred) | Aktuell uneinheitliches Annotation-Format; **v0.1-Mindeststandard (Codex-R2-F4)**: mindestens `sheet!cell + timestamp` verpflichtend, volles 4-Felder-Schema (sheet!cell + Read-Expr + Erwartet + Timestamp) erst v0.2 | v0.2-Drift-Doc (Task #7) |

**Promotion-Schwelle**: Eine Dimension wird in v0.2+ aufgenommen wenn (a) ein Real-Incident in der Dimension auftritt, ODER (b) ein User-Edit-Pattern systematisch dahin driftet, ODER (c) das xlsx-smoke-test-runner-Skill (post-Spec) Coverage-Erweiterung benötigt.

---

## Memory-Links

- [[reference_context_mode_surrogate_crash_and_fix]] — Crash-Recovery-Pfad warum dieses Doc post-Restart entstand
- [[feedback_empirie_statt_annahmen]] — Methodologie-Grundlage (jede Behauptung `verified via:`)
- [[feedback_xlsx_tools_in_sync_set]] — operative Edit-Patterns für die betroffenen xlsx-Files
- [[feedback_openpyxl_insert_merge_trap]] — AMZN-Bug-Klasse die α+ via safe_insert.py adressiert
- [[feedback_skill_name_is_scope_contract]] — Scope-Coverage-Lesson aus core-slim-refactor (warum Gate-0-Matrix Pflicht)
- [[reference_no_cloud_sync_onedrive_inactive]] — relevant für mtime-Probe (no cloud delay)
