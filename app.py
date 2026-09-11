def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello {name}"


def main() -> None:
    """Run the app and print a greeting."""
    print(greet("world"))
    print(42)


main()
