import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading the saved models
parkinson_model = pickle.load(open("disease_parkinson.sav", "rb"))
diabetes_model = pickle.load(open("disease_diabetes.sav", "rb"))
heart_disease_model = pickle.load(open("disease_heart.sav ", "rb"))

# sidebar for navigate
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction Menu",
        [
            "Parkinson's Disease Prediction",
            "Diabetes Prediction",
            "Heart Disease Prediction"
        ],
        icons=["person", "activity", "heart",],
        default_index=0)

parkinson_columns = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
    'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
    'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
    'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
    'spread1', 'spread2', 'D2', 'PPE']

diabetes_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']

heart_disease_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']

actual_data_list = []
column_nums = 3
diagnosis_statement = ""

if selected == "Parkinson's Disease Prediction":
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    column = st.columns(column_nums)
    for ind_col, column_name in enumerate(parkinson_columns):
        col = column[ind_col%column_nums]
        with col:
            actual_data_list.append(st.text_input(column_name))

    if st.button("Heart Disease Test result: "):
        cleaned_data_list = np.array([float(x) if x else 0.0 for x in list(actual_data_list)])
        predicted_result = parkinson_model.predict([cleaned_data_list])

        if predicted_result[0] == 1.0:
            diagnosis_statement = "Parkinson's disease detected!!"
        else:
            diagnosis_statement = "The person is healthy"
        st.success(diagnosis_statement)
    

elif selected == "Diabetes Prediction":
    # page title
    st.title("Diabetes Prediction using ML")

    column = st.columns(column_nums)
    for ind_col, column_name in enumerate(diabetes_columns):
        col = column[ind_col%column_nums]
        with col:
            actual_data_list.append(st.text_input(column_name))

    if st.button("Diabetes Test result: "):
        cleaned_data_list = np.array([float(x) if x else 0.0 for x in list(actual_data_list)])
        predicted_result = diabetes_model.predict([cleaned_data_list])
        if predicted_result[0] == 1.0:
            diagnosis_statement = "Diabetes detected!!"
        else:
            diagnosis_statement = "The person is healthy"
        st.success(diagnosis_statement)

elif selected == "Heart Disease Prediction":
    # page title
    st.title("Heart Disease Prediction using ML")

    column = st.columns(column_nums)
    for ind_col, column_name in enumerate(heart_disease_columns):
        col = column[ind_col%column_nums]
        with col:
            actual_data_list.append(st.text_input(column_name))

    if st.button("Heart Disease Test result: "):
        cleaned_data_list = np.array([float(x) if x else 0.0 for x in list(actual_data_list)])
        predicted_result = heart_disease_model.predict([cleaned_data_list])
        if predicted_result[0] == 1.0:
            diagnosis_statement = "Heart disease detected!!"
        else:
            diagnosis_statement = "The person is healthy"
        st.success(diagnosis_statement)
