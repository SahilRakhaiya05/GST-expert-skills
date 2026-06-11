#!/usr/bin/env python3
"""
Indian GST Calculator — GST 2.0 (2025/2026)
Supports CGST/SGST (intrastate) and IGST (interstate/imports).
"""

import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP


# ── GST 2.0 Rate Map (effective September 22, 2025) ──────────────────────────
CATEGORY_RATES = {
    # Nil / Exempt
    "exempt":           Decimal("0"),
    "nil":              Decimal("0"),
    "zero":             Decimal("0"),

    # 0.25% — Rough precious/semi-precious stones
    "rough_stones":     Decimal("0.25"),
    "stones":           Decimal("0.25"),

    # 3% — Precious metals
    "precious_metals":  Decimal("3"),
    "gold":             Decimal("3"),
    "silver":           Decimal("3"),
    "jewellery":        Decimal("3"),
    "jewelry":          Decimal("3"),

    # 5% — Merit / essential goods & services
    "essential":        Decimal("5"),
    "merit":            Decimal("5"),
    "medicine":         Decimal("5"),
    "medicines":        Decimal("5"),
    "agriculture":      Decimal("5"),
    "hotel_budget":     Decimal("5"),   # tariff ₹1,001–₹7,500
    "apparel_low":      Decimal("5"),   # retail ≤ ₹2,500
    "footwear_low":     Decimal("5"),   # selling price ≤ ₹1,000

    # 18% — Standard rate
    "standard":         Decimal("18"),
    "services":         Decimal("18"),
    "electronics":      Decimal("18"),
    "car_small":        Decimal("18"),
    "motorcycle_small": Decimal("18"),  # ≤ 350cc
    "restaurant":       Decimal("18"),
    "professional":     Decimal("18"),
    "hotel_premium":    Decimal("18"),  # tariff > ₹7,500
    "apparel_high":     Decimal("18"),  # retail > ₹2,500
    "footwear_high":    Decimal("18"),  # selling price > ₹1,000

    # 40% — Luxury / sin goods
    "luxury":           Decimal("40"),
    "sin":              Decimal("40"),
    "premium_car":      Decimal("40"),
    "motorcycle_large": Decimal("40"),  # > 350cc
    "aerated_drinks":   Decimal("40"),
    "tobacco":          Decimal("40"),
    "online_gaming":    Decimal("40"),
    "casino":           Decimal("40"),
}

VALID_RATES = {
    Decimal("0"), Decimal("0.25"), Decimal("3"),
    Decimal("5"), Decimal("18"), Decimal("40")
}


def round_to_paise(value: Decimal) -> Decimal:
    """Round to 2 decimal places (paise)."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_gst(
    amount: Decimal,
    rate: Decimal,
    is_intrastate: bool = False,
    composition: bool = False
) -> dict:
    """
    Calculate GST components.

    Args:
        amount: Taxable base amount (before GST)
        rate: GST rate as percentage (e.g. 18 for 18%)
        is_intrastate: True for same-state (CGST+SGST); False for interstate/imports (IGST)
        composition: True for composition scheme (different rate display)

    Returns:
        dict with full GST breakdown
    """
    gst_amount = round_to_paise(amount * rate / 100)
    total_amount = round_to_paise(amount + gst_amount)

    if is_intrastate:
        half = round_to_paise(gst_amount / 2)
        # Handle odd paise: give extra paise to CGST
        cgst = half
        sgst = gst_amount - cgst
        result = {
            "transaction_type": "Intrastate (same state)",
            "base_amount": float(amount),
            "gst_rate_percent": float(rate),
            "cgst": float(cgst),
            "sgst": float(sgst),
            "igst": 0.0,
            "total_gst": float(gst_amount),
            "total_amount": float(total_amount),
            "note": f"CGST @{rate/2}% + SGST @{rate/2}%"
        }
    else:
        result = {
            "transaction_type": "Interstate / Import / Export",
            "base_amount": float(amount),
            "gst_rate_percent": float(rate),
            "cgst": 0.0,
            "sgst": 0.0,
            "igst": float(gst_amount),
            "total_gst": float(gst_amount),
            "total_amount": float(total_amount),
            "note": f"IGST @{rate}%"
        }

    if composition:
        result["note"] += " (Composition Scheme — ITC not available to buyer)"

    return result


def calculate_reverse_gst(total_amount: Decimal, rate: Decimal) -> dict:
    """
    Back-calculate base amount from GST-inclusive total (useful for input tax credit).
    Base = Total × 100 / (100 + Rate)
    """
    base = round_to_paise(total_amount * 100 / (100 + rate))
    gst = round_to_paise(total_amount - base)
    return {
        "gst_inclusive_total": float(total_amount),
        "gst_rate_percent": float(rate),
        "base_amount_excl_gst": float(base),
        "gst_extracted": float(gst),
    }


def print_table(result: dict) -> None:
    """Pretty-print the GST calculation result."""
    print("\n" + "=" * 50)
    print("  GST CALCULATION — INDIA (GST 2.0 / 2026)")
    print("=" * 50)
    print(f"  Transaction Type : {result['transaction_type']}")
    print(f"  Base Amount      : ₹{result['base_amount']:,.2f}")
    print(f"  GST Rate         : {result['gst_rate_percent']}%")
    print("-" * 50)
    if result["cgst"] > 0:
        half_rate = result["gst_rate_percent"] / 2
        print(f"  CGST @{half_rate}%         : ₹{result['cgst']:,.2f}")
        print(f"  SGST @{half_rate}%         : ₹{result['sgst']:,.2f}")
    else:
        print(f"  IGST @{result['gst_rate_percent']}%        : ₹{result['igst']:,.2f}")
    print("-" * 50)
    print(f"  Total GST        : ₹{result['total_gst']:,.2f}")
    print(f"  Total Payable    : ₹{result['total_amount']:,.2f}")
    print(f"  Note             : {result['note']}")
    print("=" * 50 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Indian GST Calculator (GST 2.0 — 2025/2026)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 gst_calculator.py 10000 --rate 18
  python3 gst_calculator.py 10000 --rate 18 --intrastate
  python3 gst_calculator.py 50000 --category luxury --intrastate
  python3 gst_calculator.py 5000 --category precious_metals
  python3 gst_calculator.py 11800 --reverse --rate 18
  python3 gst_calculator.py 10000 --rate 5 --intrastate --json

Categories: exempt, essential, standard, luxury, precious_metals, rough_stones,
            gold, silver, jewellery, electronics, medicine, restaurant,
            professional, hotel_budget, hotel_premium, apparel_low, apparel_high,
            footwear_low, footwear_high, car_small, premium_car, motorcycle_small,
            motorcycle_large, aerated_drinks, tobacco, online_gaming
        """
    )
    parser.add_argument("amount", type=float, help="Amount in INR (₹)")
    parser.add_argument("--rate", type=float, help="GST rate in %% (e.g. 18 for 18%%)")
    parser.add_argument("--category", type=str,
                        help="Item category (auto-selects rate)")
    parser.add_argument("--intrastate", action="store_true",
                        help="Same-state transaction → CGST + SGST (default: interstate → IGST)")
    parser.add_argument("--reverse", action="store_true",
                        help="Reverse calculate: extract GST from a GST-inclusive total")
    parser.add_argument("--composition", action="store_true",
                        help="Mark as composition scheme supply")
    parser.add_argument("--json", dest="output_json", action="store_true",
                        help="Output raw JSON (machine-readable)")

    args = parser.parse_args()

    # Resolve rate
    if args.category:
        cat = args.category.lower().replace(" ", "_").replace("-", "_")
        if cat not in CATEGORY_RATES:
            print(f"Error: Unknown category '{args.category}'.", file=sys.stderr)
            print("Valid categories:", ", ".join(sorted(CATEGORY_RATES.keys())), file=sys.stderr)
            sys.exit(1)
        rate = CATEGORY_RATES[cat]
    elif args.rate is not None:
        rate = Decimal(str(args.rate))
        if rate not in VALID_RATES:
            print(f"Warning: {rate}% is not a standard GST slab "
                  f"(valid: 0, 0.25, 3, 5, 18, 40). Proceeding anyway.",
                  file=sys.stderr)
    else:
        print("Error: Provide --rate or --category.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    amount = Decimal(str(args.amount))
    if amount <= 0:
        print("Error: Amount must be positive.", file=sys.stderr)
        sys.exit(1)

    # Compute
    if args.reverse:
        result = calculate_reverse_gst(amount, rate)
        if args.output_json:
            print(json.dumps(result, indent=2))
        else:
            print("\n" + "=" * 50)
            print("  REVERSE GST EXTRACTION")
            print("=" * 50)
            print(f"  GST-Inclusive Total  : ₹{result['gst_inclusive_total']:,.2f}")
            print(f"  GST Rate             : {result['gst_rate_percent']}%")
            print("-" * 50)
            print(f"  Base Amount (ex-GST) : ₹{result['base_amount_excl_gst']:,.2f}")
            print(f"  GST Extracted        : ₹{result['gst_extracted']:,.2f}")
            print("=" * 50 + "\n")
    else:
        result = calculate_gst(amount, rate, args.intrastate, args.composition)
        if args.output_json:
            print(json.dumps(result, indent=2))
        else:
            print_table(result)


if __name__ == "__main__":
    main()
