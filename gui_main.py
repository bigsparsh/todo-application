import PySimpleGUI as gui
import func
import time

add_label = gui.Text('Enter todo: ')
add_input = gui.InputText(tooltip='Enter todo', key='todo')
add_btn = gui.Button('Add')

window = gui.Window('Todo Application',
                    layout=[[add_label], [add_input, add_btn]],
                    font=('OCR A Extended', 20))

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = func.get_todos()
            todo = value['todo']
            num_of_todos = len(todos)
            timestamp = time.strftime('%A %d %B %Y, %I:%M:%S %p')
            todos[f'Todo_{str((num_of_todos + 1))}'] = {'message': todo, 'timestamp': timestamp}
            func.write_todos(todos)
            print('Added successfully')

window.close()
