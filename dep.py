import streamlit as st
import numpy as np
import pandas as pd
import pickle


# Load the trained model
@st.cache_resource

def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

st.title("☀️ Solar Power Prediction ")
st.sidebar.header("🔧 Input Parameters")

def user_input():
    distance_to_solar_noon = st.sidebar.slider("Distance to Solar Noon", min_value=0.05, max_value=1.14, value=0.5)
    temperature = st.sidebar.slider("Temperature (°F)", min_value=42, max_value=78, value=58)
    wind_direction = st.sidebar.slider("Wind Direction (°)", min_value=1, max_value=36, value=25)
    wind_speed = st.sidebar.slider("Wind Speed (m/s)", min_value=1.1, max_value=26.6, value=10.1)
    sky_cover = st.sidebar.selectbox("Sky Cover", options=[0, 1, 2, 3, 4], index=2)
    visibility = st.sidebar.slider("Visibility (km)", min_value=0.1, max_value=16.1, value=10.1)
    humidity = st.sidebar.slider("Humidity (%)", min_value=14, max_value=100, value=73)
    avg_wind_speed = st.sidebar.slider("Avg Wind Speed (m/s)", min_value=0, max_value=40, value=10)
    avg_pressure = st.sidebar.slider("Avg Pressure (hPa)", min_value=29.48, max_value=30.53, value=30.02)
    
    return np.array([[distance_to_solar_noon, temperature, wind_direction, wind_speed, sky_cover, visibility, humidity, avg_wind_speed, avg_pressure]])

input_data = user_input()

if st.sidebar.button("Predict Solar Power"):
    prediction = model.predict(input_data)[0]
    st.metric("Predicted Solar Power Output (kW)", abs(round(prediction, 2)))


# Footer
st.markdown("---")  

st.markdown(
    "<h3>📌 Model Overview</h3>"
    "<p style='font-size:20px;'>This model leverages <b>XGBoost</b> and advanced machine learning techniques to analyze historical weather patterns, solar radiation, temperature, and other environmental factors. By identifying key patterns in solar energy generation, the model provides accurate power output predictions 📊, helping stakeholders optimize energy distribution and reduce reliance on non-renewable sources.</p>"
    "<p style='font-size:20px;'>This predictive system is particularly useful for solar farm operators, grid managers, and renewable energy researchers, enabling better decision-making for energy planning, storage management, and efficiency improvements. 🌱⚡</p>",
    unsafe_allow_html=True
)

st.markdown("👨‍💻 Deployed by Vamc Yadav with ❤️ Using Streamlit Cloud Community ☁")
