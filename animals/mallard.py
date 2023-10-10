
from animals import Animal
from movements import Walking, Swimming


class Mallard(Animal):

    def __init__(self, name, species, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
        Swimming.__init__(self)

    def run(self):
        print(f"{self} waddles really fast")

    def num_legs(self):
        print(f"{self} has {self.legs} legs")
