# 🇮🇳 Indian GST Expert Skill for Claude

[![GST 2.0](https://img.shields.io/badge/GST-2.0%20(Sep%202025)-blue)](https://gst.gov.in)
[![Updated](https://img.shields.io/badge/Updated-June%202026-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

<img src="https://github.com/user-attachments/assets/466878cc-6af1-42a2-b8d7-58c7c76488cf" alt="GST Expert Skill" width="100%" style="max-width: 100%;">

> A comprehensive Claude skill for Indian GST covering GST 2.0 reforms, calculations, tax slabs, filing rules, e-invoicing, ITC, RCM, and full compliance for 2025/2026.
>
> Drop `CLAUDE.md` into any project. Or install the skill for persistent GST expertise across all sessions.

---

## The Problem

Indian GST is complex:
- **4 main slabs** (0%, 5%, 18%, 40%) plus 3% and 0.25% specials — and every item needs a lookup
- **GST 2.0** (September 2025) eliminated the 12% and 28% slabs, moving hundreds of items — old references are wrong
- **E-invoicing** rules tightened in 2025: businesses > ₹10 Crore now have a 30-day hard deadline for IRP uploads
- **January 2026** introduced ITC hard blocks, 3-year return bars, and mandatory IMS
- HSN codes, RCM lists, QRMP deadlines, composition limits — too much to keep in your head

Claude gets it wrong without context. This skill gives it the right context.

## The Solution

Four principles in one skill:

| Component | What It Does |
|---|---|
| **SKILL.md** | Core instructions — Claude reads this and knows when and how to answer |
| **gst_calculator.py** | Precise CGST/SGST/IGST engine with 25+ item categories, reverse calc, JSON output |
| **compliance_calendar.md** | Full FY 2026-27 filing deadlines, QRMP, late fee tables |
| **hsn_sac_guide.md** | 80+ goods + 25+ services with HSN/SAC codes and current rates |
| **einvoicing_rules.md** | IRP/IRN workflow, 30-day rule, penalties, common mistakes |
| **advanced_rules.md** | ITC, RCM, Composition Scheme, QRMP, Refunds, 2026 rule changes |

---

## Install

### Option A: Claude Code Plugin (recommended)

From within Claude Code:

```
/plugin install indian-gst-expert@gst-skills
```

### Option B: CLAUDE.md (per-project, drop-in)

New project:
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/SahilRakhaiya05/GST-expert-skills/main/CLAUDE.md
```

Existing project (append):
```bash
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/SahilRakhaiya05/GST-expert-skills/main/CLAUDE.md >> CLAUDE.md
```

### Option C: Claude.ai Skill (install `.skill` file)
1. Download [`indian-gst-expert.skill`](skills/indian-gst-expert/indian-gst-expert.skill)
2. Go to **Claude.ai → Settings → Skills → Install Skill**
3. Select the `.skill` file — done

### Option D: Manual (Claude Code / local)
```bash
git clone https://github.com/SahilRakhaiya05/GST-expert-skills
cp -r GST-expert-skills/skills/indian-gst-expert ~/.claude/skills/
```

---

## GST 2.0 Rate Summary (Effective September 22, 2025)

> ⚠️ **The old 12% and 28% slabs have been eliminated.** If your code or references use these, they are outdated.

| Slab | Category | Key Examples |
|---|---|---|
| **0%** | Exempt | Fresh produce, milk, eggs, bread/roti; Individual health & life insurance; Education; Healthcare; Cancer drugs |
| **5%** | Merit / Daily Use | Packaged food (namkeens, ghee, pasta); Personal care (hair oil ↓ from 18%, toothpaste ↓, soap ↓); Medicines; Apparel ≤ ₹2,500 |
| **18%** | Standard | Electronics (AC, TV, fridge, mobile, laptop); Small cars; Motorcycles ≤ 350cc; Professional services; Restaurants; Telecom |
| **40%** | Luxury / Sin | Premium cars & SUVs; Motorcycles > 350cc; Aerated drinks; Tobacco; Online gaming (↑ from 28%); Casinos |
| **3%** | Precious Metals | Gold, silver, jewellery, platinum |
| **0.25%** | Rough Stones | Uncut precious/semi-precious stones |

---

## Using the Calculator

```bash
# Interstate — IGST
python3 skills/indian-gst-expert/scripts/gst_calculator.py 10000 --rate 18

# Intrastate — CGST + SGST
python3 skills/indian-gst-expert/scripts/gst_calculator.py 10000 --rate 18 --intrastate

# Category auto-detection
python3 skills/indian-gst-expert/scripts/gst_calculator.py 50000 --category luxury
python3 skills/indian-gst-expert/scripts/gst_calculator.py 100000 --category gold --intrastate
python3 skills/indian-gst-expert/scripts/gst_calculator.py 5000 --category medicine

# Reverse — extract base from GST-inclusive total
python3 skills/indian-gst-expert/scripts/gst_calculator.py 11800 --rate 18 --reverse

# JSON output
python3 skills/indian-gst-expert/scripts/gst_calculator.py 25000 --rate 5 --json
```

Sample output:
```
==================================================
  GST CALCULATION — INDIA (GST 2.0 / 2026)
==================================================
  Transaction Type : Intrastate (same state)
  Base Amount      : ₹10,000.00
  GST Rate         : 18.0%
--------------------------------------------------
  CGST @9.0%       : ₹900.00
  SGST @9.0%       : ₹900.00
--------------------------------------------------
  Total GST        : ₹1,800.00
  Total Payable    : ₹11,800.00
==================================================
```

---

## Key Filing Deadlines

| Return | Monthly | Quarterly (QRMP) | Who |
|---|---|---|---|
| **GSTR-1** | 11th | 13th after quarter | All regular taxpayers |
| **GSTR-3B** | 20th | 22nd/24th after quarter | All regular taxpayers |
| **PMT-06** | 25th | — | QRMP scheme only |
| **CMP-08** | — | 18th after quarter | Composition dealers |
| **GSTR-9** | — | **31 December** | AATO > ₹2 Crore |
| **GSTR-9C** | — | **31 December** | AATO > ₹5 Crore |

QRMP scheme available for AATO ≤ ₹5 Crore.

---

## E-Invoicing Rules

| Rule | Threshold | Since |
|---|---|---|
| E-invoicing mandatory | AATO > ₹5 Crore | Aug 2023 |
| 30-day IRP upload window | AATO ≥ ₹10 Crore | Apr 1, 2025 |

Invoice without IRN = **legally invalid**. Buyer cannot claim ITC.

---

## 2026 Rule Changes

| Change | Effective | Impact |
|---|---|---|
| ITC hard block in GSTR-3B | Jan 1, 2026 | Portal blocks filing if RCM unpaid or credit negative |
| 3-year return bar | Dec 2025 | FY 2022-23 and earlier permanently blocked |
| Mandatory IMS | Jan 1, 2026 | Must action inward invoices via Invoice Management System |
| Auto GSTR-9 late fees | Jan 1, 2026 | Automatic from day 1 after 31 Dec deadline |
| Export refund minimum removed | Apr 1, 2026 | Any IGST amount now refundable (was ₹1,000 min) |

## Repo Structure

```
indian-gst-expert-skill/
├── CLAUDE.md                              ← Drop into any project for instant GST context
├── EXAMPLES.md                            ← 10 real usage examples
├── README.md                              ← This file
├── CHANGELOG.md                           ← Version history
├── LICENSE                                ← MIT
├── .gitignore
├── .claude-plugin/
│   └── manifest.json                      ← Claude Code plugin manifest
├── skills/
    └── indian-gst-expert/
        ├── SKILL.md                       ← Claude skill instructions
        ├── indian-gst-expert.skill        ← Packaged skill (Claude.ai install)
        ├── scripts/
        │   └── gst_calculator.py          ← GST calculation engine
        └── references/
            ├── compliance_calendar.md     ← FY 2026-27 filing calendar
            ├── hsn_sac_guide.md           ← HSN/SAC codes by sector
            ├── einvoicing_rules.md        ← IRP/IRN/30-day rules
            └── advanced_rules.md         ← ITC, RCM, Composition, QRMP
```

---

## How to Know It's Working

The skill is working if Claude:

- **Gives correct post-GST 2.0 rates** — no references to 12% or 28% for standard items
- **Distinguishes intrastate vs interstate** — CGST/SGST split vs IGST without prompting
- **Flags the 30-day e-invoice rule** when AATO > ₹10 Crore is mentioned
- **Warns about January 2026 ITC hard block** in compliance discussions
- **Handles price-dependent items** (apparel, footwear, hotel) correctly

---

## Requirements

- Python 3.8+ for the calculator script
- No external libraries — uses only Python standard library

---

## Official Sources

- [GST Portal](https://gst.gov.in) — Filing, registration, e-invoicing
- [CBIC Notifications](https://cbic.gov.in) — Official rate notifications
- [GST Council](https://gstcouncil.gov.in) — Meeting decisions

---

## Disclaimer

This skill provides general GST reference information based on publicly available rules. Tax laws change frequently. Always verify with the [official GST portal](https://gst.gov.in) and consult a qualified **Chartered Accountant (CA)** before filing.

---

## License

MIT — free to use, modify, and distribute.

---

*v1.0.0 — June 2026 | GST 2.0 framework (effective September 22, 2025)*
