import streamlit as st
import joblib
import numpy as np
import google.generativeai as genai #this is for gemini
# from streamlit_navigation_bar import st_navbar
from numpy.core.numeric import ComplexWarning
# Load the trained model
model = joblib.load('solar_power_model.pkl') 
# Create the navigation tabs
st.title("Enter the Weather Conditions for Your Area")
    # User input
apparent_temp = st.number_input('Apparent Temperature (°C)', value=20.0)
air_temp = st.number_input('Air Temperature (°C)', value=20.0)
dew_point = st.number_input('Dew Point Temperature (°C)', value=10.0)
relative_humidity = st.number_input('Relative Humidity (%)', value=50.0)
wind_speed = st.number_input('Wind Speed (m/s)', value=5.0)
wind_direction = st.number_input('Wind Direction (°)', value=90.0)
hour = st.slider('Hour of the Day', 0, 23, 12)
day = st.slider('Day of the Month', 1, 31, 15)
month = st.slider('Month', 1, 12, 6)
# Prepare the input for prediction
input_features = np.array([[apparent_temp, air_temp, dew_point, relative_humidity, 
                            wind_speed, wind_direction]])
# Define the threshold for suitability
threshold = 4
# Make prediction
predicted_output = model.predict(input_features)
# Determine if the location is suitable
suitability = "suitable" if predicted_output > threshold else "not suitable"  # Define your threshold
# Display the results
st.write(f"Predicted Solar Energy Output: {predicted_output[0]:.2f} kWh")
st.write(f"The location is {suitability} for setting up a solar plant.")
# Other Tab
# with tabs[2]:
#     st.title("Other Information")
#     st.write("This is the 'Other' tab where you can display additional information.")
#     st.write("You can add any other relevant details, such as tips on optimizing solar energy generation, etc.")   
#     from streamlit_geolocation import streamlit_geolocation

#     # Title of the app
#     st.title("Get User Location")

#     # Use the geolocation function
#     location = streamlit_geolocation()
#     default_coords = {"latitude": 40.7128, "longitude": -74.0060}
#         # Try-except block to catch the KeyError for 'coords'
#     try:
#         # Try to access the 'coords' from the location
#         user_coords = location['coords']
#         st.write(f"Your current location is:")
#         st.write(f"Latitude: {user_coords['latitude']}")
#         st.write(f"Longitude: {user_coords['longitude']}")
#     except KeyError:
#         # Handle the case when 'coords' is not available
#         # st.write("Location not available or permission denied. Showing default location.")
#         st.write(f"Default Location - Latitude: {default_coords['latitude']}, Longitude: {default_coords['longitude']}")
