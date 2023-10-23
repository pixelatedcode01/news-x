import streamlit as st
from myUsers import UserRegistration
from streamlit_extras.switch_page_button import switch_page
import ISO_CODES

st.set_page_config("Sign Up", page_icon="🔑", initial_sidebar_state="collapsed")


st.write("# Sign Up")
username = st.text_input("Username *", key="uid", placeholder="Enter Username")
password = st.text_input(
    "Password *", type="password", placeholder="Enter Password", key="passw"
)
country = st.selectbox(
    "Country",
    tuple(ISO_CODES.ISO_CODES.values()),
    index=None,
    placeholder="Select Country",
    key="country",
)
if not username.strip() == "" and not password.strip() == "" and not country is None:
    signup = st.button(
        "Sign Up",
        on_click=UserRegistration(
            username.strip(), password.strip(), country
        ).register_user,
        type="primary",
    )
else:
    st.write("Fill all mandatory fields.")


st.write("Already Registered?")
if st.button("Login", type="secondary"):
    switch_page("login")
