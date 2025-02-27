from math import sqrt
import tqdm

def checkifpermutation(n):
    
    stringnumber = sorted(str(n))
    return stringnumber

def isprime(n):
    if n > 2 and n % 2 == 0:
        return False
    for number in range(3, int(sqrt(n)) + 1):
        if n % number == 0:
            return False

    return True

primes = []

for number in range(1000, 10000):
    if isprime(number):
        primes.append(number)

for number in primes:
    if isprime(number + 3330) and isprime(number + 6660):
        numbers = [number, number + 3330, number + 6660]

    if checkifpermutation(numbers[0]) == checkifpermutation(numbers[1]) == checkifpermutation(numbers[2]):
        print(numbers)


