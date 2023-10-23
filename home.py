import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config("Home", page_icon="🏠", initial_sidebar_state="collapsed")

st.header("Welcome to News X")
st.write("A news dashbaord for all your needs")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(" ")

with col2:
    st.image("news-x.png", width=300)

with col3:
    st.write(" ")

if st.button("Login", use_container_width=True, type="primary"):
    switch_page("login")


if st.button("Sign Up", use_container_width=True):
    switch_page("sign up")
