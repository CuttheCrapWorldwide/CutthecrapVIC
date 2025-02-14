import streamlit as st
import pandas as pd

# --- STREAMLIT APP HEADER ---
st.title("🏡 Fair Price Property Calculator")
st.write("Calculate a **fair, speculation-free** property price & estimate your **stamp duty**.")

# --- USER INPUTS ---
st.subheader("1️⃣ Land Details")
land_area = st.number_input(
    "Total Land Area (sqm)", 
    min_value=1, value=306, step=1,
    help="Enter the **total** plot size (do not subtract building area)."
)

st.subheader("2️⃣ Building Details")
num_floors = st.number_input(
    "Number of Floors", 
    min_value=1, value=1, step=1,
    help="For a single-story home, enter **1**. For a two-story home, enter **2**, and so on."
)
building_area_per_floor = st.number_input(
    "Building Area Per Floor (sqm)", 
    min_value=1, value=75, step=1,
    help="Enter the **size of one floor** of the building."
)

# Automatically calculate total building area
total_building_area = num_floors * building_area_per_floor
st.write(f"🏠 **Total Building Area:** {total_building_area} sqm")

st.subheader("3️⃣ Cost Inputs")

# --- LAND VALUE INPUT + GOVERNMENT LINKS ---
st.write("💡 **Need help finding your land value?** Click your state below:")
st.markdown(
    """
    - [📍 **Victoria (VIC) - Landchecker**](https://landchecker.com.au/)
    - [📍 **New South Wales (NSW) - Valuer General**](https://www.valuergeneral.nsw.gov.au/)
    - [📍 **Queensland (QLD) - QLD Globe**](https://www.qld.gov.au/environment/land/title/land-valuations)
    - [📍 **South Australia (SA) - SAILIS**](https://sailis.lssa.com.au/home/auth/login)
    - [📍 **Western Australia (WA) - Landgate**](https://www.landgate.wa.gov.au/property-reports)
    - [📍 **Tasmania (TAS) - LISTmap**](https://www.thelist.tas.gov.au/)
    - [📍 **Northern Territory (NT) - NT Government**](https://nt.gov.au/property/land-valuations)
    - [📍 **Australian Capital Territory (ACT) - ACT Revenue Office**](https://www.revenue.act.gov.au/)
    """
)

land_value = st.number_input(
    "Land Value ($ per sqm)", 
    min_value=1, value=3000, step=100,
    help="Enter the **value of the land per sqm** (from your official state website above)."
)

building_cost = st.number_input(
    "Building Cost ($ per sqm)", 
    min_value=1, value=2500, step=100,
    help="Enter the **construction cost per sqm** (based on local build estimates)."
)

# --- PROPERTY PRICE CALCULATION ---
total_fair_price = (land_area * land_value) + (total_building_area * building_cost)

# --- STAMP DUTY CALCULATION ---
st.subheader("4️⃣ Stamp Duty Estimation")

state = st.selectbox(
    "Select Your State for Stamp Duty Calculation",
    ["Victoria (VIC)", "New South Wales (NSW)", "Queensland (QLD)", "South Australia (SA)",
     "Western Australia (WA)", "Tasmania (TAS)", "Northern Territory (NT)", "Australian Capital Territory (ACT)"]
)

# Stamp Duty Rates (2024 Estimates)
stamp_duty_rates = {
    "Victoria (VIC)": 0.055,
    "New South Wales (NSW)": 0.053,
    "Queensland (QLD)": 0.049,
    "South Australia (SA)": 0.045,
    "Western Australia (WA)": 0.047,
    "Tasmania (TAS)": 0.042,
    "Northern Territory (NT)": 0.050,
    "Australian Capital Territory (ACT)": 0.048
}

stamp_duty = total_fair_price * stamp_duty_rates[state]
st.write(f"📝 **Estimated Stamp Duty in {state}:** ${stamp_duty:,.2f}")

# --- STAMP DUTY EXEMPTIONS ---
st.write("💡 **Possible Stamp Duty Exemptions:**")
st.markdown(
    """
    - **First Home Buyers** (some states offer full or partial exemptions)
    - **Pensioners / Seniors** (varies by state)
    - **Off-the-plan purchases** (in some cases)
    - **Vacant Land / New Builds** (exemptions may apply)
    - **Family Transfers** (for certain immediate family members)
    - **Charity / Non-profit purchases** (where applicable)
    
    📌 **Check your official state website for full exemption rules!**
    """
)

# --- DISPLAY FINAL PROPERTY PRICE & STAMP DUTY ---
if st.button("Calculate Fair Price & Stamp Duty"):
    st.subheader(f"🏡 Fair Property Price: **${total_fair_price:,.2f}**")
    st.subheader(f"📜 Estimated Stamp Duty: **${stamp_duty:,.2f}**")

# --- GENERATE REPORT (Downloadable) ---
if st.button("📥 Download Property Report"):
    report_data = pd.DataFrame({
        "Category": ["Total Fair Property Price", "Estimated Stamp Duty", "State"],
        "Amount": [f"${total_fair_price:,.2f}", f"${stamp_duty:,.2f}", state]
    })
    
    # Convert to CSV for download
    report_csv = report_data.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="Download Report as CSV",
        data=report_csv,
        file_name="FairPrice_Report.csv",
        mime="text/csv"
    )

# --- LEGAL DISCLAIMER ---
st.markdown(
    """
    ---
    **⚠️ Legal Disclaimer:**  
    The calculated figures are for **informational purposes only**.  
    FairPrice does not guarantee accuracy and these figures **must not be relied upon** for financial, legal, or investment decisions.  
    Always consult official government resources or financial advisors before making property-related decisions.
    """
)

