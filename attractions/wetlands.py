from .attraction import Attraction


class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            # Check if the animal has a 'swim_speed' attribute
            if hasattr(animal, 'walk_speed'):
                print(
                    f"{animal} walks, so it can't be placed in {self.attraction_name}.")
                return

            if hasattr(animal, 'slither_speed'):
                print(
                    f"{animal} slithers, so it can't be placed in {self.attraction_name}.")
                return
        # Check if the animal can walk
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")

        except AttributeError as ex:
            print(
                f"{animal} doesn't like to be petted, so please do not put it in the {self.attraction_name} attraction."
            )
