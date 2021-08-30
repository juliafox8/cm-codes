def bsearch(items, key):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == key:
            return mid
        if key > items[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

items = range(0, 16)
print(bsearch(items, 19))