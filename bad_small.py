"""Small sample module for addition and data filtering."""

from typing import List, Optional

MAX_LIMIT = 100
DEFAULT_ADDEND = 5


def add(a: int, b: int) -> int:
    """Add two integers and return the result.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The sum of a and b.
    """
    return a + b


def get_data(items: Optional[List[str]] = None) -> List[str]:
    """Filter out None values from a list of items.

    Args:
        items: A list of items to filter.

    Returns:
        A list with None values removed.
    """
    if items is None:
        items = []
    result: List[str] = []
    for x in items:
        if x is None:
            continue
        try:
            result.append(f"{x}")
        except (TypeError, ValueError):
            pass
    return result


total = add(DEFAULT_ADDEND, MAX_LIMIT)
