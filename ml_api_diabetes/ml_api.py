from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

class input_model(BaseModel): # inheriting a class present within the bracket
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

app = FastAPI() # to create an API in order for CRUD operation

# loading the model
model = pickle.load(open("disease_diabetes.sav", "rb"))

@app.post("/diabetes_prediction") #ending point
def diabetes_prediction(input_parameters: input_model):
    input_data = input_parameters.model_dump_json() # converting to json format
    # since json() is deprecated, so model_dump_json is used
    input_dict = json.loads(input_data) # converting to dictionary data structure
    # acting as keys (data member of the class input_model)
    preg = input_dict["Pregnancies"]
    gluc = input_dict["Glucose"]
    bp = input_dict["BloodPressure"]
    skin = input_dict["SkinThickness"]
    insulin = input_dict["Insulin"]
    bmi = input_dict["BMI"]
    dpf = input_dict["DiabetesPedigreeFunction"]
    age = input_dict["Age"]

    input = [preg, gluc, bp, skin, insulin, bmi, dpf, age]
    prediction = model.predict([input])

    if prediction[0] == 0:
        return "Diabetes is not detected"
    else:
        return "Diabetes is detected"

