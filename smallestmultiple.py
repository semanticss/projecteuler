import math

def leastcommon(x,y):
    z = abs(x*y) //  math.gcd(x,y)
    return z

number = 1

for i in range (1,20):
    number = leastcommon(number, i)

print(number)