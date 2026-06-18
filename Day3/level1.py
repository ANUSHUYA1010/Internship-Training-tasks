# ==========================
# Task 15: Charts
# ==========================

print("\n===== Task 15: Charts =====")

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime

# Load Iris dataset if not already loaded
df = pd.read_csv(r"C:\Users\DIVIYA LAKSHIMI.S\Downloads\Iris.csv")

# Scatter Plot
plt.figure(figsize=(8, 5))

plt.scatter(
    df["SepalLengthCm"],
    df["PetalLengthCm"]
)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Sepal Length vs Petal Length")

plt.show()

# Pair Plot
sns.pairplot(df, hue="Species")

plt.show()

# ==========================
# Task 16: Correlation
# ==========================

print("\n===== Task 16: Correlation =====")

correlation_matrix = df.select_dtypes(
    include=np.number
).corr()

print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()

# ==========================
# Task 17: Export Data
# ==========================

print("\n===== Task 17: Export Data =====")

df.to_csv(
    "cleaned_iris.csv",
    index=False
)

df.to_excel(
    "cleaned_iris.xlsx",
    index=False
)

print("Files exported successfully.")

# ==========================
# Task 18: Date/Time Handling
# ==========================

print("\n===== Task 18: Date/Time Handling =====")

current_datetime = datetime.now()

print("Current Date and Time:", current_datetime)

print("Date:", current_datetime.date())

print("Time:", current_datetime.time())

print(
    "Formatted Date:",
    current_datetime.strftime("%d-%m-%Y")
)

print(
    "Formatted Time:",
    current_datetime.strftime("%H:%M:%S")
)

# Create a date column

df["CreatedDate"] = pd.date_range(
    start="2026-01-01",
    periods=len(df),
    freq="D"
)

print(df[["CreatedDate"]].head())

# ==========================
# Task 19: Scripts
# ==========================

print("\n===== Task 19: Scripts =====")


def dataset_summary(dataframe):
    print("\nDataset Shape:", dataframe.shape)

    print("\nColumns:")
    print(dataframe.columns.tolist())

    print("\nMissing Values:")
    print(dataframe.isnull().sum())


dataset_summary(df)

# ==========================
# Task 20: Data Project
# ==========================

print("\n===== Task 20: Data Project =====")

print("\nDataset Shape:")
print(df.shape)

print("\nSpecies Count:")
print(df["Species"].value_counts())

print("\nAverage Measurements by Species:")

summary = df.groupby("Species").mean(
    numeric_only=True
)

print(summary)

summary.to_csv(
    "iris_summary.csv"
)

print("\nProject completed successfully.")

print("\nGenerated Files:")
print("1. cleaned_iris.csv")
print("2. cleaned_iris.xlsx")
print("3. iris_summary.csv")