from animals import Animal
from movements import Walking, Swimming


class Alligator(Animal, Walking, Swimming):
    def __init__(self, name, species, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
        Swimming.__init__(self)
