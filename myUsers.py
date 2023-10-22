import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page


class UsernameAlreadyExists(Exception):
    pass


class UserRegistration:
    """Class for user registration."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_user(self):
        """Register a user."""
        filename = "registered_users.txt"
        if not os.path.exists(filename):
            file = open(filename, "x")
        else:
            file = open(filename, "r+")
            lines = file.readlines()
            file.close()
            usernames = [line.split(",")[0] for line in lines]
            try:
                if self.username in usernames:
                    raise UsernameAlreadyExists
                else:
                    file = open(filename, "a+")
                    file.write(f"{self.username}, {self.password}\n")
                    file.close()
                    st.session_state["uid"] = ""
                    st.session_state["passw"] = ""
                    st.write("Registration Successful 👏")
            except UsernameAlreadyExists:
                st.write("Try a different Username")
                st.session_state["uid"] = ""
                st.session_state["passw"] = ""


class UserLogin:
    """Class for user login."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login_user(self):
        """Login the user if correct information is provided."""

        filename = "registered_users.txt"
        if not os.path.exists(filename):
            st.write("No registered users found. Please sign up first.")
            return

        with open(filename, "r") as file:
            lines = file.read().splitlines()

        for line in lines:
            stored_username, stored_password = line.strip().split(", ")
            if self.username == stored_username and self.password == stored_password:
                st.write("Login Successful 🎉")
                file = open(f"current.csv", "w+")
                file.write(f"username,{self.username}\nlogin,{True}")
                file.close()
                return

        st.write("Invalid username or password. Please try again.")
        st.session_state["uid"] = ""
        st.session_state["passw"] = ""
