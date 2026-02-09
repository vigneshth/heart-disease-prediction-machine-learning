import streamlit as st
import joblib
import numpy as np
import os
import time

# Page configuration
st.set_page_config(page_title="CAD Prediction", layout="centered")

st.title("CAD Prediction App")
st.write("This app predicts the likelihood of Coronary Artery Disease (CAD) based on user inputs.")

# Load model with caching
@st.cache_resource
def load_model():
    model_path = "bagging_rf_model.pkl"
    if not os.path.exists(model_path):
        st.error("Model file not found. Please train and save the model first.")
        st.stop()

    start_time = time.time()
    model = joblib.load(model_path)
    st.success(f"Model loaded successfully in {time.time() - start_time:.2f} seconds.")
    return model

model = load_model()

# User input form
with st.form("heart_form", clear_on_submit=True):
    st.subheader("Enter Your Details")

    age_category = st.selectbox(
        "Age Category",
        ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49",
         "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"]
    )

    sex = st.radio("Sex", ["Male", "Female"], horizontal=True)
    smoking = st.radio("Do you smoke?", ["Yes", "No"], horizontal=True)
    race = st.radio("Race", ["White", "Other"], horizontal=True)

    mental_health = st.slider("Mental health (bad days in last 30 days)", 0, 30, 5)
    physical_health = st.slider("Physical health (bad days in last 30 days)", 0, 30, 5)
    sleep_time = st.slider("Average sleep time (hours)", 1, 12, 7)
    bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=25.0)

    physical_activity = st.radio("Do you engage in physical activity?", ["Yes", "No"], horizontal=True)
    general_health = st.radio("Is your general health good?", ["Yes", "No"], horizontal=True)

    submitted = st.form_submit_button("Predict")

if submitted:
    st.info("Prediction logic goes here (model.predict).")
