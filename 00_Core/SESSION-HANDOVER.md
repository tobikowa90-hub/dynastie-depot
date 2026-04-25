# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-25 Spät-Nachmittag — Tranche 4 DONE (Sign-off + 5 Fix-Commits + Codex-Follow-up); Phase 2 Plan-File auf nächste Session geschoben

## Verweise
- [STATE.md](STATE.md) — Hub (Critical-Alerts + Last-Audit + Navigation)
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Briefing / Audit / Infra
- [CORE-MEMORY.md §13](CORE-MEMORY.md#13-system-lifecycle-history) — System-Lifecycle-Chronik (kanonische Initiative-Historie)
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

---

## 🔄 RESUME-INPUT (next session — Phase 2 Plan-File via writing-plans)

**Auftrag:** Cluster A–E + F13/F15 + Codex-Follow-up sind DONE. Nächste Session: **Phase-2-Plan-File schreiben** für `system_audit.py`-Rework via `superpowers:writing-plans`. **Keine Code-Änderung am Audit-Tool diese Session** — nur Plan, dann separate Implementierungssession.

### Was DONE ist (Tranche 4, 25.04. Spät-Nachmittag)

**6 Commits + 2 lokale Cleanups, ausgehend von Sweep-Report `docs/superpowers/specs/2026-04-25-cross-folder-sweep-findings.md`:**

| Commit | Cluster | Findings |
|--------|---------|----------|
| `4de7054` | A — §18-v2.1-Drift | F1+F2+F4 (README.md v1.7→v2.1, 7-Datei-Liste, briefing-sync-check.ps1 +config.yaml) |
| `2bafd82` | B — Header-Freshness + F5-Normalisierung | F6 (briefing-prompt-v3.md `Deployed:`) + F9 (insider-intel Stand-Datum + rev) + F5 (PIPELINE v2.1→v2.2) |
| `a2994e7` | C — Top-Level Governance | F11 (SystemAudit.md 8 Kern-Checks + --minimal-baseline) + F12 (CLAUDE.md Z31 04_Templates Pointer-Wording, Option A) |
| `7fcda23` | D — Cleanup (F8+F16) | F8 quick-screener `version: 1.0.0` Frontmatter; F16 earnings-preview/recap.zip nach `05_Archiv/orphan-skill-zips/` (gitignored, kein git-mv) |
| `ee3de50` | E — Mastercard 3-Wege-Sync | F18a config.yaml watchlist: MA mit `quick_screener:`-Block (P/FCF 30,2 / ROIC 43% / Wide); F18b Vault `satelliten/MA.md` → `ersatzbank/MA.md` + Tags + Frontmatter; F18c Watchlist_Ersatzbank_Monitor_v1.1.xlsx R10+R26 verifizierte Werte + `QuickScan ✅ 25.04.2026` |
| `11b8856` | Codex-Follow-up | Vault `Backtest-Ready-Infrastructure.md:58` §18 v1.7→v2.1 (Sweep-Lücke Folder 5); briefing-sync-check.ps1 Status-Messages an erweitertes scope angepasst |

**Lokal-only (gitignored, kein Commit):**
- **F15** — `.claude/worktrees/stupefied-bhabha-43cb6a/` gelöscht. Diff-Verifikation: alle 6 Files = pre-Tier-2-Snapshot 23.04. 22:30–22:56 (vor Hub-Split + §1→§12/§13-Reorg), durch `97a2680` + Tranche-1+2A in main übertroffen. Codex VALID via `.git/logs/*`. Branch `refactor/00core-perfect-organization` (b23fe37) bleibt als Anker.
- **F13** — 5 stale Permissions aus `.claude/settings.local.json` entfernt (Z131+Z132 doppelte c/c-Reads, Z135 Python-Syntax, Z157 non-command, Z158 missing script). JSON-Validität verifiziert.

**Codex-Review (`a05c94070d09e5a5e`, Spät-Nachmittag 25.04.):** Keine BLOCKERs. 3 Loose-Ends: 2 fixed in `11b8856`, 1 false positive (`7fcda23` Message dokumentiert gitignored-Realität bereits explizit).

### TODO Session-Start (Phase 2 Plan-File)

**Tool:** `Skill(skill="superpowers:writing-plans")` → Plan-File `docs/superpowers/plans/2026-04-25-system-audit-rework.md`.

**Plan-Inhalt (empirische Sequenz, Codex-VALID):**
1. **§18-Parity-Check** (HIGH) — F1+F2+F4 hätte gefangen
2. **PyYAML-Dependency-Preflight** (HIGH, Codex-Caveat #1 — könnte vor §18-Parity wenn Resilienz=hard prereq)
3. **Skill-Frontmatter-Completeness-Check** (HIGH NEU) — F8 silent skip in `skill_version.py:82` (`if md_ver is None: continue`)
4. **Header/Footer-Freshness-Check** (MED) — F6+F9
5. **Top-Level-Governance-Parity-Check** (MED) — F11+F12
6. **Cross-Source-Reverse-Check** (MED NEU) — F18 watchlist/ersatzbank coverage; `cross_source.py:231-241` audited heute nur `satelliten`-Direction
7. **Pointer-Completeness-Check** (LOW)
8. **Defer:** Modus-Restrukturierung, Plan-vs-Live-Drift, ZIP-Mtime

### Code-Pattern-Hinweise für Plan-Author

- **Check-Module-Pattern:** `03_Tools/system_audit/checks/skill_version.py` ist guter Vorbild (saubere `run(repo_root, context) -> CheckResult`-Signatur, `time.monotonic()` Duration, FailureDetail-List, Status-Eskalation `FAIL > WARN > PASS`).
- **Registry:** Neue Checks in `03_Tools/system_audit/checks/__init__.py` `CORE`-Dict eintragen mit `name → "system_audit.checks.<modul>:run"`.
- **Types:** `system_audit.types.AuditContext` (repo_root, include_optional, vault_timeout_s); `CheckResult` (name, status, n_checked, n_passed, failures, duration_ms, category); `FailureDetail` (frozen dataclass — location, expected, actual, severity, hint).
- **YAML:** `import yaml` + `yaml.safe_load()` (siehe `skill_version.py:35`).
- **Tests:** `03_Tools/system_audit/_smoke_test.py` (59/59 PASS Baseline). Plain `def test_*` Funktionen, run via `python 03_Tools/system_audit/_smoke_test.py`. Keine pytest-Konvention außer `system_audit/_smoke_test.py`.
- **Path-Shadowing-Workaround:** `_smoke_test.py:18-19` poppt `sys.path[0]` weil Python's `types` durch package-local `types.py` shadow'd wird. Nicht ändern.
- **Verification-Gates:** `--minimal-baseline` (3 Checks: jsonl_schema + pipeline_ssot + log_lag) muss 3/3 PASS bleiben. `--core` 4/8 PASS heute (2 known FAIL + 2 known WARN, dokumentiert in PIPELINE Item #4).

### Standing-Pre-existing-Dirty
- `00_Core/STATE.md` — Last-Audit-Timestamp 10:01→10:22Z (älter, keine Aktion nötig)
- `00_Core/SESSION-HANDOVER.md` — wird mit dieser Session-Ende aktualisiert
- `03_Tools/Rebalancing_Tool_v3.4.xlsx` — pre-existing dirty, nicht von Tranche 4 berührt

### Memory-Updates (bereits persistiert)
- `feedback_review_via_codex_not_advisor.md` — Reviews/Second-Opinions immer Codex, nie advisor()
- `feedback_onedrive_edit_collision.md` — Edit-Collision-Pattern (vor Edit Editor-Status checken)

### Wichtige Calibration-Notiz
F3 (`_forward_verify_helpers.py:25, 257-259`) bleibt **INFO, nicht FIX** — SKILL.md Z126 + Code-Kommentar dokumentieren Teil-Gate-Trade-off explizit konsistent. Codex-RECONCILED VALID. Nicht als §18-Verletzung re-klassifizieren.

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
