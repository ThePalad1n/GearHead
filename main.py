from ast import match_case
from hashlib import new
from gear import Gear
import TrainOfGears

#rich changes
#evan changes
#take2
def display():
    while(True):
        print('1. New Gear\n2. Add Tooth\n3. Rotate Left\n4. Rotate Right\n5. Exit')
        x=input()
        match x:
            case '1':
                newG = Gear()
                print('Name the gear')  
                newG.nameGear(input())
                newG.printGear()
            case '2':
                chars = [x for x in input()]
                newG.addTooth(chars)
                newG.printGear()
            case '3':
                newG.rotL()
                newG.printGear()
            case '4':
                newG.rotR()
                newG.printGear()
            case '5':
                exit()
display()
