# streamlit_todo_ui.py
import streamlit as st
import requests

# FastAPI Server URL

# Title
st.title("FastAPI Todo App")

# Function to fetch all todos
def get_all_todos():
    response = requests.get("http://localhost:8000/")
    return response.json()

# Function to fetch done todos
def list_done_todos():
    response = requests.get("http://localhost:8000/done")
    return response.json()

# Function to create a new todo
def create_todo(text, is_complete=False):
    payload = {"text": text, "is_done": is_complete}
    response = requests.post("http://localhost:8000/create", json=payload)
    return response.json()


# Function to update a todo
def update_todo(id, text=""):
    payload = {"text": text}
    response = requests.put(f"http://localhost:8000/update/{id}", json=payload)
    return response.json()

# Function to delete a todo
def delete_todo(id:int):
    print("Calling delete")
    response = requests.delete(f"http://localhost:8000/delete/{id}")
    return response.json()

# Display all todos
st.header("All Todos")
todos = get_all_todos()
if not todos:
    st.info("No todos found.")
else:
    for todo in todos:
        st.write(f"- {todo['text']} (ID: {todo['id']})")

# Add a new todo
st.header("Add a New Todo")
new_todo_text = st.text_input("Enter new todo:")
if st.button("Add Todo"):
    create_todo(new_todo_text)
    st.success(f"Todo '{new_todo_text}' added!")

# Update an existing todo
st.header("Update a Todo")
update_todo_id = st.text_input("Enter todo ID to update:")
update_todo_text = st.text_input("Enter new text (leave blank to keep existing):") 
if st.button("Update Todo"):
    update_todo(update_todo_id, update_todo_text)
    st.success(f"Todo with ID {update_todo_id} updated!")

# Delete a todo
st.header("Delete a Todo")
delete_todo_id = st.text_input("Enter todo ID to delete:")
if st.button("Delete Todo"):
    delete_todo((delete_todo_id))
    st.warning(f"Todo with ID {delete_todo_id} deleted!")

# To run the app, use the following command in your terminal:
# streamlit run streamlit_todo_ui.py
