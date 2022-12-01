with open('./puzzle.txt') as file:
    puzzle = file.readlines()


if __name__ == "__main__":
    elfs = [[]]
    calories = []

    for number in puzzle:
        if number == '\n':
            elfs.append([])
        else:
            elfs[-1].append(int(number.rstrip()))

    for elf in elfs:
        calories.append(sum(elf))

    print('Part One')
    print('Max elf>', calories.index(max(calories))+1)
    print('Calories>', max(calories))

# ===================== Part Two ================================

    three_top = []
    for i in range(0,3):
        three_top.append(max(calories))
        calories.remove(max(calories))

    print('\nPart Two')
    print('Top three>', three_top)
    print('Calories>', sum(three_top))
    