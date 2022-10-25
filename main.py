# hello_psg.py

import PySimpleGUI as sg
from playsound import playsound
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK":
        playsound('spanish.mp3')

    elif event == sg.WIN_CLOSED:
        break

window.close()