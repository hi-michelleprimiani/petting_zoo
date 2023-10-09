from animals import Bass, Goldfish, Catfish, Koi, Trout, Mallard, Goose
from animals import Copperhead, RatSnake, Python, Anaconda, Cobra
from animals import Donkey, Llama, Goat, Chicken, Cow
from attractions import PettingZoo, SnakePit, Wetlands
from datetime import date
from animals import Animal


larry = Llama("Larry", "Llama glama", "afternoon", "Llama Chow", 1234)
donkey_kong = Donkey("Donkey Kong", "Domestic Donkey", "midday", "Hay", 2345)
billy = Goat("Billy", "Domestic Goat", "afternoon", "Goat Feed", 3456)
henrietta = Chicken("Henrietta", "Hen", "midday", "Chicken Feed", 4567)
moo_moo = Cow("MooMoo", "Holstein Cow", "morning", "Grass", 5678, 4)
slither = Copperhead("Slither", "American Copperhead", "Mice", 6789)
ratty = RatSnake("Ratty", "Rat Snake", "Rats", 7890)
monty = Python("Monty", "Ball Python", "Small Mammals", 8901)
anna = Anaconda("Anna", "Green Anaconda", "Large Rodents", 9012)
king = Cobra("King", "King Cobra", "Small Mammals", 2222)
bassy = Bass("Bassy", "Largemouth Bass", "Fish Food", 1357)
goldie = Goldfish("Goldie", "Common Goldfish", "Goldfish Flakes", 2468)
whiskers = Catfish("Whiskers", "Channel Catfish", "Catfish Pellets", 3579)
koiboi = Koi("Koiboi", "Japanese Koi", "Koi Food", 4680)
trouty = Trout("Trouty", "Rainbow Trout", "Fish Pellets", 5791)
ducky = Mallard("Ducky", "Duck", "Poop", 4509, 2)
goosey = Goose("Goosey", "Goose", "Poop", 5555, 2)
lucy = Goose("Lucy", "Goose", "Grass", 4507, 2)
lucy.swim_speed = "5 mph"
ducky.run()
goosey.swim()

print(lucy)
lucy.num_legs()
moo_moo.num_legs()
print(lucy.swim_speed)

# attractions
varmint_village = PettingZoo(
    "Varmint Village", "cute and fuzzy critters to cuddle")
the_slither_inn = SnakePit(
    "The Slither Inn", "slithering reptiles, not for the faint of heart")
critter_cove = Wetlands(
    "Critter Cove", "aquatic life, both cute and interesting")


varmint_village.add_animal(larry)
varmint_village.add_animal(donkey_kong)
varmint_village.add_animal(billy)
varmint_village.add_animal(henrietta)
varmint_village.add_animal(moo_moo)

the_slither_inn.add_animal(slither)
the_slither_inn.add_animal(ratty)
the_slither_inn.add_animal(monty)
the_slither_inn.add_animal(anna)
the_slither_inn.add_animal(king)

critter_cove.add_animal(bassy)
critter_cove.add_animal(goldie)
critter_cove.add_animal(whiskers)
critter_cove.add_animal(koiboi)
critter_cove.add_animal(trouty)
critter_cove.add_animal(goosey)
critter_cove.add_animal(lucy)

# petting zoo
# print(
#    f"{varmint_village.attraction_name} is where you'll find {varmint_village.description} like,")
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
