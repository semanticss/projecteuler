import tqdm

biggestchain = 0
number = 0

def collatz(n):
    if n % 2 == 0:
        n = n // 2
        return n
    if n % 2 == 1:
        n = (3*n) + 1
        return n

for j in tqdm.tqdm(range(1, 1000000)):
    chain = 1
    n = j
    while n != 1:
        n = collatz(n)
        chain += 1
    
    if chain > biggestchain:
        biggestchain = chain
        number = j

print(number)

