import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This is to increase your productivity.")

st.checkbox("Buy grocery.")
st.checkbox("Throw trash")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Todo label", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

st.session_state
