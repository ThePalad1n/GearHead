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

    #     nameGear()
    # ---Gives value from input to name attribute
    def nameGear(self,newName):
        self.name = newName


    #     addTooth()
    # ---Add values to gear from input
    def addTooth(self,item):
        if type(item) != type([]):      #Checks if it is a list, if it is the program will append 1 element at a time
            self.ag.append(item)
        else:
            for i in range(len(item)):
                self.ag.append(item[i])

    # rotR()
    # ---Rotate the gear right
    def rotR(self):
        if self.locked == False:
            self.ag.insert(len(self.ag)-1,self.ag.pop(0))

    # rotL()
    # ---Rotate the gear left
    def rotL(self):
        if self.locked == False:
            self.ag.insert(0,self.ag.pop(len(self.ag)-1))


    # lock()
    # ---Prevents further rotation
    def lock(self):
        self.locked = True


    # free()
    # ---Allows rotation again
    def free(self):
        self.locked = False


    # prints all info
    def printGear(self):
        print(self.name, self.ag)
        x = str(self.ag)
        y = str(self.name)
        # writing to text file
        with open('secret.txt', 'a') as f:
            f.writelines(y)
            f.writelines(x)
            f.writelines('\n')



    def length(self):
        return len(self.ag)



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