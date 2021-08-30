from select_strings import select_strings
from select_strings import select_strings_backward
from shuffle import shuffle
from cumulative_product import cumulative_product

def test_all():
    print("Testing all functions... \n")
    test_select_strings()
    test_select_strings_backward()
    test_shuffle()
    test_cumulative_product()
    print("All tests completed! \n")

def test_select_strings():
    print("  Testing select_strings()... ")
    assert(select_strings(['Polymorphism'], 'm') == ['Polymorphism'])
    assert(select_strings([], 'd') == [])
    names = ['Christine', 'Yi', 'Mark', 'Vivek', 'Jonathan', 'Maung', 'David', 'Patrick',\
    'Elliott', 'Ronnie', 'Felicia', 'Yuto', 'Oliver', 'Daniel', 'Julie', 'Andrew',\
    'Shailja', 'Kevin', 'Aline', 'Abhiram', 'Meena', 'Jenna', 'Rachel']
    names_save = names
    assert(select_strings(names, 'a') == ['Felicia', 'Shailja', 'Meena', 'Jenna'])
    assert(names == names_save)
    assert(select_strings(names, 'b') == [])
    assert(names == names_save)
    assert(select_strings(names, 'k') == ['Mark', 'Vivek', 'Patrick'])
    assert(select_strings(names, 'K') == [])
    assert(select_strings(names, 'm') == ['Abhiram'])
    assert(select_strings(['SeaTaC', '', 'Haneda', 'SFC', 'Heathrow'], 'C') == ['SeaTaC', 'SFC'])
    print("  Finished testing select_strings()! \n")

def test_select_strings_backward():
    print("  Testing select_strings_backward()... ")
    assert(select_strings_backward(['Polymorphism'], 'm') == ['Polymorphism'])
    assert(select_strings_backward([], 't') == [])
    names = ['Christine', 'Yi', 'Mark', 'Vivek', 'Jonathan', 'Maung', 'David', 'Patrick',\
    'Elliott', 'Ronnie', 'Felicia', 'Yuto', 'Oliver', 'Daniel', 'Julie', 'Andrew',\
    'Shailja', 'Kevin', 'Aline', 'Abhiram', 'Meena', 'Jenna', 'Rachel']
    names_save = names
    assert(select_strings_backward(names, 'a') == ['Jenna', 'Meena', 'Shailja', 'Felicia'])
    assert(names == names_save)
    assert(select_strings_backward(names, 'A') == [])
    assert(names == names_save)
    assert(select_strings_backward(names, 'l') == ['Rachel', 'Daniel'])
    assert(names == names_save)
    assert(select_strings_backward(names, 'w') == ['Andrew'])
    assert(select_strings_backward(names, 'n') == ['Kevin', 'Jonathan'])
    assert(select_strings_backward([], 'n') == [])
    assert(select_strings_backward(['Wilson', 'Lincoln', '', 'Washington', 'JohnsoN'], 'n') 
            == ['Washington', 'Lincoln', 'Wilson'])
    print("  Finished testing select_strings_backward()! \n")

def test_shuffle():
    print("  Testing shuffle()... ")
    assert(shuffle([], []) == [])
    ls = ['Hiro', 'Wasabi', 'Honey-Lemon']
    ls_save = ls
    assert(shuffle(ls, []) == [])
    assert(ls == ls_save)
    assert(shuffle([], ls) == [])
    assert(shuffle(['1'], ['a']) == ['1', 'a']) 
    list1 = ['1', '2', 'banana']
    list2 = [1, 5, 9001]
    assert(shuffle(list1, list2) == ['1', 1, '2', 5, 'banana', 9001])
    list1 = ['arch', 'dome']
    list2 = ['peanuts', 'gluten', 'dairy', 'citrus']
    list1_save = list1
    list2_save = list2
    assert(shuffle(list1, list2) == ['arch', 'peanuts', 'dome', 'gluten'])
    assert(list1 == list1_save)
    assert(list2 == list2_save)
    list1 = ['a', 'b', 'c', 'd', 'f']
    list2 = [1, 2, 3, 4]
    assert(shuffle(list1, list2) == ['a', 1, 'b', 2, 'c', 3, 'd', 4])
    print("  Finished testing shuffle()! \n")


def test_cumulative_product():
    print("  Testing cumulative_product()... ")
    assert(cumulative_product([]) == [])
    assert(cumulative_product([3]) == [3])
    vals = [5, 4, 3, 2, 1]
    vals_save = vals
    assert(cumulative_product(vals) == [5, 20, 60, 120, 120])
    assert(vals == vals_save)
    assert(cumulative_product(vals[1:3]) == [4, 12])
    assert(cumulative_product(vals[1:4]) == [4, 12, 24])
    assert(cumulative_product(vals[2:5]) == [3, 6, 6])
    vals = list(range(-9, 0))
    assert(cumulative_product(vals) == [-9, 72, -504, 3024, -15120, 60480, -181440, 362880, -362880])
    vals = [-1, 1, -2, 2, -3, 3, 0, 4]
    assert(cumulative_product(vals) == [-1, -1, 2, 4, -12, -36, 0, 0])
    vals = [0] *10
    assert(cumulative_product(vals) == vals)
    print('  Finished testing cumulative_product()! \n')

test_all()