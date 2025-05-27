from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from src.model import load_model
from src.feature_engineering import load_scaler

app = FastAPI()
model = load_model()
scaler = load_scaler()

class Customer(BaseModel):
    Age: float
    Annual_Income_k: float
    Spending_Score: float

@app.post("/predict")
def predict(customer: Customer):
    try:
        features = np.array([[customer.Age, customer.Annual_Income_k, customer.Spending_Score]])
        features_scaled = scaler.transform(features)
        cluster = model.predict(features_scaled)
        return {"segment": int(cluster[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))