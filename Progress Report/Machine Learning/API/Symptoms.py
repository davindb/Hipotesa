# -*- coding: utf-8 -*-

from pydantic import BaseModel

class SymptomList(BaseModel):
    symptom_1: str
    symptom_2: str
    symptom_3: str
    symptom_4: str
    symptom_5: str
#     pass