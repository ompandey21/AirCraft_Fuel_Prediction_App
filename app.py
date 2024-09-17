import streamlit as st
import joblib 
import pandas as pd
import numpy as np
import sklearn

#? Load the model
model = joblib.load('linear_regression_model.pkl')

# App title
st.title('Aircraft Fuel Predictor')

# Input field
flight_Distance = st.number_input('Flight_Distance(km)', key = 1)
flight_Duration = st.number_input('Flight_Duration(hr)', key = 2)
no_of_passenger = st.number_input('Number_of_passengers', key = 3)
aircraft_Type = st.selectbox('Aircraft_Type', ['Type1', 'Type2', 'Type3'], key = 5)
# flight_Distance = st.number_input('Flight_Distance(km)', key = 4)

# Dataframe

input_data = pd.DataFrame({'Flight_Distance':[flight_Distance],
                           'Number_of_Passengers': [no_of_passenger],
                           'Flight_Duration': [flight_Duration],
                           'Aircraft_Type_Type1': [1 if aircraft_Type == 'Type1' else 0],
                           'Aircraft_Type_Type2': [1 if aircraft_Type == 'Type2' else 0],
                           'Aircraft_Type_Type3': [1 if aircraft_Type == 'Type3' else 0]
                           })

# predict
if st.button('predict'):
    fuel_consumption = model.predict(input_data)
    print(fuel_consumption)
    st.write(fuel_consumption)

