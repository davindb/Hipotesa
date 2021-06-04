from flask.helpers import make_response
from flask.json import jsonify
import pandas as pd
from flask import Flask, request, jsonify
from assets import symptoms_list, disease_description, disease_precaution
import pickle

app = Flask(__name__)
model = open("randomforest.pkl", "rb")
model = pickle.load(model)

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

    # 3. Create the Input DataFrame
    model_inputs = pd.DataFrame([model_inputs], columns=symptoms_list)

    # 4. Predict the data
    prediction = model.predict(model_inputs)
    predicted_disease = prediction[0]

    # 4. Filter the description based on the predicted disease
    filtered_desc = filter(lambda disease: disease['Disease'] == predicted_disease, disease_description)
    filtered_desc = list(filtered_desc)[0]['Description']

    # 5. Filter the precaution based on the predicted disease
    filtered_precaution = filter(lambda disease: disease['Disease'] == predicted_disease, disease_precaution)
    filtered_precaution = list(filtered_precaution)[0]
    filtered_precaution = [x[1] for x in filtered_precaution.items() if x[0] != 'Disease' and x[1] != 0]

    # 6. Store the results as json
    results = {
        'Disease': predicted_disease,
        'Description': filtered_desc,
        'Precaution': filtered_precaution
    }
    results = make_response(jsonify(results), 200)

    # 7. Return the results
    return results

if __name__ == '__main__':
    app.run()