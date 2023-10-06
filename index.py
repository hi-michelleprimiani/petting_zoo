from animals.swimming import Bass, Goldfish, Catfish, Koi, Trout
from animals.slithering import Copperhead, RatSnake, Python, Anaconda, Cobra
from animals.walking import Donkey, Llama, Goat, Chicken, Cow
from attractions import PettingZoo, SnakePit, Wetlands
from datetime import date
from animals import Animal

# walking
llama = Llama("Larry", "Llama glama", "afternoon", "Llama Chow", 1234)
donkey = Donkey("Donkey Kong", "Domestic Donkey", "midday", "Hay", 2345)
goat = Goat("Billy", "Domestic Goat", "afternoon", "Goat Feed", 3456)
chicken = Chicken("Henrietta", "Hen", "midday", "Chicken Feed", 4567)
cow = Cow("MooMoo", "Holstein Cow", "morning", "Grass", 5678)
# slithering
copperhead = Copperhead("Slither", "American Copperhead", "Mice", 6789)
ratsnake = RatSnake("Ratty", "Rat Snake", "Rats", 7890)
python = Python("Monty", "Ball Python", "Small Mammals", 8901)
anaconda = Anaconda("Anna", "Green Anaconda", "Large Rodents", 9012)
cobra = Cobra("King", "King Cobra", "Small Mammals", 2222)
# swimming
bass = Bass("Bassy", "Largemouth Bass", "Fish Food", 1357)
goldfish = Goldfish("Goldie", "Common Goldfish", "Goldfish Flakes", 2468)
catfish = Catfish("Whiskers", "Channel Catfish", "Catfish Pellets", 3579)
koi = Koi("Koiboi", "Japanese Koi", "Koi Food", 4680)
trout = Trout("Trouty", "Rainbow Trout", "Fish Pellets", 5791)

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


cow.feed()
# petting zoo
# print(
#   f"{varmint_village.attraction_name} is where you'll find {varmint_village.description} like,")
# for animal in varmint_village.animals:
#    print(f'    *{str(animal)}')

# snake pit
# print(
#    f"{the_slither_inn.attraction_name} is where you'll find {the_slither_inn.description} like,")
# for animal in the_slither_inn.animals:
#    print(f'    *{str(animal)}')

# wetlands
# print(
#    f"{critter_cove.attraction_name} is where you'll find {critter_cove.description} like,")
# for animal in critter_cove.animals:
#    print(f'    *{str(animal)}')
