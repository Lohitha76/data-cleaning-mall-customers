import pandas as pd

# Load dataset
df = pd.read_csv('Mall_Customers.csv')

# Standardize text in 'Genre' to have first letter capitalized
df['Genre'] = df['Genre'].str.capitalize()

# Rename columns to lowercase and replace spaces with underscores
df.rename(columns={
    'CustomerID': 'customer_id',
    'Genre': 'gender',
    'Age': 'age',
    'Annual Income (k$)': 'annual_income_k',
    'Spending Score (1-100)': 'spending_score'
}, inplace=True)

# Save cleaned dataset
df.to_csv('Mall_Customers_cleaned.csv', index=False)
