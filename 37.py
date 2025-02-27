import math

def isprime(n):
    if n % 2 == 0 and n != 2:
        return False
    for j in range(1, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    
    return True


x = 0
while x < 12:
