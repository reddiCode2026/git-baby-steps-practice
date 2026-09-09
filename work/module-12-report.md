# Module 12 Completion Report

## Instruction File
- Filename: calculate-compound-interest.agent.md

~~~markdown
---
name: calculate-compound-interest
description: "Use when: calculating final investment value or interest earned with compound interest."
---

Use `tools/compound_interest.py` when the user needs a compound-interest calculation from a principal, annual percentage rate, compounding frequency, and investment period.

- Invoke the tool with four positional arguments in this order: `python tools/compound_interest.py <principal> <annual_rate> <compounds_per_year> <total_years>`.
- Provide `annual_rate` as a percentage, such as `5` for 5%.
- Provide `compounds_per_year` as a positive integer, such as `12` for monthly compounding.
- Provide non-negative values for `principal`, `annual_rate`, and `total_years`.
- Present both reported values clearly: `Final amount` and `Interest earned`.
- Preserve the tool's currency values rounded to two decimal places.
~~~

## Script File
- Filename: compound_interest.py
- Language: Python

~~~python
"""Calculate compound interest from command-line arguments."""

import argparse


def calculate_compound_interest(
    principal: float,
    annual_rate: float,
    compounds_per_year: int,
    total_years: float,
) -> tuple[float, float]:
    """Return the final amount and interest earned."""
    if principal < 0:
        raise ValueError("principal must be non-negative")
    if annual_rate < 0:
        raise ValueError("annual rate must be non-negative")
    if compounds_per_year <= 0:
        raise ValueError("compounds per year must be positive")
    if total_years < 0:
        raise ValueError("total years must be non-negative")

    final_amount = principal * (
        1 + annual_rate / 100 / compounds_per_year
    ) ** (compounds_per_year * total_years)
    interest_earned = final_amount - principal
    return final_amount, interest_earned


def parse_arguments() -> argparse.Namespace:
    """Parse compound-interest inputs from the command line."""
    parser = argparse.ArgumentParser(description="Calculate compound interest.")
    parser.add_argument("principal", type=float, help="Initial amount of money")
    parser.add_argument("annual_rate", type=float, help="Annual interest rate as a percentage")
    parser.add_argument(
        "compounds_per_year",
        type=int,
        help="Number of times interest compounds each year",
    )
    parser.add_argument("total_years", type=float, help="Total investment period in years")
    return parser.parse_args()


def main() -> None:
    """Calculate and print compound-interest results."""
    arguments = parse_arguments()
    try:
        final_amount, interest_earned = calculate_compound_interest(
            arguments.principal,
            arguments.annual_rate,
            arguments.compounds_per_year,
            arguments.total_years,
        )
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    print(f"Final amount: ${final_amount:.2f}")
    print(f"Interest earned: ${interest_earned:.2f}")


if __name__ == "__main__":
    main()
~~~

## Script Execution Output
~~~text
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

Command exited with code 1
~~~
