all_values = []

# Open the text file for reading
with open('0042_words.txt', 'r') as file:
    for line in file:
        # Remove leading/trailing whitespace and newline characters
        line = line.strip()
        # Split the line into individual values using a comma as the delimiter
        values = line.split(',')
        all_values.extend(values)
        print(values)

    

trianglenums = []

for n in range(1000):
    trianglenums.append(0.5 * n * (n+1))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letsgo = 0
# index the thing and then add one

def findnumber(word):
    numval = 0
    for letter in word:
        print(letter)
        print(alphabet.index("A"))
        numval += alphabet.index(letter) + 1

        
    for trianglenumber in trianglenums:
        if trianglenumber == numval:
            return True
    
    return False


for word in all_values:
    word = word[1:]
    word = word[:len(word) - 1]
    print("word below this")
    print(word)
    if findnumber(word):
        letsgo += 1

print(letsgo)

#idk how to clean the data earlier on