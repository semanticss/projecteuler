modulo = 10**10

total = sum(pow(n,n, modulo) for n in range(1, 1001)) % modulo

print(total)