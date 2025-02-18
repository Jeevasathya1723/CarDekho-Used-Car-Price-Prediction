import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
import pandas as pd
import pickle

def app():
    colored_header(
        label='Welcome to Data :red[Prediction] page 👋🏼',
        color_name='red-70',
        description='CarDekho Used Cars Price Prediction'
    )

    @st.cache_data
    def data():
        df = pd.read_csv('Cleaned_Car_Dheko.csv')
        df1 = pd.read_csv('Preprocessed_Car_Dheko.csv')
        return df, df1

    df, df1 = data()

    df.drop(['Manufactured_By', 'No_of_Seats', 'No_of_Owners', 'Fuel_Type', 'Registration_Year', 'Car_Age'], axis=1, inplace=True)
    df1.drop(['Manufactured_By', 'No_of_Seats', 'No_of_Owners', 'Fuel_Type', 'Registration_Year', 'Car_Age'], axis=1, inplace=True)

    for i in df.columns:
        if df[i].dtype == 'object':
            col_name = i
            decode = df[i].sort_values().unique()
            encode = df1[i].sort_values().unique()
            globals()[col_name] = dict(zip(decode, encode))

    with st.form(key='form', clear_on_submit=False):

        car_model = st.selectbox("**Select a Car Model**", options=df['Car_Model'].unique())

        model_year = st.selectbox("**Select a Car Produced Year**", options=df['Car_Produced_Year'].unique())

        transmission = st.radio("**Select a Transmission Type**", options=df['Transmission_Type'].unique(), horizontal=True)

        location = st.selectbox("**Select a Location**", options=df['Location'].unique())

        km_driven = st.number_input(
            f"**Enter Kilometer Driven (Min: {df['Kilometers_Driven'].min()} & Max: {df['Kilometers_Driven'].max()})**"
        )

        engine_cc = st.number_input(
            f"**Enter Engine CC (Min: {df['Engine_CC'].min()} & Max: {df['Engine_CC'].max()})**"
        )

        mileage = st.number_input(
            f"**Enter Mileage (Min: {df['Mileage(kmpl)'].min()} & Max: {df['Mileage(kmpl)'].max()})**"
        )

        def inv_trans(x):
            return x if x == 0 else 1 / x

        inv_trans(km_driven)

        with open('GradientBoost_model.pkl', 'rb') as file:
            model = pickle.load(file)

        button = st.form_submit_button('**Predict**', use_container_width=True)

        if button:
            result = model.predict([[inv_trans(km_driven), Transmission_Type[transmission], Car_Model[car_model], model_year, engine_cc, mileage, Location[location]]])
            st.markdown(f"## :green[*Predicted Car Price is ₹{result[0]:,.2f}*]")  
