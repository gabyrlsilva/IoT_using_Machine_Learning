import joblib
from os import path
import numpy as np
from decouple import config as cfg


MODELS_FOLDER = path.join('models')
EXPERIMENT_NAME = path.join(MODELS_FOLDER, 'exp_01_default')

TRANSFORM_NAME = cfg('TRANSFORM_NAME', cast=str)
MODEL_NAME = cfg('MODEL_NAME', cast=str)



def load_models():
    tf = joblib.load(path.join(MODELS_FOLDER, EXPERIMENT_NAME, TRANSFORM_NAME))
    model = joblib.load(path.join(MODELS_FOLDER, EXPERIMENT_NAME, MODEL_NAME))

    return model,tf

def check_inputs(input):
    print(input)

    # check if is list
    if type(input) == list:
        if len(input) == 4:
            # turn strings into numbers
            input = [float(i) for i in input]
            return np.array(input).reshape(1,-1)
    
    else:
        return 205

    pass