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
