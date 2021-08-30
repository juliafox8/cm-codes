from left_index import left_index
from right_index import right_index

def is_leaf(tree, i):
    l = left_index(i)
    r = right_index(i)
    if l < len(tree) and tree[l] != None:
        return False
    if r < len(tree) and tree[r] != None:
        return False
    else:
        return True


def missing_child(tree, i):
    if is_leaf(tree, i):# base case
        return []
    l = left_index(i)
    r = right_index(i)
    has_left_kid = l < len(tree) and tree[l] != None
    has_right_kid = r < len(tree) and tree[r] != None
    if has_left_kid and has_right_kid: #recursive  check if has missing child
        return missing_child(tree, l) + missing_child(tree, r)
    # oh no has missing child add below to list 
    return [tree[i]] + (missing_child(tree, l) + missing_child(tree, r))

