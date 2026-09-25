# Regression Scenarios — ADSAT-16: Validate division by zero handling

## Requirement source
Jira ticket **ADSAT-16** — The `calculate_ratio` function must reject a denominator of zero. For valid inputs it must return numerator divided by denominator. The error message must explain that the denominator cannot be zero.

---

## Scenario 1 — Valid division returns correct ratio (positive)
**Requirement:** `calculate_ratio(10, 2)` returns `5`.

| Field | Detail |
|---|---|
| **Preconditions** | `calculate_ratio` is importable from the module under test. |
| **Steps** | Call `calculate_ratio(10, 2)`. |
| **Expected result** | Return value equals `5` (integer or float). |
| **Requirement ref** | ADSAT-16 — "For valid inputs, it must return numerator divided by denominator. `calculate_ratio(10, 2)` returns `5`." |

---

## Scenario 2 — Zero denominator raises ValueError (negative)
**Requirement:** `calculate_ratio(10, 0)` raises `ValueError`.

| Field | Detail |
|---|---|
| **Preconditions** | `calculate_ratio` is importable from the module under test. |
| **Steps** | Call `calculate_ratio(10, 0)`. |
| **Expected result** | A `ValueError` is raised (not a silent return value). |
| **Requirement ref** | ADSAT-16 — "`calculate_ratio(10, 0)` raises `ValueError`." |

---

## Scenario 3 — ValueError message explains zero-denominator prohibition (edge / message content)
**Requirement:** The error message explains that the denominator cannot be zero.

| Field | Detail |
|---|---|
| **Preconditions** | `calculate_ratio` is importable from the module under test. |
| **Steps** | Call `calculate_ratio(10, 0)` inside a `pytest.raises(ValueError)` context and capture `exc_info.value`. |
| **Expected result** | The string representation of the exception contains wording that communicates the denominator cannot be zero (case-insensitive match on "denominator" and "zero"). |
| **Requirement ref** | ADSAT-16 — "The error message explains that the denominator cannot be zero." |
