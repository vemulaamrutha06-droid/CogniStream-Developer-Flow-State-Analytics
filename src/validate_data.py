
import pandas as pd

# Load dataset
df = pd.read_csv("data/developer_activity.csv")

print("DATA VALIDATION REPORT")
print("-" * 40)

# Dataset information
print("Dataset Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Data types
print("\nData Types:")
print(df.dtypes)

# Validate score columns
score_columns = [
    "focus_score",
    "cognitive_load",
    "productivity_score"
]

for column in score_columns:
    if column in df.columns:
        invalid = (~df[column].between(0, 100)).sum()
        print(f"{column} invalid values: {invalid}")

print("\nData validation completed!")
