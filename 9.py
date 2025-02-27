import tqdm as tqdm

#this is so inefficient

list = []

for a in tqdm.tqdm(range(1, 1000)):
    for b in range(1,1000):
        for c in range(1,1000):
            if (c**2) == (a**2) + (b**2):
                # list.append("|")
                # list.append(a)
                # list.append(b)
                # list.append(c)
                # list.append("|")
                if a + b + c == 1000:
                    print(a*b*c)
print(list)