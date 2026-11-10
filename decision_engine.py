import pandas as pd
import sqlite3

def evaluate_applications(input_csv="applications.csv"):
    print("Loading applications...")
    df = pd.read_csv(input_csv)

    # 1. Calculate the Debt-to-Income (DTI) ratio
    df["dti_ratio"] = df["loan_amount"] / (df["monthly_income"] * 12)

    # 2. Initialize decision and reason columns
    df["decision"] = "APPROVE"
    df["reason"] = "Meets all criteria"

    # 3. Apply the Rules (Order matters!)
    mask_bad_credit = df["credit_score"] < 500
    df.loc[mask_bad_credit, "decision"] = "REJECT"
    df.loc[mask_bad_credit, "reason"] = "Credit score below 500"

    mask_high_dti = (df["dti_ratio"] > 0.5) & (df["decision"] != "REJECT")
    df.loc[mask_high_dti, "decision"] = "REJECT"
    df.loc[mask_high_dti, "reason"] = "Loan amount exceeds 50% of annual income"

    mask_default = (df["previous_defaults"] > 0) & (df["decision"] != "REJECT")
    df.loc[mask_default, "decision"] = "REVIEW"
    df.loc[mask_default, "reason"] = "Previous default history requires manual review"

    mask_employment = (df["employment_length_years"] < 1) & (df["decision"] == "APPROVE")
    df.loc[mask_employment, "decision"] = "REVIEW"
    df.loc[mask_employment, "reason"] = "Less than 1 year of employment history"

    # --- NEW: SAVE TO SQLITE DATABASE ---
    print("Saving results to SQLite database (credit_risk.db)...")
    conn = sqlite3.connect("credit_risk.db")
    
    # Save the raw applications with their new decisions
    df.to_sql("decision_results", conn, if_exists="replace", index=False)
    conn.close()
    
    # Save CSV just in case
    df.to_csv("decision_results.csv", index=False)
    
    print("\n--- Decision Engine Summary ---")
    print(df["decision"].value_counts().to_string())
    print("\nResults saved to SQLite (credit_risk.db) and CSV.")

if __name__ == "__main__":
    evaluate_applications()