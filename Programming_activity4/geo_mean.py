import math 

def geo_mean(numbers):
    product = 1 
    for n in numbers:
        product = product * n 
    return math.pow(product, (1/len(numbers))) 
