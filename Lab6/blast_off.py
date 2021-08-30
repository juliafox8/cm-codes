def blast_off(n):
    if (n == 0):
        print("blast_off")
        return None 
    else: 
        print(n)
        return (blast_off(n-1))


