def get_todos(filepath="files/todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


# to behave as procedure function
def write_todos(todos_arg, filepath="files/todos.txt"):   # multiple arguments
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    # get user input and strip/remove space chars
    user_action = input("Type add, show, edit, complete or exit: ")
    # strip function to remove extra whitespaces
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]      # slice input

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)      # as default no need to put filepath

    # | Bitwise OR Operator
    # f"{},{}"   - {} f_string
    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            # to remove extra break line in print, use list comprehension
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        number = int(user_action[5:])
        print(number)
        number = number - 1

        todos = get_todos()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        write_todos(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = get_todos()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")

print("Bye!")


