from math import factorial
import tqdm

curiousnumbers = []

for number in tqdm.tqdm(range(3, 9999999)):
    factorialsum = 0
    strnum = list(str(number))

    

    for digit in strnum:
        factorialsum  += factorial(int(digit))

    
    if factorialsum == number:
        curiousnumbers.append(number)


print(curiousnumbers)

