import streamlit as st 
st.title("Additon of two numbers")


a = st.number_input("Please enter the fisrt no?")
b = st.number_input("Please enter the second no?")
st.sidebar.title("Main SLide bar")

if st.sidebar.button("Click me"):
    st.write("Buuton is clicked")
a = st.sidebar.text_input("Please enter your name")
if st.sidebar.button("Show my name"):
    st.markdown(f"## YOur name is {a}")

option = st.sidebar._selectbox(
    "Select an option",
    ["OPTION 1", "OPTION 2", "OPTION 3"]
)
slider_value = st.sidebar.slider(
    "Select a range",
    0 , 100 , (25,75)
)
st.sidebar.title("Second Side bar")
if st.button("Addition"):
    z = a + b
    st.write(str(z))
    
    
    
col1, col2 , col3 = st.columns(3)

with col1:
    st.header("Columns 1")
    if st.button("Column 1"):
        st.write("Column 1 button is clicked")
with col2:
    st.header("Columns 2")
    if st.button("Column 2"):
        st.write("Column 2 button is clicked")
        
with col3:
    st.header("Columns 3")
    if st.button("Column 3"):
        st.write("Column 3 button is clicked")