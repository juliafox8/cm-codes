from random import randint

def roll():
    return randint(1,20,5)

def game():
    critHitTotal = 0
    critMissTotal = 0
    for i in range(20):
        value = roll()
        if value == 20:
            critHitTotal += 1
        elif value  == 1:
            critMissTotal += 1
    return (critHitTotal, critMissTotal)

print(roll())
print(game())