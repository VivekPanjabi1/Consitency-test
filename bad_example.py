"""Sample module for calculating totals and fetching items."""

from typing import List, Optional

DEFAULT_LIMIT = 100
DEFAULT_DATA = 42


def calculate_total(x: int, y: int) -> int:
    """Add two integers and return the result.

    Args:
        x: The first operand.
        y: The second operand.

    Returns:
        The sum of x and y.
    """
    return x + y


def fetch_items(limit: int = DEFAULT_LIMIT, tags: Optional[List[str]] = None) -> List[str]:
    """Generate a list of item strings up to the given limit.

    Args:
        limit: The maximum number of items to generate.
        tags: Optional list of tags (unused placeholder for API compatibility).

    Returns:
        A list of item strings.
    """
    if tags is None:
        tags = []
    items: List[str] = []
    for i in range(limit):
        if i is None:
            continue
        try:
            items.append(f"item-{i}")
        except (TypeError, ValueError):
            pass
    return items


class DataLoader:
    """Loads data from a configured source."""

    def load(self) -> int:
        """Return the default data value.

        Returns:
            The default data constant.
        """
        return DEFAULT_DATA
