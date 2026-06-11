# Examples

Real-world examples of what Claude can do with the Indian GST Expert skill installed.

---

## 1. GST Calculation

**Prompt:**
> Calculate GST on ₹85,000 laptop sold from Gujarat to Maharashtra.

**Claude's response:**
```
Transaction Type : Interstate (Gujarat → Maharashtra)
Base Amount      : ₹85,000.00
GST Rate         : 18% (Electronics — Standard slab)
─────────────────────────────────────────
IGST @18%        : ₹15,300.00
─────────────────────────────────────────
Total Payable    : ₹1,00,300.00
```

---

## 2. Intrastate Split

**Prompt:**
> I'm selling gold jewellery worth ₹2,50,000 within Rajasthan. What's my GST?

**Claude's response:**
```
Transaction Type : Intrastate (Rajasthan → Rajasthan)
Base Amount      : ₹2,50,000.00
GST Rate         : 3% (Precious Metals)
─────────────────────────────────────────
CGST @1.5%       : ₹3,750.00
SGST @1.5%       : ₹3,750.00
─────────────────────────────────────────
Total GST        : ₹7,500.00
Total Payable    : ₹2,57,500.00
```

---

## 3. Rate Lookup

**Prompt:**
> What GST rate applies to a ₹3,200 shirt?

**Claude's response:**
> The shirt attracts **18% GST** because its retail price (₹3,200) exceeds the ₹2,500 threshold.
> Below ₹2,500 it would have been 5%.
>
> HSN Code: 6109 (T-shirts, singlets) or 6205 (Men's shirts) — use 4-digit if AATO < ₹5 Cr, 6-digit if ≥ ₹5 Cr.

---

## 4. Filing Deadline Check

**Prompt:**
> My turnover is ₹3.2 crore. When do I file GSTR-1 and GSTR-3B for Q1 April–June 2026?

**Claude's response:**
> With AATO of ₹3.2 Crore you qualify for the **QRMP scheme** (quarterly filing):
>
> - **GSTR-1 (Q1):** 13 July 2026
> - **PMT-06 (April):** 25 April 2026
> - **PMT-06 (May):** 25 May 2026
> - **GSTR-3B (Q1):** 22 July 2026 (Cat-X state) or 24 July 2026 (Cat-Y state)
>
> Check which category your state falls under in the compliance calendar.

---

## 5. E-Invoicing Obligation

**Prompt:**
> Our company crossed ₹12 crore turnover last year. Do we need e-invoicing? Any special rules?

**Claude's response:**
> Yes, **two rules apply** to your business:
>
> 1. **E-invoicing mandatory** — Since your AATO exceeds ₹5 Crore, you must generate e-invoices for all B2B supplies and get an IRN from the Invoice Registration Portal (IRP).
>
> 2. **30-day reporting window** — Since your AATO exceeds ₹10 Crore, you must upload every invoice (including credit/debit notes) to the IRP **within 30 days of the invoice date** (effective April 1, 2025). The IRP will reject anything older than 30 days — no IRN will be issued, making the invoice invalid.
>
> Practical tip: Set up automated daily IRP uploads via your accounting software or a GST Suvidha Provider to avoid rejections.

---

## 6. ITC Eligibility Check

**Prompt:**
> Can I claim ITC on my office AC purchase worth ₹55,000?

**Claude's response:**
> **Yes**, you can claim ITC on the AC purchase, provided:
> - You hold a valid tax invoice with IRN (if supplier's AATO > ₹5 Cr)
> - The AC is used for business purposes (not in a personal residence)
> - The supplier has filed GSTR-1 and the invoice appears in your GSTR-2B
> - You pay the supplier within 180 days
>
> GST paid: ₹55,000 × 18% = ₹9,900 IGST (or split as ₹4,950 CGST + ₹4,950 SGST for intrastate).
>
> **Note:** From January 2026, the ITC claim in GSTR-3B is hard-blocked if it exceeds your GSTR-2B auto-populated credit.

---

## 7. RCM Scenario

**Prompt:**
> I hired a lawyer for my company. Who pays GST — me or the lawyer?

**Claude's response:**
> Under the **Reverse Charge Mechanism (RCM)**, **you (the company)** pay GST — not the lawyer.
>
> Legal services provided by an individual advocate to a business entity are covered under Section 9(3) of the CGST Act. Steps to comply:
>
> 1. Issue a **self-invoice** (tax invoice raised by you as the recipient)
> 2. Pay GST at **18%** on the lawyer's fees **in cash** (cannot use ITC balance for RCM payment)
> 3. Report in GSTR-3B Table 3.1(d)
> 4. Claim ITC on the GST paid (in the same or subsequent period) in Table 4(A)(3)
>
> Example: Lawyer fee ₹50,000 → Self-invoice GST = ₹9,000 (18%) → Pay ₹9,000 to govt → Claim ₹9,000 ITC.

---

## 8. Reverse Calculation

**Prompt:**
> My invoice total (GST inclusive) is ₹1,41,600. GST rate was 18%. What was the base amount?

**Claude's response:**
> ```
> GST-Inclusive Total  : ₹1,41,600.00
> GST Rate             : 18%
> ─────────────────────────────────────
> Base Amount (ex-GST) : ₹1,20,000.00
> GST Extracted        : ₹21,600.00
> ```
> Formula: Base = Total × 100 / (100 + Rate) = 1,41,600 × 100/118 = ₹1,20,000

---

## 9. New 2026 Rules Impact

**Prompt:**
> What changed in GST from January 2026 that I need to know about?

**Claude's response:**
> Four major changes hit from **1 January 2026**:
>
> 1. **ITC Hard Block:** GSTR-3B filing is now blocked by the portal if you have unpaid RCM liabilities or a negative electronic credit ledger. Clear these before filing.
>
> 2. **Mandatory Invoice Management System (IMS):** You must action all inward supply invoices through IMS. Importers must also include Bill of Entry (BoE) data.
>
> 3. **Automatic GSTR-9 Late Fees:** Annual return late fees now trigger automatically from day 1 after the 31 December deadline — no grace period.
>
> 4. **3-Year Return Bar:** GST returns for FY 2022-23 and earlier are permanently blocked and cannot be filed. If you have any pending returns for those years, that ITC is permanently lost.

---

## 10. Composition Scheme Query

**Prompt:**
> I run a small kirana store with ₹80 lakh annual turnover. Should I go for composition scheme?

**Claude's response:**
> You are **eligible** for the Composition Scheme (limit is ₹1.5 Crore for traders).
>
> **Pros:**
> - Pay only **1% GST** on your total turnover (instead of 5%/18% on each transaction)
> - File only **CMP-08** quarterly + **GSTR-4** annually (no monthly returns)
> - Much simpler compliance
>
> **Cons:**
> - You **cannot charge GST** on your bills — tax comes from your own pocket
> - Your business customers **cannot claim ITC** from you (bad for B2B)
> - **No interstate sales** allowed
> - Not eligible for e-invoicing benefits
>
> **Best for:** Retail shops selling directly to consumers (B2C) with low margins and simple operations.
> **Not ideal for:** Shops with significant B2B sales where buyers need ITC.
