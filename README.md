# Credit Decision Engine

A rules-based engine built in Python and Pandas that evaluates loan applications and makes automated credit decisions (Approve, Reject, Review).

## What This Project Does
This project simulates a core system used by fintech and lending companies. It ingests loan applications, calculates financial ratios, and applies a strict rules engine to determine credit risk.

### The Rules Engine
The engine checks applications in priority order:
1. **Credit Score:** If the score is below 500, the application is **Rejected**.
2. **Debt-to-Income (DTI) Ratio:** If the requested loan amount exceeds 50% of the applicant's annual income, the application is **Rejected**.
3. **Default History:** If the applicant has previous defaults, the application is flagged for **Manual Review**.
4. **Employment Length:** If the applicant has less than 1 year of employment, the application is flagged for **Manual Review**.

If the application passes all checks, it is **Approved**.

## Why This Matters (Auditability)
For credit risk and internal audit teams, it's not enough to just reject a loan. You must know *why* it was rejected. This engine outputs a `decision_results.csv` file that logs the exact reason for every decision.

## How to Run
1. Install dependencies: `pip install pandas numpy`
2. Generate synthetic data: `python generate_data.py`
3. Run the engine: `python decision_engine.py`

## Sample Output
```text
--- Decision Engine Summary ---
APPROVE    612
REJECT     311
REVIEW      77

--- Rejection Reasons ---
Loan amount exceeds 50% of annual income    203
Credit score below 500                      108