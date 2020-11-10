import argparse, joblib
from os import path
from utils import load_models, check_inputs
from train import load_data
from utils import load_models, check_inputs

from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

#Class vars
class Item(BaseModel):
    features: list
    label: Optional[str] = None

#Load Models
model, tf = load_models()

@app.get("/")
def home():
    return {"Bem vindo ao FastAPI"}

@app.post("/predict")
def predict(item: Item):

    x = check_inputs(item.features)
    y_hat = model.predict(tf.transform(x))

    if (y_hat[0] == 0):
        pred = 'Assinante'
    else:
        pred = "Cancelou"
    
    item.label = pred

    return item
