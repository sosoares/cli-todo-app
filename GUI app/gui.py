import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key= "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key='items',
                      enable_events= True, size=[45,10])


window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button, edit_button],
                           [list_box]
                           ],
                   font=('Helvetica', 14))
while True:
    event, values = window.read() # this return values

    print(event) #this returns the button name, and the value from the input text
    #it returns the value as a tuple and you can untuple it already
    print(values)

    match event:
        case 'Add':
            todo = values['todo']
            todos = functions.get_todos()
            todos.append(todo + '\n')
            functions.update_todos(todos)

            window['items'].update(values=todos)

        case 'Edit':
            to_edit = values['items'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todos()
            index= todos.index(to_edit)
            todos[index] = new_todo
            functions.update_todos(todos)

            window['items'].update(values= todos)

            print(to_edit)
        case 'items':
            window['todo'].update(value= values['items'][0])

        case sg.WIN_CLOSED:
            break





window.close()


