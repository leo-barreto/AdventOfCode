import sys
import math



def full_miliseconds(x, high):
    if x.is_integer():
        if high:
            return int(x - 1)
            print('high')
        else: 
            return int(x + 1)
    else:
        if high:
            return math.floor(x)
        else:
            return math.ceil(x)


inputfile = open(str(sys.argv[1]), 'r')
answer2 = 0

fullentry = [i.strip() for i in inputfile]
timetot = int(''.join([i for i in fullentry[0].split()[1:]]))
dist = int(''.join([i for i in fullentry[1].split()[1:]]))

delta = timetot ** 2 - 4 * dist
tchargehigh = full_miliseconds((timetot + math.sqrt(delta)) / 2, 1)
tchargelow = full_miliseconds((timetot - math.sqrt(delta)) / 2, 0)

answer2 = tchargehigh - tchargelow + 1

print(answer2)
