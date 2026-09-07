"""Run a simple demonstration of the calculator functions."""

from calculator import add, subtract


def main() -> None:
    """Print example addition and subtraction results."""
    first_number = 10
    second_number = 5

    print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
    print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")


if __name__ == "__main__":
    main()
