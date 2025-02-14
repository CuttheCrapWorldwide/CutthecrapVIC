import streamlit as st
import pandas as pd

# --- STREAMLIT APP HEADER ---
st.title("🏡 Fair Price Property Calculator")
st.write("Tired of property speculation nonsense? **Get the real, no-BS property price here.**")

# --- USER INPUTS ---
st.subheader("1️⃣ Land Details")
land_area = st.number_input(
    "📏 Total Land Area (sqm)", 
    min_value=1, value=1, step=1,
    help="The whole dang block. Don't subtract anything. Just the total land area."
)

st.subheader("2️⃣ Building Details")
num_floors = st.number_input(
    "🏗 Number of Floors", 
    min_value=1, value=1, step=1,
    help="Enter **how many levels** your house has. Yes, even if you have an attic where you hide Christmas decorations."
)

# Dynamic Floor Size Inputs
floor_sizes = []
for i in range(num_floors):
    size = st.number_input(
        f"🏠 Floor {i+1} Size (sqm)", 
        min_value=1, value=1, step=1,
        help=f"How big is floor {i+1}? If it's a shoebox, just be honest."
    )
    floor_sizes.append(size)

# Calculate total building area
total_building_area = sum(floor_sizes)
st.write(f"🏠 **Total Building Area:** {total_building_area} sqm. Nice digs!")

st.subheader("3️⃣ Cost Inputs")

# --- LAND VALUE INPUT + GOVERNMENT LINKS ---
st.write("💡 **Don't know your land value?** Click your state below:")
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
    "💰 Land Value ($ per sqm)", 
    min_value=1, value=3000, step=100,
    help="Find this on your council rates notice or just guess wildly."
)

building_cost = st.number_input(
    "🔨 Building Cost ($ per sqm)", 
    min_value=1, value=2500, step=100,
    help="How much did it cost (or would it cost) to build? Be real. Put $2500 if you ain't sure."
)

# --- PROPERTY PRICE CALCULATION ---
total_fair_price = (land_area * land_value) + (total_building_area * building_cost)

# --- STAMP DUTY CALCULATION ---
st.subheader("4️⃣ Stamp Duty (The Taxman Wants His Cut)")

state = st.selectbox(
    "📍 Select Your State for Stamp Duty Calculation",
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
st.write(f"📜 **Estimated Stamp Duty in {state}:** ${stamp_duty:,.2f}")

# --- STAMP DUTY EXEMPTIONS ---
st.write("💡 **Could You Dodge Stamp Duty?**")
st.markdown(
    """
    - **First Home Buyers** (Gov might cut you a break)
    - **Pensioners / Seniors** (Old age perks)
    - **Off-the-plan purchases** (Some lucky ones get a discount)
    - **Vacant Land / New Builds** (No existing home = possible lower tax)
    - **Family Transfers** (Parents giving you a free house? Nice.)
    - **Charity / Non-profit purchases** (If you’re literally a saint)

    📌 **Check your official state website for actual rules.**
    """
)

# --- DISPLAY FINAL PROPERTY PRICE & STAMP DUTY ---
if st.button("🎉 Show My Fair Property Price!"):
    st.subheader(f"🏡 **Fair Property Price:** ${total_fair_price:,.2f}")
    st.subheader(f"📜 **Estimated Stamp Duty:** ${stamp_duty:,.2f}")

# --- GENERATE REPORT (Downloadable) ---
if st.button("📥 Download My Property Report"):
    report_data = pd.DataFrame({
        "Category": ["Total Fair Property Price", "Estimated Stamp Duty", "State"],
        "Amount": [f"${total_fair_price:,.2f}", f"${stamp_duty:,.2f}", state]
    })
    
    # Convert to CSV for download
    report_csv = report_data.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Download Report as CSV",
        data=report_csv,
        file_name="FairPrice_Report.csv",
        mime="text/csv"
    )

# --- LEGAL DISCLAIMER ---
st.markdown(
    """
    ---
    **⚠️ Legal Disclaimer:**  
    This calculator **guesses things** based on what you enter. It’s **not legal advice**.  
    FairPrice **doesn't take responsibility** for errors, and this figure **should not** be relied upon for financial, legal, or investment decisions.  
    The taxman, real estate agents, and the bank probably won’t listen to this tool. Proceed with caution.
    """
)

