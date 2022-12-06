from collections import Counter
with open('./puzzle.txt') as file:
    puzzle= file.readlines()[0].strip()
if __name__ == "__main__":
    result = 0
    for i in range(4,len(puzzle)):
        group = puzzle[i-4:i]
        if set(Counter(group).values()) =={1}:
            result = i
            break
    print('\nPart One')
    print('Resp:', result)
# ===================== Part Two ================================
    for i in range(14,len(puzzle)):
        group = puzzle[i-14:i]
        if set(Counter(group).values()) =={1}:
            result = i
            break
    print('\nPart Two')
    print('Resp:', result)
