FILEPATH = 'todos.txt' # good behaviour is to declare CONSTANTS in python is to use capital letters in the beginning of the code

def show_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()  # transform the text to a list
    print("Here is your updated list of items to do")
    for i, item in enumerate(todos):
        item = item.strip('\n')
        print(f"{i + 1} - {item}")


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos

def update_todos(tasks, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(tasks)
