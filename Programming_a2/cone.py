import math

def cone_volume(radius, height):
  return(1/3) * math.pi * math.pow(radius, 2) * height 

print("volume for cone one: ", cone_volume(6, 12))
print("volume for cone 2", cone_volume(6,8))

def print_object_volume():
  print ("The total volume of the two cones is", cone_volume(6,12) + cone_volume(6,8))
