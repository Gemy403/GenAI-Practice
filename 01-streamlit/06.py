import streamlit as st
from datetime import timedelta

def add_time():
    initial_value = st.session_state["start_date"]
    days = int(st.session_state["days"].split(" ")[0])
    st.session_state["end_date"] = initial_value + timedelta(days=days)

     

##
st.radio("Select Days",["7 Day","10 Day","15 Days"],
         horizontal=True,
         key="days",
        #  index=1
         )

col1,col2 = st.columns(2)

col1.date_input("Start date",key="start_date",on_change=add_time)
col2.date_input("End Date",key="end_date")
st.write(st.session_state)

