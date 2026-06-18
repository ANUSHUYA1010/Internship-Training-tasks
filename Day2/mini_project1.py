import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv(r"C:\Users\DIVIYA LAKSHIMI.S\Downloads\Iris.csv")

X = df.drop(["Id", "Species"], axis=1)
y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "iris_model.pkl")

print("Model retrained and saved.")
import streamlit as st
import joblib

model = joblib.load("iris_model.pkl")

st.title("Iris Flower Prediction System")

sepal_length = st.number_input("Sepal Length (cm)")
sepal_width = st.number_input("Sepal Width (cm)")
petal_length = st.number_input("Petal Length (cm)")
petal_width = st.number_input("Petal Width (cm)")

if st.button("Predict"):

    prediction = model.predict([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    st.success(f"Predicted Species: {prediction[0]}")
from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load("iris_model.pkl")

@app.route("/")
def home():
    return """
    <h2>Iris Prediction System</h2>

    <form action="/predict" method="post">
        <input name="sl" placeholder="Sepal Length"><br><br>
        <input name="sw" placeholder="Sepal Width"><br><br>
        <input name="pl" placeholder="Petal Length"><br><br>
        <input name="pw" placeholder="Petal Width"><br><br>

        <button type="submit">Predict</button>
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():

    values = [[
        float(request.form["sl"]),
        float(request.form["sw"]),
        float(request.form["pl"]),
        float(request.form["pw"])
    ]]

    prediction = model.predict(values)[0]

    return f"<h3>Predicted Species: {prediction}</h3>"

if __name__ == "__main__":
    app.run(debug=True)