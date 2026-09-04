# Depot-Architektur — Zustand, Urteil, Regelwerk

**Status:** Entwurf zur Freigabe · **Stand:** 2026-09-04 · **Version:** v1.6.2 (post R5 + Stufe 0 abgeschlossen)
**Vorgänger-Dokumente:** `02_Analysen/2026-08-26_Depot-Reconciliation.md` · `02_Analysen/2026-09-04_Depot-Live-Verifikation.md`

> **Entwicklung:** Fünf Prüfrunden — R1 7 HIGH, R2 5, R3 2, R4 5 HIGH + 4 Codex-Befunde, R5 3 HIGH + 3 MEDIUM. Alle gegen die realen Dateien nachgeprüft. Fünf Behauptungen der Vorfassungen waren empirisch falsch (Schreibverhalten §9.1, Ableitungsregel §4, Blast-Radius `backtest-ready/`, „ungescort trotz Position" bei META, „GOOGL ohne Score-Record" §1.1) und sind ersetzt. R4 war die erste Runde gegen die Live-API; **R5 die erste, die die Regelwerk-Quellen jenseits von `config.yaml` gesucht hat** — und zwei fand: das xlsx-Parameterblatt (§2.3) und `KONTEXT.md` (§2.4). Schwerster Fund: eine geltende Regel, die nur in einer Datei steht, die Stufe 1 archiviert. Prüfspur in §13.
>
> **Strukturelle Neuerung von v1.6:** Ein Teil des Depotwerts gehört nicht zum Dynastie-Depot. Der Entnahme-Topf „Hochzeit" (9.000 € vom 11.08.2026, Ziel 07.08.2027) ist ab §2.5 aus allen Quoten herausgerechnet. Das ändert kein Ergebnis kosmetisch, sondern die Basis, auf der `allokation_drift`, `cap_single_stock` und `cap_us` rechnen — und damit deren Urteil.
>
> **Umsetzungsreife — am 04.09.2026 durch den Ausführungsversuch korrigiert:** **Stufe 0 ist abgeschlossen.** Schritte 2 (AMZN-Divergenz) und 3 (GOOGL-Ausschluss) ausgeführt; Schritt 1 (APH-Trigger) **entfällt** — der Ausführungsversuch zeigte, dass nicht das Schema zu eng, sondern §4.2 falsch klassifiziert war (Owner-Entscheidung Weg B, §9.3.1). `flag_events.jsonl` ist damit autoritativ, ohne dass ein Event nachgetragen werden musste. Stufe 1 freigabefähig, aber **nicht offline** — das Regelwerk-Befüllen braucht den Live-Layer und ist in §9.4 Schritt 5 um die **Extraktion der xlsx-Parameter** erweitert, die zur Vorbedingung des Archiv-Moves in Schritt 7 wird. Stufe 2 erst nach der Gate-Neufassung aus §4.4 samt Schema-Bump, beides in Schritt 9 gebündelt.
>
> **Live-Zahlen tragen einen Stichtag.** Jede Zahl aus dem Broker ist mit `[03.09.]` bzw. `[26.08.]` markiert. v1.5 führte vier Live-Zahlen ohne Datum; drei davon waren nach acht Tagen falsch. Eine Zahl ohne Stichtag wird als Konstante gelesen.

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

**Die Prüfinfrastruktur greift nicht.** Verifiziert 2026-08-26, nachgeprüft 2026-09-04 — die FLAG-Quellen widersprechen sich paarweise, keine zwei stimmen überein:

| Quelle | aktive FLAGs |
|---|---|
| `config.yaml flags_aktiv` | MSFT · APH · AVGO |
| `config.yaml flags_review` | — (leer) |
| `config.yaml flags_watchlist` | **GOOGL** (`wirkung: "Kein Einstieg, kein Nachkauf bis FLAG aufgehoben"`) |
| `flag_events.jsonl` (Trigger ohne Resolve) | MSFT · AVGO · AMZN · GOOGL |
| `PORTFOLIO.md` | MSFT · AMZN · AVGO · APH |
| Vault `entities/ersatzbank/` | GOOGL · PEGA · ZTS (nur diese drei Seiten tragen FLAG-Frontmatter) |

**`config.yaml` hält drei FLAG-Blöcke, nicht einen.** v1.5 führte an dieser Stelle allein `flags_aktiv`. Der Unterschied ist nicht formal: `flags_watchlist` trägt für GOOGL eine **Handelsregel** — kein Einstieg, kein Nachkauf — bei laufendem 50-€-Sparplan und seit dem 01.09. bestehender Position [03.09.: 50,71 €].

Konkrete Folge: **GOOGL trägt seit 2026-03-15 einen CapEx/OCF-Trigger ohne Resolve** und wird seit 2026-08-26 als Core-4-Titel mit 50 €/Monat bespart. Der Widerspruch ist damit **dreifach** — Vault-Entity („struktureller Ausschluss seit 01.04."), `flags_watchlist` („kein Einstieg") und der offene jsonl-Trigger stehen alle gegen eine laufende Rate. v1.5 zählte ihn zweifach (§9.3), weil `flags_watchlist` nicht gelesen war.

**Analyse-Aktivität** (`score_history.jsonl`, 37 Records, davon 13 `forward`, 24 Backfill):

| Monat | 2026-03 | 2026-04 | 2026-05 | 2026-06 | 2026-07 | 2026-08 |
|---|---:|---:|---:|---:|---:|---:|
| Records | 11 | 22 | 2 | 2 | **0** | **0** |

Seit dem 13.06.2026 keine Analyse. Im selben Zeitraum entstanden Skills, Hooks und Prüfskripte.

**Verfalls-Cliff — mit hartem Datum.** Am 04.09. ist noch kein Score verfallen. Der erste fällt am **22.09.2026: GOOGL** (Score 72 vom 26.03.). Danach der Cluster:

| verfällt | Titel |
|---|---|
| **2026-09-22** | GOOGL |
| 2026-10-14 | ASML · COST · RMS · SU · VEEV |
| 2026-10-20 … 10-31 | TMO · V · MSFT · APH · BRK.B |
| 2026-11-11 · 2026-12-01 | AMZN · AVGO |

Zehn Scores laufen im Oktober über die 180-Tage-Grenze. Der erste ist ausgerechnet der Titel mit offenem FLAG-Trigger, aufzuhebendem Ausschluss (§9.3), 50 €/Mt und seit 01.09. erstmals Position. v1.5 schrieb „aktuell ist kein Score verfallen" ohne Datum — das war zutreffend und blieb es genau 27 Tage.

**Ungescort trotz Depotposition [03.09.]:** **ADBE · META · NOW · ZETA** — alle vier mit Position, seit dem 01.09. auch META (53,73 €). Es gibt heute keinen Fall „Sparplan ohne Position" mehr; die Unterscheidung aus v1.5 ist gegenstandslos geworden, weil die Sparpläne gelaufen sind.

**Korrektur zu v1.5:** Dort stand „ungescort mit Sparplan, aber noch ohne Position: GOOGL und META" und zwei Sätze später „Alphabet (72) … hat gültige Records". Beides zugleich kann nicht stimmen. Empirisch gilt das Zweite: **GOOGL hat Score 72 vom 26.03.2026**, `score_history.jsonl` Zeile 12. Ohne Record sind die vier oben. Veeva (74) und Costco (69) haben ebenfalls gültige Records.

### 1.2 Abnahmekriterium

Das System muss danach **kleiner** sein:

| Entfällt | Kommt hinzu |
|---|---|
| 3 xlsx-Tools — **nach Extraktion des Parameterblatts** (§2.3) | `00_Core/REGELWERK.yaml` |
| Skill `xlsx-smoke-test-runner` (vollständig) | `03_Tools/depot_check/` |
| `precommit/xlsx_smoke_test.py` | ein `analyse_typ`-Wert |
| Skill `paragraph-18-sync` (weitgehend) + `validator.py` + Pre-Commit-Hook | |
| `cross_source.py` · `cross_source_reverse.py` · `score_event_parity.py` (≈ 900 Z) | |
| `insider_intel factor-sync` | |
| INSTRUKTIONEN §18 großteils, §18.7 vollständig | |
| INSTRUKTIONEN §22 (Sparplan-Formel + hartcodierte 13-Zeilen-Score-Tabelle) | |
| Sync-Prosa in `CLAUDE.md` (6 Stellen, §9.2) | |
| `KONTEXT.md` §§ 2 · 3 · 4 (Broker, Raten, Positionszahlen, ETF-Zuordnung — Zustand, §2.4) | |

Ist die Bilanz nicht deutlich negativ, war der Entwurf falsch.

**Kein Rückgriff auf §33.** INSTRUKTIONEN §33 begrenzt seinen Geltungsbereich ausdrücklich auf KG-Extraktion, Bayesian-RAG, Agentic-Reflection-Loops und DPO-Alignment und schließt Scoring-Parameter- und Datenquellen-Änderungen aus. Eine Datenarchitektur-Konsolidierung fällt unter keinen Punkt. Statt ein unzuständiges Gate zu zitieren, gilt für diese Spec und alles Folgende:

> **Anti-Creep-Regel (neu, ersetzt den §33-Bezug für Infrastrukturarbeit)**
> In einem Monat ohne abgeschlossene DEFCON-Analyse wird kein **additives** Infrastruktur-Item eröffnet.
> **Rückbau ist immer erlaubt** — Arbeit, die nachweislich mehr entfernt als sie hinzufügt, fällt nicht unter die Sperre.
> Maximal drei offene Pipeline-Items gleichzeitig. Kein Plandokument über 500 Zeilen.

Die Rückbau-Ausnahme ist nicht kosmetisch: Ohne sie verböte die Regel bei wörtlicher Anwendung ihr eigenes Gründungsdokument, das in einem Null-Analyse-Monat entsteht. Der Nachweis ist die Bilanz oben — wer sich auf die Ausnahme beruft, legt sie vor.

**Die 500-Zeilen-Klausel verletzt dieses Dokument selbst — offen protokolliert.** v1.5 hatte 745 Zeilen, v1.6 hat rund 1.040. Die Rückbau-Ausnahme deckt das *Öffnen* des Items, nicht die Länge. Zwei Dinge folgen daraus, und keines davon ist „Regel ignorieren":

1. **Der Zuwachs von v1.6 ist zu zwei Dritteln Prüfspur** (§13 R5) **und Quellen-Inventar** (§2.3–2.6) — Material, das nach der Umsetzung nicht mehr gebraucht wird. Es ist Beleg, nicht Plan.
2. **Nach Stufe 0 wird geteilt:** der Plan-Teil (§9–§11) bleibt als Arbeitsdokument, §13 zieht als abgeschlossene Prüfspur nach `05_Archiv/`, §2.3–2.6 gehen in `REGELWERK.yaml` und die Chronik auf. Ein Dokument, das seine eigene Regel bricht und das nicht sagt, ist genau die stille Regeländerung, gegen die §3.3 argumentiert.

Der Vollständigkeit halber: Auch die Klausel „maximal drei offene Pipeline-Items" ist an dieser Spec nicht geprüft worden. Das gehört bei der Freigabe gegen `PIPELINE.md` abgeglichen, nicht hier behauptet.

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

> **Der Titel dieses Abschnitts war die Lücke.** Bis v1.5 inventarisierte die Spec ausschließlich `config.yaml` und nannte das Ergebnis „vollständig". Vollständig war es für `config.yaml`. Zwei weitere Dateien halten geltendes Regelwerk und wurden nie durchgegangen: das xlsx-Parameterblatt (§2.3) und `KONTEXT.md` (§2.4). Beide sind Migrations-Sync-Ziele, eine davon steht auf der Archiv-Liste.

| Block | Schicht | Anmerkung |
|---|---|---|
| `portfolio` | geteilt | Caps und `zieljahr` → Regelwerk; **`sparrate_eur` → Regelwerk** (Owner-Entscheidung, siehe unten); Slots und `us_current_pct` → Zustand |
| `brokers` | Zustand | entfällt als Regel (§9.6) |
| `allokation` | Regelwerk | |
| `satelliten_tier_raten` | Regelwerk | → `klassen.satellit.tier_basis_eur` |
| `system_regeln` | Regelwerk | Verfall, Ersatz-Aktivierung, Moat-Drift, Sparplan-Verteilung, Tariff-Quelle |
| `etfs` | geteilt | ISIN + Soll-Rate → Regelwerk; `broker` → Zustand |
| `satelliten` | geteilt | feldweise aufgeschlüsselt, siehe §2.2 |
| `flags_aktiv` · `flags_review` | Urteil | wird aus `flag_events.jsonl` abgeleitet, nachdem diese vollständig ist (§4.2) |
| `flags_watchlist` | **Regelwerk** | **korrigiert in v1.6.** Der Block enthält keinen Urteilsstand, sondern eine Handelsregel — GOOGL: „Kein Einstieg, kein Nachkauf bis FLAG aufgehoben". Aus `flag_events.jsonl` ist das nicht ableitbar: die jsonl weiß, *dass* ein Trigger offen ist, nicht, *welche Handelsbeschränkung* der Owner daran geknüpft hat. Zielort ist `overrides` bzw. eine Klassenregel (§3.3), nicht der Urteil-Layer |
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

### 2.3 Zweite Regelwerk-Quelle: `Rebalancing_Tool` Blatt `Parameter & Regeln`

`03_Tools/Rebalancing_Tool_v4.0.xlsx`, Blatt `Parameter & Regeln` (A1:C65), hält Parameter, die die Spec bereits zitiert — ohne sie je als Quelle inventarisiert zu haben:

| Zelle | Parameter | Wert | steht auch in `config.yaml`? |
|---|---|---:|---|
| B4 | Sparrate monatlich | 1031 | ja |
| B5 / B6 / B7 | Zielanteile ETF / Aktien / Gold | 0,597 / 0,353 / 0,05 | ja |
| B8 / B9 | Drift-Toleranz ETF-Gold / Aktien | 0,015 / 0,04 | **nein** |
| **B10** | **Single-Stock-Cap** | **0,1** | **nein — einzige Quelle im gesamten Repo** |
| B11 | US-Hard-Cap | 0,63 | ja |
| B12 | Max Aktien-Slots | 13 | ja |
| B15 | Drift-Warnschwelle (Faktor) | 3 | nein |
| B23 | „NIEMALS durch Verkauf rebalancen" | — | ja (`KONTEXT.md` §7) |
| B65 | Nachkauf-Schwelle | 300 | nein |

**Zwei Konsequenzen, die die Migration betreffen.**

1. **§3 nannte für `single_stock_max_pct: 10` als einzigem Cap-Parameter keine Quelle.** Nicht aus Nachlässigkeit — es gab keine auffindbare. Ein `grep` über `.md` und `.yaml` liefert für den Wert nichts, weil er in einer Binärdatei steht. Die Quelle ist B10 und wird in §3 nachgetragen.
2. **Diese Datei wandert in Stufe 1 Schritt 7 nach `05_Archiv/`.** Ohne vorherige Extraktion archiviert die Migration vier geltende Regelwerte, von denen einer nirgendwo sonst existiert. Die Extraktion ist deshalb **Voraussetzung** des Moves, nicht Nacharbeit (§9.4).

Die beiden anderen xlsx (`Satelliten_Monitor`, `Watchlist_Ersatzbank_Monitor`) sind vor dem Move genauso durchzugehen. Für sie ist bislang **nicht geprüft**, ob sie eigene Regelwerte halten — die Aussage „sie tragen nur Kopien" ist unbelegt und wird beim Extraktionsschritt entschieden, nicht vorher angenommen.

### 2.4 Dritte Regelwerk-Quelle: `KONTEXT.md`

Die Datei kommt in v1.5 an keiner Stelle vor. Die Routing-Table lädt sie bei **jeder** Strategie- und Allokationsfrage. Es gilt dasselbe Argument wie bei R4-C1 zu `CLAUDE.md`: eine Datei, die der Agent regelmäßig liest und die den alten Zustand beschreibt, wirkt stärker als jede korrigierte Spec.

Verifizierte Drift [Stand 03.09.]:

| § | steht dort | Ist |
|---|---|---|
| 2 | „ING (IWDA + EIMI + EXUS) + Scalable" | ING seit 17.08. leer |
| 3 | Broker-Spalte ING · „~1031 € · 20 Positionen" | alles Scalable · 1.068 € · 24 Positionen |
| 4 | IWDA 206 / EIMI 123 / EXUS 82, alle ING | 208 / 120 / 80, alle Scalable |
| 4b | „In-Kind Herbst 2026, IWDA-**Verkauf** 2027" | am 17.08. geschehen — **IWDA wurde übertragen statt verkauft**; die daran hängende Steuerplanung („+369 € G/V steuerfrei") ist offen |
| 5 | 13 Satelliten | 17 Aktienpositionen |
| 7 | ING 1.500–1.600 € / Scalable 400–500 € Freibetrag | ab 2027 alles Scalable, ab Heirat 2.000 € (§2.6) |

**Schichtenzuordnung, analog §2.1:**

| § | Schicht |
|---|---|
| 1 Philosophie · 8 Psychologie · 9 Bus-Faktor | **Doktrin** — bleibt handgeschrieben, wird von nichts generiert |
| 3 Caps · 5 Roster · 6 Ersatzbank · 7 Freibeträge | **Regelwerk** → `REGELWERK.yaml` |
| 2 Broker · 3 Raten und Positionszahlen · 4 ETF-Zuordnung | **Zustand** → entfällt |

Die Doktrin-Schicht ist der Grund, warum `KONTEXT.md` nicht wie die xlsx verschwindet. §1 („kein Markttiming") und §7 („niemals durch Verkauf rebalancen") sind die Begründungen, gegen die §7.5 geprüft wird — sie in eine YAML zu pressen, würde sie unlesbar machen. Zustand und Regelwerk ziehen aus, die Begründung bleibt.

### 2.5 Der Entnahme-Topf „Hochzeit" ist kein Dynastie-Kapital

Am 11.08.2026 sind **9.000 €** als `DEPOSIT` eingegangen und am 13.08. in einer Order-Welle investiert worden, centgenau:

| Ticker | Stk | Einstand € | Wert [03.09.] € | |
|---|---:|---:|---:|---:|
| IWDA | 24,387411 | 3.150 | 3.115,43 | −1,1 % |
| NOW | 18,284878 | 2.000 | 2.282,87 | +14,1 % |
| EIMI | 37,072344 | 1.750 | 1.765,92 | +0,9 % |
| AVGC | 46,285492 | 1.190 | 1.183,17 | −0,6 % |
| EXUS | 22,216796 | 910 | 899,22 | −1,2 % |
| **Σ** | | **9.000** | **9.246,62** | **+2,7 %** |

Zieldatum **07.08.2027**, Zielwert **10.000–11.000 €** — es fehlen 753–1.753 €.

**Owner-Entscheidung 04.09.2026: der Topf zählt in keine Dynastie-Quote** — nicht in `allokation`, nicht in `cap_single_stock`, nicht in `cap_us`. Begründung: es ist zweckgebundenes Kapital mit Entnahmetermin, kein Depotbestandteil mit 2058er Horizont. Es im Nenner zu führen, macht jede Quotenaussage falsch, und zwar systematisch in eine Richtung.

**Warum die Basis das Ergebnis bestimmt** [03.09.]:

| Basis | ETF | Aktien | Gold | Basis € |
|---|---:|---:|---:|---:|
| Depot gesamt | 55,8 % | 41,5 % | 2,7 % | 32.128 |
| **Dynastie-Basis (Topf raus, maßgeblich)** | **47,9 %** | **48,3 %** | **3,8 %** | **22.881** |

Gegen 60/35/5 bei Toleranz 1,5 / 4,0 pp: **ETF −12,1 pp · Aktien +13,3 pp · Gold −1,2 pp.** Die Gold-Lücke, die v1.5 an zwei Stellen als größten Unterhang führt, liegt auf der maßgeblichen Basis **innerhalb** der Toleranz — der größte Unterhang ist der ETF-Core. §7.4 ist entsprechend korrigiert.

**Modellierung — Owner-Entscheidung: kein Tranchen- oder Klassen-Konstrukt.** Ein Block, fünf statische Datenzeilen im Regelwerk, **eine Subtraktion** in `depot check`. Der Topf bekommt keine eigene Klasse, keine eigene Kadenz und keine Analysepflicht; seine fünf Titel sind dieselben, die das Depot ohnehin führt. Der Preis dieser Einfachheit ist bekannt: verkauft der Owner 2027 Stücke, muss er die Stückzahlen im Regelwerk von Hand nachziehen. Bei fünf Zeilen und einem Termin ist das billiger als jede Automatik.

**Was der Topf erklärt.** NOW liegt bei 15,88 % des Gesamtdepots, aber **12,33 %** der Dynastie-Basis — und nach der Entnahme am 07.08.2027 bei rund **7,90 %** (konstante Kurse, zwölf weitere Sparplan-Monate). Der Cap-Verstoß löst sich also durch den Entnahmetermin auf, nicht durch Verwässerung. Das ist die Grundlage des NOW-Overrides in §3.3.

### 2.6 Steuer-Lage — Korrektur der Doku

Owner-Angaben vom 04.09., sie korrigieren `KONTEXT.md` §7:

- **Das ING-Depot ist durch den Übertrag auf 0** — nicht gekündigt, aber leer.
- **Ab 2027 kann der volle Freibetrag bei Scalable liegen**, ab der Heirat **2.000 €**.
- Merker: **verfügbar ≠ hinterlegt.** Der erhöhte Freistellungsauftrag muss erteilt werden; das passiert nicht von selbst.

**Offener Beleg — FIFO-Risiko der Entnahme.** Die ETF-Tranchen des Topfs werden 2027 FIFO gegen die ING-Altbestände abgerechnet (IWDA 34 · EIMI 40 · EXUS 53 Stk, übertragen am 17.08.). Deren echter Einstand ist **über die API nicht abrufbar**: `get_transaction_details` liefert für `TRANSFER_IN` nur `averagePrice` = Übertragswert (IWDA 128,615 = 4.372,91 / 34), nicht die historischen Anschaffungskosten. Quelle ist die ING-Übertragungsanzeige oder das Scalable-Steuerreporting. **Ohne diesen Beleg ist unklar, ob die 2.000 € 2027 reichen** — die Aufgabe steht in §11 mit Frist vor Q3/2027.

---

## 3 · REGELWERK.yaml

Einzige handgeschriebene Quelle für Politik.

```yaml
meta: {version: "1.0", gueltig_ab: 2026-09-05}

budget:
  monatlich_eur: 1068            # Owner-Entscheidung 04.09.2026: Broker-Ist uebernommen
                                 # (vorher 1031, xlsx B4).
                                 # ROLLE KORRIGIERT: KEINE Eingangsgroesse der Ratenrechnung.
                                 # v1.5 begruendete das Feld mit §7.2 — das ist die
                                 # Normierungsformel, die §7.4 verworfen hat. Unter
                                 # `modell: additiv` ist es die ERHALTUNGS-INVARIANTE der
                                 # §7.4-Staffel: Summe aller SOLL-Raten nach Umleitung == budget.
                                 # 1068 ist heute die IST-Summe [03.09.]: ETF 563 + Gold 80
                                 # + Aktien 425. Ob die SOLL-Summe sie trifft, ist erst nach
                                 # der Klassen-/Tier-Zuordnung (§3.1) pruefbar — siehe unten.

quoten_basis: dynastie           # Nenner fuer allokation, caps und Drift:
                                 # Depotwert MINUS entnahme_2027 (§2.5).
                                 # Owner-Entscheidung 04.09.2026.

allokation:
  gilt_fuer: depotwert           # Owner-Entscheidung 04.09.2026: WERTBASIERT.
                                 # 60/35/5 ist eine Aussage ueber den Bestand.
                                 # Die Sparraten-Verteilung ist das Instrument und darf
                                 # bewusst abweichen — die Gold-Rate von 7,5 % ist bei
                                 # einem Bestand von 3,8 % korrekter Aufholmodus,
                                 # kein Regelverstoss.
  etf_core_pct: 60               # Politik. Die 59,7/35,3/5,0 des Tools sind das
  satelliten_pct: 35             # Rundungsartefakt ganzzahliger Euro-Raten
  gold_pct: 5                    # (616/364/51 von 1031), keine abweichende Regel.
  toleranz_pp: {etf_gold: 1.5, aktien: 4.0}    # getrennt, wie im Tool (B8/B9)
  drift_warnfaktor: 3                          # Toleranz x Faktor -> rot (B15)

caps:
  us_hard_cap_pct: 63            # xlsx B11
  us_cap_gilt_fuer: [ist, ziel]  # Tool prueft beides (US-Exposure B29/B30)
  single_stock_max_pct: 10       # xlsx B10 — EINZIGE Quelle im Repo (§2.3).
                                 # Hoehe, Bezugsgroesse und Hysterese sind nach der
                                 # Entnahmetopf-Trennung neu zu bewerten (§11 Punkt 15).
  max_aktien_slots: 13           # xlsx B12 — Ist [03.09.] 17. slot_kapazitaet meldet
                                 # FAIL, bis §3.1 das Roster entschieden hat.

rebalancing:
  modell: additiv                # ENTSCHIEDEN 2026-08-26 (§7.3). Tier-Basis bedeutet Euro.
  nachkauf_schwelle_eur: 300     # Fehlbetrag fuer Einmalkauf-Signal (B65)
  block_rebalancing_durch_verkauf: verboten
                                 # ersetzt das Pauschal-Flag `niemals_durch_verkauf: true`
                                 # (B23 / KONTEXT.md §7). Praezisiert in §7.5 —
                                 # das Verbot gilt der BLOCK-Rueckfuehrung auf Zielquote,
                                 # nicht jedem Verkauf. Zulaessige Pfade abschliessend:
  verkauf_zulaessig:
    - substitution               # substitute_activation_global.steuer_regel, bestehend
    - konzentrations_kappung     # §7.5 — Parameter offen (§11 Punkt 15/16)
    - entnahme_2027              # geplante Entnahme, kein Rebalancing (§2.5)
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

# SOLL = IST, Owner-Entscheidung 04.09.2026 (Konsequenz aus budget: 1068).
# Die alten config.yaml-Werte wichen bei allen sechs Positionen ab:
#   IWDA 206→208 · EIMI 123→120 · EXUS 82→80 · AVGC 82→85 · WQTM 51→70
#   JEDI 72→0 (kein Sparplan mehr, Position bleibt) · Gold 51→80
#   Σ alt 616 gegen Σ neu 563 (ohne Gold).
# OFFEN bleibt allein JEDI: soll_rate_eur 0 ist der Ist, nicht zwingend die Absicht
# (Position 153,34 € + offenes Sell-Limit @90) — §11 Punkt 11.
etf_roster:
  - {ticker: IWDA, isin: IE00B4L5Y983, soll_rate_eur: 208}
  - {ticker: EIMI, isin: IE00BKM4GZ66, soll_rate_eur: 120}
  - {ticker: EXUS, isin: IE0006WW1TQ4, soll_rate_eur: 80}
  - {ticker: AVGC, isin: IE0003R87OG3, soll_rate_eur: 85}
  - {ticker: WQTM, isin: IE000W8WMSL2, soll_rate_eur: 70}
  - {ticker: JEDI, isin: IE000YU9K6K2, soll_rate_eur: 0}   # Position ohne Sparplan — Owner-Entscheidung offen
gold: {ticker: EWG2, isin: DE000EWG2LD7, soll_rate_eur: 80}

# Zweckgebundenes Kapital, NICHT Dynastie-Depot (§2.5). Owner-Entscheidung 04.09.2026.
# Fuenf statische Zeilen, eine Subtraktion in `depot check`. Kein Tranchen-Konstrukt,
# keine eigene Klasse, keine Analysepflicht.
entnahme_2027:
  zweck: "Hochzeitsfeier"
  ziel_datum: 2027-08-07
  eingezahlt: {betrag_eur: 9000, am: 2026-08-11, investiert_am: 2026-08-13}
  zielwert_eur: [10000, 11000]
  zaehlt_in_quoten: false        # raus aus allokation, cap_single_stock, cap_us
  tranchen:
    - {ticker: IWDA, stk: 24.387411, einstand_eur: 3150}
    - {ticker: NOW,  stk: 18.284878, einstand_eur: 2000}
    - {ticker: EIMI, stk: 37.072344, einstand_eur: 1750}
    - {ticker: AVGC, stk: 46.285492, einstand_eur: 1190}
    - {ticker: EXUS, stk: 22.216796, einstand_eur:  910}

overrides:                       # §3.3 — bewusste Regelabweichungen
  - {ticker: APH, regel: flag_wirkung, wert: rate_beibehalten, betrag_eur: 20,
     grund: "Owner-Entscheidung 26.08.2026 trotz Score-FLAG",
     seit: 2026-08-26, review_am: 2026-11-26}
  - {ticker: NOW, regel: rate, wert: 0,
     grund: "Kapitalumschichtung zugunsten Core-Aufbau 26.08.2026 — kein FLAG",
     seit: 2026-08-26, review_am: 2027-02-26}
  - {ticker: NOW, regel: cap_single_stock, wert: ausgesetzt,
     grund: "12,33 % der Dynastie-Basis [03.09.]; die Entnahme am 07.08.2027 loest den
             Verstoss auf (-> ~7,90 %), nicht Verwaesserung. Bewusst uebergewichtet.",
     seit: 2026-08-26, review_am: 2027-08-07}   # Datum = Entnahmetermin, §2.5.
                                                # Cap-HOEHE selbst offen — §11 Punkt 15.
  - {ticker: ZETA, regel: rate, wert: 0,
     grund: "Position 784,70 € [03.09.], kein Sparplan, kein FLAG. Strukturgleich NOW:
             `ohne_score: basis_voll` fordert 18 €, gewollt sind 0.",
     seit: 2026-09-04, review_am: 2027-03-04}
# GOOGL braucht KEINEN Override mehr: Owner-Entscheidung 04.09.2026 hebt den
# Ausschluss foermlich auf (§9.3). Der CapEx/OCF-FLAG bleibt aktiv und wirkt ueber
# Klasse `core` als analysepflicht — genau wie vorgesehen.
# COST: gleicher Fall wie ZETA, aber der Roster-Entscheidung nachgelagert (§3.1).

screener_exceptions: {...}       # 1:1 aus config.yaml Top-Level
watchlist: {...}                 # 1:1 aus config.yaml Top-Level
keine_zuteilung: {...}           # 1:1 aus config.yaml Top-Level
moat_drift_trigger: {...}        # aus system_regeln
substitute_activation_global: {...}
tariff_exposure_quelle: {...}
```

**`rebalancing.modell` wählt die Formel, nicht nur eine Beschriftung.** `tier_basis_eur` und `defcon.modulation` allein lesen sich wie das additive Modell. Erst `modell` entscheidet, ob daraus Euro-Beträge (additiv) oder relative Gewichte (Normierung, §7.2a) werden. Steht `additiv`, wie seit 2026-08-26 entschieden, sind Tier-Basen Euro-Beträge und `freigesetzt` bestimmt, wohin eingefrorene Raten fließen (§7.4).

**Ladezeit-Validierung** beim Einlesen des Regelwerks, fail-close: `etf_core_pct + satelliten_pct + gold_pct = 100` (entspricht dem Summen-Check B16 der xlsx) · jeder `roster`-Eintrag hat eine in `klassen` definierte Klasse · `satellit`-Einträge tragen ein `tier` · jeder Override nennt `grund`, `seit` und `review_am` · jeder Ticker in `entnahme_2027.tranchen` existiert in `roster` oder `etf_roster` · **Σ aller SOLL-Raten nach der §7.4-Staffel == `budget.monatlich_eur`**.

**Die Budget-Invariante ist der Ersatz für die verlorene Rolle des Feldes.** Unter der Normierung war `budget` ein Faktor der Formel — fiel es weg, rechnete nichts mehr. Unter `additiv` ergibt sich die Summe aus den Tier-Basen und der Umleitung; `budget` prüft sie nur noch nach. Das ist die schwächere, aber richtige Rolle: es beantwortet die Frage „ist der volle Monatsbeitrag verplant?", und zwar **nach** der Umleitung eingefrorener Beträge, nicht davor. Ohne diese Prüfung könnte ein eingefrorener Betrag ohne Ziel stillschweigend verschwinden — genau das, was `freigesetzt_ohne_ziel` (§7.1) meldet, nur auf Ebene der Gesamtsumme.

**Die Invariante ist heute noch nicht prüfbar, und das ist eine Aussage über §3.1, nicht über die Regel.** 1.068 € ist die **Ist**-Summe [03.09.]: ETF 563 + Gold 80 + Aktien 425. Die **SOLL**-Summe folgt aus `klassen` — Core-Titel mit `basis_eur: 50`, Satelliten mit ihrer Tier-Basis — und steht erst fest, wenn ADBE, VEEV, COST, ZETA und NOW eine Klasse und ein Tier haben. Zum Vergleich: die alte 13er-Staffel ergab 364 € Aktienbudget, die heutigen Aktien-Ist-Raten ergeben 425 €. **Die Differenz ist keine Drift, sondern die noch nicht getroffene Entscheidung.** Beim Befüllen (§9.4 Schritt 5) ist die Klassenzuordnung deshalb so zu wählen, dass die Invariante aufgeht — oder `budget` bewusst auf einen anderen Wert als den Ist gesetzt und die Differenz als Ratenänderung im Broker vollzogen. Was nicht zulässig ist: die Invariante beim Laden abzuschalten, weil sie nicht aufgeht.

**`klassen.*.flag_wirkung` ist die FLAG-Zweiteilung.** Bisher ein Vier-Stellen-Refactor über `config.yaml`, `PORTFOLIO.md`, `INSTRUKTIONEN §22` und eine xlsx-Formel; jetzt ein Wort. Dass das 3-Tier-Modell zwischen Beschluss und Depot-Wirklichkeit auseinanderlief, gehört zu dieser Fehlerklasse.

**`ohne_score: basis_voll`** macht die Owner-Conviction-Add-Praxis explizit, statt sie als „DEFCON-3-Platzhalter" zu tarnen — ein Platzhalter-Score ist ein erfundener Score in einer Datei, aus der Backtests gelesen werden.

### 3.1 Beim Befüllen zu entscheiden (Daten, nicht Spec)

| Ticker | offene Frage |
|---|---|
| GOOGL · MSFT · AMZN · META | Klasse `core` — durch Owner-Strategie 26.08. gesetzt |
| NOW | `satellit` T1 oder `core`? **12,33 % der Dynastie-Basis** [03.09.], Software-These, kein Weltmarkt-Dominator |
| Adobe · Veeva | Roster-Aufnahme als `satellit`, Tier offen |
| ZETA | Tier bestätigen (bisher T3, QuickScreener war Rot) — Rate-0-Override steht bereits (§3.3) |
| Costco | Take-Profit gewollt → Roster oder Abgang? **Offenes Sell-Limit @880** [03.09.] macht die Absicht sichtbar, den Abgang aber nicht vollzogen. Bei Abgang zusätzlich den `screener_exceptions`-Eintrag („Membership Yield") mit entfernen, sonst bleibt er verwaist |
| JEDI | Position ohne Sparplan, **offenes Sell-Limit @90** [03.09.]. Halten, aufstocken oder abgehen? Betrifft `etf_roster.soll_rate_eur` |
| JEDI · WQTM | `themenwette` |
| KYCCF | nicht mehr im Depot → aus Roster; Score 67 bleibt in der Historie |

**Diese Tabelle ist nicht nur Kosmetik: `max_aktien_slots` steht auf 13, das Depot führt 17 Aktienpositionen** [03.09.]. `slot_kapazitaet` meldet ab dem ersten Lauf FAIL. Entweder das Roster schrumpft auf 13 (COST, VEEV, ADBE, ZETA sind die Kandidaten), oder der Cap steigt — beides ist eine Owner-Entscheidung, keine Ableitung. Solange sie aussteht, ist der FAIL korrekt und soll leuchten.

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
| `cap_single_stock` | Prozentwert oder `ausgesetzt` | Position bewusst über Cap halten — NOW mit 12,33 % der Dynastie-Basis [03.09.] gegen 10 %, „bewusst übergewichtet" laut Owner-Strategie (Reconciliation §F.1) |

**NOW allein braucht zwei Overrides** und zeigt damit, warum die Liste über FLAG hinausgehen muss:

1. **Rate 0 ohne FLAG.** Am 26.08. auf 0 gesetzt zur Kapitalumschichtung; Tier 1 mit `ohne_score: basis_voll` würde 40 € fordern. Ohne `regel: rate` meldete `rate_abweichung` diesen gewollten Zustand dauerhaft als Verstoß.
2. **12,33 % gegen 10 % Cap.** Laut Owner-Strategie „bewusst übergewichtet" (Software-These). Ohne `regel: cap_single_stock` liefe der Check bis 2027 auf FAIL.

**Korrektur zu v1.5 im zweiten Punkt.** Dort stand, die Nullrate sei „genau der Mechanismus, über den sich die Position organisch unter den Cap zurückbilden soll". Das ist der langsame Weg und war die einzige Erklärung, solange der Entnahmetermin unbekannt war. Tatsächlich löst **die Entnahme am 07.08.2027** den Verstoß auf: NOW trägt 2.000 € Einstand im Topf (§2.5); mit dessen Abgang fällt der Anteil von 12,33 % auf rund 7,90 %, bei konstanten Kursen. Deshalb trägt der Override `review_am: 2027-08-07` und nicht ein gegriffenes Halbjahresdatum. **Ein Override-Ablaufdatum, das an ein reales Ereignis gebunden ist, ist ein anderes Instrument als eines, das an einen Kalenderrhythmus gebunden ist** — das erste läuft ab, weil sich die Lage geändert hat, das zweite nur, weil Zeit vergangen ist.

**Ein dritter Fall derselben Klasse: ZETA.** Position 784,70 € [03.09.], kein Sparplan, kein FLAG, kein Score — `ohne_score: basis_voll` fordert 18 €. Strukturidentisch mit NOW Punkt 1, in v1.5 aber weder in `overrides` noch hier genannt. Ohne Override meldet `rate_abweichung` dauerhaft FAIL. COST trifft es genauso, ist aber der Roster-Entscheidung nachgelagert (§3.1) — dort entscheidet sich, ob es überhaupt eine Regel gibt, von der abgewichen wird.

Alle Fälle sind strukturell gleich: bewusst akzeptierte Abweichung, nur an unterschiedlichen Checks. Genau davor warnt §3.3 selbst — eine Warnung, die immer leuchtet, wird nicht gelesen. **Die Lehre aus dem ZETA-Fund:** Die Override-Liste wurde bisher anlassbezogen gefüllt, wenn ein Titel auffiel. Beim Befüllen (§9.4 Schritt 5) ist sie stattdessen **systematisch** zu erzeugen — jede Position und jeder Sparplan einmal gegen die Regel gerechnet, jede Abweichung entweder korrigiert oder als Override begründet.

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

### 4.2 FLAG-Status — zwei Objektklassen, die v1.5 vermischt hat

**Regel:** aktiv, wenn das letzte Event je (Ticker, `flag_typ`) ein `trigger` ohne nachfolgendes `resolve` ist.

**Die Regel gilt — aber nur für gemessene FLAGs.** `flag_events.jsonl` enthält vier Trigger (MSFT, GOOGL, AVGO, AMZN). Alle vier stützen sich auf eine **externe Metrik**, die aus dem Score nicht folgt: CapEx/OCF, FCF-Trend, Insider-Selling, Tariff-Exposure. Genau deshalb brauchen sie ein Ereignis-Log — ihr Zustand ist ohne Messung nicht bekannt.

**APH ist kein solcher Fall — Korrektur gegenüber v1.5 (Owner-Entscheidung 04.09.2026, Weg B).** v1.5 führte APH als **Datenlücke**: „trägt seit 2026-04-09 einen Score-basierten FLAG, für den kein Event existiert", und leitete daraus Stufe 0 Schritt 1 ab. Das war eine **Fehlklassifikation der Spec, kein Datenfehler des Repos.**

APHs FLAG ist **ableitbar**: Score 61 < 65 → DEFCON 2. Er ist eine reine Funktion des Scores, und der steht bereits in `score_history.jsonl`. Ihn zusätzlich als Event zu führen, hieße einen abgeleiteten Wert ins Ereignis-Log zu kopieren — genau das Muster, das dieser Umbau beseitigt. Der Beleg lag im Code: `schemas.py` Z. 612 lässt für `flag_typ` ausschließlich die vier gemessenen Typen zu. **Das Enum ist nicht unvollständig, es ist korrekt eng.**

| | gemessener FLAG | abgeleiteter Score-Zustand |
|---|---|---|
| Beispiele | MSFT · GOOGL · AVGO · AMZN | APH |
| Quelle | externe Metrik, nur durch Messung bekannt | `score_history.jsonl` |
| Ort | `flag_events.jsonl` (Urteil) | keiner — wird berechnet |
| Auflösung | frische Evidenz (`resolve`-Event) | nächster Score über der Schwelle |

**Eine Lücke bleibt und wandert in §3.** Die Score-Schwelle allein erklärt APHs Rate nicht. DEFCON 2 bedeutet nach `defcon.modulation` **×0,5**, bei Tier 3 also 9 € — dokumentiert sind aber **0 €**, und der Broker führt live **20 €** (§3.3-Override). Es existiert also eine dritte, nirgends niedergeschriebene Regel: „Score unter D3-Schwelle → Rate 0". Unter Weg B ist sie **kein FLAG-Event, sondern eine Regelwerk-Regel** und gehört als solche nach `REGELWERK.yaml` — entweder als Klassenregel oder als expliziter `defcon.modulation`-Eintrag. Beim Befüllen (§9.4 Schritt 5) ist zu entscheiden, welcher der drei Werte gilt: 0 €, 9 € oder die 20 € des Overrides.

**GOOGL bleibt ein echter Fall** und wird nicht mit APH vermengt: Trigger vom 2026-03-15 ohne Resolve, gemessene Metrik (CapEx/OCF ~75 %), auflösbar nur durch frische Evidenz. Der Ausschluss-Vermerk daneben war eine Handelsregel und ist am 04.09.2026 förmlich aufgehoben (§9.3); der FLAG selbst bleibt aktiv und wirkt über Klasse `core` als Analysepflicht.

**Damit ist `flag_events.jsonl` ab sofort autoritativ** — es fehlt kein Event mehr. Was v1.5 als Vollständigkeits-Backfill plante, war die Aufforderung, eine korrekte Datei zu verunreinigen.

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

- **Zwei unabhängige Kanäle, nicht Primär und Ersatz.** CLI `sc` v0.6.0 in WSL-Distro **Ubuntu-24.04** und der MCP-Connector „Scalable Capital" halten **getrennte Sessions**. Am 04.09. war die CLI tot (`no_session`), während der Connector vollständig lieferte. `sc login` ist `human_only` — die CLI kann sich nicht selbst reanimieren.
- **Daraus folgt Probe-First.** `depot check` prüft **billig**, welcher Kanal lebt, bevor es die teure Abfragefolge startet; ist keiner erreichbar, bricht es ab, statt auf veralteten Daten zu rechnen. v1.5 nannte den Connector „Alternative" und unterstellte damit eine Rangfolge, die es nicht gibt: der Ausfall des einen sagt nichts über den anderen.
- Envelope: mit `--json` kommt `{ok, command, data}`, Nutzdaten unter **`data.result`**.
- Cache: `00_Core/.live/snapshot.json` mit Zeitstempel, **in `.gitignore`**.
- Staleness: älter als 12 h → neu ziehen; `--cached` erzwingt den Cache.
- **Filter beim Cachen:** `get_portfolio_holdings` liefert zusätzlich 32 `cryptoHoldings`-Blöcke, alle mit `filled: 0`. Der Snapshot verwirft sie; andernfalls besteht der Cache überwiegend aus Nullpositionen.

**Der Snapshot braucht eine dritte Quelle: offene Orders.** `holdings` und `savings_plans` genügen nicht. Am 03.09. standen zwei Sell-Limits offen — **COST @880 · JEDI @90** — die in **keiner** Repo-Datei vorkommen. Eine offene Order ist dokumentierte Owner-Absicht: sie sagt, dass ein Titel gehen soll, und sie kann jederzeit ausgeführt werden, ohne dass jemand etwas tut. Fehlt sie im Live-Layer, sieht `depot check` bei COST eine gehaltene Position und kennt den Take-Profit-Beschluss nicht, den §3.1 als offene Frage führt.

**Broker-Performance ist nicht die Depot-Historie.** `MAX` = `ONE_YEAR` = `YEAR_TO_DATE` = 2.238,47 € [03.09.], weil der Broker das Depot erst seit dem Übertrag am **17.08.2026** kennt. Die Serie beschreibt 17 Tage, nicht ein Jahr. Sie darf weder als Performance-Nachweis gelesen noch mit `transactions` zu einer scheinbar längeren Reihe vermengt werden.

**Kein Point-in-Time-Persistenzbedarf.** `score_history.jsonl` enthält keine Positionen und keine Raten, nur Score, Sub-Scores, FLAG-Metrik und Kurs am Score-Tag. Positions- und Orderhistorie liegt bei Scalable (`transactions` reicht nachweislich bis 18.06. zurück). §29.5 Sin #2 (Look-Ahead) bleibt unberührt.

**Was die API nicht liefert — und was das kostet.** Für `TRANSFER_IN`-Positionen gibt `get_transaction_details` nur `averagePrice` = Übertragswert zurück, nicht die historischen Anschaffungskosten. Für die drei ING-Alt-ETF ist der steuerliche Einstand damit **über keinen Kanal erreichbar** (§2.6). Der Live-Layer ist autoritativ für Bestand, Rate und Kurs — nicht für Steuerbasis. Diese Grenze gehört in den Snapshot-Kopf, damit sie nicht später als Datenfehler diagnostiziert wird.

**Split-Vorsicht bei Mengenvergleichen.** APH hatte am 03.09. einen `SWAP_OUT` 2,90389 → `SWAP_IN` 5,80778 Stk (1:2). Stückzahlen aus Records vor diesem Datum sind nicht direkt vergleichbar. `depot check` rechnet ausschließlich in Werten und ist davon nicht betroffen; die `entnahme_2027.tranchen` führen Stückzahlen und wären es — von den fünf Titeln dort ist heute keiner betroffen, die Regel gilt trotzdem.

---

## 6 · Analyse-Pflicht

Die Pflicht ist eine **Abfrage, kein Verwaltungsobjekt**. Es gibt keine Backlog-Liste zu pflegen; der Backlog ist das Ergebnis von `analyse_faellig`. Handgeschriebene Backlogs driften — die Liste vom 26.08. führte Alphabet und Veeva, obwohl beide gültige Records haben.

Eingaben, alle vorhanden: letzter Score je Ticker · nächster Earnings-Termin (`earnings_calendar.py`, SSoT) · Klasse und Kadenz (Regelwerk) · Depotanteil (Live-Layer).

### 6.1 Kadenz

| Pflicht | gilt für | Titel heute | pro Jahr |
|---|---|---|---:|
| **je Earnings** (quartalsweise) | Klasse `core` · Anteil > 5 % der **Dynastie-Basis** · aktives FLAG | GOOGL, MSFT, AMZN, META (core) · NOW (12,33 % [03.09.]) · AVGO, APH (FLAG) = **7** | 28 |
| **halbjährlich** | übrige Satelliten, via 180-Tage-Regel | ASML, V, TMO, SU, BRK.B, RMS, ZETA, Adobe, Veeva = **9** | 18 |
| **keine** | Themenwetten (JEDI, WQTM), ETF, Gold | — | — |

Zusammen ≈ 46 Analysen im Jahr, knapp eine pro Woche. Zum Vergleich: 13 in fünf Monaten.

MSFT und AMZN erfüllen zwei Kriterien gleichzeitig (Klasse `core` und aktives FLAG) und zählen einmal. Bei Klasse `core` ist Analysepflicht ohnehin der Regelfall.

**Die 5-%-Schwelle misst gegen die Dynastie-Basis, nicht gegen den Depotwert** (§2.5) — sonst zöge der Entnahme-Topf Titel in die Quartalspflicht, die nur wegen zweckgebundenen Kapitals groß aussehen. NOW ist heute der einzige Titel oberhalb der Schwelle: auf Gesamtdepot-Basis wären es 15,88 %, auf Dynastie-Basis 12,33 % — beide über 5 %, das Ergebnis ändert sich hier nicht. Bei knapperen Fällen würde es das.

**COST fehlt in beiden Zeilen bewusst.** Position 357,59 € und gültiger Score 69, aber offenes Sell-Limit (§3.1). Ob eine Analysepflicht besteht, entscheidet sich mit der Roster-Frage, nicht vorher.

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

Ablauf: Kanal proben → Zustand ziehen → **Entnahme-Topf subtrahieren** → Regelwerk laden → Urteil ableiten → SOLL rechnen → gegen IST diffen → melden → Views bauen.

**Die Subtraktion steht bewusst vor allem Rechnen.** Jeder Quotencheck — `allokation_drift`, `cap_single_stock`, `cap_us` — benutzt denselben Nenner, und der ist die Dynastie-Basis (§2.5). Wird die Subtraktion erst je Check gemacht, entstehen genau die drei verschiedenen Prozentzahlen für dieselbe Position, die diese Spec beseitigen soll. Der Report nennt seinen Nenner im Kopf, in Euro.

### 7.1 Checks

| Check | meldet | Konflikt aus Reconciliation §C |
|---|---|---|
| `regel_flag` | Rate > 0 trotz FLAG, wo Klasse `rate_null` fordert — **außer** ein gültiger Override greift (§3.3) | C1 — 135 €/Mt |
| `score_fehlt` | Position oder Sparrate ohne Record | C2 — Adobe, META, NOW, ZETA |
| `score_verfallen` | letzter Record älter als `verfall_tage` | — |
| `analyse_faellig` | Pflichttermin nach §6.1 erreicht oder überfällig | — |
| `cap_single_stock` | Position über `single_stock_max_pct`, gemessen an der Dynastie-Basis | C3 — NOW 12,33 % [03.09.] |
| `slot_kapazitaet` | belegte Aktien-Slots über `max_aktien_slots` | — (Tool B12 gegen B13) |
| `cap_us` | US-Quote **Ist** über `us_hard_cap_pct` | — |
| `cap_us_ziel` | US-Quote der **Ziel**-Allokation über Cap, je Position gewichtet | — (Tool-Funktion) |
| `rate_abweichung` | Ist-Rate ≠ SOLL nach additivem Modell (§7.4) | C4 — 3-Tier unwirksam |
| `freigesetzt_ohne_ziel` | eingefrorener Betrag, für den die Staffel aus §7.4 kein Ziel findet | — |
| `roster_fremd` | in **Position ∪ Sparplan ∪ offene Order**, nicht im Regelwerk | C5 — Adobe, Costco, Veeva |
| `roster_verwaist` | im Regelwerk, weder Position noch Sparplan noch offene Order | C5 — KYCCF |
| `allokation_drift` | Block-Abweichung über `toleranz_pp` (getrennt ETF/Gold und Aktien), Dynastie-Basis | ETF −12,1 pp · Aktien +13,3 pp [03.09.] — **Schweregrad offen, §11 Punkt 14** |
| `entnahme_ziel` | Wert des Topfs gegen `zielwert_eur`; WARN ab 3 Monate vor `ziel_datum` | 9.246,62 € gegen 10.000–11.000 € [03.09.] |
| `position_drift` | Einzelposition außerhalb Toleranz → Reduzieren / Aufstocken / Halten | — (Tool Spalte L) |
| `nachkauf_signal` | Fehlbetrag über `nachkauf_schwelle_eur`; bei FLAG „gesperrt" statt Kaufsignal | — (Tool Spalte J/R) |
| `flag_gate_faellig` | Resolve-Gate-Termin erreicht | AVGO 03.09. |
| `override_faellig` | Override über `review_am` hinaus aktiv | — |

C6 (Broker-Modell überholt) braucht keinen Check: Broker ist Zustand und hört auf, eine Regel zu sein.

**Warum `roster_fremd` und `roster_verwaist` die offene Order brauchen.** Mit nur zwei Eingaben gilt ein bloß *beabsichtigter* Abgang als vollzogen, sobald der Sparplan endet — oder umgekehrt ein Titel als fremd, für den längst eine Order liegt. COST ist der lebende Fall: Position vorhanden, Sparplan aus, Sell-Limit @880 offen. Ohne die dritte Menge behauptet der Check, COST sei ein regulär gehaltener Fremdtitel; mit ihr sagt er, was zutrifft — ein Abgang, der auf seinen Kurs wartet.

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

**Größenordnung [Stand 03.09.].** Die Klassen-Zweiteilung hat das Problem weitgehend aufgelöst: MSFT und AMZN werden `core` und frieren nicht mehr ein, APH läuft über einen Override. Von den ursprünglich 135 €/Monat bleibt **AVGO mit 40 €**. Score 56 = DEFCON 2, also kein Substitutionsfall → **Stufe 2 der Staffel, Ziel ETF-Core.** Das Cash-Drag-Argument, das für die Normierung sprach, trägt bei dieser Größe nicht mehr.

**Korrektur zu v1.5 — das Ziel war Gold.** Dort stand „Ziel Gold (2,7 % gegen 5 %)". Die Zahl war der Gold-Anteil am **Gesamtdepot**. Auf der Dynastie-Basis (§2.5) liegt Gold bei **3,8 %**, also −1,2 pp und damit **innerhalb** der 1,5-pp-Toleranz; größter Unterhang ist der **ETF-Core mit −12,1 pp**. Die Regel „an den größten Unterhang" war richtig und ist unverändert — nur ihr eingefrorenes Ergebnis war es nicht.

**Und darum steht hier kein Ergebnis mehr.** Ein Zielblock ist eine **Live-Ableitung**, keine Konstante: er wechselt, sobald sich Kurse oder Raten bewegen. Ihn im Fließtext festzuschreiben, hat genau einmal funktioniert und dann zehn Tage lang eine falsche Auskunft gegeben. `depot check` rechnet ihn bei jedem Lauf neu; der Beispielwert oben trägt einen Stichtag und ist nicht Teil der Regel.

**Bekannter Nebeneffekt:** Bei lange aktiven FLAGs verschiebt sich die Quote vorübergehend zugunsten von Gold und ETF. Das ist gewollt — ein materialisiertes Einzeltitel-Risiko soll in die breite Basis fließen, nicht in andere Einzeltitel. Sichtbar bleibt es über `allokation_drift`; still ist es nicht.

**Warum die Sparraten-Verteilung nicht 60/35/5 spiegeln muss.** Owner-Entscheidung 04.09.: `allokation` gilt **wertbasiert** (§3). Die Gold-Rate liegt bei 80 von 1.068 € = 7,5 %, der Bestand bei 3,8 % — das ist kein Regelverstoß, sondern der Aufholmodus, der ihn beheben soll. Umgekehrt gilt dasselbe als Warnung: die ETF-Rate von 563/1.068 = **52,7 %** liegt unter dem 60-%-Ziel. Bei gleicher Rendite beider Blöcke konvergiert der Bestandsanteil gegen den Ratenanteil — unter dieser Annahme wird 60 % nicht erreicht; der Stabilisierungs-Floor läge bei einer ETF-Rate von **641 €**. Die Annahme ist streng: bei ETF-Outperformance wird das Ziel erreicht, bei Aktien-Outperformance verfehlt. Das ist eine Beobachtung für `depot check`, keine Handlungsanweisung — und ausdrücklich **kein** Argument für Verkäufe (§7.5).

### 7.5 Konzentrations-Kappung — der zweite zulässige Verkaufspfad

**Die Unterscheidung, ohne die `niemals_durch_verkauf` falsch gelesen wird:**

> **Block-Rebalancing** — ETF/Aktien/Gold durch Verkauf auf Zielquote zurückführen → **verboten.** `KONTEXT.md` §7, `Rebalancing_Tool` B23. Das Instrument ist die Umleitung der Sparrate, nicht der Verkauf.
>
> **Konzentrations-Kappung** — eine Einzelposition wächst über ihren Cap, der Überhang wird verkauft → **erlaubt.** Das ist Risikokontrolle gegen idiosynkratisches Risiko, keine Quotenpflege.

Beides unter ein Pauschal-Flag `niemals_durch_verkauf: true` zu stellen, verwechselt sie. Deshalb steht im Regelwerk jetzt `block_rebalancing_durch_verkauf: verboten` plus eine **abschließende** Liste zulässiger Pfade (§3). Der erste dieser Pfade ist keine Neuerung: `system_regeln.substitute_activation_global.steuer_regel` kennt ihn bereits — „Bei unvermeidbarem Verkauf: Abgeltungsteuer 26,375 % + FIFO + Freibetragscheck". Die Kappung ist der zweite, die geplante Entnahme 2027 der dritte.

**Warum die Kappung als Ernte-Mechanismus trägt** (Owner-Vorschlag 04.09.2026, Prinzip freigegeben):

- **Kein Markttiming.** Auslöser ist die Positionsgröße, nicht ein Kursziel. Das ist mit `KONTEXT.md` §1 verträglich — dort ist nicht Verkaufen verboten, sondern das Raten über Kurse.
- **Erntet strukturell nur Gewinner.** Über den Cap wächst eine Position nur durch Kursanstieg (die Sparrate ist gedeckelt und bei FLAG null).
- **Verkauft nur den Überhang.** Die Kernposition bleibt, die These bleibt investiert.
- **Der Erlös hat ein definiertes Ziel.** ETF-Core — dieselbe Richtung wie die §7.4-Staffel. Kein freies Cash, das eine Wiederanlage-Entscheidung erzwingt.

**Was das heute kostet: nichts.** Bei `single_stock_max_pct: 10` auf der Dynastie-Basis [03.09.: 22.881 € → Cap 2.288 €] ist **nur NOW** gebunden (12,33 %), und dort greift der Owner-Override bis 07.08.2027 (§3.3). Die nächstgrößte Aktienposition ist ADBE mit 4,3 %. Die Regel liegt vorerst still. **Als Leitplanke ist sie trotzdem jetzt richtig zu formulieren** — sie soll stehen, bevor der erste Titel sie erreicht, nicht danach; eine Kappungsregel, die während des Anstiegs geschrieben wird, wird für diesen Anstieg geschrieben.

**Die Parameter sind offen und stehen bewusst nicht hier** — Höhe, Bezugsgröße, Hysterese und die Kopplung ans Steuerjahr: §11 Punkt 15. Ebenso die Frage, ob der Cap als einziger Ernte-Auslöser genügt: §11 Punkt 16. Solange diese Punkte offen sind, ist §7.5 eine **Zulässigkeitsaussage**, kein ausführbarer Mechanismus — `depot check` meldet den Cap-Verstoß (`cap_single_stock`) und schlägt keine Order vor.

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

- **`KONTEXT.md`** → **neu in v1.6, vorher an keiner Stelle der Spec.** Die Zustands-Abschnitte (§2 Broker, §3 Raten und Positionszahlen, §4 ETF-Zuordnung) entfallen; die Regelwerk-Abschnitte (§3 Caps, §5 Roster, §6 Ersatzbank, §7 Freibeträge) ziehen nach `REGELWERK.yaml`; die Doktrin (§1, §8, §9) bleibt handgeschrieben. Vollständige Zuordnung und die verifizierte Drift in **§2.4**. Zeitpunkt: **Stufe 1 Schritt 7**, im selben Commit wie `CLAUDE.md` — aus demselben Grund.

**`CLAUDE.md` und `KONTEXT.md` sind damit Sync-Ziele der Migration** — `CLAUDE.md` fehlte in v1.0 ganz und war in v1.4 auf „xlsx-Referenzen entfernen" verengt; `KONTEXT.md` fehlte bis v1.5 vollständig. Tatsächlich betroffen sind sechs Stellen (Z. 27, 29, 57, 59, 77, 78), darunter der vollständige Sync-Pflicht-Bullet, der das alte 8-9-Datei-Modell im Fließtext festschreibt, sowie zwei Routing-Zeilen, die `paragraph-18-sync` aufrufen. Weil die Datei zu Beginn **jeder** Session gelesen wird und darüber entscheidet, ob `INSTRUKTIONEN.md` überhaupt lädt, ist sie kein nachlaufendes Sync-Ziel, sondern gehört in denselben Commit wie der Move. Eine dort stehen gebliebene Sync-Anweisung wirkt stärker als jede korrigierte Spec.

**Für `KONTEXT.md` gilt derselbe Mechanismus, nur seltener und dafür gezielter.** Die Routing-Table lädt sie bei jeder Strategie- und Allokationsfrage — also genau dann, wenn jemand wissen will, wo das Geld hinsoll. Dort steht heute ein leergeräumtes ING-Depot als aktiver Broker und eine Freibetragsaufteilung, die es nicht mehr gibt. Der Fall ist am 04.09. eingetreten: Die Session las die veraltete Steuer-Tabelle und schloss aus ihr auf einen ungenutzten Freibetrag — eine Behauptung, die anschließend zurückgezogen werden musste. Eine Doku-Drift, die der Agent regelmäßig liest, ist keine Kosmetik, sondern eine Fehlerquelle mit Beleg.

### 9.3 Stufe 0 — Datenreparatur, Voraussetzung für alles Weitere

Ohne diesen Schritt zementiert der Umbau bestehende Fehler.

1. ❌ **ENTFÄLLT — der Schritt war selbst der Fehler.** Ursprüngliche Fassung: APH-Trigger nachtragen mit `flag_typ: score_basiert` via `archive_flag.py trigger`. Der Ausführungsversuch am 04.09.2026 scheiterte am Schema; die Analyse ergab, dass nicht das Schema zu eng, sondern die Spec falsch war. **Owner-Entscheidung 04.09.2026 (Weg B): APH wird nicht als Event geführt** — §4.2. Es fehlt kein Event, `flag_events.jsonl` ist bereits vollständig. Herleitung und Konsequenzen: §9.3.1.
2. ✅ **ERLEDIGT 04.09.2026 — AMZN-FLAG in `config.yaml flags_aktiv` ergänzt.** Der FLAG lief seit 15.05. in `flag_events.jsonl`, `PORTFOLIO.md` und `Faktortabelle.md`, fehlte aber in `flags_aktiv`. Reine Auslassung; die Rate stand korrekt auf 0 €, weil `PORTFOLIO.md` führend war. `flags_aktiv` = MSFT · APH · AVGO · AMZN.
3. ✅ **ERLEDIGT 04.09.2026 — GOOGL-Ausschluss förmlich aufgehoben**, an drei Stellen (siehe unten). `flags_watchlist` steht jetzt auf `[]`, der Originaleintrag bleibt als Kommentar erhalten.
4. ✅ **ERREICHT 04.09.2026** — `flag_events.jsonl` ist die einzige gelesene FLAG-Quelle. **Stufe 0 ist damit abgeschlossen.**

#### 9.3.1 Warum Schritt 1 entfiel — und was der Ausführungsversuch über Prüfrunden verrät

`03_Tools/backtest-ready/schemas.py` Z. 612:

```python
flag_typ: Literal["capex_ocf", "fcf_trend_neg", "insider_selling_20m", "tariff_exposure"]
```

`score_basiert` steht nicht im Enum; die CLI lehnt den Wert ab, bevor irgendetwas geschrieben wird. Zusätzlich verlangt der Validator zu jedem `flag_typ` eine `schwelle` aus `FLAG_RULES` und prüft, dass ein Trigger sie *verletzt* — für einen score-basierten FLAG existiert dort kein Eintrag.

**Der Code wusste es bereits.** `03_Tools/backtest-ready/backfill_flags.py` Z. 104 trägt wörtlich `flag_typ="score_basiert",  # NICHT im schema-enum`. Der Kommentar ist älter als diese Spec.

**Die Folge trifft die Stufen-Ordnung, nicht nur diesen Schritt.** §9.3 nennt Stufe 0 die „Voraussetzung für alles Weitere". Schritt 1 dieser Voraussetzung braucht eine Schema-Änderung (Enum + `FLAG_RULES` + `schema_version`-Bump), und §4.1 weist Schema-Bumps ausdrücklich **Stufe 2 Schritt 9** zu. Die Abhängigkeit läuft rückwärts: **Stufe 0 ist nicht unabhängig von Stufe 2.** Das ist kein Tippfehler, sondern ein Planungsfehler, den vier Prüfrunden nicht gefunden haben — weil niemand den Schritt ausgeführt hat.

**ENTSCHIEDEN 04.09.2026 — Weg B: APH wird nicht als Event geführt.**

Ein score-basierter FLAG ist **ableitbar**: Score 61 < 65 → DEFCON 2. Er ist eine reine Funktion des Scores, der bereits in `score_history.jsonl` steht. Die vier Enum-Typen sind allesamt **externe** Metriken, die aus dem Score nicht folgen — genau deshalb brauchen sie ein Ereignis-Log. Einen abgeleiteten Wert dort einzutragen, wäre die Kopie, die dieser Umbau beseitigt.

**Damit kehrt sich der Befund um.** Das Enum ist nicht unvollständig, sondern korrekt eng. Nicht `schemas.py` war zu streng — **§4.2 hat den Fall falsch klassifiziert** und daraus einen Reparaturschritt abgeleitet, der eine korrekte Datei verunreinigt hätte. §4.2 ist entsprechend neu gefasst.

**Der verworfene Weg A** hätte `flag_typ` um `score_basiert` erweitert, einen `FLAG_RULES`-Eintrag (Schwelle 65, Richtung `<`) ergänzt und `schema_version` auf 1.1 gehoben — samt `sum_consistency.py`. Er hätte funktioniert und Stufe-2-Arbeit vorgezogen. Er hätte aber die Vermischung zementiert, statt sie aufzulösen.

**Die Stufen-Ordnung ist damit wiederhergestellt:** Stufe 0 braucht keinen Schema-Bump und ist tatsächlich voraussetzungsfrei — allerdings erst, nachdem der Ausführungsversuch den Planungsfehler sichtbar gemacht hat. **Hätte man Weg A ohne diese Analyse gewählt, wäre die Rückwärts-Abhängigkeit real geworden** — und niemand hätte gemerkt, dass sie vermeidbar war.

**Eine Restaufgabe wandert nach §3:** Die Score-Schwelle erklärt APHs Rate nicht vollständig (0 € dokumentiert, 9 € nach `defcon.modulation`, 20 € live beim Broker). Die dahinterliegende Regel „Score unter D3-Schwelle → Rate 0" ist nirgends niedergeschrieben und gehört als **Regelwerk-Regel** nach `REGELWERK.yaml`, nicht als Event (§4.2 Schluss, §9.4 Schritt 5).

**Lehre — die wichtigste dieser Spec.** Ein Reparaturschritt, der nie ausgeführt wurde, ist keine verifizierte Anweisung. Schritt 1 stand seit v1.1 in vier Fassungen, hat vier Codex-Runden und ein 95%-Confidence-Gate überlebt und war die ganze Zeit **nicht nur unausführbar, sondern inhaltlich falsch**. Gescheitert ist er in der Sekunde, in der jemand `--help` aufgerufen hat. Prüfrunden lesen, was dasteht; Ausführung prüft, ob es stimmt — **das sind verschiedene Achsen, und die zweite war hier stärker als vier Durchgänge der ersten.** **Regel ab jetzt: Vor der Freigabe einer gestuften Migration wird jeder Schritt, der ein Tool aufruft, gegen dessen Signatur gelesen — und pro Stufe geprüft, ob wirklich nur Vorwärts-Abhängigkeiten bestehen. Wo möglich wird der Schritt trocken ausgeführt, bevor er freigegeben wird.**

**Der GOOGL-Trigger gehört nicht hierher.** Ihn aufzulösen erfordert nach dem eigenen Modell frische Evidenz (§4.2) — das ist Analysearbeit, keine Datenhygiene. Bis dahin gilt die konservative Lesart: **ein Trigger ohne Resolve ist aktiv.** Das Modell trägt den Fall von selbst, weil GOOGL Klasse `core` ist und `flag_wirkung: analysepflicht` gilt: Der offene FLAG stoppt keine Rate, sondern macht GOOGL über `analyse_faellig` (§6.1) analysepflichtig. Der Titel landet damit im Analyse-Backlog, wo er hingehört — und nicht in einem Reparaturschritt, der ihn stillschweigend wegräumt.

**Der Ausschluss dagegen schon — und er ist entschieden.** `entities/ersatzbank/GOOGL.md` führt GOOGL als „struktureller Ausschluss seit 01.04.2026 — kein Einstieg", `config.yaml flags_watchlist` als „Kein Einstieg, kein Nachkauf bis FLAG aufgehoben" — während seit dem 26.08. ein Sparplan über 50 €/Mt läuft und seit dem 01.09. eine Position besteht. v1.5 kannte nur die Vault-Seite und bot deshalb zwei Wege an (aufheben oder Override).

**Owner-Entscheidung 04.09.2026: förmlich aufheben.** Konkret, alle drei im selben Commit:

| Ort | Aktion |
|---|---|
| Chronik (`CORE-MEMORY §12` + `log.md`) | Eintrag mit **Datum und Begründung**, dass der Ausschluss vom 01.04.2026 aufgehoben ist |
| Vault `entities/ersatzbank/GOOGL.md` | Ausschluss-Vermerk auflösen, auf den Chronik-Eintrag verweisen |
| `config.yaml flags_watchlist` | GOOGL-Eintrag entfernen — die Handelsregel „kein Einstieg" existiert nicht mehr |

**Der CapEx/OCF-FLAG bleibt davon unberührt und bleibt aktiv.** Das ist der Kern der Entscheidung und keine Inkonsequenz: Ein Ausschluss ist eine *Handelsregel* („nicht kaufen"), ein FLAG ist ein *Urteilsstand* („Risiko offen, Evidenz fehlt"). Der Ausschluss wird aufgehoben, weil der Owner GOOGL bewusst als Core-Titel aufbaut; der FLAG bleibt, weil ihn nur frische Evidenz auflöst (§4.2). Er wirkt über Klasse `core` als `flag_wirkung: analysepflicht` — stoppt also keine Rate, sondern erzwingt die Analyse. **Damit braucht GOOGL keinen Override mehr** (§3): Was v1.5 als Ausnahme modellieren musste, ist nach der Aufhebung der Regelfall.

**Warum das trotzdem in Stufe 0 gehört und nicht in die laufende Pflege.** Bliebe die Divergenz stehen, würde der Umbau eine dokumentierte Owner-Entscheidung stillschweigend aufheben — genau die stille Regeländerung, gegen die §3.3 argumentiert. Der Unterschied zwischen „aufgehoben" und „ignoriert" ist der Chronik-Eintrag, und den schreibt niemand nachträglich.

**Deckungsgleich sind die FLAG-Listen nach Stufe 0 nicht** — GOOGL trägt weiterhin einen offenen Trigger, den keine der Markdown-Dateien führt. Das ist kein Restfehler, sondern der Unterschied zwischen „eine Quelle ist maßgeblich" und „alle Kopien stimmen überein". Genau diesen Unterschied stellt der Umbau her.

### 9.4 Stufe 1 — begrenzter Blast-Radius

5. `REGELWERK.yaml` anlegen und befüllen — **aus drei Quellen, nicht aus einer:** `config.yaml` (§2.1), das xlsx-Parameterblatt (§2.3) und `KONTEXT.md` §§ 3/5/6/7 (§2.4). Für die xlsx heißt das: **alle drei Dateien mit `openpyxl` durchgehen und jeden Wert protokollieren, der keine Entsprechung in `.md`/`.yaml` hat** — B10 ist der bekannte Fall, nicht notwendig der einzige; für `Satelliten_Monitor` und `Watchlist_Ersatzbank_Monitor` ist bisher nichts geprüft. Dazu Klassen nach §3.1, Ersatzbank nach §3.2, Overrides nach §3.3 — Letztere **systematisch**, jede Position und jeder Sparplan einmal gegen die Regel gerechnet, nicht anlassbezogen. **Voraussetzung: laufender Live-Layer** — die ISINs des Rosters existieren nirgends im Repo und werden einmalig aus `holdings ∪ savings_plans` gezogen. Für Roster-Titel ohne Position **und** ohne Sparplan ist die ISIN von Hand zu ergänzen. Stufe 1 ist damit nicht offline durchführbar.
6. `depot check` als reiner Report bauen (Live-Layer inkl. **Probe-First** und **offenen Orders** nach §5, Entnahme-Subtraktion nach §2.5, Checks, Verteilungsrechnung). Noch kein View-Bau.
7. Die drei xlsx nach `05_Archiv/` verschieben — **Vorbedingung: Schritt 5 hat die Parameter-Extraktion nachweislich abgeschlossen** (§2.3; sonst archiviert der Move geltende Regeln, darunter die einzige Quelle des Single-Stock-Caps). Der Move läuft **gemeinsam** mit: Stilllegung von `xlsx-smoke-test-runner` und `precommit/xlsx_smoke_test.py`, Fix von `para18_sync/validator.py` (hart codierter Pfad), und Entfernen der xlsx-Referenzen aus `CLAUDE.md`, `INSTRUKTIONEN.md`, `SYSTEM.md`. **`para18_sync_reminder.py` bleibt aktiv** (§9.2).
   Zu Schritt 7 gehören zusätzlich die Neufassungen von **`CLAUDE.md`** und **`KONTEXT.md`** (§2.4 — Zustands-Abschnitte raus, Regelwerk-Abschnitte nach `REGELWERK.yaml`, Doktrin bleibt), und zwar über die xlsx-Dateinamen hinaus: der Sync-Pflicht-Bullet (Z. 27) beschreibt das alte 8-9-Datei-Modell im Fließtext, die Routing-Zeile „§18-File-Touch" (Z. 78) und die `!ParaSync18`-Zeile (Z. 77) rufen einen Skill, der zurückgebaut wird, und die Projektstruktur (Z. 57/59) führt `paragraph-18-sync`, `xlsx-smoke-test-runner` sowie alle drei xlsx als aktives Inventar. Bleibt das stehen, folgt der Agent nach dem Move weiter der alten Prosa — mit zwei konkreten Folgen: manuelles Editieren von `PORTFOLIO.md` entgegen §8, und Suche nach xlsx-Pfaden, die es nicht mehr gibt.
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
| **Entnahme-Topf bewegt** (Zukauf, Teilverkauf, Entnahme 2027) | `REGELWERK.yaml` `entnahme_2027.tranchen` · Chronik — der einzige Zustand, der von Hand nachgezogen wird, bewusst (§2.5) |
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
11. **JEDI** — Position (153,34 € [03.09.]) ohne Sparplan, **offenes Sell-Limit @90** (+32 % vom Kurs entfernt). Halten, aufstocken oder abgehen? Betrifft `etf_roster.soll_rate_eur`.
12. ~~**GOOGL-Ausschluss**~~ **ENTSCHIEDEN 04.09.2026:** förmlich aufheben, an drei Stellen (§9.3). FLAG bleibt aktiv, Override entfällt.
13. **ETF-SOLL-Raten** — **eingegrenzt durch Entscheidung 2** (`budget: 1068`, Ist übernommen): die sechs Positionswerte folgen dem Ist (Σ 563). Offen bleibt allein JEDI mit `soll_rate_eur: 0` → Punkt 11.

**Neu mit v1.6 — die vier Fragen, die diese Runde bewusst nicht beantwortet hat.** Sie stehen hier und nicht im Kern, weil beide Antworten vertretbar sind und die Wahl dem Owner gehört.

14. **`allokation_drift` — FAIL, WARN oder INFO?** Auf der Dynastie-Basis [03.09.] liegen ETF bei −12,1 pp und Aktien bei +13,3 pp, beide über der Warnschwelle. In der Session wurden beide Lesarten vertreten: „ROT, Handlungsbedarf" gegen „der Check ist falsch konstruiert".
    **Was für die zweite Lesart spricht:** Die Drift ist **kein Disziplinproblem.** Der Aktien-Überhang beträgt 3.040 €; der Überschuss der Aktienrate liegt bei 51 €/Mt — über die Rate hätte der Aufbau **59 Monate** gedauert. Er ist Bestand: der ING-Übertrag brachte fast nur ETF (8.444,88 €), die Einzelaktien wurden bei Scalable gebaut und haben outperformt. In einem System, das Rebalancing durch Verkauf ausschließt (§7.5) und Satelliten-Rotation über dreißig Jahre vorsieht, ist eine Blockabweichung in der Aufbauphase möglicherweise der **erwartete** Zustand — dann wäre FAIL die eingebaute Warnung, die immer leuchtet, gegen die §3.3 argumentiert.
    **Was für die erste spricht:** Ein Ziel, dessen Verfehlung folgenlos gemeldet wird, ist keins.
15. **Cap-Parameter für §7.5.** Vier Teilfragen, jede eigenständig: **Höhe** (B10 sagt 10 % — nach der Entnahmetopf-Trennung neu zu bewerten, weil derselbe Prozentsatz auf kleinerer Basis eine kleinere absolute Position bedeutet) · **Bezugsgröße** (Gesamtdepot, Dynastie-Basis oder Aktienblock? 10 % der Dynastie-Basis sind **28,6 %** des Aktienblocks — dieselbe Zahl, drei sehr verschiedene Regeln) · **Hysterese** (bei exakt 10 % zu kappen heißt, bei jedem weiteren Anstieg erneut zu verkaufen; ein Band — kappen bei 12 %, zurück auf 10 % — vermeidet das) · **Steuerjahr-Kopplung** (der Freibetrag ist jährlich, ein Q4-Termin nutzt ihn, eine Sofort-Mechanik verschenkt ihn).
16. **Ernte-Auslöser — reicht der Cap allein?** Oder braucht es einen zweiten (Thesenerfüllung, Bewertung)? **Der einzige dokumentierte Präzedenzfall geht in die andere Richtung:** `KONTEXT.md` §5 hält fest, der „VEEV+COST-Erlös finanziert mit" — dort ging der Erlös in **neue Satelliten**, nicht in den ETF-Core. Bevor §7.5 den ETF-Core als Ziel festschreibt, ist zu klären, ob das die Praxis ändern soll oder ob beide Ziele nebeneinander gelten.
17. **FIFO-Beleg für die Entnahme 2027 — mit Frist.** Die ING-Einstandsdaten für IWDA (34), EIMI (40) und EXUS (53 Stk) sind **über keinen API-Kanal erreichbar** (§2.6). Quelle ist die ING-Übertragungsanzeige oder das Scalable-Steuerreporting. Ohne den Beleg ist unklar, ob die 2.000 € Freibetrag 2027 reichen. **Zu beschaffen vor Q3/2027**, nicht im Zuge dieser Migration — aber hier notiert, weil es sonst niemand aufschreibt.
18. **`max_aktien_slots` 13 gegen 17 Ist-Positionen** [03.09.]. `slot_kapazitaet` meldet FAIL, sobald `depot check` läuft. Roster schrumpfen oder Cap anheben — hängt an §3.1 und ist dort die eigentliche Frage.
19. ~~**APH-FLAG: Schema erweitern oder als ableitbar behandeln?**~~ **ENTSCHIEDEN 04.09.2026 — Weg B** (§9.3.1): APH wird nicht als Event geführt, weil ein score-basierter FLAG aus `score_history.jsonl` ableitbar ist. §4.2 neu gefasst, das `flag_typ`-Enum bleibt unverändert, **Stufe 0 ist abgeschlossen**. Restaufgabe daraus: die Regel „Score unter D3-Schwelle → Rate 0" ist nirgends niedergeschrieben (0 € dokumentiert / 9 € nach Modulation / 20 € live) und gehört beim Befüllen nach `REGELWERK.yaml`.
20. **GOOGL-Vollanalyse vor dem 22.09.2026 — terminiert, nicht offen.** Kein Architektur-Punkt, aber der einzige mit hartem Datum: Score 72 verfällt (§1.1), der CapEx/OCF-Trigger vom 15.03. ist offen, die Rate läuft mit 50 €/Mt und seit 01.09. besteht eine Position. Die Analyse entscheidet zugleich über den FLAG-Resolve.

*Geschlossen mit v1.5: Punkte 4, 5, 6, 7. Geschlossen mit v1.6: Punkt 12; Punkt 13 eingegrenzt.*
*Anmerkung zu Punkt 4: die dort genannten Live-Ist-Quoten 57,4/39,9/2,7 sind vom 26.08. und gegen den **Gesamtdepotwert** gerechnet. Maßgeblich ist die Dynastie-Basis — 47,9/48,3/3,8 [03.09.], §2.5. Die Klärung der Zieldefinition bleibt davon unberührt.*

---

## 12 · Prüfung dieser Spec

- **Vollständigkeit — mit benanntem Suchraum.** §2.1 ordnet jeden Top-Level-Block aus `config.yaml` einer Schicht zu; §2.3 das xlsx-Parameterblatt; §2.4 `KONTEXT.md`. Jede heute im §18-Set geführte Datei ist in §2, §8 oder §1.2 als Quelle, generiert oder entfallend klassifiziert. **Nicht abgedeckt und offen deklariert:** die Blätter der beiden anderen xlsx jenseits des Parameterblatts (§9.4 Schritt 5) und der `satelliten`-Block feldweise über §2.2 hinaus.
- **Deckung:** Jeder Konflikt aus Reconciliation §C hat in §7.1 einen benannten Check; C6 ist begründet gegenstandslos.
- **Empirie:** Die in §9.1 genannten Zugriffe sind am Quellcode verifiziert, nicht aus Suchtreffern erschlossen. Die Ableitungsregeln in §4 sind gegen die realen jsonl-Dateien getestet. Live-Zahlen tragen einen Stichtag und sind gegen die Scalable-API belegt (04.09., MCP-Kanal).
- **Negativbefunde nennen ihren Suchraum.** Jede Aussage der Form „X existiert nicht" nennt, wo gesucht wurde. Das ist keine Stilregel, sondern die Konsequenz aus dem schwersten Fehler dieser Runde: „Single-Stock-Cap nirgends verankert" war das Ergebnis eines `grep` über `.md` und `.yaml` — der Wert steht in einer `.xlsx` (§2.3). Ein Suchraum ohne Binärdateien liefert über Binärdateien keine Auskunft.

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

### R5 — Live-Verifikation und sechs Owner-Entscheidungen (2026-09-04)

Grundlage: `02_Analysen/2026-09-04_Depot-Live-Verifikation.md`. Alle 24 Positionen tranchenscharf gegen den Broker verifiziert (MCP-Kanal; die CLI war tot, §5). Erste Runde, die nicht nach Fehlern **in** der Spec suchte, sondern nach **Quellen außerhalb** von `config.yaml`.

**Sechs Owner-Entscheidungen, alle im Kern verankert:**

| # | Frage | Entscheidung | steht in |
|---|---|---|---|
| 1 | Woran misst `allokation_drift`? | **wertbasiert** — 60/35/5 gilt dem Bestand, die Rate ist das Instrument | §3 `allokation.gilt_fuer` · §7.4 |
| 2 | `budget.monatlich_eur` | **1.068 €** (Ist übernommen); Rolle korrigiert: Erhaltungs-Invariante, keine Eingangsgröße | §3 |
| 3 | GOOGL-Ausschluss | **förmlich aufheben**, drei Stellen; FLAG bleibt aktiv | §9.3 · §11.12 |
| 4 | Entnahme-Topf im US-Cap? | **nein** — aus allen Dynastie-Quoten heraus | §2.5 · §3 `quoten_basis` |
| 5 | Zieldatum Entnahme | **07.08.2027** | §2.5 |
| 6 | Modellierung des Topfs | **kein Tranchen-/Klassen-Konstrukt** — ein Block, fünf Zeilen, eine Subtraktion | §2.5 · §7 |

**Befunde:**

| Befund | Status in v1.6 |
|---|---|
| **R5-H14** xlsx-Parameterblatt ist nicht inventarisierte Regelwerk-Quelle; **B10 Single-Stock-Cap existiert nur dort** und wandert in Stufe 1 ins Archiv | **§2.3 neu** · §1.2 · §3 `caps` · §9.4 Schritt 5 als Move-Vorbedingung |
| **R5-H15** `KONTEXT.md` fehlt vollständig als Migrations-Sync-Ziel, wird aber bei jeder Allokationsfrage geladen; sechs Drift-Stellen verifiziert | **§2.4 neu** · §1.2 · §9.2 · §9.4 Schritt 7 |
| **R5-H10** `config.yaml` hat drei FLAG-Blöcke, die Spec kannte einen; GOOGL steht in `flags_watchlist` — Widerspruch ist dreifach, nicht zweifach; `flags_watchlist` war zudem als Urteil fehlklassifiziert (ist Regelwerk) | §1.1 · §2.1 · §9.3 |
| **R5-H11** §7.4 verankert ein basisabhängiges Rechenbeispiel („Ziel Gold 2,7 % gegen 5 %") — auf der maßgeblichen Basis liegt Gold **innerhalb** der Toleranz, größter Unterhang ist ETF-Core | §7.4 korrigiert, Beispiel mit Stichtag entschärft |
| **R5-H1** ZETA fehlt in der Override-Liste — strukturgleich mit NOW „Rate 0 ohne FLAG" | §3 `overrides` · §3.3 |
| **R5-M5** §1.1 widersprach sich bei GOOGL („ohne Record" gegen „hat gültige Records") | §1.1 korrigiert — ohne Record sind ADBE, META, NOW, ZETA |
| **R5-M6** Verfall hat ein hartes Datum: **GOOGL 22.09.2026**, danach zehn im Oktober | §1.1 Verfalls-Tabelle |
| R5-K1…K4 Live-Zahlen ohne Stichtag · Performance ≠ Depot-Historie · offene Orders fehlen im Live-Layer · `roster_fremd` braucht die dritte Menge | Header · §5 · §7.1 |

**Korrektur-Log: sechs Fehlaussagen, eine Wurzel.** In derselben Session entstanden sechs falsche Aussagen — „die Drift löst sich auf" (nur eine von fünf Tranchen aus dem Nenner genommen), VEEV als Exit-Kandidat (Roster-Notiz gelesen, laufenden Sparplan ignoriert), Verkauf als Drift-Reaktion (`KONTEXT.md` nicht gelesen, das es in einer Zeile verbietet), „NOW braucht 18 Monate Verwässerung" (Entnahmetermin unbekannt), „Single-Stock-Cap nirgends verankert" (`grep` ohne `.xlsx`), „998 € Freibetrag ungenutzt" (Abfragefenster begann erst am 25.07.; unbelegt und aus der Spec entfernt). **Jede einzelne Rechnung war korrekt.** Falsch war jedes Mal der Ausschnitt: Teil-Basis, Teil-Datei, Teil-Verzeichnis, Teil-Zeitfenster, fehlender Kontext.

**Methodische Lehre — die vierte, und sie schlägt die ersten drei.** R1–R3 prüften Schreibpfade, R4 prüfte gegen Live-Daten, R5 prüfte den **Suchraum selbst**. Alle sieben R5-Befunde liegen außerhalb dessen, was die Vorrunden abgesucht hatten, und zwei waren nur durch die Frage zu finden „woher weiß ich, dass ich alles gesehen habe?" statt „stimmt, was ich sehe?".

> **Regel für alles Weitere:** Vor jeder Aussage über **Abwesenheit oder Vollständigkeit** wird der Suchraum benannt — welcher Nenner, welche Dateitypen, welcher Zeitraum, welche Quellen. Ein negativer Befund ist erst belastbar, wenn der Suchraum steht. Widerspricht er dem Gedächtnis des Owners, wird **zuerst der Suchraum angezweifelt**, nicht das Gedächtnis.
>
> **Korollar für Migrationen:** Eine Datei, die archiviert werden soll, wird vorher inventarisiert. Die drei xlsx halten Regelwerte, die in keiner `.md` und keiner `.yaml` stehen.

**Präzisierung, die sich R5 selbst vorhält:** „60 % sind mit der heutigen Rate unerreichbar" war zu absolut. Es gilt nur *ceteris paribus* — bei gleicher Rendite beider Blöcke (§7.4).

**Nächster Schritt:** Codex-Gegenprüfung auf §2.3, §2.4 und die sechs Entscheidungen, danach Owner-Freigabe, danach Stufe 0.

---

*Dynasty-Depot · Architektur-Spec v1.6.2 · Stand 2026-09-04 · Entwurf zur Freigabe. v1.6.2-Delta: Owner-Entscheidung Weg B — §4.2 neu gefasst (gemessene vs. abgeleitete FLAGs), Stufe 0 abgeschlossen, §11 Punkt 19 geschlossen. Die schwerste Korrektur dieser Spec stammt nicht aus einer Prüfrunde, sondern aus dem ersten Ausführungsversuch.*
