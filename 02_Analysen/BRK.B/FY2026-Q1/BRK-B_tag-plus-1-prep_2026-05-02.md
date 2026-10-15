# Berkshire Hathaway (BRK.B) — Tag-+1 Vorbereitungs-Brief Q1 FY26

**Erstellt:** 02.05.2026 (Sa) Tag-0 spätnachmittag, NACH `chore(brk-b)` Commit `77fd6d3` (Tag-0 PR-Recap + 10-Q Quick-Read in CORE-MEMORY §12.4)
**Tag-+1 Vollanalyse-Slot:** 03.05. (So) ODER 04.05. (Mo) morgens — §19.1 Wait-Discipline
**Aktueller Score:** 75 · DEFCON 🟡 3 · Sparrate 38,00€ · ✅ Insurance Exception (Klasse B, Float-Modell)
**Datenquelle:** `02_Analysen/Earnings Reports/Berkshire Hataway/1stqtr26.pdf` (10-Q, committed `fff3184`) + Annual Meeting Q&A Live-Stream Sa-Nachmittag
**Zweck:** Tag-+1-Vollanalyse-Beschleunigung · Codex-HIGH-Antizipation · Annual-Meeting-Q&A-Watch-Items strukturiert

> **⚠️ Pre-Append-Audit (Provenance-Gate, dynastie-depot v3.7.6):**
> Vor Schritt 7 Pflicht-Check: (a) Sub-Score `!= 0` → Rohwert in `metriken_roh` nicht null, ODER `quellen.<block>` enthält `*_carryover`-Suffix; (b) Insurance-Exception-spezifische Sub-Scores (Float, Investment-Income-Yield, UW-Profitabilität) brauchen explizite Insurance-Anker im `notizen`-Feld, sonst FAIL bei Codex-Review (V-Q2-Lehre).

---

## 1. NEUE Insurance-Segment-Dekomposition (NICHT in §12.4)

§12.4 hat Insurance-UW total +28,5% ($1,72B → $2,21B). **Segmentaufschlüsselung 10-Q Note 24** zeigt asymmetrisches Bild:

| Insurance-Sub | Q1-26 UW-Earnings | Q1-25 UW-Earnings | YoY |
|---------------|-------------------|-------------------|-----|
| **GEICO** | **$1.416M** | $2.173M | **−34,8%** |
| **BH Primary** | $476M | **−$144M** | Recovery from Loss |
| **BHRG (Reinsurance)** | $373M | **−$307M** | Recovery from Loss |
| **Total** | **$2.265M** | **$1.722M** | **+31,5%** (Mio-Basis; §12.4 berichtet gerundet +28,5% auf Mrd-Basis: ($2,21B−$1,72B)/$1,72B; konsistent, unterschiedliche Rundungs-Granularität) |

**Critical Insight:**
- **GEICO −34,8% YoY** (DECELERATING, nicht Beat-Treiber wie Headline suggeriert) — Loss-Ratio 73,9% Q1-26 (8.277/11.186) vs 69,0% Q1-25 (7.424/10.752) = +4,9pp Loss-Severity ODER -Frequency-Up. Auto-Insurance-Cycle-Reversion-Frühwarnung.
- **BHRG + BH Primary +$1,3B Recovery** allein aus Q1-25-UW-Loss-Base — Q1-25 war Cat-Light + Adverse-Development Quartal. **Reine Base-Effekt-Mechanik, nicht Underlying-Improvement.**
- **Cat-Loss-Light Q1-26 bestätigt** durch 10-Q Sektion „no significant catastrophe events (>$150M per event) in the first quarter 2026, including no material losses on California wildfires."

→ **Score-Reasoning Tag-+1:** Insurance-UW-Sub-Score darf NICHT mechanisch +1/+2 vergeben werden. Headline +28,5% ist asymmetrisch (Reinsurance Recovery + GEICO Drift). Vorschlag: Sub-Score unverändert ODER +1 mit expliziter `notizen`-Klausel „GEICO-Decel-Watch + BHRG-Base-Effekt".

→ **Codex-HIGH-Antizipation #1:** Reviewer wird GEICO-Loss-Ratio-Verschlechterung challengen, falls Sub-Score-Move begründet mit „Insurance-UW +28,5%". Pre-empt mit Segment-Dekomposition im Score-Record.

---

## 2. NEUE Apple/Consumer-Products Trim-Cost-Basis-Signal (NICHT in §12.4)

§12.4 hat Consumer Products FV-Move −$3,9B aber kein Cost-Basis-Detail. **10-Q Note 4 zeigt:**

| Consumer Products | Cost Basis | Net Unrealized | FV |
|-------------------|------------|----------------|-----|
| **31.03.2026** | $8.847M | $82.191M | $91.038M |
| **31.12.2025** | $11.899M | $83.055M | $94.954M |
| **Δ** | **−$3.052M** | −$864M | −$3.916M |

**Cost-Basis −$3,05B Q1** = **expliziter Trim-Beleg** (nicht reine Wert-Decline) auf Sub-Cluster-Ebene Consumer-Products (Cost Basis $11,899B → $8,847B = **−25,6% Cost-Basis-Reduktion** des Sub-Clusters). Tag-+1 Verfeinerung Pflicht: Decomposition Apple- vs Non-Apple-Anteil im Consumer-Products-Sub (10-Q Note 4 nennt Top-5-Composition aber keine per-Holding-Cost-Basis-Aufschlüsselung). FV-%-Bezug zu Apple irreführend ohne per-Holding-Cost-Basis-Kenntnis (z.B. Apple FV ~$80B vs Cost-Basis ~$5-10B — Cost-Basis-Trim ist rechnerisch zwischen $0,6B und $3,05B Apple-Anteil je nach Allocation-Annahme).
→ **Apple-Trim-Welle Q1-26 STARK INDIZIERT** (PR-Detail allein ließ es offen, FV-Drop allein wäre Markt; Sub-Cluster-Cost-Basis-Move kann nur durch Trim ausgelöst sein, nicht durch Markt). Tag-+1: Form-13F Q1-26 (Filing ~mid-Mai) liefert per-Holding-Share-Count-Move definitiv; bis dahin Trim-Magnitude-Annahme im notizen mit „Sub-Cluster-Inferenz, nicht per-Holding-bestätigt"-Caveat.

**Banks/Insurance/Finance Trim:**

| | Cost Basis | Net Unrealized | FV |
|---|---|---|---|
| 31.03.2026 | $14.685M | $69.891M | $84.576M |
| 31.12.2025 | $15.454M | $88.675M | $104.129M |
| **Δ** | **−$769M** | −$18.784M | −$19.553M |

→ Bank-Sub Cost-Basis-Trim nur −$769M — **Hauptteil der −$19,6B FV-Decline ist Markt-Wert-Drop, nicht Trim**. BoA/Citi/Allies Q1 brutal (Bank-Sektor-Drawdown-Quartal). Trim-Komponente moderat ~$0,8B.

→ **Score-Reasoning Tag-+1:** Apple-Trim-Welle als Konzentrations-Reduktions-Signal positiv (Top-5 65→61% confirmed); Bank-Position bleibt stabil (kein materieller Trim trotz BoA-Schwäche) = Conviction-Hold-Signal. **Asymmetrische Lesart der Top-5-Roll** ist Tag-+1-Verfeinerung.

---

## 3. NEUE Equity-Method KHC vs Occidental Mark-Up-Asymmetrie

| | Carrying | Fair Value | Excess C-FV | Status |
|---|---|---|---|---|
| **Kraft Heinz** | $8.689M | $7.324M | **−$1.365M (15,7%)** | KEINE OTTI Q1 trotz FV<Carrying; explicit „current expectations and..." Caveat-Sprache |
| **Occidental** | $10.808M | $17.221M | **+$6.413M Mark-Up** | Recovery von Q4-25 OTTI |
| Berkadia | $454M | (n/a privat) | — | flat |
| **Total** | $19.951M | — | — | — |

**Critical:**
- **KHC FV<Carrying 15,7%** + Q4-25 OTTI bereits genommen → **Q2-26 OTTI-Risk material**, falls KHC-Aktie nicht recovered (QTD seit 31.03.: KHC ~$25-26 vs Carrying-impliziert ~$30-31). **Annual-Meeting-Q&A-Watch:** Buffett/Abel-Statement zu KHC-Position-Outlook ist hochwahrscheinlich = Codex-HIGH-Antizipation #2.
- **OXY +$6,4B Mark-Up** = unrealized winner, OxyChem-Acquisition-Konsistenz mit Equity-Position validiert (26,9% Common + Preferred + Warrants).

→ **Score-Reasoning Tag-+1:** Equity-Method-Block ist Bewertungs-neutral (kein direkter Score-Hebel), ABER KHC-Q2-OTTI-Risk gehört in `notizen`-Feld als Forward-Watch. **PIPELINE-Item neu** (Tag-+1 Schritt 6): „BRK_KHC_OTTI_Watch_Q2_FY26".

---

## 4. NEUE BNSF + BHE Margin-Operating-Leverage

§12.4 hatte BNSF +13,4% earnings-side ohne Topline-Kontext.

| | Q1-26 Rev | Q1-25 Rev | YoY | Q1-26 PreTax | Q1-25 PreTax | YoY |
|---|---|---|---|---|---|---|
| **BNSF** | $5.994M | $5.720M | **+4,8%** | $1.820M | $1.603M | **+13,5%** |
| **BHE** | $6.661M | $6.356M | +4,8% | (compute below) | | |

**BNSF Operating-Leverage** Faktor 2,8× (13,5% / 4,8%) — Compensation -0,9% YoY ($1.374M vs $1.387M), Fuel +flat, D&A −0,3%, Other +4,8%. **Productivity-Story bestätigt**, nicht reine Volume.

**BHE PreTax (rechnerisch aus 10-Q):** Costs ~$5.961M (1.670+1.298+1.080+879+700+334 ≈), → PreTax ~$700M vs $646M = **+8,4%**. Konsistenz mit §12.4-Headline +1,5% MUSS Tag-+1 reconciled werden — §12.4 sagte $1,11B vs $1,09B (+1,5%) auf earnings-after-tax-Ebene; PreTax-Ebene zeigt +8,4%. Discrepancy = Tax-Rate-Move. **Wildfire-Liability-Discount-Effekt Q1?** PacifiCorp Wildfire-unpaid Liabilities $577M (vs $1,2B YE25) = Reduktion Q1 −$623M (Settlement-Tranche $2,3B kumulativ paid). Tax-Treatment dieser Settlements treibt evtl. ETR-Move.

→ **Score-Reasoning Tag-+1:** BNSF Operating-Leverage = Sub-Score-positiv (Productivity-Story); BHE earnings-after-tax-flat trotz PreTax-Beat = Tax-Item-Watch + Wildfire-Settlement-Trajektorie-Verfeinerung gegenüber §12.4-Lesart.

---

## 5. NEUE Cashflow-Statement Detail (Equity-Sale + Treasury-Stock Diskrepanz)

10-Q Z.460-477 zeigt:
- **Purchases of equity securities Q1-26: $24.087M** (vs $4.677M Q1-25 = **5×**)
- **Sales of equity securities Q1-26: −$15.939M** (Net-Buy-Zeile -); reconciled-out: **Net-Sale-cash-flow $8.148M** (matches §12.4-Net-Sale)
- **Acquisitions of treasury stock $4.568B (= $4.568M in 10-Q-Raw, da Cashflow-Statement in Millionen)** — diese Zahl widerspricht §12.4-Buyback $235M deutlich (Faktor ~19,4×).

**Discrepancy-Investigation Tag-+1 Pflicht:** $4,568B (10-Q `Acquisitions of treasury stock`) vs $235M Press-Release-Buyback = Faktor ~19× Diff. Mögliche Erklärungen: (a) Settlement-Timing 25Q4-Käufe Cash-Out 26Q1, (b) BHE-Subsidiary-Treasury-Stock-Activity (separate Entity-Buyback), (c) Reading-Error bei PDF-Layout-Conversion. **Pflicht-Verify** im Tag-+1-Workflow vor Score-Move.

→ **Codex-HIGH-Antizipation #3:** Reviewer wird Buyback-Run-Rate-Aussage challengen, falls Cashflow-Statement-Read nicht reconciled. Pre-empt mit expliziter Discrepancy-Notiz.

---

## 6. NEUE Investment-Income-Decline Mechanik (für Tag-+1 Sparring)

§12.4 hatte Insurance-Investment-Income $2,68B vs $2,89B (−7,4%). **Note 24 bestätigt $3.307M vs $3.571M (−7,4%, Insurance-Segment-Investment-Income inkl. dividends).**

**Konsolidiertes „Interest, dividend and other investment income"** (Z.273): $5.430M Q1-26 vs $5.632M Q1-25 = **−3,6%**.

**Diff Insurance-Inv-Income (−7,4%) vs Konsolidiert (−3,6%):** $2,1B Non-Insurance-Investment-Income (BHE/BNSF/Other-Holdings/Float-Outside-Insurance) ist gestiegen. Treasury-Yield-Mix-Decline trifft asymmetrisch Insurance-Sub stärker — wahrscheinlich Mix-Shift Long-Duration-Treasuries → Short-T-Bills (kürzerer Yield-Pickup auf rolling-basis bei Q1-26 vs Q1-25 Yield-Curve-Shape).

→ **Score-Reasoning Tag-+1:** Investment-Income-Decline ist NICHT Sub-Score-Trigger (Insurance-Exception), aber Float-Yield-Mix-Watch gehört in `notizen`. Mid-Term-Earnings-Power leicht gedrückt, Cash-Pile $397B = Trockenpulver bei Yield-Recovery-Phase.

---

## 7. Insurance-Exception-Score-Reasoning-Anchor (Tag-+1 Pflicht-Section)

BRK ist **Insurance-Exception** (PORTFOLIO §Aktive Watches; FLAG-Status „✅ Clean (Insurance Exception)"). Standard-DEFCON-Sub-Scores nicht direkt anwendbar:

| Standard-Sub | BRK-Insurance-Anchor | Tag-+1 Wert |
|--------------|---------------------|-------------|
| CapEx/OCF | N/A (Float-Modell) | — |
| FCF-Yield | N/A (Holdings-Modell) | — |
| ROIC | N/A (Float-Investment-Spread statt operativer ROIC) | — |
| Bilanz | Cash + T-Bills $397,4B (+$24,1B QoQ ATH) | **9/9 oder 8/9?** Reasoning-Punkt: ATH-Cash = positiv (Trockenpulver) ODER negativ (No-Deal-Opportunity-Cost)? |
| OpMargin | UW-Margin (Insurance) + Operating-Leverage (BNSF/BHE) | Insurance-UW-Margin Q1-26 10,3% (2.265/22.005) vs 7,9% Q1-25 — verbessert, aber GEICO-Decel-Asymmetrie |
| Moat | Wide (3 Quellen) | unverändert 18-19/20 |
| Tech | Float-Growth + Top-5-Konzentrations-Roll | Float +$0,5B QoQ flat; Top-5 65→61% Diversifikations-Signal |

**Sub-Score-Drift-Risk Tag-+1:** Cash-Pile $397B als Bilanz-Sub-Score-Hebel oder negativ-Opportunity-Cost? Codex-Sparring wird das aufnehmen → Pre-empt mit klarer Methodology-Wahl im Score-Record.

→ **Methodology-Watch-Vorschlag (PIPELINE-Item Tag-+1 Schritt 6):** „BRK_Insurance_Exception_Cash_Pile_Score_Treatment" — definiert Tag-+1, ob Cash-ATH positiv (Sub-Score-Lift) oder Opportunity-Cost-Notiz (Sub-Score-neutral mit `notizen`-Caveat). Empfehlung: **NEUTRAL mit Caveat** (V-Q2-Lehre: keine ad-hoc Score-Lifts ohne SKILL-Klausel-Hardening).

---

## 8. Annual Meeting Q&A Watch-Items (strukturiert für Live-Stream)

Sa 02.05. ~14:30 Berlin Annual Meeting startet. Watch-Liste für Tag-+1-Vorbereitung:

**Tier-1 (Score-relevant):**
1. **Cash-Allokation $397B** — explizite Buffett/Abel-Statement zu „warum kein Major-Deal trotz Trockenpulver". Antwort prägt Bilanz-Sub-Score-Lesart Tag-+1.
2. **Apple-Position-Detail** — Trim-Welle Q1-26 (Cost-Basis −$3,05B) bestätigt? Wenn Frage gestellt + Antwort gegeben → Top-5-Konzentrations-Sub-Score-Reasoning.
3. **KHC-Outlook** — direkte Frage erwartet (FV<Carrying 15,7%); Antwort prägt Equity-Method-Position-Reasoning (Q2-OTTI-Pre-empt).
4. **OxyChem-Strategie + Pipeline** — erste Major-M&A seit Alleghany 2022; ist das ein Modell-Wechsel zu Operating-Acquisitions statt Equity-Investments?
5. **Succession** — Greg Abel als CEO-Pfad, Buffett-Reduzierung; Stabilitäts-Score-Reasoning.

**Tier-2 (Watch-only, kein Score-Hebel):**
6. **Geopolitik / Trade-War / Tariffs** — Apple-Tariff-Indirect-Exposure relevant.
7. **Insurance-Cycle-Outlook** — GEICO-Loss-Ratio-Verschlechterung Reaktion.
8. **BNSF-Operating-Leverage-Sustainability** — Productivity-Story dauerhaft?

**Tag-+1 Workflow:** Annual Meeting Transcript via `mcp__defeatbeta-api__get_stock_earning_call_transcript` (sollte Sa-Abend / So-morgen verfügbar sein). Falls nicht verfügbar bis 04.05. → Tag-+1 mit 10-Q + PR-only durchziehen, Annual-Meeting-Q&A als Q2-Methodology-Watch deferred.

---

## 9. Codex-HIGH-Antizipation (12 wahrscheinliche Findings)

Pre-empt im Score-Record `notizen`-Feld:

| # | Wahrsch. Codex-Finding | Pre-empt-Strategie |
|---|------------------------|---------------------|
| 1 | GEICO −34,8% UW-Decel ignoriert in Insurance-UW-Sub-Score | Segment-Dekomposition explizit im notizen + Sub-Score nicht mechanisch +1/+2 |
| 2 | KHC-Q2-OTTI-Risk nicht erwähnt | PIPELINE-Item „BRK_KHC_OTTI_Watch_Q2_FY26" in Schritt 6 |
| 3 | Buyback-Cashflow vs PR-Discrepancy ($4,57B vs $235M) | Discrepancy-Notiz im notizen + Reconciliation-Versuch (Settlement-Timing-Hypothese) |
| 4 | Cash-Pile-ATH als Sub-Score-Lift ohne SKILL-Klausel | Methodology-Watch Item #neu + Sub-Score NEUTRAL gehalten (V-Q2-Lehre) |
| 5 | Apple-Trim-Cost-Basis-Signal nicht explizit | Apple-Cost-Basis-Move im notizen explizit, Top-5-Konz-Roll mit Apple-Komponente trennen |
| 6 | Insurance-Exception-Anchor-Begründung pro Sub-Score fehlt | Section §7 dieses Briefs in Score-Record `notizen` voll übernehmen |
| 7 | BHE Tax-Rate-Move-Mechanik (Wildfire-Settlement-ETR) ungelöst | „BHE-ETR-Watch-Q2" im notizen + Schritt 6 |
| 8 | BHRG/BH Primary Base-Effekt (Q1-25 UW-Loss-Quartal) Codex-MED | „Recovery-from-Loss-Base" explizit im Insurance-UW-Reasoning |
| 9 | OxyChem-Acquisition Konsolidierung Q1-only-period | OxyChem $9,5B Acquisition-Goodwill / Identifiable-Assets-Allocation noch „preliminarily estimated" — Q2-Refinement-Watch |
| 10 | Float +$0,5B QoQ flat als Tech-Sub-Score-Drift-Risk | Float-Growth Sub-Score 0/+1 (NICHT +2) — Q1 saisonal flat, kein Decel-Signal |
| 11 | Insider-Block carryover-only (kein Form-4-Pull bis 02.05.) | Form-4-Pull `python 01_Skills/insider-intelligence/insider_intel.py scan BRK.B` Tag-+1 PFLICHT |
| 12 | PacifiCorp-Wildfire-Liability-Restbeträge ($577M unpaid + reasonably possible material additional) als Risk-Map-Notiz fehlend | Risk-Map-Sektion explizit + BHE-PreTax-Move-Erklärung |

---

## 10. Tag-+1 Workflow-Plan (sequenziell)

**Geschätzter Aufwand:** 90-150 Min Vollanalyse + 30-45 Min Codex-Sparring + 30 Min Sync-Welle = ~3-4h Tag-+1-Slot.

1. **Pre-Open (Sa-Abend / So-morgen):** Annual Meeting Transcript via defeatbeta-MCP holen (falls verfügbar); falls nein → Earnings-Call-Transcripts-Liste prüfen.
2. **Insider-Form-4-Pull:** `python 01_Skills/insider-intelligence/insider_intel.py scan BRK.B` — Tag-0 PR hatte keine Form-4-Detail.
3. **Insurance-Exception-Anchor schreiben** (Section §7 dieses Briefs als Vorlage in Score-Record `notizen`).
4. **`!Analysiere BRK.B`** mit dynastie-depot-Skill, voll dekomponierte Sub-Scores incl. Insurance-Exception-Anchors.
5. **Schritt 6c Pre-Flight-Audit** (V-Q2-Lehre: jeder Sub-Score `!=0` braucht Rohwert ODER `_carryover`).
6. **Pre-Append-Audit Sektion §1-8 dieses Briefs gegenchecken** (alle Codex-HIGH-Pre-empt-Items im notizen-Feld).
7. **Schritt 7 backtest-ready-forward-verify Append.**
8. **Codex R1-Review** via `codex:codex-rescue` mit explizitem Verweis auf diesen Pre-Brief als Antizipations-Material → Erwartung: ≤2 HIGH-Findings (vs MSFT 5 + AVGO 5), R1-Pass-Wahrscheinlichkeit 80%+.
9. **R2-Round nur bei HIGH-Count ≥2** (Codex-Sparring-Heuristik Memory).
10. **§18-Sync-Welle** voll: PORTFOLIO + CORE-MEMORY §12.4 Update + Faktortabelle + log + score_history.jsonl + config.yaml + xlsx-Tools (KEIN flag_events.jsonl, da kein FLAG-Move).
11. **PIPELINE-Item-Updates:** BRK.B-Trigger 02.05. abhaken → DONE; ggf. neue Items #35-40 (KHC-OTTI-Watch + Insurance-Exception-Cash-Treatment + GEICO-Decel-Watch + BHE-ETR-Watch + OxyChem-Refinement-Watch).
12. **CORE-MEMORY §13** ggf. Lifecycle-Eintrag falls Methodology-Watch-Items entstehen.

**Sparraten-Erwartung:** Score 75 → wahrscheinlich 73-77 Range (Insurance-UW-Asymmetrie zieht +1 ab, Cash-ATH-Bilanz-Diskussion neutralisiert sich, BNSF-Operating-Leverage marginal +1). **Kein D-Level-Wechsel erwartet** (D3 65-79 Band hat 14pt-Puffer). Sparrate **38,00€ unverändert** wahrscheinlich; Kaskade nicht erwartet.

---

## 11. Synthesis (Tag-0 spätnachmittag)

BRK.B Q1 FY26 hat **3 Big-Surprises** (Cash $397B / Equity-Net-Sale $8,15B / OxyChem $9,5B M&A — siehe §12.4) UND **3 unter-der-Oberfläche-Asymmetrien** dieser Brief deckt:
1. **GEICO-Decel −34,8% UW** trotz Insurance-Total +28,5% (Headline irreführend).
2. **Apple-Cost-Basis-Trim −$3,05B** = explizite Trim-Welle (nicht reine FV-Marktbewegung).
3. **KHC-Carrying-Value-Excess 15,7%** = Q2-OTTI-Risk material trotz Q1-No-OTTI.

Codex-HIGH-Antizipation pre-empted (12 Items) → Tag-+1 R1-Pass-Wahrscheinlichkeit 80%+ realistisch (vs. MSFT 60% / AVGO 55% historisch). Token-Effizienz Tag-+1 erwartet **−40% vs. blanker Vollanalyse-Run** durch dieses Brief-Material.

**Tag-+1 Slot-Empfehlung:** **So 03.05. morgens** (volle Q&A-Transcript-Verfügbarkeit + frischer Kopf). Falls Annual-Meeting-Transcript bis Sa-Abend nicht verfügbar → **Mo 04.05. morgens** mit voll-Transcript-Read.

---

*Caveats: Pre-Brief auf 10-Q + PR + §12.4-Stand 02.05. Tag-0; Annual-Meeting-Q&A nicht inkludiert (Live-Stream während Brief-Erstellung läuft). Numerische Detail-Discrepancies (Buyback-Cashflow vs PR; BHE-PreTax vs After-Tax) sind Reconciliation-Pflicht Tag-+1, nicht Brief-Konflikt. Keine Anlageberatung.*

*Erstellt 02.05.2026 (Sa) Tag-0 spätnachmittag — analog `MSFT_pre-earnings_2026-04-29.md` Format, mit Tag-+1-Vorbereitungs-Fokus statt Pre-Earnings-Setup (BRK ist Tag-+1-Slot wegen §19.1 Wait-Discipline + Annual-Meeting-Timing).*
