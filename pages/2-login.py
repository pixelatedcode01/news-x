import streamlit as st
from myUsers import UserLogin
from streamlit_extras.switch_page_button import switch_page

st.set_page_config("Log in", page_icon="🔐", initial_sidebar_state="collapsed")

st.write("# Login")
login_username = st.text_input("Username", key="uid", placeholder="Enter Username")
login_password = st.text_input(
    "Password", type="password", placeholder="Enter Password", key="passw"
)
# signup = st.button(
#     "Log In",
#     on_click=
#     type="primary",
# )
if st.button("Log In", type="primary"):
    UserLogin(login_username, login_password).login_user()
    switch_page("dashboard")

st.write("New User?")
if st.button("Sign Up"):
    switch_page("sign_up")
