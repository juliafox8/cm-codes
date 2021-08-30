from right_index import right_index
from left_index import left_index


def bst_search(tree, key):
    curr_index = 0 
    while curr_index < len(tree) and tree[curr_index] != None:
        curr_value = tree[curr_index]
        if curr_value == key:
            return True
        if key < curr_value:
            curr_index = left_index(curr_index)
        if key > curr_value:
            curr_index = right_index(curr_index)
    return False

