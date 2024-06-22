import pickle
from catboost import CatBoostClassifier
import numpy as np
import pandas as pd

def predict(A):
    model = CatBoostClassifier()
    model.load_model('breast_cancer1.cbm')
    RESULT=model.predict(A)
    return RESULT
