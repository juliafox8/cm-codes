def second_largest(values):
    max_start = None
    max_yay = None 
    for num in range (len(values)):
        if max_start == None or values[num] > max_start:
            max_yay = max_start
            max_start = values[num]
        elif max_yay == None or values[num] > max_yay:
            max_yay = values[num]
 #       if values[num] 

    return max_yay

print(second_largest([10, 1]))