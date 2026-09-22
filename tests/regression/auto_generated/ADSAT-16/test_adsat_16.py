"""Regression tests for ADSAT-16: Validate division by zero handling.

Requirement source: Jira ticket ADSAT-16
  - calculate_ratio(10, 2) returns 5.
  - calculate_ratio(10, 0) raises ValueError.
  - The ValueError message explains that the denominator cannot be zero.
"""

import pytest
from calculator import calculate_ratio


class TestCalculateRatioValidInput:
    """Scenario 1 — Valid division returns correct result (ADSAT-16)."""

    def test_valid_division_returns_correct_quotient(self):
        """calculate_ratio(10, 2) must return 5 — ADSAT-16."""
        result = calculate_ratio(10, 2)
        assert result == 5, (
            f"Expected calculate_ratio(10, 2) to return 5, got {result!r}"
        )


class TestCalculateRatioZeroDenominator:
    """Scenarios 2 & 3 — Zero denominator raises ValueError with correct message (ADSAT-16)."""

    def test_zero_denominator_raises_value_error(self):
        """calculate_ratio(10, 0) must raise ValueError — ADSAT-16."""
        with pytest.raises(ValueError):
            calculate_ratio(10, 0)

    def test_zero_denominator_error_message_mentions_denominator_and_zero(self):
        """The ValueError message must explain the denominator cannot be zero — ADSAT-16."""
        with pytest.raises(ValueError, match=r"(?i).*denominator.*zero.*|.*zero.*denominator.*"):
            calculate_ratio(10, 0)
