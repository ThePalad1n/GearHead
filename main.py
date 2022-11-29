from ast import match_case
from hashlib import new
from gear import Gear
from TrainOfGears import trainOfGears



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
                '''
            case '2':
                ToG.encode()
                '''
                Function Process:
                //set for number of elements
                chars = [x for x in input()]
                //add teeth to the gear with for element
                newG.addTooth(chars)
                //print newly toothed gear
                newG.printGear()
                '''
            case '3':
                ToG.decode()
                '''
                Function Process:
                //rotate gear in reverse order
                newG.rotL()
                //print decoded phrase
                newG.printGear()
                '''
            case '4':
                exit()
display()
