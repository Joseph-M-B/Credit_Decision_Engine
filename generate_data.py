import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_applications(num_rows=1000):
    np.random.seed(42)
    random.seed(42)

    data = {
        "applicant_name": [f"Customer_{i}" for i in range(num_rows)],
        "credit_score": np.random.randint(300, 850, num_rows),
        "monthly_income": np.random.randint(1000, 15000, num_rows),
        "loan_amount": np.random.randint(500, 50000, num_rows),
        "employment_length_years": np.random.randint(0, 20, num_rows),
        "previous_defaults": np.random.choice([0, 0, 0, 1, 2], num_rows, p=[0.6, 0.2, 0.1, 0.05, 0.05]),
        "application_date": [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_rows)]
    }
    
    df = pd.DataFrame(data)
    # Round currency to 2 decimals
    df["monthly_income"] = df["monthly_income"].round(2)
    df["loan_amount"] = df["loan_amount"].round(2)
    
    df.to_csv("applications.csv", index=False)
    print(f"Generated {num_rows} applications to applications.csv")

if __name__ == "__main__":
    generate_applications()