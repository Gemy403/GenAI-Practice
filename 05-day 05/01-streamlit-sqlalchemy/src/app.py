import streamlit as st
from database import Task,get_session,create_task

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
            # new_task = Task(title=title,description=description)
            # session.add(new_task)
            # session.commit()
            create_task(session,title,description)
            st.success("Task Added Successfully !")


    elif choices == "Read":
        st.subheader("Read Task") 
        tasks = session.query(Task).all()
        for task in tasks :
            st.write(f"id: {task.id}")
            st.write(f"titled: {task.title}")
            st.write(f"Descriptiond: {task.description}")
            st.write("---------------------------------")

    elif choices == "Update":
        st.subheader("Update Task") 
        task_id = st.number_input("Task ID",min_value=1,step=1)
        task = session.query(Task).filter_by(id=task_id).first()
        if task :
            new_title= st.text_input("New Title",value=task.title)
            new_discription = st.text_area("New Discrption",value=task.description)
            if st.button("Update Task"):
                task.title = new_title
                task.description = new_discription
                session.commit()
                st.success("Updated Successfully !!")

        else:
            st.warning("Task Not Found")


    elif choices == "Delete":
        st.subheader("Delete Task") 
        task_id = st.number_input("Task ID",min_value=1,step=1)
        if st.button("Delete Task"):
            task = session.query(Task).filter_by(id=task_id).first()
            if task:
                session.delete(task)
                session.commit()
                st.success("Deleted Successfully !!")
            else:
                st.warning("Task Not Found !!")





if __name__ == "__main__":
    main()