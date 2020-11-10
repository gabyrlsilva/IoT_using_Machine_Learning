import joblib
from os import path
import numpy as np
from train import load_data
import pandas as pd
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
    cols = ['user','week','total_sessions','total_mediaids','total_days','total_played','max_played_time','age_without_access','sexo','idade','cidade','estado','android_app_time','ios_app_time','tv_app_time','mobile_web_time','desktop_web_time','time_spent_on_news','time_spent_on_humor','time_spent_on_series','time_spent_on_novelas','time_spent_on_special','time_spent_on_varieties','time_spent_on_sports','time_spent_on_realities','time_spent_on_disclosure','time_spent_on_archived','time_spent_on_subscribed_content','time_spent_on_free_content','time_spent_on_grade','video_info_excerpt_time','video_info_extra_time','video_info_episode_time','video_info_time_spent_0_5','video_info_time_spent_5_15','video_info_time_spent_15_30','video_info_time_spent_30_60','video_info_time_spent_60mais','total_dependents','total_active_dependents','total_played_for_dependents','tipo_de_cobranca','total_cancels','month_subs','assinatura_age',]
    print(input)
   
    if type(input) == list:
        if len(input) == 45:
            input = [float(i) for i in input]
            print(input)
            data = np.array(input).reshape(1,-1)
            df = pd.DataFrame(data, columns=cols)

            print(df)

            return df

    else:
        return 205

    pass
