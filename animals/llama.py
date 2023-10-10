from datetime import date
from animals import Animal
from movements import Walking


class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
        self.shift = shift

    def feed(self):
        return print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')
