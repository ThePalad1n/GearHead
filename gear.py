'''
Eirc J. Estadt
10.18.22
This class represents the gear data structure.
This data structure is a circular list with the ability to rotate.
Methods:
nameGear()
---Gives value from input to name attribute
addTooth()
---Add values to gear from input
rotR()
---Rotates the gear right
rotL()
---Roatates the gear left
lock()
---Prevents further rotation
free()
---Allows rotation again
printGear()
'''
class Gear:
    def __init__(self):
        self.name = None
        self.ag = []
        self.locked = False 
    def nameGear(self,newName):
        self.name = newName
    def addTooth(self,item):
        if type(item) != type([]):      #Checks if it is a list, if it is the program will append 1 element at a time
            self.ag.append(item)
        else:
            for i in range(len(item)):
                self.ag.append(item[i])
    def rotR(self):
        if self.locked == False:
            self.ag.insert(len(self.ag)-1,self.ag.pop(0))
    def rotL(self):
        if self.locked == False:
            self.ag.insert(0,self.ag.pop(len(self.ag)-1))
    def lock(self):
        self.locked = True
    def free(self):
        self.locked = False

    def printGear(self):
        print(self.name, self.ag)

    def length(self):
        return len(self.ag)

    def getHalf(self):
        return (self.length()//2) if(self.length() % 2 == 0) else ((self.length()+1)//2)

    def append(self, object):
        self.ag.append(object)

    def pop(self, pos):
        return self.ag.pop(pos)

    def insert(self, pos, object):
        self.ag.insert(pos, object)

'''
gear = Gear()
gear.name = 'A'
gear.addTooth(1)
gear.addTooth(2)
gear.addTooth(3)
gear.addTooth(4)
gear.lock()
gear.printGear()
gear.rotL()
gear.printGear()
gear.rotR()
gear.printGear()
'''