def findmin(lst):
    min_num = lst[0]
    i = 1
    while i < len(lst): 
        if lst[i] < min_num:
            min_num = lst[i]
        i = i + 1
    return min_num.index

lst = [7, 4, 6, -1, 4, 19]
print(findmin(lst))