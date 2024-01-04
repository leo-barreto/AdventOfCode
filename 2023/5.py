import sys


#def split_ranges(initialranges, mapped):
#    for i in initialranges:
#        start = i[0]
#        end = i[1]
#
#        for v in mapped:
#            entry = v.split()
#            source = int(entry[1])
#            rang = int(entry[2])
#
#            if start < source:
#                if end > source:
#                    ranges.append([
#
#            else if start >= source and start < source + rang:
#                if start + step > source + rang:
#                    return dest + start - source, source + rang - start
#                else:
#                    return dest + start - source, step
#
#    return start, step

def find_next_destination(s, mapped):
    for v in mapped:
        entry = v.split()
        dest = int(entry[0])
        source = int(entry[1])
        rang = int(entry[2])

        if s in range(source, source + rang):
            return dest + s - source, mapped.index(v)

    return s


def find_next_break(start, step, mapped):
    for v in mapped:
        entry = v.split()
        dest = int(entry[0])
        source = int(entry[1])
        rang = int(entry[2])
        
        if start > source and start < source + rang:
            if start + step < source + rag:
                return -1
            else:
                return source + rang

    return -1



inputfile = open(str(sys.argv[1]), 'r')
sum1 = 0
sum2 = 0

fullentry = [i.strip() for i in inputfile]

seeds = fullentry[0].split(': ')[1].split()
uniqueseeds = unique_seeds(seeds)

maps = []

ileft = 0
for i, line in enumerate(fullentry):
    if line == '':
       maps.append(fullentry[ileft + 2:i])
       ileft = i
    elif i == len(fullentry) - 1:
        maps.append(fullentry[ileft + 2:])


brokenseedsstart = seeds[::2]
brokenseedsstep = seeds[1::2]
locations = []
for i in range(len(brokenseedsstart):
    breaksstart = [brokenseedsstart[i]]
    breaksstep = [brokenseedsstep[i]]
    
    for j in range(len(breaksstart)):
        start = breaksstart[j]
        step = breaksstep[j]
        for mapped in maps[1:]:
            nextbreak = find_next_break(start, breaksstep[j], mapped)

            if nextbreak != -1:
                breaksstart.append(nextbreak)
                breaksstep.append(start + step - nextbreak)
        
            s = find_next_destination(start, mapped)

        locations.append
    


locations = []
for i in range(0, len(seeds[:-1]), 2):
    start = int(seeds[i])
    end = start + int(seeds[i + 1])
    for mapped in maps[1:]:
        s = find_next_destination(start, mapped)
       
    locations.append(s)
print()
print(min(locations))

