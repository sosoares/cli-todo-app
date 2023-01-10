import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key= "todo")
add_button = sg.Button("Add")
reset_button = sg.Button("Reset")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button, reset_button]],
                   font=('Helvetica', 14))
while True:
    event, values = window.read() # this return values

    print(event) #this returns the button name, and the value from the input text
    #it returns the value as a tuple and you can untuple it already
    print(values)

    match event:
        case 'Add':
            todo = values['todo']
            functions.update_todos(todo)
        case sg.WIN_CLOSED:
            break





window.close()


