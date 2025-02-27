import math

x = 234839345343 #any number
#basically the log base ten rounded up gives the highest power of ten needed to find the digits or wtv

y = math.ceil(math.log(x, 10))

print(y)