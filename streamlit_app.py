import streamlit as st
from src.core.ai_engine import get_response  # adjust path as needed

st.title("Tanushka AI Assistant")

user_input = st.text_input("You:")
if user_input:
    response = get_response(user_input)
    st.write("Tanushka:", response)
