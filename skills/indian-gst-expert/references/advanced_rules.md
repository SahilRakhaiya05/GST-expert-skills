# Advanced GST Rules — ITC, RCM, Composition, Penalties

> Covers: Input Tax Credit, Reverse Charge Mechanism, Composition Scheme,
> QRMP Scheme, Anti-profiteering, Refunds, and 2026 compliance updates.

## Table of Contents
1. [Input Tax Credit (ITC)](#1-input-tax-credit-itc)
2. [Reverse Charge Mechanism (RCM)](#2-reverse-charge-mechanism-rcm)
3. [Composition Scheme](#3-composition-scheme)
4. [QRMP Scheme (Quarterly Return Monthly Payment)](#4-qrmp-scheme)
5. [Refunds under GST](#5-refunds-under-gst)
6. [Penalties & Offences](#6-penalties--offences)
7. [GST Audit & Annual Return](#7-gst-audit--annual-return)
8. [Special Transactions](#8-special-transactions)

---

## 1. Input Tax Credit (ITC)

### What Is ITC?
ITC allows a registered taxpayer to **offset GST paid on purchases (inputs)** against the **GST liability on sales (output)**. Only the net GST is deposited with the government.

**Example:**
- You buy raw material and pay ₹1,800 IGST
- You sell finished goods and collect ₹3,600 IGST
- You pay only: ₹3,600 − ₹1,800 = **₹1,800 net to government**

### ITC Eligibility Conditions (all must be met)
1. You are a **registered GST taxpayer**
2. You hold a **valid tax invoice or debit note** from the supplier
3. Goods/services have been **actually received**
4. Supplier has **filed GSTR-1** and the invoice appears in your **GSTR-2B**
5. Tax has been **paid to the government** by the supplier
6. You have **filed your GST return** (GSTR-3B)
7. The goods/services are used for **business purposes** (not personal)

### ITC Blocked Items (Section 17(5) — Cannot Claim ITC)
| Item | Rule |
|---|---|
| Motor vehicles for personal use (≤13 seats) | Blocked |
| Food and beverages, outdoor catering | Blocked |
| Beauty treatment, health/fitness services | Blocked |
| Life insurance, health insurance (personal) | Blocked |
| Works contract services for construction of own immovable property | Blocked |
| Goods/services for construction of own immovable property | Blocked |
| Membership of clubs/health clubs | Blocked |
| Travel benefits for employees (vacation/LTC) | Blocked |
| Any goods/services for non-business use | Blocked |

**Exceptions (ITC allowed even for above):**
- Vehicles used for transport of goods (trucks, delivery vans)
- Vehicles used for passenger transport as business (taxi service, bus operator)
- Motor vehicles used for training driving school
- Food/beverages where it is obligatory for employer to provide under any law
- Insurance of vehicles used for business purposes

### ITC for Capital Goods
- ITC on capital goods can be claimed in full in the **year of purchase**
- If capital goods are partly used for business + partly for personal use, ITC is proportional to business use
- If capital goods are sold later, ITC reversal or payment required per rules

### ITC Reconciliation (GSTR-2B)
- GSTR-2B is auto-generated on the 14th of every month
- It shows all ITC available based on supplier GSTR-1 filings
- **From January 2026:** ITC claimed in GSTR-3B **must not exceed** GSTR-2B amounts (hard block)
- Discrepancies must be resolved with suppliers before claiming ITC

### ITC Reversal Rules
| Situation | Reversal Required |
|---|---|
| Payment not made to supplier within 180 days | Reverse ITC + pay interest @18% |
| Supplier cancels/amends invoice | Reverse proportionate ITC |
| Goods returned to supplier | Reverse ITC or issue debit note |
| Goods used for personal purpose | Reverse proportionate ITC |
| Post-sale discount received (from Apr 2026) | Buyer must reverse ITC via IMS |

### Time Limit for ITC Claims
- ITC must be claimed by **30 November** of the next financial year OR the date of filing annual return, **whichever is earlier**
- Example: ITC for FY 2025-26 must be claimed by 30 November 2026

---

## 2. Reverse Charge Mechanism (RCM)

### What Is RCM?
Under RCM, the **recipient (buyer) pays GST** instead of the supplier. The buyer self-invoices, pays GST to the government, and can then claim ITC on it (if eligible).

### When Does RCM Apply?

#### A. Specified Goods (Section 9(3))
| Goods | Supplier | Rate |
|---|---|---|
| Cashew nuts (unshelled/shelled) | Agriculturist → registered dealer | 5% |
| Bidi wrapper leaves | Agriculturist | 5% |
| Tobacco leaves | Agriculturist | 5% |
| Silk yarn | Silk yarn manufacturer | 5% |
| Raw cotton | Agriculturist | 5% |
| Used vehicles, waste, scrap | Government | As applicable |
| Lottery | State Government / distributor | As applicable |

#### B. Specified Services (Section 9(3))
| Service | Supplier | GST Paid By |
|---|---|---|
| Legal services by advocate | Individual advocate to business | Recipient (business) |
| Services by director to company | Director (as individual) | Company |
| Rent for immovable property to registered person | Unregistered landlord | Registered tenant |
| Security services | Unregistered person to registered body | Recipient |
| Services by GTA (if opted for RCM) | Goods Transport Agency | Recipient |
| Sponsorship services | Any person to body corporate | Body corporate |
| Services of insurance agent | Insurance agent | Insurance company |
| Services of recovery agent | Recovery agent | Banking company |
| Manpower/labour supply | Unregistered person to registered body | Recipient |
| Works contract (government infrastructure) | Any supplier to government | Government |

#### C. Unregistered Supplier (Section 9(4))
- If a **registered person** buys **taxable goods or services** from an **unregistered person**, RCM applies
- Recipient must pay full GST
- De minimis threshold: If total purchases from unregistered persons in a day < ₹5,000, RCM may not apply (check specific category notifications)

### RCM Compliance Steps
1. Identify supply as RCM
2. Issue **self-invoice** (tax invoice by recipient)
3. Pay GST under RCM in **cash** (cannot use ITC balance for RCM payment)
4. Declare in GSTR-3B (Table 3.1(d))
5. Claim ITC on RCM paid (in the same or next period, after payment) — Table 4(A)(3) in GSTR-3B

> **2026 Rule:** From January 2026, GSTR-3B filing is **blocked** if RCM liabilities are unpaid.

---

## 3. Composition Scheme

### Eligibility
- AATO ≤ ₹1.5 Crore (₹75 Lakh in certain NE/hill states) — for manufacturers and traders
- AATO ≤ ₹50 Lakh — for service providers (Section 10(2A))
- Cannot make interstate outward supplies (except services up to ₹5 Lakh)
- Cannot supply exempt goods
- Cannot be an e-commerce operator

### Tax Rates under Composition Scheme

| Business Type | Composition Rate | Notes |
|---|---|---|
| Manufacturers | 1% (0.5% CGST + 0.5% SGST) | On turnover |
| Traders (goods) | 1% (0.5% CGST + 0.5% SGST) | On turnover |
| Restaurants / food (not supplying alcohol) | 5% (2.5% CGST + 2.5% SGST) | On turnover |
| Service providers | 6% (3% CGST + 3% SGST) | On turnover |
| Mixed (goods + services) | 1% on goods; 6% on services | Combined |

### Key Restrictions
- **Cannot charge GST** on invoices to buyers (pays from own pocket)
- **No ITC** available (cannot claim credit on purchases)
- Must display **"Composition Taxable Person"** on all invoices and signboards
- Buyers cannot claim ITC on purchases from composition dealers
- Cannot issue tax invoices — issues **Bill of Supply** instead
- **Not eligible for e-invoicing** mandate

### Compliance
- **CMP-08:** Quarterly self-assessed tax payment (18th of month after quarter)
- **GSTR-4:** Annual return (30 April each year)
- **No GSTR-1 or GSTR-3B** filing required

### Opting In/Out
- Opt in: At start of FY or at time of new registration
- Opt out: If turnover exceeds limit, or voluntarily at start of FY
- File **CMP-04** (intimation to opt out)

---

## 4. QRMP Scheme

### What Is QRMP?
Quarterly Return Monthly Payment — allows small taxpayers (AATO ≤ ₹5 Crore) to:
- **File GSTR-1 and GSTR-3B quarterly** (instead of monthly)
- **Pay tax monthly** via PMT-06 challan

### Eligibility
- AATO ≤ ₹5 Crore in previous FY
- Must be a regular (non-composition) taxpayer
- All GSTINs under same PAN must be under QRMP (no mixing)

### Filing Under QRMP

| Action | Month 1 & 2 of Quarter | Month 3 of Quarter |
|---|---|---|
| B2B invoice upload | IFF (optional, by 13th) | Part of GSTR-1 (by 13th after quarter) |
| Tax payment | PMT-06 (by 25th) | Included in GSTR-3B |
| GSTR-3B filing | Not required | By 22nd/24th of month after quarter end |

### PMT-06 Payment Amount
For months 1 and 2, pay either:
- **Fixed Sum Method:** 35% of net tax paid in last quarter's GSTR-3B
- **Self-Assessment Method:** Exact tax based on actual supplies in the month

### IFF (Invoice Furnishing Facility)
- Optional upload of B2B invoices in months 1 and 2 of quarter
- Allows buyer to claim ITC without waiting for quarterly GSTR-1
- Deadline: 13th of the following month
- Not mandatory — GSTR-1 at quarter end captures all invoices anyway

---

## 5. Refunds under GST

### Refund Scenarios

| Scenario | Refund Available |
|---|---|
| Export of goods with payment of IGST | Yes — IGST refund |
| Export of services with payment of IGST | Yes — IGST refund |
| Export under LUT (Letter of Undertaking) | Yes — accumulated ITC refund |
| SEZ supplies | Yes — IGST or ITC refund |
| Excess tax paid by mistake | Yes |
| ITC accumulated due to inverted duty structure | Yes (GST on inputs > GST on output) |
| Deemed exports | Yes |

### Key Refund Rules (2026)
- **Export refund minimum threshold removed (April 2026):** The earlier ₹1,000 minimum for IGST-paid export refunds is abolished — any amount is refundable
- **Fast-track refund:** Businesses with strong compliance history receive 90% provisional refund within 7 days
- Refund application filed in **Form RFD-01** on GST portal
- Time limit: Within **2 years** from the relevant date
- Refund of accumulated ITC (inverted duty): Applied per quarter

### Refund for Tourists
Foreign tourists visiting India can claim refund of GST paid on goods purchased in India and taken out of India (scheme applicable at notified airports).

---

## 6. Penalties & Offences

### Late Filing Fees
See `compliance_calendar.md` Section 5 for the full late fee table.

### Penalties for Tax Evasion

| Offence | Penalty |
|---|---|
| Tax unpaid/short-paid (genuine error) | 10% of tax due (min ₹10,000) |
| Tax unpaid/short-paid (fraud/suppression) | 100% of tax due (equal to tax amount) |
| Non-registration despite being liable | 10% of tax due (min ₹10,000) |
| Furnishing false information | Up to ₹25,000 |
| Failure to maintain accounts/records | ₹25,000 |
| Failure to furnish information/documents | ₹25,000 |
| Failure to appear before GST officer | ₹25,000 |
| E-invoice non-compliance | ₹10,000 per invoice or 100% of tax |
| Incorrect e-invoice details | ₹25,000 per invoice |

### Criminal Offences (Prosecution)
These can lead to **imprisonment**:
- Tax evasion > ₹5 Crore: Up to 5 years + fine
- Fraudulent ITC claims > ₹5 Crore: Up to 5 years + fine
- Repeat offences: Enhanced penalties

### Demand & Recovery Process
1. Show Cause Notice (SCN) issued
2. Reply within specified time
3. Adjudication order
4. Appeal: GSTAT → High Court → Supreme Court
5. Payment of demand + interest + penalty

---

## 7. GST Audit & Annual Return

### GSTR-9 (Annual Return)
- **Who:** Regular taxpayers with AATO > ₹2 Crore
- **Due:** 31 December following FY end
- **Contents:** Consolidated summary of all monthly returns, ITC summary, HSN-wise summary
- **Turnover ≤ ₹2 Crore:** Optional but recommended

### GSTR-9C (Reconciliation Statement)
- **Who:** AATO > ₹5 Crore
- **Due:** Same as GSTR-9 (31 December)
- **Nature:** Self-certified reconciliation between audited books and GST returns (CA certification not mandatory since changes in 2020-21, but many businesses still use CA for accuracy)

### Departmental Audit (Section 65)
- GST officer may conduct audit at business premises
- Notice given at least 15 days prior
- Audit completed within 3 months (extendable to 6 months)
- Discrepancy found → demand notice issued

### Special Audit (Section 66)
- Commissioner can order special audit by CA/CMA if complexity warrants
- All costs borne by government

---

## 8. Special Transactions

### Imports
- IGST + Basic Customs Duty (BCD) levied at point of import
- IGST on imports = (Customs Value + BCD + other duties) × IGST rate
- IGST paid on imports is fully available as ITC
- From January 2026: Importers must include Bill of Entry (BoE) in IMS for ITC claims

### Exports
- Exports are **zero-rated** (taxed at 0%)
- Two options:
  1. **Export under LUT/Bond:** No IGST paid; claim refund of accumulated ITC
  2. **Export with IGST payment:** Pay IGST, claim refund of IGST paid
- LUT (Letter of Undertaking) must be filed annually on GST portal

### SEZ (Special Economic Zones)
- Supplies to SEZ = zero-rated (treated as exports)
- SEZ units claim refund of IGST paid on inputs
- SEZ developers: Same zero-rating applies

### Cross-Border Services (OIDAR)
- Online Information Database Access and Retrieval services
- Foreign providers supplying digital services to Indian non-business consumers must register and pay GST in India
- Rate: 18%

### E-Commerce
- E-commerce operators (Amazon, Flipkart, Zomato, etc.) must collect **TCS (Tax Collected at Source)** at 1% on net value of taxable supplies
- Sellers on e-commerce platforms must register for GST regardless of turnover (no threshold exemption)
- TCS is reflected in GSTR-8 by operator and GSTR-2B of seller

### Works Contract
- Treated as supply of services
- Rate: 18% (general); 12% (government infrastructure projects)
- Construction of own immovable property: ITC blocked

### Real Estate (New Projects from April 2019)
| Type | GST Rate | ITC |
|---|---|---|
| Affordable housing (PMAY) | 1% | No ITC |
| Residential (non-affordable) | 5% | No ITC |
| Commercial (under construction) | 12% | No ITC |
| Ready-to-move (completion certificate) | 0% (exempt) | N/A |

### Agricultural Produce
- Most unprocessed agricultural produce: 0%
- Once processed/branded/packaged differently: May attract 5% or 18%
- Farmers are generally not required to register under GST
