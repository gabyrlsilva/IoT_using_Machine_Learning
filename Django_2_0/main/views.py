from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from .utils import load_models, check_inputs
from .train import load_data
from .models import iris
from .forms import IrisForm
from django.views.decorators.csrf import csrf_exempt
from os import path

import json
import joblib
import argparse
import numpy as np
import sys

sys.path.append('../app')

model, tf = load_models()

@csrf_exempt
def predict(request):

    df = json.loads(request.body)
    
    x = list((df['features']).split(","))
    x = np.array(x).reshape(1,-1)
    y_hat = model.predict(tf.transform(x))

    df['label'] = str(y_hat)

    return JsonResponse(df)

@csrf_exempt
def predict_test(request):
    X, y = load_data()
    y_hat = model.predict(tf.transform(X))
    
    df = {'predict_test': 'predict'}

    return JsonResponse(df)


