import streamlit as st
from streamlit import session_state as state
import urllib.parse
from dashboard import show_dashboard

items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']

def main():
    if 'logged_in' not in state:
        state.logged_in = False

    if state.logged_in:
        show_dashboard()
    else:
        login_page()

def login_page():
    st.title('Meu Primeiro App com Streamlit')
    st.write('Olá, mundo!')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login')

    if login_button:
        if username == 'admin' and password == 'password':
            state.logged_in = True
            st.experimental_rerun()

    st.table({'Index': range(1, len(items)+1), 'Name': items})

if __name__ == '__main__':
    main()
