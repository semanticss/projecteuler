import tqdm
from math import sqrt
x = True
n = 0
divisors = 0
def trinumgen(n): #make triangle number
    return ((n*(n+1))//2)

while x:
    divisors = 0
    numbr = trinumgen(n) #nth triangle number

    for potentialdivisor in range(1, int(sqrt(numbr)) + 1):
        if numbr % potentialdivisor == 0:
            divisors += 2 if potentialdivisor * potentialdivisor != numbr else 1

    n += 1
    if divisors > 500:
        x = False
        print(numbr)
