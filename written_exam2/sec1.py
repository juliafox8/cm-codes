def bad(n):        
    if n <= 1:            
        return True        
    elif n % 2 == 0:            
        return bad(n/2)        
    else:            
        return bad(n/1) 

print(bad(6))