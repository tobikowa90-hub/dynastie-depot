# 🌅 morning-briefing-spec.md — §24 + §25 Morning Briefing & Briefing-Sync Detail-Spec

**Version:** 1.0 (Pointer-Extraction 09.05.2026 aus INSTRUKTIONEN.md, PIPELINE #16 Variante A; inline-Drift-Refresh §24-Header v2.1 → v3.1.1)

> Detail-Spec für `00_Core/INSTRUKTIONEN.md §24` (Morning Briefing Scheduled Trigger) und `§25` (Briefing-Sync Shortcuts GitHub ↔ Local). Stub+Pointer in INSTRUKTIONEN.md erhält Trigger-Worte (`!Briefing`, `!BriefingCheck`, `!SyncBriefing`) + Anchor-Refs aus CLAUDE.md/SessionEnd-Hook funktional.
>
> Co-located mit `03_Tools/morning-briefing-prompt-v3.md` (Single Source of Truth für Trigger-Prompt, v3.1.1 prod live; v3.2.0 Probe-Cutover PENDING — Detail `00_Core/SYSTEM.md §Briefing-Status`) und `03_Tools/briefing-sync-check.ps1` (SessionStart/SessionEnd-Hook).
>
> **Token-Drift-Note (09.05.2026):** §24-Header und Prompt-Datei-Pfad wurden im Zuge des Pointer-Extracts von Stand v2.1 (28.04.-Plan-Anlage) auf aktuellen Live-Stand v3.1.1 (deployed 07.05. ~01:40, PIPELINE #49 Stufe 2) nachgezogen. Detail-Mechanik (Allow-List-Regex, Bracket-Reservation, AIDefence-Hook v3.2.0) bleibt SSoT in `00_Core/SYSTEM.md §Briefing-Status` — wird hier NICHT dupliziert.

---

## 24. Morning Briefing (Scheduled Trigger v3.1.1, prod live seit 07.05.2026)

**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`
**Frequenz:** Taeglich 10:00 Uhr MESZ (Cron `0 8 * * *` UTC, ~10-15 Min Jitter)
**Modell:** claude-sonnet-4-6 | **Repo:** github.com/tobikowa90-hub/dynastie-depot
**Token-Budget:** ~12-18k/Tag (Mo-Fr), ~2-3k/Tag (Sa-So)
**Prompt-Datei:** `03_Tools/morning-briefing-prompt-v3.md` (Single Source of Truth; v3.1.1 prod live, v3.2.0 Probe-Cutover PENDING — Detail `00_Core/SYSTEM.md §Briefing-Status`)
**Rollback-Backup:** `03_Tools/morning-briefing-prompt-v2.md` (30-Tage-Recovery-Window post v3.x-Deploy)

**Scope:** 11 Satelliten + 5 Ersatzbank mit Score (MKL, SNPS, SPGI, RACE, ZTS) = 16 Symbole

**Datenquellen (2 Tiers):**

| Tier | Symbole | Quelle | Status |
|------|---------|--------|--------|
| Shibui | ASML, AVGO, MSFT, TMO, VEEV, V, APH, COST, MKL, SNPS, SPGI, RACE, ZTS (13) | `stock_data_query` P1-Pattern mit `g.code IN(...)` | ✅ Live |
| Yahoo curl | BRK.B (`BRK-B`), RMS (`RMS.PA`), SU (`SU.PA`) (3) | `curl` in Bash | ❌ HTTP 403 — Yahoo blockiert Cloud-IPs. V3-Backlog. |

**Critical Guards im Prompt:**
- 🚨 SUNCOR-TRAP: Shibui `code='SU'` = Suncor Energy. Schneider Electric ist NICHT in Shibui. Nie 'SU' in Shibui-Query.
- 🚨 BERKSHIRE-GAP: BRK.B ist nicht in Shibui indexiert (bestaetigt).
- 🚨 HERMES-GAP: RMS ist nicht in Shibui.
- 🚨 ANTI-HALLUCINATION: Bei fehlenden Daten exakter Fehlertext, keine erfundenen Gruende.
- 🚨 KEIN RETRY: Keine Symbol-Varianten bei Query-Fehlschlag.

**Schwellenwerte:**
| Trigger | Schwelle | Empfehlung |
|---------|----------|------------|
| Kurs-Drop | >10% seit Score | !QuickCheck |
| Kurs-Drop | >20% seit Score | !Analysiere |
| Earnings | <7 Tage | Countdown + !QuickCheck |
| Score-Alter | >90 Tage | Update empfohlen |
| Score-Alter | >180 Tage | !Analysiere dringend |

**Manueller Trigger:** `!Briefing` (identischer Output) oder Desktop App → Routines → Jetzt ausfuehren

**Voraussetzung:** Faktortabelle muss aktuell sein (Sync-Pflicht §18). GitHub-Repo muss gepusht sein (`!SyncBriefing`).

**API-Update-Regel (KRITISCH):** RemoteTrigger-Update ersetzt `ccr`-Objekt KOMPLETT (kein Merge). Immer alle 3 Felder (`environment_id`, `session_context`, `events`) zusammen senden. JSON-Nesting: `parent_tool_use_id`, `session_id`, `type`, `uuid` gehoeren auf **data-Level**, NICHT in message.

**Known Limitations (v2.1-Baseline, v3.x-Stand siehe `00_Core/SYSTEM.md §Briefing-Status`):**
- BRK.B/RMS/SU-Kurse nicht verfuegbar (Yahoo 403 von Cloud-IPs). Zeigt ehrlich "n.v.".
- Push-Notifications: Kein Routines-Toggle in Claude iOS App. Wartet auf Anthropic-Update.
- `RemoteTrigger run` API-Endpoint ist Noop fuer Cron-basierte Trigger — manuell nur via Desktop App "Jetzt ausfuehren".

---

## 25. Briefing-Sync Shortcuts (GitHub ↔ Local)

**Problem:** Der 10:00-Morning-Briefing-Trigger läuft als Remote-Session auf claude.ai und liest `00_Core/` aus dem **GitHub-Repo** — nicht aus dem lokalen Arbeitsverzeichnis. Jede lokale Änderung an STATE.md (Hub) / PORTFOLIO.md / PIPELINE.md / SYSTEM.md / Faktortabelle / CORE-MEMORY / SESSION-HANDOVER / INSTRUKTIONEN muss vor 10:00 gepusht sein, sonst analysiert der Trigger veraltete Daten.

### `!BriefingCheck`

**Zweck:** Schneller Vorab-Check: *Liest der Trigger heute aktuelle Daten?*

**Schritte (Claude führt aus):**
1. `git fetch origin main --quiet`
2. `git diff --stat origin/main -- 00_Core/` — zeigt welche Briefing-Quellen lokal vom Remote abweichen
3. Wenn Unterschiede: Liste ausgeben + Empfehlung `!SyncBriefing`
4. Wenn keine Unterschiede: `✅ Trigger liest aktuellen Stand — kein Push nötig`

**Ausgabeformat:**
```
BriefingCheck [Datum HH:MM]
  STATE.md             [X Zeilen divergent] / [✅ identisch]
  PORTFOLIO.md         [X Zeilen divergent] / [✅ identisch]
  PIPELINE.md          [X Zeilen divergent] / [✅ identisch]
  SYSTEM.md            [X Zeilen divergent] / [✅ identisch]
  Faktortabelle.md     [X Zeilen divergent] / [✅ identisch]
  CORE-MEMORY.md       [X Zeilen divergent] / [✅ identisch]
  SESSION-HANDOVER.md  [X Zeilen divergent] / [✅ identisch]
Empfehlung: [!SyncBriefing ausführen] / [Kein Handeln nötig]
```

### `!SyncBriefing`

**Zweck:** Briefing-relevante `00_Core/`-Änderungen ins Repo pushen — mit Review-Gate.

**Schritte (Claude führt aus):**
1. `git status --short 00_Core/` — welche Dateien modified
2. `git diff 00_Core/` — vollständigen Diff anzeigen
3. **Review-Gate:** User bestätigt *explizit* mit `ja`/`push` bevor committed wird — nie automatisch
4. Nach Bestätigung: `git add 00_Core/STATE.md 00_Core/PORTFOLIO.md 00_Core/PIPELINE.md 00_Core/SYSTEM.md 00_Core/Faktortabelle.md 00_Core/CORE-MEMORY.md 00_Core/SESSION-HANDOVER.md 00_Core/INSTRUKTIONEN.md` (Hub-Split-Set, parallel zu `briefing-sync-check.ps1` `$briefingFiles`)
5. `git commit -m "Briefing-Sync: <kurze Begründung aus Diff abgeleitet>"`
6. `git push origin main`
7. Verifikation: `git log -1 --format="%h %s"` ausgeben

**Wichtig:**
- **Nur `00_Core/` wird synchronisiert** — keine Skills, Tools, Vault
- **Nie `git add .`** — Pfade explizit
- **Review-Gate ist Pflicht** — kein Auto-Commit
- **Commit-Message-Schema:** `Briefing-Sync: <Inhalt>` (z.B. `Briefing-Sync: RMS 71→69, Sparraten-Logik D3=voll`)

### Reminder (Scheduled Task `briefing-sync-reminder`)

- **Frequenz:** Werktags 09:50
- **Verhalten:** Prüft `00_Core/` auf uncommitted/unpushed Änderungen. Bei Treffern: Reminder-Output für nächste Claude-Code-Session. Kein Auto-Push.
- **Warum 09:50:** 10 Minuten Puffer vor Remote-Trigger um 10:00
- **Manueller Start:** `scheduled-tasks → briefing-sync-reminder → Run now`

### Wann `!SyncBriefing` nötig ist

- Nach jeder DEFCON-Analyse (Score/FLAG-Änderung)
- Nach `CORE-MEMORY.md`-Einträgen (institutionelles Gedächtnis)
- Nach Sparraten-Änderungen in `SESSION-HANDOVER.md`
- Spätestens abends vor Session-Ende, wenn Score-Updates vom Tag noch nicht gepusht sind

### Wann **kein** Push nötig ist

- Reine Skill-/Tool-/Vault-Änderungen (`01_Skills/`, `03_Tools/`, `07_Obsidian Vault/`) — Briefing liest diese nicht
- Work-in-Progress-Analysen (Score noch nicht final) — erst nach Abschluss pushen

---

*🦅 morning-briefing-spec.md v1.0 | Dynasty-Depot | §24+§25-Detail-Spec — verbatim-Extraktion aus INSTRUKTIONEN.md (PIPELINE #16 Variante A) | Stand: 09.05.2026 spätabends Konsolidierungstag-Wave-3*
