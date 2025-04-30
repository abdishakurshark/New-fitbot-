
import streamlit as st
import numpy as np
import joblib
import base64

# Set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the background setter
set_background("My ChatGPT image.png")

# Load trained model
model = joblib.load("decision_tree_model.pkl")

st.title("🏋️‍♂️ FitBot: Gym Workout Recommender")

# Input form
age = st.number_input('Age', 10, 100)
gender = st.selectbox('Gender', ['Male', 'Female'])
weight = st.number_input('Weight (kg)', 30.0, 200.0)
height = st.number_input('Height (m)', 1.0, 2.5)
max_bpm = st.number_input('Max BPM', 100, 250)
avg_bpm = st.number_input('Avg BPM', 50, 200)
resting_bpm = st.number_input('Resting BPM', 40, 100)
session_duration = st.number_input('Session Duration (hours)', 0.5, 5.0)
calories_burned = st.number_input('Calories Burned', 100.0, 5000.0)
fat_percentage = st.number_input('Fat Percentage', 5.0, 60.0)
water_intake = st.number_input('Water Intake (liters)', 0.5, 10.0)
workout_frequency = st.slider('Workout Frequency (days/week)', 1, 7)
experience_level = st.slider('Experience Level (1=Beginner, 2=Intermediate, 3=Advanced)', 1, 3)
bmi = st.number_input('BMI', 10.0, 50.0)

# Encode gender
gender_encoded = 1 if gender == 'Male' else 0

if st.button('Predict Workout Type'):
    input_data = np.array([[age, gender_encoded, weight, height, max_bpm, avg_bpm,
                            resting_bpm, session_duration, calories_burned,
                            fat_percentage, water_intake, workout_frequency,
                            experience_level, bmi]])
    prediction = model.predict(input_data)[0]
    workout_types = ['Cardio', 'Strength', 'Yoga', 'HIIT']  # Adjust if needed
    st.success(f"💪 Recommended Workout Type: {workout_types[prediction]}")
