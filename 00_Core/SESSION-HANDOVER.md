# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-25 — Session-Ende nach Tranche 1 + Tranche 2A (Drift-Konsolidierung post-Tier-2-Merge)

## Verweise
- [STATE.md](STATE.md) — Hub (Critical-Alerts + Last-Audit + Navigation)
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Briefing / Audit / Infra
- [CORE-MEMORY.md §13](CORE-MEMORY.md#13-system-lifecycle-history) — System-Lifecycle-Chronik (kanonische Initiative-Historie)
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

---

## 🔄 RESUME-INPUT (next session — System-Audit-Rework + finale Cross-Doc-Prüfung)

**Auftrag:** (1) Letzte umfassende systemweite Cross-Doc-/Cross-Folder-Prüfung über **alle** Ordner und Dateien, nicht nur 00_Core + dynastie-depot-Skill. (2) Danach `03_Tools/system_audit.py`-Rework gemäß Codex-Architecture-Critique (siehe unten). Reihenfolge: erst Audit, dann Tool-Bau — damit das Tool die richtigen Checks abdeckt.

**User-Begründung (zitiert):** „sinn und zweck dieses tools ist ja, dass es genau das macht. systemweite gaps aufdecken und schließen. und das in allen ordnern und dateien."

### (1) Umfassende Cross-Doc-/Cross-Folder-Prüfung

**Heute schon abgedeckt** (Tranche 1 + 2A): 00_Core/*, CLAUDE.md, 01_Skills/dynastie-depot/* (SKILL.md, PIPELINE.md, manifest.md, sources.md, Beispiele.md, config.yaml). Drift-Funde abgearbeitet außer einer:
- **OPEN — Stille Gap `03_Tools/backtest-ready/_forward_verify_helpers.py:25, :252-259`** — prüft nur `PORTFOLIO.md`, `Faktortabelle.md`, `log.md` als Freshness-Targets; CORE-MEMORY.md + config.yaml nicht. Widerspricht §18 v2.1 Score-Event-Set. Codex-Empfehlung: Helper auf §18 v2.1 erweitern ODER klar als Teil-Gate dokumentieren. Code-Change-Entscheidung in nächster Session.

**Noch nicht systematisch geprüft (Scope nächste Session):**
- `01_Skills/backtest-ready-forward-verify/*` — Skill-eigene SKILL.md, schemas, Doku
- `01_Skills/insider-intelligence/*`, `non-us-fundamentals/*`, `quick-screener/*` — andere aktive Skills
- `03_Tools/*` — Rebalancing/Satelliten-Monitor/Watchlist-Tooling, portfolio_risk.py, briefing-sync-check.ps1, system_audit/, backtest-ready/
- `04_Templates/*` — CAPEX-FCF + Alerts-Log + Analyse-Template
- `06_Skills-Pakete/*` — installierbare ZIPs (post-23.04.-Archive-Sweep)
- `docs/superpowers/specs/` und `docs/superpowers/plans/` — bekannt: many archivierte Pläne haben stale Pfad-Refs (siehe Audit-existence-FAIL 210/471, viele in Plan-Files)
- Top-Level: `MEMORY.md` (falls vorhanden), `.claude/`-Konfiguration, sonstige Root-Files

**Methodik-Vorschlag:** Pro Ordner ein Sweep-Pass (kann Explore-Agent parallel) → Funde-Report mit Severity → Fix-Liste → Fix-Commit(s).

### (2) `system_audit.py`-Rework — Codex-Architecture-Critique

**Codex-Verdikt (Agent-ID `a6ac838545a243eae`):** Inkrementell patchbar, kein formeller Tranche-3-Plan nötig. Konkrete Erweiterungen:

1. **PyYAML-Dependency-Preflight** — kein silent skip mehr. Bei ImportError klare Meldung „missing PyYAML; blocked checks: cross_source, skill_version" + rc=2. **Plus:** pyyaml installieren oder als Pure-Python-YAML-Replacement (`ruamel.yaml`?) erwägen.
2. **§18-Parity-Check** — vergleicht dokumentiertes Score-Event-Set in `INSTRUKTIONEN.md` §18.1 + `SKILL.md` Schritt 7 + `CLAUDE.md` Sync-Pflicht-Zeile gegen tatsächliche Schreib-Verhalten der Tools (z.B. `_forward_verify_helpers.py`). **Genau das hätte TMO-Drift gefangen.**
3. **Pointer-Completeness-Check** — explizite `SSoT →`-Pointer müssen Zielsektion/Zieldatei haben + Datei muss existieren.
4. **Top-Level-Governance-Parity-Check** — `CLAUDE.md` Kurzregeln gegen `INSTRUKTIONEN §17/§18` diffen.
5. **Header/Footer-Freshness-Check** — Datei mit 25.04.-Inhalt aber 20.04.-Footer = WARN/FAIL.
6. **Modus-Restrukturierung** — `--minimal-baseline` als CI/Smoke beibehalten; menschliche Routine: `--governance`, `--scoring`, `--vault`, `--all`.

**Codex-Risk-Calls:** Pointer-Verifikation niedrig-mittel Scope; Sektion-Redundancy-Detection HOCH (Fuzzy-Text-Overlap noisy + maintenance-lastig) — **nicht als nächsten Schritt**.

**Codex-Recommendation-Sequenz:**
1. Cross-Folder-Sweep zuerst (Phase 1 oben)
2. Dependency-Preflight + §18-Parity + Pointer-Check + Header/Footer-Check als 4 inkrementelle Patches
3. Modus-Restrukturierung (`--governance`/`--scoring`/`--vault`) ggf. später

**Codex-Output-Artefakt:** `.claude/codex-prompt-2026-04-25-drift-audit.md` (temp-File aus Tranche 2A, kann gelöscht werden nach Sichtung — Codex-Output ist in CORE-MEMORY §13 + Resume-Input zusammengefasst).

---

## Standing-Focus 30 Tage (unverändert seit Tier-2-Finalize)

- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal-Gate)
- **29.04. MSFT Q3 FY26** — FLAG-Review (CapEx/OCF bereinigt <60%)

---

## 📜 Handover-Policy (seit 2026-04-25 — Tier 2 Follow-up)

Nur **aktiver** RESUME-INPUT-Block in dieser Datei. Historie kanonisch in:
- **`git log`** — jeder Session-Ende-`handover:`-Commit ist die Banner-Chronik
- **`CORE-MEMORY.md` §13** — System-Lifecycle-History
- **`PIPELINE.md`** — Strikethrough-DONE-Items mit Datum + Commit-Hash

Pflege-Pflicht: Bei Session-Ende den aktiven Block durch den neuen ersetzen — nicht anhängen.

---

*🔁 SESSION-HANDOVER.md v2.0 | Dynasty-Depot | Slim-Resume — Policy B*
