# 🔁 Session-Übergabeprompt — Dynastie-Depot
**Erstellt:** 08.04.2026 | **Für:** Neue Cowork-Session

---

## ▶️ TRIGGER

```
Session starten
```

---

## 📋 Übergabe-Kontext (an Claude übergeben wenn Session startet)

Bitte lies zuerst die vier Core-Dateien wie gewohnt (CORE-MEMORY, KONTEXT, INSTRUKTIONEN, Faktortabelle).
Danach gilt folgender Kontext aus der letzten Session:

---

### ✅ Was in der letzten Session abgeschlossen wurde

1. **defeatbeta MCP via WSL2 vollständig repariert** (07.04.2026)
   - Konfiguration: `wsl -d Ubuntu-24.04 bash -c /home/tobia/.defeatbeta-env/bin/python -m defeatbeta_mcp`
   - Version 1.27.0 | 100+ Tools | Daten bis 03.04.2026

2. **ASML API Sanity Check abgeschlossen** (07.04.2026)
   - OCF-Δ ~10% = IFRS 16 vs. ASC 842 strukturell (Leasingzahlungen) — kein API-Drift
   - CapEx-Δ ≤ 3.5% plausibel. FLAG-Schlussfolgerung: Clean unter beiden Standards
   - IFRS-OCF-Toleranz auf ±15% erweitert wenn Leasingbasis erklärbar

3. **TMO DEFCON v3.4 Re-Analyse abgeschlossen** (07.04.2026)
   - Score: **67/100** | DEFCON: 🟡 3 | Sparrate: volle Rate (D3, kein 🔴)
   - Verbesserungen: Net Debt/EBITDA 2.57x ✅ | Fwd P/E 19.9x ✅
   - Schwächen: ROIC 2.6% Q (Goodwill $49.4B) | FCF -13.4% YoY | Unter 200MA
   - **Entscheidung ausstehend:** Q1 Earnings 23.04.2026 (FCF >$7.3B nötig für DEFCON 4)

4. **SKILL.md Token-Optimierungen implementiert** (08.04.2026)
   - WACC: nur neuester Wert (70+ Handelstage ignorieren)
   - ROIC quarterly: max. 6 Quartale auswerten
   - Quarterly CF: bedingt (nur bei CapEx/OCF 45–65%)
   - Geography: bedingt (nur bei Produktions-Risikoländern CN/TW/MY/TH/VN)
   - WebSearch: konsolidieren (mehrere Metriken in einer Suche)
   - ZIP-Paket: `06_Skills-Pakete/dynastie-depot_v3.4.1.zip` bereit zur Reinstallation

---

### 🚀 Nächste Aufgaben (in dieser Reihenfolge)

| Priorität | Aufgabe | Details |
|-----------|---------|---------|
| 🔴 1 | **!Analysiere MSFT** | Earnings 29.04. — FLAG-Review CapEx/OCF, aktuell 65.3% |
| 🔴 2 | **!Analysiere AVGO** | Tariff-Exposure MY/TH ~35%, Insider-FLAG läuft |
| 🟡 3 | **!Analysiere COST** | Retail, US-lastig, Tariff-Ketteneffekte |
| 🟡 4 | **!Analysiere V** | Kein Tariff-Risiko, aber Konsumrückgang-Check |
| 🟡 5 | **!Analysiere APH** | Produktion CN/MY — Tariff-Exposure prüfen |
| 🟢 6 | **!Analysiere BRK.B** | Holding, defensiv |
| 🟢 7 | **!Analysiere VEEV** | SaaS, kein Tariff-Risiko |
| 🟢 8 | **!Analysiere RMS** | Luxury, EUR, Preismacht |
| 🟢 9 | **!Analysiere SU** | Industrie, EUR |

**Hinweis Liberation Day:** Bei jedem Satelliten Tariff-Exposure prüfen (CN/TW/MY/TH/VN >35% = FLAG). Kurse seit 02.04. teilweise -10–20% gefallen → Forward-Metriken als Primärbasis, TTM als Kontext.

---

### 📅 Kritische Termine

| Datum | Ereignis | Aktion |
|-------|----------|--------|
| **23.04.2026** | TMO Q1 Earnings | FCF >$7.3B → DEFCON 4 / sonst ZTS-Aktivierung prüfen |
| **28.04.2026** | SPGI Earnings | QuickCheck SPGI (Score 79, Watchlist) |
| **29.04.2026** | MSFT Q3 Earnings | FLAG-Auflösung wenn CapEx/OCF <60% |
| **Mai 2026** | PEGA Earnings | Slot-16-Entscheidung |
| **01.05.2026** | Sparplan | !Rebalancing live testen (erster echter Lauf) |
| **Juni 2026** | Sparplan-Booster | 9.500€ Bausparvertrag + 2.000€ Steuererstattung |

---

### ⚙️ System-Status (Stand 08.04.2026)

| Komponente | Status |
|-----------|--------|
| defeatbeta MCP | ✅ WSL2 Ubuntu-24.04 — produktiv |
| Shibui Finance SQL | ✅ Primärquelle Technicals + FLAG-Historie |
| insider_intel.py | ✅ Form-4-Scanner 8 US-Satelliten |
| eodhd_intel.py / yfinance | ✅ Non-US Fundamentals (Cowork-Session: Web-Fallback) |
| SKILL.md | ✅ v3.4.1 — Token-Optimierungen aktiv |
| ZIP-Paket | ✅ dynasty-depot_v3.4.1.zip — reinstallation bereit |
| Shibui SQL column | ⚠️ `code` nicht `ticker` — immer `WHERE code = 'TICKER'` |

---

### 💡 Wichtige Einzel-Hinweise für die nächste Session

- **MSFT FLAG:** CapEx/OCF war 65.3% (Q2 FY26). Nächste Earnings 29.04. entscheidend. Wenn <60% → FLAG auflösen, D3 volle Rate aktivieren (D3 = Gewicht 1.0).
- **AVGO Insider:** Modul zeigt $123M FLAG, aber wahrscheinlich Post-Vesting. OpenInsider Spalte „X"/„M" immer manuell gegenchecken vor FLAG-Aktivierung.
- **Token-Effizienz:** Die neuen Regeln in SKILL.md (v3.4.1) greifen ab sofort. WACC-Zeitreihe kürzen, ROIC auf 6Q, Geography nur bei Risikoländern.
- **!Rebalancing:** Noch nicht live getestet — Test-Lauf erst am 01.05. wenn Sparplan eingeht.

---

## ✅ Briefing-Sync-Infrastruktur live (15.04.2026)

**Problem gelöst:** Morning-Briefing-Trigger (Remote 10:00) liest aus GitHub-Repo → lokale unpushed Änderungen = veraltetes Briefing. Jetzt dreifach abgesichert:

### Layer 1 — SessionEnd/SessionStart Hook (lokal, garantiert)
- **Datei:** `.claude/settings.local.json` (gitignored)
- **Script:** `03_Tools/briefing-sync-check.ps1`
- **Prüft:** `git status` + unpushed commits auf Faktortabelle, CORE-MEMORY, SESSION-HANDOVER, INSTRUKTIONEN
- **Output bei dirty:** Terminal-Warnung (systemMessage JSON) + **native Windows-Toast** (WinRT-API, kein BurntToast)
- **Silent bei clean**
- **Feuert:** 1× beim Session-Start (Catch-up) und 1× beim Session-Ende (Reminder)

### Layer 2 — Claude Mobile App Notifications (Push Handy/Desktop)
- **Bedingung:** User muss in Claude Mobile App + Desktop App **Notifications für Routines/Scheduled Agents** aktivieren (nicht von Claude konfigurierbar)
- **Quelle:** Remote-Trigger `morning-briefing` liefert Push via Claude-Account

### Layer 3 — Scheduled Task `briefing-sync-reminder`
- **Cron:** 09:54 MESZ werktags (11 Min vor 10:00-Briefing)
- **Bedingung:** Läuft nur wenn Claude Code CLI aktiv
- **Zweck:** Fallback für den Fall, dass CLI morgens schon offen ist

### Manuelle Shortcuts (INSTRUKTIONEN.md §25)
- `!BriefingCheck` — Diagnostischer Drift-Check gegen `origin/main`
- `!SyncBriefing` — Kontrollierter Push-Workflow mit Review-Gate, Scope `00_Core/` only

### RMS Exception (COST-Analogie) institutionell fixiert
- CORE-MEMORY-Eintrag 15.04.2026 um Screener-Exception ergänzt: ROIC 24% >> WACC 6,5% (Spread +17,5 PP) rechtfertigt DEFCON 🟢 4 trotz Score 69 — analog COST (MY 15,2% > WACC 12,3%)
- Re-Check-Trigger: H1 2026 Report Juli/Aug 2026

### Verworfene Alternativen
- **ntfy.sh**: External service — zugunsten nativer Windows-Toast + Claude-App verworfen
- **Stop-Hook**: Rauschen bei jedem Turn — zugunsten SessionEnd/SessionStart verworfen
- **Auto-Commit-Hook**: Verschmutzt Git-Historie mit WIP — Review-Gate bleibt Pflicht

---

*🦅 SESSION-HANDOVER.md v1.2 | Dynastie-Depot | Aktualisiert: 15.04.2026 (Briefing-Sync live)*
