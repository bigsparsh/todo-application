import json

FILENAME = 'todos.json'


def get_todos():
    """
    Returns the dictionary of todos in json file
    :return:
    """
    with open(FILENAME, 'r') as file_local:
        data = json.load(file_local)
    return data


def write_todos(data_local):
    """
    Writes the given dictionary into the json file
    :param data_local:
    :return:
    """
    with open(FILENAME, 'w') as file_local:
        json.dump(data_local, file_local, indent=4)


def rearrange_todos(data_local):
    """
    Rearranges the todo items after completion
    :param data_local:
    :return:
    """
    temp_dict = {}
    for index, key in enumerate(data_local.keys()):
        temp_dict[f'Todo_{index + 1}'] = {'message': data_local[key]['message'], 'timestamp': data_local[key]['timestamp']}
    return temp_dict
