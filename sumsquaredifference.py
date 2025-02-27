import tqdm as tqdm

sum = 0
squaresum = 0
for i in range(1, 101):
    sum += i

print(sum)

for i in range(1, 101):
    squaresum += i ** 2

bigsum = sum ** 2

print(bigsum)

difference = bigsum - squaresum

print(difference)