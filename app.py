import pickle

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# Load the trained model
with open("model/house_price_model1.pkl", "rb") as file:
    model = pickle.load(file)


app = FastAPI(
    title="California Housing Price Prediction API",
    description="Machine Learning API for predicting California house prices",
    version="1.0.0"
)


class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def home():
    return {
        "message": "California Housing Price Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(data: HouseData):

    input_data = pd.DataFrame([{
        "MedInc": data.MedInc,
        "HouseAge": data.HouseAge,
        "AveRooms": data.AveRooms,
        "AveBedrms": data.AveBedrms,
        "Population": data.Population,
        "AveOccup": data.AveOccup,
        "Latitude": data.Latitude,
        "Longitude": data.Longitude
    }])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": float(prediction),
        "predicted_price_usd": float(prediction * 100000)
    }