import streamlit as st
from myUsers import UserLogin
from streamlit_extras.switch_page_button import switch_page

# Configure the Streamlit page settings for the "Log in" page
st.set_page_config("Log in", page_icon="🔐", initial_sidebar_state="collapsed")

# Display a title for the "Log in" page
st.write("# Login")

# Create text input fields for entering the username and password
login_username = st.text_input("Username", key="uid", placeholder="Enter Username")
login_password = st.text_input(
    "Password", type="password", placeholder="Enter Password", key="passw"
)

# Check if the "Log In" button is clicked
if st.button("Log In", type="primary"):
    # If the login is successful, switch to the "dashboard" page
    if UserLogin(login_username, login_password).login_user():
        switch_page("dashboard")
    else:
        # Display a message if the login fails
        st.write("Check your username and password.")

# Provide an option for new users to navigate to the "Sign Up" page
st.write("New User?")
if st.button("Sign Up"):
    switch_page("sign_up")  # Switch to the "sign_up" page when the button is clicked
