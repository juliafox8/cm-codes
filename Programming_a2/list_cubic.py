import math

def list_cubic(a, b, c, d):
    for x in range (0, 21):
        print(int((a * math.pow(x, 3)) + (b * (math.pow(x, 2))) + (c * x) + d))


