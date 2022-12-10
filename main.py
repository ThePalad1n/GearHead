from ast import match_case
from hashlib import new
from gear import Gear
'''
GUI! Can Encode but does not currently 
print encoded message where user can see. 
Can Decode but does not currently receive input
~Not Finished~ Committing so group can See It~ 
'''
from tkinter import *
from tkinter import ttk
from TrainOfGears import trainOfGears

main = Tk()
main.title("Gear Train")
main.geometry("500x500")
notebook = ttk.Notebook(main)
notebook.pack()

def select0():
    notebook.select(0)
    notebook.hide(1)
    notebook.hide(2)
def select1():
    notebook.select(1)
    notebook.hide(0)
    notebook.hide(2)

def select2():
    notebook.select(2)
    notebook.hide(0)
    notebook.hide(1)

def encodeinput():
    ToG = trainOfGears()
    ToG.makeTrain(EncodeInput.get())

    EncodedLabel = Label(frame1, textvariable = ToG.encode())
    EncodedLabel.pack()

def decodeinput():
    ToG = trainOfGears()
    ToG.decode()






frame0 = Frame(notebook, width = 500, height = 500, bg = "Gray18")

notebook.add(frame0, text = "frame0")
frame1 = Frame(notebook, width = 500, height = 500, bg = "Gray18")
notebook.add(frame1, text = "frame1")
frame2 = Frame(notebook, width = 500, height = 500, bg = "Gray18")
notebook.add(frame2, text = "frame2")
notebook.pack(fill = "both", expand =1)
notebook.hide(1)
notebook.hide(2)


Title0 =Label(frame0, text = "GearTrain", bg = "gray18", fg = "white", font=("Arial Black", 18, "bold"))
Title0.pack()
L1 = LabelFrame(frame0, text = "Instructions", bg = "SpringGreen4")
L1.pack(padx = 50, pady = 50)
Instructiontext =  Message(L1, text = "Welcome to GearTrain!\n Here you can encode and decode messages. \nPlease click one of the buttons below to begin", font=("Arial", 15), justify=CENTER, bg = "Gray90")
Instructiontext.pack()
EncodeFrameButton = Button(frame0, text = "Encode", bg = "SpringGreen4", fg = "white", command = select1)
EncodeFrameButton.pack(padx = 2, pady = 2)
DecodeFrameButton = Button(frame0, text = "Decode", bg = "SpringGreen4", fg = "white", command =  select2)
DecodeFrameButton.pack(padx = 2, pady = 2)

Title1= Label(frame1, text = "Type Message for Encoding", bg = "gray18", fg = "white",  font = ("Arial BLack", 18, "bold"))

Title1.pack(padx = 50, pady = 50)


EncodeInput = Entry(frame1)
EncodeInput.pack()
EncodeButton = Button(frame1, text = "Encode", bg = "SpringGreen4", fg = "white", command = encodeinput )
EncodeButton.pack(padx = 20, pady = 20)

BackButton1 = Button(frame1, text = "Back", bg = "SpringGreen4", fg = "white", command = select0)
BackButton1.pack(padx = 20, pady = 20)

Title2 = Label(frame2, text = "Decode", bg = "gray18", fg = "white",  font = ("Arial Black", 18, "bold"))
Title2.pack(padx = 50, pady = 50)
L3 = LabelFrame(frame2)
L3.pack()
Password = Entry(frame2)
Password.pack(padx=20, pady= 20)
DecodeButton = Button(frame2, text = "Decode", bg = "SpringGreen4", fg = "white", command = decodeinput)
DecodeButton.pack(padx = 20, pady = 20)
BackButton2 = Button(frame2, text = "Back", bg = "SpringGreen4", fg = "white", command= select0)
BackButton2.pack(padx = 20, pady = 20)















main.mainloop()


#rich changes
#evan changes
#take2
'''

def display():
    # conditional for our main menu screen
    while(True):

        #print('1. New Gear\n2. Add Tooth\n3. Rotate Left\n4. Rotate Right')
        print("            ___                            _____                     _            ")
        print("    o O O  / __|    ___    __ _      _ _  |_   _|    _ _   __ _     (_)    _ _    ")
        print("   o      | (_ |   / -_)  / _` |    | '_|   | |     | '_| / _` |    | |   | ' \   ")
        print("  TS__[O]  \___|   \___|  \__,_|   _|_|_   _|_|_   _|_|_  \__,_|   _|_|_  |_||_|  ")
        print(" {======|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| ")
        print("./o--000\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\'\"`-0-0-\' ")
        print()

        print('1. Insert Word or Phrase\n2. Encode\n3. Decode\n4. Exit')

        x=input()
        match x:
            case '1':
                ToG = trainOfGears()
                print("Please type message to be encoded")
                ToG.makeTrain(input())

                
=======
                '''
                Function Process:
                //Creates initial gear

                newG = Gear()
                //print name of new gear
                print('Name the gear') 
                //create array to encode
                newG.nameGear(input())
                //print new
                newG.printGear()
                
            case '2':
                ToG.encode()

                
=======
                '''
                Function Process:
                //set for number of elements

                chars = [x for x in input()]
                //add teeth to the gear with for element
                newG.addTooth(chars)
                //print newly toothed gear
                newG.printGear()
                
            case '3':
                ToG.decode()

                
                newG.rotL()
                newG.printGear()
            case '4':
                newG.rotR()

                '''
                Function Process:
                //rotate gear in reverse order
                newG.rotL()
                //print decoded phrase

                newG.printGear()

            case '4':
                exit()
display()
'''
