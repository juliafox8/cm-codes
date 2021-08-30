def digitSum(number):
    num_string = str(number) 
    if len(num_string) == 1:
        return number
    else:
        return int(num_string[0]) + int(digitSum(num_string[1:]))


