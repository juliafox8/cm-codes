from triplets import triplets
from left_index import left_index
from right_index import right_index
from parent_index import parent_index
from leaf import is_leaf
from missing_child import missing_child
from bst_search import bst_search

def test_all():
    print("Testing all functions... \n")
    test_triplets()
    test_left_index()
    test_right_index()
    test_parent_index()
    test_is_leaf()
    test_missing_child()
    test_bst_search()
    print("All tests completed! \n")

def test_triplets():
    print("Testing triplets...")
    assert(triplets({}) == 0)
    assert(triplets({1: "a", 2: "a", 3:"a"}) == 1)
    assert(triplets({1: 'a', 2: 'b', 3: 'a'}) == 0)
    assert(triplets({1: 'a', 2: 'b', 3: 'c', 4: 'c', 5: 'b'}) == 0)
    letters = {1: "z", 2: "z", 3: "z", 4: "z"}
    assert(triplets(letters) == 0)
    letters[4] = "a"
    letters[5] = "a"
    letters[6] = "a"
    assert(triplets(letters) == 2)
    print("Finished testing triplets!")

def test_left_index():
    print("Testing left_index...")
    assert(left_index(0) == 1)
    assert(left_index(1) == 3)
    assert(left_index(2) == 5)
    assert(left_index(3) == 7)
    assert(left_index(4) == 9)
    assert(left_index(5) == 11)
    print("Finished testing left_index!")

def test_right_index():
    print("Testing right_index...")
    assert(right_index(0) == 2)
    assert(right_index(1) == 4)
    assert(right_index(2) == 6)
    assert(right_index(3) == 8)
    assert(right_index(4) == 10)
    assert(right_index(5) == 12)
    print("Finished testing right_index!")

def test_parent_index():
    print("Testing parent_index...")
    assert(parent_index(1) == 0)
    assert(parent_index(2) == 0)
    assert(parent_index(6) == 2)
    assert(parent_index(7) == 3)
    assert(parent_index(12) == 5)
    assert(parent_index(11) == 5)
    assert(parent_index(13) == 6)
    print("Finished testing parent_index!")

def test_is_leaf():
    print("Testing is_leaf...")
    tree = ["alpha"]
    assert(is_leaf(tree, 0) == True)
    a = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "kilo", "lima", "mike", "nova", "oscar"]
    assert(is_leaf(a, 0) == False)
    assert(is_leaf(a, 13) == True)
    assert(is_leaf(a, 10) == True)
    assert(is_leaf(a, 7) == True)
    assert(is_leaf(a, 6) == False)
    assert(is_leaf(a, 2) == False)
    print("Finished testing is_leaf!")


def test_missing_child():
    print("Testing missing_child...")
    a = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", None, "hotel", "india", "juliet", None, "lima", "mike", None, None]
    assert(missing_child(a, 0) == ["echo", "charlie"])
    assert(missing_child(a, 1) == ["echo"])
    assert(missing_child(a, 2) == ["charlie"])
    assert(missing_child(a, 5) == [])
    assert(missing_child(a, 9) == [])
    b = ["apple", "banana", "cherry", None, "date", None, None]
    assert(missing_child(b, 0) == ["banana"])
    c = ["aardvark", "bear", None, "cat", "dog", None, None, "eel", None, None, None, None, None, None, None]
    assert(missing_child(c, 0) == ["aardvark", "cat"])
    print("Finished testing missing_child!")

def test_bst_search():
    print("Testing bst_search...")
    bstree = [84,41,96,24,52,91,98,10,26,43,None,85,94,None,None]
    assert(bst_search(bstree, 52) == True)
    assert(bst_search(bstree, 51) == False)
    assert(bst_search(bstree, 97) == False)
    assert(bst_search(bstree, 84) == True)
    assert(bst_search(bstree, 98) == True)
    assert(bst_search(bstree, 94) == True)
    assert(bst_search(bstree, 41) == True)
    assert(bst_search(bstree, 42) == False)
    assert(bst_search(bstree, 122) == False)
    bstree = [1]
    assert(bst_search(bstree, 1) == True)
    assert(bst_search(bstree, 2) == False)
    print("Finished testing bst_search!")

test_all()