#pip install fastapi uvicorn tensorflow tensorflow_decision_forests numpy pandas 

# 1. Importing Libraries
import uvicorn
from fastapi import FastAPI
from Symptoms import SymptomList
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import tensorflow_decision_forests as tfdf

# 2. Create the App object
app = FastAPI()

# 3. Importing machine learning SavedModel
model_path = '../saved_model/my_model'
model = keras.models.load_model(model_path)

# 4. List of sorted diseases and symptoms
diseases_list = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer diseae', 'AIDS',   
                'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia', 
                'Dimorphic hemorrhoids', 'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 
                'Osteoarthristis', 'Arthritis', 'Benign paroxysmal positional vertigo', 'Acne', 'Urinary tract infection', 
                'Psoriasis', 'Impetigo']

symptoms_list = ['abdominal_pain', 'abnormal_menstruation', 'acidity', 'acute_liver_failure', 'altered_sensorium', 'anxiety','back_pain', 'belly_pain', 'blackheads', 'bladder_discomfort', 'blister', 'blood_in_sputum', 'bloody_stool','blurred_and_distorted_vision', 'breathlessness', 'brittle_nails', 'bruising', 'burning_micturition', 'chest_pain', 'chills', 'cold_hands_and_feets', 'coma', 'congestion', 'constipation', 'continuous_feel_of_urine', 'continuous_sneezing', 'cough', 'cramps', 'dark_urine', 'dehydration', 'depression', 'diarrhoea', 'dischromic_patches', 'distention_of_abdomen', 'dizziness', 'drying_and_tingling_lips', 'enlarged_thyroid', 'excessive_hunger', 'extra_marital_contacts', 'family_history', 'fast_heart_rate', 'fatigue', 'fluid_overload', 'foul_smell_of_urine', 'headache', 'high_fever', 'hip_joint_pain', 'history_of_alcohol_consumption', 'increased_appetite', 'indigestion', 'inflammatory_nails', 'internal_itching', 'irregular_sugar_level', 'irritability', 'irritation_in_anus', 'itching', 'joint_pain', 'knee_pain', 'lack_of_concentration', 'lethargy', 'loss_of_appetite', 'loss_of_balance', 'loss_of_smell', 'malaise', 'mild_fever', 'mood_swings', 'movement_stiffness', 'mucoid_sputum', 'muscle_pain', 'muscle_wasting', 'muscle_weakness', 'nausea', 'neck_pain', 'nodal_skin_eruptions', 'obesity', 'pain_behind_the_eyes', 'pain_during_bowel_movements', 'pain_in_anal_region', 'painful_walking', 'palpitations', 'passage_of_gases', 'patches_in_throat', 'phlegm', 'polyuria', 'prominent_veins_on_calf', 'puffy_face_and_eyes', 'pus_filled_pimples', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'red_sore_around_nose', 'red_spots_over_body', 'redness_of_eyes', 'restlessness', 'runny_nose', 'rusty_sputum', 'scurring', 'shivering', 'silver_like_dusting', 'sinus_pressure', 'skin_peeling', 'skin_rash', 'slurred_speech', 'small_dents_in_nails', 'spinning_movements', 'spotting_urination', 'stiff_neck', 'stomach_bleeding', 'stomach_pain', 'sunken_eyes', 'sweating', 'swelled_lymph_nodes', 'swelling_joints', 'swelling_of_stomach', 'swollen_blood_vessels', 'swollen_extremeties', 'swollen_legs', 'throat_irritation', 'toxic_look', 'ulcers_on_tongue', 'unsteadiness', 'visual_disturbances', 'vomiting', 'watering_from_eyes', 'weakness_in_limbs', 'weakness_of_one_body_side', 'weight_gain', 'weight_loss', 'yellow_crust_ooze', 'yellow_urine', 'yellowing_of_eyes', 'yellowish_skin']

# 5. User inputs
user_inputs = {
    "symptom_1": "abdominal_pain",
    "symptom_2": "abnormal_menstruation",
    "symptom_3": "anxiety",
    "symptom_4": "0",
    "symptom_5": "0"
}

@app.post('/DiseasePredict')
def disease_predict(data:SymptomList):
    data = data.dict()
    symptom_1=data['symptom_1']
    symptom_2=data['symptom_2']
    symptom_3=data['symptom_3']
    symptom_4=data['symptom_4']
    symptom_5=data['symptom_5']

    # 6. Define the model_inputs
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
    uvicorn.run(app, host='127.0.0.1', port=8000)
