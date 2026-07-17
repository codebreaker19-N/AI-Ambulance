import os
import joblib
import streamlit as st

import utils.preprocessing as prep




print("=" * 60)
print(prep.__file__)
print("=" * 60)
from utils.predictor import predict_dispatch


st.set_page_config(
    page_title="Dispatch Time Prediction",
    page_icon="🚑",
    layout="wide"
)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")

borough_encoder = joblib.load(
    os.path.join(ARTIFACT_DIR, "borough_encoder.pkl")
)

initial_encoder = joblib.load(
    os.path.join(ARTIFACT_DIR, "initial_call_type_encoder.pkl")
)

final_encoder = joblib.load(
    os.path.join(ARTIFACT_DIR, "final_call_type_encoder.pkl")
)

dispatch_encoder = joblib.load(
    os.path.join(ARTIFACT_DIR, "incident_dispatch_area_encoder.pkl")
)


st.title("Dispatch Time Prediction")

st.write(
    "Predict ambulance dispatch time using the trained AI model."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    dispatch_delay = st.number_input(
        "Dispatch Delay (seconds)",
        min_value=0.0,
        value=60.0
    )

    incident_duration = st.number_input(
        "Incident Duration (seconds)",
        min_value=0.0,
        value=1200.0
    )

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
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][x]
    )

    year = st.number_input(
        "Year",
        min_value=2020,
        max_value=2035,
        value=2025
    )

with col2:

    zipcode = st.number_input(
        "Zipcode",
        min_value=10000,
        max_value=99999,
        value=10457
    )

    borough = st.selectbox(
        "Borough",
        borough_encoder.classes_
    )

    initial_call_type = st.selectbox(
        "Initial Call Type",
        initial_encoder.classes_
    )

    final_call_type = st.selectbox(
        "Final Call Type",
        final_encoder.classes_
    )

    incident_dispatch_area = st.selectbox(
        "Incident Dispatch Area",
        dispatch_encoder.classes_
    )

st.divider()


if st.button(
    "Predict Dispatch Time",
    use_container_width=True
):

    data = {

        "dispatch_delay": dispatch_delay,
        "incident_duration": incident_duration,
        "hour": hour,
        "month": month,
        "weekday": weekday,
        "Year": year,

        "zipcode": zipcode,
        "borough": borough,
        "initial_call_type": initial_call_type,
        "final_call_type": final_call_type,
        "incident_dispatch_area": incident_dispatch_area

    }

    processed = prep.prepare_dispatch_data(data)
    

    prediction = predict_dispatch(processed)

    st.success(
        f" Estimated Dispatch Time: **{prediction:.2f} seconds**"
    )

    st.metric(
        "Estimated Time",
        f"{prediction/60:.2f} minutes"
    )