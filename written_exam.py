# def search_pair(items):
#     for i in range (0, ):
#         assert i + 1 < len(items)
#         if items[i] > items [i + 1]:
#             return i 
#     return None

# items = [1, 3, 4, 6, 4, 7, 6]
# print(search_pair(items))

# def mystery1(m, n):
#     i = 0 
#     while i < n:
#         i = i + 1
#     print(i ** m, end = " ")
#     return None

# mystery_val = mystery1(2, 3)
# if mystery_val == 9:
#     print ("here is nine: ", mystery_val)
# else:
#     print("here im: value", mystery_val)

def is_sorted(my_list):
    index = 0 
    while index < (len(my_list) - 1) :
        if my_list[index] > my_list[index + 1]:
            return False
        index = index + 1
    return True 

print(is_sorted([1, 2, 3]))