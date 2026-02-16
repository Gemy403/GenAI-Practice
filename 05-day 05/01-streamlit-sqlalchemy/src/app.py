import streamlit as st

from database import Task,get_session

def main():
    st.title("Taks Manager")
    menu_items = ["Create","Read","Update","Delete"]
    choices = st.sidebar.selectbox("Menu",menu_items)


if __name__ == "__main__":
    main()