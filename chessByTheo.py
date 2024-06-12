
import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text("Choose your option:")],
            [sg.Button('Version 1.5 - Console UI')], 
            [sg.Button('Version 1.6+ - GUI')],
            [sg.Button('Quit Game')] ]

# Create the Window
window = sg.Window('Chess by Theo', layout)

while True:
    event, values = window.read()

    if event == 'Version 1.5 - Console UI':
        window.close()
        with open("chess-v1.5-consoleUI_stableVersion.py") as file:
            exec(file.read())
    elif event == 'Version 1.6+ - GUI':
        window.close()
        with open("chess-v1.6.py") as file:
            exec(file.read())
    elif event == sg.WIN_CLOSED or event == 'Quit Game': 
        window.close()
        break