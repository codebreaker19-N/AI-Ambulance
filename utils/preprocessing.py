import os
import joblib
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")


def _load_artifact(filename):
    path = os.path.join(ARTIFACT_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"{filename} not found inside artifacts folder."
        )

    return joblib.load(path)



borough_encoder = _load_artifact("borough_encoder.pkl")
initial_encoder = _load_artifact("initial_call_type_encoder.pkl")
final_encoder = _load_artifact("final_call_type_encoder.pkl")
dispatch_encoder = _load_artifact("incident_dispatch_area_encoder.pkl")



zipcode_frequency = _load_artifact("zipcode_frequency.pkl")
borough_frequency = _load_artifact("borough_frequency.pkl")
dispatch_frequency = _load_artifact("dispatch_area_frequency.pkl")
initial_frequency = _load_artifact("initial_call_frequency.pkl")
final_frequency = _load_artifact("final_call_frequency.pkl")



call_borough_mapping = _load_artifact("call_borough_mapping.pkl")
zip_hour_mapping = _load_artifact("zip_hour_mapping.pkl")



response_features = _load_artifact("response_features.pkl")
dispatch_features = _load_artifact("dispatch_features.pkl")
eta_features = _load_artifact("eta_features.pkl")
delay_features = _load_artifact("delay_features.pkl")
demand_features = _load_artifact("demand_features.pkl")


def _to_dataframe(data):

    if isinstance(data, dict):
        return pd.DataFrame([data])

    return data.copy()



def _safe_transform(encoder, series):

    mapping = {
        cls: idx
        for idx, cls in enumerate(encoder.classes_)
    }

    return series.map(mapping).fillna(-1).astype(int)



def _basic_preprocessing(df):

    df = df.copy()

    

    defaults = {

        "zipcode": 0,
        "borough": "Unknown",
        "initial_call_type": "Unknown",
        "final_call_type": "Unknown",
        "incident_dispatch_area": "Unknown",

        "hour": 0,
        "month": 1,
        "weekday": 0,
        "Year": 2025

    }

    for col, val in defaults.items():

        if col not in df.columns:
            df[col] = val

    raw_zip = df["zipcode"].copy()
    raw_hour = df["hour"].copy()



    df["borough"] = _safe_transform(
        borough_encoder,
        df["borough"]
    )

    df["initial_call_type"] = _safe_transform(
        initial_encoder,
        df["initial_call_type"]
    )

    df["final_call_type"] = _safe_transform(
        final_encoder,
        df["final_call_type"]
    )

    df["incident_dispatch_area"] = _safe_transform(
        dispatch_encoder,
        df["incident_dispatch_area"]
    )


    df["Weekend"] = (df["weekday"] >= 5).astype(int)

    df["peak_hour"] = (
        ((df["hour"] >= 7) & (df["hour"] <= 10)) |
        ((df["hour"] >= 16) & (df["hour"] <= 19))
    ).astype(int)

    df["night_shift"] = (
        (df["hour"] >= 22) | (df["hour"] <= 5)
    ).astype(int)

    df["rush_hour"] = (
        df["hour"].isin([7, 8, 9, 16, 17, 18, 19])
    ).astype(int)

    df["office_hours"] = (
        df["hour"].between(9, 17)
    ).astype(int)

    

    df["zipcode_frequency"] = (
        raw_zip
        .map(zipcode_frequency)
        .fillna(0)
    )

    df["borough_frequency"] = (
        df["borough"]
        .map(borough_frequency)
        .fillna(0)
    )

    df["dispatch_area_frequency"] = (
        df["incident_dispatch_area"]
        .map(dispatch_frequency)
        .fillna(0)
    )

    df["initial_call_frequency"] = (
        df["initial_call_type"]
        .map(initial_frequency)
        .fillna(0)
    )

    df["final_call_frequency"] = (
        df["final_call_type"]
        .map(final_frequency)
        .fillna(0)
    )



    call_key = (
        df["initial_call_type"].astype(str)
        + "_"
        + df["borough"].astype(str)
    )

    df["call_borough"] = (
        call_key
        .map(call_borough_mapping)
        .fillna(-1)
    )

    zip_key = (
        raw_zip.astype(str)
        + "_"
        + raw_hour.astype(str)
    )

    df["zip_hour"] = (
        zip_key
        .map(zip_hour_mapping)
        .fillna(-1)
    )

    

    optional_defaults = {

        "dispatch_delay": 0,
        "incident_duration": 0,
        "incident_response_seconds_qy": 0,

        "lag1": 0,
        "lag2": 0,
        "lag3": 0,

        "day": 1,
        "weekend": df["Weekend"]

    }

    for col, value in optional_defaults.items():

        if col not in df.columns:
            df[col] = value

    return df



def _prepare_features(df, feature_list):

    feature_list = list(feature_list)

    df = _basic_preprocessing(df)

    

    for feature in feature_list:

        if feature not in df.columns:
            df[feature] = 0


    return df[feature_list]



def prepare_response_data(data):

    df = _to_dataframe(data)

    return _prepare_features(
        df,
        response_features
    )



def prepare_dispatch_data(data):

    df = _to_dataframe(data)

    return _prepare_features(
        df,
        dispatch_features
    )


def prepare_eta_data(data):

    df = _to_dataframe(data)

    return _prepare_features(
        df,
        eta_features
    )



def prepare_delay_data(data):

    df = _to_dataframe(data)

    return _prepare_features(
        df,
        delay_features
    )



def prepare_demand_data(data):

    df = _to_dataframe(data)

    return _prepare_features(
        df,
        demand_features
    )

