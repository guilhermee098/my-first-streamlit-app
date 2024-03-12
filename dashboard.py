import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

def show_home():
    st.subheader("Settings")
    st.write("Aqui estão as configurações.")
    

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
