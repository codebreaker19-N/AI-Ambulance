import os
import joblib
from xgboost import XGBRegressor, XGBClassifier

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

incident_response_model = joblib.load(
    os.path.join(MODEL_DIR, "incident_response_model.pkl")
)

dispatch_time_model = XGBRegressor()
dispatch_time_model.load_model(
    os.path.join(MODEL_DIR, "dispatch_time_model.json")
)

eta_prediction_model = XGBRegressor()
eta_prediction_model.load_model(
    os.path.join(MODEL_DIR, "ETA_Prediction_Model.json")
)

delay_classifier = XGBClassifier()
delay_classifier.load_model(
    os.path.join(MODEL_DIR, "delay_classifier.json")
)

demand_forecast_model = joblib.load(
    os.path.join(MODEL_DIR, "demand_forecast_model.pkl")
)