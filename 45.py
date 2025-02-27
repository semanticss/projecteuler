from tqdm import tqdm
from math import sqrt
# i cannot believe this works

def quadratic_solver(a,b,c):
    solution1 = 0
    solution2 = 0
    d = (b**2) - (4*a*c)

    if d < 0:
        return "DNE"
    if d == 0:
        return ((b * -1) + sqrt((b**2) - (4*a*c))) / (2*a)
    else:
        return ((b * -1) + sqrt((b**2) - (4*a*c))) / (2*a)
    
trianglenums = [int((n * (n + 1) * 0.5)) for n in range(100000)]

for number in trianglenums:
    x = 0
    pentc = number * -2
    hexc = number * -1
    if (quadratic_solver(3, -1, pentc) * 10) % 10 == 0:
        x += 1
    if ((quadratic_solver(2, -1, hexc)) * 10) % 10 == 0:
        x += 1

    if x == 2:
        print(number)