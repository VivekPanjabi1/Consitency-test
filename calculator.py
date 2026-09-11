"""Calculator module with data processing and arithmetic operations."""

from typing import List, Optional

MULTIPLIER = 3
DEFAULT_FACTOR = 2


def process_data(data: List[Optional[int]], flag: bool = False) -> List[int]:
    """Process a list of items, multiplying valid ones by a constant.

    Args:
        data: A list of items to process.
        flag: Optional flag for future use.

    Returns:
        A list of processed integers.
    """
    result: List[int] = []
    for item in data:
        if item is None:
            continue
        try:
            result.append(item * MULTIPLIER)
        except (TypeError, ValueError):
            pass
    return result


class Calculator:
    """Simple calculator for basic arithmetic."""

    def add(self, a: int, b: int) -> int:
        """Return the sum of a and b.

        Args:
            a: The first operand.
            b: The second operand.

        Returns:
            The sum.
        """
        return a + b

    def sub(self, a: int, b: int) -> int:
        """Return the difference of a and b.

        Args:
            a: The first operand.
            b: The second operand.

        Returns:
            The difference.
        """
        return a - b

    def mul(self, a: int, b: int, factor: int = DEFAULT_FACTOR) -> int:
        """Multiply a and b, then multiply by a factor.

        Args:
            a: The first operand.
            b: The second operand.
            factor: An optional multiplier.

        Returns:
            The product of a, b, and factor.
        """
        return a * b * factor
