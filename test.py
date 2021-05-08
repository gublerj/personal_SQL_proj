import sqlite3

#from itertools import chain

"""
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM contacts")
db_len = len(cursor.fetchall())
db_index_range = range(db_len)
"""

"""
test = [('a',), ('b',)]

print(test[0][0])

print(".......................")

print(list(chain.from_iterable(test)))
"""


"""
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()

"""