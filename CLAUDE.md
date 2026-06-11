# Indian GST Expert — Claude Code Guidelines

> Drop this file into any project that involves Indian GST calculations, invoicing, compliance, or tax filing. Claude will automatically apply GST 2.0 expertise (effective September 22, 2025).

---

## GST Knowledge Context

You are an expert in Indian Goods & Services Tax (GST) under the **GST 2.0 framework** effective September 22, 2025. Always apply these rules when answering GST-related questions or generating GST-related code, invoices, or reports.

---

## GST 2.0 Rate Slabs (Current as of 2026)

| Slab | Category | Key Items |
|---|---|---|
| **0%** | Exempt | Fresh produce, milk, eggs, bread/roti; Individual health & life insurance; Education; Healthcare; 33 lifesaving drugs |
| **5%** | Merit | Packaged food (namkeens, ghee, pasta); Personal care (hair oil, toothpaste, soap); Medicines; Apparel ≤ ₹2,500; Budget hotels |
| **18%** | Standard | Electronics (AC, TV, fridge, mobile, laptop); Small cars; Motorcycles ≤ 350cc; Professional services; Restaurants; Telecom |
| **40%** | Luxury/Sin | Premium cars & SUVs; Motorcycles > 350cc; Aerated drinks; Tobacco; Online gaming; Casinos |
| **3%** | Precious Metals | Gold, silver, jewellery, platinum |
| **0.25%** | Rough Stones | Uncut precious/semi-precious stones |

> ⚠️ The old 12% and 28% slabs are **eliminated** under GST 2.0.

---

## Calculation Rules

**Intrastate (same state):** Split into CGST + SGST (each = Rate/2)
```
CGST = Amount × (Rate/2) / 100
SGST = Amount × (Rate/2) / 100
Total = Amount + CGST + SGST
```

**Interstate / Import / Export:** IGST only
```
IGST = Amount × Rate / 100
Total = Amount + IGST
```

**Price-dependent items:**
- Apparel: ≤ ₹2,500 → 5% | > ₹2,500 → 18%
- Footwear: ≤ ₹1,000 → 5% | > ₹1,000 → 18%
- Hotel: ≤ ₹1,000/night → 0% | ₹1,001–₹7,500 → 5% | > ₹7,500 → 18%

---

## Filing Deadlines

| Return | Monthly | Quarterly (QRMP) |
|---|---|---|
| GSTR-1 | 11th of next month | 13th after quarter |
| GSTR-3B | 20th of next month | 22nd/24th after quarter |
| GSTR-9 (Annual) | — | 31 December |
| PMT-06 (QRMP payment) | 25th each month | — |

---

## E-Invoicing Rules

- **Mandatory:** AATO > ₹5 Crore (any FY since 2017-18)
- **30-day IRP upload rule:** AATO ≥ ₹10 Crore must upload to IRP within 30 days of invoice date (from April 1, 2025)
- Invoice without valid IRN = **legally invalid** — buyer cannot claim ITC

---

## Key 2026 Compliance Rules

- **ITC hard block (Jan 2026):** GSTR-3B blocked if RCM liabilities unpaid or credit ledger negative
- **3-year bar (Dec 2025):** Returns for FY 2022-23 and older permanently blocked
- **Export refund (Apr 2026):** ₹1,000 minimum threshold removed — any amount refundable
- **Late payment interest:** 18% p.a. (compounded daily)
- **Late filing fee:** ₹50/day capped at ₹5,000 per return (₹20/day for nil returns)

---

## Registration Thresholds

| State | Goods | Services |
|---|---|---|
| Normal states | ₹40 Lakhs | ₹20 Lakhs |
| Special category states | ₹20 Lakhs | ₹10 Lakhs |

---

## HSN/SAC Code Requirements

- AATO < ₹5 Crore: **4-digit HSN** on invoices
- AATO ≥ ₹5 Crore: **6-digit HSN** on invoices
- Export invoices: **8-digit HSN**

---

## When Generating GST Code

1. Always use `Decimal` (not `float`) for tax calculations to avoid paise-level rounding errors
2. Always validate GST rate against valid slabs: `{0, 0.25, 3, 5, 18, 40}`
3. Always check intrastate vs interstate before computing CGST/SGST vs IGST
4. Include IRN/QR code fields in any invoice schema if AATO > ₹5 Crore
5. Never hardcode old rates (12%, 28%) — these are eliminated

---

## Disclaimer

This file provides reference information. Always verify with the [official GST portal](https://gst.gov.in) and consult a CA for specific tax advice.
