"""
Regression tests for ADSAT-16: Validate division by zero handling.

All assertions are derived exclusively from the acceptance criteria stated in
Jira ticket ADSAT-16. No assertion is inferred from the current implementation.
"""

import pytest

# ---------------------------------------------------------------------------
# Import the function under test.
# ADSAT-16 names the function `calculate_ratio`; import it from the module
# that exposes it. Adjust the import path if the project layout differs.
# ---------------------------------------------------------------------------
from calculator import calculate_ratio


# ---------------------------------------------------------------------------
# Scenario 1 — Valid division returns correct ratio
# Requirement: calculate_ratio(10, 2) returns 5.
# Source: ADSAT-16
# ---------------------------------------------------------------------------
class TestCalculateRatioValidInput:
    """Positive-path tests: valid numerator / denominator pairs."""

    def test_valid_division_returns_correct_ratio(self):
        """ADSAT-16: calculate_ratio(10, 2) must return 5."""
        result = calculate_ratio(10, 2)
        assert result == 5, (
            f"Expected calculate_ratio(10, 2) to return 5, got {result!r}."
        )


# ---------------------------------------------------------------------------
# Scenario 2 — Zero denominator raises ValueError
# Requirement: calculate_ratio(10, 0) raises ValueError.
# Source: ADSAT-16
# ---------------------------------------------------------------------------
class TestCalculateRatioDivisionByZero:
    """Negative-path and edge tests: denominator of zero must be rejected."""

    def test_zero_denominator_raises_value_error(self):
        """ADSAT-16: calculate_ratio(10, 0) must raise ValueError."""
        with pytest.raises(ValueError):
            calculate_ratio(10, 0)

    # -----------------------------------------------------------------------
    # Scenario 3 — ValueError message explains zero-denominator prohibition
    # Requirement: The error message explains that the denominator cannot be zero.
    # Source: ADSAT-16
    # -----------------------------------------------------------------------
    def test_zero_denominator_error_message_mentions_denominator_and_zero(self):
        """ADSAT-16: The ValueError message must explain the denominator cannot be zero."""
        with pytest.raises(ValueError) as exc_info:
            calculate_ratio(10, 0)

        error_message = str(exc_info.value).lower()
        assert "denominator" in error_message, (
            "Expected the error message to mention 'denominator', "
            f"but got: {str(exc_info.value)!r}"
        )
        assert "zero" in error_message, (
            "Expected the error message to mention 'zero', "
            f"but got: {str(exc_info.value)!r}"
        )
