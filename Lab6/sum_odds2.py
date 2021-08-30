def sum_odds2(x):
    #base case
    if x == []:
        return 0

    #recursive
    if isinstance(x[0], int) == True:
        #isinstance checks if the number is an integer
        if (x[0] % 2 == 0):
            return sum_odds2(x[1:])
        elif (x[0] % 2 == 1):
            return x[0] + sum_odds2(x[1:])
    
    #isinstance checks if the number is a list
    if isinstance(x[0], list) == True:
        return sum_odds2(x[0]) + sum_odds2(x[1:])


def test_sum_odds2(): 
    print("Testing sum_odds2()...", end="")
    x0 = [[1, 2], 3]
    assert(sum_odds2(x0) == 4)
    x1 = [1, [2, 3]]
    assert(sum_odds2(x1) == 4)
    x2 = []
    assert(sum_odds2(x2) == 0)
    x3 = [2, [3], 1, [4]]
    assert(sum_odds2(x3) == 4)
    x4 = [2, [4, 6], 8]
    assert(sum_odds2(x4) == 0)
    x5 = [1, [2, [3, 4], 5], 6]
    assert(sum_odds2(x5) == 9)
    x6 = [[[], []], [[[]]]]
    assert(sum_odds2(x6) == 0)
    print("Passed!")

test_sum_odds2()