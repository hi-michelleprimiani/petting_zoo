
from animals import Animal
from movements import Walking


class Goat(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
