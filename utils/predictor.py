import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")


def load_model(filename):
    model_path = os.path.join(ARTIFACT_DIR, filename)
    return joblib.load(model_path)


response_model = load_model("response_model.pkl")
dispatch_model = load_model("dispatch_model.pkl")
eta_model = load_model("eta_model.pkl")
delay_model = load_model("delay_model.pkl")
demand_model = load_model("demand_model.pkl")

# DEBUG
print("Response:", type(response_model))
print("Dispatch:", type(dispatch_model))
print("ETA:", type(eta_model))
print("Delay:", type(delay_model))
print("Demand:", type(demand_model))


def predict_incident_response(data):
    return response_model.predict(data)[0]


def predict_dispatch(data):
    return dispatch_model.predict(data)[0]


def predict_eta(data):
    return eta_model.predict(data)[0]


def predict_delay(data):
    return delay_model.predict(data)[0]


def predict_response(data):

    print("="*50)
    print("MODEL TYPE:", type(response_model))
    print("MODEL:", response_model)

    print("="*50)
    print("DATA TYPE:", type(data))

    print("="*50)
    print("HAS PREDICT:", hasattr(response_model, "predict"))

    print("="*50)
    print("ID:", id(response_model))

    prediction = response_model.predict(data)

    return prediction[0]

print("Response model type:", type(response_model))
print("Response model:", response_model)

print("Has predict:", hasattr(response_model, "predict"))

if isinstance(response_model, list):
    print("LIST LENGTH:", len(response_model))
    print("FIRST ITEM:", type(response_model[0]))

def predict_dispatch(data):

    print("="*50)
    print("MODEL TYPE:", type(dispatch_model))
    print("MODEL:", dispatch_model)

    print("="*50)
    print("DATA TYPE:", type(data))

    print("="*50)
    print("HAS PREDICT:", hasattr(dispatch_model, "predict"))

    print("="*50)
    print("ID:", id(dispatch_model))

    prediction = dispatch_model.predict(data)

    return prediction[0]

def predict_eta(data):

    print("="*50)
    print("MODEL TYPE:", type(eta_model))
    print("MODEL:", eta_model)

    print("="*50)
    print("DATA TYPE:", type(data))

    print("="*50)
    print("HAS PREDICT:", hasattr(eta_model, "predict"))

    print("="*50)
    print("ID:", id(eta_model))

    prediction = eta_model.predict(data)

    return prediction[0]

def predict_demand(data):

    print("="*50)
    print("MODEL TYPE:", type(demand_model))
    print("MODEL:", demand_model)

    print("="*50)
    print("DATA TYPE:", type(data))

    print("="*50)
    print("HAS PREDICT:", hasattr(demand_model, "predict"))

    print("="*50)
    print("ID:", id(demand_model))

    prediction = demand_model.predict(data)

    return prediction[0]







