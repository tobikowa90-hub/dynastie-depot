# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 17.04.2026 nach Backtest-Ready Infrastructure Phase 0-4 komplett | **Für:** Nächste Session

---

## ▶️ TRIGGER

```
Session starten
```

Claude liest automatisch `00_Core/STATE.md` (Single-Entry-Point).

---

## ✅ LETZTE SESSION (17.04.2026 — Abend) — ERLEDIGT

**Backtest-Ready Infrastructure Phase 0 + 0.5 + 1 + 2 + 3 + 4 komplett.** Skill v3.7.1 deployed (SKILL.md Schritt 6b/7). Forward-Pipeline scharfgeschaltet — ab nächster `!Analysiere` verliert keine Analyse mehr Historie.

### Was entstanden ist

**Code** (`03_Tools/backtest-ready/`, ~2991 Zeilen):
- `schemas.py` (678 Z.) — 14 Pydantic-Modelle, Arithmetik + DEFCON-Konsistenz + Quality-Trap-Interaktion (v3.7) + FLAG-Direction
- `archive_score.py` (468 Z.) — CLI-Append mit Uniqueness + Forward-Window
- `archive_flag.py` (606 Z.) — trigger/resolve/list Subcommands
- `backfill_scores.py` (383 Z.) — einmal-Run aus CORE-MEMORY Section 4
- `backfill_flags.py` (260 Z.) — einmal-Run für MSFT + GOOGL Capex-FLAGs
- `flag_event_study.py` (596 Z.) — deskriptive Event-Auswertung
- `README.md` — Tool-Doku

**Archive** (`05_Archiv/`, git-tracked via Whitelist):
- `score_history.jsonl` — **24 Records** (alle Backfill aus Section 4)
- `flag_events.jsonl` — **2 Records** (MSFT_capex_ocf_2026-01-15, GOOGL_capex_ocf_2026-03-15)
- `_parser_errors.log` — lokal-only (APH + AVGO Backfill-Skips dokumentiert)

**Doku-Updates:**
- `CLAUDE.md` Sync-Pflicht 2 Stellen (Z.19 + Z.55) auf 6 Dateien
- `STATE.md` Z.76 + System-Zustand um Backtest-Ready-Zeile
- `INSTRUKTIONEN.md` v1.5 → **v1.7** (§18 erweitert, §26 Archiv-Sync neu, getrimmt)
- `KONTEXT.md` **§11 4-Layer-Architektur** (State/Narrative/History/Projection)
- `CORE-MEMORY.md` §4 Tabelle → Pointer, **§11 Backtest-Ready** neu, §1 Meilenstein-Eintrag
- `01_Skills/dynastie-depot/SKILL.md` **Schritt 6b + 7** nach Depot-Einordnung
- `06_Skills-Pakete/dynastie-depot_v3.7.1.zip` — manuell Desktop-installiert
- `docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md` — v3.7-realigned (9 Deltas, §15 neu)
- `02_Analysen/flag_event_study_2026-04-17.md` — Einmal-Report (n=2, Disclaimer)

**Vault** (4 neu + 6 ergänzt, **84 → 88 Notes**):
- Neu: `Score-Archiv`, `FLAG-Event-Log`, `Backtest-Ready-Infrastructure` (concepts/defcon/), `Backtest-Methodik-Roadmap` (synthesis/)
- Ergänzt: DEFCON-System, Analyse-Pipeline, CapEx-FLAG, Tariff-Exposure-Regel, Wissenschaftliche-Fundierung-DEFCON, index.md

### Event-Study Kurz-Ergebnis (n=2, nicht statistisch belastbar)

- MSFT capex_ocf +30d: **-12.12%** raw, Alpha **-10.56pp** vs S&P500 — FLAG-Konzept-Sanity-Check bestätigt Direction
- GOOGL capex_ocf +30d: **+8.95%** raw, Alpha +4.95pp — kurze Fensterfrist, Score-FLAG funktioniert trotzdem auf Portfolio-Ebene (kein Einstieg)
- 5/8 Horizonte pending (+180/+360 noch nicht observierbar)

### Portfolio unverändert

Scores + DEFCON-Level + Sparraten (8.5-Nenner / 33,53€ / 16,76€) unverändert. Keine Score-Änderungen durch Infrastruktur-Arbeit.

---

## 🎯 NÄCHSTER FOKUS: Earnings-Trigger + Live-Verify

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| ~22.04. | V | B | Q2 FY26 — QuickCheck + Sparplan bestätigen |
| **23.04.** | **TMO** | **B** | **Q1 — D2-Entscheidung (FCF >$7.3B nötig für FCF-Yield >4%)** |
| 28.04. | SNPS / SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — CapEx/OCF FLAG-Review (bereinigt <60% = Auflösung)** |
| Mai | BRK.B / ZTS / PEGA | B | Q-Earnings + Slot-16 |
| Juli/Aug | RMS + SU | — | H1 Reports → Re-Check D4-Exceptions |
| 2026-07-23 | APH | C | Q2 Earnings + Tariff-Check |

**Archiv-Disziplin-Check** bei jeder !Analysiere ab jetzt:
- SKILL.md Schritt 7 → `archive_score.py` ausführen
- Bei FLAG-Trigger/Resolution → Schritt 6b → `archive_flag.py`
- §18 Sync-Pflicht: **6 Dateien** im gleichen git-Commit

---

## 🧭 START-PROTOKOLL NÄCHSTE SESSION

1. `Session starten` → `STATE.md` wird gelesen
2. Backtest-Ready-Status im "System-Zustand"-Block sichtbar
3. Earnings-Trigger checken, ggf. `!Analysiere <TICKER>` oder `!QuickCheck`
4. Bei `!Analysiere`: **Neuer Workflow** — Schritt 6b + 7 pflicht (SKILL.md v3.7.1)

---

## 🚫 WAS NICHT ZU TUN

- **Kein** Narrative-Layer (log.md / CORE-MEMORY.md) als Backtest-Primärquelle zitieren — Point-in-Time-Integrität nur im History-Layer (JSONL-Archive).
- **Kein** manuelles Editieren von `05_Archiv/*.jsonl` — append-only, Korrekturen nur via neuen Record mit Cross-Reference in `notizen`.
- **Kein** Commit von JSONL-Archiven ohne die begleitenden 4 Narrative/State/Projection-Dateien (§18 Sync-Pflicht).

---

## 📂 KRITISCHE DATEIEN (Navigation)

- **Entry:** `00_Core/STATE.md` — Portfolio-State + Watches + Trigger
- **Gedächtnis:** `00_Core/CORE-MEMORY.md` — §11 Backtest-Ready, §4 Pointer auf JSONL
- **Regeln:** `00_Core/INSTRUKTIONEN.md` v1.7 — §18 Sync-Pflicht, §26 Archiv-Sync
- **Architektur:** `00_Core/KONTEXT.md` — §11 4-Layer-Architektur
- **Tools:** `03_Tools/backtest-ready/README.md` — CLI-Usage
- **Archive:** `05_Archiv/score_history.jsonl` + `flag_events.jsonl`
- **Skill:** `01_Skills/dynastie-depot/SKILL.md` v3.7.1 — Workflow inkl. Schritt 6b + 7
- **Spec + Plan:** `docs/superpowers/` (gitignored, lokal-only)

---

## 🔬 System-Reife-Tracker

- v3.5 (16.04.): 85%
- v3.7 (17.04. Morgen): ~92%
- **Backtest-Ready (17.04. Abend): ~95%** — History-Layer aktiv, Forward-Pipeline scharf, 4-Layer-Architektur dokumentiert
- Weitere Hebel: Verhaltens-Layer (Execution Discipline), Makro-Overlay, Position-Sizing-Regel, FLAG-Historie-Volumen für 2028-Review
