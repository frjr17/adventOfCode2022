with open('./puzzle.txt') as file:
    puzzle =[line.rstrip() for line in file.readlines()]
    alphabet = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'.split(', ')
    alphabet_upper = [char.upper() for char in alphabet]
    alphabet = alphabet+alphabet_upper
    # print(puzzle)

if __name__ == "__main__":
    results = []
    for line in puzzle:
        length = len(line)
        for letter in line:
            common = line.find(letter,0,int(length/2)) != -1 and line.find(letter,int(length/2)) != -1
            if common:
                results.append(letter)
                break 
    
    results = [alphabet.index(l)+1 for l in results]
    print('Part One')
    print('Sum:',sum(results))

# ===================== Part Two ================================
    results = []
    i = 0
    
    while True:
        if i == len(puzzle):
            break
        group = [puzzle[i],puzzle[i+1],puzzle[i+2]]
       
        for letter in ''.join(group):
            common  = letter if group[0].find(letter) != -1 and group[1].find(letter) != -1 and group[2].find(letter)!=-1 else False
            if common:
                results.append(common)
                break
        i+=3
   
    results = [alphabet.index(l)+1 for l in results]
    print('\nPart Two')
    print('Sum:',sum(results))
    
