from platform import java_ver
from PIL import Image, ImageTk
import tkinter

asanas = __import__('asanas')

class Window():
    def __init__(self, root, routine, routine_timing):
        self.canvas = tkinter.Canvas(root, width=600, height=600)
        self.canvas.pack()
        self.img = routine[0]._order[0]._image.resize((600, 600))
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.image_id = self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.tkimg)

    def change_image(self, i, j, routine):
        self.img = routine[i]._order[j]._image.resize((600, 600))
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.canvas.itemconfig(self.image_id, image=self.tkimg)
                
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
    routine = asanas.lib._build_routine(asanas.mountain, length)
    routine_timing = asanas.lib._get_routine_timing(routine, length)

    for i in range(0, len(routine)):
        for j in range(0, len(routine[i]._order)):
            print(f"{routine[i]._order[j]} - hold for {routine_timing[i][j]} seconds")
    print("shavasana!")
   
    
    #tried to get the routine to show in a tkinter window but couldn't get it to work :( might revisit this some day

    #root = tkinter.Tk()
    #window = Window(root, routine, routine_timing)     
    #root.mainloop()


main()