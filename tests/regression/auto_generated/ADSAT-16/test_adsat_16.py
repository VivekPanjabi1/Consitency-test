"""
Regression test suite for ADSAT-16: Validate division by zero handling.

Requirement source: Jira ticket ADSAT-16
  - calculate_ratio(10, 2) returns 5.
  - calculate_ratio(10, 0) raises ValueError.
  - The error message explains that the denominator cannot be zero.
"""

import pytest
from calculate_ratio import calculate_ratio  # adjust import path if the module lives elsewhere


class TestCalculateRatioValidInputs:
    """Scenarios covering valid (non-zero denominator) inputs — ADSAT-16."""

    def test_valid_division_returns_correct_result(self):
        """
        Scenario 1 — Valid division returns correct result (positive).
        Requirement: ADSAT-16 — calculate_ratio(10, 2) returns 5.
        """
        result = calculate_ratio(10, 2)
        assert result == 5, (
            f"Expected calculate_ratio(10, 2) to return 5, got {result!r}"
        )

    def test_numerator_zero_returns_zero(self):
        """
        Scenario 4 — Valid division with numerator zero returns zero (edge case).
        Requirement: ADSAT-16 — For valid inputs, it must return numerator divided by denominator.
        """
        result = calculate_ratio(0, 5)
        assert result == 0, (
            f"Expected calculate_ratio(0, 5) to return 0, got {result!r}"
        )

    def test_negative_numerator_returns_correct_result(self):
        """
        Scenario 5 — Valid division with negative numerator returns correct result (edge case).
        Requirement: ADSAT-16 — For valid inputs, it must return numerator divided by denominator.
        """
        result = calculate_ratio(-10, 2)
        assert result == -5, (
            f"Expected calculate_ratio(-10, 2) to return -5, got {result!r}"
        )

    def test_negative_denominator_returns_correct_result(self):
        """
        Scenario 6 — Valid division with negative denominator returns correct result (edge case).
        Requirement: ADSAT-16 — For valid inputs, it must return numerator divided by denominator.
        """
        result = calculate_ratio(10, -2)
        assert result == -5, (
            f"Expected calculate_ratio(10, -2) to return -5, got {result!r}"
        )


class TestCalculateRatioZeroDenominator:
    """Scenarios covering zero-denominator rejection — ADSAT-16."""

    def test_zero_denominator_raises_value_error(self):
        """
        Scenario 2 — Zero denominator raises ValueError (negative).
        Requirement: ADSAT-16 — calculate_ratio(10, 0) raises ValueError.
        """
        with pytest.raises(ValueError):
            calculate_ratio(10, 0)

    def test_zero_denominator_error_message_mentions_denominator_and_zero(self):
        """
        Scenario 3 — ValueError message explains denominator cannot be zero.
        Requirement: ADSAT-16 — The error message explains that the denominator cannot be zero.
        """
        with pytest.raises(ValueError) as exc_info:
            calculate_ratio(10, 0)

        error_message = str(exc_info.value).lower()
        assert "denominator" in error_message, (
            f"Expected the error message to mention 'denominator', got: {str(exc_info.value)!r}"
        )
        assert "zero" in error_message, (
            f"Expected the error message to mention 'zero', got: {str(exc_info.value)!r}"
        )
