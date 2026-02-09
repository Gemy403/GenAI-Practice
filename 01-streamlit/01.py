import streamlit as st


st.title("Hello Gemy")
st.header("Test")
st.subheader("Test 2")
st.markdown("# Welcone 1")
st.markdown("## Welcone 2")
st.markdown("### Welcone 3")
st.caption("my caption")

st.button ('Login')

st.latex(r"E = mc^2")

st.code("import os \n print('hello Gemy')")

st.write("Simple Text")

## metric

st.metric("Temp","11C","1.5C",delta_color="normal")
st.metric("Temp","11C","-1.5C",delta_color="normal")
st.metric("Temp","11C","1.5C",delta_color="inverse")

## input
f= st.text_input("Enter Your Name: ")
print(f)