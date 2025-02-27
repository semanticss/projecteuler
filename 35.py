from math import sqrt
from itertools import permutations

#this so cooked you have to rotate them

primesbelowonemillion = []

circularprimes = 0

def isprime(n):
    if n > 2 and n % 2 == 0:
        return False
    for number in range(3, int(sqrt(n)) + 1):
        if n % number == 0:
            return False

    return True

for number in range(2, 1_000_001):
    if isprime(number):
        primesbelowonemillion.append(number)

def rotation(list, k): #rotates
    k = k % len(list)
    return int(list[-k:] + list[:-k])

def rotationcheck(num): #are all rotations prime?
    strnum = str(num)
    for i in range(len(strnum)):
        if not isprime(rotation(strnum, i)):
            return False
    
    return True

    
for number in primesbelowonemillion:
    if rotationcheck(number):
        circularprimes += 1


print(circularprimes)

