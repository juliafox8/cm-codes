def counting_sort(keys, max_key):
    counts = [0] * (max_key + 1) 
    for k in keys:
        counts[k] += 1 
    result = []
    for k in range(0, max_key + 1):
        count = counts[k]
        for n in range(count):
            result.append(k)
    return result 

from time import time 

def time_sort(n):
    stuff = list(range(n))
    start = time()
    counting_sort(stuff, n)
    return time() - start 

# print(time_sort(10000000))


