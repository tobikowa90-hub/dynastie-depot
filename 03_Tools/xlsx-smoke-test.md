# xlsx Smoke-Test Stufe 1 (Manual Post-Write-Validation)

**Zweck:** Nach jedem `openpyxl`-Write auf eine der drei xlsx-Dateien (§18-Sync-Welle) Post-Write-Integrität verifizieren, bevor `git add` der xlsx-Files erfolgt. Adressiert silent-Korruptions-Risiken (gebrochene Cross-Sheet-Formeln, Conditional-Formats, verlorene Charts/Pivots), die `openpyxl` ohne Fehler-Return verursachen kann.

**Spec-Anker:** `00_Core/INSTRUKTIONEN.md §18.7` (verpflichtend, fail-close, kein `--force`-Bypass).

**Trigger:** Jeder Score-/FLAG-/Sparraten-Change-Sync-Lauf (§18.1) der mindestens eine xlsx-Datei berührt. Nicht-xlsx-only-Tooling-Changes triggern den Smoke-Test nicht.

**Reihenfolge im Sync:** Nach Provenance-Gate §18.5 (P3.5 PASS), nach `openpyxl`-Write, **vor** `git add` der xlsx-Files.

---

## Scope

| Datei | Smoke-Test-Tiefe | Begründung |
|-------|------------------|------------|
| `03_Tools/Rebalancing_Tool_v3.4.xlsx` | **Voll** (Punkte A-F) | 218 Formeln + 6 Conditional Formats — hohes Korruptions-Risiko |
| `03_Tools/Satelliten_Monitor_v2.0.xlsx` | **Voll** (Punkte A-F) | 12 Formeln + 5 Conditional Formats + Σ-Check-Formel im Footer |
| `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx` | **Minimal-Check-Annex** (nur A + Existenz) | 0 Formeln, 0 CF — kein Korruptions-Risiko via openpyxl. Hochstufung in Voll-Smoke-Test erst nach Watchlist-Tool-Update (offenes PIPELINE-Item, Sekundär-Priorität). |

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

### D. Pflicht-Zell-Cross-Check Satelliten-Monitor

Sheet `Satelliten Monitor`. Verifizieren:

| Zelle | Inhalt | Erwartung |
|-------|--------|-----------|
| `O2` | Stand-Stempel | `Stand: YYYY-MM-DD ...` |
| `B3` | Header-Sparraten-Zeile | `D3/D4-Rate: X€ \| D2-Sockelbetrag: Y€ \| Nenner Z (Pfad-Note)` |
| `H3` | Eingefroren-Liste | Alle FLAG-Tickers mit Datum |
| `K3` | Ergebnis-Zeile | `🟢 N Voll  🟠 M D2  🔴 K Eingefroren (Liste)` |
| `L<ticker>` | Score-String | `'NN / DEFCON X'` pro Ticker-Zeile |
| `M<ticker>` | Δ-Note | aktueller Δ vs. Vorperiode |
| `N<ticker>` | Status/FLAG-Text | mit Pfad-Note + ggf. Q-Verify-Pointer / PIPELINE-Item |
| `B24` | Footer Eingefroren-Liste | Komplett, mit FLAG-Grund pro Ticker |
| `B25` | Footer Volle-Rate-Liste | Mit Σ-Check-Formel (z.B. `7×38,00 + 1×19,00 + 3×0 = 285,00€ ✓`) — Σ muss aufgehen |

- ✅ **PASS:** Alle Pflicht-Zellen aktuell + Σ-Check-Formel im Footer `B25` resolvet ohne Fehler
- ❌ **FAIL:** Pflicht-Zelle stale ODER Σ-Check schlägt rechnerisch fehl. STOP.

### E. Conditional-Format-Stichprobe

Pro Voll-Scope-Datei drei zufällige Zellen mit Color-Coding sichten (z.B. DEFCON-Spalte N18, FLAG-Spalte O18, Σ-Check-Footer B25):

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

Punkte B-F entfallen (0 Formeln, 0 Conditional Formats — kein Korruptions-Risiko via openpyxl). Hochstufung in Voll-Smoke-Test sobald Watchlist-Tool-Update PIPELINE-Item resolved (Formeln / Logik hinzugefügt).

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
