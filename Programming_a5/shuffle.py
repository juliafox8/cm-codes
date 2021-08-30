def shuffle(list1, list2):
    if list1 == [] or list2 == []:
        return []
    
    return [list1[0], list2[0]] + shuffle(list1[1:], list2[1:])

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(shuffle(list1, list2))