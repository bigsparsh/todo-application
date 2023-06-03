import PySimpleGUI as gui
import func
import time

add_label = gui.Text('Enter todo: ')
add_input = gui.InputText(tooltip='Enter todo', key='todo')
add_btn = gui.Button('Add')
complete_btn = gui.Button('Complete')

todo_listbox = gui.Listbox(values=[func.get_todos()[key]['message'] for key in func.get_todos()],
                           size=(40, 10),
                           key='todos',
                           enable_events=True)
edit_btn = gui.Button('Edit')

window = gui.Window('Todo Application',
                    layout=[[add_label], [add_input, add_btn], [todo_listbox, edit_btn, complete_btn]],
                    font=('OCR A Extended', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = func.get_todos()
            todo = value['todo']
            num_of_todos = len(todos)
            timestamp = time.strftime('%A %d %B %Y, %I:%M:%S %p')
            todos[f'Todo_{str((num_of_todos + 1))}'] = {'message': todo, 'timestamp': timestamp}
            func.write_todos(todos)
            window['todos'].update(values=[todos[key]['message'] for key in todos])
            print('Added successfully')
        case 'Edit':
            new_todo_value = value['todo']
            todo_to_edit = value['todos'][0]
            timestamp = time.strftime('%A %d %B %Y, %I:%M:%S %p')
            todos = func.get_todos()
            for todo in todos:
                if todos[todo]['message'] == todo_to_edit:
                    print(todos[todo]['message'])
                    todos[todo]['message'] = f'{new_todo_value} (edited)'
                    todos[todo]['timestamp'] = f'{timestamp} (Updated)'
            window['todos'].update(values=[todos[key]['message'] for key in todos])
            func.write_todos(todos)
            print('Edited successfully')
        case 'Complete':
            todo_to_complete = value['todos'][0]
            todos = func.get_todos()
            for todo in todos.copy():
                if todos[todo]['message'] == todo_to_complete:
                    todos.pop(todo)
            todos = func.rearrange_todos(todos)
            func.write_todos(todos)
            window['todos'].update(values=[todos[key]['message'] for key in todos])
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case gui.WIN_CLOSED:
            break

window.close()
