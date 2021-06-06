from flask.helpers import make_response
from flask.json import jsonify
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from tensorflow import keras
from tensorflow.python.ops.gen_array_ops import where
import tensorflow_decision_forests as tfdf
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from operator import itemgetter

# Setup Flask, Model and Firestore
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

model_path = '../saved_model/my_model'
model = keras.models.load_model(model_path)

cred = credentials.Certificate("service_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

# Read all diseases
@app.route('/diseases', methods = ['GET'])
def diseases():
    results = []
    docs = db.collection('diseases')

    # Retrieve the data from users as json
    data = request.data

    if data:

        data = request.get_json()

        try:
            if 'where' in data:

                where = data.get('where')

                for i in where.items():
                    if type(i[1]) is list:
                        docs = docs.where(i[0], 'in', i[1])
                    else:
                        print(i)
                        docs = docs.where(i[0], '==', i[1])

            if 'order' in data:
                order = data.get('order')
                if 'descending' in data:
                    descending = data.get('descending')
                
                    if descending:
                        docs = docs.order_by(order, direction=firestore.Query.DESCENDING)
                    else:
                        docs = docs.order_by(order)
                else:
                    docs = docs.order_by(order)
            
            if 'descending' in data:
                descending = data.get('descending')
                if 'order' not in data and descending is True:
                    docs = docs.order_by('Id' ,direction=firestore.Query.DESCENDING)

            if 'limit' in data:
                limit = data.get('limit')
                docs = docs.limit(limit)

            docs = docs.get()
            for doc in docs:
                results.append(doc.to_dict())

            # Return the results
            return jsonify(results)
            
        except TypeError as err:
            return f'Type error: {err}'

    elif request.args:
        try:
            args = request.args

            for i in args.items():
                docs = docs.where(i[0], '==', int(i[1]) if i[0] == 'Id' else i[1])
            
            docs = docs.get()
            for doc in docs:
                results.append(doc.to_dict())
            
            results = sorted(results, key=itemgetter('Id'))

            # Return the results
            return jsonify(results)

        except TypeError as err:
            return f'Type error: {err}'
    else:
        
        docs = docs.get()
        for doc in docs:
            results.append(doc.to_dict())
        
        results = sorted(results, key=itemgetter('Id'))

        # Return the results
        return jsonify(results)

# Read all symptoms
@app.route('/symptoms', methods = ['GET'])
def symptoms():
    results = []
    docs = db.collection('symptoms')

    # Retrieve the data from users as json
    data = request.data

    if data:

        data = request.get_json()

        try:
            if 'where' in data:

                where = data.get('where')

                for i in where.items():
                    if type(i[1]) is list:
                        docs = docs.where(i[0], 'in', i[1])
                    else:
                        print(i)
                        docs = docs.where(i[0], '==', i[1])

            if 'order' in data:
                order = data.get('order')
                if 'descending' in data:
                    descending = data.get('descending')
                
                    if descending:
                        docs = docs.order_by(order, direction=firestore.Query.DESCENDING)
                    else:
                        docs = docs.order_by(order)
                else:
                    docs = docs.order_by(order)
            
            if 'descending' in data:
                descending = data.get('descending')
                if 'order' not in data and descending is True:
                    docs = docs.order_by('Id' ,direction=firestore.Query.DESCENDING)

            if 'limit' in data:
                limit = data.get('limit')
                docs = docs.limit(limit)

            docs = docs.get()
            for doc in docs:
                results.append(doc.to_dict())

            # Return the results
            return jsonify(results)
            
        except TypeError as err:
            return f'Type error: {err}'

    elif request.args:
        try:
            args = request.args

            for i in args.items():
                print(i)
                docs = docs.where(i[0], '==', int(i[1]) if i[0] == 'Id' else i[1])
            
            docs = docs.get()
            for doc in docs:
                results.append(doc.to_dict())
            
            results = sorted(results, key=itemgetter('Id'))

            # Return the results
            return jsonify(results)

        except TypeError as err:
            return f'Type error: {err}'
    else:
        
        docs = docs.get()
        for doc in docs:
            results.append(doc.to_dict())
        
        results = sorted(results, key=itemgetter('Id'))

        # Return the results
        return jsonify(results)

@app.route('/predict', methods = ['POST'])
def predict():
    # Retrieve the data from users as json
    data = request.get_json()

    # Retrieve all the symptoms data from firestore
    symptoms = []
    docs = db.collection('symptoms').get()
    for doc in docs:
        symptoms.append(doc.to_dict())

    # Create an array of symptoms sorted by Id
    symptoms_list = sorted(symptoms, key=itemgetter('Id'))
    symptoms_list = [x['Symptom'] for x in symptoms_list]

    # Retrieve all the diseases data from firestore
    diseases = []
    docs = db.collection('diseases').get()
    for doc in docs:
        diseases.append(doc.to_dict())

    # Create an array of diseases sorted by Id
    diseases_list = sorted(diseases, key=itemgetter('Id'))
    diseases_list = [x['Disease'] for x in diseases_list]

    # Create the inputs for the model
    model_inputs = []
    for i in symptoms_list:
        model_inputs.append(float(0))

    for i in data.values():
        if i != '0':
            symptom_index = symptoms_list.index(i)
            model_inputs[symptom_index] = float(1)

    # Create the Input DataFrame and convert to tensorflow dataset
    df_inputs = pd.DataFrame([model_inputs], columns=symptoms_list)
    model_inputs = tfdf.keras.pd_dataframe_to_tf_dataset(df_inputs, label=None)

    # Predict the data
    prediction = model.predict(model_inputs)
    predicted = prediction[0]

    # Catch the highest probability value from predicted output
    highest_probability = max(predicted)

    # Catch the disease index
    disease_index = np.where(predicted == highest_probability)
    disease_index = disease_index[0][0]

    # Find the disease based on the disease index
    for i in diseases:
        if i['Id'] == disease_index:
            predicted_disease = i

    # Assign diseases name, probability, description, and precautions to a variable
    disease_name = predicted_disease['Disease']
    probability = highest_probability*100
    description = predicted_disease['Description']
    precaution = predicted_disease['Precautions']

    # Store the results as json
    results = {
        'Disease': disease_name,
        'Probability': probability,
        'Description': description,
        'Precaution': precaution
    }
    results = make_response(jsonify(results), 200)

    # Return the results
    return results

if __name__ == '__main__':
    app.run(debug=True)