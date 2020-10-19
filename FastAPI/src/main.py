import argparse, joblib
from os import path
from utils import load_models, check_inputs
from train import load_data, transform

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

#Class vars
class feature_iris(BaseModel):
    sepl: float
    sepw: float
    petl: float
    petw: float

#Load Models
model, tf = load_models()

@app.get("/")
def home():
    return {"Bem vindo ao FastAPI"}

@app.post("/predict")
def predict(features: feature_iris):

    labels = [features.sepl, features.sepw, features.petl, features.petw]

    x = check_inputs(labels)
    y_hat = model.predict(tf.transform(x))

    t_hat = str(y_hat)[1:-1]
    json_t_hat = {"t_hat":t_hat}
    return json_t_hat
