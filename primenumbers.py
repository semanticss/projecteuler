from math import sqrt
import tqdm as tqdm

x = True
n = 2
count = 1
sum = 0
def isprime(n):
    if n > 2 and n % 2 == 0:
        return False
    for number in range(3, int(sqrt(n)) + 1):
        if n % number == 0:
            return False

    return True


while x:
    if isprime(n):
        count += 1
    n += 1
    if count == 10001:
        print(n)
        x = False

# for number in tqdm.tqdm(range(2, 2_000_001)):
#     if isprime(number):
#         # print(number)
#         sum += number
    
# print(sum)

        

