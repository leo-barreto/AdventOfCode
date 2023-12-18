import sys


def expand_matrix(matrix):
    expmatrix = matrix.copy()
    sizecolumn = len(matrix[0])
    expmatrix.insert(0, '.' * sizecolumn)
    expmatrix.append('.' * sizecolumn)

    for i in range(len(expmatrix)):
        expmatrix[i] = '.' + expmatrix[i] + '.'

    return expmatrix


def find_symbol(matrix):
    allsymbols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            element = matrix[i][j]
            if element.isdigit() == False and element != '.':
                allsymbols.append([i, j])
    
    return allsymbols



def find_number(matrix):
    number = ''
    # allnumbers: [number, line, column end]
    allnumber = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            element = matrix[i][j]
            jend = j
            if element.isdigit():
                number += element
                jend += 1
           
            else: 
                if number != '':
                    allnumber.append([number, i, jend])
                number = ''

    return allnumber


inputfile = open(str(sys.argv[1]), 'r')
sum1 = 0
sum2 = 0

fullentry = [i.strip() for i in inputfile]
expmatrix = expand_matrix(fullentry)
numbers = find_number(expmatrix)
symbols = find_symbol(expmatrix)

gearnumbers = [[] for i in range(len(symbols))]
for n in numbers:
    number = int(n[0])
    line = n[1]
    colmin = n[2] - len(n[0])
    colmax = n[2] - 1

    for s in symbols:
        # Check if adjacent
        if abs(s[0] - line) <= 1:
            if s[1] >= colmin - 1 and s[1] <= colmax + 1:
                sum1 += number
                if expmatrix[s[0]][s[1]] == '*':
                    gearnumbers[symbols.index(s)].append(number)

for g in gearnumbers:
    if len(g) == 2:
        sum2 += g[0] * g[1]

print(sum1)
print(sum2)
