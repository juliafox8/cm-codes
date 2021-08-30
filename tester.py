# def search_pair(items):
#     for i in range((len(items)) - 1):
#         assert i + 1 < len(items)
#         if items[i] > items[ i + 1]:
#             return i 
#     return None

# items = [1, 3, 4, 6, 4, 7, 7]
# print(search_pair(items))


# num_A = ([1, 2, 3, 4])
# num_B = ([5, 6, 7, 8])
# num_B.insert(0, num_A.pop(1) )
# print(num_B)
# print(num_A)


def mystery1(m, n):  
    i=0  
    while i < n:  
        i=i+1  
    print(i ** m, end=", ")

mystery_val = mystery1(2, 3) 
if mystery_val == 9: 
    print("Here is Nine: ", mystery_val) 
else: 
    print("Here I’m: value", mystery_val) 


