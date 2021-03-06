# coding:utf-8

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline


class FillValueTransformerArray(BaseEstimator, TransformerMixin):

    def __init__(self, filling_values=0):
        self.filling_values=filling_values

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        x = X.copy()
        return pd.DataFrame(x).fillna(self.filling_values).values

    def fit_transform(self, X, y=None, **fit_params):
        x = X.copy()
        return pd.DataFrame(x).fillna(self.filling_values).values