from functions import show_todos, update_todos
import time

day = time.strftime("%d-%m-%Y")
hour = time.strftime("%H:%M")

print(f"Hello, today is {day} and the time is {hour}")

with open('todos.txt', 'r') as file:
    todos = file.readlines()  # transform the text to a list

while True:
    user_action = input("Type add, edit, remove, complete, show or exit: ")
    user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action.split(' ', maxsplit=1)

        # another option to do the same thing to get the (to do), is to slice it for example (to do) = user_actions[4:0]
        todos.append(todo[1] + '\n')
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('edit'):
        try:
            change = user_action.split(" ", maxsplit=1)
            change = int(change[1])
            rewrite = input('Insert new to do: ')
            todos[change - 1] = rewrite + '\n'
            update_todos()
        except ValueError:
            print('Your command is not valid')
            continue #this is begin the while loop again, so we don't have to ask the user input again
    elif user_action.startswith('show'):
        show_todos()

    elif user_action.startswith('remove'):
        show_todos()
        index = int(user_action.split(' ', maxsplit=1)[1])
        todos.pop(index-1)
        update_todos(todos)
        show_todos()
    elif user_action.startswith('complete'):
        try:
            completed = user_action.split(" ", maxsplit=1)
            completed = int(completed[1])
            todos.pop(completed-1)
            update_todos(todos)
            show_todos()
        except IndexError:
            print('Invalid command')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('This command is not valid')




