import streamlit as st
import pandas as pd
import os
import currency_fetch
import get_users_information
import numpy as np
from streamlit_option_menu import option_menu

def show_home():
    st.subheader("Página inicial")
    import os


    st.write("Aqui estão algumas chamadas de API...")
    st.write("Por exemplo, você pode chamar uma API realizar a conversão de moedas.")
    # create two floating lists with some currencies including USD, EUR, GBP, JPY, CNY and BRL
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'BRL']
    # create a selectbox to choose the currency
    currency = st.selectbox('Selecione a moeda', currencies)
    # create another selectbox to choose the currency to convert to 
    currency_to = st.selectbox('Selecione a moeda para converter', [c for c in currencies if c != currency])
    # create a text input to enter the amount of currency to convert
    amount = st.number_input('Digite o valor a ser convertido', value=1)
    # create a button to perform the conversion
    if st.button('Converter'):
        # perform the conversion here
        converted_amount = currency_fetch.currency_fetch(currency, currency_to, amount)
        st.write(f'{amount} {currency} é o mesmo que {converted_amount} {currency_to}')

    user_info = get_users_information.get_users_information()
    if 'city' in user_info:
        user_city = user_info['city']
        user_org = user_info['org']
        user_region = user_info['region']
        user_country = user_info['country']
        st.write(f"Ou por exemplo, conseguimos saber que você está localizado em {user_city}, certo?")
        st.write(f"Isso é uma informação que conseguimos através do seu IP. Além da organização ({user_org}), região ({user_region}) e país ({user_country}).")
    else:
        st.write("Informação de cidade não disponível")

    

def show_settings():
    st.subheader("Perfil")
    # Personal information
    st.write("Informações pessoais")
    name = st.text_input("Nome", "Seu nome")
    age = st.number_input("Idade", min_value=0, max_value=150, value=21)
    email = st.text_input("Email", "seuemail@example.com")
    
    # Edit button
    if st.button("Editar"):
        # Perform client-side editing logic here
        # For example, update the profile information in the UI
        st.write("Edição realizada com sucesso!")

def show_dashboard():
    # Sidebar menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", "Dashboard", "Settings"], 
                               icons=['house', 'bar-chart-line', 'gear'], menu_icon="cast", default_index=1)
    
    if selected == "Home":
        show_home()
    elif selected == "Dashboard":
        # Generate fake data
        data = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'D', 'E'],
            'Value': np.random.randint(0, 100, 5)
        })

        # Display bar chart
        st.subheader('Bar Chart')
        st.bar_chart(data['Value'])

        # Display line chart
        st.subheader('Line Chart')
        st.line_chart(data['Value'])

        # Display table
        st.subheader('Table')
        st.table(data)
    elif selected == "Settings":
        show_settings()

if __name__ == "__main__":
    show_dashboard()
