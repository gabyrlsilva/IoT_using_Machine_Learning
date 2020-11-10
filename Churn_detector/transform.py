from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class dataclean(BaseEstimator, TransformerMixin):

    def fit(self, df):
        return self

    def transform(self, df):
        features_numerical = df.drop(columns=['sexo', 'tipo_de_cobranca','cidade', 'estado'])

        #Excluir coisas
        df_buffer = features_numerical.loc[features_numerical['week']<18]
        mean_fn = df_buffer.groupby(['user']).agg('mean')

        return mean_fn
    
class dropNAN(BaseEstimator, TransformerMixin):

    def fit(self, mean_fn):
        return self

    def transform(self, mean_fn):

        mean_fn.fillna(0, inplace=True)

        X = mean_fn.iloc[:,1:40].values

        return X