from tqdm import tqdm
from math import sqrt

def quadratic(a, b, n):
    return (n**2) + (a * n) + b

longestconsec = 0
bestab = 0
def isprime(n):
    if n < 0:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for number in range(3, int(sqrt(n)) + 1):
        if n % number == 0:
            return False
    return True

bprimes = [n for n in range(1000) if isprime(n)]

for a in tqdm(range(-1000, 1000)):
    for b in bprimes:
        primes = 0
        n = 0
        while isprime(quadratic(a, b, n)):
            primes += 1
            n += 1
        if primes > longestconsec:
            longestconsec = primes
            bestab = a * b


print(bestab)



