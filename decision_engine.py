import pandas as pd

def evaluate_applications(input_csv="applications.csv"):
    print("Loading applications...")
    df = pd.read_csv(input_csv)

    # 1. Calculate the Debt-to-Income (DTI) ratio
    # If the loan is more than 50% of their annual income, it's risky.
    # We'll simplify: Loan amount / (Monthly income * 12)
    df["dti_ratio"] = df["loan_amount"] / (df["monthly_income"] * 12)

    # 2. Initialize decision and reason columns
    df["decision"] = "APPROVE"
    df["reason"] = "Meets all criteria"

    # 3. Apply the Rules (Order matters! We check the worst rules first)
    
    # Rule 1: Credit Score < 500 -> REJECT
    mask_bad_credit = df["credit_score"] < 500
    df.loc[mask_bad_credit, "decision"] = "REJECT"
    df.loc[mask_bad_credit, "reason"] = "Credit score below 500"

    # Rule 2: DTI > 0.5 -> REJECT (but only if not already rejected)
    mask_high_dti = (df["dti_ratio"] > 0.5) & (df["decision"] != "REJECT")
    df.loc[mask_high_dti, "decision"] = "REJECT"
    df.loc[mask_high_dti, "reason"] = "Loan amount exceeds 50% of annual income"

    # Rule 3: Previous Defaults > 0 -> REVIEW (Manual check needed)
    mask_default = (df["previous_defaults"] > 0) & (df["decision"] != "REJECT")
    df.loc[mask_default, "decision"] = "REVIEW"
    df.loc[mask_default, "reason"] = "Previous default history requires manual review"

    # Rule 4: Employment length < 1 year -> REVIEW
    mask_employment = (df["employment_length_years"] < 1) & (df["decision"] == "APPROVE")
    df.loc[mask_employment, "decision"] = "REVIEW"
    df.loc[mask_employment, "reason"] = "Less than 1 year of employment history"

    # 4. Save the results
    output_df = df[["applicant_name", "credit_score", "loan_amount", "dti_ratio", "decision", "reason"]]
    output_df.to_csv("decision_results.csv", index=False)
    
    # 5. Print a summary for the business
    print("\n--- Decision Engine Summary ---")
    print(df["decision"].value_counts().to_string())
    
    print("\n--- Rejection Reasons ---")
    rejected = df[df["decision"] == "REJECT"]
    print(rejected["reason"].value_counts().to_string())
    
    print(f"\nResults saved to decision_results.csv")

if __name__ == "__main__":
    evaluate_applications()