import sys



def find_next_destination(s, mapped):
    for v in mapped:
        entry = v.split()
        dest = int(entry[0])
        source = int(entry[1])
        rang = int(entry[2])

        if s in range(source, source + rang):
            return dest + s - source, mapped.index(v)

    return s


def find_range_dest(start, step, mapped):
    for v in mapped:
        entry = v.split()
        dest = int(entry[0])
        source = int(entry[1])
        rang = int(entry[2])
            
        if start > source:
            nextbreak = start + step - source - rang
            if nextbreak <= 0:
                path.append([dest + start - source, step])
            else:
                path.append([dest + start - source, 





inputfile = open(str(sys.argv[1]), 'r')
sum1 = 0
sum2 = 0

fullentry = [i.strip() for i in inputfile]

seeds = fullentry[0].split(': ')[1].split()

maps = []

ileft = 0
for i, line in enumerate(fullentry):
    if line == '':
       maps.append(fullentry[ileft + 2:i])
       ileft = i
    elif i == len(fullentry) - 1:
        maps.append(fullentry[ileft + 2:])

    



