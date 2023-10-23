# Import the necessary libraries
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Configure the Streamlit page settings
st.set_page_config("Home", page_icon="🏠", initial_sidebar_state="collapsed")

# Display a header and introductory text
st.header("Welcome to News X")
st.write("A news dashboard for all your needs")

# Display the News X logo
st.image("news-x.png", width=300, caption="news-x-logo")

# Provide a brief description of the News X application
st.write(
    "NEWS-X is a user-friendly, Python-powered news dashboard that puts you in control of your news consumption. "
    "With a straightforward design and an array of features, this application allows you to read, manage, and visualize news effortlessly."
)

# Create a "Login" button that, when clicked, switches to the login page
if st.button("Login", use_container_width=True, type="primary"):
    switch_page("login")

# Create a "Sign Up" button that, when clicked, switches to the sign-up page
if st.button("Sign Up", use_container_width=True):
    switch_page("sign up")
