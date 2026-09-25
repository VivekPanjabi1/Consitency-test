# Regression Scenarios — ADSAT-16: Validate division by zero handling

## Requirement source
Jira ticket ADSAT-16 — `calculate_ratio` function must:
1. Return `numerator / denominator` for valid (non-zero denominator) inputs.
2. Raise `ValueError` when the denominator is zero.
3. Include an error message that explains the denominator cannot be zero.

---

## Scenario 1 — Positive: valid division returns correct ratio
**Requirement:** ADSAT-16 — "For valid inputs, it must return numerator divided by denominator. `calculate_ratio(10, 2)` returns `5`."

**Preconditions:**
- The `calculate_ratio` function is importable from the production module.
- Numerator = 10, Denominator = 2 (non-zero).

**Steps:**
1. Call `calculate_ratio(10, 2)`.

**Expected result:**
- The return value equals `5`.

---

## Scenario 2 — Negative: zero denominator raises ValueError
**Requirement:** ADSAT-16 — "`calculate_ratio(10, 0)` raises `ValueError`."

**Preconditions:**
- The `calculate_ratio` function is importable from the production module.
- Numerator = 10, Denominator = 0.

**Steps:**
1. Call `calculate_ratio(10, 0)` inside a context that captures exceptions.

**Expected result:**
- A `ValueError` is raised (not any other exception type).

---

## Scenario 3 — Edge: error message mentions denominator cannot be zero
**Requirement:** ADSAT-16 — "The error message explains that the denominator cannot be zero."

**Preconditions:**
- The `calculate_ratio` function is importable from the production module.
- Numerator = 10, Denominator = 0.

**Steps:**
1. Call `calculate_ratio(10, 0)` inside a context that captures the raised `ValueError`.
2. Inspect the string representation of the exception.

**Expected result:**
- The exception message contains text indicating the denominator cannot be zero (case-insensitive match on "denominator" and "zero").

---

## Scenario 4 — Edge: other valid numerator/denominator pairs return correct ratio
**Requirement:** ADSAT-16 — "For valid inputs, it must return numerator divided by denominator."

**Preconditions:**
- The `calculate_ratio` function is importable from the production module.
- Multiple non-zero denominator pairs are tested.

**Steps:**
1. Call `calculate_ratio` with each of the following pairs and compare the result:
   - `(1, 1)` → `1.0`
   - `(9, 3)` → `3.0`
   - `(7, 2)` → `3.5`
   - `(-10, 2)` → `-5.0`

**Expected result:**
- Each call returns the arithmetically correct quotient.

---

## Scenario 5 — Edge: negative denominator is valid (not zero) and returns correct ratio
**Requirement:** ADSAT-16 — "The function must reject a denominator of **zero**" (only zero is rejected).

**Preconditions:**
- The `calculate_ratio` function is importable from the production module.
- Denominator = -2 (non-zero, negative).

**Steps:**
1. Call `calculate_ratio(10, -2)`.

**Expected result:**
- The return value equals `-5.0` (no exception is raised).
