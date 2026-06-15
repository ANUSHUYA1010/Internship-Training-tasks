# Student Performance Prediction using Linear Regression

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample Dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [20, 25, 35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Input and Output
X = df[['Hours_Studied']]
y = df['Marks']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict Test Data
y_pred = model.predict(X_test)

# Display Results
print("Actual Marks:", list(y_test))
print("Predicted Marks:", y_pred)

# Model Accuracy
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error:", mse)

# User Input Prediction
hours = float(input("\nEnter Hours Studied: "))

predicted_marks = model.predict([[hours]])

print("Predicted Marks:", round(predicted_marks[0], 2))