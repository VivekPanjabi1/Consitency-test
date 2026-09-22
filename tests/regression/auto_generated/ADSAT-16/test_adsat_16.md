# Regression Scenarios — ADSAT-16: Validate division by zero handling

## Requirement source
Jira ticket **ADSAT-16** — The `calculate_ratio` function must:
1. Return `numerator / denominator` for valid (non-zero denominator) inputs.
2. Raise a `ValueError` when the denominator is zero.
3. Include an explanatory message in the `ValueError` that communicates the denominator cannot be zero.

---

## Scenario 1 — Valid division returns correct result (Positive)
**Requirement:** ADSAT-16 — `calculate_ratio(10, 2)` returns `5`.

**Preconditions:** The `calculate_ratio` function is importable from the module.

**Steps:**
1. Call `calculate_ratio(10, 2)`.

**Expected result:** The return value equals `5`.

---

## Scenario 2 — Zero denominator raises ValueError (Negative)
**Requirement:** ADSAT-16 — `calculate_ratio(10, 0)` raises `ValueError`.

**Preconditions:** The `calculate_ratio` function is importable from the module.

**Steps:**
1. Call `calculate_ratio(10, 0)`.

**Expected result:** A `ValueError` is raised (not any other exception type).

---

## Scenario 3 — ValueError message explains denominator constraint (Edge)
**Requirement:** ADSAT-16 — The error message explains that the denominator cannot be zero.

**Preconditions:** The `calculate_ratio` function is importable from the module.

**Steps:**
1. Call `calculate_ratio(10, 0)` inside a try/except block and capture the exception message.

**Expected result:** The exception message contains wording that communicates the denominator cannot be zero (case-insensitive match on "denominator" and "zero").
