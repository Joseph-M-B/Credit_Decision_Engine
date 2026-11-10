import sqlite3
import pandas as pd

def run_credit_analysis():
    print("Running SQL Risk Analysis...")
    conn = sqlite3.connect("credit_risk.db")
    
    # Query 1: Portfolio Risk Summary
    query1 = """
    SELECT 
        decision,
        COUNT(*) AS total_applications,
        ROUND(AVG(credit_score), 0) AS avg_credit_score,
        ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
        ROUND(AVG(dti_ratio), 3) AS avg_dti_ratio
    FROM decision_results
    GROUP BY decision;
    """
    
    # Query 2: Total Financial Exposure (How much money is at risk?)
    query2 = """
    SELECT 
        decision,
        ROUND(SUM(loan_amount), 2) AS total_loan_value
    FROM decision_results
    GROUP BY decision
    ORDER BY total_loan_value DESC;
    """
    
    # Query 3: Top 5 Riskiest Applications (For Audit Review)
    query3 = """
    SELECT applicant_name, credit_score, loan_amount, dti_ratio, reason
    FROM decision_results
    WHERE decision = 'REJECT'
    ORDER BY dti_ratio DESC
    LIMIT 5;
    """

    print("\n--- Portfolio Risk Summary ---")
    df1 = pd.read_sql_query(query1, conn)
    print(df1.to_string(index=False))

    print("\n--- Total Financial Exposure by Decision ---")
    df2 = pd.read_sql_query(query2, conn)
    print(df2.to_string(index=False))

    print("\n--- Top 5 Riskiest Rejected Applications ---")
    df3 = pd.read_sql_query(query3, conn)
    print(df3.to_string(index=False))

    conn.close()

if __name__ == "__main__":
    run_credit_analysis()