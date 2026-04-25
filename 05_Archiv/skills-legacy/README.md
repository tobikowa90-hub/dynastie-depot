# Skills-Legacy — Archivierte ZIP-Installer

**Zweck:** Retention der Original-ZIP-Installer von Skills, die im Dynasty-Depot-System nicht aktiv genutzt werden (Legacy, Duplikate, oder nach Re-Eval rejected). Informationsverlust-Aversion: Files werden nicht gelöscht, sondern archiviert.

**Konvention:** Wer `06_Skills-Pakete/` nicht findet → hier schauen, dann `git log` der jeweiligen Rejection-Entscheidung.

---

## Inhalt (Stand 2026-04-23)

| ZIP | Skill-Name (aus SKILL.md) | Rejection-Grund | Evidenz |
|-----|--------------------------|-----------------|---------|
| `adaptationio-fmp-api.zip` | `fmp-api` | Redundanter Fremd-Skill, 17.04.2026 rejected | `01_Skills/dynastie-depot/PIPELINE.md:293` |
| `defeat-beta-defeatbeta-analyst.zip` | `defeatbeta-analyst` | Duplikat: Skill ist als `01_Skills/_extern/defeatbeta-analyst/` materialisiert. ZIP ist nur publisher-prefixed Legacy-Installer. | `01_Skills/_extern/defeatbeta-analyst/` exists |
| `neversight-sec-edgar-skill.zip` | `sec-edgar-skill` | Duplikat: Skill ist als `01_Skills/_extern/sec-edgar-skill/` materialisiert. ZIP ist nur publisher-prefixed Legacy-Installer. Track 5a (Promotion nach `01_Skills/sec-edgar-skill/`) entscheidet Fr 24.04.; ZIP wird in keinem Ausgang gebraucht. | `01_Skills/_extern/sec-edgar-skill/` + `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` |
| `qualitative-valuation.zip` | `qualitative-valuation` | Legacy, 17.04.2026 rejected: ~80% in DEFCON-Scoring kodifiziert, ESG bewusst ausgelassen. `_extern/qualitative-valuation/` explizit gelöscht. | `01_Skills/dynastie-depot/PIPELINE.md:294` + `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md:346` |
| `dynastie-depot_v3.7.2.zip` | `dynastie-depot` | Superseded by v3.7.3 (00_Core Struktur-Refactor: PORTFOLIO-Tripwire, CORE-MEMORY §1→§12/§13-Refs). DEFCON v3.7 unverändert. | `docs/superpowers/specs/2026-04-24-00core-perfect-organization-design.md` v0.4 AC #7 |

---

## Wiederherstellung

Falls ein Skill re-evaluiert werden soll:

```bash
# 1. ZIP zurückholen
cp 05_Archiv/skills-legacy/<name>.zip 06_Skills-Pakete/

# 2. Entpacken + materialisieren
unzip -o 06_Skills-Pakete/<name>.zip -d 01_Skills/_extern/<skill-name>/

# 3. SKILL.md lesen + INSTRUKTIONEN §17-Tabelle updaten

# 4. Re-Evaluation-Eintrag in CORE-MEMORY.md §1 Meilensteine
```

---

## Historisierung

- **2026-04-23 Abend:** Erster Batch archiviert (4 ZIPs). Trigger: Check-6 `skill_version` WARN nach bare-name-Fix c07f2c3 deckte 4 Orphan-ZIPs auf. Triage-Entscheidung: alle 4 → Archive (keine Re-Eval-Kandidaten erkennbar, 2 Legacy per PIPELINE.md, 2 Duplikate des jeweils bereits materialisierten `_extern/`-Skills).

### 2026-04-25 — 00_Core Struktur-Refactor

- `dynastie-depot_v3.7.2.zip` → superseded by `dynastie-depot_v3.7.3.zip` (00_Core Struktur-Refactor: PORTFOLIO-Tripwire, §1→§12/§13-Refs). DEFCON v3.7 unverändert.
- `backtest-ready-forward-verify` semver 1.0.0 → 1.0.1 (gleicher Refactor; bare-name-ZIP in `06_Skills-Pakete/` überschrieben; keine versionierte Trail-Kopie per User-Entscheidung).
