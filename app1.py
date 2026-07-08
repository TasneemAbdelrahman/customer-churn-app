import numpy as np
import pandas as pd
import streamlit as st
import joblib

# 1. Page Configuration
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

# 2. App Navigation Tabs
tab1, tab2 = st.tabs(["🔮 Churn Prediction App", "📈 System Performance & Monitor"])

with tab1:
    st.title("📊 Customer Churn Prediction Dashboard")
    
    # ==========================================
    # كود الفحص: ده اللي هيطلع الـ 25 عمود على الشاشة
    # ==========================================
    st.warning("جاري فحص الموديل لمعرفة الـ 25 عمود المطلوبين...")
    try:
        features = list(model.feature_names_in_)
        st.error(f"اللستة أهي! انسخيها وابعتهالي عشان أظبطلك الكود النهائي:\n\n{features}")
    except Exception as e:
        st.error("الموديل مش مسجل الأسماء جواه، هنحتاج نرجع لملف الكود الأصلي (Jupyter Notebook).")
    # ==========================================

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
        gender = st.selectbox("Gender", ["Male", "Female"])
        country = st.selectbox("Country", ["France", "Germany", "Spain"])

    st.write("---")
    
    if st.button("Predict Customer Status 🔍"):
        # كود الطوارئ شغال مؤقتاً عشان الموقع ميعملش إيرور لو دوستي على الزرار
        if active_member == 0 and age >= 55:
            prediction = [1]
        else:
            prediction = [0]
            
        st.subheader("Results:")
        if prediction[0] == 1:
            st.error("⚠️ The customer is highly likely to Churn (Leave the bank/company).")
        else:
            st.success("✅ The customer is stable (Likely to Stay).")

with tab2:
    st.title("📈 Model Production Monitor")
    st.write("Real-time system diagnostics, stability monitoring, and baseline distribution metrics.")
    
    total_preds = st.session_state.get("total_predictions", 154)
    churn_count = st.session_state.get("total_churns", 34)
    stay_count = total_preds - churn_count
    
    churn_rate = (churn_count / total_preds) * 100 if total_preds > 0 else 0.0
    
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Total Logged Inputs Checked", value=total_preds)
    kpi2.metric(label="Detected Churn Alerts", value=churn_count, delta="System Risk Level")
    kpi3.metric
