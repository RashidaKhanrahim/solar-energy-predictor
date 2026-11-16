import streamlit as st
import requests
import numpy as np
import joblib
import pandas as pd
from datetime import datetime

# Load model
# Ensure 'solar_power_model.pkl' is in the same directory
try:
    model = joblib.load("solar_power_model.pkl")
except:
    st.error("Model file not found. Please ensure 'solar_power_model.pkl' exists.")

st.set_page_config(page_title="Solar Suitability Predictor", layout="wide")
st.title("☀️ Solar Plant Suitability Prediction")

# City input
city = st.text_input("Enter City Name", "Dahod")

if st.button("Predict"):
    # Using your API Key (Note: It's best practice to use st.secrets for keys)
    api_key = "88a485f926e54dd4bdc84420260405"
    # Change endpoint to 'forecast' and request 3 days
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&aqi=yes"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        st.error("❌ Invalid location. Please enter a valid city name.")
    else:
        country = data["location"]["country"]

        if country != "India":
            st.warning("⚠️ Warning: This project is optimized for India. Results elsewhere may vary.")

        # --- GPS / LOCATION INFO (from weatherapi.com response, no extra API needed) ---
        lat = data["location"]["lat"]
        lon = data["location"]["lon"]
        resolved_name = data["location"]["name"]
        region = data["location"]["region"]

        # --- DATA PROCESSING ---
        forecast_list = data["forecast"]["forecastday"]
        prediction_results = []

        for day in forecast_list:
            # Extract features (averages for the day to represent total potential)
            date = day["date"]
            avg_temp = day["day"]["avgtemp_c"]
            max_temp = day["day"]["maxtemp_c"]
            humidity = day["day"]["avghumidity"]
            # Weather API doesn't give dew point directly in daily summary,
            # so we approximate or use the first hourly record
            dew_point = day["hour"][12]["dewpoint_c"]
            wind_kph = day["day"]["maxwind_kph"]

            # Prepare features for model (matching your training columns)
            # Order: apparent_temp, air_temp, dew_point, relative_humidity, wind_speed, wind_direction
            input_features = np.array([[
                avg_temp + 2,  # Approximation for apparent temp
                avg_temp,
                dew_point,
                humidity,
                wind_kph,
                180  # Standardized wind direction if not available in day summary
            ]])

            # Prediction
            pred = model.predict(input_features)[0]
            # Clip negative values
            final_output = max(pred, 0)

            status = "Suitable ✅" if final_output > 4 else "Marginal ⚠️" if final_output > 2.5 else "Unsuitable ❌"

            prediction_results.append({
                "Date": date,
                "Condition": day["day"]["condition"]["text"],
                "Avg Temp (°C)": avg_temp,
                "Humidity (%)": humidity,
                "Output (kWh)": round(final_output, 2),
                "Status": status
            })

        # --- UI DISPLAY ---

        # 0. Location header + map (NEW)
        st.subheader("📍 Location")
        loc_col1, loc_col2 = st.columns([2, 1])
        with loc_col1:
            st.write(f"**Resolved Location:** {resolved_name}, {region}, {country}")
            st.write(f"**Coordinates:** {lat:.4f}° N, {lon:.4f}° E")
            map_df = pd.DataFrame({"lat": [lat], "lon": [lon]})
            st.map(map_df, zoom=9)
        with loc_col2:
            st.metric("Latitude", f"{lat:.4f}")
            st.metric("Longitude", f"{lon:.4f}")

        st.divider()

        # 1. 3-Day Forecast Table
        st.subheader("📅 3-Day Solar Output Forecast")
        df = pd.DataFrame(prediction_results)
        st.table(df)

        # 2. Detailed Suitability Analysis (For Today)
        st.divider()
        st.subheader("📊 Suitability Analysis Report (Today)")

        today_data = prediction_results[0]
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Predicted Output", f"{today_data['Output (kWh)']} kWh")
            st.write(f"**Weather:** {today_data['Condition']}")
            st.write(f"**Thermal Stress:** {'High' if today_data['Avg Temp (°C)'] > 35 else 'Low'}")

        with col2:
            st.write(f"**Final Verdict:** {today_data['Status']}")
            st.progress(min(today_data['Output (kWh)'] / 10, 1.0))  # Visual bar
            st.caption("Score based on daily irradiance and weather factors.")

        # Additional technical details in a table
        analysis_table = {
            "Factor": ["Cloud Cover Impact", "Temperature Efficiency", "Humidity Interference", "Wind Cooling"],
            "Status": [
                "Low" if "Sunny" in today_data["Condition"] else "Moderate",
                "Reduced" if today_data["Avg Temp (°C)"] > 30 else "Optimal",
                "High" if today_data["Humidity (%)"] > 70 else "Normal",
                "Good" if today_data["Avg Temp (°C)"] > 35 else "Minimal"
            ]
        }
        st.table(analysis_table)
        # import streamlit as st
# import requests
# import numpy as np
# import joblib
# import pandas as pd
# from datetime import datetime

# # Load model
# # Ensure 'solar_power_model.pkl' is in the same directory
# try:
#     model = joblib.load("solar_power_model.pkl")
# except:
#     st.error("Model file not found. Please ensure 'solar_power_model.pkl' exists.")

# st.set_page_config(page_title="Solar Suitability Predictor", layout="wide")
# st.title("☀️ Solar Plant Suitability Prediction")

# # City input
# city = st.text_input("Enter City Name", "Dahod")

# if st.button("Predict"):
#     # Using your API Key (Note: It's best practice to use st.secrets for keys)
#     api_key = "88a485f926e54dd4bdc84420260405"
#     # Change endpoint to 'forecast' and request 3 days
#     url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&aqi=yes"

#     response = requests.get(url)
#     data = response.json()

#     if "error" in data:
#         st.error("❌ Invalid location. Please enter a valid city name.")
#     else:
#         country = data["location"]["country"]
        
#         if country != "India":
#             st.warning("⚠️ Warning: This project is optimized for India. Results elsewhere may vary.")

#         # --- DATA PROCESSING ---
#         forecast_list = data["forecast"]["forecastday"]
#         prediction_results = []

#         for day in forecast_list:
#             # Extract features (averages for the day to represent total potential)
#             date = day["date"]
#             avg_temp = day["day"]["avgtemp_c"]
#             max_temp = day["day"]["maxtemp_c"]
#             humidity = day["day"]["avghumidity"]
#             # Weather API doesn't give dew point directly in daily summary, 
#             # so we approximate or use the first hourly record
#             dew_point = day["hour"][12]["dewpoint_c"] 
#             wind_kph = day["day"]["maxwind_kph"]
            
#             # Prepare features for model (matching your training columns)
#             # Order: apparent_temp, air_temp, dew_point, relative_humidity, wind_speed, wind_direction
#             input_features = np.array([[
#                 avg_temp + 2, # Approximation for apparent temp
#                 avg_temp,
#                 dew_point,
#                 humidity,
#                 wind_kph,
#                 180 # Standardized wind direction if not available in day summary
#             ]])

#             # Prediction
#             pred = model.predict(input_features)[0]
#             # Clip negative values
#             final_output = max(pred, 0)
            
#             status = "Suitable ✅" if final_output > 4 else "Marginal ⚠️" if final_output > 2.5 else "Unsuitable ❌"
            
#             prediction_results.append({
#                 "Date": date,
#                 "Condition": day["day"]["condition"]["text"],
#                 "Avg Temp (°C)": avg_temp,
#                 "Humidity (%)": humidity,
#                 "Output (kWh)": round(final_output, 2),
#                 "Status": status
#             })

#         # --- UI DISPLAY ---
        
#         # 1. 3-Day Forecast Table
#         st.subheader("📅 3-Day Solar Output Forecast")
#         df = pd.DataFrame(prediction_results)
#         st.table(df)

#         # 2. Detailed Suitability Analysis (For Today)
#         st.divider()
#         st.subheader("📊 Suitability Analysis Report (Today)")
        
#         today_data = prediction_results[0]
#         col1, col2 = st.columns(2)

#         with col1:
#             st.metric("Predicted Output", f"{today_data['Output (kWh)']} kWh")
#             st.write(f"**Weather:** {today_data['Condition']}")
#             st.write(f"**Thermal Stress:** {'High' if today_data['Avg Temp (°C)'] > 35 else 'Low'}")

#         with col2:
#             st.write(f"**Final Verdict:** {today_data['Status']}")
#             st.progress(min(today_data['Output (kWh)'] / 10, 1.0)) # Visual bar
#             st.caption("Score based on daily irradiance and weather factors.")

#         # Additional technical details in a table
#         analysis_table = {
#             "Factor": ["Cloud Cover Impact", "Temperature Efficiency", "Humidity Interference", "Wind Cooling"],
#             "Status": [
#                 "Low" if "Sunny" in today_data["Condition"] else "Moderate",
#                 "Reduced" if today_data["Avg Temp (°C)"] > 30 else "Optimal",
#                 "High" if today_data["Humidity (%)"] > 70 else "Normal",
#                 "Good" if today_data["Avg Temp (°C)"] > 35 else "Minimal"
#             ]
#         }
#         st.table(analysis_table)



# # import streamlit as st
# # import requests
# # import numpy as np
# # import joblib
# # import random

# # # Load model
# # model = joblib.load("solar_power_model.pkl")

# # st.title("☀ Solar Plant Suitability Prediction")

# # # City input
# # city = st.text_input("Enter City Name", "Dahod")

# # if st.button("Predict"):

# #     api_key = "88a485f926e54dd4bdc84420260405"

# #     url = f"http://api.weatherapi.com/v1/current.json?key=88a485f926e54dd4bdc84420260405&q=India&aqi=no"

# #     response = requests.get(url)
# #     data = response.json()

# #       # Check API error
# #     if "error" in data:
# #         st.error("❌ Invalid location. Please enter a valid city name.")
    
# #     else:
# #         # Check if location is in India
# #         country = data["location"]["country"]

# #         if country != "India":
# #             st.error("🚫 Sorry! This project currently supports only locations within India.")

# #         else:
# #             # Weather values
# #             current = data["current"]

# #             apparent_temp = current["feelslike_c"]
# #             air_temp = current["temp_c"]
# #             dew_point = current["dewpoint_c"]
# #             relative_humidity = current["humidity"]
# #             wind_speed = current["wind_kph"]
# #             wind_direction = current["wind_degree"]

# #             # Model input
# #             input_features = np.array([[
# #                 apparent_temp,
# #                 air_temp,
# #                 dew_point,
# #                 relative_humidity,
# #                 wind_speed,
# #                 wind_direction
# #             ]])

# #             # Base prediction
# #             predicted_output = model.predict(input_features)[0]

# #             # Add random variation
# #             final_output = predicted_output + random.uniform(-1, 1)

# #             # Prevent negative values
# #             final_output = max(final_output, 0)

# #             # Threshold
# #             threshold = 4

# #             suitability = "Suitable ✅" if final_output > threshold else "Not Suitable ❌"

# #             # Output
# #             st.subheader("Prediction Result")

# #             st.write(f"📍 Location: {city}, India")
# #             st.write(f"⚡ Predicted Solar Energy Output: {final_output:.2f} kWh")
# #             st.write(f"☀ The location is {suitability} for setting up a solar plant.")