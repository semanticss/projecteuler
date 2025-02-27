start = 0
tracker = 0

for counter in range(999):
    start += 1
    if start % 3 == 0 or start % 5 == 0 and start < 1000:
        print(start)
        tracker += start
    

print(tracker)