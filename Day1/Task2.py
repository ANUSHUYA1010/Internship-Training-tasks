import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
df = pd.read_excel("C:\internshiptask\iris.csv.xlsx")
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Duplicate Rows:")
print(df[df.duplicated()])
plt.scatter(df['SepalLengthCm'],
            df['SepalWidthCm'])
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()