import sys


def isgamepossible(s):
    for cubes in s.split(','):
        numberstr, color = cubes.split()
        number = int(numberstr)
        if color == 'red' and number > 12:
            return False
        elif color == 'green' and number > 13:
            return False
        elif color == 'blue' and number > 14:
            return False

    return True

def gamepower(line):
    minred, mingreen, minblue = 0, 0, 0
    for s in line.split(':')[1].split(';'):
        for cubes in s.split(','):
            numberstr, color = cubes.split()
            number = int(numberstr)
            if color == 'red' and number > minred:
                minred = number
            elif color == 'green' and number > mingreen:
                mingreen = number
            elif color == 'blue' and number > minblue:
                minblue = number

    return minred * mingreen * minblue

inputfile = open(str(sys.argv[1]), 'r')
sum1 = 0
sum2 = 0

game = 1
for line in inputfile:
    sum2 += gamepower(line)
    sets = line.split(':')[1].split(';')
    conditions = [isgamepossible(i) for i in sets]
    if all(conditions):
        sum1 += game
    game += 1

print(sum1)
print(sum2)
