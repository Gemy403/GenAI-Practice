import streamlit as st

from database import Task,get_session

def main():
    ## create session
    session = get_session()

    st.title("Taks Manager")
    menu_items = ["Create","Read","Update","Delete"]
    choices = st.sidebar.selectbox("Menu",menu_items)
    
    ## CRU Operations
    if choices == "Create":
        st.subheader("Add New Task") 
        title = st.text_input("Task Title")
        description = st.text_area("Task Description")
        
        if st.button("Add Task"):
            new_task = Task(title=title,description=description)
            session.add(new_task)
            session.commit()
            st.success("Task Added Successfully !")


    elif choices == "Read":
        st.subheader("Read Task") 

    elif choices == "Read":
        st.subheader("Ciew Task") 

    elif choices == "Update":
        st.subheader("Update Task") 

    elif choices == "Delete":
        st.subheader("Delete Task") 



if __name__ == "__main__":
    main()