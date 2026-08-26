# Depot-Reconciliation — Ist vs. Soll

**Stichtag:** 2026-08-26 · **Status:** Arbeitsdokument, **keine Entscheidung getroffen**, keine SSoT verändert.

## Quellen

| Seite | Quelle | Stand |
|---|---|---|
| **IST** | Scalable Capital CLI `sc` v0.6.0 (`broker holdings` / `savings-plans` / `cash-breakdown` / `transactions`) | 2026-08-26, Valuation 12:00 UTC |
| **SOLL** | `01_Skills/dynastie-depot/config.yaml` (etfs, satelliten, brokers, allokation) | 2026-06-13 |
| **SOLL** | `00_Core/PORTFOLIO.md` v1.5 (Tier/Score/DEFCON/FLAG/Rate) | 2026-06-13 |
| **SOLL** | `03_Tools/Rebalancing_Tool_v4.0.xlsx` (Raten-SSoT) | Depotwerte 2026-08-18, **Roster Juni** |

**Wichtig zur Soll-Seite:** Das Rebalancing-Tool ist inkonsistent in sich — die Depotwert-Spalte wurde am 18.08. gepflegt, die Positions-Liste nicht. Es führt KYCCF (561 €) und JEDI (175 €), kennt aber Adobe, Alphabet, Meta, Veeva und Costco nicht.

---

## A · Positionen

Ist-Anteil bezogen auf 29.987,70 € Wertpapiere (+ 143,23 € Cash = 30.130,93 € gesamt).

| # | ISIN | Titel | Ist € | Ist % | Soll-Rolle (config/PORTFOLIO) | Score/DEFCON | FLAG | Delta |
|---|---|---|---|---|---|---|---|---|
| 1 | IE00B4L5Y983 | iShares Core MSCI World (IWDA) | 7.394,77 | 24,7% | ETF-Core, Broker **ING** | — | — | Broker gewechselt → Scalable |
| 2 | US81762P1021 | ServiceNow (NOW) | 4.335,38 | **14,5%** | Satellit T1 | **— (O3 offen)** | ✅ | **Single-Stock-Cap 10% verletzt**; Score fehlt |
| 3 | IE00BKM4GZ66 | iShares Core MSCI EM IMI (EIMI) | 3.653,81 | 12,2% | ETF-Core, Broker **ING** | — | — | Broker gewechselt → Scalable |
| 4 | IE0006WW1TQ4 | Xtrackers MSCI World ex USA (EXUS) | 3.053,99 | 10,2% | ETF-Core, Broker **ING** | — | — | Broker gewechselt → Scalable |
| 5 | IE0003R87OG3 | Avantis Global Small Cap Value (AVGC) | 2.670,12 | 8,9% | ETF-Core, Scalable | — | — | ✅ deckungsgleich |
| 6 | US00724F1012 | **Adobe (ADBE)** | 900,69 | 3,0% | **nicht im Soll** | **kein Score** | — | **Neu, ungescort** |
| 7 | DE000EWG2LD7 | EUWAX Gold II (EWG2) | 810,52 | 2,7% | Gold-Block, Ziel 5% | — | — | Untergewicht (2,7% vs 5%) |
| 8 | US5949181045 | Microsoft (MSFT) | 704,35 | 2,3% | Satellit T1 | 50 / 🟠 D2 | 🔴 CapEx/OCF | Position ok, **Rate verletzt FLAG** |
| 9 | US98956A1051 | Zeta Global (ZETA) | 658,00 | 2,2% | Satellit T3 | **— (O3 offen)** | ✅ | Sparplan **entfallen** (Soll 18 €) |
| 10 | US0231351067 | Amazon (AMZN) | 590,18 | 2,0% | Satellit T1 | 42 / 🔴 D1 | 🔴 CapEx/OCF | Position ok, **Rate verletzt FLAG** |
| 11 | US9224751084 | **Veeva (VEEV)** | 569,01 | 1,9% | **in Phase A gedroppt** | kein aktueller Score | — | **Wieder da**, 3× SELL cancelled |
| 12 | US92826C8394 | Visa (V) | 563,37 | 1,9% | Satellit T2 | 64 / 🟠 D2 | ✅ | ✅ im Roster |
| 13 | NL0010273215 | ASML | 559,71 | 1,9% | Satellit T2 | 68 / 🟡 D3 | ✅ | SELL 24.08. cancelled |
| 14 | US8835561023 | Thermo Fisher (TMO) | 522,29 | 1,7% | Satellit T3 | 67 / 🟡 D3 | ✅ | ✅ im Roster |
| 15 | FR0000121972 | Schneider Electric (SU) | 461,98 | 1,5% | Satellit T3 | 69 / 🟡 D3 | ✅ | ✅ im Roster |
| 16 | US0846707026 | Berkshire Hathaway B (BRK.B) | 458,99 | 1,5% | Satellit T3 | 71 / 🟡 D3 | ✅ | ✅ im Roster |
| 17 | US11135F1012 | Broadcom (AVGO) | 434,02 | 1,4% | Satellit T1 | 56 / 🟠 D2 | 🔴 Insider-Selling | Position ok, **Rate verletzt FLAG**; SELL 24.08. cancelled |
| 18 | FR0000052292 | Hermès (RMS) | 394,52 | 1,3% | Satellit T3 | 68 / 🟡 D3 | ✅ | ✅ im Roster |
| 19 | US0320951017 | Amphenol (APH) | 376,70 | 1,3% | Satellit T3 | 61 / 🟠 D2 | 🔴 Score < 65 | Position ok, **Rate verletzt FLAG** |
| 20 | US22160K1051 | **Costco (COST)** | 369,94 | 1,2% | **in Phase A gedroppt** | kein aktueller Score | — | **Wieder da**, SELL seit 18.08. **PENDING** |
| 21 | IE000W8WMSL2 | WisdomTree Quantum (WQTM) | 346,29 | 1,2% | ETF-Themenwette, Scalable | — | — | ✅ deckungsgleich |
| 22 | IE000YU9K6K2 | VanEck Space Innovators (JEDI) | 159,07 | 0,5% | ETF-Themenwette, Soll-Rate 72 € | — | — | Sparplan **entfallen**, SELL seit 18.08. **PENDING** |
| 23 | US02079K3059 | **Alphabet A (GOOGL)** | 0,00 | 0,0% | **nicht im Soll** | **kein Score** | — | **Sparplan aktiv, Erstkauf 01.09.** |
| 24 | US30303M1027 | **Meta Platforms A (META)** | 0,00 | 0,0% | **nicht im Soll** | **kein Score** | — | **Sparplan aktiv, Erstkauf 01.09.** |
| — | — | **Keyence (KYCCF)** | **nicht mehr im Depot** | — | Satellit T2, Soll-Rate 32 € | **67 / 🟡 D3** | ✅ | **Faktisch ausgeschieden.** Die KYCCF-Zeile im Rebalancing-Tool (561 €) trägt in Wahrheit den händisch gepflegten Veeva-Wert — Provisorium des Owners, um das Tool nicht ohne Abstimmung umzubauen. Der O3-Score 67 vom 13.06. hat damit kein Objekt mehr. |

**Block-Allokation Ist:** ETF 17.278 € (57,6%) · Gold 811 € (2,7%) · Aktien 11.899 € (39,7%) — Ziel laut config: 60 / 5 / 35.

---

## B · Sparraten

> ⚠️ **Diese Tabelle zeigt den Stand VOR der Umstellung vom 26.08.** Der aktuelle Stand steht in Abschnitt F.

| ISIN | Titel | Ist €/Mt | Soll €/Mt | Soll-Herleitung | Delta |
|---|---|---|---|---|---|
| IE00B4L5Y983 | IWDA | 208 | 206 | config etfs | +2 |
| IE00BKM4GZ66 | EIMI | 120 | 123 | config etfs | −3 |
| IE0003R87OG3 | AVGC | 85 | 82 | config etfs | +3 |
| IE0006WW1TQ4 | EXUS | 80 | 82 | config etfs | −2 |
| IE000W8WMSL2 | WQTM | 70 | 51 | config etfs | **+19** |
| DE000EWG2LD7 | Gold EWG2 | 52 | 51 | config etfs | +1 |
| IE000YU9K6K2 | JEDI | **0** | 72 | config etfs | **−72 (Sparplan gelöscht)** |
| US02079K3059 | Alphabet | **40** | — | kein Soll | **+40 ungescort** |
| US0231351067 | Amazon | **40** | **0** | T1, 🔴 FLAG | **+40 FLAG-Verletzung** |
| US30303M1027 | Meta | **40** | — | kein Soll | **+40 ungescort** |
| US5949181045 | Microsoft | **40** | **0** | T1, 🔴 FLAG | **+40 FLAG-Verletzung** |
| NL0010273215 | ASML | 35 | 32 | T2 × D3 | +3 |
| US00724F1012 | Adobe | **35** | — | kein Soll | **+35 ungescort** |
| US11135F1012 | Broadcom | **35** | **0** | T1, 🔴 FLAG | **+35 FLAG-Verletzung** |
| US81762P1021 | ServiceNow | 35 | 40 | T1 × Platzhalter-D3 | −5 |
| US92826C8394 | Visa | 35 | 16 | T2 × D2-Sockel 50% | **+19** |
| FR0000052292 | Hermès | 20 | 18 | T3 × D3 | +2 |
| FR0000121972 | Schneider | 20 | 18 | T3 × D3 | +2 |
| US0320951017 | Amphenol | **20** | **0** | T3, 🔴 FLAG Score<65 | **+20 FLAG-Verletzung** |
| US0846707026 | Berkshire B (BRK.B) | 20 | 18 | T3 × D3 | +2 |
| US8835561023 | Thermo Fisher | 20 | 18 | T3 × D3 | +2 |
| US9224751084 | **Veeva** | **20** | — | Phase-A-Dropout | **+20 ungescort** |
| US98956A1051 | Zeta | **0** | 18 | T3 × Platzhalter-D3 | **−18 (Sparplan gelöscht)** |
| — | **Keyence** | **0** | 32 | T2 × D3 | **−32 (kein Sparplan)** |
| | **Σ** | **1.070** | **1.031** | | **+39** |

**Block-Split Ist:** ETF 563 € (52,6%) · Gold 52 € (4,9%) · Aktien 455 € (42,5%) — Ziel 60 / 5 / 35.
**Ausführung:** alle 21 Pläne am **1. des Monats**, nächste am **2026-09-01**. Cash 143,23 €, Rest per Referenzkonto-Fallback.

---

## C · Konflikte, sortiert nach Tragweite

1. **FLAG-Regel gebrochen — 135 €/Mt.** MSFT 40 · AMZN 40 · AVGO 35 · APH 20 laufen, obwohl alle vier 🔴 tragen und `flag_wirkung` in config.yaml lautet: *„Sparrate komplett gestoppt (0 €) — FLAG überschreibt DEFCON-Level (Score-unabhängig)."* Bereits ausgeführt am 03.08.: MSFT 200 €, AMZN 200 €.
2. **135 €/Mt in ungescorte Titel.** Adobe 35 · Alphabet 40 · Meta 40 · Veeva 20. Alphabet und Meta kaufen am **01.09.** zum ersten Mal — bis dahin sind es reine Sparplan-Einträge ohne Position.
3. **Single-Stock-Cap gerissen.** NOW 14,5% gegen 10% Cap laut `Parameter & Regeln`. Gleichzeitig trägt NOW keinen echten Score (O3-Platzhalter seit 08.06.).
4. **3-Tier-Modell existiert nicht mehr.** Ist-Staffel 40/35/20, Soll 40/32/18 × DEFCON-Modulation × FLAG. Keine der DEFCON-Modulationen ist im Depot wirksam.
5. **Roster-Drift beidseitig.** Rein ohne Beschluss: Adobe, Alphabet, Meta. Zurück nach Drop: Veeva, Costco. Raus ohne Vermerk: Keyence (trotz O3-Vollanalyse 13.06.), JEDI-Sparplan.
6. **Broker-Modell überholt.** config.yaml teilt 616 € ING / 364 € Scalable / 51 € Gold. Faktisch liegt alles bei Scalable — ING-Bestände kamen am 17.08. per Depotübertrag (8.445 €).

---

## D · Offene Fragen

1. ~~**Keyence:** verkauft oder übertragen?~~ **GEKLÄRT 26.08.:** nicht mehr im Depot. Die KYCCF-Zeile im Rebalancing-Tool führt den händisch gepflegten Veeva-Wert — Owner-Provisorium, kein Datenfehler. Offen bleibt nur, ob der O3-Score 67 archiviert oder auf einen Wiedereinstieg vorgehalten wird.
2. ~~**ING:** noch Restbestände?~~ **GEKLÄRT 26.08.:** nein. Der Übertrag am 17.08. war vollständig, Scalable hält das gesamte Depot. Die 30.131 € sind das Gesamtvermögen, alle Prozentangaben in diesem Dokument sind damit gültig.
3. **Costco + JEDI:** die SELL-Orders stehen seit 18.08. auf `PENDING` — gewollt so, oder hängen sie?
4. **Broadcom + ASML SELL am 24.08. `CANCELLED`:** war das ein Verkaufsversuch, der scheitern sollte, oder ist er nur nicht durchgegangen?
5. **Veeva:** drei SELL-Orders (18.06., 28.06., 18.08.) alle cancelled, gleichzeitig 20 €/Mt Sparplan aktiv — Position soll weg oder bleiben?
6. **Zielallokation:** gilt weiter 60/35/5, oder ist die Ist-Verteilung 53/42/5 (Raten) bzw. 58/40/3 (Bestand) die neue Absicht?

---

## E · Stand der Markdown-/Config-Ebene

`PORTFOLIO.md`, `config.yaml`, `Faktortabelle.md` und die drei xlsx-Tools sind **unverändert** und damit seit dem 26.08. bewusst veraltet. Kein §18-Sync ausgelöst. Die Nachführung gehört in die Architektur-Phase (Zwei-Schichten-Modell), nicht in punktuelle Edits.

---

## F · Strategie-Kontext und Umsetzung 26.08.2026

### F.1 Owner-Strategie (Interview 26.08.)

- **Broker-Konsolidierung:** ING → Scalable war eine Vereinfachungsentscheidung, getroffen *vor* Kenntnis von Agentic Investing. Das ING-Depot ist **nicht aufgelöst**, bleibt reaktivierbar für spätere Entnahme- oder Besparungsstrategien.
- **Core-4:** Alphabet, Microsoft, Amazon, Meta sollen langfristig die größten Aktienpositionen werden. Sie sind von der strengen FLAG-Politik ausgenommen — Begründung des Owners: Weltmarkt-Dominatoren wegen roter Quartalszahlen nicht zu besparen, wäre eine Farce.
- **Software-These:** Nach dem KI-/Halbleiter-Boom wird eine Software-Renaissance erwartet. Daher NOW bewusst übergewichtet, Adobe neu aufgenommen, Veeva behalten (auch wegen der starken Erholung). ASML und Broadcom stehen zum Jahreswechsel zur Disposition.
- **Zweckkapital 9.000 €:** Geschenk des Schwiegervaters in spe, gedacht für die Hochzeit 2027, ein Jahr im Voraus zum Anlegen gegeben. Aufteilung 13.08.: 7.000 € ETF-Kombi + 2.000 € ServiceNow. Zielband 10–11k bis zur Entnahme; Überschuss darf im Depot bleiben.
- **Zielallokation:** 60/35/5 wird beibehalten und soll wieder erreicht werden. Gold als 5%-Puffer und ein festes US-Cap bleiben gewollt, ebenso breite Sektor- und Weltmarkt-Diversifikation und DEFCON-geprüfte Non-US-Positionen.
- **JEDI:** reine Sektorwette aus dem SpaceX-IPO-Hype. Owner-Erkenntnis: Themenwetten lohnen nur bespart, nicht als Einmal-Cash. Tendenz halten, Entscheidung offen. **WQTM** dagegen mit Überzeugung weiter besparen. **Costco** soll raus, aber als Take-Profit.

### F.2 Analyse-Ergebnisse

| Befund | Ergebnis |
|---|---|
| **FIFO-Steuerrisiko** | **Widerlegt.** Buchgewinne klein (IWDA +5,9% · EIMI +4,8% · EXUS +6,4%), Gesamtdepot +2.144 € = +7,7%. Steuer bei 10.000-€-Entnahme ≈ 98 € und damit unter dem Sparerpauschbetrag. ETF-Besparung läuft erst seit 17.12.2025 — es konnte sich nichts aufbauen. Eine Depot-Trennung aus Steuergründen ist unnötig. |
| **US-Quote** | Bestand 59,4%, Sparrate 58,9% → **stabil**, kein Cap-Problem (Hard-Cap 63%). Bei Core-4 auf je 100 €/Mt würde die Grenze nach 24 Monaten erreicht. |
| **Sektor-Konzentration** | NOW + Adobe + Veeva = **48,9% des Aktienteils**, mit Microsoft 54,9%. Alle drei sind Enterprise-SaaS und diversifizieren einander kaum. Offene Analysefrage: Das Hauptrisiko dieser Titel *ist* KI (Agenten ersetzen Seats) — die These „nach KI kommt Software" könnte sich gegen die Positionierung richten. |
| **Core-4-Aufbau** | Damit jede Core-4-Position ServiceNow überholt: **48 Monate** bei je 100 €/Mt und gestopptem NOW-Sparplan. Läuft NOW weiter, passiert es nie (Start 4.357 € gegen 1.306 € für alle vier zusammen). |
| **Allokations-Lesart** | Zählt man die Core-4 zum Core-Block statt zu den Satelliten, liegt das Depot bei **61,9 / 35,4 / 2,7** gegen Ziel 60/35/5 — nur Gold fehlt. Sachlich begründet: Die vier *sind* die größten MSCI-World-Werte, ein Core-ETF hält sie ohnehin; sie werden hier nur übergewichtet. Grenze: Bei Core je 100 €/Mt wächst der Core-Block auf 70% (60 Mt) — der Ausbau muss innerhalb der 60% aus sinkenden ETF-Raten finanziert werden. |

### F.3 Ausgeführte Sparplan-Änderungen (Owner-Freigabe im Klartext)

| Titel | vorher | nachher | Grund |
|---|---|---|---|
| Broadcom | 35 | **0** (entfernt) | FLAG Insider-Selling + Verkaufsabsicht; Satellit, keine Core-Ausnahme |
| ServiceNow | 35 | **0** (entfernt) | Position bleibt größte Aktie; Mittel dienen dem Core-Aufbau |
| EUWAX Gold II | 52 | **80** | schließt die 694-€-Lücke auf die gewollten 5% |
| Alphabet · Microsoft · Amazon · Meta | je 40 | **je 50** | Core-Aufbau, budgetneutral gegenfinanziert |

**Ergebnis: 19 Sparpläne, 1.068,00 €/Mt** (vorher 21 / 1.070,00 €), alle MONTHLY zum 1., nächste Ausführung 2026-09-01.
Ex-ante-Kosten je Plan: Einstieg 0, laufend 0, Ausstieg 0,99 € (reine Servicekosten).
Verifiziert Titel für Titel gegen das freigegebene Soll — 19/19 OK, Summe exakt, Broadcom und ServiceNow bestätigt entfernt, kein unerwarteter Plan, Ausführungstag einheitlich 1.

**Nicht angefasst:** Amphenol (20 €, Owner-Entscheidung trotz FLAG), ASML (35 €, Score 68/D3 — bester Satellit nach BRK.B und Schneider), alle übrigen Pläne, sämtliche Positionen, die offenen Limit-Orders.

### F.4 Offen

1. **Regelwerk-Nachzug:** `config.yaml` und `PORTFOLIO.md` beschreiben eine FLAG-Wirkung und ein 3-Tier-Modell, denen das Depot bewusst nicht mehr folgt. Vorschlag: FLAG zweiteilen — bei Core-Titeln Informations- und Analysepflicht ohne Ratenwirkung, bei Satelliten weiterhin hart 0 €.
2. **Scoring-Backlog:** NOW · ZETA · Adobe · Alphabet · Meta · Veeva ohne gültigen DEFCON-Score.
3. **Earnings-Nachzug:** Juli-Cluster unbearbeitet (ASML 15.07. · TMO 22.07. · V 28.07. · MSFT/APH/RMS 29.07. · SU/AMZN 30.07. · BRK.B 01.08.), AVGO Q3 am **03.09.**
4. **Architektur:** Zwei-Schichten-Modell (Live aus API, Urteil in git) — Spec steht aus.
5. **Zweckkapital:** Trennung steuerlich unnötig; offen bleibt allein, ob die 2.000 € in ServiceNow für Geld mit Termin in zwölf Monaten das gewünschte Risiko sind.
