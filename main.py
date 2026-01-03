import os
import pandas as pd

# Path to dataset
file_path = 'data/credit_data.csv'

# Check if dataset exists
if not os.path.exists(file_path):
    print(f"{file_path} not found. Creating a sample dataset...")

    # Make sure the data folder exists
    os.makedirs('data', exist_ok=True)

    # Sample dataset
    data = {
        "age": [25, 40, 35, 50, 28],
        "income": [50000, 80000, 60000, 100000, 45000],
        "loan_amount": [20000, 30000, 15000, 50000, 10000],
        "credit_history": [1, 0, 1, 0, 1],
        "default": [0, 1, 0, 1, 0]
    }

    # Convert to DataFrame and save
    pd.DataFrame(data).to_csv(file_path, index=False)
    print(f"Sample dataset created at {file_path}")

# Load dataset
df = pd.read_csv(file_path)
print("Dataset loaded successfully!")
print(df.head())
