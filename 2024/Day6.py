strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2024\\Day6Input.txt", mode="r").readlines()]
matrix = [[*map(str, line)] for line in strip_data]

def set_x_to_current_guard(matrix, guard):
    matrix[guard[0]][guard[1]] = 'X'

def get_current_guard(matrix):
    targets = {'^', '<', '>', 'v'}
    return next(((i, j, char) for i, row in enumerate(matrix) for j, char in enumerate(row) if char in targets), None)

guard = get_current_guard(matrix)

finished = False
while not finished: 
    if guard[2] == '^':
        if guard[0] == 0:
            finished = True
            set_x_to_current_guard(matrix, guard)
        elif matrix[guard[0]-1][guard[1]] == '#':
            matrix[guard[0]][guard[1]] = '>'
            guard = get_current_guard(matrix)
        else:
            matrix[guard[0]-1][guard[1]] = guard[2]
            set_x_to_current_guard(matrix, guard)
            guard = get_current_guard(matrix)
    elif guard[2] == '>':
        if guard[1] == len(matrix[0])-1:
            finished = True
            set_x_to_current_guard(matrix, guard)
        elif matrix[guard[0]][guard[1]+1] == '#':
            matrix[guard[0]][guard[1]] = 'v'
            guard = get_current_guard(matrix)
        else:
            matrix[guard[0]][guard[1]+1] = guard[2]
            set_x_to_current_guard(matrix, guard)
            guard = get_current_guard(matrix)
    elif guard[2] == 'v':
        if guard[0] == len(matrix[0])-1:
            finished = True
            set_x_to_current_guard(matrix, guard)
        elif matrix[guard[0]+1][guard[1]] == '#':
            matrix[guard[0]][guard[1]] = '<'
            guard = get_current_guard(matrix)
        else:
            matrix[guard[0]+1][guard[1]] = guard[2]
            set_x_to_current_guard(matrix, guard)
            guard = get_current_guard(matrix)
    elif guard[2] == '<':
        if guard[1] == 0:
            finished = True
            set_x_to_current_guard(matrix, guard)
        elif matrix[guard[0]][guard[1]-1] == '#':
            matrix[guard[0]][guard[1]] = '^'
            guard = get_current_guard(matrix)
        else:
            matrix[guard[0]][guard[1]-1] = guard[2]
            set_x_to_current_guard(matrix, guard)
            guard = get_current_guard(matrix)
    else:
        finished = True

result = sum(row.count('X') for row in matrix)
print("matrix: " + str(result))