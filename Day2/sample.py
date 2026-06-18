# ==========================
# Task 1: Setup Python
# ==========================

print("\n1. Setup Python")

# ==========================
# Task 2: Variables & Datatypes
# ==========================

print("\n2. Variables & Datatypes")

a = 1
b = 1.23
c = "Anu"
d = True

print("Datatype of A:", type(a))
print("Datatype of B:", type(b))
print("Datatype of C:", type(c))
print("Datatype of D:", type(d))

# ==========================
# Task 3: Lists, Tuples, Dictionaries
# ==========================

print("\n3. Lists, Tuples & Dictionaries")

numbers = [1, 2, 2, 3, 3, 4, 45, 5, 1010110101]

print("Original List:", numbers)
print("Sliced List:", numbers[1:7])

numbers.append(56)
numbers.remove(2)

print("Updated List:", numbers)

tup = (1, 3, 5, 6, 7, 9)
print("Tuple Element:", tup[4])

data_dict = {"A": 5, "B": 3, "C": 10}
print("Dictionary Value:", data_dict["A"])

employees = [
    {"id": 101, "name": "Anu", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Rahul", "department": "HR", "salary": 45000},
    {"id": 103, "name": "Priya", "department": "Finance", "salary": 60000}
]

print("\nEmployee Details")

for emp in employees:
    print(emp["name"], emp["salary"])

# ==========================
# Task 4: Functions & Loops
# ==========================

print("\n4. Functions & Loops")


def greet(name):
    return f"Hello, {name}"


for i in range(1, 9):
    print(i)

print(greet("Anu"))

# ==========================
# Task 5: File Handling
# ==========================

print("\n5. File Handling")

with open("Notes.txt", "w") as file:
    file.write("Python file handling\n")

name = input("Enter your Name: ")

with open("Notes.txt", "a") as file:
    file.write(name + "\n")

with open("Notes.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# ==========================
# Task 6: NumPy Arrays
# ==========================

print("\n6. NumPy Arrays")

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)

a1 = np.array([4, 5, 6, 7, 8])
b1 = np.array([10, 9, 8, 7, 6])

print("Addition:", a1 + b1)
print("Multiplication:", a1 * b1)

mat = arr.reshape(2, 5)

print("Reshaped Array:")
print(mat)

# ==========================
# Task 7: Pandas DataFrames
# ==========================

print("\n7. Pandas DataFrames")

import pandas as pd

data = {
    "Name": ["Anu", "Rahul", "Priya"],
    "Age": [22, 25, 23],
    "Department": ["IT", "HR", "Finance"]
}

employee_df = pd.DataFrame(data)

print(employee_df)
print("\nHead:")
print(employee_df.head())

print("\nColumns:")
print(employee_df.columns)

print("\nShape:")
print(employee_df.shape)

# ==========================
# Task 8: Load CSV
# ==========================

print("\n8. Load CSV")

iris_path = r"C:\Users\DIVIYA LAKSHIMI.S\Downloads\Iris.csv"

df = pd.read_csv(iris_path)

print(df.head())

print("\nInfo:")
df.info()

print("\nStatistics:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)

# ==========================
# Task 9: Data Cleansing
# ==========================

print("\n9. Data Cleansing")

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()
df = df.drop_duplicates()

print("\nDataset Shape After Cleaning:")
print(df.shape)

# ==========================
# Task 10: Filtering & Sorting
# ==========================

print("\n10. Filtering & Sorting")

filtered = df[df["SepalLengthCm"] > 5.0]

print("\nSepalLengthCm > 5.0")
print(filtered.head())

filtered_species = df[
    (df["Species"] == "Iris-setosa") &
    (df["PetalLengthCm"] > 1.5)
]

print("\nFiltered Species")
print(filtered_species.head())

sorted_df = df.sort_values(
    by="SepalLengthCm",
    ascending=False
)

print("\nSorted Data")
print(sorted_df.head())

# ==========================
# Task 11: Grouping
# ==========================

print("\n11. Grouping")

sales = pd.DataFrame({
    "Region": ["East", "West", "East", "North"],
    "Sales": [1000, 2000, 1500, 1200]
})

result = sales.groupby("Region")["Sales"].mean()

print(result)

# ==========================
# Task 12: Merge Datasets
# ==========================

print("\n12. Merge Datasets")

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Anu", "Rahul", "Priya"]
})

orders = pd.DataFrame({
    "CustomerID": [1, 2, 1],
    "Amount": [500, 700, 300]
})

merged = pd.merge(customers, orders, on="CustomerID")

print(merged)

# ==========================
# Task 13: Statistics Basics
# ==========================

print("\n13. Statistics Basics")

print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nMode:")
print(df.mode())

print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# ==========================
# Task 14: Data Visualization
# ==========================

print("\n14. Data Visualization")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(18, 12))

# Line Plot
plt.subplot(3, 3, 1)
plt.plot(df["SepalLengthCm"], color="hotpink")
plt.title("Line Plot")

# Bar Plot
plt.subplot(3, 3, 2)
species_count = df["Species"].value_counts()
plt.bar(species_count.index, species_count.values, color="hotpink")
plt.title("Bar Plot")
plt.xticks(rotation=15)

# Pie Chart
plt.subplot(3, 3, 3)
plt.pie(
    species_count.values,
    labels=species_count.index,
    autopct="%1.1f%%",
    colors=["hotpink", "pink", "lightgreen"]
)
plt.title("Pie Chart")

# Histogram
plt.subplot(3, 3, 4)
plt.hist(df["SepalLengthCm"], bins=10, color="hotpink")
plt.title("Histogram")

# Heatmap
plt.subplot(3, 3, 5)
sns.heatmap(
    df.select_dtypes(include=np.number).corr(),
    annot=True,
    cmap="RdPu"
)
plt.title("Heatmap")

# Density Plot
plt.subplot(3, 3, 6)
sns.kdeplot(
    df["PetalLengthCm"],
    fill=True,
    color="green"
)
plt.title("Density Plot")

# Contour Plot
plt.subplot(3, 3, 7)

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

plt.contour(X, Y, Z, colors="red")
plt.title("Contour Plot")

# Box Plot
plt.subplot(3, 3, 8)
plt.boxplot(
    df["SepalLengthCm"],
    patch_artist=True,
    boxprops=dict(facecolor="hotpink")
)
plt.title("Box Plot")

plt.tight_layout()
plt.show()