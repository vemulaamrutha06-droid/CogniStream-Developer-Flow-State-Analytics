
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load dataset
df = pd.read_csv("data/developer_activity.csv")

print("Original Dataset Shape:", df.shape)

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Handle missing values
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include="object").columns
df[categorical_cols] = df[categorical_cols].fillna("Unknown")

# 5. Convert date column
df["date"] = pd.to_datetime(df["date"])

# 6. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 7. Save cleaned dataset
Path("data").mkdir(exist_ok=True)
df.to_csv("data/cleaned_developer_activity.csv", index=False)

# 8. Create visualizations
Path("reports/figures").mkdir(parents=True, exist_ok=True)
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.histplot(df["focus_score"], kde=True)
plt.title("Developer Focus Score Distribution")
plt.savefig("reports/figures/focus_distribution.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.histplot(df["cognitive_load"], kde=True)
plt.title("Cognitive Load Distribution")
plt.savefig("reports/figures/cognitive_load_distribution.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="focus_score",
    y="productivity_score",
    hue="task_type"
)
plt.title("Focus Score vs Productivity")
plt.savefig("reports/figures/focus_vs_productivity.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Developer Activity Correlation Heatmap")
plt.tight_layout()
plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

print("\nData cleaning and EDA completed successfully!")
print("Cleaned dataset saved.")
print("Visualizations saved in reports/figures/")
print("Final Dataset Shape:", df.shape)
