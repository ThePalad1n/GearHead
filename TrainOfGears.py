
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

    def encode(self): #still need to make sure this is turning correctly, sorry oops
        y = self.gear.length()
        print(y)
        for i in range(y - 1):
            self.pRotL()
            self.right.append(self.gear.pop(1))
            self.gear.insert(0, self.right.pop(-2))
            self.left.insert(0, self.gear.pop(-1))
            self.gear.append(self.left.pop(-1))
        # self.left.insert(0, self.gear.pop(-1))
        # self.gear.insert(0,self.right.pop(-2))
        self.gear.printGear()
        self.right.printGear()
        self.left.printGear()

ToG = trainOfGears()
ToG.makeTrain("Gear")
ToG.encode()
