import streamlit as st
import pandas as pd

st.title("Fair Property Price Calculator")
st.write("Enter details below to get a fair property price per sqm.")

location = st.text_input("Enter Suburb Name")
land_area = st.number_input("Enter Land Area (sqm)", min_value=1)
building_area = st.number_input("Enter Building Area (sqm)", min_value=1)

if st.button("Calculate"):
    price = (land_area * 7000 + building_area * 2500) / land_area
    st.write(f"Fair Price: ${price:.2f} per sqm")
