FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.

    :param filepath: Location on disk of the to-do list.
    :return: The todos as a list.
    """
    with open(filepath, 'r') as todos_file:
        current_todos = todos_file.readlines()
    return current_todos

def write_todos(todo_list, filepath=FILEPATH):
    """ Write the to-do list into a text file.
    :param todo_list: List of todos
    :param filepath: Location on disk of where to write todos
    :return: None
    """
    with open(filepath, 'w') as todos_file:
        todos_file.writelines(todo_list)


if __name__ == "__main__":
    print("Hello")