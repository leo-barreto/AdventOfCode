import sys



def break_range(seedranges, soilmatrix):
    newranges = seedranges.copy()
  
    i = 0 
    while i < len(newranges):
        seedrange = newranges[i]
        seedstart = seedrange[0]
        seedend = seedstart + seedrange[1] - 1

        soiltoplantstart = which_soil(seedstart, soilmatrix)
        soiltoplantend = which_soil(seedend, soilmatrix)

        if soiltoplantstart != soiltoplantend:
            newranges.remove(seedrange)
            # Break from right, add rest on left
            s = soiltoplantstart
            if isinstance(s, int):
                newbreak = soilmatrix[s][1] + soilmatrix[s][2] - seedstart
                newranges.append([seedstart, newbreak])
            else:
                nexts = int(s + 0.5)
                newbreak = soilmatrix[nexts][1] - seedstart
                newranges.append([seedstart, newbreak])

            newstartleft = seedstart + newbreak
            newranges.append([newstartleft, seedend - newstartleft + 1])

        else:
            i += 1

    return newranges


def plant_seed_range(brokenranges, soilmatrix):
    plantedrange = []
    for seedrange in brokenranges:
        for s in soilmatrix:
            if is_seed_in_soil(seedrange[0], s[1], s[2]):
                plantedrange.append(plant_seed_full(seedrange, s))
                break

        if isinstance(which_soil(seedrange[0], soilmatrix), float):
            plantedrange.append(seedrange)

    return sorted(plantedrange, key=lambda x: x[0])


def is_seed_in_soil(seedstart, plantstart, plantrange):
    return (seedstart >= plantstart and seedstart < plantstart + plantrange)

def which_soil(seedtest, soils):
    for i, s in enumerate(soils):
        if i == 0 and seedtest < s[1]:
            return -0.5

        if is_seed_in_soil(seedtest, s[1], s[2]):
            return i
        
        if seedtest < s[1]:
            return i - 0.5
        
        if i == len(soils) - 1:
            return i + 0.5

        if seedtest > s[1] + s[2] and seedtest < soils[i + 1][1]:
            return i + 0.5

def plant_seed_full(seed, s):
    return [seed[0] - s[1] + s[0], seed[1]]



inputfile = open(str(sys.argv[1]), 'r')
sum1 = 0
sum2 = 0

fullentry = [i.strip() for i in inputfile]

seeds = fullentry[0].split(': ')[1].split()
seedranges = [[int(seeds[i]), int(seeds[i + 1])] for i in range(0, len(seeds), 2)]

maps = []

ileft = 0
for i, line in enumerate(fullentry):
    if line == '':
       maps.append(fullentry[ileft + 2:i])
       ileft = i
    elif i == len(fullentry) - 1:
        maps.append(fullentry[ileft + 2:])

locations = []
for seed in seedranges:
    seed = [seed]
    for m in maps[1:]:
        soilsint = []
        for i in m:
            soilsint.append([int(s) for s in i.split()])

        soilmatrix = sorted(soilsint, key=lambda x: x[1])
        brokenrange = break_range(seed, soilmatrix)
        seed = plant_seed_range(brokenrange, soilmatrix)
    
    locations.extend(seed)

print(f'Minimum location: {sorted(locations, key=lambda x: x[0])[0][0]}')


