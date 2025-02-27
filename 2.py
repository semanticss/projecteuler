import numpy as np

sum = 0

phi = (1 + np.sqrt(5))/2

tao = -1/phi

def binets(n):
    binet = np.floor((pow(phi, n) - pow(tao, n))/(np.sqrt(5)))
    return binet

for n in range(1000):
    if binets(n) < 4000000 and binets(n) % 2 == 0:
        sum += binets(n)

print(sum)