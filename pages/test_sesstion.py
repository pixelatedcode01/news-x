import streamlit as st


class SessionState:
    def __init__(self):
        self.data = {}


session_state = SessionState()

# Store a session variable

if "user_id" not in st.session_state:
    st.session_state.user_id = 123

# if not hasattr(session_state, "user_id"):
#     session_state.user_id = 123



# Retrieve and display the session variable
st.write(f"User ID: {st.session_state.user_id}")

