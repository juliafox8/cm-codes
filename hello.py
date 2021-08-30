import random 
from random import randint

def loaded_coin():
    unfair = randint(1, 4)
    if unfair >= 2:
        return "H"
    else:
        return "T"

print(loaded_coin())
