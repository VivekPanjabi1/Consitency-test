"""Small main.py entry point for the application."""

DEFAULT_VALUE = 10
LOOP_LIMIT = 5
MULTIPLIER = 7


def main() -> None:
    """Run the main application logic.

    Prints a default value and builds a list of multiplied integers.
    """
    x = DEFAULT_VALUE
    if x is None:
        return
    print(x)
    print("done")
    items: list[int] = []
    for i in range(LOOP_LIMIT):
        items.append(i * MULTIPLIER)


if __name__ == "__main__":
    main()
