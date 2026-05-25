# xlsx Smoke-Test Stufe 1 (Manual Post-Write-Validation)

**Zweck:** Nach jedem `openpyxl`-Write auf eine der drei xlsx-Dateien (§18-Sync-Welle) Post-Write-Integrität verifizieren, bevor `git add` der xlsx-Files erfolgt. Adressiert silent-Korruptions-Risiken (gebrochene Cross-Sheet-Formeln, Conditional-Formats, verlorene Charts/Pivots), die `openpyxl` ohne Fehler-Return verursachen kann.

**Spec-Anker:** `00_Core/INSTRUKTIONEN.md §18.7` (verpflichtend, fail-close, kein `--force`-Bypass).

**Trigger:** Jeder Score-/FLAG-/Sparraten-Change-Sync-Lauf (§18.1) der mindestens eine xlsx-Datei berührt. Nicht-xlsx-only-Tooling-Changes triggern den Smoke-Test nicht.

**Reihenfolge im Sync:** Nach Provenance-Gate §18.5 (P3.5 PASS), nach `openpyxl`-Write, **vor** `git add` der xlsx-Files.

---

## Scope

| Datei | Smoke-Test-Tiefe | Begründung |
|-------|------------------|------------|
| `03_Tools/Rebalancing_Tool_v3.4.xlsx` | **Voll** (Punkte A-F) | 249 Formeln + 6 Conditional Formats — hohes Korruptions-Risiko (Live-State 2026-05-25 post User-Update; vorher 218/6, drift via Q-Spalten-Erweiterung + R28-Row) |
| `03_Tools/Satelliten_Monitor_v2.0.xlsx` | **Voll** (Punkte A-F) | 13 Formeln + 5 Conditional Formats + §G Σ-Check via Hook (`brokers.scalable.sparrate_eur`-Anker, Live-State 2026-05-25 post User-Update; Σ-Check-Lokus per Variante G zu Hook verlagert, vorher Excel-Text-Sanity N19) |
| `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx` | **Minimal-Check-Annex** (nur A + Existenz) | 0 Formeln, 0 CF — kein Korruptions-Risiko via openpyxl. Hochstufung in Voll-Smoke-Test erst sobald Excel-Formeln (`=...`) zur Watchlist hinzugefügt werden (file-pattern-driven Trigger, kein PIPELINE-Item-Backing). |

---

## 6-Punkte-Checklist (pro Voll-Scope-Datei)

Reihenfolge ist verpflichtend. Bei jedem Fail-Signal: **STOP**, kein `git add`, Recovery durch Re-Edit des openpyxl-Write-Scripts. Kein `--force`-Bypass (analog §18.5-Pattern).

### A. Open-Repair-Prompt

Datei in Excel-Desktop öffnen.

- ✅ **PASS:** Datei öffnet sauber, kein Repair-Dialog
- ❌ **FAIL:** Excel zeigt "Wir haben Probleme mit einem Inhalt … entdeckt. Möchten Sie versuchen, soviel wie möglich wiederherzustellen?" → openpyxl hat strukturelle Inkonsistenz erzeugt. STOP.

### B. Formel-Fehler-Scan

In Excel: `Strg+F` → Suchfeld → für jeden der vier Patterns einzeln suchen über alle Sheets:

- `#REF!`
- `#NAME?`
- `#VALUE!`
- `#N/A`

Empfehlung: "Suchen in: Arbeitsmappe" + "Suchen: Werte".

- ✅ **PASS:** Kein Treffer für alle vier Patterns
- ❌ **FAIL:** Mindestens ein Treffer → gebrochene Formel-Referenz oder fehlende Daten-Quelle. STOP.

**Toleranz-Ausnahme:** `#N/A` ist akzeptabel **nur** wenn die Zelle explizit als `=NA()` definiert ist (intentionale Lücken-Markierung) und das Pattern vor dem Sync schon vorhanden war.

### C. Pflicht-Zell-Cross-Check Rebalancing-Tool

Sheet `Portfolio & Rebalancing`. Per Ticker-Zeile (R18-R28) verifizieren:

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `N18`-`N28` | DEFCON-Score-String | Format `'DEFCON X (NN)'`, X = aktueller DEFCON-Level, NN = aktueller Score |
| `O18`-`O28` | FLAG-Status-Text | bei FLAG aktiv: `🔴 ... (Pfad-Note)`; sonst grün/leer |
| `P18`-`P28` | Sparrate-Output (Formel) | Formel-Resolve gegen erwartete Sparrate des Tickers (Cross-Check gegen `01_Skills/dynastie-depot/config.yaml`) |
| `R2` | Datum-Stempel | `Stand: YYYY-MM-DD` aktuell, ggf. mit Tagesdatum-Wechsel |

- ✅ **PASS:** Alle Pflicht-Zellen reflektieren den aktuellen Sync-Stand
- ❌ **FAIL:** Eine oder mehrere Pflicht-Zellen stale → openpyxl-Write hat nicht alle Zellen erreicht. STOP.

**US-Exposure-Sentinel-Set (P14, Sheet `US-Exposure`):** Spiegel-Sheet (R4-R20 = Portfolio R5-R21, 1:1-Mirror). Sentinel-Pflicht-Checks zur Drift-Vermeidung bei Portfolio-Ticker-Range-Änderungen:

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `US-Exposure!R4` (Spalten A-D) | `='Portfolio & Rebalancing'!A5/B5/F5/E5` | Erste Mirror-Zeile resolvet ohne `#REF!` (Portfolio R5 = EUWAX Gold) |
| `US-Exposure!R20` (Spalten A-D) | `='Portfolio & Rebalancing'!A21/B21/F21/E21` | Letzte Mirror-Zeile resolvet ohne `#REF!` (Portfolio R21 = letzter Ticker, aktuell AMZN) |
| `US-Exposure!R21 E` | `=SUM(E4:E20)` | Σ-US-Anteil € resolvet auf `> 0` (nicht 0/leer) |
| `US-Exposure!R25 B` | `='Parameter & Regeln'!B11` | US-Hard-Cap-Lookup resolvet (aktuell `0.63` = 63%); Cross-Ref-Existenz |

- ✅ **PASS:** R4 + R20 Mirror ohne `#REF!`, R21 E Σ > 0, R25 B löst zum aktuellen US-Hard-Cap-Wert auf
- ❌ **FAIL:** `#REF!` in R4/R20 (Portfolio-Range-Drift, Mirror gebrochen) ODER R21 E = 0/leer (Σ-Aggregat verloren) ODER R25 B = `#REF!` (Parameter-Sheet umbenannt/B11 verschoben). STOP.

### D. Pflicht-Zell-Cross-Check Satelliten-Monitor

Sheet `Satelliten Monitor`. Verifizieren:

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `O2` | Stand-Stempel | `Stand: YYYY-MM-DD ...` |
| `B3` | Header-Sparraten-Zeile | `D3/D4-Rate: X€ \| D2-Sockelbetrag: Y€ \| Nenner Z (Pfad-Note)` |
| `H3` | Eingefroren-Liste | Alle FLAG-Tickers mit Datum |
| `K3` | Ergebnis-Zeile | `● N Voll  ● M D2-Sockelbetrag  ● K Eingefroren (Liste)` (●-Marker vereinheitlicht 2026-05-25, vorher 🟢/🟠/🔴) |
| `L<ticker>` | Score-String | `'NN / DEFCON X'` pro Ticker-Zeile |
| `M<ticker>` | Δ-Note | aktueller Δ vs. Vorperiode |
| `N<ticker>` | Status/FLAG-Text | mit Pfad-Note + ggf. Q-Verify-Pointer / PIPELINE-Item |
| `B24` | Legende Verifikations-Marker | `[~]` Schätzung Wissensbasis (plausibel) \| `[V]` Vollanalyse verifiziert \| `[TC]` Tariff-Check abgeschlossen (statischer Legende-Text, keine Ticker-Liste) |
| `B25` | Footer Eingefroren-Liste | Komplett, mit FLAG-Grund pro Ticker (Pattern: `● EINGEFROREN: <Ticker> (FLAG <Grund>, D<X>, Score <NN>) \| ...`) |
| `B26` | Footer Volle-Rate-Liste + Nenner-Aufteilung | Aufteilung Volle-Rate (38,00€) / D2-Sockelbetrag (19,00€) / Eingefroren (0€) mit Ticker-Listen + Nenner-Formel (Pattern: `● Volle Rate 38,00€ (N Positionen): <Ticker>... \| ● D2-Sockelbetrag 19,00€ (M): <Ticker>... \| ● Eingefroren 0€ (K): <Ticker>... \| Nenner ...`) |
| `N19` | Σ-Check Text-Sanity | Literal `'→ muss = 285,00 €'` (Sanity-Echo, **keine** Excel-Formel; Σ-Verifikation per Hook-Punkt §G `_check_g_sparrate_sigma` — Mapping config.yaml SSoT) |

- ✅ **PASS:** Alle Pflicht-Zellen aktuell + `N19` Sanity-Text literal präsent; Σ-Check-Verifikation erfolgt im Hook-Punkt §G (`01_Skills/dynastie-depot/config.yaml` SSoT → `derive_rate(flag, defcon)`-Mapping: `flag=True→0€`, `flag=False+defcon∈{3,4}→38€`, `flag=False+defcon=2→19€` → `Σ == cfg.brokers.scalable.sparrate_eur` = 285,00€)
- ❌ **FAIL:** Pflicht-Zelle stale ODER `N19`-Sanity-Text fehlt/falsch ODER Hook-§G-Σ-Check failed. STOP.

**Status-Marker-Konvention (P10, vereinheitlicht 2026-05-25):** `●` ersetzt die alten Emoji-Marker (🟢/🟡/🟠/🔴) konsistent in B3/H3/K3/B25/B26/N7-N18. Inhaltliche Klassifikation bleibt erhalten (Volle Rate / D2-Sockel / Eingefroren / FLAG), nur das Glyph ist neutral. Smoke-Test prüft Existenz der Pflicht-Zellen, nicht das Marker-Glyph.

### D2. QuickScreen-Ampel-Sheet Cross-Check (Satelliten_Monitor_v2.0.xlsx, Sheet 2)

Sheet `QuickScreen Ampel` (zweites Sheet im Satelliten-Monitor). 0 Formeln, 0 CF — Pflichtprüfung ist Struktur- + Ticker-Konsistenz gegen Hauptsheet:

| Zelle / Range | Inhalt | Erwartung |
|---------------|--------|-----------|
| `B5:I5` (Header-Row) | Spalten-Header: Ticker, Name, P/FCF Filter, ROIC Filter, Moat Filter, FLAG, Gesamt-Ampel, Nächster Schritt | 8 Spalten-Header in Row 5, alle besetzt (Sheet-Dims starten bei `B2`, Spalte A leer by-design) |
| `B6:B17` (Ticker-Range) | 12 Ticker (ASML, AVGO, MSFT, COST, RMS, VEEV, SU, BRK.B, V, TMO, APH, AMZN) mit Ampel-Status pro Filter | **Cross-Check gegen `Satelliten Monitor`-Sheet `B7:B18`**: identisches Ticker-Set (Set-Gleichheit) |
| `B19` (Legende-Header) + `B20:B23` (Erklärung) | LEGENDE-Block mit ●-Marker-Semantik (HALTEN / PRÜFEN / EINGEFROREN / Exception-Logik) | Header-Zelle `B19` enthält literal `'LEGENDE'` + 4 Beschreibungs-Rows `B20:B23` |

- ✅ **PASS:** R5-Header vollständig, R6-R17 Ticker-Set identisch zu Hauptsheet R7-R18 (Set-Gleichheit, nicht Order-Drift-tolerant), Legende-Block ab R19 präsent
- ❌ **FAIL:** Ticker-Drift zwischen QuickScreen R6-R17 und Hauptsheet R7-R18 (z.B. Hauptsheet hat AMZN aber QuickScreen nicht) → manueller xlsx-Edit hat eines der beiden Sheets vergessen. STOP.

### E. Conditional-Format-Stichprobe

Pro Voll-Scope-Datei drei zufällige Zellen mit Color-Coding sichten (z.B. Rebal: DEFCON-Spalte N10-N21, FLAG-Spalte O10-O21, Sparrate P10-P21 — Sat: K3 Ergebnis-Zeile, L7-L18 Score-String, N7-N18 Status-Marker):

- ✅ **PASS:** Color-Coding entspricht dem erwarteten Wert (z.B. DEFCON 1 = rot, DEFCON 4 = grün)
- ❌ **FAIL:** Color-Coding fehlt komplett oder Farbe passt nicht zum Wert → Conditional-Format wurde von `openpyxl`-Write zerstört. STOP.

**Hinweis:** Volle Conditional-Format-Inventur (5-6 Regeln pro Datei) ist Stufe-2-Pflicht (siehe Roadmap unten). Stufe 1 begnügt sich mit 3-Zellen-Stichprobe.

### F. Read-only-Close-Verify

Datei **ohne Save** schließen (`X`-Button → "Nicht speichern" bei Prompt).

- ✅ **PASS:** Kein "Möchten Sie speichern?"-Prompt erzwingt Save → keine versehentliche Smoke-Test-Mutation
- ❌ **FAIL:** Speicher-Prompt erscheint trotz "Nicht-Save"-Intent → ungewollte Cell-Mutation während Smoke-Test (z.B. durch Click in Formel-Bar). Bei Schließen ohne Save: kein Schaden. Bei versehentlichem Save: openpyxl-Write neu ausführen.

---

## Minimal-Check-Annex (Watchlist_Ersatzbank_Monitor_v1.1.xlsx)

Aktuell nur:

- ✅ Datei öffnet ohne Repair-Prompt (Punkt A)
- ✅ Datei existiert + ist lesbar (`ls 03_Tools/Watchlist_*.xlsx` returns Pfad)

Punkte B-F entfallen (0 Formeln, 0 Conditional Formats — kein Korruptions-Risiko via openpyxl). Hochstufung in Voll-Smoke-Test erst wenn Excel-Formeln (`=...`) zur Watchlist hinzugefügt werden (Status-Ampel-Werte sind aktuell Plain-Text, kein Korruptions-Risiko via openpyxl-Write). Kein konkretes PIPELINE-Backing — Trigger ist file-pattern-driven (Formel-Count > 0 bei nächstem Smoke-Test-Probe-Lauf).

---

## Excel-Desktop-Fallback (Linux/Remote-Session ohne lokale Excel-Installation)

Bei nicht-verfügbarer Excel-Desktop-Installation:

| Punkt | Fallback |
|-------|----------|
| **A** | `python -c "import openpyxl; wb=openpyxl.load_workbook('<file>', data_only=False); print('OK')"` — kein Exception + kein Warning auf stderr = PASS. **Warning-Operationalisierung:** jede `UserWarning` / `DeprecationWarning` aus openpyxl auf stderr gilt als Fail-Signal und muss vor PASS-Verdict per `--force`-freier Investigation aufgelöst werden (z.B. Pivot-Skip-Warning = strukturelle Korruption). |
| **B** | Python-Loop: `for ws in wb: for row in ws: for c in row: assert not (isinstance(c.value,str) and c.value in {'#REF!','#NAME?','#VALUE!','#N/A'})` — falls Toleranz-Ausnahme für `=NA()`-Zellen relevant: Cell-Pattern-Compare statt Value-Compare. |
| **C / D** | Manuell unverändert via `openpyxl`-Read auf die Pflicht-Zellen — die Zell-Adressen sind im Fallback identisch. |
| **E** | `len(ws.conditional_formatting._cf_rules)` vor `openpyxl`-Write notieren + nach Write re-verifizieren. Count-Diff = Fail. |
| **F** | Im Fallback nicht anwendbar (kein interaktiver Open-Close-Cycle). Entfällt. |

**Validitäts-Klausel:** Der Excel-Fallback ersetzt Stufe-1 **nur partiell**. Punkte E + F prüfen Rendering- und UI-Verhalten, das `openpyxl`-Re-Read nicht abdecken kann (z.B. CF-Formel die syntaktisch valide ist aber durch Excel anders gerendert wird). Ein vollständiger Smoke-Test-PASS ohne Sichtprüfung auf Excel-Desktop gilt als **partiell bestanden** — bei Score-/FLAG-Sync mit operativer Sparraten-Konsequenz (Lookup-Werte für nächsten Sparplan-Lauf) sollte die Sichtprüfung beim nächsten Excel-Zugriff nachgezogen werden. Reine Tooling-/Spec-Changes ohne operative Sparraten-Wirkung sind mit partiellem Fallback abnahmefähig.

---

## Stufe-2-Roadmap (DEFERRED)

Falls Stufe-1-Manual-Disziplin sich als unzureichend erweist (z.B. silent-Skip eines Smoke-Test-Laufs, der zu Daten-Drift führt), Promotion auf programmatisches Audit-Modul:

- `03_Tools/system_audit/checks/xlsx_integrity.py` (symmetrisch zu existierenden 19 system_audit-Checks)
- `CheckResult` + `FailureDetail`-Pattern wie `score_event_parity.py` / `header_freshness.py`
- SHA256-Hash-Snapshot + Diff-Wächter für nicht-erwartete-Touch-Zellen (Strukturzellen die nie verändert werden sollten — Header, Formelzellen, Pivot-Source-Refs)
- Auto-Integration in `system_audit.py --full`-Lauf

**Re-Activation-Trigger:** (a) erster realer Daten-Drift-Vorfall durch übersprungenen Smoke-Test, ODER (b) erweiterte xlsx-Toolchain (>3 Voll-Scope-Files macht Manual-Disziplin unwirtschaftlich), ODER (c) Konsolidierungs-Slot mit explizitem xlsx-Integrity-Refactor.

---

## Memory-Pointer (nicht-normativ)

`feedback_xlsx_tools_in_sync_set.md` enthält `openpyxl`-Code-Snippets für die Pflicht-Zell-Edits (Konvenienz-Helper für den Schreib-Schritt). Diese Memory ist **nicht-normativ** für die Pflicht-Zell-Liste — bei Drift gegen die Spec gewinnt **immer** §18.1 (Sync-Vertrag) und §18.7 (Verify-Pflicht, dieses Dokument). Die Memory-Datei darf nur als Edit-Pattern-Helper zitiert werden, nie als Pflicht-Zell-SSoT.

---

*Stand: 2026-05-11 (Initial-Erstellung Stufe 1 — Codex-Sparring-Konfidenz 96% bei Variante A verbindlich + §18 v2.3→v2.4)*
