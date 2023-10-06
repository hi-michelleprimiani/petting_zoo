
from animals import Animal


class Cow(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        return print(f"On {self.date_added.strftime('%m/%d/%Y')}, Miss {self.name} only eats her {self.food} when she listens to Moo by Doja Cat.")
