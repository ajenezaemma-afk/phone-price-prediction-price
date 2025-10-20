import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('phone_sales_data.sav', 'rb'))

# Function to predict phone price
def phone_price_prediction(screen_size, ram, storage, battery_capacity, camera_quality):
    new_phone = pd.DataFrame([{
        'Screen Size (inches)': screen_size,
        'RAM (GB)': ram,
        'Storage (GB)': storage,
        'Battery Capacity (mAh)': battery_capacity,
        'Camera Quality (MP)': camera_quality
    }])
    predicted_price = loaded_model.predict(new_phone)
    return predicted_price[0]

# Main Streamlit app
def main():
    st.title("📱 Phone Price Prediction App")
    

    # Number input fields (safe and validated automatically)
    screen_size = st.number_input('Screen Size (inches)', min_value=3.0, max_value=10.0, value=6.2, step=0.1)
    ram = st.number_input('RAM (GB)', min_value=1, max_value=64, value=4, step=1)
    storage = st.number_input('Storage (GB)', min_value=8, max_value=1024, value=64, step=8)
    battery_capacity = st.number_input('Battery Capacity (mAh)', min_value=500, max_value=10000, value=4000, step=100)
    camera_quality = st.number_input('Camera Quality (MP)', min_value=1, max_value=200, value=48, step=1)

    if st.button('Predict Price'):
        # Predict directly (no try-except needed)
        price = phone_price_prediction(screen_size, ram, storage, battery_capacity, camera_quality)
        st.success(f"💰 The predicted price for the phone is: *${price:,.2f}*")

if _name_ == '_main_':
    main()

