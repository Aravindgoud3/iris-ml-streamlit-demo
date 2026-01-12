import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Iris ML Model Comparison")

st.title("Iris Species Prediction")

st.write("Select any trained model to see how predictions change in real time.")

# Load all models
models = {
    "KNN": joblib.load("best_models/knn.pkl"),
    "SVC": joblib.load("best_models/svc.pkl"),
    "Logistic Regression": joblib.load("best_models/logistic_regression.pkl"),
    "Random Forest": joblib.load("best_models/random_forest.pkl"),
    "Decision Tree": joblib.load("best_models/decision_tree.pkl"),
    "Naive Bayes (Best Model)": joblib.load("best_models/naive_bayes.pkl"),
}

# Model selection
selected_model_name = st.selectbox(
    "Choose a Model",
    list(models.keys())
)

selected_model = models[selected_model_name]

# Input fields
sl = st.number_input("Sepal Length (cm)", value=5.1)
sw = st.number_input("Sepal Width (cm)", value=3.5)
pl = st.number_input("Petal Length (cm)", value=1.4)
pw = st.number_input("Petal Width (cm)", value=0.2)

if st.button("Predict"):
    X = np.array([[sl, sw, pl, pw]])
    prediction = selected_model.predict(X)
    st.success(f"Prediction using {selected_model_name}: **{prediction[0]}**")

