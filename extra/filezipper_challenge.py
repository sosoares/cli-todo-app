import PySimpleGUI as sg


button1 = sg.FilesBrowse("Choose")
button2 = sg.FolderBrowse("Choose")

label_file = sg.Text('Select files to compress:')
label_folder = sg.Text('Select destination folder:')

file_input = sg.InputText(tooltip='Select files to compress')
folder_input = sg.InputText(tooltip='Select destination folder')

compress_button = sg.Button("Compress")

window = sg.Window("File Zipper",
                   layout=[
                       [label_file, file_input,button1],
                       [label_folder, folder_input,button2],
                       [compress_button]])
window.read()
window.close()