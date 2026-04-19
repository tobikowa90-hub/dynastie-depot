# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 19.04.2026 Nachmittag (Track 2 abgeschlossen + Track 3 Spec+Plan ready) | **Für:** Nächste Session — Track 3 Paper-Integration Execution

---

## ⚡ SESSION 19.04. NACHMITTAG — PROGRESS SAVE

### ✅ ABGESCHLOSSEN IN DIESER SESSION

**Track 2 (Phase 4a Sync-Commit) abgeschlossen:**
- Commit `f915e5f` — 4-Paper-Backtest-Validation-Framework (20 files, +1063/-24)
- `git push origin main` — 21 Commits inkl. Tavily-Arc + Phase 4a nach GitHub synced
- Working tree clean, origin/main up-to-date

**Track 3 (Paper-Integration) — Brainstorming + Spec + Plan:**

| Artefakt | Pfad | Commit | Status |
|---|---|---|---|
| **Spec** (9 Sektionen, 5 Codex-Review-Runden) | `docs/superpowers/specs/2026-04-19-paper-integration-design.md` | `976e67a` | ✅ User-approved |
| **Plan** (11 Tasks, 5 Phasen + System-Audit) | `docs/superpowers/plans/2026-04-19-paper-integration.md` | `ee61535` | ✅ ready für Execution |

**Session-Workflow war:**
- Brainstorming-Skill: 2 Clarifying-Fragen (Scope, Batching) mit Codex-Review je
- Design-Präsentation: 4 Sektionen mit Codex-Review je (insgesamt 5 Runden)
- Spec-Write + Self-Review (2 Fixes inline: Tool-Pfade, R4-Template)
- Plan-Write + User-Ergänzungen: System-Audit Task + ZIP-Repack-Manual-Callouts

---

## 🔥 TRACK 3 EXECUTION — NÄCHSTE SESSION

### Start (User-Trigger)

```
Session starten
```

Claude liest `00_Core/STATE.md`. Dann hierher wechseln.

### Execution-Modus

**Inline via `executing-plans`-Skill** (User-Entscheidung 19.04.: "keine Subagents, kein Kontext-Bloat"). Applied-Learning #1: Markdown/YAML direkt editieren, nur Phase 3 Python-Code ggf. sorgfältiger.

**Plan:** `docs/superpowers/plans/2026-04-19-paper-integration.md`
**Spec:** `docs/superpowers/specs/2026-04-19-paper-integration-design.md`

### Phasen-Überblick (11 Tasks)

| Task | Phase | Inhalt | Review |
|---|---|---|---|
| 1 | 1a | 11 Satelliten-Pages mit Factor-Exposure-Block (Aghassi 2023) | User-Review |
| 2-3 | 1b | 6 defcon-Concepts + 8 bestehende Concepts + Index/Log | User-Review |
| 4 | 1b-End | Codex-Konsistenz-Pass (rg-basiert) | **Codex** |
| 5 | 2 | Skills + Tool-Dokus + INSTRUKTIONEN §§18/27/28/29-Anker | User-Review |
| — | ⏸️ | ZIP-Repack-Entscheidung (optional sofort / empfohlen nach Phase 4) | **User** |
| 6-7 | 3 | R5 portfolio_risk.py --persist daily + Daily-Schema + erster Snapshot | **Codex** |
| 8-9 | 4 | §30 Live-Monitoring Draft + Codex-Review + CORE-MEMORY/SKILL/STATE | **Codex** |
| — | ⏸️ | **ZIP-Repack-PFLICHT** (dynastie-depot + backtest-ready-forward-verify) | **User-Pause** |
| 10 | Audit | Multi-Source-Drift-Check + Codex-Final-Audit | **Codex** |
| 11 | Push | Final Sync + `git push origin main` | User-Approval |

### Schlüssel-Constraints

- **Applied-Learning strikt:** Kein Scoring-Kern-Change, keine neuen DEFCON-Columns, keine versteckten Workflow-/Trigger-Änderungen in Skills (siehe Spec §5 Guardrails)
- **Reviewer:** Codex (via `codex:rescue`-Skill oder `codex:codex-rescue`-Subagent mit `--resume`), nicht Advisor
- **FLAG-Semantik (Phase 4):** "Aktiver FLAG" (MSFT, binär in flag_events.jsonl) vs "Schema-Watch" (TMO, schema-getriggert-nicht-aktiviert) — Disambiguierung zu STATE.md "Aktive Watches"
- **R5 Schema:** `schema_version: "1.0"` pro Record in `portfolio_returns.jsonl`, Cashflow-Trennung, eigene `benchmark-series.jsonl` (keine retrospektive SPY-Rekonstruktion)
- **ZIP-Repack-Pause:** Claude pausiert nach Task 9, wartet auf User-GO nach erfolgreichem Repack + Redeploy

### Codex-Thread-Context

Vorherige Codex-Reviews dieser Session (Agent-IDs für `--resume`):
- Scope C+ → R5 Blind Spot identifiziert
- Batching B1.5 → R5 vor R1
- Scope-Items → R1→§30, Daily-Schema, R4-5-Zeilen-Struktur
- Execution-Phasen → Sub-Commits, schema_version, Benchmark-Serie, FLAG-Semantik
- Guardrails → Workflow-Guardrail, PBO-Smoke-Test, §30-Re-Review, Schema-Watch-Rename

Bei Execution: `--resume` flag nutzen für Thread-Kontinuität. Falls Thread-Loss: neu mit `--fresh`.

---

## 📋 PENDING PARALLEL TRACKS (nicht heute)

### Track 1 — Tavily-Plan ausführen (aus vorheriger Handover-Version)

- Plan: `docs/superpowers/plans/2026-04-19-tavily-morning-briefing.md` (d1b5bf7)
- Spec: `03_Tools/specs/2026-04-19-tavily-morning-briefing-design.md` (6bd32f4)
- 13 Tasks, ~60-90 Min inkl. manueller Desktop-App-Runs
- Nach Go-Live: Key-Rotation in 7 Tagen
- **Dependency:** Track 3 Execution zuerst (wegen CORE-MEMORY/STATE-Konflikt-Vermeidung)

### Track 4 — Portfolio-Risk-Tool ETF+Gold-Erweiterung

**Braucht User-Input am Session-Start:**
- **ETF-Core-Ticker?** (IWDA.AS / SWDA.L / EUNL.DE / ähnlich?)
- **Gold-Ticker?** (SGLD.DE / 4GLD.DE / GC=F / ähnlich?)

Danach: `03_Tools/portfolio_risk.py` um ETF+Gold erweitern.

**Synergie mit Track 3:** Track 3 Phase 3 führt `--persist daily` ein. Track 4 ETF+Gold wird danach natürlich in dieses Schema einfließen. Track 3 zuerst.

### Track 5 — SEC EDGAR + FRED MCPs

Deferred nach Tavily stabil (3-Tage-Monitoring). SEC EDGAR hat höheren Hebel als FRED.

---

## ⚠️ OPEN RISKS / REMINDERS

1. **Tavily Dev-Key Rotation** innerhalb 7 Tagen nach Tavily-Go-Live (aus vorheriger Handover — unverändert).
2. **ZIP-Repack-Pause** in Task 9 — Claude wartet, User führt manuell aus.
3. **Codex-Plugin Review-Gate** NICHT aktiviert (User-Entscheidung 19.04.) — Codex nur on-demand.
4. **Track-3-Execution-Monitor:** Applied-Learning-Regel 3× bestätigt vor Track-3-Start. Jeder neue "operative Regel-Kandidat" während Execution muss gegen R1-R5-Scope geprüft werden, nicht ad-hoc hinzugefügt.

---

## 💡 LEARNINGS SESSION 19.04. NACHMITTAG

**Codex als Reviewer (5 Runden in einer Session):**
- Workflow `Claude-Position → Codex-Review → User-Ratifikation` hat konsistent saubere Decisions produziert
- Codex findet Blind Spots systematisch (R5 Portfolio-Persistenz war Claude-Vorschlag fehlte komplett)
- `--resume`-Flag funktioniert gut für mehrstufige Reviews (gleicher Thread behält Kontext)

**Brainstorming-Skill mit Codex-Kette:**
- 4 Design-Sektionen sequentiell mit Codex-Review je → kompakter Iterations-Loop
- Gate zwischen Sektionen (User-"Ja") lässt User je Sektion priorisieren
- Spec-Self-Review fand 2 echte Issues (Tool-Pfade, Placeholder) — nicht redundant

**Kontext-Disziplin:**
- Plan-Execution wurde bewusst in neue Session gelegt (User-Entscheidung) — verhindert Context-Bloat
- SESSION-HANDOVER als Thread-Kontinuität-Bridge
- Plan-Dokument (1458 Zeilen) ersetzt tiefen Session-Kontext für Executor

---

## ▶️ TRIGGER (nächste Session)

```
Session starten
```

1. Claude liest `STATE.md`
2. Wechsel hierher
3. Primär-Track: **Track 3 Paper-Integration Execution**
4. Plan öffnen: `docs/superpowers/plans/2026-04-19-paper-integration.md`
5. `executing-plans`-Skill invoken
6. Task 1 starten

Bei abweichender Priorität (Track 1/4/5): User-Wahl respektieren, aber Dependency-Reihenfolge beachten (Track 3 blockiert Track 1/4).
