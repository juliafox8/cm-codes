from left_index import left_index
from right_index import right_index

def is_leaf(tree, i):
    l = left_index(i)
    r = right_index(i)
    if l < len(tree):
        return False
    if r < len(tree):
        return False
    else:
        return True

