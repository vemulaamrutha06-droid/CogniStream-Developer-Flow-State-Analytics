
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

n = 1000

data = {
    "developer_id": np.random.choice(
        ["DEV001", "DEV002", "DEV003", "DEV004", "DEV005"], n
    ),
    "date": pd.date_range("2026-09-01", periods=n, freq="h"),
    "task_type": np.random.choice(
        ["Coding", "Debugging", "Testing", "Code Review", "Documentation"], n
    ),
    "coding_hours": np.round(np.random.uniform(1, 9, n), 2),
    "break_minutes": np.random.randint(5, 90, n),
    "interruptions": np.random.randint(0, 16, n),
    "commits": np.random.randint(0, 21, n),
    "bugs_reported": np.random.randint(0, 11, n),
    "sleep_hours": np.round(np.random.uniform(4, 10, n), 1),
}

df = pd.DataFrame(data)

df["focus_score"] = np.clip(
    100 - df["interruptions"] * 4
    + df["sleep_hours"] * 3
    - df["break_minutes"] * 0.15
    + np.random.normal(0, 8, n),
    0, 100
).round(2)

df["cognitive_load"] = np.clip(
    100 - df["focus_score"]
    + df["bugs_reported"] * 2
    + np.random.normal(0, 5, n),
    0, 100
).round(2)

df["productivity_score"] = np.clip(
    df["focus_score"] * 0.6
    + df["commits"] * 2
    - df["bugs_reported"] * 2
    + np.random.normal(0, 5, n),
    0, 100
).round(2)

output_path = Path("data") / "developer_activity.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print("Saved at:", output_path)
print(df.head())
