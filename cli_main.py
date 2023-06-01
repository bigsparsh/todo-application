import func
import time

while True:
    command = input('You want to add, show, edit, complete or exit: ')
    operation = command.split(' ')[0]
    match operation.lower():
        case 'add':
            if len(command.split(" ")) > 1:
                data = func.get_todos()
                todo = command.strip(f'{operation} ')
                num_of_todos = len(data)
                timestamp = time.strftime('%A %d %B %Y, %I:%M:%S %p')
                data[f'Todo_{str((num_of_todos + 1))}'] = {'message': todo, 'timestamp': timestamp}
                func.write_todos(data)
                print('Added successfully')
            else:
                print('Invalid add command, specify the todo after the add command')
        case 'show':
            print()
            data = func.get_todos()
            for i, key in enumerate(data.keys()):
                print(f'=================|Todo - {i+1}|=================')
                print(f'Created on: {data[key]["timestamp"]}')
                print(f'Todo: {data[key]["message"]}')
                print('=============================================')
            print()
        case 'edit':
            edit_index = int(command.split(' ')[1])
            new_todo = command.strip(f'{operation} {edit_index} ')
            data = func.get_todos()
            todo_to_search = f'Todo_{edit_index}'
            timestamp = time.strftime('%A %d %B %Y, %I:%M:%S %p')
            data[todo_to_search]['message'] = new_todo + ' (edited)'
            data[todo_to_search]['timestamp'] = timestamp + ' (updated)'
            func.write_todos(data)
            print('Edited successfully')
        case 'complete':
            data = func.get_todos()
            try:
                complete_index = int(command.split(' ')[1])
                todo_to_complete = f"Todo_{complete_index}"
                data.pop(todo_to_complete)
                data = func.rearrange_todos(data)
                func.write_todos(data)
                print('Completed successfully')
            except ValueError as e:
                print('Invalid complete command, specify the correct todo number after the complete command')
                print(e)
            except KeyError as e:
                print('Invalid complete command, specify the correct todo number after the complete command')
                print(e)
        case 'exit':
            exit('All the data has been saved....')
        case _:
            print('Invalid command, try again.')