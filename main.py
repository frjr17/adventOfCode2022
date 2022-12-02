with open('./puzzle.txt') as file:
    puzzle = [line.rstrip().split(' ') for line in file.readlines()]


if __name__ == "__main__":
    # A = Rock = X
    # B = Paper = Y
    # C = Scissors = Z
    answers = {'A': 'Y', 'B': 'Z', 'C': "X"}
    equals = {'A':'X','B':"Y",'C':"Z"}
    values = {'X': 1, 'Y': 2, 'Z': 3}
    # rock = [1, 'A', 'Y']
    # paper = [2, 'B', 'Z']
    # scissors = [3, 'C', 'X']
    results = []

    for game in puzzle:
        opponent, answer = game
        if answer == equals[opponent]:
            results.append(values[answer]+3)
        elif answer == answers[opponent]:
            results.append(values[answer]+6)
        else:
            results.append(values[answer])

    print('Part One')
    print('Sum',sum(results))
# ===================== Part Two ================================
    results = []
    
    for game in puzzle:
        opponent, answer = game
        if answer == 'Y':
            results.append(values[equals[opponent]]+3)
        elif answer == 'Z':
            results.append(values[answers[opponent]]+6)
        else:
            loser_item = [item for item in answers if answers[item] == equals[opponent]][0]
            results.append(values[equals[loser_item]])

    print('\nPart Two')
    print('Sum',sum(results))

