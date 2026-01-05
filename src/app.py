import pandas as pd
import streamlit as st

df = pd.read_csv("data/bookings.csv", parse_dates=["date"])
# interpret "date" column as datetime instead of text
df["date"] = df["date"].dt.date # convert to python date objects

# make sure 'utilisation' exists
if 'utilisation' not in df.columns:
    df['utilisation'] = df['booked_courts'] / df['total_courts']

# calculate risk_score based on utilisation, creating a categorical variable
# Low: <0.6, Medium: 0.6–0.85, High: >0.85
df['risk_score'] = pd.cut(
    df['utilisation'],
    bins=[-1, 0.6, 0.85, 1],
    labels=['Low', 'Medium', 'High']
)

# streamlit UI
venue = st.selectbox("Select venue", df["venue"].unique())
# default date is the earliest date
# user can only pick valid dates 
selected_date = st.date_input(
    "Select date", 
    value=df["date"].min(),
    min_value=df["date"].min(),
    max_value=df["date"].max())

hour = st.slider("Select hour", 7, 22)
# filtering dataset to match venue, date and time 
slot = df[
    (df["venue"] == venue) & 
    (df["date"] == selected_date) &
    (df["hour"] == hour)]

if not slot.empty:
    st.write(f"Risk: {slot['risk_score'].values[0]}")
    st.write(f"Utilisation: {slot['utilisation'].values[0]*100:.1f}%")
    st.write(f"Total courts: {slot['total_courts'].values[0]}")
    available_courts = slot['total_courts'].values[0] - slot['booked_courts'].values[0]
    st.write(f"Available courts: {available_courts}")
else:
    st.write("No data for this slot")

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\venv\Scripts\activate
# pip install streamlit
# pwd
# dir or cd [folder name] then dir
# !!! streamlit run src/app.py

