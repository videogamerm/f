# hello_psg.py

import PySimpleGUI as sg
from playsound import playsound
layout = [[sg.Text("Spooooookeeeee")], [sg.Button("Spookeeeeee")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Spookeeeeee":
        playsound("/home/mason/Music/secretLoop02.mp3")
        break
    elif event == sg.WIN_CLOSED:
        break

window.close()