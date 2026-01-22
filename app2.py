import streamlit as st

st.title("Hello, Streamlit!")
age = st.slider("Select your age", 0, 100)

city = st.selectbox("Select your city", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
st.button("Submit")

st.write("Age:", age)
st.write("City:", city)