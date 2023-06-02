import PySimpleGUI as gui
import func
import time

add_label = gui.Text('Enter todo: ')
add_input = gui.InputText(tooltip='Enter todo', key='todo')
add_btn = gui.Button('Add')

todo_listbox = gui.Listbox(values=[func.get_todos()[key]['message'] for key in func.get_todos()],
                           size=(40, 10),
                           key='todos')
edit_btn = gui.Button('Edit')

window = gui.Window('Todo Application',
                    layout=[[add_label], [add_input, add_btn], [todo_listbox, edit_btn]],
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
            func.write_todos(todos)
            print('Edited successfully')

        case gui.WIN_CLOSED:
            break

window.close()
