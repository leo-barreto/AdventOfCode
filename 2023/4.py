import sys


inputfile = open(str(sys.argv[1]), 'r')
sum1 = 0
sum2 = 0

fullentry = [i.strip() for i in inputfile]
cardcount = [1 for i in range(len(fullentry))]

for game, line in enumerate(fullentry, start=1):
    numbers = line.split(': ')[1].split(' | ')
    winnumbers = numbers[0].split()
    cardnumbers = numbers[1].split()
    matches = sum([i in winnumbers for i in cardnumbers])
    if matches > 0:
        sum1 += 2 ** (matches - 1)

    for i in range(matches):
        cardcount[game + i] += cardcount[game - 1]
    
sum2 = sum(cardcount)
print(sum1)
print(sum2)
