import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config("Home", page_icon="🏠", initial_sidebar_state="collapsed")

st.write("# Welcome to News X")

st.image("news-x.png", width=300, caption="News-X: Logo")
if st.button("Login", use_container_width=True, type="primary"):
    switch_page("login")

if st.button("Sign Up", use_container_width=True):
    switch_page("sign up")
