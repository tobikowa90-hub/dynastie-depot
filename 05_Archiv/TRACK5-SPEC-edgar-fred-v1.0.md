# 🎯 TRACK 5 — SEC EDGAR + FRED Integration (Design-Spec)

**Status:** Draft | **Datum:** 2026-04-20 | **Autor:** Tobias Kowalski (mit Claude + Codex Co-Review)
**Scope:** Zwei technisch unabhängige Sub-Tracks als ein gemeinsames Paket
**Gate vor Implementation-Start:** 3-Tage-Monitoring nach Tavily-Go-Live stabil (per `SESSION-HANDOVER.md`)

---

## 1. Kontext & Motivation

Dynasty-Depot ist bottom-up-Value/Quality-Portfolio mit 11 Satelliten und DEFCON-Scoring v3.7. Zwei Datenquellen-Dimensionen sind aktuell **unvollständig** im System:

- **SEC EDGAR** ist nur als WebFetch-Fallback + `_extern/sec-edgar-skill` (nicht aktiv) präsent. Strukturierte XBRL-Pipeline fehlt bei Daten-Konflikten zwischen defeatbeta und Shibui.
- **FRED** ist vollständig greenfield. Kein Macro-Input in Scoring, keine Sparraten-Regime-Modulation, kein Makro-Kontext für Backtest-Auswertung.

Dieser Track adressiert beides **parallel** in zwei klar getrennten Sub-Tracks. Jede Erweiterung hat klare Grenzen: keine Duplikation bestehender Primärquellen (defeatbeta/Shibui für Fundamentals), keine Verschiebung der Bottom-up-Doktrin.

### 1.1 Design-Entscheidungen (Co-Review Claude + Codex, 2026-04-20)

| Entscheidung | Wert | Begründung (kurz) |
|--------------|------|-------------------|
| FRED-Integrationstiefe | **Option B (Regime-Filter)** | Nicht Scoring-Input (Option C): bei nur 3 zyklischen Tickers (APH/AVGO/teils Schneider) Overfitting-Risiko hoch, per-Ticker-Kausalität schwach. Regime-Filter auf Sparraten-Ebene sauber testbar. |
| EDGAR-Integrationstiefe | **Variante (ii): Skill-Promotion** | Nicht First-Class-MCP (iii): würde defeatbeta duplizieren bei 11 Namen und quartalsweiser Kadenz. Nicht Status quo (i): WebFetch-Fallback ist fragil für XBRL. |
| Sequencing | **5a + 5b parallel** | Write-Ziele konzeptionell getrennt (EDGAR → Fundamentals-Fallback; FRED → Sparraten-Overlay). Integrations-Risiko statt Blocker-Risiko. |
| Paper-Logging-Phase (ursprünglich erwogen) | **Gestrichen** | Ersetzt durch historischen Backtest (FRED-Serien ab 1970er, SPY ab 1993). Evidenz-basierte Threshold-Kalibrierung statt 6-12M-Forward-Logging. |
| As-of-Policy (Lookahead-Vermeidung) | **(c) Hybrid** | Daily-Serien (HY-OAS, 10Y-2Y Treasury-Curve) Release-Day-Wert. Monthly-Serien (ISM) T+1 nach Veröffentlichung. Reflektiert reale Entscheidungssituation. |
| Grid-Search-Optimierungsziel | **Sparraten-Utility primär, MaxDD als Constraint** | Regime-Filter moduliert Sparrate, handelt keine Position → Utility-Funktion ist „nicht auf Hochs vor Drawdowns kaufen". MaxDD-Constraint verhindert Utility-Optimum auf Kosten katastrophaler Verluste. |
| Kalibrierungs-Disziplin | **Konservative Params + Sensitivitätsfenster** | Nicht Point-Optimum. Codex-Mitigation gegen Regime-Snooping (wenige Krisenepisoden 2008/2020/2022). |

### 1.2 Vorherige Codex-Empfehlung (SESSION-HANDOVER.md)

> 1. SEC EDGAR zuerst (klarer Hebel, bereits partiell im System)
> 2. FRED separat — erst wenn Macro-in-DEFCON-Strategie-Entscheidung getroffen ist

**Update 2026-04-20:** Strategische Frage geklärt als „Ja, aber nur als Regime-Filter auf Sparraten-Ebene — kein Eingriff in per-Ticker-Scoring". Damit ist FRED nicht mehr strategisch-blockiert, sondern technisch ausgeführt.

---

## 2. Sub-Track 5a — SEC EDGAR Skill-Promotion

### 2.1 Ziel
`sec-edgar-skill` als **aktiven Eskalations-Fallback** etablieren (INSTRUKTIONEN §22) — verbesserter Zugriff bei Daten-Konflikten, 10-K/10-Q-Section-Disputen und als strukturierte zweite Quelle für Form-4-Fälle, die `insider_intel.py` nicht sauber löst.

### 2.2 Was verändert sich

**Vorher (Status quo):**
- `01_Skills/_extern/sec-edgar-skill/SKILL.md` — liegt als read-only Referenz vor, **nicht aktiv**
- WebFetch-Permission auf `efts.sec.gov` — HTML-Scraping als Fallback
- `insider_intel.py` nutzt eigene SEC-EDGAR-Form-4-Pipeline

**Nachher:**
- Skill promoted nach `01_Skills/sec-edgar-skill/SKILL.md`
- EdgarTools installiert (`pip install edgartools`)
- `set_identity("Tobias Kowalski tobikowa90@gmail.com")` einmalig in Skill-Init dokumentiert (SEC-Legal-Requirement)
- Skill-Auto-Discovery über Claude Code (SKILL.md mit frontmatter)

### 2.3 Was bleibt unverändert (explizit)
- **defeatbeta MCP** bleibt Primärquelle für US-Fundamentals (income/cashflow/balance/ROIC/WACC)
- **Shibui SQL** bleibt Primärquelle für Technicals und historische Breite
- **`insider_intel.py`** bleibt Primärpipeline für Form-4 — EDGAR-Skill **nur als Fallback** bei unklaren Cashless-Exercise-Fällen
- `!Analysiere`-Routing bleibt unverändert — Skill ist eskalations-getriggert, nicht kadenz-getriggert

### 2.4 Use-Cases (wann wird Skill aktiv aufgerufen)
1. **Daten-Konflikt:** defeatbeta-Wert weicht >5% von Shibui ab → EDGAR als Schiedsquelle via XBRL (`company.income_statement(periods=5)`)
2. **10-K/10-Q-Textsuche:** Spezifische Risk-Factor / MD&A-Passagen (`filing.search("climate risk")`) — aktuell nur per WebFetch-HTML, fehleranfällig
3. **Form-4-Eskalation:** Ein Insider-Fall in `insider_intel.py` trägt ambiguous Broadcom-10b5-1-Pattern → EDGAR-Skill liefert strukturierten Filing-Kontext (`company.get_filings(form="4")`)
4. **Multi-Period-Trend:** Entity Facts API (`company.income_statement(periods=20)`) für 5-Jahres-Trends ohne Multi-Filing-Parse

### 2.5 INSTRUKTIONEN-Integration
- §22 (Skill-Referenz-Tabelle) bleibt strukturell. Zeile „`sec-edgar-skill` | Eskalations-Fallback" wird aktualisiert mit Hinweis: „aktiver Skill (v1.0) seit 2026-04-XX, EdgarTools-basiert, `.to_context()` obligatorisch zur Token-Effizienz".
- §19 (API-Routing) — keine Änderung. Sequenz „defeatbeta → Shibui → SEC EDGAR" bleibt.

### 2.6 Akzeptanz-Kriterien 5a
- [ ] `01_Skills/sec-edgar-skill/SKILL.md` existiert mit frontmatter und ist via Skill-Auto-Discovery erreichbar
- [ ] `pip install edgartools` erfolgreich in Projekt-Python-Environment
- [ ] Smoke-Test: `Company("MSFT").income_statement(periods=3)` liefert strukturierte XBRL-Response ohne Fehler
- [ ] `.to_context()`-Token-Check: ≤100 Tokens für Company-Summary, ≤300 für XBRL-Summary
- [ ] INSTRUKTIONEN §22 aktualisiert
- [ ] CORE-MEMORY §5 Audit-Eintrag: „EDGAR-Skill promoted, EdgarTools installed"

### 2.7 Out of Scope (5a)
- **Kein** First-Class-EDGAR-MCP als Ersatz für defeatbeta
- **Keine** automatische Einbindung in `!Analysiere`-Workflow
- **Keine** Migration von `insider_intel.py` auf EDGAR-Skill — beide existieren parallel

---

## 3. Sub-Track 5b — FRED Regime-Filter (Option B)

### 3.1 Ziel
Drei FRED-Macro-Serien als **Sparraten-Regime-Modulator** — ex-ante-mechanische Trigger-Regeln schalten Sparraten-Modus zwischen `normal` und `risk_off`. Kein Eingriff in DEFCON-Scoring. Kein diskretionärer Override.

### 3.2 Komponenten

#### 3.2.1 FRED API Integration
**TBD in Implementation-Phase:** zwei Kandidaten
- **Option α:** `dracepj/fred-mcp` — MCP-Server, konsistent mit Projekt-Muster (defeatbeta/Shibui/Tavily)
- **Option β:** `fredapi` Python-Lib direkt — einfacher, kein MCP-Overhead, aber Bruch mit Muster

Beide erfordern FRED-API-Key (kostenlos, Registrierung via `https://fred.stlouisfed.org/docs/api/api_key.html`).

**Spec-Entscheidung:** Implementation-Plan entscheidet α vs. β basierend auf MCP-Verfügbarkeit und Maintenance-Status von `dracepj/fred-mcp`.

#### 3.2.2 Persistenz: `05_Archiv/macro_regime.jsonl`

**Schema v1.0 (tägliches Append, Trading-Days only):**

```jsonl
{"date":"2026-04-20","hy_oas":3.15,"treasury_10y_2y":0.18,"ism_pmi":51.3,"ism_asof":"2026-04-01","regime_state":"normal","triggers_fired":[],"sparraten_factor":1.00,"schema_version":"1.0"}
```

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `date` | ISO-Date | Trading-Day (aligned mit `portfolio_returns.jsonl`) |
| `hy_oas` | Float (%) | FRED-Serie `BAMLH0A0HYM2` — Release-Day-Wert (siehe As-of-Policy) |
| `treasury_10y_2y` | Float (%) | FRED-Serie `T10Y2Y` — Release-Day-Wert |
| `ism_pmi` | Float | FRED-Serie `NAPM` — **T+1-Wert** (Monthly → As-of-Policy) |
| `ism_asof` | ISO-Date | Tatsächliches Release-Datum der ISM-Publikation (Transparenz-Feld) |
| `regime_state` | Enum | `normal` \| `risk_off` |
| `triggers_fired` | Array | Welche Trigger-Regeln heute feuerten (z.B. `["hy_oas_above_threshold"]`) |
| `sparraten_factor` | Float | 1.00 = normal, <1.00 = Risk-Off-Modulator (exakter Wert aus Trigger-Regeln) |
| `schema_version` | String | "1.0" |

**Backfill-Policy:** Historische Serien werden in separatem Bootstrap-Archiv (`05_Archiv/macro_regime_historical.jsonl`) abgelegt, nicht in Live-Stream. Live-Stream startet mit Go-Live-Datum.

#### 3.2.3 Backtest-Tool: `03_Tools/macro_regime_backtest.py`

**Zweck:** Einmaliger Pre-Activation-Backtest zur Threshold-Kalibrierung.

**Inputs:**
- FRED-Historie (HY-OAS ab 1996, T10Y2Y ab 1976, ISM ab 1948 — effektiver Startpunkt: **1996** = intersection)
- SPY-Historie (ab 1993 via Yahoo/Shibui) als Satelliten-Return-Proxy
- Grid-Search-Parameter-Ranges:
  - `hy_oas_threshold`: 350 / 400 / 450 / 500 / 550 bps
  - `curve_inversion_threshold`: -25 / 0 / +25 bps
  - `ism_floor`: 45 / 47 / 48 / 50
  - `persistence_months`: 1 / 2 / 3
  - `logic_operator`: OR (any 1 trigger) / AND-of-2 (2-of-3) / AND-all (all 3)
  - `sparraten_factor_riskoff`: 0.50 / 0.70 / 0.80

**Output:**
- CSV/Markdown-Report mit Performance-Metriken pro Kombination:
  - **Primär:** Sparraten-Utility (= vermiedener Kauf-Cost auf Pre-Drawdown-Hochs, definiert in §3.3.1)
  - **Sekundär-Constraint:** MaxDD muss ≤ MaxDD-Unfiltered sein (Regime-Filter darf Drawdown nicht erhöhen)
  - **Diagnostik:** Trigger-Frequency (% der Zeit in risk_off), Hit-Rate (% der Trigger gefolgt von SPY-Drawdown >10% binnen 6M)
- Sensitivitätsanalyse: Robustheit der Top-3-Kombinationen über Sub-Perioden 1996-2007 / 2008-2019 / 2020-2026

**Disziplin gegen Regime-Snooping (Codex):**
- **Nicht** Point-Optimum wählen, sondern Parameter-Region mit stabiler Performance über alle Sub-Perioden
- Konservative Default-Präferenz: bei Tie → höhere Threshold, längere Persistenz, niedrigerer Sparraten-Faktor-Reduktion
- Final-Thresholds werden in **CORE-MEMORY §5 + INSTRUKTIONEN §31** dokumentiert mit expliziter Audit-Trail (welcher Backtest-Run, welches Datum, welche Sub-Perioden-Stabilität)

#### 3.2.4 Trigger-Regeln: Neue INSTRUKTIONEN §31

**Strukturell (Werte werden post-Backtest gefüllt):**

```markdown
## §31 Macro-Regime-Filter (Sparraten-Modulation)

### 31.1 Serien-Inputs
- HY-OAS (FRED: BAMLH0A0HYM2) — Daily, Release-Day-Wert
- 10Y-2Y Treasury-Curve (FRED: T10Y2Y) — Daily, Release-Day-Wert
- ISM Manufacturing PMI (FRED: NAPM) — Monthly, T+1 nach Veröffentlichung

### 31.2 Trigger-Regeln (mechanisch, ex ante)
[POST-BACKTEST FÜLLEN]
Beispiel-Form:
Regime = risk_off WENN:
  (HY-OAS > X bps PERSISTENT über Y Monate) UND
  (ISM < Z PERSISTENT über Y Monate)
SONST normal.

### 31.3 Sparraten-Modulation
risk_off → Sparraten-Faktor [POST-BACKTEST]; Rest in Cash-Reserve
normal → Sparraten-Faktor 1.00

### 31.4 Override / Kill-Switch
- Kein diskretionärer Override außer via Versions-Bump (§31 v1.1+)
- Threshold-Änderung erfordert (1) neuen Backtest-Run, (2) CORE-MEMORY §5 Audit-Eintrag, (3) STATE.md-Update
- Kill-Switch: explizite §31-Deaktivierung erfordert gleiche Prozedur

### 31.5 Daily-Run-Pflicht
Nach Tavily-Morning-Briefing-Trigger: macro_regime.jsonl append, STATE.md-Regime-Zeile aktualisieren
```

### 3.3 Integration in bestehende Backtest-Infrastruktur

#### 3.3.1 Forward-Tagging (Angle 1)
`portfolio_returns.jsonl` Schema v1.0 bleibt unverändert — Regime-Tag wird **beim Analysis-Zeitpunkt** via Join auf `macro_regime.jsonl` (auf `date`) hinzugefügt. Kein Schema-Bruch.

**Implementations-Hinweis:** `portfolio_risk.py --persist daily` muss NICHT modifiziert werden. Read-Side-Join in `risk-metrics-calculation` Skill (Interim-Gate 2027-10-19).

**Sparraten-Utility-Definition (für Grid-Search-Ziel):**
> Sparraten-Utility = Σ über alle Monate t: (Durchschnittskurs_Satelliten_t × Sparraten_Faktor_t) verglichen mit (Durchschnittskurs_Satelliten_t × 1.00).
> Utility positiv, wenn Regime-Filter Käufe auf Phasen verschoben hat, die im 6M-Forward-Fenster niedrigere Durchschnittskurse hatten.

Proxy im Backtest: SPY-Monats-Close statt Satelliten-Durchschnittskurs (SPY ab 1993 verfügbar, Satelliten-Gewichtung ändert sich über Zeit — Proxy-Ansatz vermeidet Historical-Constituent-Bias).

#### 3.3.2 Historischer Backtest als Pre-Activation-Gate (Angle 2)
**Vor** INSTRUKTIONEN §31-Aktivierung:
1. `macro_regime_backtest.py` läuft Grid-Search über 1996-2026
2. Top-3 robuste Parameter-Regionen identifiziert (Sensitivitätsfenster)
3. Konservativste Kombination gewählt (höhere Thresholds, niedrigerer Sparraten-Faktor-Reduktion)
4. Gewählte Thresholds in §31.2 + §31.3 eingetragen
5. CORE-MEMORY §5 Audit-Eintrag mit Backtest-Timestamp und Sub-Perioden-Metriken
6. **Dann** Go-Live: Daily-Append von `macro_regime.jsonl` startet, Sparraten-Modulation scharf

#### 3.3.3 Interim-Gate-Mehrwert (2027-10-19)
Beim 18-Monats-Dry-Run `risk-metrics-calculation`:
- Regime-konditionierte Portfolio-Performance (normal vs. risk_off-Phasen)
- Regime-konditionierte DEFCON-Score-Hit-Rate (funktioniert Scoring in Risk-Off schlechter?)
- Validierung: Hat Regime-Filter Drawdowns tatsächlich reduziert (vs. unfiltered-Szenario)?

### 3.4 Red-Flag-Mitigation (aus Codex-Review)

| Red Flag | Mitigation in Design |
|----------|---------------------|
| Kalibrierungs-Rauschen (ISM/HY-OAS/Curve revidieren) | As-of-Policy (c) Hybrid: Release-Day für Daily, T+1 für Monthly. Keine Revisions-Rewrites in `macro_regime.jsonl` — First-Release-Werte bleiben stehen, Transparenz via `ism_asof`-Feld. |
| Kadenz-Mismatch (Quartals-Analyse hinkt Macro-Wechseln nach) | Sparraten-Modulation ist **monatlich** (vor monatlicher Sparplan-Ausführung), nicht quartalsweise. Kein Mismatch bei monatlichem `macro_regime.jsonl`-Read. |
| False-Positive (1 Serie stresst, 8/11 Fundamentals clean) | `logic_operator` im Grid-Search bevorzugt AND-of-2 (Persistenz + Multi-Signal) über OR. Dokumentiert in §31.2. |
| Governance-Last (diskretionäres Macro-Timing unter anderem Namen) | §31.4: kein Override außer via Versions-Bump + Audit. Versions-Bump ist 3-Schritt-Prozedur (Backtest + Audit + STATE-Update). Macht diskretionäres Timing teurer als es wert ist. |
| Regime-Snooping (wenige Krisenepisoden, retrospektive Thresholds) | Konservative Params + Sensitivitätsfenster statt Point-Optimum. Sub-Perioden-Validierung (1996-2007 / 2008-2019 / 2020-2026). |
| Frequency-Mixing (ISM nicht täglich) | Schema hat `ism_asof`-Feld; ISM-Wert bleibt zwischen Releases konstant. Explizit dokumentiert in §3.2.2. |
| SPY 1993+ Kalibrierung | Proxy-Ansatz dokumentiert: Backtest nutzt SPY als Satelliten-Return-Proxy, nicht echten investierbaren Benchmark für aktuelles Portfolio. Limitation in CORE-MEMORY §5 vermerkt. |

### 3.5 Akzeptanz-Kriterien 5b
- [ ] FRED-API-Key bezogen, in `.env` gespeichert (nicht committed)
- [ ] FRED-Integration (α MCP oder β Python-Lib) funktionsfähig, Daily-Fetch von HY-OAS/T10Y2Y/ISM erfolgreich
- [ ] `05_Archiv/macro_regime.jsonl` — Schema v1.0 dokumentiert, erster Record geschrieben
- [ ] `05_Archiv/macro_regime_historical.jsonl` — Backfill 1996-2026 erstellt
- [ ] `03_Tools/macro_regime_backtest.py` — Grid-Search läuft, Report generiert
- [ ] Top-3 Parameter-Regionen identifiziert, Sensitivitätsfenster dokumentiert
- [ ] Konservative Parameter-Wahl begründet und in INSTRUKTIONEN §31 eingetragen
- [ ] CORE-MEMORY §5 Audit-Eintrag mit Backtest-Timestamp + Sub-Perioden-Metriken
- [ ] STATE.md aktualisiert (neue Zeile: „Regime-State" in System-Zustand-Sektion)
- [ ] Daily-Run in Morning-Briefing-Trigger-Skript integriert
- [ ] Interim-Gate-Nutzung dokumentiert (wie Regime-Tags in `risk-metrics-calculation` eingelesen werden)

### 3.6 Out of Scope (5b)
- **Keine** per-Ticker-Macro-Sensitivitäten (Option C — explizit abgelehnt)
- **Keine** Position-Entscheidungen basierend auf Macro (nur Sparraten-Ebene)
- **Kein** Macro-Input in DEFCON-Score-Berechnung
- **Keine** Macro-FLAG-Events (Regime-Wechsel ist keine FLAG-Aktivierung)
- **Kein** Override des Sparraten-Nenners aus STATE.md — `sparraten_factor` multipliziert nur die resultierenden Einzel-Raten

---

## 4. Sequencing & Dependencies

### 4.1 Vorbedingung (Gate)
- [ ] Tavily-Go-Live stabil seit mindestens 3 Tagen (per SESSION-HANDOVER.md)

### 4.2 Parallelisierung
5a und 5b starten parallel nach Gate. Gemeinsamer Checkpoint: beide Sub-Tracks haben eigene Akzeptanz-Kriterien.

### 4.3 Abhängigkeiten
- **5a ↔ 5b:** keine technische Abhängigkeit
- **5a → Existing System:** EdgarTools-Install muss Python-Env nicht brechen (defeatbeta-MCP-Koexistenz prüfen)
- **5b → Existing System:** `macro_regime.jsonl` ist neuer File, kein Schema-Bruch bei `portfolio_returns.jsonl`

### 4.4 Rollback-Strategie
- **5a Rollback:** Skill-Verzeichnis zurück nach `_extern/` verschieben, `pip uninstall edgartools`. Kein Daten-Impact.
- **5b Rollback vor §31-Aktivierung:** Backtest-Tool behalten, `macro_regime.jsonl` stoppen. Kein User-facing-Impact.
- **5b Rollback nach §31-Aktivierung:** §31-Deaktivierung via Versions-Bump (§31 v0.0 = Filter aus, `sparraten_factor` hart 1.00). Historische `macro_regime.jsonl`-Records bleiben als Dokumentation.

---

## 5. Open Questions / Implementation-Plan-Entscheidungen

Folgende Punkte werden im nachgelagerten **Implementation-Plan** (via `writing-plans` Skill) entschieden, nicht hier:

1. **5b-FRED-Zugriff:** α MCP (`dracepj/fred-mcp`) vs. β Python-Lib (`fredapi`) — Entscheidung basierend auf MCP-Maintenance-Status und Integrations-Aufwand
2. **5b-Grid-Search-Runtime:** Abschätzung der Backtest-Laufzeit (erwartet <30 Min bei Full-Grid auf 30-Jahre-Daily-Data)
3. **5b-Backfill-Bootstrap:** Einmaliger Pull vs. inkrementeller Import für `macro_regime_historical.jsonl`
4. **5a-Identity-String:** Genauer Wortlaut `set_identity()` im Skill-Init (Privacy-Review: Email `tobikowa90@gmail.com` ist bereits in Memory + STATE)
5. **5a-Kollisionscheck:** Existiert `01_Skills/sec-edgar-skill/` bereits als Leerverzeichnis? Namens-Kollision mit `_extern/sec-edgar-skill/` beim Promote?

---

## 6. Erfolgs-Definition (End-of-Track-5)

**5a erfolgreich, wenn:**
- In einem realen Daten-Konflikt-Fall (US-Ticker) liefert EDGAR-Skill XBRL-Schiedsquelle mit ≤200 Tokens via `.to_context()`
- CORE-MEMORY §5 zeigt mindestens einen Audit-Eintrag mit EDGAR-Resolve-Nutzung innerhalb 90 Tagen post-Aktivierung

**5b erfolgreich, wenn:**
- §31 aktiviert mit Backtest-evidenzbasierten Thresholds
- Sub-Perioden-Sensitivitätsfenster dokumentiert
- Daily-Append-Pipeline läuft seit mindestens 30 Tagen fehlerfrei
- STATE.md zeigt aktuellen Regime-State mit jedem Refresh
- Interim-Gate 2027-10-19 liefert Regime-konditionierte Performance-Metriken (Validierung der Filter-Effektivität)

**Track 5 Gesamt erfolgreich, wenn:**
- Keine Regression in bestehenden Workflows (`!Analysiere`, Morning-Briefing, backtest-ready-forward-verify)
- Keine Überschreitung des Sparraten-Nenners (8.0) durch Regime-Modulation
- CORE-MEMORY und STATE.md spiegeln beide Sub-Tracks konsistent

---

## 7. Referenzen

- `00_Core/SESSION-HANDOVER.md` §Track 5 (Vorherige Codex-Empfehlung, 2026-04-19)
- `00_Core/CORE-MEMORY.md` §5 (Audit-Log-Eintrag nach Go-Live)
- `00_Core/INSTRUKTIONEN.md` §19 (API-Routing), §22 (Skill-Referenz), §31 (neu: Macro-Regime-Filter)
- `01_Skills/_extern/sec-edgar-skill/SKILL.md` (EdgarTools-Referenz-Skill)
- `05_Archiv/portfolio_returns.jsonl` Schema v1.0 (existing)
- `05_Archiv/score_history.jsonl` Schema (existing, unaffected)
- FRED-Serien: `BAMLH0A0HYM2` (HY-OAS), `T10Y2Y` (Treasury-Curve), `NAPM` (ISM PMI)

---

*🦅 Track-5-Spec v1.0 | 2026-04-20 | Co-Review: Claude (Opus 4.7) + Codex*
