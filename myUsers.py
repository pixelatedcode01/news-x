import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page


# Custom exception to handle cases where the username already exists during registration
class UsernameAlreadyExists(Exception):
    pass


class UserRegistration:
    """Class for user registration."""

    def __init__(self, username, password, country):
        self.username = username
        self.password = password
        self.country = country

    def register_user(self):
        """Register a user."""
        filename = "registered_users.txt"

        # Check if the file exists, and create it if it doesn't
        if not os.path.exists(filename):
            file = open(filename, "x")
        else:
            file = open(filename, "r+")
            lines = file.readlines()
            file.close()
            usernames = [line.split(",")[0] for line in lines]

            try:
                # Check if the username already exists; if so, raise an exception
                if self.username in usernames:
                    raise UsernameAlreadyExists
                else:
                    # If the username is unique, append the user information to the file
                    file = open(filename, "a+")
                    file.write(f"{self.username}, {self.password}, {self.country}\n")
                    file.close()
                    st.session_state["uid"] = ""
                    st.session_state["passw"] = ""
                    st.session_state["country"] = None
                    st.write("Registration Successful 👏")
            except UsernameAlreadyExists:
                st.write("Try a different Username")
                st.session_state["uid"] = ""
                st.session_state["passw"] = ""
                st.session_state["country"] = None


class UserLogin:
    """Class for user login."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login_user(self):
        """Login the user if correct information is provided."""

        filename = "registered_users.txt"

        # Check if the registered users file exists
        if not os.path.exists(filename):
            st.write("No registered users found. Please sign up first.")
            return

        with open(filename, "r") as file:
            lines = file.read().splitlines()

            for line in lines:
                # Split the line into stored username, stored password, and stored country
                stored_username, stored_password, stored_country = line.strip().split(
                    ", "
                )

                if (
                    self.username == stored_username
                    and self.password == stored_password
                ):
                    # If the username and password match, log in the user and create a session
                    st.write("Login Successful 🎉")
                    file = open(f"current.csv", "w+")
                    file.write(
                        f"username,{self.username}\ncountry,{stored_country}\nlogin,{True}"
                    )
                    file.close()
                    return True
                else:
                    st.write("Invalid username or password. Please try again.")
