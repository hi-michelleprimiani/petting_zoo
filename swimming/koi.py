from datetime import date


class Koi:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
