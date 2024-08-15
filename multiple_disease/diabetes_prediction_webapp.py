import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_file = pickle.load(open("trained_model.sav", "rb")) # reading the binary formatted file 

# creating a function for prediction
def diabetes_prediction(input_data):
    # input_data = (5,166,72,19,175,25.8,0.587,51)

    # converting the input data (tuple) into numpy array
    input_data_as_np = np.asarray(input_data)

    # reshaping the numpy array as it has only 1 row
    input_data_reshaped = input_data_as_np.reshape(1,-1)

    # standardize the input values
    # std_input_data = scaler.transform(input_data_reshaped)
    #print(std_input_data)

    # prediction
    prediction = loaded_file.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "The person is non-diabetic"
    else:
        return "The person is diabetic"



# getting input data from the user
def main():
    
    # giving a title
    st.title("DIABETES PREDICTION")
    pregnancies = st.text_input("Number of pregnancies: ")
    glucose = st.text_input("Glucose level: ")
    blood_pressure = st.text_input("Blood pressure level: ")
    skin_thickness = st.text_input("Skin thickness: ")
    insulin = st.text_input("Insulin level: ")
    bmi = st.text_input("BMI: ")
    diabetes_pedigree_function = st.text_input("Diabetes predigree prediction: ")
    age = st.text_input("Person's age: ")

    # code for prediction
    diagnosis_decision = ""

    if st.button("Diabetes Test Result"):
        diagnosis_decision = diabetes_prediction([pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age])

    st.success(diagnosis_decision)



if __name__ == "__main__":
    main()