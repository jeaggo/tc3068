import streamlit as st

# Create the title for the web app
st.title("My First Streamlit App")
sidebar = st.sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")


st.header("Dataset Overview")

st.header("Data Description")

st.write("""
# Simple Example Prediction App

This app predicts my data!

""")