def sift(lst,k):    
    i = 0    
    while i < len(lst):        
        if lst[i] != None and lst[i] % k == 0:    
            lst[i] = None       
        i = i + 1    
    return lst 

def sift_wrong(lst,k):
    # eliminates multiples of k 
    for i in range(0,len(lst)):
        if lst[i] % k == 0:
            lst.remove(lst[i])
    return lst

print(sift([1, 2, 3], 2))
print(sift_wrong([1, 2, 3], 2))

def sieve(n):    
    numlist = list(range(2, n+1))    
    primes = []    
    for i in range(0, len(numlist)):        
        if numlist[i] != None:            
            primes.append(numlist[i])            
            sift(numlist, numlist[i])            
    return primes.pop()

print(sieve(20))