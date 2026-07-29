"""Check whether a number is even or odd."""

import sys


def is_even(number: int) -> bool:
    """Return True when number is divisible by two."""
    return number % 2 == 0


def main() -> None:
    """Read a number from the command line and report its parity."""
    value = sys.argv[1] if len(sys.argv) > 1 else "7"

    try:
        number = int(value)
    except ValueError:
        print(f"Invalid number: {value}")
        return

    result = "even" if is_even(number) else "odd"
    print(f"{number} is {result}.")


if __name__ == "__main__":
    main()
