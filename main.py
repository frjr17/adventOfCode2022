with open('./puzzle.txt') as file:
    puzzle = [[a for a in line.strip()] for line in file.readlines()]
    height = len(puzzle)
    length = len(puzzle[0])
    height_range = range(1, height-1)
    length_range = range(1, length-1)


def look_top(number, i, j):
    result = True
    scenic_score = 0
    k = 1
    while i-k in range(0, height):
        result = bool(puzzle[i-k][j] < number)

        scenic_score += 1
        if result == False:
            break
        k += 1

    return result, scenic_score


def look_bottom(number, i, j):
    result = True
    scenic_score = 0
    k = 1
    while i+k in range(0, height):
        result = bool(puzzle[i+k][j] < number)

        scenic_score += 1
        if result == False:
            break
        k += 1

    return result, scenic_score


def look_left(number, i, j):
    result = True
    k = 1
    scenic_score = 0

    while j-k in range(0, length):
        result = bool(puzzle[i][j-k] < number)

        scenic_score += 1
        if result == False:
            break
        k += 1

    return result, scenic_score


def look_right(number, i, j):
    result = True
    k = 1
    scenic_score = 0

    while j+k in range(0, length):
        result = bool(puzzle[i][j+k] < number)

        scenic_score += 1
        if result == False:
            break
        k += 1

    return result, scenic_score


def look_visibility(number, i, j):
    # print('Top Visibility:',look_top(number,i,j))
    # print('Bottom Visibility:',look_bottom(number,i,j))
    # print('Left Visibility:',look_left(number,i,j))
    # print('Right Visibility:',look_right(number,i,j))
    top = look_top(number, i, j)
    bottom = look_bottom(number, i, j)
    left = look_left(number, i, j)
    right = look_right(number, i, j)
    visibility = top[0] or bottom[0] or left[0] or right[0]
    scenic_score = top[1] * bottom[1] * left[1] * right[1]
    return visibility, scenic_score


if __name__ == "__main__":
    result = height*2+(length-2)*2
    scenic_scores = []
    for i in height_range:
        for j in length_range:
            number = puzzle[i][j]
            visibility, scenic_score = look_visibility(number, i, j)
            scenic_scores.append(scenic_score)
            if visibility:
                result += 1

    # Printing Results
    print('\nPart One')
    print('Resp:', result)

# ===================== Part Two ================================

    # Printing Results
    print('\nPart Two')
    print('Resp:', max(scenic_scores))
