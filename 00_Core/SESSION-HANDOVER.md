# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 18.04.2026 (Nacht) | **Für:** Nächste Session (vmtl. 19.04.)

---

## ▶️ TRIGGER

```
Session starten
```

Claude liest automatisch `00_Core/STATE.md` (Single-Entry-Point). Für Skill-Planung zusätzlich: `superpowers:brainstorming` → `superpowers:writing-plans`.

---

## ✅ LETZTE SESSION (18.04.2026 Nacht) — ERLEDIGT

**1 Commit (`d6d6aaa`), strategischer Meta-Sprung.** Keine Portfolio-Änderungen — rein systemische Institutionalisierung.

### Kernereignisse

**1. BuildPartner-Plugin Install → Cleanup**
- Plugin `buildpartner@buildpartner v0.5.2` installiert, evaluiert, **vollständig entfernt**
- Keine Passung zum Dynasty-Depot-System (Business-Builder-Frameworks, keine Investment-Experten)
- Cleanup: `settings.json` + `installed_plugins.json` + `known_marketplaces.json` + Plugin-Dirs
- Onboarding-Hook wurde **bewusst nicht ausgeführt** (würde in `next session` ohnehin still verschwinden)

**2. Skill-Strategie-Analyse (63 Commits, 9 Tage, 8 Cluster)**

Systemweite Mustererkennung über gesamte System-Aufbau-Phase:

| Cluster | Commits | Status |
|---|---|---|
| Backtest-Ready Forward-Pipeline | ~8 | **Skill-Kandidat #1** (nächste Session) |
| Scoring-Version-Migration | ~10 | ✓ Als §28 institutionalisiert |
| Briefing-Sync / Pre-10:00-Gate | ~8 | ✓ §25 + Hook |
| Excel-Tool-Debugging | ~6 | Ad-hoc, nicht skillbar |
| System-Hygiene | ~10 | Ad-hoc |
| Vault/Wiki | ~5 | ✓ WIKI-SCHEMA |
| Session-Lifecycle | ~4 | ✓ SessionEnd-Hook |
| Learning-System (3-Tier) | ~3 | ✓ §27 |

**Meta-Insight:** Engine:Content ~ 2:1 in den letzten 9 Tagen — System wird aktuell stärker gebaut als genutzt. Phase wird sich mit Earnings-Dichte ab 23.04. umkehren.

**3. §28 Scoring-Version-Migration-Workflow** (Commit `d6d6aaa`)

Promotion aus Applied Learning Bullet #8 + systemische Fassung aus v3.4→v3.5 + v3.5→v3.7 Präzedenzfällen.

- **§28.1 Pflicht-Checklist** — 7 Steps: Paper-Evidence → Redundanz-Check (§27.1) → Algebra n≥5 → Forward-Verify → Orphan-Grep (ripgrep `-e` Syntax) → Anchor-Rekalibrierung → Fan-Out-Gate (7 Oberflächen)
- **Sequencing-Gate:** Steps 1-6 auf Branch, Step 4 muss grün sein bevor Step 7 Fan-Out
- **§28.2 Gestufte Δ-Toleranz:** ≤2 akzeptiert / 3-5 in CORE-MEMORY §5 loggen / **>5 blockiert** Migration
- **§28.3 Nicht-Migration-Trigger:** Quartals-Rekalibrierung + Bugfix ohne Skalen-Änderung + FLAG-only-Disclosure = keine Migration-Pflicht
- **Präzedenzfall §28.2:** V Algebra 86 vs Forward 63 (Δ23), Ursache WC-Proxy-Fehler → Regel-Bug
- **Präzedenzfall §28.3:** TMO fcf_trend_neg Option B (struktureller FLAG ohne Score-Penalty)

**4. Applied Learning: 9/20 → 8/20**
- Bullet #8 "Scoring-Version-Bump re-verify" → INSTRUKTIONEN §28.2 promoted
- CLAUDE.md Historie v2.0 → **v2.1** (Stand: **8/20**)

### Was entstanden ist

- `INSTRUKTIONEN.md v1.8 → v1.9` — §28 neu (+79 Zeilen)
- `CLAUDE.md` — 1 Bullet weniger, Historie v2.1

---

## 🎯 NÄCHSTER FOKUS (in dieser Reihenfolge)

### Priorität 1: Skill `backtest-ready-forward-verify` — Planung (superpowers)

**User-Wunsch:** In nächster Session mit **superpowers** in den Planungsprozess gehen.

**Workflow:**
1. `superpowers:brainstorming` — Anforderungen, Scope, Integrationspunkte klären
2. `superpowers:writing-plans` — konkreter Implementation-Plan mit Checkpoints
3. Implementation erst in darauffolgender Session (Subagent-Ready)

**Input-Basis:**
- Bestehendes Tool: `03_Tools/backtest-ready/` (Phase 0-4 bereits implementiert, README vorhanden)
- Kodifizierte Regeln: §28.1 Steps + §28.2 Delta-Regel + §18 Sync-Pflicht
- Präzedenzfälle: V/TMO/ASML/RMS Forward-Vollanalysen in `score_history.jsonl`

**Zu klärende Fragen im Brainstorming:**
- Skill-Scope: Nur !Analysiere-Forward-Run, oder auch Backfill-Re-Runs + FLAG-Event-Studies?
- Trigger: Automatisch bei !Analysiere, oder separater `!ForwardVerify`-Befehl?
- Verhältnis zu `dynastie-depot` Skill: Einzelner neuer Skill, oder Sub-Workflow des Haupt-Skills?
- Output-Format: Direkt `score_history.jsonl`-Write, oder Tempfile→Review→archive_score.py?

### Priorität 2: Earnings-Trigger (unverändert aus Session 18.04. Abend)

| Datum | Ticker | Klasse | Aktion |
|---|---|---|---|
| **23.04.** | **TMO** | **B** | Q1 FY26 — D2-Entscheidung + **fcf_trend_neg Resolve-Gate** (WC-Unwind? → Disclosure bleibt; sonst FLAG nachtragen) |
| **28.04.** | **V** | **B** | Q2 FY26 — D2-Entscheidung (Technicals-Reversal bei Beat + Guidance?) |
| 28.04. | SNPS / SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | Q3 FY26 — CapEx/OCF FLAG-Review (bereinigt <60% = Auflösung) |
| Mai | BRK.B / ZTS / PEGA | B | Q-Earnings + Slot-16 |

---

## 🧭 START-PROTOKOLL NÄCHSTE SESSION

1. `Session starten` → `STATE.md` wird gelesen (Nenner 8.0, 35,63€/17,81€)
2. Falls Skill-Planung: `superpowers:brainstorming` direkt aufrufen mit Prompt *"Skill `backtest-ready-forward-verify` konzipieren — siehe SESSION-HANDOVER Priorität 1"*
3. Falls Earnings: Schritt 0 Trigger-Check → Vollanalyse-Pfad
4. Backtest-Ready-Status (unverändert): **27 Records** (24 Backfill + 3 Forward), 2 FLAG-Events

---

## 🚫 WAS NICHT ZU TUN

- **Kein** ad-hoc-Bau des `backtest-ready-forward-verify`-Skills ohne vorherigen Brainstorming+Plan-Schritt (User-Wunsch: strukturierter Prozess via superpowers)
- **Keine** weiteren §-Erweiterungen vor Skill-Planung — Reihenfolge eingehalten, nicht gleichzeitig
- **Kein** Narrative-Layer (log.md / CORE-MEMORY.md) als Backtest-Primärquelle zitieren — Point-in-Time nur im History-Layer (JSONL)
- **Kein** manuelles Editieren von `05_Archiv/*.jsonl` — append-only, Korrekturen nur via neuer Record + Cross-Reference
- **Kein** mechanisches FLAG-Triggern ohne strukturellen Review (Präzedenz: TMO fcf_trend_neg Option B)
- **Kein** Ad-hoc-Version-Bump mehr — **§28 Pflicht-Checklist** ist jetzt das Gate
- **Kein** BuildPartner-Plugin-Reinstall (evaluiert, entfernt, nicht nützlich für Dynasty-Depot)

---

## 📂 KRITISCHE DATEIEN (Navigation)

- **Entry:** `00_Core/STATE.md` — Portfolio + Watches + Trigger
- **Gedächtnis:** `00_Core/CORE-MEMORY.md` §11 — 4 Befunde (Backtest-Ready + Drift + V + TMO Option B)
- **Regeln:** `00_Core/INSTRUKTIONEN.md v1.9` — §18 Sync-Pflicht, §22 Sparplan-Formel, §26 Archiv-Sync, §27 Scoring-Hygiene, **§28 Scoring-Version-Migration-Workflow (neu)**
- **Architektur:** `00_Core/KONTEXT.md` §11 — 4-Layer-Architektur
- **Tools:** `03_Tools/backtest-ready/README.md` — CLI-Usage (Skill-Planung-Input!)
- **Archive:** `05_Archiv/score_history.jsonl` (27) + `flag_events.jsonl` (2)
- **Skill:** `01_Skills/dynastie-depot/SKILL.md v3.7.1` + `config.yaml` (Stand 18.04.)
- **Applied Learning:** `CLAUDE.md` — 8 Bullets (v2.1)

---

## 🔬 System-Reife-Tracker

- v3.5 (16.04.): 85%
- v3.7 (17.04. Morgen): ~92%
- Backtest-Ready (17.04. Abend): ~95%
- Schema-SKILL-Aligned + Forward-Pipeline-bewährt (18.04. Abend): ~96%
- **Scoring-Version-Migration-Workflow formalisiert (18.04. Nacht): ~97%** — §28 gate gegen künftige Migration-Drift; Engine-Bau-Phase nähert sich Sedimentierung

### Outstanding Engine-Arbeit (nach aktueller Analyse)

- **Skill-Kapsel für Forward-Pipeline** (Priorität 1 nächste Session)
- Sonst: Engine "fertig genug" — Fokus-Shift auf Content (Earnings-Analysen ab 23.04.)
