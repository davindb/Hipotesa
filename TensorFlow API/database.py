from flask.helpers import make_response
from flask.json import jsonify
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from tensorflow import keras
import tensorflow_decision_forests as tfdf
# from assets import diseases_list, symptoms_list, disease_description, disease_precaution
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from operator import itemgetter

cred = credentials.Certificate("service_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Read data by id
# result = db.collection('symptoms').document('0').get()
# if result.exists:
#     print(result.to_dict())

# Read all data
# results = db.collection('diseases').get()
# for result in results:
#     print(result.to_dict())

# Querying 
# results = db.collection('diseases').where('Id', '<', 11).get()
# for result in results:
#     print(result.to_dict())

results = []
docs = db.collection('symptoms')

# Retrieve the data from users as json
data = False

# if data:
#     if 'where' in data:

#         where = data.get('where')

#         for i in where.items():
#             if type(i[1]) is list:
#                 docs = docs.where(i[0], 'in', i[1])
#             else:
#                 print(i)
#                 docs = docs.where(i[0], '==', i[1])

#     if 'order' in data:
#         order = data.get('order')
#         docs = docs.order_by(order)
#         print(order)

#     if 'limit' in data:
#         limit = data.get('limit')
#         # if type(limit) is int:
#         docs = docs.limit_to_last(limit)

#     docs = docs.get()
#     for doc in docs:
#         results.append(doc.to_dict())
#     results = make_response(jsonify(results), 200)

#     # Return the results
#     print(results)

# elif request.args:
#     args = request.args

#     for i in args.items():
#         print(i)
#         docs = docs.where(i[0], '==', int(i[1]) if i[0] == 'Id' else i[1])
    
#     docs = docs.get()
#     for doc in docs:
#         results.append(doc.to_dict())
    
#     results = sorted(results, key=itemgetter('Id'))
#     results = make_response(jsonify(results), 200)

#     # Return the results
#     print(results)

# else:
docs = docs.get()
for doc in docs:
    results.append(doc.to_dict())

results = sorted(results, key=itemgetter('Id'))
# results = make_response(jsonify(results), 200)

# Return the results
print(results)