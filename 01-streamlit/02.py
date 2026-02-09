import streamlit as st

from streamlit_extras.add_vertical_space import add_vertical_space
def example():
    add_n_lines = st.slider("Add n vertical lines below this", 1, 20, 5)
    add_vertical_space(add_n_lines)
    st.write("Here is text after the nth line!")



from streamlit_card import card
hasClicked = card(
  title="Hello World!",
  text="Some description",
  image="http://placekitten.com/200/300",
  url="https://github.com/gamcoh/st-card"
)