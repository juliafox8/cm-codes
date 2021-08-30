def sift(lst,k):    
    i = 0    
    while i < len(lst):        
        if lst[i] != None and lst[i] % k == 0:    
            lst[i] = None       
        i = i + 1    
    return lst 

def sift2(lst,k):  
    i = 0    
    while i < len(lst):         
        if lst[i] % k == 0:            
            lst.remove(lst[i])        
        else:            
            i = i + 1     
    return lst 
    
def sieve(n):    
    numlist = list(range(2, n+1))    
    primes = []    
    for i in range(0, len(numlist)):        
        if numlist[i] != None:            
            primes.append(numlist[i])            
            sift(numlist, numlist[i])            
    return primes
    
import math

def better_sieve(n):    
    numlist = list(range(2, n + 1))    
    primes = []    
    i = 0 # index 0 contains number 2    
    while ((i+2) <= math.sqrt(n)):   
             if numlist[i] != None:            
                 primes.append(numlist[i])            
                 sift(numlist, numlist[i])        
                 i = i + 1      
    return primes + numlist
    
print(better_sieve(50))