import sys


MAPINT = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
          'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 

def findnumbers(linestr):
    numbers = []
    for i in range(len(linestr)):
        for add in range(6):  # maximum number of characters in number strings = 5
            char = linestr[i:i+add]
            if char in MAPINT:
                numbers.append(int(MAPINT.index(char) % 9 + 1))
    return numbers


inputfile = open(str(sys.argv[1]), 'r')
sum = 0

for line in inputfile:
    numbers = findnumbers(line)

    if len(numbers) > 0:
         sum += 10 * numbers[0] + numbers[-1]

print(sum)
