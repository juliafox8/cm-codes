def num_even(numbers):
    count = 0 
    for i in range (len(numbers)):
        if numbers[i] % 2 == 0:
            count += 1 #increment by 1 (facy shmacy adding count = count + 1)
    return count 


