def count_a_words(lst):
    if lst == []:
        return 0
    if isinstance(lst[0], str) == True:
        if (lst[0] != "") and (lst[0][0] == 'a'):
            return 1 + count_a_words(lst[1:])

    return count_a_words(lst[1:])

def test_count_a_words(): 
    print("Testing count_a_words()...", end="")
    lst0 = [1, "apple", "foo", "anaconda", True, []]
    assert(count_a_words(lst0) == 2)
    lst1 = ["alligator"]
    assert(count_a_words(lst1) == 1)
    lst2 = [True] 
    assert(count_a_words(lst2) == 0)
    lst3 = ["alligator", "anaconda"]
    assert(count_a_words(lst3) == 2)
    lst4 = ["foo", "bar", "hello", "world"] 
    assert(count_a_words(lst4) == 0)
    lst5 = []
    assert(count_a_words(lst5) == 0)
    lst6 = ["Alligator", "alligator"]
    assert(count_a_words(lst6) == 1)
    print("Passed!")

test_count_a_words()
  