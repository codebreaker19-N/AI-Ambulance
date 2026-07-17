import streamlit as st

st.set_page_config(
    page_title="AI Ambulance Intelligence System",
    page_icon="🚑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* Main Page */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1250px;
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background: rgba(255,255,255,0.75);

    backdrop-filter: blur(10px);

    border-radius:20px;
    padding:20px;
    
    border:1px solid #E5E7EB;
    box-shadow:0px 4px 12px rgba(0,0,0,.08);
    transition:.3s;

    transform:translateY(-5px);
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    height:52px;
    border:none;
    background:#2563EB;
    color:white;
    font-weight:bold;
    font-size:16px;
    
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* Input Boxes */
.stSelectbox,
.stNumberInput,
.stTextInput{
    border-radius:12px;
}

/* Success Box */
.stSuccess{
    border-radius:15px;
}

/* Info Box */
.stInfo{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown("# 🚑 AI Ambulance Intelligence System")

st.caption(
    "AI-Powered Emergency Decision Support Platform"
)

# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""

<div class="hero">

<h2> Smart Emergency Prediction Dashboard</h2>

<p style="font-size:18px">

Predict

• Incident Response Time

• Dispatch Time

• Estimated Time of Arrival (ETA)

• Delay Classification

• Future Ambulance Demand

using Machine Learning.

</p>

</div>

""",unsafe_allow_html=True)

st.write("")

# ============================================================
# METRICS
# ============================================================

col1,col2,col3,col4=st.columns(4)

with col1:

    st.metric(
        "AI Models",
        "5"
    )

with col2:

    st.metric(
        "⚡ Prediction Speed",
        "<1 sec"
    )

with col3:

    st.metric(
        "🎯 Best R² Score",
        "0.9277"
    )

with col4:

    st.metric(
        "📊 Dataset",
        "200K+"
    )

st.divider()

# ============================================================
# AI MODULES
# ============================================================

st.subheader("🤖 AI Prediction Modules")

col1,col2=st.columns(2)

with col1:

    st.markdown("""

<div class="module-card">

<h4>🚑 Incident Response Prediction</h4>

<b>Algorithm</b>

XGBoost Regression

<br><br>

Predicts ambulance response time.

</div>

""",unsafe_allow_html=True)

    st.write("")

    st.markdown("""

<div class="module-card">

<h4>📍 ETA Prediction</h4>

<b>Algorithm</b>

XGBoost Regression

<br><br>

Predicts ambulance arrival time.

</div>

""",unsafe_allow_html=True)

    st.write("")

    st.markdown("""

<div class="module-card">

<h4>📈 Demand Forecasting</h4>

<b>Algorithm</b>

XGBoost Regression

<br><br>

Forecasts future ambulance demand.

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="module-card">

<h4>📡 Dispatch Time Prediction</h4>

<b>Algorithm</b>

XGBoost Regression

<br><br>

Predicts dispatch processing time.

</div>

""",unsafe_allow_html=True)

    st.write("")

    st.markdown("""

<div class="module-card">

<h4>⏱ Delay Classification</h4>

<b>Algorithm</b>

Random Forest

<br><br>

Classifies delayed incidents.

</div>

""",unsafe_allow_html=True)
    


import plotly.express as px
import pandas as pd

response_df = pd.DataFrame({
    "Hour":[0,3,6,9,12,15,18,21],
    "Response":[420,390,320,250,280,310,350,400]
})

fig = px.line(
    response_df,
    x="Hour",
    y="Response",
    markers=True,
    title="Average Response Time by Hour"
)

st.plotly_chart(fig, use_container_width=True)
    
# ============================================================
# KEY FEATURES
# ============================================================

st.divider()

st.subheader("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.markdown("""
### 🚑 Emergency Prediction

- ✅ Incident Response Prediction
- ✅ Dispatch Time Prediction
- ✅ ETA Prediction
- ✅ Delay Classification
- ✅ Ambulance Demand Forecasting
""")

with col2:

    with st.container(border=True):

        st.markdown("""
### 🤖 AI Capabilities

- ✅ Machine Learning Models
- ✅ Feature Engineering
- ✅ Interactive Dashboard
- ✅ Real-Time Predictions
- ✅ Decision Support System
""")
        

demand_df = pd.DataFrame({

    "Day":[
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],

    "Demand":[
        120,
        135,
        150,
        160,
        190,
        210,
        170
    ]
})

fig = px.bar(
    demand_df,
    x="Day",
    y="Demand",
    title="Weekly Ambulance Demand"
)

st.plotly_chart(fig,use_container_width=True)


# ============================================================
# WORKFLOW
# ============================================================

st.divider()

st.subheader("🔄 AI Prediction Workflow")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.success("📞\n\nEmergency\nCall")

with col2:
    st.info("📋\n\nIncident\nDetails")

with col3:
    st.warning("🤖\n\nMachine Learning\nPrediction")

with col4:
    st.info("🚑\n\nResponse\nPlanning")

with col5:
    st.success("✅\n\nDecision\nSupport")


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.divider()

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    with st.container(border=True):

        st.markdown("""
### 🤖 Machine Learning

- XGBoost
- Random Forest
- Scikit-Learn
""")


with tech2:

    with st.container(border=True):

        st.markdown("""
### 🐍 Python

- Pandas
- NumPy
- Joblib
""")


with tech3:

    with st.container(border=True):

        st.markdown("""
### 🌐 Deployment

- Streamlit
- Python
- Interactive Dashboard
""")


# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================

st.divider()

st.subheader("📊 Project Highlights")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🚑 Prediction Modules", "5")

with c2:
    st.metric("📈 ML Algorithms", "2")

with c3:
    st.metric("⚡ Prediction Time", "< 1 Second")


# ============================================================
# READY STATUS
# ============================================================

st.divider()

st.success("""
## ✅ System Ready

All trained Machine Learning models have been loaded successfully.

Use the sidebar to access:

- 🚑 Incident Response Prediction
- 📡 Dispatch Prediction
- 📍 ETA Prediction
- ⏱ Delay Classification
- 📈 Demand Forecasting
""")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
"""
<div class="footer">

<h4>🚑 AI Ambulance Intelligence System</h4>

<p>
AI-Powered Emergency Decision Support Platform
</p>

<p>
Built with ❤️ using
Python • Streamlit • XGBoost • Random Forest • Scikit-Learn
</p>

</div>
""",
unsafe_allow_html=True
)