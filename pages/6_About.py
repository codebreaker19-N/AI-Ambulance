import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About AI Ambulance Intelligence System")

st.markdown("""
### 🚑 AI-Powered Emergency Decision Support Platform

The **AI Ambulance Intelligence System** is a Machine Learning-based decision support platform designed to assist emergency medical services by predicting critical operational metrics.

The goal of this project is to improve emergency response efficiency, reduce dispatch delays, optimize ambulance allocation, and support data-driven decision making.
""")

st.divider()

# ---------------------------------------------------------
# Project Modules
# ---------------------------------------------------------

st.subheader("🚀 Project Modules")

col1, col2 = st.columns(2)

with col1:
    st.success("""
🚑 Incident Response Prediction

Predicts the estimated response time for emergency incidents.
""")

    st.success("""
📡 Dispatch Time Prediction

Predicts ambulance dispatch processing time.
""")

    st.success("""
📍 ETA Prediction

Predicts ambulance arrival time.
""")

with col2:
    st.success("""
⏱ Delay Classification

Classifies whether an emergency response is delayed.
""")

    st.success("""
📈 Demand Forecasting

Forecasts future ambulance demand using historical trends.
""")

st.divider()

# ---------------------------------------------------------
# Machine Learning Models
# ---------------------------------------------------------

st.subheader("🤖 Machine Learning Models")

st.markdown("""
| Module | Algorithm | Type |
|--------|-----------|------|
| Incident Response | XGBoost | Regression |
| Dispatch Time | XGBoost | Regression |
| ETA Prediction | XGBoost | Regression |
| Delay Classification | Random Forest | Classification |
| Demand Forecasting | XGBoost | Regression |
""")

st.divider()

# ---------------------------------------------------------
# Dataset
# ---------------------------------------------------------

st.subheader("📊 Dataset")

st.info("""
Dataset Used:

**NYC EMS Incident Dispatch Data**

The dataset contains emergency incident records including:

- Incident Time
- Borough
- ZIP Code
- Dispatch Area
- Initial Call Type
- Final Call Type
- Ambulance Assignment
- Arrival Time
- Response Duration
""")

st.divider()

# ---------------------------------------------------------
# Feature Engineering
# ---------------------------------------------------------

st.subheader("⚙️ Feature Engineering")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
✅ Peak Hour

✅ Night Shift

✅ Weekend

✅ Office Hours

✅ Rush Hour
""")

with col2:

    st.markdown("""
✅ ZIP Frequency

✅ Borough Frequency

✅ Dispatch Frequency

✅ Interaction Features
""")

st.divider()

# ---------------------------------------------------------
# Tech Stack
# ---------------------------------------------------------

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.info("""
### Programming

- Python
- Pandas
- NumPy
""")

with tech2:

    st.info("""
### Machine Learning

- XGBoost
- Random Forest
- Scikit-Learn
""")

with tech3:

    st.info("""
### Deployment

- Streamlit
- Joblib
- Plotly
""")

st.divider()

# ---------------------------------------------------------
# Project Highlights
# ---------------------------------------------------------

st.subheader("📈 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("ML Models", "5")

with c2:
    st.metric("Algorithms", "2")

with c3:
    st.metric("Deployment", "Streamlit")

with c4:
    st.metric("Best R²", "0.9277")

st.divider()

# ---------------------------------------------------------
# Future Scope
# ---------------------------------------------------------

st.subheader("🚀 Future Scope")

st.markdown("""
- Live ambulance tracking using GPS
- Real-time traffic integration
- Deep Learning based prediction
- Multi-city deployment
- Cloud deployment
- Hospital availability prediction
- Route optimization
""")

st.divider()

# ---------------------------------------------------------
# Developer
# ---------------------------------------------------------


st.divider()

st.caption("🚑 AI Ambulance Intelligence System | Built with ❤️ using Python, Streamlit & Machine Learning")