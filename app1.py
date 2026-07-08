import numpy as np
import pandas as pd
import streamlit as st
import joblib

st.set_page_config(
    page_title="Customer Churn System & Monitor", 
    page_icon="📊", 
    layout="wide"
)

@st.cache_resource
def load_assets():
    model = joblib.load("final_churn_model (1).pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_assets()

tab1, tab2 = st.tabs(["🔮 Churn Prediction App", "📈 System Performance & Monitor"])

with tab1:
    st.title("📊 Customer Churn Prediction Dashboard")
    st.write("Enter the customer metrics below to check the prediction probability.")
    
    st.header("Customer Profiles")
    col1, col2 = st.columns(2)

    with col1:
        credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
        age = st.number_input("Age", min_value=18, max_value=100, value=35)
        tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=5)
        balance = st.number_input("Account Balance", min_value=0.0, value=50000.0, step=1000.0)
        estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=60000.0, step=1000.0)

    with col2:
        products_number = st.selectbox("Number of Products", [1, 2, 3, 4])
        credit_card = st.selectbox("Has Credit Card?", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        active_member = st.selectbox("Is Active Member?", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        gender_input = st.selectbox("Gender", ["Male", "Female"])
        country = st.selectbox("Country", ["France", "Germany", "Spain"])

    st.write("---")
    
    if
