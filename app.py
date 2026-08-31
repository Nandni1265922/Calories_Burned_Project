import streamlit as st
import joblib 
import pandas as pd

model = joblib.load("calories_random_forest.pkl")
preprocessor = joblib.load("calories_preprocessor.pkl")

st.title("🔥 Calories Burn Prediction")
st.write("Enter your activity details to predict calories burned.")

age_group = st.selectbox(
    "Age Group",
    ["18-24", "25-34", "35-44", "45-54", "55+"]
)


gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

activity = st.selectbox(
    "Activity Type",
    [
        "Walking",
        "Running",
        "Cycling",
        "Swimming",
        "Yoga",
        "HIIT",
        "Strength Training"
    ]
)


duration = st.number_input(
    "Duration (Minutes)",
    min_value=1,
    max_value=300,
    value=60
)


steps = st.number_input(
    "Steps",
    min_value=0,
    max_value=50000,
    value=8000
)

heart_rate = st.number_input(
    "Average Heart Rate (BPM)",
    min_value=40,
    max_value=220,
    value=120
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

water = st.number_input(
    "Water Intake (Liters)",
    min_value=0.0,
    max_value=10.0,
    value=2.0
)

weight = st.number_input(
    "Weight (KG)",
    min_value=20.0,
    max_value=200.0,
    value=60.0
)

mood = st.slider(
    "Mood Score",
    min_value=1,
    max_value=5,
    value=3
)


device = st.selectbox(
    "Device",
    [
        "Fitbit",
        "Apple Watch",
        "Mi Band",
        "Samsung Galaxy Watch",
        "Garmin"
    ]
)


date = st.date_input("Activity Date")


date = pd.to_datetime(date)

year = date.year
month = date.month
day = date.day
day_of_week = date.dayofweek
is_weekend = 1 if day_of_week >= 5 else 0

# Ab sab inputs ko exactly wahi column names dekar DataFrame me convert karenge:

input_data = pd.DataFrame({
    "Age_Group": [age_group],
    "Gender": [gender],
    "Activity_Type": [activity],
    "Duration_Min": [duration],
    "Steps": [steps],
    "Avg_Heart_Rate_BPM": [heart_rate],
    "Sleep_Hours": [sleep_hours],
    "Water_Intake_Liters": [water],
    "Weight_KG": [weight],
    "Mood_Score": [mood],
    "Device": [device],
    "Year": [year],
    "Month": [month],
    "Day": [day],
    "DayOfWeek": [day_of_week],
    "IsWeekend": [is_weekend]
})


if st.button("Predict Calories 🔥"):

    processed_data = preprocessor.transform(input_data)

    prediction = model.predict(processed_data)

    st.success(
        f"Estimated Calories Burned: {prediction[0]:.2f} kcal"
    )