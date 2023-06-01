import PySimpleGUI as gui

label = gui.Text("Type in a todo: ")
input_ = gui.InputText(tooltip='Enter todo')
btn = gui.Button('Add')
window = gui.Window('Sparsh Singh', layout=[[label, input_], [btn]])
window.read()
window.close()
