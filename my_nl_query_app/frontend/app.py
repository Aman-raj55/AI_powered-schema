import streamlit as st
import requests

st.title("AI-Powered Table Selector")

query = st.text_input("Enter your query:")
if st.button("Find Tables"):
    response = requests.post("http://127.0.0.1:8000/filter-tables/", json={"query": query})
    st.json(response.json()["filtered_schema"])