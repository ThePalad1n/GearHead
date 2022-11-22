from ast import match_case
from hashlib import new
from gear import Gear
from TrainOfGears import trainOfGears


#rich changes
#evan changes
def display():
    while(True):
        #print('1. New Gear\n2. Add Tooth\n3. Rotate Left\n4. Rotate Right')
        print('1. Insert Word or Phrase\n2. Encode\n3. Decode')
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
display()
