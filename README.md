# 🚑 AI Ambulance Intelligence System

> **AI-Powered Emergency Decision Support System**
>
> Predict ambulance response time, dispatch delay, ETA, incident delay, and emergency demand using Machine Learning.

---

## 🌐 Live Demo

🔗 **Live Application**

https://ai-ambulance-intelligence.streamlit.app/

📂 **GitHub Repository**

https://github.com/codebreaker19-N/AI-Ambulance

---

# 📖 Project Overview

The **AI Ambulance Intelligence System** is an end-to-end Machine Learning application developed to improve emergency medical service decision-making.

The system predicts multiple operational metrics such as:

- 🚑 Incident Response Time
- 📞 Dispatch Response Time
- 🗺 Estimated Travel Time (ETA)
- ⚠ Delay Classification
- 📈 Emergency Demand Forecasting

The application provides an interactive Streamlit dashboard where users can enter incident details and obtain real-time predictions.

---

# ✨ Features

✅ Incident Response Time Prediction

✅ Dispatch Time Prediction

✅ ETA Prediction

✅ Delay Classification

✅ Demand Forecasting

✅ Interactive Streamlit Dashboard

✅ Multiple ML Models

✅ Feature Engineering Pipeline

✅ Beautiful Visual Analytics

---

# 📊 Dataset

**Dataset Source**

NYC Emergency Medical Service (EMS) Incident Dispatch Data

The dataset contains emergency incident records including:

- Borough
- ZIP Code
- Initial Call Type
- Final Call Type
- Incident Time
- Dispatch Time
- Arrival Time
- Hospital Time
- Incident Duration
- Travel Time

---

# 🧠 Machine Learning Models

| Model | Purpose |
|--------|----------|
| Random Forest | Baseline Regression |
| XGBoost | Response Time Prediction |
| CatBoost | Dispatch & ETA Prediction |
| Random Forest Classifier | Delay Classification |
| Forecasting Model | Demand Prediction |

---

# ⚙ Feature Engineering

The following engineered features were created:

- Hour
- Month
- Weekday
- Weekend
- Peak Hour
- Rush Hour
- Night Shift
- Borough Frequency
- ZIP Frequency
- Initial Call Frequency
- Final Call Frequency
- Dispatch Area Frequency
- Call-Borough Mapping
- ZIP-Hour Mapping

---

# 📈 Model Performance

| Model | Task |
|--------|------|
| Response Model | Incident Response Prediction |
| Dispatch Model | Dispatch Time Prediction |
| ETA Model | Travel Time Prediction |
| Delay Model | Delay Classification |
| Demand Model | Demand Forecasting |

---

# 🛠 Tech Stack

### Programming

- Python

### Machine Learning

- Scikit-Learn
- XGBoost
- CatBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Plotly
- Matplotlib

### Deployment

- Streamlit
- GitHub

---

# 📂 Project Structure

```
AI-Ambulance/
│
├── app.py
├── artifacts/
├── assets/
├── data/
├── models/
├── pages/
├── utils/
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/codebreaker19-N/AI-Ambulance.git
```

Move into project directory

```bash
cd AI-Ambulance
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Screenshots

> Add screenshots here after deployment.

Example:

- Home Page
- Response Prediction
- ETA Prediction
- Dashboard
- About Page

---

# 🌍 Live Application

### Streamlit

https://ai-ambulance-intelligence.streamlit.app/

---

# 👩‍💻 Developer

B.Tech CSE (AI)

Frontend Developer | Machine Learning Enthusiast

GitHub

https://github.com/codebreaker19-N

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 🚀 Future Improvements

- Real-time Traffic Integration
- Weather-Based Prediction
- GPS Route Optimization
- Hospital Recommendation System
- Explainable AI Dashboard
- Real-Time Ambulance Tracking
- Mobile Application
