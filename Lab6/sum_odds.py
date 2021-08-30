def sum_odds(x):
    #base case
    if x == []:
        return 0 
    #recursive
    elif (x[0] % 2 == 0):
        return sum_odds(x[1:])
        #excludes the first index at the begining of the list
    elif (x[0] % 2 != 0):
        return x[0] + sum_odds(x[1:])

def test_sum_odds(): 
    print("Testing sum_odds()...", end="")
    x0 = []
    assert(sum_odds(x0) == 0)
    x1 = [5]
    assert(sum_odds(x1) == 5)
    x2 = [1, 2, 3]
    assert(sum_odds(x2) == 4)
    x3 = [2, 4, 6, 8]
    assert(sum_odds(x3) == 0)
    x4 = [1, 2, 3, 4, 5, 6]
    assert(sum_odds(x4) == 9)
    print("Passed!")

test_sum_odds()
