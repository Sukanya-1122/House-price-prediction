import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1.0, 5.0, 2.0)
sqft_living = st.number_input("Living Area (sqft)", 500, 10000, 1500)
sqft_lot = st.number_input("Lot Size (sqft)", 500, 100000, 5000)
floors = st.number_input("Floors", 1.0, 3.0, 1.0)
waterfront = st.selectbox("Waterfront", [0,1])
view = st.slider("View Rating",0,4,0)
condition = st.slider("Condition",1,5,3)
sqft_above = st.number_input("Sqft Above",500,10000,1500)
sqft_basement = st.number_input("Basement Sqft",0,5000,0)
yr_built = st.number_input("Year Built",1900,2025,1990)
yr_renovated = st.number_input("Year Renovated",0,2025,0)

if st.button("Predict Price"):

    features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot,
                          floors, waterfront, view, condition,
                          sqft_above, sqft_basement, yr_built, yr_renovated]])

    prediction = model.predict(features)

    st.success(f"💰 Predicted House Price: ${prediction[0]:,.2f}")