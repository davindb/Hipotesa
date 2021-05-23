# -*- coding: utf-8 -*-

# from pydantic import BaseModel

# class SymptomList(BaseModel):
#     symptom_1: str
#     symptom_2: str
#     symptom_3: str
#     symptom_4: str
#     symptom_5: str
#     pass

import tensorflow as tf
from tensorflow import keras
import tensorflow_decision_forests as tfdf

print(tf.__version__)
print(tfdf.__version__)