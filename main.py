from modules import functions

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}. {item.replace('\n', '')}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
        except ValueError:
            print("Your command is not valid.")
            continue
        print(number)
        number = number - 1
        new_todo = input("Enter new todo: ") + "\n"

        todos = functions.get_todos()
        todos[number] = new_todo
        functions.write_todos(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = functions.get_todos()

        index = number - 1
        try:
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
        except IndexError:
            print("There is no todo with that number.")
            continue

        functions.write_todos(todos)

        print(f"Todo '{todo_to_remove}' was removed from the list.")

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")

print("Bye!")