from cone import cone_volume, print_object_volume
from quadratic import quadratic
from list_cubic import list_cubic
# from digit import digit, reverse_num, pal_num


import math

def test_all():
    test_cone_volume()
    test_print_object_volume()
    test_quadratic()
    test_list_cubic()
    test_digit()
    # test_reverse_num()
    # test_pal_num()
    print("All tests completed")

def test_cone_volume():
    assert round(cone_volume(3, 5), 5) == round(1/3 * math.pi * 9 * 5, 5)
    assert round(cone_volume(4, 10), 5) == round(1/3 * math.pi * 16 * 10, 5)
    assert round(cone_volume(4, 15), 5) == round(1/3 * math.pi * 16 * 15, 5)
    assert round(cone_volume(1, 1), 5) == round(1/3 * math.pi * 1 * 1, 5)
    print("Test complete")
    
def test_print_object_volume():
    print("You must check visually that your output looks like the following (it may be slightly different in the final digits):")
    print("The total volume of the two cones is " + str(1/3*math.pi*6*6*8 + 1/3*math.pi*6*6*12))
    print("Here is your output:")
    print_object_volume()
    print("Test complete")

def test_quadratic():
    print("You must check visually that your output looks like the following:")
    print("[x1: 1.0, x2: -4.0]")
    print("[x1: -2.0, x2: -2.0]")
    print("[x1: -0.5, x2: -0.5]")
    print("Here is your output:")
    quadratic(1, 3, -4)
    quadratic(1, 4, 4)
    quadratic(4, 4, 1)
    print("Test complete")

def test_list_cubic():
    print("You must check visually that your output looks like the following:")
    print("2\n6\n36\n110\n246\n462\n776\n1206\n1770\n2486\n3372\n4446\n5726\n7230\n8976\n10982\n13266\n15846\n18740\n21966\n25542")
    print("Here is your output:")
    list_cubic(3, 4, -3, 2)
    print("Test complete")

def test_digit():
    assert digit(123, 3) == 1
    assert digit(293586, 4) == 3
    assert digit(123456, 3) == 4
    print("Test complete")

def test_reverse_num():
    assert reverse_num(12345, 5) == 54321
    assert reverse_num(596920 ,6) == 29695
    assert reverse_num(2020, 4) == 202
    print("Test complete")

def test_pal_num():
    assert pal_num(1234, 4) == False
    assert pal_num(1234321, 7) == True
    assert pal_num(1234 + reverse_num(1234, 4), 4) == True
    print("Test complete")


test_all()
