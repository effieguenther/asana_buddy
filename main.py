from platform import java_ver
import time
import io
import os
from PIL import Image
import PySimpleGUI as sg

asanas = __import__('asanas')

def play_routine(routine, routine_timing):
    layout = [[sg.Image(asanas.mountain._image, size=(400,400), key = '-img-')],
        [sg.Button('Quit')],
        [sg.Button('Begin')]
    ]
    window = sg.Window('Routine', layout, size=(800, 600))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        if event == 'Begin':
            for i in range(0, len(routine)):
                for j in range(0, len(routine[i]._order)):
                    window['-img-'].update(routine[i]._order[j]._image)
                    time.sleep(routine_timing[i][j])
    window.close()


def input_length(question):
    while True:
        try:
            length = int(input(question))
        except ValueError:
            print("Please enter an integer")
            continue
        if length > 200:
            print("Woah, that's a long time! Please enter a number between 3 and 120")
            continue
        if length < 3:
            print("That's no time at all! Please enter a number between 3 and 120")
            continue
        else:
            return length
            break

def input_pace(question):
    while True:
        pace = input(question)
        if pace != 'fast' and pace != 'slow':
            print("Please enter 'fast' or 'slow'")
            continue
        else:
            return pace
            break

def main():

    print('Welcome to Asana Buddy!')
    print('Would you like to view the list of poses? (yes or no)')
    while True:
        y_n = input()
        if y_n == 'yes' or y_n == 'Yes':
            for i in asanas.lib._poses:
                for j in asanas.lib._poses[i]:
                    for k in range(0, len(asanas.lib._poses[i][j])):
                        print(f"{asanas.lib._poses[i][j][k]} - {asanas.lib._poses[i][j][k]._sanskrit}")
                        print(asanas.lib._poses[i][j][k]._desc)
                        print()
            break
        if y_n == 'no' or y_n == 'No':
            break
        print("Please enter 'yes' or 'no', or 'quit'")
        if y_n == 'quit':
            exit()    
    length = input_length("Let's begin your routine! How long would you like to exercise? (in minutes): ")
    pace = input_pace("Would you like the pace to be fast or slow?: ")
    
    routine = asanas.lib._build_routine(asanas.mountain, length, pace)
    routine_timing = asanas.lib._get_routine_timing(routine, length, pace)

    play_routine(routine, routine_timing)

main()