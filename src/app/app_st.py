import streamlit as st
import requests
from textblob import TextBlob
import pickle
# URL base do seu servidor Flask
BASE_URL = "http://localhost:8501"  # Substitua pela URL do seu servidor Flask

house_model = pickle.load(open('models/model_houses.sav', 'rb'))

# Função para previsão de preço da casa
def predict_house_price(size, year, garage):
    data = {
        "tamanho": size,
        "ano": year,
        "garagem": garage
    }

    input_data = [data[col] for col in ['tamanho', 'ano', 'garagem']]
    predict = house_model.predict([input_data])
    return predict

# Front-end para a previsão de preços de casas
st.title('House Prices Prediction')
size = st.number_input('Size of the house', step=1, value=100)
year = st.number_input('Year of construction', step=1)
garage = st.number_input('Number of garages', step=1)

if st.button('Predict House Price'):
    house_price = predict_house_price(size, year, garage)
    if house_price is not None:
        st.write(f"Predicted house price: U$ {house_price[0].__round__(2)}")
    else:
        st.write("Prediction failed. Please try again.")
