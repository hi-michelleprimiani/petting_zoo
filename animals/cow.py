
from animals import Animal
from movements import Walking


class Cow(Animal):

    def __init__(self, name, species, shift, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
        self.shift = shift

    def feed(self):
        return print(f"On {self.date_added.strftime('%m/%d/%Y')}, Miss {self.name} only eats her {self.food} when she listens to Moo by Doja Cat.")

    def num_legs(self):
        print(f"{self} has {self.legs} legs")
