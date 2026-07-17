import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go


from utils.preprocessing import prepare_response_data
import utils.predictor as predictor


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


st.title("🚑 Incident Response Time Prediction")

st.write("Predict ambulance response time using trained AI model.")

st.info(
    "Fill in the incident details below. "
    "The trained AI model will estimate the expected response time."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    borough = st.selectbox(
        "Borough",
        list(borough_encoder.classes_)
    )

    initial_call = st.selectbox(
        "Initial Call Type",
        list(initial_encoder.classes_)
    )

    final_call = st.selectbox(
        "Final Call Type",
        list(final_encoder.classes_)
    )

    zipcode = st.number_input(
        "Zipcode",
        min_value=10000,
        max_value=99999,
        value=10457
    )

    dispatch_area = st.selectbox(
        "Dispatch Area",
        list(dispatch_encoder.classes_)
    )

with col2:

    hour = st.slider("Hour", 0, 23, 12)

    month = st.slider("Month", 1, 12, 1)

    weekday = st.selectbox(
        "Weekday",
        [0,1,2,3,4,5,6]
    )

    year = st.number_input(
        "Year",
        value=2025
    )

    incident_duration = st.number_input(
        "Incident Duration (sec)",
        value=600
    )

    dispatch_delay = st.number_input(
        "Dispatch Delay (sec)",
        value=30
    )

st.divider()

if st.button("Predict Response Time"):

    sample = pd.DataFrame({

        "initial_call_type": [initial_call],
        "final_call_type": [final_call],
        "zipcode": [zipcode],
        "borough": [borough],
        "incident_dispatch_area": [dispatch_area],
        "hour": [hour],
        "month": [month],
        "weekday": [weekday],
        "Year": [year],
        "incident_duration": [incident_duration],
        "dispatch_delay": [dispatch_delay]

    })

    # Preprocess
    processed = prepare_response_data(sample)

    

    print("TYPE OF predictor.response_model")
    print(type(predictor.response_model))

    print("OBJECT")
    print(predictor.response_model)

    print("HAS PREDICT")
    print(hasattr(predictor.response_model, "predict"))

    print("ID")
    print(id(predictor.response_model))

    

    prediction = predictor.predict_response(processed)

    
    if st.button("🚀 Predict Response Time"):

    
     st.success(f"Predicted Response Time: {prediction:.2f} seconds")

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=float(prediction),
            title={"text": "Response Time (sec)"},
            gauge={
                "axis": {"range": [0, 600]}
            }
        )
    )

    st.plotly_chart(fig, use_container_width=True)