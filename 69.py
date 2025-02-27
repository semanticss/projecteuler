# euler totient is all numbers relatively prime to n less than n
# can be given by n times the product of (1-1/p) where p is every prime number that divides n

from math import sqrt, ceil
from tqdm import tqdm




def isprime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


primes = []

for number in range(2, 10000):
    if isprime(number):
        primes.append(number)

def phi_n(n):
    evenprimedivisors = []
    phin = 1
    for number in primes:
        if n % number == 0:
            evenprimedivisors.append(number)

    
    for p in evenprimedivisors:
        # print(1-(1/p))
        phin *= (1 - (1 / p))
        # print(phin)

    phin *= n
    return int(phin)

max = 0
corresponding = 0

for number in tqdm(range(2, 1_000_000)):
    if number / phi_n(number) > max:
        max = number / phi_n(number)
        corresponding = number


print(corresponding)



