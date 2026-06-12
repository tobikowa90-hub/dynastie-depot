# xlsx Smoke-Test Stufe 1 (Manual Post-Write-Validation)

**Zweck:** Nach jedem `openpyxl`-Write auf eine der drei xlsx-Dateien (§18-Sync-Welle) Post-Write-Integrität verifizieren, bevor `git add` der xlsx-Files erfolgt. Adressiert silent-Korruptions-Risiken (gebrochene Cross-Sheet-Formeln, Conditional-Formats, verlorene Charts/Pivots), die `openpyxl` ohne Fehler-Return verursachen kann.

**Spec-Anker:** `00_Core/INSTRUKTIONEN.md §18.7` (verpflichtend, fail-close, kein `--force`-Bypass).

**Trigger:** Jeder Score-/FLAG-/Sparraten-Change-Sync-Lauf (§18.1) der mindestens eine xlsx-Datei berührt. Nicht-xlsx-only-Tooling-Changes triggern den Smoke-Test nicht.

**Reihenfolge im Sync:** Nach Provenance-Gate §18.5 (P3.5 PASS), nach `openpyxl`-Write, **vor** `git add` der xlsx-Files.

---

## Scope

| Datei | Smoke-Test-Tiefe | Begründung |
|-------|------------------|------------|
| `03_Tools/Rebalancing_Tool` | **Voll** (Punkte A-F) | **9 Conditional Formats** (CF-Ranges) — hohes Korruptions-Risiko (Live-State 2026-06-12 v4.0-Roster + **exUSA-Re-Add**: 13 Satelliten + **6 ETF** [EXUS reaktiviert als R8]; CF 7→9: User-Edit +K5:K24 dataBar [Abw.%] +H25 [GESAMT-Check], +EXUS-Row-Shift; §C/§D-Zell-Ref-Reconcile 2026-06-12: Satelliten **R12-R24** [R5 Gold EWG2, **R6-R11 ETFs**], GESAMT R25, US-Exposure-Mirror **R4-R23** = Portfolio R5-R24; vorher 2026-06-07 Satelliten R11-R23/R6-R10 ETF/19 Pos/7 CF) |
| `03_Tools/Satelliten_Monitor` | **Voll** (Punkte A-F) | 11 Conditional Formats (5 Sheet `Satelliten Monitor`: L/M/N/O/R + 6 Sheet `QuickScreen Ampel`: Ampel-Coloring D/D-G/E/F/G/H, Umstrukturierung 2026-06-07) + §G SOLL-Σ-Check via Hook (Tier-Modell: `Σ satelliten_tier_raten[tier] == brokers.scalable.sparrate_eur` = 364€; Funded-Echo-Display layout-robust per Content-Scan, vorher fixe N19; vorher 2026-05-25 5 CF + flaches 285€-Modell) |
| `03_Tools/Watchlist_Ersatzbank_Monitor` | **Minimal-Check-Annex** (nur A + Existenz) | 0 Formeln, 0 CF — kein Korruptions-Risiko via openpyxl. Hochstufung in Voll-Smoke-Test erst sobald Excel-Formeln (`=...`) zur Watchlist hinzugefügt werden (file-pattern-driven Trigger, kein PIPELINE-Item-Backing). |

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

Sheet `Portfolio & Rebalancing`. Positionen R5-R24 (R5 Gold EWG2, **R6-R11 ETFs** [EXUS R8, exUSA-Re-Add 2026-06-12], **R12-R24 = 13 Satelliten**, R25 GESAMT). Per Satelliten-Zeile (R12-R24) verifizieren:

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `N12`-`N24` | DEFCON-Score-String | Format `'DEFCON X (NN)'`, X = aktueller DEFCON-Level, NN = aktueller Score; Platzhalter NOW/KYCCF/ZETA = `'DEFCON 3 (–) \| Neu …'` |
| `O12`-`O24` | FLAG-Status-Text | bei FLAG aktiv: `🔴 ... (Pfad-Note)`; sonst grün/leer |
| `P12`-`P24` | Sparrate-Output (Formel) | Formel-Resolve gegen erwartete effektive Tier-Rate des Tickers (Tier-Modell: Cross-Check gegen `01_Skills/dynastie-depot/config.yaml` `satelliten_tier_raten` × DEFCON/FLAG-Modulation) |

- ✅ **PASS:** Alle Pflicht-Zellen reflektieren den aktuellen Sync-Stand
- ❌ **FAIL:** Eine oder mehrere Pflicht-Zellen stale → openpyxl-Write hat nicht alle Zellen erreicht. STOP.

**US-Exposure-Sentinel-Set (Sheet `US-Exposure`):** Spiegel-Sheet (R4-R23 = Portfolio R5-R24, 1:1-Mirror; R24 = GESAMT). Sentinel-Pflicht-Checks zur Drift-Vermeidung bei Portfolio-Ticker-Range-Änderungen (Range erweitert 2026-06-12 exUSA-Re-Add EXUS-Einschub, vorher R4-R22 / 19 Pos):

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `US-Exposure!R4` (Spalten A-D) | `='Portfolio & Rebalancing'!A5/B5/F5/E5` | Erste Mirror-Zeile resolvet ohne `#REF!` (Portfolio R5 = EWG2 Gold) |
| `US-Exposure!R23` (Spalten A-D) | `='Portfolio & Rebalancing'!A24/B24/F24/E24` | Letzte Mirror-Zeile resolvet ohne `#REF!` (Portfolio R24 = letzter Satellit, aktuell ZETA) |
| `US-Exposure!R24 E` | `=SUM(E4:E23)` | Σ-US-Anteil € resolvet auf `> 0` (nicht 0/leer) |
| `US-Exposure!B26/B28` | `='Portfolio & Rebalancing'!…` / `='Parameter & Regeln'!B11` | US-Ist (B26) + US-Hard-Cap-Lookup (B28) resolvet (aktuell `0.63` = 63%); Cross-Ref-Existenz |

- ✅ **PASS:** R4 + R23 Mirror ohne `#REF!`, GESAMT-Σ (E24) > 0, US-Hard-Cap-Lookup löst auf
- ❌ **FAIL:** `#REF!` in R4/R23 (Portfolio-Range-Drift, Mirror gebrochen) ODER Σ = 0/leer (Σ-Aggregat verloren) ODER Hard-Cap-Lookup = `#REF!` (Parameter-Sheet umbenannt/verschoben). STOP.

### D. Pflicht-Zell-Cross-Check Satelliten-Monitor

Sheet `Satelliten Monitor`. Verifizieren:

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `O2` | Stand-Stempel | `Stand: YYYY-MM-DD ...` |
| `B3` | Header-Sparraten-Zeile | Tier-System (ab 06.06.2026): `Funded X€/Monat \| SOLL Y€/Monat \| Tier 1=40€, Tier 2=32€, Tier 3=18€ (DEFCON/FLAG überschreibt SOLL)` |
| `H3` | Eingefroren-Liste | Alle FLAG-Tickers mit Datum |
| `K3` | Ergebnis-Zeile | `● N Volle Tier-Rate  ● M D2-Sockelbetrag  ● K Eingefroren (Liste) \| Funded X€ / SOLL Y€` (●-Marker vereinheitlicht 2026-05-25) |
| `L<ticker>` (L7-L19) | Score-String | `'NN / DEFCON X'` pro Ticker-Zeile (13 Satelliten R7-R19; Platzhalter NOW/KYCCF/ZETA = `'[ausstehend]'`) |
| `M<ticker>` (M7-M19) | Δ-Note | aktueller Δ vs. Vorperiode |
| `N<ticker>` (N7-N19) | Status/FLAG-Text | mit Pfad-Note + ggf. Q-Verify-Pointer / PIPELINE-Item |
| `B22` | Legende-Header | `'LEGENDE & DATENQUALITÄT'` |
| `B25` | Legende Verifikations-Marker | `[~]` Schätzung Wissensbasis (plausibel) \| `[V]` Vollanalyse verifiziert \| `[TC]` Tariff-Check (statischer Legende-Text) |
| `B26` | Footer Eingefroren-Liste | Komplett, mit FLAG-Grund pro Ticker (Pattern: `● EINGEFROREN: <Ticker> (FLAG <Grund>, D<X>, Score <NN>) \| ...`) |
| `B27` | Footer Tier-System | Tier-Aufteilung (SOLL → Real): `● Tier 1 (SOLL 40€): <Ticker>... \| ● Tier 2 (SOLL 32€): ... \| ● Tier 3 (SOLL 18€): ... \| Funded Σ = ... \| SOLL Σ = ...` |
| Funded-Echo (Content-Scan) | Σ-Check Text-Sanity | Zelle(n) mit `'Funded … SOLL …'` (aktuell N20 `'→ Funded 210,00 € (SOLL 364,00 € …)'` + B3-Header; **keine** Excel-Formel; **layout-robust per Content-Scan** statt fixe Zelle — N19→N20-Drift bei Roster-Resize 2026-06-07; Σ-Verifikation per Hook-Punkt §G `_check_g_sparrate_sigma`) |

- ✅ **PASS:** Alle Pflicht-Zellen aktuell + Funded-Echo-Zelle präsent; Σ-Check-Verifikation erfolgt im Hook-Punkt §G (`01_Skills/dynastie-depot/config.yaml` SSoT → **Tier-Modell**: effektive Rate = `satelliten_tier_raten[tier] × DEFCON-Modulation × FLAG` [`flag=True→0`, `defcon∈{3,4}→voll`, `defcon=2→halb`, `defcon=1→0`]; **SOLL-Invariante** `Σ satelliten_tier_raten[tier] == cfg.brokers.scalable.sparrate_eur` = 364,00€; Funded-Echo = `Σ modulierte Raten` = 210,00€)
- ❌ **FAIL:** Pflicht-Zelle stale ODER Funded-Echo-Zelle fehlt/falsch ODER Hook-§G-SOLL-Σ-Check failed. STOP.

**Status-Marker-Konvention (P10, vereinheitlicht 2026-05-25):** `●` ersetzt die alten Emoji-Marker (🟢/🟡/🟠/🔴) konsistent in B3/H3/K3/B25/B26/N7-N18. Inhaltliche Klassifikation bleibt erhalten (Volle Rate / D2-Sockel / Eingefroren / FLAG), nur das Glyph ist neutral. Smoke-Test prüft Existenz der Pflicht-Zellen, nicht das Marker-Glyph.

### D2. QuickScreen-Ampel-Sheet Cross-Check (Satelliten_Monitor, Sheet 2)

Sheet `QuickScreen Ampel` (zweites Sheet im Satelliten-Monitor). 0 Formeln, **6 CF** (Ampel-Coloring D/D-G/E/F/G/H, neu ab 2026-06-07 Umstrukturierung — zählt in den §E-CF-Count 11) — Pflichtprüfung ist Struktur- + Ticker-Konsistenz gegen Hauptsheet:

| Zelle / Range | Inhalt | Erwartung |
|---------------|--------|-----------|
| `B5:I5` (Header-Row) | Spalten-Header: Ticker, Name, P/FCF Filter, ROIC Filter, Moat Filter, FLAG, Gesamt-Ampel, Nächster Schritt | 8 Spalten-Header in Row 5, alle besetzt (Sheet-Dims starten bei `B2`, Spalte A leer by-design) |
| `B6:B18` (Ticker-Range) | 13 Ticker (ASML, AVGO, MSFT, RMS, SU, BRK.B, V, TMO, APH, AMZN, NOW, KYCCF, ZETA) mit Ampel-Status pro Filter | **Cross-Check gegen `Satelliten Monitor`-Sheet `B7:B19`**: identisches Ticker-Set (Set-Gleichheit) |
| `B19` (Legende-Header) + Folge-Rows | LEGENDE-Block mit ●-Marker-Semantik (HALTEN / PRÜFEN / EINGEFROREN / Exception-Logik) | Header-Zelle `B19` enthält literal `'LEGENDE'` + Beschreibungs-Rows |

- ✅ **PASS:** R5-Header vollständig, R6-R18 Ticker-Set identisch zu Hauptsheet R7-R19 (Set-Gleichheit, nicht Order-Drift-tolerant), Legende-Block ab R19 präsent
- ❌ **FAIL:** Ticker-Drift zwischen QuickScreen R6-R18 und Hauptsheet R7-R19 (z.B. Hauptsheet hat ZETA aber QuickScreen nicht) → manueller xlsx-Edit hat eines der beiden Sheets vergessen. STOP.

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

## Minimal-Check-Annex (Watchlist_Ersatzbank_Monitor)

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
