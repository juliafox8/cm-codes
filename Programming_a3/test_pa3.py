from largest import largest
from wages import pay, pay_table
from make_triangle import make_triangle
from vacation import vacation

def test_all():
    test_largest()
    # test_pay()
    # test_pay_table()
    # test_vacation()
    # test_make_triangle()
    # print("All tests completed")

def test_largest():
    assert largest(10,100,0)==100
    assert largest(300,100,500)==500
    assert largest(700,300,500)==700
    assert largest(-1,3,4)==4
    print ("Largest: Test complete")

def test_pay():
    assert pay(10,15) == 150
    assert pay(10,45) == 475.0
    assert pay(10,40) == 400
    assert pay(10,43) == 445.0
    assert pay(10,44) == 460.0
    print ("Test complete")

def test_pay_table():
    print ("PAY TABLE: You must check visually that your output looks like the following:")
    print ("Week  1  :  150")
    print ("Week  2  :  460.0")
    print ("Week  3  :  475.0")
    print ("Week  1  :  0")
    print ("Week  2  :  100")
    print ("Week  3  :  800")
    print ("Week  4  :  1250.0")
    print ("Here is your output:")
    pay_table(10,[15,44,45])
    pay_table(20,[0,5,40,55])
    print ("Test complete")

def test_vacation():
    places = ["San Francisco", "New York", "Orlando", "Philadelphia", "Chicago"]
    temps = [80,50,100,60,50]
    costs = [400,180,303,250,200]
    assert vacation(places,temps,costs,100)=="Orlando"
    assert vacation(places,temps,costs,59)=="Philadelphia"
    assert vacation(places,temps,costs,50)== "New York"
    assert vacation(places,temps,costs,130)== "Home"
    print ("VACATION: Test complete")

def test_make_triangle():
    print("MAKER TRIANGLE: You must check visually that your output looks like the following:")
    print ("*")
    print ("\n")
    print ("*")
    print ("* *")
    print ("* * *")
    print ("\n")
    print ("*")
    print ("* *")
    print ("*   *")
    print ("*     *")
    print ("* * * * *")
    print("Here is your output:")
    make_triangle(1)
    print ("\n")
    make_triangle(3)
    print ("\n")
    make_triangle(5)
    print ("\n")
    print ("Test complete")



test_all()