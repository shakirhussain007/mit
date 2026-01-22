import streamlit as st

st.title("Hello, Streamlit!")
Name = st.text_input("Welcome to your first Streamlit app.")

if st.button("Show Message"):
    st.write(Name)