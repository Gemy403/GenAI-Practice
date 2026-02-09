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

st.divider()

## input
f= st.text_input("Enter Your Name: ")
print(f)

rd_selection = st.radio(
    "Chose an option",
    ["option 1","option 2"]
    )
st.write(rd_selection)

ck_select = st.checkbox(
    "Please Select",value=True
    
)

st_box = st.selectbox(
    "Chose an option",
    ["option 1","option 2"]
    )

multi_select = st.multiselect(

    "Chose an option",
    ["option 1","option 2","option 3"]
    )
st.write(multi_select)

volume = st.slider("select Volume",0,100,10)
st.write(volume)

# st.date_input("Start Date")
# st.date_input("End Date")

col1,col2 = st.columns(2)
col1.date_input("Start Date")
col2.date_input("End Date")


st.info ("Data was saved")
st.warning ("Data Not saved")
st.error ("Data Error")

with st.sidebar:
    st.header("Home")    
    pdf_file = st.file_uploader("Upload PDF",type="pdf")