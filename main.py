import streamlit as st 
import pandas as pd
st.title("Pakistan")
st.header("Its a header")
st.markdown(" :moon:")
st.chat_input("Enter your name?")
data = pd.read_csv("train.csv")

st.table(data)