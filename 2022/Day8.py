# visible tree
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2022\\Day8Input.txt", mode="r").readlines()]
trees = [[*map(int, line)] for line in strip_data]

# outer ring
tree_count = 2 * (len(trees[0]) + len(trees) - 2)
#print("outer ring " + str(visible))

for row_index in range(1, len(trees) - 1):
    for column_index in range(1, len(trees[0]) - 1):
        tree = trees[row_index][column_index]
        # check if it is the biggest in the row
        trees_in_row = trees[row_index]
        trees_in_column = [i[column_index] for i in trees]

        left = trees_in_row[:column_index]
        right = trees_in_row[column_index + 1 :]
        top = trees_in_column[:row_index]
        bottom = trees_in_column[row_index + 1 :]

        # if tree is visible in any direction add to the counter
        if tree > min(max(left), max(right), max(top), max(bottom)):
            tree_count +=1   
print("visible trees:" + str(tree_count))

s = 0
w = len(trees[0])
h = len(trees)

for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        t = trees[y][x]

        row = trees[y]
        col = [i[x] for i in trees]

        left = row[:x][::-1]
        right = row[x + 1 :]
        top = col[:y][::-1]
        bottom = col[y + 1 :]

        left_blocked = [i for i, v in enumerate(left) if v - t >= 0]
        left_score = x if len(left_blocked) == 0 else left_blocked[0] + 1

        right_blocked = [i for i, v in enumerate(right) if v - t >= 0]
        right_score = w - x - 1 if len(right_blocked) == 0 else right_blocked[0] + 1

        top_blocked = [i for i, v in enumerate(top) if v - t >= 0]
        top_score = y if len(top_blocked) == 0 else top_blocked[0] + 1

        bottom_blocked = [i for i, v in enumerate(bottom) if v - t >= 0]
        bottom_score = h - y - 1 if len(bottom_blocked) == 0 else bottom_blocked[0] + 1

        ss = left_score * right_score * top_score * bottom_score
        if ss > s:
            s = ss
print(s)
