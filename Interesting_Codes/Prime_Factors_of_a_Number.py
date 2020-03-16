import math

def prime_factor(n):
    ls = []
    while n % 2 == 0:
        ls.append(2)
        n /= 2
        
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            ls.append(i)
            n /= i
            
    if n > 2:
        ls.append(n)
        
    return ls
    
    
n = int(input())
print(prime_factor(n))
