# Regression Scenarios — ADSAT-16: Validate division by zero handling

## Requirement source
Jira ticket ADSAT-16 — `calculate_ratio` must:
1. Return `numerator / denominator` for valid (non-zero denominator) inputs.
2. Raise `ValueError` when the denominator is zero.
3. Include an explanatory message in the `ValueError` that states the denominator cannot be zero.

---

## Scenario 1 — Valid division returns correct result (positive)
**Requirement:** ADSAT-16 — "For valid inputs, it must return numerator divided by denominator. `calculate_ratio(10, 2)` returns `5`."

**Preconditions:** The `calculate_ratio` function is importable and the denominator is non-zero.

**Steps:**
1. Call `calculate_ratio(10, 2)`.

**Expected result:** The return value equals `5`.

---

## Scenario 2 — Zero denominator raises ValueError (negative)
**Requirement:** ADSAT-16 — "`calculate_ratio(10, 0)` raises `ValueError`."

**Preconditions:** The `calculate_ratio` function is importable.

**Steps:**
1. Call `calculate_ratio(10, 0)`.

**Expected result:** A `ValueError` is raised.

---

## Scenario 3 — ValueError message explains denominator cannot be zero (negative / message content)
**Requirement:** ADSAT-16 — "The error message explains that the denominator cannot be zero."

**Preconditions:** The `calculate_ratio` function is importable.

**Steps:**
1. Call `calculate_ratio(10, 0)` inside a try/except block and capture the exception message.

**Expected result:** The exception message contains wording indicating the denominator cannot be zero (case-insensitive match on "denominator" and "zero").

---

## Scenario 4 — Valid division with numerator zero returns zero (edge case)
**Requirement:** ADSAT-16 — "For valid inputs, it must return numerator divided by denominator."

**Preconditions:** The `calculate_ratio` function is importable and the denominator is non-zero.

**Steps:**
1. Call `calculate_ratio(0, 5)`.

**Expected result:** The return value equals `0`.

---

## Scenario 5 — Valid division with negative numerator returns correct result (edge case)
**Requirement:** ADSAT-16 — "For valid inputs, it must return numerator divided by denominator."

**Preconditions:** The `calculate_ratio` function is importable and the denominator is non-zero.

**Steps:**
1. Call `calculate_ratio(-10, 2)`.

**Expected result:** The return value equals `-5`.

---

## Scenario 6 — Valid division with negative denominator returns correct result (edge case)
**Requirement:** ADSAT-16 — "For valid inputs, it must return numerator divided by denominator."

**Preconditions:** The `calculate_ratio` function is importable and the denominator is non-zero.

**Steps:**
1. Call `calculate_ratio(10, -2)`.

**Expected result:** The return value equals `-5`.
