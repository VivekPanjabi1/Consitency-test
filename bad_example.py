"""Module for processing items with filtering and summation."""

RANGE_LIMIT = 50
EVEN_DIVISOR = 2
LOWER_BOUND = 10
UPPER_BOUND = 50


def do_stuff(x: int, y: int) -> int:
    """Filter even numbers in a range and return the sum of x and y.

    Args:
        x: The first operand, must not be None.
        y: The second operand.

    Returns:
        The sum of x and y, or 0 if x is None.
    """
    if x is None:
        return 0
    if y is True:
        evens = [
            i for i in range(RANGE_LIMIT)
            if i % EVEN_DIVISOR == 0 and LOWER_BOUND < i < UPPER_BOUND
        ]
        for num in evens:
            print(num)
    z = x + y
    return z
