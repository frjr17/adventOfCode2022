with open('./puzzle.txt') as file:
    stack, instructions = file.read().split("\n\n")
    stack = stack.split("\n")
    numbers = len(stack.pop().split())
    positions = [[i,i+2] for i in range(0,numbers*3+numbers-1,4)]
    _stack = {i:[] for i in range(1,numbers+1)}
    for line in stack:
        i =1
        for position in positions:
            start,end = position
            if line[start:end+1] != "   ":
                _stack[i].append(line[start:end+1])
            i+=1
    stack = _stack
    puzzle= _stack
    instructions = [[int(i.split(" ")[1]),int(i.split(" ")[3]),int(i.split(" ")[5])] for i in instructions.strip().split('\n')]

if __name__ == "__main__":
    results = []
    stack1 = eval(repr(stack))
    for instruction in instructions:
        move,_from,to = instruction
        for i in range(0,move):
            stack1[to].insert(0,stack1[_from].pop(0))
    results = ''.join([crates[0][1] for crates in stack1.values()])
    print('Part One')
    print('Resp:', results)
# ===================== Part Two ================================
    for instruction in instructions:
        move,_from,to = instruction
        for i in range(move-1,-1,-1):
            if move >1:
                stack[to].insert(0,stack[_from].pop(i))
            else:
                stack[to].insert(0,stack[_from].pop(0))
    results = ''.join([crates[0][1] for crates in stack.values()])
    print('\nPart Two')
    print('Resp:', results)
