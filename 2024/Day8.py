strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2024\\Day8Input.txt", mode="r").readlines()]
matrix = [[*map(str, line)] for line in strip_data]

positions = {}
for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
        if char != ".": 
            if char not in positions:
                positions[char] = []
            positions[char].append((col_idx, row_idx))

antinodes = []
for char, coords in positions.items():
    for item in coords:
        for checkItem in coords:
            if item != checkItem:
                #print(f"{item} -> {checkItem}")
                x1 = item[0]
                y1 = item[1]
                x2 = checkItem[0]
                y2 = checkItem[1]

                dx = (x2 - x1) * -1
                dy = (y2 - y1) * -1
                
                new_coord_x = x1 + dx
                new_coord_y = y1 + dy
                
                if new_coord_x < 0 or new_coord_x >= len(matrix[0]):
                    continue
                if new_coord_y <0 or new_coord_y >= len(matrix):
                    continue
                
                matrix_entry = matrix[new_coord_y][new_coord_x]
                #print(f"character {char}: ({(x1 + 1)}, {y1 + 1}) -> ({(x2 + 1)}, {y2 + 1}) antinode: ({new_coord_x+1}, {new_coord_y+1}) with char: {matrix_entry}")
                if matrix_entry == ".":
                    matrix[new_coord_y][new_coord_x] = "#"               
                c = (new_coord_x, new_coord_y)
                if c not in antinodes:
                    antinodes.append(c)

print("unique antinodes part one: " + str(len(antinodes)))
#print(str(matrix))