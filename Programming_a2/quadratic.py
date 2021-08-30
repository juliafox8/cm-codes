import math

def quadratic(a, b, c):
    x1 = (-b + ((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - ((b ** 2) - (4 * a * c))) / (2 * a)
    print ("[x1: ", x1, ", x2: ", x2,"]", sep = "")

