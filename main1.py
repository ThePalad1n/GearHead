from ast import match_case
from hashlib import new
from gear import Gear

#rich changes
#evan changes
#take2
def display():
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
                newG = Gear()
                print('Name the gear')  
                newG.nameGear(input())
                newG.printGear()
                '''
            case '2':
                ToG.encode()
                '''
                chars = [x for x in input()]
                newG.addTooth(chars)
                newG.printGear()
                '''
            case '3':
                ToG.decode()
                '''
                newG.rotL()
                newG.printGear()
                '''
                '''   
            case '4':
                newG.rotR()
                newG.printGear()
                '''
            case '4':
                exit()
display()
