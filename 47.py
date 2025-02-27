from math import sqrt

def prime(n): # checks if prime fr
    for a in range(2, int(sqrt(n)) + 1):
        if n % a == 0:
            return False
        
    return True

primes = []

for number in range(1000, 10000):
    if prime(number):
        primes.append(number)

def factors(n):
    list = []
    for number in range(2,int(sqrt(n))): #only have to check until sqrt n
        if n % number == 0:
            if prime(number):
                print(number)
                list.append(number)
            if prime(n / number):
                list.append(number)

    return list

print(factors(644))