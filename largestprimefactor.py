import numpy as np
from math import sqrt
from tqdm import tqdm

#code stolen from online fr

def prime(n): # checks if prime fr
    for a in range(2, int(sqrt(n))):
        if n % a == 0:
            return False
        
    return True

def factors(n):
    list = []
    for number in range(2,int(sqrt(n))): #only have to check until sqrt n
        if n % number == 0:
            if prime(number):
                list.append(number)
            if prime(n / number):
                list.append(number)
    print(max(list))

factors(600851475143)
