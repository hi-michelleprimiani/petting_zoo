from swimming import Bass, Goldfish, Catfish, Koi, Trout
from slithering import Copperhead, RatSnake, Python, Anaconda, Cobra
from walking import Donkey, Llama, Goat, Chicken, Cow
from datetime import date


# walking
donkey = Donkey("Donkey Kong", "Domestic Donkey", "midday")
llama = Llama("Larry", "Llama glama", "afternoon")
goat = Goat("Billy", "Domestic Goat", "afternoon")
chicken = Chicken("Henrietta", "Hen", "midday")
cow = Cow("MooMoo", "Holstein Cow", "morning")
# slithering
copperhead = Copperhead("Slither", "American Copperhead")
ratsnake = RatSnake("Ratty", "Rat Snake")
python = Python("Monty", "Ball Python")
anaconda = Anaconda("Anna", "Green Anaconda")
cobra = Cobra("King", "King Cobra")
# swimming
bass = Bass("Bassy", "Largemouth Bass")
goldfish = Goldfish("Goldie", "Common Goldfish")
catfish = Catfish("Whiskers", "Channel Catfish")
koi = Koi("Koiboi", "Japanese Koi")
trout = Trout("Trouty", "Rainbow Trout")


print(f'{chicken.name} the {chicken.species} is available to pet during the {chicken.shift} shift.')
