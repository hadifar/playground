import streamlit as st
from streamlit_cookies_controller import CookieController

from config import config
from frontend.utils import check_hashes, make_hashes

controller = CookieController(key='cookies')


def login_page():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    def check_login():
        return 'username' in controller.getAll()

    if check_login() or st.session_state.authenticated:
        cookies = controller.getAll()
        username = cookies.get('username', 'Guest')
        st.write(f'hello {username}')
        # if st.button("delete cookie"):
        #     controller.remove('username')
        #     st.rerun()
    else:
        st.title("Login")
        st.write("Please log in to continue.")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_btn = st.form_submit_button("Login")

        if login_btn:
            users = config.users
            if username in users and check_hashes(make_hashes(password), users[username]):
                st.session_state.authenticated = True
                st.session_state.username = username
                controller.set('username', username)
                st.rerun()
            else:
                st.error("Invalid username or password")
