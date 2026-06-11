---
name: indian-gst-expert
description: >
  Comprehensive Indian GST (Goods and Services Tax) expert covering GST 2.0 reforms
  (effective September 22, 2025), calculations, tax slabs, filing rules, e-invoicing
  compliance, ITC, RCM, penalties, and registration rules. ALWAYS use this skill when
  the user asks about: GST rates, CGST/SGST/IGST calculations, HSN codes, GST filing
  deadlines (GSTR-1, GSTR-3B, GSTR-9), e-invoicing (IRP, IRN), composition scheme,
  input tax credit, reverse charge mechanism, GST registration thresholds, late fees,
  or any Indian indirect tax question — even if phrased casually (e.g. "how much GST
  on X?", "when to file GST?", "do I need GST registration?").
---

# Indian GST Expert (GST 2.0 — 2025/2026)

This skill covers the full Indian GST framework post the landmark **GST 2.0 reforms effective September 22, 2025**, through 2026 and into FY 2026-27.

## Quick Reference

| Task | Go To |
|---|---|
| Calculate GST (CGST/SGST/IGST) | [Calculator Script](#1-gst-calculator) |
| Find rate for a specific item | [Tax Slab Reference](#2-tax-slab-determination) |
| Filing deadlines / compliance calendar | `references/compliance_calendar.md` |
| HSN/SAC code lookup guidance | `references/hsn_sac_guide.md` |
| E-invoicing rules | `references/einvoicing_rules.md` |
| ITC, RCM, penalties | `references/advanced_rules.md` |
| Registration thresholds | [Registration Rules](#4-registration-rules) |

---

## 1. GST Calculator

Run the Python script for precise calculations:

```bash
python3 /home/claude/indian-gst-expert/scripts/gst_calculator.py <amount> --rate <rate> [--intrastate]
# OR use --category flag:
python3 /home/claude/indian-gst-expert/scripts/gst_calculator.py <amount> --category <category> [--intrastate]
```

**Categories:** `exempt` (0%), `essential` (5%), `standard` (18%), `luxury` (40%), `precious_metals` (3%), `rough_stones` (0.25%)

**Default is interstate (IGST).** Add `--intrastate` for same-state transactions (CGST + SGST).

**Example outputs:**

- Interstate ₹10,000 at 18%: IGST = ₹1,800, Total = ₹11,800
- Intrastate ₹10,000 at 18%: CGST = ₹900 + SGST = ₹900, Total = ₹11,800

> For manual computation in responses: IGST = Amount × Rate%; CGST = SGST = Amount × (Rate/2)%

---

## 2. Tax Slab Determination

### GST 2.0 Core Slabs (Effective September 22, 2025)

| Slab | Category | Key Examples |
|---|---|---|
| **0% (Nil)** | Essentials & Exempt | Fresh/frozen vegetables, fresh fruit, milk, eggs, bread, roti/paratha/chapati, rice, flour, pulses, fresh meat/fish, unbranded honey; Individual health insurance (family floater, senior citizen plans); Term life insurance, ULIPs, endowment plans; Education services; Healthcare/hospital services; Books, newspapers; Cancer drugs (3 specific lifesaving drugs); 33 specified lifesaving drugs |
| **5%** | Merit / Daily Use | Packaged namkeens, bhujia, instant noodles, pasta, chocolates, cornflakes, coffee, ghee, butter, cheese, dairy spreads; Hair oil, shampoo, toothpaste, soaps, tooth brushes, shaving cream; Agricultural equipment (tractors, parts, bio-pesticides, drip irrigation); Medical: thermometers, diagnostic kits, medical grade oxygen; Utensils, sewing machines; Baby feeding bottles, napkins; Apparel/footwear **≤ ₹2,500**; Hotel stays (₹1,001–₹7,500/night); Essential medicines |
| **18%** | Standard | Consumer durables: ACs, TVs (all sizes), refrigerators, washing machines, dishwashers; Electronics: laptops, mobiles (HSN 8517), monitors, projectors; Small cars (petrol/hybrid ≤1200cc & ≤4000mm; diesel ≤1500cc & ≤4000mm); 3-wheelers; Motorcycles **≤ 350cc**; Professional services (CA, legal, IT, consulting); Restaurants; Telecom; Banking/financial services (non-exempt); Cosmetics; Most packaged goods not in 5% |
| **40%** | Luxury / Sin | Premium cars (>4000mm or >1500cc diesel); SUVs; Motorcycles **> 350cc**; Aerated/caffeinated beverages; Pan masala; Cigarettes, tobacco; Online gaming (real money); Casinos; Betting; Premium event tickets |
| **3%** | Precious Metals | Gold, silver, jewellery, platinum |
| **0.25%** | Rough Stones | Uncut/unprocessed precious and semi-precious stones |

> **Note on 12% and 28% slabs:** These have been **eliminated** under GST 2.0. Items previously at 12% moved to 5% or 18%. Items previously at 28% moved to 18% or 40%.

### Price-Dependent Rates

| Item | Condition | Rate |
|---|---|---|
| Apparel / Clothing | Retail price ≤ ₹2,500 | 5% |
| Apparel / Clothing | Retail price > ₹2,500 | 18% |
| Footwear | Selling price ≤ ₹1,000 | 5% |
| Footwear | Selling price > ₹1,000 | 18% |
| Hotel accommodation | Room tariff ≤ ₹1,000/night | 0% |
| Hotel accommodation | Room tariff ₹1,001–₹7,500/night | 5% |
| Hotel accommodation | Room tariff > ₹7,500/night | 18% |

---

## 3. Filing & Compliance Overview

Read `references/compliance_calendar.md` for the full month-wise calendar. Quick summary:

| Return | Who Files | Due Date |
|---|---|---|
| **GSTR-1** (monthly) | Turnover > ₹5 Cr | 11th of next month |
| **GSTR-1** (quarterly, QRMP) | Turnover ≤ ₹5 Cr | 13th of month after quarter |
| **IFF** (Invoice Furnishing Facility) | QRMP taxpayers (monthly uploads) | 13th of next month |
| **GSTR-3B** (monthly) | Turnover > ₹5 Cr | 20th of next month |
| **GSTR-3B** (quarterly, QRMP) | Turnover ≤ ₹5 Cr | 22nd (Cat-X states) / 24th (Cat-Y states) |
| **PMT-06** (QRMP monthly payment) | QRMP scheme taxpayers | 25th of each month |
| **GSTR-4** (annual, composition) | Composition dealers | 30th April |
| **CMP-08** (quarterly, composition) | Composition dealers | 18th of month after quarter |
| **GSTR-7** (TDS) | TDS deductors | 10th of next month |
| **GSTR-8** (TCS) | E-commerce operators | 10th of next month |
| **GSTR-9** (annual) | Regular taxpayers, turnover > ₹2 Cr | **31 December** (for prior FY) |
| **GSTR-9C** (reconciliation) | Turnover > ₹5 Cr | **31 December** (same as GSTR-9) |

**QRMP Scheme:** Available for taxpayers with AATO ≤ ₹5 Crore. File GSTR-1 and GSTR-3B quarterly, pay tax monthly via PMT-06.

---

## 4. Registration Rules

### Mandatory Registration Thresholds

| Business Type | Normal States | Special Category States |
|---|---|---|
| Goods only | ₹40 Lakhs | ₹20 Lakhs |
| Services / Mixed | ₹20 Lakhs | ₹10 Lakhs |

**Special Category States:** Manipur, Mizoram, Nagaland, Tripura (₹10L services); Arunachal Pradesh, Meghalaya, Sikkim, Uttarakhand, Himachal Pradesh, J&K (₹20L goods, ₹10L services for some).

### Mandatory Registration Regardless of Turnover
- Interstate taxable supplies
- E-commerce sellers / marketplace operators (TCS applicable)
- Reverse charge mechanism (RCM) recipients
- Input Service Distributors (ISD) — **mandatory from April 1, 2025**
- Non-resident taxable persons
- Casual taxable persons

---

## 5. Key 2025-2026 Compliance Rules (Quick Reference)

| Rule | Detail |
|---|---|
| **E-invoicing threshold** | Mandatory for AATO > ₹5 Crore (any FY since 2017-18) |
| **30-day IRP reporting** | AATO ≥ ₹10 Crore must upload invoices within 30 days of issue (from April 1, 2025) |
| **HSN digits (AATO < ₹5 Cr)** | 4-digit HSN mandatory on invoices |
| **HSN digits (AATO ≥ ₹5 Cr)** | 6-digit HSN mandatory on invoices |
| **ITC hard block (Jan 2026)** | GSTR-3B blocked if RCM liabilities unpaid or negative credit ledger |
| **3-year return filing limit** | Returns older than 3 years from due date permanently blocked (from Dec 2025) |
| **ISD mandatory (April 2025)** | Entities receiving common input services for multiple GSTINs must register as ISD |
| **Late payment interest** | 18% per annum (compounded daily) |
| **Late filing fee (GSTR-1/3B)** | ₹50/day (₹25 CGST + ₹25 SGST), capped at ₹2,000 per return for nil returns; ₹50/day capped at ₹5,000 for others |
| **Late fee (GSTR-9)** | ₹200/day (₹100 CGST + ₹100 SGST), capped at 0.25% of turnover |
| **Non-registration penalty** | 10% of tax due (min ₹10,000); fraud: 100% of tax + interest |

---

## 6. Workflows

### Workflow A — Calculate GST for a Transaction
1. Identify **base amount** and **item/service**
2. Determine **GST slab** (Section 2 or run script with --category)
3. Determine **transaction type**: same-state (intrastate → CGST+SGST) or different states/imports (interstate → IGST)
4. Run `gst_calculator.py` or compute manually
5. Present breakdown: Base Amount, GST Rate, CGST/SGST or IGST, Total Amount

### Workflow B — Determine Filing Obligation
1. Check taxpayer **AATO** and **registration type** (regular, composition, QRMP)
2. Load `references/compliance_calendar.md` for current month deadlines
3. Flag any **e-invoicing obligations** based on AATO
4. Note any applicable **penalties** for missed deadlines

### Workflow C — Research & Advisory
1. For HSN code questions, load `references/hsn_sac_guide.md`
2. For ITC / RCM questions, load `references/advanced_rules.md`
3. For e-invoicing, load `references/einvoicing_rules.md`
4. Summarize with practical action steps; always cite effective dates

---

## Reference Files

| File | Contents |
|---|---|
| `references/compliance_calendar.md` | Month-by-month filing calendar FY 2026-27, late fee tables |
| `references/hsn_sac_guide.md` | HSN/SAC code lookup guide, common codes by sector |
| `references/einvoicing_rules.md` | Full e-invoicing rules, IRP process, IRN, penalties |
| `references/advanced_rules.md` | ITC eligibility, RCM, composition scheme, QRMP details |
| `scripts/gst_calculator.py` | GST calculation engine (CGST/SGST/IGST) |

> **Always** load the relevant reference file before answering detailed questions on those topics.
