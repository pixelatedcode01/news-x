import streamlit as st
from myUsers import UserRegistration
from streamlit_extras.switch_page_button import switch_page

st.set_page_config("Sign Up", page_icon="🔑", initial_sidebar_state="collapsed")


st.write("# Sign Up")
username = st.text_input("Username", key="uid", placeholder="Enter Username")
password = st.text_input(
    "Password", type="password", placeholder="Enter Password", key="passw"
)
if not username == "" and not password == "":
    signup = st.button(
        "Sign Up",
        on_click=UserRegistration(username.strip(), password.strip()).register_user,
        type="primary",
    )
else:
    st.write("Enter both username and password")


st.write("Already Registered?")
if st.button("Login", type="secondary"):
    switch_page("login")
