
from gear import Gear
class trainOfGears:
    def __init__(self):
        self.gear = Gear()
        self.left = Gear()
        self.right = Gear()
    def makeTrain(self, gear):
        self.gear.nameGear("Parent")
        self.left.nameGear("E1")
        self.right.nameGear("E2")
        Teeth = 0
        chars = [x for x in gear]
        self.gear.addTooth(chars)

        for i in range(len(chars)):#currently have it as different numbers to ensure it's doing what it's supposed to
            Teeth += 1
            self.left.addTooth(Teeth)
            self.right.addTooth(Teeth)
        #self.left.addTooth([1] * Teeth)

        #self.right.addTooth([1] * Teeth)
        self.gear.printGear()
        self.left.printGear()
        self.right.printGear()

    def pRotL(self):
        self.gear.rotL()
        self.left.rotR()
        self.right.rotR()

    def pRotR(self):
        self.gear.rotR()
        self.left.rotL()
        self.right.rotL()
    '''The following functions currently 
        print everything they do so that we can
        all follow along, please run this file'''
    def encode(self):
        y = self.gear.length()
        print(y)
        for i in range(y - 1):
            self.pRotL()
            x = self.gear.pop(0)
            y = self.right.pop(-1)
            self.right.append(x)
            self.gear.insert(0, y)
            x = self.gear.pop(-1)
            y = self.left.pop(0)
            self.left.insert(0, x)
            self.gear.append(y)
            self.gear.printGear()
            self.right.printGear()
            self.left.printGear()

    def decode(self):
        y = self.gear.length()
        print(y)
        for i in range(y - 1):

            x = self.gear.pop(0)
            y = self.right.pop(-1)
            self.right.append(x)
            self.gear.insert(0, y)
            x = self.gear.pop(-1)
            y = self.left.pop(0)
            self.left.insert(0, x)
            self.gear.append(y)
            self.pRotR()
            self.gear.printGear()
            self.right.printGear()
            self.left.printGear()



'''
ToG = trainOfGears()
ToG.makeTrain("Gear")
ToG.encode()
ToG.decode()
'''
