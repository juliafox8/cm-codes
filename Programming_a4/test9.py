def findmin(lst):
    min_num = lst[0]
    i = 1
    while i < len(lst): 
        if lst[i] < min_num:
            min_num = lst[i]
        i = i + 1
    return lst.index(min_num)

print(findmin([1, 2, 3]))