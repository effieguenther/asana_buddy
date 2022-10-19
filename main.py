from pose import Pose, Library, Sequence
import PySimpleGUI as sg

def open_library():
    layout_col1 = [
        [sg.Text("This is where the library will go")]
    ]

    layout_col2 = [
        [sg.Text("This is where the images and description will appear")]
    ]

    layout_library = [
        [sg.Text('Asana Library', key='open')],
        [sg.Column(layout_col1), sg.VSeparator(), sg.Column(layout_col2)],
        [sg.Button('Quit')]
    ]

    window_lib = sg.Window('Asana Library', layout_library, size=(800, 600), modal=True)
    while True:
            event = window_lib.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
    window_lib.close()

def open_routine_build():
    layout_build = [ 
        [sg.Text('This is where the routine builder will go')],
        [sg.Button('Quit')]
    ]
    window_build = sg.Window('Routine Builder', layout_build, size=(800, 600))
    while True:
        event = window_build.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
    window_build.close()

def open_begin():
    layout_begin = [
        [sg.Text("Welcome to Asana Buddy!", justification='center')],
        [sg.Button('Asana Library'), sg.Button('Routine Builder')],
        [sg.Button('Quit')]
    ]

    window = sg.Window('Asana Buddy', layout_begin, size=(400,300))        
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        if event == 'Asana Library':
            open_library()
        if event == 'Routine Builder':
            open_routine_build()
    window.close()

def main():
    lib = Library('standing', 'seated', 'supine', 'prone', 'arm & leg')

    mountain = Pose('mountain', 'tadasana', 'standing', 'neutral', lib)
    chair = Pose('chair', 'utkatasana', 'standing','balancing', lib)
    crescent_lunge = Pose('crescent lunge', 'ashta chandrasana', 'standing', 'balancing', lib)
    forward_bend = Pose('forward bend', 'uttanasana', 'standing', 'forward bend', lib)
    halfway_lift = Pose('halfway lift', 'ardha uttanasana', 'standing', 'forward bend', lib)
    mountain_arms_up = Pose('mountain arms up', 'urdhva hastasana', 'standing', 'neutral', lib)
    warrior1 = Pose('warrior I', 'virabhadrasana a', 'standing', 'balancing', lib)
    warrior2 = Pose('warrior II', 'virabhadrasana b', 'standing', 'balancing', lib)
    down_dog = Pose('downward dog', 'adho mukha shvanasana', 'arm & leg', 'forward bend', lib)

    seq = Sequence(mountain, lib)
    print(seq._order[0])
    print(seq._order[1])
    print(seq._order[2])
    print(seq._order[3])
    print(seq._order[4])

    seq1 = Sequence(seq._order[4], lib)
    print(seq1._order[0])
    print(seq1._order[1])
    print(seq1._order[2])
    print(seq1._order[3])
    print(seq1._order[4])
    
main()