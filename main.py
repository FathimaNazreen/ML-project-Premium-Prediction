# Health Insurance Cost Predictor App
# Project by Fathima Nazreen | Netcom Academy

import streamlit as st
import pandas as pd
import io
from prediction_helper import predict

# Sidebar with Project Info
with st.sidebar:
    st.markdown("""
    ## 📋 Project Info
    **Project:** Health Insurance Cost Predictor  
    **By:** Fathima Nazreen  
    **Academy:** Netcom Academy  
    **Tech Stack:** Python, Streamlit, Machine Learning  
    **Note:** This model predicts insurance cost based on personal, health, and financial data.  
    """)

# Optional Dark Mode
if st.toggle("🌙 Dark Mode"):
    st.markdown("""
        <style>
            body {
                background-color: #1e1e1e;
                color: white;
            }
            .stButton>button {
                background-color: #444;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)

# App title and instructions
st.title('Health Insurance Cost Predictor')
st.image("picture_health.png", width=150)
st.markdown("💡 *Fill the form below to estimate your health insurance cost*")
st.subheader("ℹ️ How This App Works")
st.write("This app uses a trained Machine Learning model to estimate the cost of health insurance. It considers various factors like age, income, smoking habits, and medical history.")

# Categorical options for selectboxes
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Form container
with st.container():
    st.subheader("📝 Fill Your Details")
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

    with row2[0]:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[1]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

    with row3[0]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row3[1]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with row3[2]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    with row4[0]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row4[1]:
        region = st.selectbox('Region', categorical_options['Region'])
    with row4[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction logic
if st.button('Predict'):
    prediction = predict(input_dict)

    st.subheader("🔍 Input Summary")
    for key, value in input_dict.items():
        st.write(f"**{key}**: {value}")

    st.subheader("💸 Predicted Health Insurance Cost")
    st.success(f"₹{prediction:,.2f}")

    # Optional Download CSV Button
    result_data = input_dict.copy()
    result_data['Predicted Cost'] = prediction
    df = pd.DataFrame([result_data])
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    st.download_button("📥 Download CSV Report", buffer.getvalue(), file_name="insurance_prediction.csv", mime="text/csv")

# Footer
st.markdown("""
---
📊 Powered by Machine Learning | © 2025 Fathima Nazreen | Netcom Academy
""")
