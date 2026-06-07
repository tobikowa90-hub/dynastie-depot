# 🔧 UMSTRUKTURIERUNG-2027 — Depot-Restrukturierung (Plandokument)

**Erstellt:** 2026-06-05 | **Quelle:** Claude-Chat-Session 02.–04.06.2026 (`Umstrukturierung.md`)
**Status:** Phase A = Ist (real ausgeführt, Live-Sync ausstehend) · Phase B = Plan (Ausführung Q4 2026 / Jan 2027)

> **Provenienz-Warnung:** Die zugrundeliegende Chat-Session lief **blind ohne Zugriff auf 00_Core** und hat das System aus dem Gedächtnis rekonstruiert. Sie enthält mehrere Eigen-Rechenfehler und veraltete Basis-Parameter (950 € vs. ~1.031 €, 65/30/5 vs. 60/35/5, fehlendes COST). Dieses Dokument ist der **reconciled** Stand nach Abgleich gegen den echten Live-State am 2026-06-05.

---

## 1. Entschiedene Eckpunkte (User-Lock 2026-06-05)

| Entscheidung | Wert |
|---|---|
| Basis-Sparrate Dynastie | real bereits ~1.031 € SOLL (Live-File 950 € war veraltet) |
| Allokations-Split | **60/35/5** (ETF/Aktien/Gold) — vorher 65/30/5 |
| Satelliten-Methodik | **3-Tier Conviction-Weighting** ersetzt Equal-Weight |
| FLAG-Disziplin | **FLAG bleibt heilig** — geflaggte Titel = 0 € trotz Tier (Override-frei) |
| COST | **wird gedroppt** (Verkauf) |
| VEEV | **wird gedroppt** → Erlös in NOW |
| AVD-Core-ETF | **Invesco MSCI World** (IE00B60SX394, TER 0,05%, Swap) |
| Combined-View 60/35/5 | gilt auf Dynastie + AVD **zusammen, erst ab 2027** |
| AVD-Budget | **kein +Extra** — World-Sleeve (257 €) relociert in AVD-Steuermantel, Gesamtrate bleibt ~1.031 € |

---

## 2. Phase A — Ist-Zustand (real am Broker, 2026-06-05)

### ETF-Block (616 €)

| ETF | ISIN | Rate | Status |
|---|---|---|---|
| IWDA (iShares Core MSCI World) | IE00B4L5Y983 | 257 € | läuft (noch ING) |
| EIMI (iShares Core MSCI EM IMI) | IE00BKM4GZ66 | 123 € | läuft (noch ING) |
| AVGC (Avantis Global Small Cap Value) | IE0003R87OG3 | 103 € | läuft |
| JEDI (VanEck Space Innovators) | IE000YU9K6K2 | 82 € | 🟢 neu gestartet 04.06. |
| WQTM (WisdomTree Quantum Computing) | IE000W8WMSL2 | 51 € | läuft |
| EXUSA (Xtrackers MSCI World ex USA) | — | 0 € | 🔴 gestoppt 04.06. |

### Satelliten — 3-Tier, FLAG-heilig (SOLL 364 € / real-funded 210 €)

| Tier | SOLL-Rate | Titel | Real-Rate |
|---|---|---|---|
| **Tier 1** | 40 € | AMZN | **0 €** 🔴 CapEx/OCF-FLAG |
| | | MSFT | **0 €** 🔴 CapEx/OCF-FLAG |
| | | NOW | 40 € |
| | | AVGO | **0 €** 🔴 Insider-Selling-FLAG |
| **Tier 2** | 32 € | V | **16 €** 🟡 D2-Sockelbetrag (50%) |
| | | KYCCF (Keyence) | 32 € |
| | | ASML | 32 € |
| **Tier 3** | 18 € | RMS | 18 € |
| | | BRK.B | 18 € |
| | | TMO | 18 € |
| | | APH | **0 €** 🔴 Score-FLAG (<65) |
| | | SU | 18 € |
| | | ZETA | 18 € |

**Funded gesamt:** 40 + 80 + 90 = **210 €** · **SOLL:** 160 + 96 + 108 = **364 €** (Tier 2 funded = ASML 32 + KYCCF 32 + V 16 = 80 €, da V D2-moduliert)

- **Transitional:** VEEV + COST **roster-exited** (Sparpläne gestoppt, aus der 13er-Satelliten-Liste raus — alle Live-State-Files behandeln sie als exited). Die physische Verkaufs-Transaktion kann noch offen sein (COST LIMIT @863€, VEEV-Verkauf läuft) — siehe §4 Transaktionsplan.
- **Roster-Wechsel:** 12 → 13 aktive Satelliten. Neu: NOW, KYCCF, ZETA. Raus: VEEV, COST.

### Gold
EWG2 (EUWAX Gold II) — 51 €

### Bilanz — Rebalancing_Tool ist SSoT (war immer so)

- **Soll-Gewichtung (Grün-Zustand, 60/35/5):** Tier-Raten 40/32/18 + ETF 616 + Gold 51 = **~1.031 €/Monat** — Ziel-Gewichtung nach Beträgen innerhalb des Gesamtdepots.
- **`Rebalancing_Tool_v3.x.xlsx` = SSoT:** hält die Soll-Gewichtung; die Formellogik errechnet automatisch, wo Geld fehlt (untergewichtete Ist-Werte), und lenkt **freies Kapital** dorthin. Value-based, nicht starre Festbeträge.
- **FLAG-Titel** (AMZN/MSFT/AVGO/APH) werden aus der monatlichen Zuteilung ausgeschlossen (0 €); ihr Budget wird vom Tool **automatisch auf untergewichtete Positionen umgelenkt** — nicht idle gehalten. Der volle Monatsbeitrag wird deployed, nur die Verteilung verschiebt sich. (Das frühere „893 € real deployed" war ein falsches Festbetrags-Modell.)
- **Neue Positionen** (NOW, KYCCF, ZETA, JEDI, WQTM) mit Fehlbeträgen werden vom Tool bevorzugt aufgestockt, bis Ist = Soll. Einmal-Erlöse aus den 2026-Verkäufen (§4) beschleunigen das (KONTEXT §7 Steuer-Bremse: „nie durch Verkauf rebalancen — Sparplan umleiten").
- **Konsequenz für den Sync:** Die Tier-Raten sind Soll-Anker; das Rebalancing_Tool (A3) muss diese als neue Soll-Gewichtung übernehmen, die Verteilungs-/FLAG-Logik bleibt unverändert.

---

## 3. Phase B — Ziel-Struktur ab 2027

### Altersvorsorgedepot (AVD), neu, bei Scalable
- **ETF:** Invesco MSCI World (IE00B60SX394), 257 €/Monat (davon 150 € förderfähig, Rest ungefördert aber steuerbegünstigt)
- **Riester-Altvertrag** (~5.251 €+) → Übertrag als Invesco-Einmalkauf ins AVD (Jan 2027)
- World-Sleeve relociert komplett aus Dynastie → AVD (IWDA-Sparplan im Dynastie endet Ende 2026)

### Dynastie-ETF nach World-Relocation (Combined-View 60 %)
| ETF | Anteil (combined) | Quelle |
|---|---|---|
| Invesco World | 25 % | AVD |
| EIMI | 12 % | Dynastie |
| AVGC | 10 % | Dynastie |
| JEDI | 8 % | Dynastie |
| WQTM | 5 % | Dynastie |
| **ETF gesamt** | **60 %** | |

Satelliten 35 % · Gold 5 %.

### Broker-Konsolidierung
Alles → **Scalable**. EIMI per In-Kind-Übertrag ING→Scalable. ING danach leer → kündigen.

---

## 4. Transaktionsplan 2026 (alle steuerfrei via Freistellungsauftrag)

| Aktion | Erlös | G/V | Wohin | Timing |
|---|---|---|---|---|
| exUSA Sparplan stoppen | — | — | — | ✅ erledigt 04.06. |
| JEDI Sparplan starten @82 € | — | — | — | ✅ erledigt 04.06. |
| VEEV verkaufen | 399,88 € | **−31,12 €** | → NOW | läuft |
| COST verkaufen | 387,74 € (LIMIT @863 €) | **+1,74 €** | → Rebalancing-Tool (freies Kapital)¹ | LIMIT offen @863 € (Kurs 841 €) |
| exUSA verkaufen | 1.967,41 € | **+77,41 €** | 70 % JEDI / 30 % WQTM | noch 2026 |
| EIMI Sparplan ING stoppen + Übertrag→Scalable | 1.387,26 € (in natura) | 0 € (keine Realisierung; +204,26 € latent) | Scalable | Herbst 2026 |
| IWDA Sparplan stoppen | — | — | — | Ende 2026 |
| IWDA verkaufen | 3.994,52 € | **+369,36 €** | Teil WQTM, Rest Satelliten | Ende 2026 |
| AVD eröffnen + Invesco Sparplan @257 € | — | — | Scalable | Jan 2027 |
| Riester-Übertrag → AVD | ~5.251,70 €+ | — | Invesco | Jan 2027 |
| ING Depot kündigen | — | — | — | nach EIMI-Übertrag |

**Netto-Gewinn (VEEV+exUSA+IWDA+COST):** −31,12 +77,41 +369,36 +1,74 = **+417,39 € < 1.000 € Freibetrag → 0 € Steuer.** Restpuffer 2026 ~582,61 € (1.000 − 417,39). Split-Realisierung nicht nötig (COST-Gewinn marginal; bei Verkauf zum aktuellen Kurs 841 € sogar −8,15 € Verlust).

¹ **COST-Erlös-Ziel:** ✅ User-Lock 06.06. — keine explizite Zuweisung; Erlös (~388 €, marginal) läuft universell über das Rebalancing-Tool auf untergewichtete Tier-Positionen (konsistent mit O1).

---

## 5. Offene / vertagte Entscheidungen

| # | Item | Status |
|---|---|---|
| O1 | **Umverteilungs-/Rebalancing-Mechanik** — ✅ GEKLÄRT 05.06.: `Rebalancing_Tool` ist SSoT (war immer so). Value-based über Beträge im Gesamtdepot; Formellogik errechnet Unterdeckung; freies Kapital (inkl. FLAG-Budget) wird automatisch auf untergewichtete Positionen umgelenkt. Voller Monatsbeitrag deployed, nur Verteilung verschiebt sich. Tier-Raten = Soll-Anker. | ✅ erledigt |
| O2 | **COST-Verkauf** — ✅ GEKLÄRT 06.06.: 0,449289 Anteile, Cost-Basis 386,00 € (859,21 €/Anteil), Kurswert 377,85 € (Kurs 841 €). Verkaufs-LIMIT @863 € → Erlös 387,74 €, G/V **+1,74 €**. Marginal, Restpuffer ~582,61 €, kein Split. Erlös-Ziel ✅ User-Lock 06.06. (Rebalancing universell, §4 Fn.¹). Rest-offen: nur LIMIT-Ausführung @863 € (marktabhängig). | ✅ erledigt |
| O3 | **NOW / KYCCF / ZETA Scoring** — aktuell Owner-Conviction-Adds ohne DEFCON-Score (wie AMZN-Präzedenz §1). NOW → !Analysiere; KYCCF → non-us-fundamentals; ZETA = QuickScreener-Rot, bewusste Spekulation | offen |
| O4 | **AVGO Q2-Earnings 03.06.** — Tag-+1-Vollanalyse überfällig (§19.1). FLAG-Resolve-Gate + neuer Score; bestimmt Tier-1-Förderung | 🔴 überfällig |
| O5 | **config.yaml / xlsx-Tools Tier-Schema** — bisher Equal-Weight-Nenner; Tier-Struktur erfordert Schema-Anpassung | offen (Code) |

---

## 6. Governance-Overrides (zu dokumentieren in CORE-MEMORY §2/§13)

1. **Equal-Weight → Conviction-Tier** — überstimmt die als „dauerhaft bindend" geltende Autopilot-Entscheidung (KONTEXT §5). Bewusstes Owner-Mandat.
2. **DEFCON-Score moduliert die Rate WEITER** (Korrektur 06.06. — die ursprüngliche Chat-Annahme „moduliert nicht mehr" war FALSCH). Effektive Rate = `Tier-Basis × DEFCON-Modulation × FLAG`: D3/D4 → volle Tier-Rate, D2 → halbe Tier-Rate (z.B. V = 50% von 32 = **16 €**), D1/FLAG → 0 €. Die EINZIGE Methodik-Änderung ggü. alt ist Equal-Weight→Tier-Basis; die DEFCON-Modulation bleibt unverändert erhalten.
3. **FLAG bleibt heilig** — geflaggte Titel weiter 0 € (beibehalten, konsistent mit AMZN-Präzedenz 18.05.).
4. **Satelliten ohne Score** (NOW/KYCCF/ZETA) — Owner-Override analog AMZN; KONTEXT §12 Watchlist-Eintritts-Disziplin per §1 „Mein Portfolio, meine Regeln" gewaivt; Score-Wahrheit faktentreu dokumentieren.
5. **exUSA raus, JEDI + WQTM** als zwei bewusste Themen-Wetten (zusammen 13 % ETF-Block).
6. **COST raus**, **VEEV raus** (→ NOW).
7. **Split 65/30/5 → 60/35/5.**
8. **AVD als 3. struktureller Baustein** (KONTEXT §2 „geplant ab 2027" → konkret).

---

*🦅 UMSTRUKTURIERUNG-2027.md v0.2 | Dynastie-Depot | erstellt 2026-06-05 reconciled; v0.2 (06.06.) COST-Datenlücke O2 geschlossen → §4 + Netto-Steuerrechnung komplett. Phase A → Live-Sync ausstehend (gated: O4 AVGO Tag-+1), Phase B → PIPELINE-Gate*
