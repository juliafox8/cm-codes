# def contains_even(list):
#     for num in list:
#         if num % 2 == 0:
#             return True 
#     else: 
#         return False

# list = [1, 2, 3, 4, 5]
# print(contains_even(list))


def counts_even(list):
    count = 0 
    for num in list:
        if num % 2 == 0:
            count = count + 1
    return count 

list = [1, 3, 5]
print(counts_even(list))