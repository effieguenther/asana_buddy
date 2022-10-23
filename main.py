from platform import java_ver
import time
from PIL import Image, ImageTk
import tkinter

asanas = __import__('asanas')
global i, j
i = 0
j = 0

class Window():
    def __init__(self, root, routine, routine_timing):
        self.canvas = tkinter.Canvas(root, width=600, height=600)
        self.canvas.pack()
        self.img = routine[0]._order[0]._image.resize((600, 600))
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.image_id = self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.tkimg)

    def change_image(self, routine, i, j):
        self.img = routine[i]._order[j]._image.resize((600, 600))
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.canvas.itemconfig(self.image_id, image=self.tkimg)
    
    def next(self, routine):
        global i, j
        if i >= len(routine) - 1:
            return
        if i < len(routine) and j == 4:
            i += 1
            j = -1
        if j < len(routine[i]._order):
            j += 1
            self.change_image(routine, i, j)
        self.canvas.after(1000, self.next(routine))

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

    root = tkinter.Tk()
    window = Window(root, routine, routine_timing)     
    window.next(routine)
    root.mainloop()


main()