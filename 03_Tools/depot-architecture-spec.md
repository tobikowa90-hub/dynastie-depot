# Depot-Architektur — Zustand, Urteil, Regelwerk

**Status:** Entwurf zur Freigabe · **Stand:** 2026-08-26 · **Version:** v1.5 (post R4: Eigenrunde + Live-Verifikation + Codex-Gegenprüfung)
**Vorgänger-Dokument:** `02_Analysen/2026-08-26_Depot-Reconciliation.md`

> **Entwicklung:** Vier Prüfrunden — R1 7 HIGH, R2 5, R3 2, R4 5 HIGH + 4 Codex-Befunde. Alle gegen die realen Dateien nachgeprüft. Vier Behauptungen der Vorfassungen waren empirisch falsch (Schreibverhalten §9.1, Ableitungsregel §4, Blast-Radius `backtest-ready/`, „ungescort trotz Position" bei META) und sind ersetzt. R4 war die erste Runde **gegen die Live-API** statt nur gegen das Repo. Schwerster Fund: der Score-Schreibpfad hat drei Abhängigkeiten, nicht zwei (§4.4 Gate 1 mit zwei Abnehmern, Gate 2, dazu das Schema aus §4.1). Prüfspur in §13.
>
> **Umsetzungsreife:** Stufe 0 freigabefähig. Stufe 1 freigabefähig, aber **nicht offline** — das Regelwerk-Befüllen braucht den Live-Layer (§9.4 Schritt 5). Stufe 2 erst nach der Gate-Neufassung aus §4.4 samt Schema-Bump, beides in Schritt 9 gebündelt.

---

## 1 · Zweck und Abnahmekriterium

Das Depot ist seit dem 17.08.2026 vollständig bei Scalable Capital konsolidiert und seit dem 26.08. per API abfragbar. Damit sind Positionen, Sparraten, Cash und Kurse **Zustand aus einer Fremdquelle** und keine gepflegten Dateien mehr.

Die Spec zieht daraus die Konsequenz — nicht weil die Markdown-Ebene veraltet ist, sondern weil die bisherige Struktur eine Wartungslast erzeugt hat, die den eigentlichen Zweck verdrängt: **regelmäßige DEFCON-Analysen**.

### 1.1 Befund

**Sieben Kopien.** Derselbe Score steht in `PORTFOLIO.md`, `Faktortabelle.md`, `config.yaml`, `INSTRUKTIONEN.md §22`, `score_history.jsonl`, `Rebalancing_Tool.xlsx` Spalte N und `Satelliten_Monitor.xlsx` Spalte L.

Nicht mitgezählt, weil disjunkt: das **Vault-Entity-Frontmatter** trägt Scores für genau drei Seiten (`wiki/entities/ersatzbank/{GOOGL,PEGA,ZTS}.md`), keine davon ein Satellit; das Standardschema in `WIKI-SCHEMA.md` (Z. 57–71) kennt gar kein Score-Feld.

**Damit ist auch geklärt, warum die Prüfinfrastruktur schweigt.** `cross_source.py` vergleicht laut Docstring vier Quellen, überspringt die leere aber **still und absichtlich**: Z. 184 `if "score" not in data: continue` — keine Satelliten-Entity gelangt je in den Vergleich; Z. 332–334 `if mirror_name == "Vault" and m.get("defcon") is None: pass  # DEFCON not required in Vault frontmatter`. Der Check ist nicht defekt, er wurde für diese Quelle zuständigkeitslos gestellt — mit einem Kommentar, der es begründet. Ein Check, der die Abwesenheit seiner Datenbasis als Normalfall behandelt, meldet auch dann nichts, wenn die Datenbasis fehlerhaft ist.

**Die Kopien haben eigene Infrastruktur:**

| Komponente | Zeilen | Aufgabe |
|---|---:|---|
| `system_audit/checks/cross_source.py` | 400 | Score/DEFCON/FLAG über config.yaml / PORTFOLIO.md / Faktortabelle.md / Vault-Frontmatter |
| `system_audit/checks/score_event_parity.py` | 293 | Score-Event-Parität |
| `system_audit/checks/cross_source_reverse.py` | 206 | Rückrichtung Roster |
| `insider_intel.py factor-sync` | — | 3-Wege-Vergleich config.yaml / Faktortabelle / Live-Scan |
| Skill `paragraph-18-sync` + `validator.py` + Pre-Commit-Hook | — | erinnert daran, keine Kopie zu vergessen |
| Skill `xlsx-smoke-test-runner` + `precommit/xlsx_smoke_test.py` | — | prüft Integrität der xlsx-Kopien nach jedem Write |

**Die Prüfinfrastruktur greift nicht.** Verifiziert 2026-08-26 — die drei FLAG-Quellen widersprechen sich paarweise, keine zwei stimmen überein:

| Quelle | aktive FLAGs |
|---|---|
| `config.yaml flags_aktiv` | MSFT · APH · AVGO |
| `flag_events.jsonl` (Trigger ohne Resolve) | MSFT · AVGO · AMZN · GOOGL |
| `PORTFOLIO.md` | MSFT · AMZN · AVGO · APH |
| Vault `entities/ersatzbank/` | GOOGL · PEGA · ZTS (nur diese drei Seiten tragen FLAG-Frontmatter) |

Konkrete Folge: **GOOGL trägt seit 2026-03-15 einen CapEx/OCF-Trigger ohne Resolve** und wird seit 2026-08-26 als Core-4-Titel mit 50 €/Monat bespart. Der FLAG steht ausschließlich in der jsonl, in keiner der beiden gelesenen Dateien.

**Analyse-Aktivität** (`score_history.jsonl`, 37 Records, davon 13 `forward`, 24 Backfill):

| Monat | 2026-03 | 2026-04 | 2026-05 | 2026-06 | 2026-07 | 2026-08 |
|---|---:|---:|---:|---:|---:|---:|
| Records | 11 | 22 | 2 | 2 | **0** | **0** |

Seit dem 13.06.2026 keine Analyse. Im selben Zeitraum entstanden Skills, Hooks und Prüfskripte.

**Verfalls-Cliff:** Aktuell ist kein Score verfallen, acht liegen bei 118–131 Tagen, GOOGL bei 153. Um den **Oktober 2026** laufen neun von dreizehn gleichzeitig über die 180-Tage-Grenze.

**Ungescort trotz Depotposition:** NOW (14,6 % Depotanteil), Adobe, ZETA. **Ungescort mit Sparplan, aber noch ohne Position:** GOOGL und META — beide Sparpläne laufen erst ab 01.09. an. Der Unterschied ist für `score_fehlt` und `cap_single_stock` erheblich: der eine Fall ist bereits Kapital im Risiko, der andere Kapital, das nächsten Monat fließt. Alphabet (72), Veeva (74) und Costco (69) haben entgegen der Annahme in der Reconciliation gültige Records.

### 1.2 Abnahmekriterium

Das System muss danach **kleiner** sein:

| Entfällt | Kommt hinzu |
|---|---|
| 3 xlsx-Tools | `00_Core/REGELWERK.yaml` |
| Skill `xlsx-smoke-test-runner` (vollständig) | `03_Tools/depot_check/` |
| `precommit/xlsx_smoke_test.py` | ein `analyse_typ`-Wert |
| Skill `paragraph-18-sync` (weitgehend) + `validator.py` + Pre-Commit-Hook | |
| `cross_source.py` · `cross_source_reverse.py` · `score_event_parity.py` (≈ 900 Z) | |
| `insider_intel factor-sync` | |
| INSTRUKTIONEN §18 großteils, §18.7 vollständig | |
| INSTRUKTIONEN §22 (Sparplan-Formel + hartcodierte 13-Zeilen-Score-Tabelle) | |
| Sync-Prosa in `CLAUDE.md` (6 Stellen, §9.2) | |

Ist die Bilanz nicht deutlich negativ, war der Entwurf falsch.

**Kein Rückgriff auf §33.** INSTRUKTIONEN §33 begrenzt seinen Geltungsbereich ausdrücklich auf KG-Extraktion, Bayesian-RAG, Agentic-Reflection-Loops und DPO-Alignment und schließt Scoring-Parameter- und Datenquellen-Änderungen aus. Eine Datenarchitektur-Konsolidierung fällt unter keinen Punkt. Statt ein unzuständiges Gate zu zitieren, gilt für diese Spec und alles Folgende:

> **Anti-Creep-Regel (neu, ersetzt den §33-Bezug für Infrastrukturarbeit)**
> In einem Monat ohne abgeschlossene DEFCON-Analyse wird kein **additives** Infrastruktur-Item eröffnet.
> **Rückbau ist immer erlaubt** — Arbeit, die nachweislich mehr entfernt als sie hinzufügt, fällt nicht unter die Sperre.
> Maximal drei offene Pipeline-Items gleichzeitig. Kein Plandokument über 500 Zeilen.

Die Rückbau-Ausnahme ist nicht kosmetisch: Ohne sie verböte die Regel bei wörtlicher Anwendung ihr eigenes Gründungsdokument, das in einem Null-Analyse-Monat entsteht. Der Nachweis ist die Bilanz oben — wer sich auf die Ausnahme beruft, legt sie vor.

Empirische Grundlage: 719 Commits zwischen 15.04. und 26.08.2026, davon 42 (5,8 %) mit Bezug zu Portfolio, Score oder Analyse. Nach dieser Regel wären April und Mai gesperrt gewesen — die zwei Monate, in denen 644 der 719 Commits entstanden.

---

## 2 · Datenmodell

| Schicht | Inhalt | Ort | Schreibt |
|---|---|---|---|
| **Zustand** | Positionen, Ist-Sparraten, Cash, Kurse, Broker, US-Quote-Ist, belegte Slots, **Broker-Watchlist** | Scalable-API; Cache `00_Core/.live/snapshot.json`, **gitignored** | niemand |
| **Urteil** | Score, Sub-Scores, DEFCON, FLAG, Kurs am Score-Tag | `05_Archiv/score_history.jsonl` · `flag_events.jsonl`, append-only | `backtest-ready-forward-verify` · `archive_flag.py` |
| **Regelwerk** | Allokation, Caps, Klassen, Tier-Basen, Roster, Kadenz, Verfall, Overrides, Ersatz-Zuordnung, Screener-Exceptions, Watchlist, Beobachtungsliste | `00_Core/REGELWERK.yaml` | Owner |
| **Chronik** | Begründungen, Per-Ticker-Historie, API-Audit-Log, freie Termine | `CORE-MEMORY.md §12` · Vault `log.md` | Owner |

**Kernsatz:** Der aktuelle Score ist keine Datei. Er ist der letzte Record je Ticker in `score_history.jsonl`. Sechs der sieben Kopien verschwinden nicht durch Disziplin, sondern weil sie keinen Ort mehr haben.

**„Watchlist" bezeichnet zwei verschiedene Dinge.** Die Broker-Watchlist ist eine Beobachtungsliste (13 Titel, darunter SpaceX, Roku, Kraken Robotics) und liefert je Eintrag ISIN, Name und Kurs — sie ist Zustand. Die kuratierte Ersatzbank ist eine 1:1-Zuordnung „wer ersetzt wen bei DEFCON 1 oder Veto" samt Aktivierungsschwelle und Steuerlogik — sie ist Regelwerk. Überschneidung heute: drei Titel (NVDA, DE, MA). Beide Listen unter einem Namen zu führen, erzeugt genau die Doppelquelle, die dieser Umbau beseitigen soll; `depot check` liest die Broker-Liste rein informativ und leitet daraus keine Regel ab.

Beispiel für die heutige Vermischung, `config.yaml` `portfolio:` (Z. 8–16): `us_hard_cap_pct` und `zieljahr` sind Regel, `us_current_pct` und `belegte_aktien_slots` sind Zustand — ein Block, eine gemeinsame Pflegepflicht.

### 2.1 Zuordnung aller heutigen `config.yaml`-Blöcke

Vollständig **auf Blockebene** — alle 15 Top-Level-Keys sind zugeordnet. Nicht feldweise: der `satelliten`-Block (Z. 158–398) ist laut §11 Punkt 7 noch nicht durchgegangen.

| Block | Schicht | Anmerkung |
|---|---|---|
| `portfolio` | geteilt | Caps und `zieljahr` → Regelwerk; **`sparrate_eur` → Regelwerk** (Owner-Entscheidung, siehe unten); Slots und `us_current_pct` → Zustand |
| `brokers` | Zustand | entfällt als Regel (§9.6) |
| `allokation` | Regelwerk | |
| `satelliten_tier_raten` | Regelwerk | → `klassen.satellit.tier_basis_eur` |
| `system_regeln` | Regelwerk | Verfall, Ersatz-Aktivierung, Moat-Drift, Sparplan-Verteilung, Tariff-Quelle |
| `etfs` | geteilt | ISIN + Soll-Rate → Regelwerk; `broker` → Zustand |
| `satelliten` | geteilt | feldweise aufgeschlüsselt, siehe §2.2 |
| `flags_aktiv` · `flags_review` · `flags_watchlist` | Urteil | wird aus `flag_events.jsonl` abgeleitet, nachdem diese vollständig ist (§4.2) |
| `screener_exceptions` | Regelwerk | |
| `watchlist` | Regelwerk | Score-Felder je Eintrag → Urteil (§4.3) |
| `keine_zuteilung` | Regelwerk | Beobachtungsliste ohne Analysepflicht |
| `termine` | geteilt | Earnings → generiert aus `earnings_calendar.py`; freie Reminder ohne Ticker-Bezug → Chronik |
| `api_audit_log` | Chronik | |

### 2.2 `satelliten`-Block feldweise (24 Felder, alle 13 Einträge)

| Schicht | Felder |
|---|---|
| **Regelwerk** | `name` · `typ` · `tier` · `region` · `us_exposure` · `ersatz` · `substitute_activation_rule` · `screener_exception` |
| **Urteil** | `score` · `score_datum` · `defcon` · `flag` · `flag_grund` · `flag_seit` · `flag_aufloesung` |
| **Chronik** | `scoring_notiz` · `roic_notiz` · `flag_hinweis` · `worst_case` |
| **Generiert** | `naechste_pruefung` · `earnings_trigger` (aus `earnings_calendar.py`) · `sparrate_hinweis` · `score_valid_until` (= `score_datum` + `verfall_tage`) |
| **Override-Vorlage** | `flag_wirkung` — siehe unten |

**`flag_wirkung` existiert bereits per Ticker**, viermal, als Freitext. §3 stellt die Klassenregel als Neuerung dar („bisher ein Vier-Stellen-Refactor, jetzt ein Wort") — zutreffend für die *Regel*, nicht für das *Feld*. Die vier Freitexte tragen Owner-Entscheidungshistorie, die beim Übertrag in einen Enum-Wert verloren ginge, etwa `config.yaml` Z. 340: „User-Entscheidung 2026-05-18: regelkonform 0 €, KEIN Owner-Override." Diese Sätze gehören in die Chronik, bevor der Block entfällt. Damit hat die Override-Synthese nach §3.3 dieselbe Ausgangslage wie die Ersatzbank nach §3.2: eine verstreute Vorlage, kein leeres Blatt.

---

## 3 · REGELWERK.yaml

Einzige handgeschriebene Quelle für Politik.

```yaml
meta: {version: "1.0", gueltig_ab: 2026-08-27}

budget:
  monatlich_eur: 1031            # SOLL-Gesamtsparrate, Owner-Entscheidung (xlsx B4).
                                 # NICHT der Broker-Ist (aktuell 1068) — der ist Zustand.
                                 # Direkter Faktor in §7.2; ohne dieses Feld rechnet depot check nicht.

allokation:
  etf_core_pct: 60               # Politik. Die 59,7/35,3/5,0 des Tools sind das
  satelliten_pct: 35             # Rundungsartefakt ganzzahliger Euro-Raten
  gold_pct: 5                    # (616/364/51 von 1031), keine abweichende Regel.
  toleranz_pp: {etf_gold: 1.5, aktien: 4.0}    # getrennt, wie im Tool (B8/B9)
  drift_warnfaktor: 3                          # Toleranz x Faktor -> rot (B15)

caps:
  us_hard_cap_pct: 63
  us_cap_gilt_fuer: [ist, ziel]  # Tool prueft beides (US-Exposure B29/B30)
  single_stock_max_pct: 10
  max_aktien_slots: 13

rebalancing:
  modell: additiv                # ENTSCHIEDEN 2026-08-26 (§7.3). Tier-Basis bedeutet Euro.
  nachkauf_schwelle_eur: 300     # Fehlbetrag fuer Einmalkauf-Signal (B65)
  niemals_durch_verkauf: true    # Steuer-Bremse (B23)
  freigesetzt:                   # Ziel eingefrorener Betraege, in dieser Reihenfolge
    - ersatz                     # 1. Substitutionsfall (D1 oder Veto, Ersatz Score >=80 ohne FLAG)
                                 #    -> substitute_activation_global, bestehende Regel
    - block_untergewicht         # 2. Block mit groesster Abweichung unter Ziel
    - etf_core                   # 3. Rueckfall, wenn alle Bloecke auf Ziel
  freigesetzt_nie: satelliten_diffus   # nie ungezielt auf uebrige Satelliten verteilen

defcon:
  schwellen: {D4: 80, D3: 65, D2: 50}
  modulation: {4: 1.0, 3: 1.0, 2: 0.5, 1: 0.0}

klassen:
  core:        {flag_wirkung: analysepflicht, defcon_modulation: false, basis_eur: 50}
  satellit:    {flag_wirkung: rate_null, defcon_modulation: true,
                tier_basis_eur: {1: 40, 2: 32, 3: 18}}
  themenwette: {flag_wirkung: keine, defcon_modulation: false}

ohne_score: {core: basis_voll, satellit: basis_voll, themenwette: basis_voll}
score_regeln: {verfall_tage: 180}

analyse_pflicht:
  je_earnings:   {klassen: [core], ab_depotanteil_pct: 5, bei_aktivem_flag: true}
  halbjaehrlich: {klassen: [satellit], max_score_alter_tage: 180}
  ausgenommen:   {klassen: [themenwette], typen: [etf, gold]}

# ISIN-Quelle: Scalable (holdings ∪ savings_plans). Steht nirgends im Repo —
# weder config.yaml (dort nur die 6 ETF-ISINs, Gold hat keine) noch in den xlsx.
# Einmalig beim Befuellen ziehen, dann als Regelwerk-Stammdatum festschreiben.
roster:
  - {ticker: MSFT, isin: US5949181045, klasse: core}
  - {ticker: NOW,  isin: US81762P1021, klasse: satellit, tier: 1, ersatz: [SNPS]}
  # …

# SOLL-Raten beim Befuellen neu entscheiden — Ist weicht durchgaengig ab:
#   IWDA 206→208 · EIMI 123→120 · EXUS 82→80 · AVGC 82→85 · WQTM 51→70
#   JEDI 72→ kein Sparplan mehr, Position bleibt (2,25 Stk.) · Gold 51→80
#   Σ config.yaml 616 gegen Σ Broker 563 (ohne Gold).
etf_roster:
  - {ticker: IWDA, isin: IE00B4L5Y983, soll_rate_eur: 208}
  - {ticker: EIMI, isin: IE00BKM4GZ66, soll_rate_eur: 120}
  - {ticker: EXUS, isin: IE0006WW1TQ4, soll_rate_eur: 80}
  - {ticker: AVGC, isin: IE0003R87OG3, soll_rate_eur: 85}
  - {ticker: WQTM, isin: IE000W8WMSL2, soll_rate_eur: 70}
  - {ticker: JEDI, isin: IE000YU9K6K2, soll_rate_eur: 0}   # Position ohne Sparplan — Owner-Entscheidung offen
gold: {ticker: EWG2, isin: DE000EWG2LD7, soll_rate_eur: 80}

overrides:                       # §3.3 — bewusste Regelabweichungen
  - {ticker: APH, regel: flag_wirkung, wert: rate_beibehalten, betrag_eur: 20,
     grund: "Owner-Entscheidung 26.08.2026 trotz Score-FLAG",
     seit: 2026-08-26, review_am: 2026-11-26}
  - {ticker: NOW, regel: rate, wert: 0,
     grund: "Kapitalumschichtung zugunsten Core-Aufbau 26.08.2026 — kein FLAG",
     seit: 2026-08-26, review_am: 2027-02-26}
  - {ticker: GOOGL, regel: flag_wirkung, wert: analysepflicht,
     grund: "Core-Aufbau 26.08.2026; CapEx/OCF-Trigger vom 15.03. offen, Ausschluss-Vermerk im Vault vom 01.04. bewusst ausgesetzt bis Vollanalyse",
     seit: 2026-08-26, review_am: 2026-11-26}   # nur noetig, falls der Ausschluss nicht foermlich aufgehoben wird — §9.3

screener_exceptions: {...}       # 1:1 aus config.yaml Top-Level
watchlist: {...}                 # 1:1 aus config.yaml Top-Level
keine_zuteilung: {...}           # 1:1 aus config.yaml Top-Level
moat_drift_trigger: {...}        # aus system_regeln
substitute_activation_global: {...}
tariff_exposure_quelle: {...}
```

**`rebalancing.modell` wählt die Formel, nicht nur eine Beschriftung.** `tier_basis_eur` und `defcon.modulation` allein lesen sich wie das additive Modell. Erst `modell` entscheidet, ob daraus Euro-Beträge (additiv) oder relative Gewichte (Normierung, §7.2a) werden. Steht `additiv`, wie seit 2026-08-26 entschieden, sind Tier-Basen Euro-Beträge und `freigesetzt` bestimmt, wohin eingefrorene Raten fließen (§7.4).

**Ladezeit-Validierung** beim Einlesen des Regelwerks, fail-close: `etf_core_pct + satelliten_pct + gold_pct = 100` (entspricht dem Summen-Check B16 der xlsx) · jeder `roster`-Eintrag hat eine in `klassen` definierte Klasse · `satellit`-Einträge tragen ein `tier` · jeder Override nennt `grund`, `seit` und `review_am`.

**`klassen.*.flag_wirkung` ist die FLAG-Zweiteilung.** Bisher ein Vier-Stellen-Refactor über `config.yaml`, `PORTFOLIO.md`, `INSTRUKTIONEN §22` und eine xlsx-Formel; jetzt ein Wort. Dass das 3-Tier-Modell zwischen Beschluss und Depot-Wirklichkeit auseinanderlief, gehört zu dieser Fehlerklasse.

**`ohne_score: basis_voll`** macht die Owner-Conviction-Add-Praxis explizit, statt sie als „DEFCON-3-Platzhalter" zu tarnen — ein Platzhalter-Score ist ein erfundener Score in einer Datei, aus der Backtests gelesen werden.

### 3.1 Beim Befüllen zu entscheiden (Daten, nicht Spec)

| Ticker | offene Frage |
|---|---|
| GOOGL · MSFT · AMZN · META | Klasse `core` — durch Owner-Strategie 26.08. gesetzt |
| NOW | `satellit` T1 oder `core`? 14,5 % Depotanteil, Software-These, kein Weltmarkt-Dominator |
| Adobe · Veeva | Roster-Aufnahme als `satellit`, Tier offen |
| ZETA | Tier bestätigen (bisher T3, QuickScreener war Rot) |
| Costco | Take-Profit gewollt → Roster oder Abgang? Bei Abgang zusätzlich den `screener_exceptions`-Eintrag („Membership Yield") mit entfernen, sonst bleibt er verwaist |
| JEDI | Position ohne Sparplan. Halten, aufstocken oder abgehen? Betrifft `etf_roster.soll_rate_eur` |
| JEDI · WQTM | `themenwette` |
| KYCCF | nicht mehr im Depot → aus Roster; Score 67 bleibt in der Historie |

### 3.2 Ersatzbank ist Synthesearbeit, kein Verschieben

Es gibt **keinen** `ersatzbank`-Block in `config.yaml`. Die Ersatz-Zuordnung liegt heute verstreut: als Inline-Feld `ersatz:` bzw. `substitute_activation_rule:` je Satellit, als globale Regel in `system_regeln.substitute_activation_global`, und als Freitext in `watchlist`-Einträgen (`status: "Ersatzbank BRK.B"`, vereinzelt `related:`).

Beim Befüllen ist daraus eine konsistente Zuordnung zu bilden. Das ist eine eigene Aufgabe mit Entscheidungsbedarf, kein mechanischer Umzug.

**Der Broker hilft dabei nicht.** Seine Watchlist enthält von den zehn Ersatz-Kandidaten drei (NVDA, DE, MA) und zusätzlich zehn Titel ohne Ersatz-Zuordnung. Was ihr fehlt, ist die Zuordnung selbst — und daran hängen Stufe 1 der Freigesetzt-Staffel (§7.4) und die Regel „niemals durch Verkauf tauschen". Die Synthese bleibt Handarbeit.

### 3.3 Overrides — Escape-Hatch für bewusste Regelabweichungen

Ohne dieses Feld meldet `depot check` jede vom Owner bewusst akzeptierte Abweichung dauerhaft als Verstoß, und der Report wird ignoriert wie jede Warnung, die immer leuchtet. Konkreter Fall: APH läuft mit 20 €/Monat trotz aktivem Score-FLAG (Reconciliation §F.3, „nicht angefasst").

Ein Override trägt Pflichtfelder `grund`, `seit` und `review_am`. `depot check` meldet ihn als **INFO** statt FAIL, und als **WARN**, sobald `review_am` überschritten ist. Eine Ausnahme ohne Ablaufdatum ist keine Ausnahme, sondern eine stille Regeländerung.

**Übersteuerbare Regeln — abschließende Liste.** Ein Override, dessen `regel` hier nicht steht, wird beim Laden abgelehnt.

| `regel` | `wert` | Fall |
|---|---|---|
| `flag_wirkung` | `rate_beibehalten` · `rate_null` · `analysepflicht` | Klassenregel für diesen Titel übersteuern — APH läuft mit 20 € trotz Score-FLAG |
| `rate` | Euro-Betrag | Rate unabhängig von jeder Regel setzen — NOW auf 0 € ohne FLAG, reine Kapitalumschichtung |
| `tier` | 1 · 2 · 3 | befristete Conviction-Abweichung ohne Roster-Änderung |
| `analyse_pflicht` | `ausgesetzt` | Kadenz aussetzen, etwa bei laufendem Verkauf |
| `cap_single_stock` | Prozentwert oder `ausgesetzt` | Position bewusst über Cap halten — NOW mit 14,5 % gegen 10 %, „bewusst übergewichtet" laut Owner-Strategie (Reconciliation §F.1) |

**NOW allein braucht zwei Overrides** und zeigt damit, warum die Liste über FLAG hinausgehen muss:

1. **Rate 0 ohne FLAG.** Am 26.08. auf 0 gesetzt zur Kapitalumschichtung; Tier 1 mit `ohne_score: basis_voll` würde 40 € fordern. Ohne `regel: rate` meldete `rate_abweichung` diesen gewollten Zustand dauerhaft als Verstoß.
2. **14,5 % gegen 10 % Cap.** Laut Owner-Strategie „bewusst übergewichtet" (Software-These). Die Nullrate ist genau der Mechanismus, über den sich die Position organisch unter den Cap zurückbilden soll — bis dahin ist die Cap-Verletzung gewollt. Ohne `regel: cap_single_stock` liefe `cap_single_stock` monatelang auf FAIL.

Beide Fälle sind strukturell gleich: bewusst akzeptierte Abweichung, nur an unterschiedlichen Checks. Genau davor warnt §3.3 selbst — eine Warnung, die immer leuchtet, wird nicht gelesen.

Abgrenzung: `screener_exceptions` bleibt ein eigener Mechanismus (Methodik-Ausnahme bei der Bewertung, nicht Abweichung von einer Portfolio-Regel) und wird hier nicht mit vermischt.

---

## 4 · Urteil-Layer

Schreibwege bleiben. Das Schema erhält **eine** additive Erweiterung (§4.1) — sie erzwingt einen Versions-Bump und ist damit kein Nebeneffekt, sondern ein eigener Migrationsschritt. Neuerung im Übrigen: der Layer wird gelesen statt kopiert. Die Ableitungsregeln aus v1.0 waren zu grob und sind hier ersetzt.

### 4.1 Aktueller Score — Dateireihenfolge, nicht Datum

**Regel:** Der aktuelle Score ist der **letzte Record je Ticker in Dateireihenfolge**, nicht das Maximum nach `score_datum`.

Begründung, empirisch: `score_history.jsonl` enthält für V zwei Record-Paare mit identischem `score_datum` — Zeile 25/26 (2026-04-18: `vollanalyse` 72, dann `rescoring` 63) und Zeile 29/30 (2026-04-28: `vollanalyse` 68, dann `rescoring` 64). Eine Ableitung nach „jüngstes Datum" ist bei Tages-Kollision nicht eindeutig und lieferte im Test 68; `PORTFOLIO.md` führt 64. Die Datei ist append-only, also ist ihre Reihenfolge die Wahrheit: ein `rescoring` korrigiert die `vollanalyse` desselben Tages, weil es danach geschrieben wurde.

- **Verfallen:** `heute − score_datum > verfall_tage`.
- **Kein Record:** Fall `ohne_score`, nicht Score 0 und kein Platzhalter.

**Absicherung.** Dass die Wahrheit an der physischen Zeilenreihenfolge hängt, ist ohne Schutz fragil — eine Merge-Konflikt-Auflösung oder ein Reformat könnte sie unbemerkt ändern. Zwei Maßnahmen:

1. **Neue Records tragen `geschrieben_am`** (ISO-Zeitstempel des Schreibvorgangs, unabhängig von `score_datum`). Die Ableitung nutzt dieses Feld, wo vorhanden; die Dateireihenfolge bleibt Rückfallebene für die 37 Alt-Records.

   **Das ist kein Ein-Zeilen-Eingriff.** `schemas.py` Z. 364 setzt `ConfigDict(extra="forbid")`, Z. 366 `schema_version: Literal["1.0"]`. Ein Record mit unbekanntem Feld wird von **jedem** Validator abgelehnt — `jsonl_schema.py` (Z. 34/38), `validate_score_history.py` (Z. 132, Pre-Commit) und dem Schreibweg `archive_score.py` (Z. 39/201). Erforderlich ist deshalb:
   - `schema_version` auf `Literal["1.0", "1.1"]` erweitern, `geschrieben_am` als `str | None = None` (optional, damit die 37 Alt-Records gültig bleiben);
   - `sum_consistency.py` mitziehen: dort gilt „v1.0 grandfathered, v2.0+ strict" — ein `1.1`-Bump muss bewusst eingeordnet werden, sonst kippt die Allowlist-Logik unbemerkt;
   - der Bump gehört in **Stufe 2 Schritt 9**, gemeinsam mit der Gate-Neufassung. Bis dahin trägt die Dateireihenfolge allein, abgesichert durch den bestehenden Append-only-Check.
2. **Append-only-Invariante wird geprüft.** Für `score_history.jsonl` **existiert das bereits**: `03_Tools/precommit/validate_score_history.py::check_append_only` (Z. 82–136), verdrahtet als Pre-Commit-Hook. Für `flag_events.jsonl` fehlt es — `validate_flag_events.py` prüft nur Schema und Open/Resolve-Paarung. Der Umbau ergänzt also **einen** Check, nicht zwei, und schließt eine Lücke, die schon heute besteht.

### 4.2 FLAG-Status — erst nach Vollständigkeits-Backfill ableitbar

**Regel:** aktiv, wenn das letzte Event je (Ticker, `flag_typ`) ein `trigger` ohne nachfolgendes `resolve` ist.

**Diese Regel ist heute nicht anwendbar.** `flag_events.jsonl` enthält vier Trigger (MSFT, GOOGL, AVGO, AMZN). APH trägt seit 2026-04-09 einen Score-basierten FLAG in `config.yaml` und `PORTFOLIO.md`, für den **kein** Event existiert. Umgekehrt trägt GOOGL einen Trigger vom 2026-03-15 ohne Resolve, der in keiner der beiden gelesenen Dateien auftaucht — bei einem Titel, der seit 26.08. mit 50 €/Monat bespart wird.

**Daraus folgt Stufe 0 (§9.3):** Vor jeder Ableitung wird `flag_events.jsonl` auf Vollständigkeit gebracht — APH-Trigger nachtragen, GOOGL-Trigger entweder auflösen oder als aktiv bestätigen. Erst danach ist die jsonl autoritativ. Ohne diesen Schritt würde der Umbau einen bestehenden Datenfehler zementieren, statt ihn zu beheben.

### 4.3 Nicht-Roster-Ticker

`score_history.jsonl` enthält 26 Ticker, davon 14 ohne aktuelle Roster-Zugehörigkeit (MKL, SNPS, SPGI, HON, FICO, NVDA, RACE, SAP, EXPN, ZTS, FFH.TO, PEGA, VEEV, COST). Die Historie bleibt vollständig erhalten — sie ist die Backtest-Grundlage.

`depot check` wertet nur Roster- und Depot-Ticker gegen Regeln aus. Watchlist-Einträge behalten ihren Score als Information, unterliegen aber keiner Analyse-Pflicht und keinem Regel-Check. Ein Ticker, der ins Roster zurückkehrt, bringt seine Historie automatisch mit.

### 4.4 Zwei Gates im Score-Schreibpfad müssen neu gefasst werden

Schreibwege bleiben im Grundsatz: `score_history.jsonl` via `backtest-ready-forward-verify` (Schritt 7), `flag_events.jsonl` via `archive_flag.py`, beide mit `provenance_gate.py` inklusive §27.7-Carryover-Asymmetrie und §27.8-Bull-Source-Pflicht.

**Eine Ausnahme, die v1.1 übersehen hatte.** `03_Tools/backtest-ready/_forward_verify_helpers.py` Z. 26 definiert

```python
REQUIRED_TOUCH_FILES = ("PORTFOLIO.md", "Faktortabelle.md", "log.md")
```

`check_freshness()` (Z. 256 ff.) lässt einen `vollanalyse`-Record nur durch, wenn alle drei im `git status` als modifiziert erscheinen. Das Gate beweist heute: „Die Analyse wurde von den erforderlichen Zustands-Updates begleitet."

Werden `PORTFOLIO.md` und `Faktortabelle.md` zu generierten Artefakten, **scheitert das Gate nicht — es wird bedeutungslos.** Der Generator fasst beide Dateien bei jedem Lauf an, das Gate ist damit immer erfüllt und schützt nichts mehr. Das ist die gefährlichere Variante, weil sie unsichtbar bleibt.

**Das gilt nur für den ersten von zwei Abnehmern.** `check_freshness()` liefert seine Fehlliste an eine zweite Stelle: `provenance_gate.py` Z. 176–181 blockiert damit in Phase P3.5 **fail-close**, sobald `analyse_typ == "vollanalyse"` — laut `SKILL.md` Z. 106 ohne Archiv-Write. Für 35 der 37 Records ist Gate 1 also nicht bedeutungslos, sondern hart. Wird `PORTFOLIO.md` generiert, ohne dass der Generator garantiert **vor** jedem Forward-Verify-Lauf läuft, scheitert jeder Vollanalyse-Write sofort. Beide Fehlerbilder existieren damit gleichzeitig: unsichtbar in P2a, blockierend in P3.5. Die datei-lokale Prüfregel aus der R3-Lehre greift hier nicht — der zweite Abnehmer steht in einer anderen Datei, aber im selben Datenfluss.

**Neufassung ab Stufe 2 Schritt 9:** Das Required-Touch-Set wird auf das reduziert, was noch von Hand entsteht und den Nachweis tatsächlich trägt:

```python
REQUIRED_TOUCH_FILES = ("log.md",)          # Chronik, weiterhin handgeschrieben
# zusätzlich: REGELWERK.yaml, wenn die Analyse eine Regel geändert hat
```

Die Umstellung gehört **in denselben Schritt** wie die View-Generierung, nicht danach — sonst existiert ein Fenster, in dem das Gate scheinbar grün ist und nichts prüft.

#### Gate 2 — die Tripwire P2b, härter und in derselben Datei

`SKILL.md` Z. 104–105 unterscheidet zwei Phasen: P2a (Freshness) ist **Warnung, nicht blockierend**. **P2b (Tripwire) ist FAIL-blockierend** — Z. 147: „Pipeline abbrechen … Kein Archiv-Write."

P2b ruft `parse_state_row(ticker, PORTFOLIO.md)` (`_forward_verify_helpers.py` Z. 152–191) und vergleicht Score, DEFCON und FLAG des Entwurfs gegen `PORTFOLIO.md`. Der Parser liest die Markdown-Tabelle **spaltenoffset-basiert relativ zum Ticker**:

```
Ticker  +1=Score  +2=DEFCON  +3=Rate  +4=FLAG
```

Sein eigener Docstring (Z. 165–169) dokumentiert, dass die Juni-Umstrukturierung eine `Tier`-Spalte vorangestellt hat und er deshalb auf Ticker-relative Offsets umgebaut werden musste. **Er ist an genau dieser Ursache bereits einmal gescheitert.**

Das Fehlerbild ist schärfer als bei Gate 1: Nicht Bedeutungslosigkeit, sondern **harter Stopp des gesamten Score-Schreibwegs**. Ändert sich die Spaltenfolge, greift entweder `ticker_idx + 4 >= len(cells)` (Zeile wird übersprungen → `ValueError: ticker not found` → `FAIL P2b`) oder der FLAG wird aus der falschen Spalte gelesen. Beides trifft jeden Ticker, nicht nur einen.

**Neufassung, ebenfalls Stufe 2 Schritt 9:** Die Tripwire vergleicht künftig gegen den **abgeleiteten Zustand** (`score_history.jsonl` + `flag_events.jsonl` + `REGELWERK.yaml`), nicht gegen eine generierte Markdown-Ansicht. Ein Entwurf gegen ein Artefakt zu prüfen, das aus derselben Quelle gebaut wird, wäre ohnehin zirkulär. `parse_state_row` entfällt damit ersatzlos — ein weiterer Posten auf der Rückbau-Seite von §1.2.

**Lehre für die Bearbeitung dieser Spec:** Beide Gates stehen in derselben Datei, Z. 152 und Z. 256. v1.2 hat eines repariert und die Datei nicht nach Geschwistern durchsucht. Wenn eine Korrektur eine Datei berührt, wird die ganze Datei auf gleichartige Abhängigkeiten geprüft, nicht nur die gemeldete Zeile.

---

## 5 · Live-Layer

- Kanal: CLI `sc` v0.6.0 in WSL-Distro **Ubuntu-24.04**; MCP-Connector als Alternative.
- Envelope: mit `--json` kommt `{ok, command, data}`, Nutzdaten unter **`data.result`**.
- Cache: `00_Core/.live/snapshot.json` mit Zeitstempel, **in `.gitignore`**.
- Staleness: älter als 12 h → neu ziehen; `--cached` erzwingt den Cache.
- **Filter beim Cachen:** `get_portfolio_holdings` liefert zusätzlich 32 `cryptoHoldings`-Blöcke, alle mit `filled: 0`. Der Snapshot verwirft sie; andernfalls besteht der Cache überwiegend aus Nullpositionen.
- `sc login` ist `human_only`; bei abgelaufener Session bricht der Befehl mit klarer Meldung ab, statt auf veralteten Daten zu rechnen.

**Kein Point-in-Time-Persistenzbedarf.** `score_history.jsonl` enthält keine Positionen und keine Raten, nur Score, Sub-Scores, FLAG-Metrik und Kurs am Score-Tag. Positions- und Orderhistorie liegt bei Scalable (`transactions` reicht nachweislich bis 18.06. zurück). §29.5 Sin #2 (Look-Ahead) bleibt unberührt.

---

## 6 · Analyse-Pflicht

Die Pflicht ist eine **Abfrage, kein Verwaltungsobjekt**. Es gibt keine Backlog-Liste zu pflegen; der Backlog ist das Ergebnis von `analyse_faellig`. Handgeschriebene Backlogs driften — die Liste vom 26.08. führte Alphabet und Veeva, obwohl beide gültige Records haben.

Eingaben, alle vorhanden: letzter Score je Ticker · nächster Earnings-Termin (`earnings_calendar.py`, SSoT) · Klasse und Kadenz (Regelwerk) · Depotanteil (Live-Layer).

### 6.1 Kadenz

| Pflicht | gilt für | Titel heute | pro Jahr |
|---|---|---|---:|
| **je Earnings** (quartalsweise) | Klasse `core` · Anteil > 5 % am Gesamtdepot · aktives FLAG | GOOGL, MSFT, AMZN, META (core) · NOW (14,5 %) · AVGO, APH (FLAG) = **7** | 28 |
| **halbjährlich** | übrige Satelliten, via 180-Tage-Regel | ASML, V, TMO, SU, BRK.B, RMS, ZETA, Adobe, Veeva = **9** | 18 |
| **keine** | Themenwetten (JEDI, WQTM), ETF, Gold | — | — |

Zusammen ≈ 46 Analysen im Jahr, knapp eine pro Woche. Zum Vergleich: 13 in fünf Monaten.

MSFT und AMZN erfüllen zwei Kriterien gleichzeitig (Klasse `core` und aktives FLAG) und zählen einmal. Bei Klasse `core` ist Analysepflicht ohnehin der Regelfall.

### 6.2 Zwei Stufen

| | `quartals-update` — Regelfall | `vollanalyse` — Ausnahme |
|---|---|---|
| Fundamentals · Technicals · Sentiment · Insider | frisch erhoben | frisch erhoben |
| Moat · Tariff | `_carryover` nach §27.7 | frisch hergeleitet |
| Auslöser | jeder Pflicht-Earnings-Termin | DEFCON-Schwelle gerissen · FLAG-Trigger · `moat_drift_trigger` · Neuaufnahme · Score älter als `verfall_tage` |

Beide schreiben einen vollwertigen Record. Kein neuer Skill: `analyse_typ` trägt bereits zwei Werte (`vollanalyse` 35×, `rescoring` 2×), `provenance_gate.py` prüft die Carryover-Disziplin schon heute.

**§27.7 trägt das Modell ohne Änderung:** `_carryover`-markierte Sub-Scores dürfen nur unverändert übernommen werden. Up-Scoring ist Verstoß, Down-Scoring bleibt zulässig — ein Burggraben verbessert sich nicht ohne neue Evidenz, verschlechtert sich aber sehr wohl.

**§19.1 bleibt gültig:** Tag 0 Press-Release-Recap plus FLAG-Quick-Check, Score-Move erst Tag +1 mit Transcript. Ausnahme BRK.B (kein Quarterly Call, Trigger = 10-Q).

---

## 7 · `depot check`

Ablauf: Zustand ziehen → Regelwerk laden → Urteil ableiten → SOLL rechnen → gegen IST diffen → melden → Views bauen.

### 7.1 Checks

| Check | meldet | Konflikt aus Reconciliation §C |
|---|---|---|
| `regel_flag` | Rate > 0 trotz FLAG, wo Klasse `rate_null` fordert — **außer** ein gültiger Override greift (§3.3) | C1 — 135 €/Mt |
| `score_fehlt` | Position oder Sparrate ohne Record | C2 — Adobe, META, NOW, ZETA |
| `score_verfallen` | letzter Record älter als `verfall_tage` | — |
| `analyse_faellig` | Pflichttermin nach §6.1 erreicht oder überfällig | — |
| `cap_single_stock` | Position über `single_stock_max_pct` | C3 — NOW 14,5 % |
| `slot_kapazitaet` | belegte Aktien-Slots über `max_aktien_slots` | — (Tool B12 gegen B13) |
| `cap_us` | US-Quote **Ist** über `us_hard_cap_pct` | — |
| `cap_us_ziel` | US-Quote der **Ziel**-Allokation über Cap, je Position gewichtet | — (Tool-Funktion) |
| `rate_abweichung` | Ist-Rate ≠ SOLL nach additivem Modell (§7.4) | C4 — 3-Tier unwirksam |
| `freigesetzt_ohne_ziel` | eingefrorener Betrag, für den die Staffel aus §7.4 kein Ziel findet | — |
| `roster_fremd` | in **Position ∪ Sparplan**, nicht im Regelwerk | C5 — Adobe, Costco, Veeva |
| `roster_verwaist` | im Regelwerk, weder Position noch Sparplan | C5 — KYCCF |
| `allokation_drift` | Block-Abweichung über `toleranz_pp` (getrennt ETF/Gold und Aktien) | Gold 2,7 % vs. 5 % |
| `position_drift` | Einzelposition außerhalb Toleranz → Reduzieren / Aufstocken / Halten | — (Tool Spalte L) |
| `nachkauf_signal` | Fehlbetrag über `nachkauf_schwelle_eur`; bei FLAG „gesperrt" statt Kaufsignal | — (Tool Spalte J/R) |
| `flag_gate_faellig` | Resolve-Gate-Termin erreicht | AVGO 03.09. |
| `override_faellig` | Override über `review_am` hinaus aktiv | — |

C6 (Broker-Modell überholt) braucht keinen Check: Broker ist Zustand und hört auf, eine Regel zu sein.

Schweregrade: **FAIL** = Regelverstoß · **WARN** = Drift in Toleranznähe, Fälligkeit in Sicht, abgelaufener Override · **INFO** = aktiver gültiger Override.

### 7.2 Verteilungsrechnung

Aus `Rebalancing_Tool_v4.0.xlsx` ausgelesen, nicht aus der Prosa-Dokumentation übernommen — die beiden widersprechen sich, siehe §7.3.

Fundstellen für die Reproduktion: Die Formeln stehen auf Blatt **`Portfolio & Rebalancing`** (Bereich A1:R36), Spalte Q (Gewicht) und Spalte P (Rate). Blatt **`Parameter & Regeln`** (A1:C65) hält nur die Parameter, auf die diese Formeln per Cross-Sheet-Referenz zugreifen (`'Parameter & Regeln'!$B$4` usw.).

**Zwei getrennte Mechanismen, die die bisherige Doku vermengt hat.**

**(a) Sparraten-Verteilung — proportionale Normierung.**

```
Gewicht  Q_i = 0                       falls FLAG aktiv oder DEFCON 1
              tier_basis(i) × 0,5      falls DEFCON 2
              tier_basis(i)            sonst
Rate     P_i = Sparrate × Aktienanteil × Q_i / Σ Q     (nur Aktien)
```

ETF und Gold laufen **nicht** über diese Formel, sondern über feste Raten je ISIN aus dem Regelwerk.

Entscheidend: Die Tier-Basis wirkt als **relatives Gewicht**, nicht als Euro-Betrag. Fällt ein Titel auf Q = 0, sinkt der Nenner, und alle übrigen bekommen mehr als ihre Tier-Basis. Das Aktienbudget ist immer vollständig verteilt.

**(b) Nachkauf-Signal — wertbasiert.** Fehlbetrag zwischen Ziel- und Ist-Wert je Position; über `nachkauf_schwelle_eur` ein Einmalkauf-Signal, bei aktivem FLAG als „gesperrt". Das ist der value-based Teil — er betrifft Einmalkäufe, nicht die Sparrate.

Ausgabe ist ein **Vorschlag**, kein Auftrag. Sparplan-Änderungen laufen über den Two-Phase-Weg mit getrennter Bestätigung.

### 7.3 Vorgefundener Widerspruch (Befund 2026-08-26)

`PORTFOLIO.md` und `config.yaml system_regeln.sparplan_verteilung` beschreiben ein additives Modell: „SOLL-Σ = 364 €, Funded-Σ = 210 €, Differenz 154 € wird value-based auf untergewichtete Positionen umgelenkt." Das Tool rechnet anders. Beim dokumentierten Juni-Stand (Σ Q = 210):

| Titel | laut `PORTFOLIO.md` | laut xlsx-Formel | Ist-Rate 26.08. |
|---|---:|---:|---:|
| NOW | 40 € | **69,32 €** | 35 € |
| ASML | 32 € | **55,46 €** | 35 € |
| V (D2-Sockel) | 16 € | **27,73 €** | 35 € |
| RMS · BRK.B · TMO · SU · ZETA | je 18 € | **je 31,20 €** | je 20 € |

Drei Quellen, drei Ergebnisse. Grund für die lange Unsichtbarkeit: Σ aller Tier-Basen (4×40 + 3×32 + 6×18 = 364) ist zufällig gleich dem Aktienbudget (1031 × 0,353 = 363,94). Ohne gesperrte Titel liefern beide Modelle dasselbe. Erst mit dem ersten FLAG laufen sie auseinander — und seit April tragen dauerhaft vier Titel ein FLAG.

Genau genommen sind es drei Doku-Stellen gegen eine Formel: `PORTFOLIO.md`, `config.yaml system_regeln.sparplan_verteilung` und `INSTRUKTIONEN §22` (Z. 539) beschreiben übereinstimmend das additive Modell. Allein die xlsx normiert. Das entkräftet den Verdacht, die Prosa sei die nachlässige Seite — sie war konsistent, die ausführbare Schicht wich ab.

Kein Fehler dieser Spec, sondern ein Befund über den Ist-Zustand. Er stützt die Begründung des Umbaus: Rechenlogik, die in einer Tabellenformel steckt und in Prosa nacherzählt wird, driftet unbemerkt. In `depot check` ist sie einmal vorhanden und ausführbar.

### 7.4 Entscheidung: additiv mit gestaffeltem Ziel (Owner-Freigabe 2026-08-26)

**Gewählt: `modell: additiv`.** Die Tier-Basis bedeutet Euro. „Tier 1 = 40 €" ist wahr, ohne dass man den FLAG-Zustand aller dreizehn Titel kennen muss.

**Gegen die Normierung sprach die Kopplung.** Friert AVGO wegen Insider-Verkäufen ein, bekäme ASML unter der Normierung 73 % mehr als seine Conviction-Stufe hergibt — obwohl sich an ASML nichts geändert hat. Ein FLAG ist ein Veto gegen *diesen* Titel, keine Aussage über die übrigen. Dieselbe Undurchsichtigkeit hat den Drift zwischen Tabelle und Doku monatelang verdeckt.

**Freigewordene Beträge haben ein gestaffeltes Ziel**, nicht bloß eines:

| Lage | Ziel | Grundlage |
|---|---|---|
| DEFCON 1 oder Owner-Veto, Ersatz mit Score ≥ 80 und ohne FLAG vorhanden | Sparplan auf den Ersatz umleiten | `substitute_activation_global`, bestehende Regel |
| FLAG bei DEFCON 2/3 — kein Substitutionsfall | Block mit dem größten Untergewicht | `allokation_drift`, ohnehin berechnet |
| alle Blöcke auf Zielquote | ETF-Core | Rückfall |

Die erste Stufe ist keine Erfindung dieser Spec, sondern die bestehende Ersatzbank-Regel inklusive ihrer Steuerlogik („niemals durch Verkauf tauschen"). Eine flache Regel „alles nach Gold" hätte sie stillschweigend übersteuert.

**Nie diffus auf die übrigen Satelliten.** Sonst entsteht ein Kreis: Der Satelliten-Block fällt durch das Einfrieren unter Ziel, `allokation_drift` meldet Untergewicht, und das Geld liefe zurück in genau den Block, aus dem es wegen eines Risikos abgezogen wurde. Ein **benannter** Ersatz ist davon nicht betroffen — er ist eine Einzelentscheidung, keine Streuung.

**Größenordnung heute.** Die Klassen-Zweiteilung hat das Problem weitgehend aufgelöst: MSFT und AMZN werden `core` und frieren nicht mehr ein, APH läuft über einen Override. Von den ursprünglich 135 €/Monat bleibt **AVGO mit 40 €**. Score 56 = DEFCON 2, also kein Substitutionsfall → Stufe 2 der Staffel, Ziel Gold (2,7 % gegen 5 %). Das Cash-Drag-Argument, das für die Normierung sprach, trägt bei dieser Größe nicht mehr.

**Bekannter Nebeneffekt:** Bei lange aktiven FLAGs verschiebt sich die Quote vorübergehend zugunsten von Gold und ETF. Das ist gewollt — ein materialisiertes Einzeltitel-Risiko soll in die breite Basis fließen, nicht in andere Einzeltitel. Sichtbar bleibt es über `allokation_drift`; still ist es nicht.

---

## 8 · Generierte Artefakte

Nie von Hand editieren. Bleiben committed und lesbar wie heute; geändert wird die Quelle.

| Artefakt | gebaut aus | Zweck |
|---|---|---|
| `PORTFOLIO.md` | Regelwerk × Urteil × Live | Session-Start-Lesedatei, unveränderte Rolle |
| `Faktortabelle.md` | `score_history.jsonl` | Sub-Score-Detail |
| `config.yaml` | Regelwerk + Urteil + `earnings_calendar.py` | Kompatibilität für `dynastie-depot`, das unverändert weiterläuft |
| Vault-Entity-Frontmatter | Regelwerk + Urteil | **Vorerst zurückgestellt.** Heute tragen drei Ersatzbank-Seiten Score-Frontmatter, das Standardschema keines. Frontmatter für alle Roster-Ticker zu generieren wäre additive Arbeit und fiele unter die Anti-Creep-Regel (§1.2). Entscheidung nach Stufe 2. |

Jedes generierte File trägt einen Kopfhinweis („generiert von `depot check`, nicht editieren") und wird beim Bau vollständig ersetzt.

---

## 9 · Migration

### 9.1 Blast-Radius (korrigiert nach Codex-R1-H1)

**Zwei Korrekturen gegenüber den Vorfassungen, beide derselbe Methodenfehler: Mustervergleich statt Codelesen.**

*v1.0 behauptete*, `insider_intel.py` und `screen.py` schrieben `config.yaml` — eine Heuristik hatte „Datei schreibt irgendetwas" mit „schreibt dieses Ziel" gleichgesetzt. Nachgeprüft: `insider_intel.py` Z. 845 trägt den Kommentar „Schreibt NIE config.yaml."; der einzige Write ist `Faktortabelle.md` (Z. 908). `screen.py` hat genau einen File-Write (Z. 315), eine CSV-Ausgabe.

*v1.1 übersah das gesamte Verzeichnis `03_Tools/backtest-ready/`*, weil der Ordnername die Zeichenfolge „test" enthält und ein Filter ihn deshalb als Testcode einstufte. Tatsächlich sind **11 von 13 Dateien dort produktiv**, darunter `archive_flag.py` und `archive_score.py` — die beiden Schreibwege, die diese Spec selbst als kanonisch benennt.

Produktive Konsumenten, bereinigt um echte Tests (`test_*`, `*_test.py`, `_smoke_test*`), Fixtures und `.claude/skills`-Junctions:

| Datei | Zugriff | betrifft |
|---|---|---|
| `01_Skills/insider-intelligence/insider_intel.py` | **schreibt** `Faktortabelle.md`; liest `config.yaml` | Faktortabelle, config |
| `01_Skills/quick-screener/scripts/screen.py` | liest | config |
| `03_Tools/earnings_calendar.py` | liest | PORTFOLIO, config |
| **`03_Tools/backtest-ready/_forward_verify_helpers.py`** | **liest PORTFOLIO/Faktortabelle als Freshness-Gate** (§4.4) und parst die Portfolio-Tabelle (Z. 154/191) | PORTFOLIO, Faktortabelle |
| **`03_Tools/backtest-ready/provenance_gate.py`** | konsumiert das Gate | PORTFOLIO, Faktortabelle |
| **`03_Tools/backtest-ready/archive_score.py` · `archive_flag.py`** | **schreiben die beiden jsonl** — kanonischer Urteil-Schreibweg | jsonl |
| **`03_Tools/backtest-ready/schemas.py`** | **definiert `ScoreRecord`/`FlagEvent` mit `extra="forbid"` + `schema_version: Literal["1.0"]`** (Z. 364/366, 605/606) | jsonl-Schema |
| `03_Tools/para18_sync/validator.py` | liest | xlsx (Pfad hart codiert, §9.2) |
| `03_Tools/precommit/para18_sync_reminder.py` | liest | alle sechs (xlsx-Zweig hart auf `03_Tools/`) |
| `03_Tools/precommit/validate_flag_events.py` · `validate_score_history.py` | liest | PORTFOLIO, jsonl |
| `03_Tools/system_audit/checks/` (**7 von 17 Checks**: `cross_source`, `cross_source_reverse`, `score_event_parity`, `existence`, `jsonl_schema`, `markdown_header`, `sum_consistency`) | liest | alle; `existence.py` zusätzlich Pfad-Existenz aus Markdown; `cross_source.py` überspringt die Vault-Quelle still (Z. 184, 332–334) |
| **`.pre-commit-config.yaml`** | **Fundort der hart codierten Pattern** — Z. 61 (§18-Reminder, sechs Alternativen) und Z. 110 (`^03_Tools/.*\.xlsx$`) | xlsx, alle Markdown-SSoT |

### 9.2 Zwingende Anpassungen

- **`insider_intel.py`** → schreibt FLAG-Befunde nach `flag_events.jsonl` statt in `Faktortabelle.md`; `factor-sync` entfällt, weil es Kopien vergleicht, die es nicht mehr gibt.
- **`screen.py`** → liest Roster und Watchlist aus `REGELWERK.yaml` statt `config.yaml`. Kein Write-Umbau nötig.
- **`earnings_calendar.py`** → liest Roster aus `REGELWERK.yaml`, liefert Termine an den `depot check`-Build statt nach `PORTFOLIO.md`.
- **`para18_sync/validator.py`** → `tools_dir = PROJECT_ROOT / "03_Tools"` ist hart codiert (Z. 441/444/468). Nach dem xlsx-Move findet es die Dateien nicht mehr. Es **bricht dabei nicht** — bei 0 Glob-Matches setzt es nur eine Warnung und läuft weiter (Z. 447–449); FAIL gibt es allein beim Semver-Tie (Z. 458–467). Die Stilllegung gehört trotzdem **in Stufe 1**: sonst warnt ein Pre-Commit-Validator ab dem Move bei jedem Commit über Dateien, die absichtlich weg sind — und eine Warnung, die immer leuchtet, wird nicht gelesen (§3.3). Nebenbei: greift der `SYSTEM.md`-Pin, übernimmt Z. 444 den Pfad ohne Existenzprüfung.
- **`precommit/para18_sync_reminder.py`** → **bleibt in Stufe 1 aktiv.** Sein Pattern (`.pre-commit-config.yaml` Z. 61) hat sechs Alternativen; nur eine betrifft xlsx und verstummt nach dem Move von selbst. Die übrigen — `PORTFOLIO.md`, `config.yaml`, `CORE-MEMORY`, `PIPELINE`, `SYSTEM`, `STATE` — bleiben durch Stufe 1 hindurch relevant, weil diese Dateien bis Stufe 2 handgepflegt sind. Der Rückbau gehört in Stufe 2 Schritt 11, nicht in Schritt 7.
- **`precommit/xlsx_smoke_test.py`** → sein Hook ist auf `^03_Tools/.*\.xlsx$` verankert und verstummt nach dem Move automatisch. Die Stilllegung ist Hygiene, keine Sicherheitsvoraussetzung.
- **`system_audit/checks/existence.py`** → prüft Backtick-Pfade aus Markdown gegen die Platte. `CLAUDE.md`, `INSTRUKTIONEN.md` und `SYSTEM.md` (§Active xlsx-Filenames) referenzieren die drei xlsx unter `03_Tools/`. Diese Referenzen müssen im selben Schritt entfernt werden, sonst erzeugt der Move neue FAILs.
- **`system_audit`** → die drei Cross-Source-Checks entfallen (`cross_source.py`, `cross_source_reverse.py`, `score_event_parity.py`, zusammen 899 Z.). `existence.py`, `markdown_header.py`, `jsonl_schema.py` und `sum_consistency.py` bleiben, ziehen aber auf die neuen Pfade um — **`sum_consistency.py` zusätzlich beim `schema_version`-Bump aus §4.1**, da es v1.0 anders behandelt als v2.0+. Die übrigen 12 Checks sind nicht betroffen.
- **`INSTRUKTIONEN.md §22`** → die hartcodierte Positionstabelle (Z. 542–556) entfällt; die Formel wird durch den Verweis auf `REGELWERK.yaml` + §7.4 ersetzt. Der Abschnitt führt heute Scores, DEFCON-Stufen und Raten für alle 13 Titel und ist damit eine vollwertige Score-Kopie, die in v1.4 weder in §1.1 noch in den Sync-Zielen auftauchte. **Kein Skript liest ihn** — ein Grep über alle `.py` findet ausschließlich §18-Bezüge, nie §22. Der Rückbau ist deshalb reine Dokumentationsarbeit ohne Code-Risiko und **gehört in Stufe 2 Schritt 11**, gemeinsam mit der §18-Neufassung.

**`CLAUDE.md` ist damit Sync-Ziel der Migration** — in v1.0 fehlte es ganz, in v1.4 war es auf „xlsx-Referenzen entfernen" verengt. Tatsächlich betroffen sind sechs Stellen (Z. 27, 29, 57, 59, 77, 78), darunter der vollständige Sync-Pflicht-Bullet, der das alte 8-9-Datei-Modell im Fließtext festschreibt, sowie zwei Routing-Zeilen, die `paragraph-18-sync` aufrufen. Weil die Datei zu Beginn **jeder** Session gelesen wird und darüber entscheidet, ob `INSTRUKTIONEN.md` überhaupt lädt, ist sie kein nachlaufendes Sync-Ziel, sondern gehört in denselben Commit wie der Move. Eine dort stehen gebliebene Sync-Anweisung wirkt stärker als jede korrigierte Spec.

### 9.3 Stufe 0 — Datenreparatur, Voraussetzung für alles Weitere

Ohne diesen Schritt zementiert der Umbau bestehende Fehler.

1. `flag_events.jsonl` vervollständigen: APH-Trigger (seit 2026-04-09, score-basiert) nachtragen.
2. AMZN-FLAG in `config.yaml flags_aktiv` ergänzen oder die Divergenz begründen.
3. Danach ist `flag_events.jsonl` die einzige gelesene Quelle. Deckungsgleich sind die Listen damit **nicht** — GOOGL bleibt bewusst divergent, bis eine Analyse den Trigger auflöst oder bestätigt (siehe folgender Absatz). Das ist kein Restfehler, sondern der Unterschied zwischen „eine Quelle ist maßgeblich" und „alle Kopien stimmen überein". Genau diesen Unterschied stellt der Umbau her.

**Der GOOGL-Trigger gehört nicht hierher.** Ihn aufzulösen erfordert nach dem eigenen Modell frische Evidenz (§4.2) — das ist Analysearbeit, keine Datenhygiene. Bis dahin gilt die konservative Lesart: **ein Trigger ohne Resolve ist aktiv.** Das Modell trägt den Fall von selbst, weil GOOGL Klasse `core` ist und `flag_wirkung: analysepflicht` gilt: Der offene FLAG stoppt keine Rate, sondern macht GOOGL über `analyse_faellig` (§6.1) analysepflichtig. Der Titel landet damit im Analyse-Backlog, wo er hingehört — und nicht in einem Reparaturschritt, der ihn stillschweigend wegräumt.

**Zusatz: der Vault hält eine gegenläufige Entscheidung.** `entities/ersatzbank/GOOGL.md` führt GOOGL als „struktureller Ausschluss seit 01.04.2026 — kein Einstieg", während seit dem 26.08. ein Sparplan über 50 €/Mt läuft und die Klassenregel `core` + `flag_wirkung: analysepflicht` die Rate ausdrücklich nicht stoppt. Der Umbau würde damit eine dokumentierte Ausschluss-Entscheidung stillschweigend aufheben — genau die stille Regeländerung, gegen die §3.3 argumentiert. **Stufe 0 trägt daher zusätzlich:** entweder die Ausschluss-Entscheidung wird schriftlich aufgehoben (Chronik-Eintrag mit Datum und Begründung), oder GOOGL bekommt einen Override nach §3.3 mit `grund`, `seit` und `review_am`. Die Vault-Seite wird in beiden Fällen mitgezogen. Was nicht zulässig ist: die Divergenz unkommentiert stehen zu lassen.

### 9.4 Stufe 1 — begrenzter Blast-Radius

5. `REGELWERK.yaml` anlegen und befüllen; Klassen nach §3.1, Ersatzbank nach §3.2, Overrides nach §3.3. **Voraussetzung: laufender Live-Layer** — die ISINs des Rosters existieren nirgends im Repo und werden einmalig aus `holdings ∪ savings_plans` gezogen. Für Roster-Titel ohne Position **und** ohne Sparplan ist die ISIN von Hand zu ergänzen. Stufe 1 ist damit nicht offline durchführbar.
6. `depot check` als reiner Report bauen (Live-Layer, Checks, Verteilungsrechnung). Noch kein View-Bau.
7. Die drei xlsx nach `05_Archiv/` verschieben — **gemeinsam** mit: Stilllegung von `xlsx-smoke-test-runner` und `precommit/xlsx_smoke_test.py`, Fix von `para18_sync/validator.py` (hart codierter Pfad), und Entfernen der xlsx-Referenzen aus `CLAUDE.md`, `INSTRUKTIONEN.md`, `SYSTEM.md`. **`para18_sync_reminder.py` bleibt aktiv** (§9.2).
   Zu Schritt 7 gehört zusätzlich die Neufassung von **`CLAUDE.md`**, und zwar über die xlsx-Dateinamen hinaus: der Sync-Pflicht-Bullet (Z. 27) beschreibt das alte 8-9-Datei-Modell im Fließtext, die Routing-Zeile „§18-File-Touch" (Z. 78) und die `!ParaSync18`-Zeile (Z. 77) rufen einen Skill, der zurückgebaut wird, und die Projektstruktur (Z. 57/59) führt `paragraph-18-sync`, `xlsx-smoke-test-runner` sowie alle drei xlsx als aktives Inventar. Bleibt das stehen, folgt der Agent nach dem Move weiter der alten Prosa — mit zwei konkreten Folgen: manuelles Editieren von `PORTFOLIO.md` entgegen §8, und Suche nach xlsx-Pfaden, die es nicht mehr gibt.
**Was Stufe 1 ausdrücklich NICHT tut:** die Tabellenstruktur von `PORTFOLIO.md` anfassen. Der ursprüngliche Schritt „Live-Felder entfernen" ist nach Stufe 2 verschoben, weil die Tripwire ihre Spalten offsetbasiert liest (§4.4 Gate 2). Fiele die `Rate`-Spalte in Stufe 1 weg, rückte FLAG von Ticker+4 auf Ticker+3 — der Score-Schreibweg bräche **in Stufe 1**, lange vor der Neufassung, die ihn ersetzen soll. Das Sicherungsnetz darf nicht vor dem Plan reißen, der es ablöst.

Anders als in v1.0 behauptet, laufen die bestehenden Skripte hier **nicht** unverändert weiter — Schritt 7 ist ein gebündelter Eingriff, kein reiner Move. Innerhalb des Schritts gibt es keine Reihenfolge-Falle: pre-commit liest seine Konfiguration zum Commit-Zeitpunkt aus dem Working-Tree, die Änderungen wirken also gemeinsam.

### 9.5 Stufe 2 — eigene Session, eigener Plan

9. View-Generierung für `config.yaml`, `PORTFOLIO.md`, `Faktortabelle.md`, Vault-Frontmatter — **im selben Schritt**: Neufassung **beider** Gates nach §4.4 (Freshness-Set reduzieren, **`provenance_gate.py::check_provenance` Check #2 mitziehen — Z. 176–181, sonst blockiert P3.5 jeden Vollanalyse-Write**, Tripwire auf den abgeleiteten Zustand umstellen, `parse_state_row` entfernen), **`schema_version`-Bump 1.0→1.1 in `schemas.py` + `sum_consistency.py` nach §4.1** und das Entfernen der Live-Felder aus `PORTFOLIO.md`, das aus Stufe 1 hierher verschoben wurde. Erst wenn die Tripwire nicht mehr aus der Tabelle liest, darf die Tabelle sich ändern.
10. Umlenkungen nach §9.2 für `insider_intel.py`, `screen.py`, `earnings_calendar.py`.
11. `system_audit` ausdünnen, `paragraph-18-sync` inklusive `para18_sync_reminder.py` zurückbauen, INSTRUKTIONEN §18 neu fassen.

### 9.6 Die §18-Schuld vom 26.08. löst sich auf

Die Sparplan-Änderung (AVGO und NOW entfernt, Gold 52 → 80, Core-4 je 40 → 50) braucht **keinen** Sync über acht Dateien. Ist-Raten sind Zustand und leben im Broker. Nachzutragen sind die geänderten SOLL-Werte in `REGELWERK.yaml` und die Begründung in der Chronik. Zwei Orte statt acht — die Schuld wird nicht bezahlt, sie entsteht nicht mehr.

---

## 10 · §18 neu

| Ereignis | Pflicht-Files |
|---|---|
| **Analyse abgeschlossen** | `score_history.jsonl` (via Skill) · `flag_events.jsonl` bei FLAG-Ereignis (via `archive_flag.py`) · Chronik (`CORE-MEMORY §12` + `log.md`) |
| **Regelwerk-Änderung** (Allokation, Klasse, Tier, Roster, Kadenz, Cap, Override) | `REGELWERK.yaml` · Chronik |
| **Sparraten-Änderung im Broker** | nichts — Zustand |
| **Pipeline / System-Zustand** | unverändert `PIPELINE.md` bzw. `SYSTEM.md` + `log.md` |

Aus 8–9 Pflicht-Dateien mit gegenseitiger Konsistenzpflicht werden **vier Quellen mit je genau einem Schreiber**. Multi-Event-Union (§18.2) bleibt gültig, greift aber ins Leere, weil sich die Sets nicht mehr überlappen.

---

## 11 · Offen

1. **Klassen-Zuordnung** nach §3.1 — Daten-Entscheidung beim Befüllen.
2. **Ersatzbank-Synthese** nach §3.2 — eigene Aufgabe mit Entscheidungsbedarf.
3. ~~**Rebalancing-Modell**~~ **ENTSCHIEDEN 2026-08-26:** additiv mit gestaffeltem Ziel (§7.4). `rate_abweichung` damit entblockt.
4. ~~**Zielallokation**~~ **GEKLÄRT 2026-08-26:** 60/35/5 ist die Politik; 59,7/35,3/5,0 sind gerundete Euro-Beträge (616/364/51 von 1031). Live-Ist 57,4/39,9/2,7 — die Drift ist das eigentliche Thema, nicht die Zieldefinition. Nebenbefund: bei `satelliten_pct: 35` beträgt das Aktienbudget 360,85 €, die Summe der Tier-Basen 364 € — unter `modell: additiv` unkritisch (0,3 pp gegen 4,0 pp Toleranz).
5. ~~**Vault-Frontmatter-Schema**~~ **GEPRÜFT 2026-08-26:** Standardschema (`WIKI-SCHEMA.md` Z. 57–71) ohne Score-Feld; Score-Frontmatter existiert auf drei Ersatzbank-Seiten. Generierung zurückgestellt (§8). Anmerkung: eine Ausweitung wäre Schema-**Design**, nicht bloß Abgleich.
6. ~~**`INSTRUKTIONEN §22`**~~ **GELESEN 2026-08-26:** beschreibt dasselbe additive Modell wie §7.4 und ist damit die dritte Doku-Stelle gegen die Tool-Normierung. Inhaltlich bestätigt; als Score-Kopie aber Sync-Ziel — siehe §9.2.
7. ~~**`satelliten`-Block**~~ **DURCHGEGANGEN 2026-08-26:** alle 24 Felder in §2.2 zugeordnet.
8. **`local_trade_controls`** — außerhalb dieser Spec, als Folge-Option notiert.
9. **US-Cap beim Core-Ausbau** — bei je 100 €/Mt auf die Core-4 wird die 63-%-Grenze nach ca. 24 Monaten erreicht (Reconciliation §F.2). Der Check meldet es rechtzeitig; die Politik dazu ist offen.
10. **`PORTFOLIO.md` Datums-Inkonsistenz** — Header nennt 09.06.2026, Footer 13.06.2026. Erledigt sich mit der Generierung.
11. **JEDI** — Position (2,25 Stk. ≈ 158 €) ohne Sparplan. Halten, aufstocken oder abgehen? Betrifft `etf_roster.soll_rate_eur`.
12. **GOOGL-Ausschluss** — Vault-Vermerk vom 01.04. förmlich aufheben oder Override nach §3.3 setzen (§9.3).
13. **ETF-SOLL-Raten** — Ist weicht bei allen sechs Positionen ab (Σ 616 gegen 563). Beim Befüllen neu festlegen.

*Geschlossen mit v1.5: Punkte 4, 5, 6, 7.*

---

## 12 · Prüfung dieser Spec

- **Vollständigkeit:** §2.1 ordnet jeden Top-Level-Block aus `config.yaml` genau einer Schicht zu. Jede heute im §18-Set geführte Datei ist in §2, §8 oder §1.2 als Quelle, generiert oder entfallend klassifiziert.
- **Deckung:** Jeder Konflikt aus Reconciliation §C hat in §7.1 einen benannten Check; C6 ist begründet gegenstandslos.
- **Empirie:** Die in §9.1 genannten Zugriffe sind am Quellcode verifiziert, nicht aus Suchtreffern erschlossen. Die Ableitungsregeln in §4 sind gegen die realen jsonl-Dateien getestet.

## 13 · Review-Spur

**Codex-Review R1, 2026-08-26** — 7 HIGH, 6 MEDIUM, 3 LOW. Alle HIGH gegen die realen Dateien nachgeprüft und bestätigt.

| Befund | Status in v1.1 |
|---|---|
| H1 Schreibverhalten falsch behauptet | korrigiert §9.1, Ursache benannt |
| H2 FLAG-Ableitung an APH falsifiziert | §4.2 + neue Stufe 0 §9.3 |
| H3 Datums-Kollision bei V | §4.1, Regel auf Dateireihenfolge umgestellt |
| H4 `ersatzbank`-Block existiert nicht | §3.2 als Synthesearbeit ausgewiesen |
| H5 `validator.py` bricht nach xlsx-Move | §9.2 + in Stufe 1 vorgezogen |
| H6 `existence.py` + fehlendes `CLAUDE.md` als Sync-Ziel | §9.2 + §9.4 Schritt 7 |
| H7 §33 nicht zuständig | §1.2, durch eigene Anti-Creep-Regel ersetzt |
| M1 `keine_zuteilung` · M2 `api_audit_log` · L1 freie Termine | §2.1 zugeordnet |
| M3 Nicht-Roster-Scores | §4.3 |
| M4 Blockzuordnung falsch kommentiert | §2.1 + §3 korrigiert |
| M5 kein Override-Mechanismus | §3.3 neu |
| M6 `para18_sync_reminder.py` | §9.2 |
| L2 Datums-Inkonsistenz PORTFOLIO.md | §11 Punkt 10 |
| L3 verwaister `screener_exceptions`-Eintrag COST | §3.1 |

**Eigenbefund über den Review hinaus:** Die drei FLAG-Quellen widersprechen sich paarweise (§1.1). GOOGL trägt einen unaufgelösten Trigger und wird als Core-4-Titel bespart.

**Codex-Nachtrag R1b zu §7.2/§7.3** — Formel unabhängig gegen die xlsx nachgerechnet, inhaltlich bestätigt (69,32 / 55,46 / 27,73 / 31,20 exakt). Vier Befunde eingearbeitet:

| Befund | Status |
|---|---|
| Blattname falsch zitiert — P/Q liegen auf `Portfolio & Rebalancing`, nicht `Parameter & Regeln` | §7.2 Fundstellen-Absatz korrigiert |
| `rate_abweichung` gelistet, obwohl sein SOLL laut §7.3 unentschieden ist | §7.1 als blockiert markiert, §3 `modell`-Absatz ergänzt |
| Slot-Kapazitäts-Check (B12/B13) fehlt | §7.1 `slot_kapazitaet` neu |
| Allokations-Summen-Check (B16) ohne Zielort | §3 Ladezeit-Validierung |
| doppelte Abschnittsnummer 7.3 | betraf v1.0, mit dem Neuschreiben entfallen |

### Codex-Sparring R2 auf v1.1 — 5 HIGH, 4 MEDIUM, 1 LOW

Alle nachgeprüft und bestätigt. R2 attestierte zehn der sechzehn R1-Befunde substanzielle Schließung.

| Befund | Status in v1.2 |
|---|---|
| R2-H1 Anti-Creep-Regel verbietet ihr eigenes Gründungsdokument | §1.2 Rückbau-Ausnahme ergänzt |
| R2-H2 `sparrate_eur` (1031 €) fehlt im Regelwerk, §7.2 hängt davon ab | §3 `budget.monatlich_eur`, §2.1 umklassifiziert |
| R2-H3 Override-Schema deckt NOW (Rate 0 ohne FLAG) nicht | §3.3 abschließende Regel-Liste + NOW-Beispiel |
| R2-H4 `para18_sync_reminder.py` darf in Stufe 1 nicht sterben | §9.2 + §9.4 Schritt 7 korrigiert, Rückbau nach Stufe 2 |
| **R2-H5 Freshness-Gate** `REQUIRED_TOUCH_FILES` | **§4.4 neu** — Gate scheitert nicht, es wird bedeutungslos |
| R2-M1 stale Referenz §9.5 nach Renumbering | §2.1 auf §9.6 korrigiert |
| R2-M2 Dateireihenfolge ohne Integritäts-Backstop | §4.1 `geschrieben_am` + Append-only-Check |
| R2-M3 GOOGL-Auflösung ist Analyse, nicht Reparatur | §9.3 herausgenommen, konservative Lesart begründet |
| R2-M4 `.pre-commit-config.yaml` fehlt als Fundort | §9.1 Tabelle |
| R2-L1 „vollständig" gilt nur auf Blockebene | §2.1 Formulierung präzisiert |

**Methodenfehler zweimal gemacht, beim zweiten Mal größer.** v1.0 verwechselte „Datei schreibt" mit „schreibt dieses Ziel". v1.1 stufte das gesamte Verzeichnis `backtest-ready/` als Testcode ein, weil der Ordnername „test" enthält — 11 von 13 produktiven Dateien fielen aus dem Blast-Radius, darunter beide kanonischen Schreibwege. Beide Male war die Ursache Mustervergleich statt Codelesen. Für §9.1 gilt ab jetzt: Zugriffsrichtung wird an der Schreibzeile gelesen, Testcode an `test_*` / `*_test.py` / `_smoke_test*` erkannt, nicht am Pfad.

### v1.3 — Owner-Entscheidung Rebalancing-Modell (2026-08-26)

Nach R2 angestoßen, während R3 lief. `modell: additiv` mit gestaffeltem Ziel für freigesetzte Beträge (§7.4). Beim Ausarbeiten fiel auf, dass eine flache Regel „freigesetzt → Gold" die bestehende `substitute_activation_global` stillschweigend übersteuert hätte — die Umleitung auf einen Ersatzkandidaten bei DEFCON 1 ist bereits geltende Regel inklusive Steuerlogik. Die Staffel setzt sie an erste Stelle, statt sie zu ersetzen.

`rate_abweichung` ist damit entblockt, `freigesetzt_ohne_ziel` als Check ergänzt. §11 Punkt 3 geschlossen.

### Codex-Sparring R3 auf v1.2 — 2 HIGH, 1 MEDIUM, 1 Präzisierung

Urteil: **Stufe 0 und der Großteil von Stufe 1 umsetzungsreif, Stufe 2 nicht.** Alle zehn R2-Befunde als substanziell geschlossen bestätigt. Beide HIGH nachgeprüft und bestätigt.

| Befund | Status in v1.4 |
|---|---|
| **R3-H1 Tripwire P2b** — hart blockierend, liest `PORTFOLIO.md` offsetbasiert, bereits einmal gebrochen | §4.4 Gate 2 neu; Tripwire wird auf abgeleiteten Zustand umgestellt, `parse_state_row` entfällt |
| **R3-H2** `cap_single_stock` fehlt in der Override-Liste — NOW ist bewusst über Cap | §3.3 ergänzt; NOW braucht zwei Overrides |
| R3-M1 Stufe 1 Schritt 8 könnte die Tripwire vorzeitig zerstören | Schritt 8 nach Stufe 2 Schritt 9 verschoben; Stufe 1 fasst die Tabelle nicht an |
| Präzisierung: Append-only existiert für `score_history.jsonl` bereits | §4.1 korrigiert — der Umbau ergänzt **einen** Check, nicht zwei |

**Sparring endet hier.** Die Heuristik deckelt bei drei Runden; die verbleibenden Punkte waren lokal und sind eingearbeitet. Eine R4 würde nach eigener Klausel formal greifen, aber R3 hat keine strukturellen Lücken mehr gemeldet, sondern zwei benannte Abhängigkeiten — beide jetzt versorgt.

**Methodische Lehre aus R3:** `check_freshness` (Z. 256) und `parse_state_row` (Z. 152) stehen in derselben Datei. v1.2 reparierte das eine und durchsuchte die Datei nicht nach Geschwistern. Regel für die Umsetzung: berührt eine Korrektur eine Datei, wird die ganze Datei auf gleichartige Abhängigkeiten geprüft.

**Nächster Schritt:** Freigabe durch den Owner. Danach Stufe 0.

### R4 — Eigenrunde mit Live-Verifikation und Codex-Gegenprüfung (2026-08-26)

Erste Runde gegen die **Scalable-API** statt nur gegen das Repo. Vier Spec-Zahlen bestätigt (NOW 14,6 % · Gold 2,7 % · Sparplan-Ist 1068 gegen SOLL 1031 · Depotwert 30.124 €), eine falsifiziert (META hat keine Position). Zwei Codex-Runden liefen parallel: eine enge Verifikation der fünf HIGH-Belege, eine offene Suche.

| Befund | Status in v1.5 |
|---|---|
| **R4-H1** `geschrieben_am` scheitert an `extra="forbid"` + `schema_version: Literal["1.0"]` | §4.1 · §4-Einleitung · §9.1 (`schemas.py` ergänzt) · §9.5 Schritt 9 |
| **R4-H2** Roster-ISINs existieren nirgends im Repo | §3 · §9.4 Schritt 5 — Quelle ist der Broker, Stufe 1 ist nicht offline |
| **R4-H3** Vault-Frontmatter trägt Scores für 3 Seiten, keinen Satelliten | §1.1 · §8 · §11.5 |
| **R4-H4** Vault führt GOOGL als „struktureller Ausschluss", Sparplan läuft | §9.3 · §3 `overrides` · §11.12 |
| **R4-H5** `INSTRUKTIONEN §22` ist Score-Kopie und fehlte als Sync-Ziel | §1.1 · §1.2 · §9.2 |
| **R4-C1** `CLAUDE.md` trägt den alten 8-9-Datei-Sync als Prosa (Z. 27/29/57/59/77/78) | §9.2 · §9.4 Schritt 7 — gehört in denselben Commit wie der Move |
| **R4-C2** Gate 1 hat einen zweiten Abnehmer: `provenance_gate.py` Z. 176–181 blockiert P3.5 fail-close | §4.4 · §9.5 Schritt 9 |
| R4-C3 §9.3 Punkt 3 („Quellen stimmen überein") widersprach dem Folgeabsatz | §9.3 präzisiert |
| R4-C4 `validator.py` bricht nicht, es warnt dauerhaft | §9.2 Begründung korrigiert, Maßnahme bleibt |
| R4-M6…M9 · N10…N14 | §2 · §2.2 · §3 · §3.1 · §3.2 · §5 · §7.1 · §7.3 · §9.1 · §9.2 · §11.4 · §11.6 · §11.7 |

**Gegenprüfung:** Bei zwei Zählungen war ich zu korrigieren — 6 statt 7 ISINs (ein `grep`-Substring-Treffer in „r*isin*g"), 18 statt 19 Check-Dateien (`__pycache__/` mitgezählt). Beide Kernaussagen blieben unberührt.

**Methodische Lehre:** Drei Runden ohne strukturelle HIGHs bedeuten nicht Konvergenz, sondern Konvergenz *innerhalb der geprüften Achse*. R1–R3 liefen sämtlich auf Schreibpfaden und Gates; alle neun R4-Befunde liegen außerhalb. Zwei waren nur durch **Abwesenheit** von Treffern zu finden (keine Satelliten-ISIN, kein Score im Vault-Schema), zwei nur gegen **Live-Daten**. Die beiden R4-Teilrunden — eigene und Codex — überschnitten sich in genau einem Punkt: getrennte Achsen finden getrennte Fehler. Zweite Lehre, aus den zwei Zählfehlern: `grep -c` auf einen kurzen Begriff zählt Substrings mit, `ls` listet Verzeichnisse neben Dateien — jede Zahl, die in eine Spec einzieht, gehört einzeln belegt.

**Dritte Lehre, aus R4-C2:** Die R3-Regel „berührt eine Korrektur eine Datei, prüfe die ganze Datei" reicht nicht. Die richtige Frage ist nicht, was sonst noch in dieser Datei steht, sondern **wer diesen Rückgabewert konsumiert**.

---

*Dynasty-Depot · Architektur-Spec v1.5 · Stand 2026-08-26 · Entwurf zur Freigabe, keine SSoT verändert*
