from random import randint

def roll_20_sided(number):
    value = 0 
    for i in range(number): 
        roll = randint(1, 20)
        value = value + roll
    return value 
