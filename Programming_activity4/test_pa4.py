from first_even import first_even
from num_even import num_even
from geo_mean import geo_mean
from second_largest import second_largest
from counting_sort import counting_sort

def test_first_even():
    print("Testing first_even()...\n")
    assert(first_even(list(range(5))) == 0)
    assert(first_even([1, 3, 1, 5, 7, 9, 11, 13, 0]) == 8)
    assert(first_even([1, 3, 1, 5, 7, 9, 11, 13, 0, 11, 4]) == 8)
    assert(first_even([-5, 5, -1, 1, -4, 4]) == 4)
    assert(first_even([0]) == 0)
    assert(first_even([4, 4]) == 0)
    assert(first_even([]) == None)
    assert(first_even([1, 1, 1, 1]) == None)
    print("Finished testing first_even()!\n")

def test_num_even():
    print("Testing num_even()...\n")
    assert(num_even([]) == 0)
    assert(num_even(list(range(10))) == 5)
    assert(num_even([-1]*10) == 0)
    assert(num_even([0]*10) == 10)
    assert(num_even([-6, -4, -2, 0, 2, 4, 6, 99]) == 7)
    assert(num_even([99, -6, -4, -2, 0, 2, 4, 6]) == 7)
    print("Finished testing num_even()!\n")

def test_geo_mean():
    print("Testing geo_mean()...\n")
    epsilon = 0.001
    assert((geo_mean([9]) - 9.0) < epsilon)
    assert((geo_mean([2, 8]) - 4.0) < epsilon)
    assert((geo_mean([.5, 32]) - 4.0) < epsilon)
    assert((geo_mean([1/32, 1, 4]) - 0.5) < epsilon)
    assert((geo_mean([2, 8]) - 4.0) < epsilon)
    print("Finished testing geo_mean()!\n")

def test_second_largest():
    print("Testing second_largest()...\n")
    assert(second_largest([3, -2, 10, -1, 5]) == 5)
    assert(second_largest([-2, 1, 1, -3, 5]) == 1)
    assert(second_largest([1, 1, 3, 3]) == 3)
    assert(second_largest(["alpha", "gamma", "beta", "delta"]) == "delta")
    assert(second_largest([3.1, 3.1]) == 3.1)
    assert(second_largest([False, True, False, False]) == False)
    assert(second_largest([True, False, True]) == True)
    print("Finished testing second_largest()!\n")

def test_counting_sort():
    print("Testing counting_sort()...\n")
    assert counting_sort([44, 22, 44, 11, 33, 33, 22, 44, 33, 44], 44) == [11, 22, 22, 33, 33, 33, 44, 44, 44, 44]
    assert counting_sort([], 0) == []
    assert counting_sort([5], 5) == [5]
    assert counting_sort([5, 5, 5, 5], 5) == [5, 5, 5, 5]
    assert counting_sort(list(range(10)), 9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert counting_sort(list(range(9, -1, -1)), 9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Finished testing counting_sort()!\n")
    

def test_all():
    print("Testing all functions...\n")
    test_first_even()
    test_num_even()
    test_geo_mean()
    test_second_largest()
    test_counting_sort()
    print("All tests completed\n")

test_all()
