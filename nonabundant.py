import tqdm as tqdm
from math import sqrt


# all integers more than 28123 can be written as two abundant numbers
# the BIGGEST number that CANNOT be wrriten as number abundant numbers is LESS than 28123

abundantnumbers = []
sum = 0
def checkabundant(n):
    factors = []
    sum = 1
    for potentialfactor in range(2 ,int(sqrt(n)) + 1):
        if n % potentialfactor == 0:
            factors.append(potentialfactor)
            factors.append(n / potentialfactor)

    # print(factors)
    
    for factor in factors:
        sum += factor

    if sum > n:
        return True
    else:
        return False
    
for potentialabundant in range(28123):
    if checkabundant(potentialabundant):
        abundantnumbers.append(potentialabundant)

for test in tqdm.tqdm(range(28123)):
    for firstabundant in range(len(abundantnumbers)):
        for secondabundant in range(len(abundantnumbers)):
            if test != firstabundant + secondabundant:
                sum += test

print(abundantnumbers)



