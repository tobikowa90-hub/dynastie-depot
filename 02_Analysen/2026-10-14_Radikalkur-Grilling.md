# Radikalkur — Grilling-Entscheidungen (PIPELINE #83)

> Laufendes Entscheidungsprotokoll. Je Entscheidung ein Satz. Wird nach Abschluss in die neue `INSTRUKTIONEN.md` / `CLAUDE.md` überführt und dann archiviert.

**Abbruchkriterium:** Jede Datei beantwortet eine der Kernfragen unten. Was keiner Frage dient, entfällt.

## E1 — Kernfragen des Systems (14.10.2026)

1. **Was mache ich mit Titel X?** → Score, FLAG, Sparrate
2. **Wie verteile ich die monatliche Sparrate?** → ETF / Aktien / Gold
3. **Halte ich meine Regeln ein?** → 60/35/5, US-Cap, Single-Stock-Cap, FLAG
4. **Was steht als Nächstes an?** → Earnings-Termine, Analyse-Fälligkeit
5. **Hat mein Verfahren funktioniert?** → Ledger, Rückblick ab 2028
6. **Schichte ich um?** → Gewinne einer Einzelaktie realisieren und in ETF-Core / Core-4 überleiten, oder Position durch einen nach fundierter Analyse besseren Kandidaten ersetzen

**Nicht im Scope:** tägliche News/Kurse (Scalable-App), System-Gesundheit/Audits, Sync-Status, Token-Statistik.

## E2 — Zustand = Broker, ausnahmslos (14.10.2026)

Positionen, Stückzahlen, Kurse, Sparraten, Cash **und Einstände** kommen live aus der Scalable-API und werden nirgends abgeschrieben. Einstände sind via `fifo_price` korrekt (ING-Übertrag mit steuerlichen Anschaffungsdaten; IWDA-Plausi: Rest-Einstand ~114,7 €/Stk ≠ Übertragswert ~128 €). ING komplett aufgelöst. Entnahme-Topf 2027 = befristete Regel in INSTRUKTIONEN, keine Extra-Datei.

## E3 — Urteil: Dreiteilung (14.10.2026)

- **Aktuelle Zahl** (Score, DEFCON, FLAG): letzter Eintrag je Ticker in `score_history.jsonl` / `flag_events.jsonl` — einzige Quelle.
- **Owner-Festlegung** (Tier, Overrides wie AVGO trotz FLAG, GOOGL/META 100 €, Veeva): Tabelle in `INSTRUKTIONEN.md`.
- **Begründung**: eine Datei je Ticker `02_Analysen/<TICKER>.md`, Abschnitt je Quartal, neuester oben. Ersetzt CORE-MEMORY §12, Vault-Frontmatter-Scores, verstreute Earnings-Notizen.
- **Statistik-Ledger** `portfolio_returns` + `benchmark-series` (+ `portfolio_risk.py`) seit 23.04. tot → Archiv (Vorschlag, Owner-Bestätigung ausstehend). Frage 5 aus `score_history` + Broker-Performance.

## E4 — Prüfen statt rechnen; FLAG = Warnsignal, kein Verbot (14.10.2026)

Sparraten sind Owner-Entscheidung. Keine Formelrate mehr (§22, Tier×DEFCON×FLAG, Nenner, Funded-Σ, xlsx-Rebalancing entfallen). INSTRUKTIONEN hält nur Leitplanken, `depot_status.py` prüft sie live: **hart** US-Cap 63 %, Single-Stock-Cap 10 % · **Korridor** 60/35/5 mit Toleranz (Hinweis) · **FLAG** bei laufender Rate = deutliche Meldung, kein Verbot; bewusstes Festhalten = Override-Zeile mit einem Satz Begründung. Tier keine Rechengröße mehr.

## E5 — Score = Handlungsleiter, Schwellen empirisch kalibriert; Core-4 ausgenommen (14.10.2026)

**Befund:** 15 echte v3.7-Analysen, Max 72 (BRK.B 71), **0× ≥80** — alle ≥80-Scores sind substanzlose Backfills. §20-Ersatzbedingung „≥80" war nie erfüllbar.

- DEFCON-Skala bleibt als **Messung** unverändert (Ledger-Vergleichbarkeit).
- **Handlungsschwellen:** ≥70 Aufstocken/Neuaufnahme-Kandidat · 65–69 Halten · 50–64 keine Erhöhung, Ersatz prüfen · <50 Umschichtung prüfen (Pflicht, Entscheidung beim Owner).
- **Ersatz schlägt Bestand:** Kandidat ≥70, kein FLAG, ≥10 Punkte über dem Bestandstitel.
- **Core-4 (MSFT, AMZN, GOOGL, META) sind von Ersatz/Umschichtung ausgenommen** — bleiben immer im Depot und werden sukzessive zur größten Position ausgebaut. Score/FLAG wirken dort nur als Information/Warnung, nie als Ersatz-Auslöser.
- **Termin:** Schwellen nach dem Q3-Cluster (~27 Analysen, Mitte Nov.) einmal gegen die Verteilung prüfen.

## E6 — Block-Definition Variante B (14.10.2026)

**60 % Core = ETFs + Core-4 (MSFT, AMZN, GOOGL, META) · 35 % Satelliten = übrige Einzelaktien · 5 % Gold.** Core-4 haben Fundament-Rolle (nie ersetzt, wachsen), die 35 % sind die aktiven Wetten. Entnahme-Topf 2027 zählt in keinen Block.

## E7 — Core-4-Ausbau unter hartem US-Cap; Depot wird weniger US-lastig (14.10.2026)

**Befund:** US-Anteil heute ~60,8 % (ETF-Faktoren geschätzt, IWDA ~0,72). Bei Core-4 >~11 % reißt der 63 %-Cap, wenn ETF-Mix + Satelliten so bleiben.

- **US-Cap 63 % bleibt hart.** Raum für Core-4 entsteht durch ex-US-lastigeren ETF-Mix (neues ETF-Geld bevorzugt EXUS/EIMI, solange der Cap knapp ist) und bewusst weniger US-lastige Satelliten über die nächsten Jahre (Owner-Ziel).
- **Core-4-Zielmarke ~20 % Depot** (je ~5 %, größte Einzelaktien; offen: „größte Position" = größte Einzelaktien, nicht größer als IWDA — Owner-Bestätigung ausstehend).
- Single-Stock-Cap 10 % kollidiert damit nicht.

## E8 — Altersvorsorgedepot ab 2027 = separater Topf, nur Platzhalter (14.10.2026)

Zählt nicht in 60/35/5 und nicht in den US-Cap. Vorhaben: Riester-Übertrag + staatliche Förderung, Anleihen-ETF (möglichst ex-US) als sichere Klasse. **Jetzt nur Platzhalter-Satz in INSTRUKTIONEN**; Regeln erst, wenn Produkt + Förderbedingungen feststehen (Reform-Details nach Wissensstand Mitte 2026 unsicher).

## E9 — Roster = Broker-Bestand; Score-Pflicht nach Gewicht/Rate (14.10.2026)

- Keine Roster-Liste mehr: was beim Broker liegt, wird geprüft. Satellit = jede Einzelaktie außer Core-4 **plus Themen-ETFs** (Quantum, Space = Satelliten-Wetten; AVGC = Faktor-ETF, Core).
- **Score-Pflicht:** jeder Satellit (Einzelaktie) mit laufender Rate **oder** >2 % Depotgewicht; Score aus echter Analyse, max. ~6 Monate alt — sonst `depot_status.py` „Analyse fällig". Core-4 ebenfalls Pflicht (nur Information, E5). Themen-ETFs: kein DEFCON-Score (Methode ist für Einzelaktien), nur Block-/Cap-Prüfung.
- Positionen ohne Rate und <2 % (Costco, Space-ETF) = „Auslauf", keine Pflicht.
- Folge Q3-Cluster: Erst-Scores NOW, Adobe, ZETA; erste echte Scores ASML, SU, RMS, Veeva (bisher nur Backfill).

## E10 — Methode bleibt, Ablauf radikal gekürzt (14.10.2026)

- **DEFCON-Methode** (Skalen, Schwellen, FLAG-Regeln) unverändert; Änderungen nur als bewusster Versionssprung (Ledger-Vergleichbarkeit für Frage 5).
- **Ablauf** = GOOGL-Minimal-Lauf: Daten (Primärquelle, defeatbeta, SEC Form 4) → scoren → Ledger-Record + Abschnitt `02_Analysen/<TICKER>.md` + ein Commit. Entfallen: §18-Schritte, Faktortabelle-/PORTFOLIO-Reads, Freshness-Gate, PORTFOLIO-Tripwire.
- **Persistenz:** Skill `backtest-ready-forward-verify` → Archiv; bleiben `archive_score.py` + Pre-Commit-Validator.
- **Nebenworkflows:** `!Rebalancing` = `depot_status.py`; `!CAPEX-FCF-ANALYSIS` → Archiv (Owner 14.10.); `!QuickCheck` bleibt als Kandidaten-Vorfilter.
- **§19.1 Tag-0/Tag+1** bleibt.
- Ziel: Skill ~600 statt 1.154 Zeilen, überwiegend Methode.

## E11 — Vault = reine Literatur/Ablage für Claude, kein Urteil, keine Regeln (14.10.2026)

- Satelliten-Seiten: `score_aktuell`/`flag`/`gültig_bis` raus → Link auf `02_Analysen/<TICKER>.md`; Inhalt (Geschäftsmodell, Moat-These) bleibt.
- Concept-Seiten: `operative_regel` → `herleitung_fuer:` (Verweis auf Methoden-Abschnitt; Regel lebt nur im Skill).
- `log.md` eingefroren bis 14.10.; Chronik ab jetzt = git log.
- WIKI-SCHEMA + Vault-CLAUDE.md bleiben für Ingest (Papers/Videos), aus dem Scoring-Pfad gelöst; `!Analysiere` liest Vault nicht standardmäßig.
- Nutzung: Ablage, die Claude liest (Owner nutzt Obsidian nicht aktiv).

## E12 — Regel-Parameter als markierter YAML-Block in INSTRUKTIONEN.md (14.10.2026)

Ein Block (~30 Z.) mit bloecke, caps, schwellen, core4, themen_etf_satellit, us_faktor_etf, overrides, entnahme_2027 — Prosa erklärt, Block ist die Zahl; Pre-Commit validiert ihn. `config.yaml` → Archiv. **Overrides: `bis:`-Ablaufdatum Pflicht** (danach warnt `depot_status.py` wieder). Ausgabe `depot_status.py`: Tabelle je Titel (Gewicht · Rate · Score · Stufe · FLAG · Alter · Widerspruch) + Blöcke vs. 60/35/5 + Caps + Fälliges (Earnings 30 d, Analysen nach E9).

## E13 — Verkaufsanlässe, Geldfluss, Freibetrag-Ernte (14.10.2026)

- **Drei zulässige Verkaufsanlässe, nie automatisch, immer Owner-Entscheidung:** (1) **Kappung** Satellit >10 % Single-Stock-Cap → zurück auf ~8 % (Core-4 ausgenommen) · (2) **Umschichtung** Satellit <50 oder Ersatz ≥70 mit +10 Pkt. (E5) · (3) **Gewinnmitnahme** nach Owner-Ermessen.
- **Geldfluss-Reihenfolge:** Core-4 solange <20 %-Zielmarke (E7) → sonst ETF ex-US solange US-Cap knapp → sonst IWDA. Bei Anlass 2 alternativ Ersatz-Kandidat.
- **Verboten:** Verkauf nur zur Glättung der 60/35/5-Quote (Quote = Sparraten-Steuerung).
- **NOW:** ~12 % gegen Dynastie-Basis (Topf-Tranche 2.000 € ausgenommen) → Anlass 1 nach Erst-Score (Analyse ~29.10.).
- **Freibetrag:** Sparerpauschbetrag 1.000 € (ledig) bis Heirat **07.08.2027**, danach 2.000 € Zusammenveranlagung (§ 26 EStG — für das ganze Jahr 2027 über die Steuererklärung; beim Broker erst mit gemeinsamem Freistellungsauftrag; geteilt mit Kapitalerträgen des Partners). **Jährliche Ernte:** Gewinne bis zum freien Rest realisieren + direkt zurückkaufen (Einstand steigt). `depot_status.py` zeigt bei Verkaufsanlässen Buchgewinn aus `fifo_price` + freien Freibetrag-Rest.

## E14 — Zielstruktur + Archivliste (14.10.2026)

**Aktiv:** `CLAUDE.md` · `00_Core/{INSTRUKTIONEN, KONTEXT, PIPELINE, APPLIED-LEARNING, CODE_GUIDELINES, SESSION-HANDOVER}` · `01_Skills/{dynastie-depot, insider-intelligence, non-us-fundamentals, quick-screener, _extern}` · `02_Analysen/<TICKER>.md` + Earnings Reports · `03_Tools/{depot_status.py (neu), earnings_calendar.py + overrides, backtest-ready/{archive_score, archive_flag, schemas}, precommit/{validate_score_history, validate_flag_events, crlf_guard}, video_ingest, defeatbeta_subprocess, Utils}` · `05_Archiv/{score_history, flag_events}.jsonl` · Vault (E11).

**Archiv `05_Archiv/radikalkur-2026-10/`:** 00_Core PORTFOLIO · Faktortabelle · STATE · CORE-MEMORY · SYSTEM · TOKEN-RULES · RETROSPECTIVE-GATE — Skills paragraph-18-sync · xlsx-smoke-test-runner (+workspace) · core-slim-refactor · backtest-ready-forward-verify · cross-source-verify · session-closure · sec-edgar-skill — Tools para18_sync · system_audit (+ Slash-Command) · spec_inventory_diff · depot-architecture-spec · 3× xlsx · xlsx-smoke-test.md · finnhub_* · hook-latency-* · portfolio_risk · schema_drift_phase2 · precommit para18-Reminder + xlsx-Hook · specs/ — `config.yaml` · `04_Templates/CAPEX-FCF` · Statistik-Ledger · `06_Skills-Pakete/` (Owner nutzt nicht). Nichts wird gelöscht.

## E15 — CLAUDE.md ~40 Z. mit Routing-Tabelle als Navigator; Scalable-CLI = Depot-Werkzeug (14.10.2026)

- **Routing-Tabelle bleibt als Navigator + Inhaltsverzeichnis** (3 Spalten Anlass | Lies/Nutze | Ergebnis, ~9 Zeilen; jede aktive Datei genau einmal). Entfallen: Skip-Spalte, Hybrid-Match-Regel, Edge-Case-Absatz, separate Ordnerliste. `!`-Trigger strikt deutsch/PascalCase (ein Satz).
- **Scalable-CLI** = primäres Werkzeug für Depot-Fragen, Strategie, Rebalancing **und Ausführung**; MCP-Connector = Fallback. `depot_status.py` = Regel-Brille auf CLI-Live-Daten, speichert nichts.
- **Ausführungsregeln (INSTRUKTIONEN):** zweiphasig, Owner-Freigabe in eigener Nachricht vor `--confirm`, nie bündeln (ein Vorschau-Slot), nach Ausführung Live-Stand gegen Vorschlag prüfen. Bedienwissen bleibt in Memory-Referenz.
- **Trade-Control:** `max_order_notional` = **10.000 €** scharf schalten (in der Umsetzungsphase, mit Owner-Freigabe); allowed/denied_isins bleiben aus (FLAG ≠ Verbot, E4).
- **Bleibt in CLAUDE.md:** Earnings Tag 0/Tag +1 als Einzeiler · harte Regel „Kein neuer Zustand in Dateien — nie eine Datei anlegen, die Broker-Zustand spiegelt, ohne Owner-Frage".
- **Entfällt:** §18-Sync-Pflicht, Pre-Investigation-Recall-Regel, S-Tier-Memory-Liste, Tier-1/2/3-Lerntabelle, Plugin-Layer, Pocock, Memory-Guard-Rail, Token-Effizienz-Regeln.

## E16 — Memories: 86 → ~35–40 in drei Körben (14.10.2026)

(1) **Löschen**, wo das Objekt nicht mehr existiert (§18, xlsx, core-slim, system_audit, FinnHub, Umstrukturierung-2027, Spec-Prozess) · (2) **Behalten**: gültige Werkzeug-Referenzen + Owner-Präferenzen · (3) **Verdichten**: fundamentale Lektionen (Verifikations-Ratsche, Teilausschnitt-Schluss, Empirie statt Annahme, Zustand vs. Urteil) → `APPLIED-LEARNING.md`. Konkrete Liste Eintrag für Eintrag zur Owner-Freigabe; nichts wird ungesehen gelöscht.

## E17 — Umsetzung in Phasen 0–3, Abnahmetest TMO (14.10.2026)

| Phase | Wann | Inhalt | Abnahme |
|---|---|---|---|
| 0 Pilot | 15.10. | ASML Tag +1 Minimal-Lauf, erste `02_Analysen/ASML.md` im neuen Format | Ledger-Record + Format vom Owner abgesegnet |
| 1 Regeln | bis 20.10. | INSTRUKTIONEN neu (Prosa + YAML-Block) + Abgleichliste aller alten Regeln (INSTRUKTIONEN/config.yaml/xlsx-B10/KONTEXT: übernommen oder bewusst gestrichen) | Owner-Freigabe + Codex-Gegenprüfung |
| 2 Werkzeug | bis 21.10. | `depot_status.py` + dynastie-depot-Skill gekürzt (E10) | Ausgabe = CLI-Rohdaten für alle Positionen; Ledger-Scores korrekt zugeordnet |
| 3 Abriss | bis 27.10. | Archiv-Move (E14), CLAUDE.md (E15), KONTEXT/PIPELINE/APPLIED-LEARNING ausdünnen, Vault-Frontmatter (E11), Memories (E16), Pre-Commit-Config, Trade-Control 10 k | `git grep` archivierte Namen im aktiven Pfad = 0 · Session startet sauber · Pre-Commit grün |
| Abnahmetest | 22.10. TMO | erste echte Analyse im neuen System | ohne Sync-Schritte: 1 Record + 1 Abschnitt + 1 Commit |

**Q3-Cluster-Umfang = Ist-Bestand laut Scalable-CLI**, nicht Roster-Listen der Altdateien (Owner 14.10.). **KYCCF ist nicht im Depot** → keine Analyse. Score-Pflicht nach E9. Abschluss-Check Ende Phase 3: Zuordnung jede aktive Datei → Kernfrage (E1).

## E18 — Phase-1-Klärungen (14.10.2026)

1. **Moat-Drift:** eigener Trigger entfällt (nie ausgelöst); Morningstar-Rating wird in jeder Analyse/QuickCheck geprüft, Downgrade seit letzter Analyse = „Analyse fällig“.
2. **Ersatzbank:** KONTEXT hält nur eine Namensliste (Ticker + 1 Satz, keine Zahlen); ersatz-tauglich nach E5 erst mit echter Analyse im Ledger. Watchlist-xlsx + config-`watchlist` → Archiv.
3. **§30 Monats-Refresh** gestrichen: FLAG-Prüfung in jeder Quartalsanalyse, Resolve-Check-Datum in der Ticker-Datei; Altbestand (5 FLAGs, 0 Resolves) im Q3-Cluster prüfen.
4. **§28/§29:** 5-Zeilen-Regel „Versionssprung“ in INSTRUKTIONEN; §29 wörtlich ins Archiv, Verweis „vor Rückblick 2028 lesen“.
5. **Aktien-Slots (13)** gestrichen — Roster = Broker (E9).
6. **Tier** komplett gestrichen — die Rate drückt die Conviction aus.
7. **Quellen-Drift ROIC:** >10 pp Abweichung Primär- vs. Sekundärquelle → Quellen/Definitionen ins `notizen`-Feld + Methodik-Check vor Append; Prüfer ohne Score-Änderungsbefugnis, Score folgt Primärquelle. Kein Versionssprung (Codex 14.10.: Option C, 91 %).
8. **Statistik-Ledger** → Archiv bestätigt. **Core-4 „größte Position“** = größte Einzelaktien, IWDA bleibt größte Position.
9. **Score-Alter:** 180 Tage im YAML-Block → danach „Analyse fällig“.

**Verfahren Abgleichliste:** eine Zeile je Regel mit allen Fundstellen · Wert aus E1–E18 gilt, ohne E-Bezug bei widersprüchlichen Altwerten → „offen → Owner“ · Methode nur im Skill, je Zeile geprüft ob der Skill sie wörtlich hat (sonst Phase 2 unverändert einfügen) · xlsx via openpyxl · Vollständigkeit per Skript (Fehlende = 0) · je Regel Lebensnachweis prüfen (Ledger/git log), „AKTIV“ im Dokument reicht nicht.

**Phase-1-Plan:** 16.10. Inventar → 16.–17. Verdikte → 18. Entwurf (eigene Datei neben diesem Protokoll; Tausch gegen alte INSTRUKTIONEN erst Phase 3 mit Skill-Kürzung) → 19. Codex + Owner-Review → 20. Commit.

## Offene Punkte aus den Gotchas (in die Phasen eingeplant)

- **Phase 2 — `earnings_calendar.py` auf CLI-Bestand umstellen:** kennt nur das alte 13er-Roster; **META, GOOGL, Adobe, Veeva fehlen**, KYCCF ist noch drin. Ticker künftig aus `sc broker holdings` statt aus PORTFOLIO — sonst fehlen genau die Core-4-Termine (META/GOOGL melden Ende Oktober).
- **Phase 2 — Freibetrag-Rest:** prüfen, ob die CLI den genutzten Sparerpauschbetrag liefert; sonst Owner-Eingabe 1×/Jahr im YAML-Block (E13).
- **Bis Phase 3 — §18-Hook:** `paragraph-18-sync-reminder` läuft bei jedem 00_Core-Commit weiter; Übergehen mit `PARA18_VERIFIED=1` nur bis zur Archivierung des Hooks, nicht als Gewohnheit.
- **Phase 3 — `.claude/settings.json`/Hook-Konfig:** Edits blockiert der Auto-Mode-Classifier (Self-Modification) trotz Owner-Freigabe → Owner führt per `!`-Befehl selbst aus.
- **Mitte November — Schwellen-Review:** 70/65/50 beruhen auf 15 echten Analysen; nach dem Cluster (~27) einmal gegen die Verteilung prüfen (E5).
- **Erledigt 14.10.:** `2026-09-20_Sparplan-Anpassung.md` mit Überholt-Vermerk committet (Begründungen erhalten, Live-Stand gilt).

---
**Grilling abgeschlossen 14.10.2026 — E1–E17; Phase-1-Klärungen E18 (14.10.).**
