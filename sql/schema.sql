CREATE TABLE IF NOT EXISTS loan_applications (
    application_id SERIAL PRIMARY KEY,
    applicant_name VARCHAR(100),
    credit_score INTEGER,
    monthly_income NUMERIC,
    loan_amount NUMERIC,
    employment_length_years INTEGER,
    previous_defaults INTEGER,
    application_date DATE
);

CREATE TABLE IF NOT EXISTS decision_results (
    decision_id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES loan_applications(application_id),
    decision VARCHAR(20),
    reason VARCHAR(255),
    decision_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);