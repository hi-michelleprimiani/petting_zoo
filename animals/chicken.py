from animals import Animal
from movements import Walking


class Chicken(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)

    def feed(self):
        return print(f"On {self.date_added.strftime('%m/%d/%Y')}, Miss {self.name} only eats her {self.food} when she listens to Moo by Doja Cat.")
