import streamlit as st
import func
import time
import os

if not os.path.exists('todos.json'):
    with open('todos.json', 'w') as file:
        file.write('{}')

st.title('My todo application')
st.subheader('This application was made by sparsh singh')
todos = func.get_todos()

for todo in todos:
    st.checkbox(todos[todo]['message'])

st.text_input(label='',
              placeholder='Add new todo...')
