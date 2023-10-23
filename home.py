import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config("Home", page_icon="🏠", initial_sidebar_state="collapsed")

st.header("Welcome to News X")
st.write("A news dashbaord for all your needs")

st.image("news-x.png", width=300, caption="news-x-logo")

st.write(
    "NEWS-X is a user-friendly, Python-powered news dashboard that puts you in control of your news consumption. With a straightforward design and an array of features, this application allows you to read, manage, and visualize news effortlessly."
)

if st.button("Login", use_container_width=True, type="primary"):
    switch_page("login")


if st.button("Sign Up", use_container_width=True):
    switch_page("sign up")
