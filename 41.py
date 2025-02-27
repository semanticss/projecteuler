from math import sqrt
import tqdm

def isprime(n):
    if n > 2 and n % 2 == 0:
        return False
    for number in range(3, int(sqrt(n)) + 1):
        if n % number == 0:
            return False
        
    return True

primenumbers = []
pandigitals = []

for potentialprime in tqdm.tqdm(range(1, 999999999)):
    if isprime(potentialprime):
        primenumbers.append(potentialprime)

for prime in primenumbers:
    primeset = list(set(str(prime)))
    if len(primeset) == len(prime):
        pandigitals.append(prime)


    # make a set

print(max(pandigitals))