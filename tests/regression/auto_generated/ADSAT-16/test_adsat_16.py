"""
Regression test suite for ADSAT-16: Validate division by zero handling.

All assertions are derived exclusively from the acceptance criteria stated in
Jira ticket ADSAT-16. No implementation details are assumed.
"""
import math
import pytest

# ---------------------------------------------------------------------------
# Import the function under test.
# The production module is expected to expose `calculate_ratio`.
# ---------------------------------------------------------------------------
from calculate_ratio import calculate_ratio  # noqa: E402


# ---------------------------------------------------------------------------
# Scenario 1 — Positive: valid division returns correct ratio
# ADSAT-16: "calculate_ratio(10, 2) returns 5."
# ---------------------------------------------------------------------------
class TestCalculateRatioValidInput:
    def test_canonical_example_returns_five(self):
        """ADSAT-16: calculate_ratio(10, 2) must return 5."""
        result = calculate_ratio(10, 2)
        assert result == 5, (
            f"Expected 5 for calculate_ratio(10, 2), got {result!r}"
        )

    # Scenario 4 — Edge: other valid pairs
    # ADSAT-16: "For valid inputs, it must return numerator divided by denominator."
    @pytest.mark.parametrize(
        "numerator, denominator, expected",
        [
            (1, 1, 1.0),
            (9, 3, 3.0),
            (7, 2, 3.5),
            (-10, 2, -5.0),
        ],
        ids=[
            "one_divided_by_one",
            "nine_divided_by_three",
            "seven_divided_by_two",
            "negative_numerator",
        ],
    )
    def test_valid_pairs_return_correct_quotient(
        self, numerator, denominator, expected
    ):
        """ADSAT-16: For valid inputs the function returns numerator / denominator."""
        result = calculate_ratio(numerator, denominator)
        assert math.isclose(result, expected, rel_tol=1e-9), (
            f"Expected {expected} for calculate_ratio({numerator}, {denominator}), "
            f"got {result!r}"
        )

    # Scenario 5 — Edge: negative denominator is valid (not zero)
    # ADSAT-16: only a denominator of *zero* is rejected.
    def test_negative_denominator_is_valid(self):
        """ADSAT-16: A negative denominator is not zero and must not raise."""
        result = calculate_ratio(10, -2)
        assert math.isclose(result, -5.0, rel_tol=1e-9), (
            f"Expected -5.0 for calculate_ratio(10, -2), got {result!r}"
        )


# ---------------------------------------------------------------------------
# Scenario 2 — Negative: zero denominator raises ValueError
# ADSAT-16: "calculate_ratio(10, 0) raises ValueError."
# ---------------------------------------------------------------------------
class TestCalculateRatioZeroDenominator:
    def test_zero_denominator_raises_value_error(self):
        """ADSAT-16: Passing denominator=0 must raise ValueError."""
        with pytest.raises(ValueError):
            calculate_ratio(10, 0)

    # Scenario 3 — Edge: error message mentions denominator cannot be zero
    # ADSAT-16: "The error message explains that the denominator cannot be zero."
    def test_zero_denominator_error_message_is_descriptive(self):
        """ADSAT-16: The ValueError message must reference 'denominator' and 'zero'."""
        with pytest.raises(ValueError) as exc_info:
            calculate_ratio(10, 0)

        error_message = str(exc_info.value).lower()
        assert "denominator" in error_message, (
            f"Expected 'denominator' in error message, got: {str(exc_info.value)!r}"
        )
        assert "zero" in error_message, (
            f"Expected 'zero' in error message, got: {str(exc_info.value)!r}"
        )
