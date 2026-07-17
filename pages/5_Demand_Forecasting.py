import os
import joblib
import pandas as pd
import streamlit as st

import utils.preprocessing as prep
from utils.predictor import predict_demand


st.set_page_config(
    page_title="Demand Forecasting",
    page_icon="📈",
    layout="wide"
)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")


borough_encoder = joblib.load(
    os.path.join(
        ARTIFACT_DIR,
        "borough_encoder.pkl"
    )
)


st.title("📈 Ambulance Demand Forecasting")

st.write(
    "Predict expected ambulance demand based on time and location."
)

st.divider()


col1, col2 = st.columns(2)


with col1:

    hour = st.slider(
        "Hour",
        0,
        23,
        12
    )


    month = st.slider(
        "Month",
        1,
        12,
        1
    )


    weekday = st.selectbox(
        "Weekday",
        [0,1,2,3,4,5,6],
        format_func=lambda x:
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ][x]
    )


    year = st.number_input(
        "Year",
        min_value=2020,
        max_value=2035,
        value=2025
    )



with col2:


    borough = st.selectbox(
        "Borough",
        borough_encoder.classes_
    )


    historical_calls = st.number_input(
        "Historical Calls",
        min_value=0,
        value=100
    )


    peak_hour = st.selectbox(
        "Peak Hour",
        [0,1],
        format_func=lambda x:
        "Yes" if x == 1 else "No"
    )


    night_shift = st.selectbox(
        "Night Shift",
        [0,1],
        format_func=lambda x:
        "Yes" if x == 1 else "No"
    )



st.divider()


if st.button(
    "📈 Forecast Demand",
    use_container_width=True
):


    data = pd.DataFrame(
        [{
            "borough": borough,

            "hour": hour,
            "month": month,
            "weekday": weekday,
            "Year": year,

            "historical_calls": historical_calls,

            "peak_hour": peak_hour,
            "night_shift": night_shift
        }]
    )


    processed = prep.prepare_demand_data(data)


    prediction = predict_demand(
        processed
    )


    st.success(
        f"🚑 Expected Ambulance Calls: {prediction:.0f}"
    )


    st.metric(
        "Predicted Demand",
        f"{prediction:.0f} Calls"
    )