# The package syntax is what allows for these clean import statements
from .animal import Animal
from movements import Walking, Swimming


class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num, legs):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
        Swimming.__init__(self)
        # no more self.swimming = True

    def honk(self):
        print("The goose honks. A lot")

    def run(self):
        print(f"{self} runs")

    def num_legs(self):
        print(f"{self} has {self.legs} legs")
