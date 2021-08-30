def sum(n):
    sum = 0 
    for i in range(1, n +1):
        sum = sum + i
    return sum

print(sum(6))

def sum2(lst):
    sum = 0 
    for i in range (len(lst)):
        sum = sum + lst[i]
    return sum 

print(sum2([2,4, 6]))

def sum3(lst):
    sum = 0 
    for num in lst:
        sum = sum + num
    return sum 


def sum4(lst):
    sum = 0
    i = 0  
    while i < (len(lst)):
        sum = sum + lst[i]
        i = i + 1
    return sum 

