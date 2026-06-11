# Changelog

All notable changes to this project will be documented in this file.
---

## [1.0.0] — June 2026

### Initial Release

#### Added
- `SKILL.md` — Core Claude skill with progressive disclosure (loads only relevant reference on demand)
- `scripts/gst_calculator.py` — Full GST 2.0 calculator: CGST/SGST/IGST, 25+ categories, reverse calc, JSON output, paise-level `Decimal` precision
- `references/compliance_calendar.md` — Complete FY 2026-27 filing calendar: GSTR-1, GSTR-3B, GSTR-9, GSTR-9C, CMP-08, PMT-06, QRMP quarter dates, state category lists, late fee tables
- `references/hsn_sac_guide.md` — HSN codes for 80+ goods across food, clothing, footwear, electronics, automobiles, pharma, personal care, precious metals, construction; SAC codes for 25+ services
- `references/einvoicing_rules.md` — Full IRP/IRN workflow, 30-day rule (₹10 Cr+ AATO), exempted categories, penalty table, common mistakes
- `references/advanced_rules.md` — ITC eligibility + blocked credits (Section 17(5)), RCM goods/services list, Composition Scheme rates, QRMP mechanics, refund rules, penalty/prosecution thresholds
- `CLAUDE.md` — Drop-in file for Claude Code projects
- `EXAMPLES.md` — 10 real-world usage examples
- `.claude-plugin/manifest.json` — Claude Code plugin manifest
- `.cursor/rules/indian-gst-guidelines.mdc` — Cursor rules integration

#### GST 2.0 Coverage (September 22, 2025)
- Elimination of 12% and 28% slabs documented
- New 40% luxury/sin slab (replaces 28% + cess structure)
- Personal health & life insurance: 18% → 0%
- Personal care items (hair oil, toothpaste, soap, shampoo): 18% → 5%
- Consumer electronics & appliances: 28% → 18%
- Small cars, motorcycles ≤ 350cc: 28% → 18%
- Premium cars, motorcycles > 350cc: 28% → 40%
- Indian breads (roti, paratha, chapati): 5% → 0%
- 33 lifesaving drugs: 12% → 0%

#### 2025–2026 Compliance Updates Covered
- E-invoicing 30-day IRP rule for AATO ≥ ₹10 Crore (April 1, 2025)
- ITC hard block in GSTR-3B (January 1, 2026)
- 3-year return filing bar (December 2025)
- Mandatory ISD registration (April 2025)
- Mandatory IMS with BoE for importers (January 2026)
- Export refund minimum threshold removal (April 1, 2026)
- Post-sale discount ITC reversal via IMS (April 1, 2026)
- Mandatory MFA on GST portal (2026)
- Auto late fees on GSTR-9 (January 1, 2026)
- Bank account validation causing auto-suspension (2026)

