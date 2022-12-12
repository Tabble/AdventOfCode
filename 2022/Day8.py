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
