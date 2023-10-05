from swimming import Bass, Goldfish, Catfish, Koi, Trout
from slithering import Copperhead, RatSnake, Python, Anaconda, Cobra
from walking import Donkey, Llama, Goat, Chicken, Cow
from attractions import PettingZoo, SnakePit, Wetlands
from datetime import date


# walking
llama = Llama("Larry", "Llama glama", "afternoon", "Llama Chow")
donkey = Donkey("Donkey Kong", "Domestic Donkey", "midday", "Hay")
goat = Goat("Billy", "Domestic Goat", "afternoon", "Goat Feed")
chicken = Chicken("Henrietta", "Hen", "midday", "Chicken Feed")
cow = Cow("MooMoo", "Holstein Cow", "morning", "Grass")
# slithering
copperhead = Copperhead("Slither", "American Copperhead", "Mice")
ratsnake = RatSnake("Ratty", "Rat Snake", "Rats")
python = Python("Monty", "Ball Python", "Small Mammals")
anaconda = Anaconda("Anna", "Green Anaconda", "Large Rodents")
cobra = Cobra("King", "King Cobra", "Small Mammals")
# swimming
bass = Bass("Bassy", "Largemouth Bass", "Fish Food")
goldfish = Goldfish("Goldie", "Common Goldfish", "Goldfish Flakes")
catfish = Catfish("Whiskers", "Channel Catfish", "Catfish Pellets")
koi = Koi("Koiboi", "Japanese Koi", "Koi Food")
trout = Trout("Trouty", "Rainbow Trout", "Fish Pellets")
# attractions
varmint_village = PettingZoo(
    "Varmint Village", "cute and fuzzy critters to cuddle")
the_slither_inn = SnakePit(
    "The Slither Inn", "slithering reptiles, not for the faint of heart")
critter_cove = Wetlands(
    "Critter Cove", "aquatic life, both cute and interesting")


varmint_village.add_animal(llama)
varmint_village.add_animal(donkey)
varmint_village.add_animal(goat)
varmint_village.add_animal(chicken)
varmint_village.add_animal(cow)

the_slither_inn.add_animal(copperhead)
the_slither_inn.add_animal(ratsnake)
the_slither_inn.add_animal(python)
the_slither_inn.add_animal(anaconda)
the_slither_inn.add_animal(cobra)

critter_cove.add_animal(bass)
critter_cove.add_animal(goldfish)
critter_cove.add_animal(catfish)
critter_cove.add_animal(koi)
critter_cove.add_animal(trout)

# petting zoo
print(
    f"{varmint_village.attraction_name} is where you'll find {varmint_village.description} like,")
for animal in varmint_village.animals:
    print(f'    *{str(animal)}')

# snake pit
print(
    f"{the_slither_inn.attraction_name} is where you'll find {the_slither_inn.description} like,")
for animal in the_slither_inn.animals:
    print(f'    *{str(animal)}')

# wetlands
print(
    f"{critter_cove.attraction_name} is where you'll find {critter_cove.description} like,")
for animal in critter_cove.animals:
    print(f'    *{str(animal)}')
