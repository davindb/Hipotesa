from flask.helpers import url_for
from flask.json import jsonify
from flask.templating import render_template
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for
import tensorflow as tf
from tensorflow import keras
import tensorflow_decision_forests as tfdf
from assets import diseases_list, symptoms_list, user_inputs

app = Flask(__name__)
model_path = '../saved_model/my_model'
model = keras.models.load_model(model_path)

@app.route('/')
def home():
    return '''
    Symptoms Based Disease Prediction Public API built by Kreasi Anak Bangsa team from Bangkit 2021.
    '''

@app.route('/DiseasePredict', methods = ['POST'])
def predict():
    model_inputs = []
    for i in symptoms_list:
        model_inputs.append(float(0))

    for i in user_inputs.values():
        if i != '0':
            symptom_index = symptoms_list.index(i)
            model_inputs[symptom_index] = float(1)

    # 7. Create the Input DataFrame and convert to tensorflow dataset
    df_inputs = pd.DataFrame([model_inputs], columns=symptoms_list)
    model_inputs = tfdf.keras.pd_dataframe_to_tf_dataset(df_inputs, label=None)

    # 8. Predict the data
    prediction = model.predict(model_inputs)

    # Catch the specific prediction
    index_of_prediction = 0
    predicted = prediction[index_of_prediction]

    # 'predicted' will be performed in an ndarray of probability

    # 9. Initialize the highest probability variable
    highest_probability = 0
    second_highest = 0

    # Iterate the ndarray to catch the highest probability of predicted disease
    for i in predicted:
        if i > highest_probability:
            highest_probability = i

    # Catch the second highest
    for s in predicted:
        if s > second_highest and s < highest_probability:
            second_highest = s

    # Catch the disease index
    disease_index_1 = np.where(predicted == highest_probability)
    disease_index_1 = disease_index_1[0][0]

    disease_index_2 = np.where(predicted == second_highest)
    disease_index_2 = disease_index_2[0][0]

    # # Find the disease based on the disease index
    predicted_disease_1 = diseases_list[disease_index_1]
    predicted_disease_2 = diseases_list[disease_index_2]

    # The probability percentage
    probability_1 = highest_probability*100
    probability_2 = second_highest*100

    # print(f'Probability: {probability_1} %')
    # print(f'Predicted disease: {predicted_disease_1}\n')
    
    return {
        'Prediction': predicted_disease_1,
        'Probability': probability_1
    }

if __name__ == '__main__':
    app.run()