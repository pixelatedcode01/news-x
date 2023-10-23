# Import necessary libraries and modules
import streamlit as st
from myUsers import UserRegistration
from streamlit_extras.switch_page_button import switch_page
import ISO_CODES

# Configure the Streamlit page settings for the "Sign Up" page
st.set_page_config("Sign Up", page_icon="🔑", initial_sidebar_state="collapsed")

# Display a title for the "Sign Up" page
st.write("# Sign Up")

# Create text input fields for username and password
username = st.text_input("Username *", key="uid", placeholder="Enter Username")
password = st.text_input(
    "Password *", type="password", placeholder="Enter Password", key="passw"
)

# Create a dropdown select box for choosing the user's country
country = st.selectbox(
    "Country",
    tuple(ISO_CODES.ISO_CODES.values()),  # Use ISO country codes as options
    index=None,
    placeholder="Select Country",
    key="country",
)

# Check if the username, password, and country are not empty
if not username.strip() == "" and not password.strip() == "" and not country is None:
    # Create a "Sign Up" button that calls the UserRegistration function when clicked
    signup = st.button(
        "Sign Up",
        on_click=UserRegistration(
            username.strip(), password.strip(), country
        ).register_user,  # Calls the register_user method
        type="primary",
    )
else:
    st.write("Fill all mandatory fields.")  # Display a message if mandatory fields are not filled

# Provide an option for users to navigate to the "Login" page
st.write("Already Registered?")
if st.button("Login", type="secondary"):
    switch_page("login")  # Switch to the "login" page when the "Login" button is clicked
