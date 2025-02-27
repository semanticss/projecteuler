# find sum of proper divisors
# double for loop through a and b less than 10k
# sum them fr
from math import sqrt

def sumofproperdivisors(number):
    sum = 0
    properdivisors = []
    for n in range(1, int(sqrt(number)) + 1):
        print(n)
        print(number % n == 0)
        if number % n == 0 and number / n != number:
            properdivisors.append(n)
            properdivisors.append(number / n)
            sum = sum + n + (number / n)
    return sum + 1

for a in range(10_000):
    for b in range(10_000):
        if a != b and 

        # how do you remove this bro