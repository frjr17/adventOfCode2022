with open('./puzzle.txt') as file:
    puzzle = [[[int(c.split('-')[0]), int(c.split("-")[1])] for c in line.rstrip().split(",")] for line in file.readlines()]


def cr(l):
    return range(l[0],l[1]+1)

if __name__ == "__main__":
    results = 0
    
    for group in puzzle:
        group1 = set(cr(group[0]))        
        group2 = set(cr(group[1])) 
        if group1.issuperset(group2) or group2.issuperset(group1):
            results+=1

    print('Part One')
    print('Resp:',results)
# ===================== Part Two ================================
    results=0
    for group in puzzle:
        group1 = set(cr(group[0]))        
        group2 = set(cr(group[1])) 
        if group1.intersection(group2) or group2.intersection(group1):
            results+=1

    
    print('\nPart Two')
    print('Resp:',results)
