from flask.helpers import make_response
from flask.json import jsonify
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from tensorflow import keras
import tensorflow_decision_forests as tfdf
from assets import diseases_list, symptoms_list, disease_description, disease_precaution

app = Flask(__name__)
model_path = '../saved_model/my_model'
model = keras.models.load_model(model_path)

@app.route('/')
def index():
    return '''
    Symptoms Based Disease Prediction Public API built by Kreasi Anak Bangsa team from Bangkit 2021.
    '''

@app.route('/predict', methods = ['POST'])
def predict():
    # 1. Retrieve the data from users as json
    data = request.get_json()

    # 2. Define the inputs for the model
    model_inputs = []
    for i in symptoms_list:
        model_inputs.append(float(0))

    # 3. Create the inputs for the model
    for i in data.values():
        if i != '0':
            symptom_index = symptoms_list.index(i)
            model_inputs[symptom_index] = float(1)

    # 3. Create the Input DataFrame and convert to tensorflow dataset
    df_inputs = pd.DataFrame([model_inputs], columns=symptoms_list)
    model_inputs = tfdf.keras.pd_dataframe_to_tf_dataset(df_inputs, label=None)

    # 4. Predict the data
    prediction = model.predict(model_inputs)
    predicted = prediction[0]

    # 5. Initialize the highest probability variable
    first_probability = 0

    # 6. Iterate the ndarray to catch the highest probability of predicted disease
    for i in predicted:
        if i > first_probability:
            first_probability = i

    # 7. Catch the disease index
    disease_index = np.where(predicted == first_probability)
    disease_index = disease_index[0][0]

    # 8. Find the disease based on the disease index
    predicted_disease = diseases_list[disease_index]

    # 9. The probability percentage
    probability = first_probability*100

    # 10. Filter the description based on the predicted disease
    filtered_desc = filter(lambda disease: disease['Disease'] == predicted_disease, disease_description)
    filtered_desc = list(filtered_desc)[0]['Description']

    # 11. Filter the precaution based on the predicted disease
    filtered_precaution = filter(lambda disease: disease['Disease'] == predicted_disease, disease_precaution)
    filtered_precaution = list(filtered_precaution)[0]
    filtered_precaution = [x[1] for x in filtered_precaution.items() if x[0] != 'Disease' and x[1] != 0]

    # 12. Store the results as json
    results = {
        'Disease': predicted_disease,
        'Probability': probability,
        'Description': filtered_desc,
        'Precaution': filtered_precaution
    }
    results = make_response(jsonify(results), 200)

    # 13. Return the results
    # return jsonify(results)
    return results

if __name__ == '__main__':
    app.run()