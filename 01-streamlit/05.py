import streamlit as st
import time

@st.cache_data
def processing():
    time.sleep(4)
    return [1,2,3,4,5,6,7]

st.write("Loading Data")

data = processing()

st.warning(data)