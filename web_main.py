import streamlit as st
import func
import time
import os

if not os.path.exists('todos.json'):
    with open('todos.json', 'w') as file:
        file.write('{}')


def add_todo():
    todo_local = st.session_state['new_todo']
    todos_local = func.get_todos()
    num_of_todos = len(todos)
    timestamp = time.strftime('%A %d %B %Y, %I:%M:%S %p')
    todos_local[f'Todo_{str((num_of_todos + 1))}'] = {'message': todo_local, 'timestamp': timestamp}
    func.write_todos(todos_local)
    print('Added successfully')


st.title('My todo application')
st.subheader('This application was made by sparsh singh')
todos = func.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todos[todo]['message'],
                           key=f'Todo_{index}')
    if checkbox:
        new_todo = todos[todo]['message']
        for todo_this in todos.copy():
            if todos[todo_this]['message'] == new_todo:
                todos.pop(todo_this)
        todos = func.rearrange_todos(todos)
        func.write_todos(todos)
        del st.session_state[f'Todo_{index}']
        st.experimental_rerun()

st.text_input(label='',
              placeholder='Add new todo...',
              key='new_todo',
              on_change=add_todo)
