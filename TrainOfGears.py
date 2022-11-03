
from gear import Gear
class trainOfGears:
    def __init__(self):
        self.gear = Gear()
        self.left = Gear()
        self.right = Gear()
    def makeTrain(self,gear):
        self.gear.name("Parent")
        self.left.nameGear("E")
        self.right.nameGear("E2")

        chars = [x for x in gear]
        self.gear.addTooth(chars)
        
        for i in range(self.gear.length()):
            self.left.addTooth(1)
            self.right.addTooth(1)
    def pRotL(self):
        self.gear.rotL()
        self.left.rotR()
        self.right.rotR()
    def pRotR(self):
        self.gear.rotR()
        self.left.rotL()
        self.right.rotL()