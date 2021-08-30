def first_even(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            return i
    return None

