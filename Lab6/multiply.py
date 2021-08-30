def multiply(a, b):
    #base case
    if (b == 1):
        return a
    
    if a == 0 or b == 0:
        return 0 
    
    #recursion case b > 1
    else:
        return a + multiply(a, b-1)

def test_multiply(): 
    print("Testing multiply()...", end="")
    assert(multiply(0, 3) == 0)
    assert(multiply(0, 0) == 0)
    assert(multiply(1, 2) == 2)
    assert(multiply(4, 6) == 24)
    assert(multiply(11, 11) == 121)
    print("Passed!")

test_multiply()
  