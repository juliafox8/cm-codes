def triplets(d):
    unique= {}
    tripletsnum = 0
    for value in d.values():
        unique[value] = unique.get(value, 0) + 1
    for count in unique.values():
        if count == 3:
            tripletsnum = tripletsnum + 1
    return tripletsnum
        


