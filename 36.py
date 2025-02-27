#this inefficient asf but it works

sum = 0
def palindrome(number):
    if str(number)[::-1] == str(number):
        return True
    else:
        return False

def bin_string(number):
    if palindrome(bin(number)[2:]):
        return True
    else:
        return False

for number in range (1_000_000):
    if palindrome(number) and bin_string(number):
        sum += number

print(sum)