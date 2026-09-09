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
