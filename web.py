import streamlit as st
import functions

todos = functions.get_todos()

st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This is to increase your productivity.")

st.checkbox("Buy grocery.")
st.checkbox("Throw trash")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Todo label", placeholder="Add new todo...")

