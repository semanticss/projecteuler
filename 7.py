from math import sqrt

def isprime(n):
    if n % 2 == 0 and n != 2:
        return False
    for j in range(3, int(sqrt(n)) + 1):
        if n % j == 0:
            return False
    
    return True

primes = 0
n = 1
while primes != 10002:
    if isprime(n):
        print(n)
        primes += 1
    n += 1

print(n - 1)

