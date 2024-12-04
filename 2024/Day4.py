import re
strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2024\\Day4Input.txt", mode="r").readlines()]

matrix = [[*map(str, line)] for line in strip_data]


def sum_xmas_occurences(subsstring):
    pattern = r"(?=(XMAS|SAMX))"
    matches = re.findall(pattern, subsstring)
    return len(matches)
def sum_altered_xmas_occurences(subsstring):
    pattern = r"(?=(MAS|SAM))"
    matches = re.findall(pattern, subsstring)
    return len(matches)    

xmas_occurences = 0
# rows
for row_index in range(0, len(matrix)):
    char_in_row = matrix[row_index]
    row_string = ''.join(char_in_row)
    xmas_occurences += sum_xmas_occurences(row_string)

# columns
for column_index in range(0, len(matrix[0])):
        char_in_column = [i[column_index] for i in matrix]
        column_string =''.join(char_in_column)
        xmas_occurences += sum_xmas_occurences(column_string)
    
# diagonal -> start bottom left and then move up. First possible occurense is 4 to the left
row_lenght = len(matrix[0]) 
start_row_index = 3
end_row_index = row_lenght - 1
# upwards left
loop = start_row_index
while loop <= end_row_index:
    j = loop
    i = len(matrix) - 1
    diagonal_string = ""
    while j >= 0:      
        diagonal_string += matrix[i][j]
        i -= 1
        j -= 1
    loop += 1
    xmas_occurences += sum_xmas_occurences(diagonal_string)
    #print("diagonal_string: " + str(diagonal_string)) 

# upwards right
loop = 0
while loop <= end_row_index - 3:
    i = len(matrix) - 1
    j = loop
    diagonal_string = ""
    while j <= end_row_index:      
        diagonal_string += matrix[i][j]
        i -= 1
        j += 1
    loop += 1
    xmas_occurences += sum_xmas_occurences(diagonal_string)
    #print("diagonal_string: " + str(diagonal_string))               

# downwards -> start at [0,1] and go down
loop = 1
while loop <= end_row_index - 3:
    i = 0
    j = loop
    diagonal_string = ""
    while j <= end_row_index:
        diagonal_string += matrix[i][j]
        i += 1
        j += 1
    loop += 1
    xmas_occurences += sum_xmas_occurences(diagonal_string)
    #print("diagonal_string: " + str(diagonal_string)) 

# downwards -> start at [0,len(matrix)- 1] and go down
loop = 1
while loop <= end_row_index - 3:
    i = 0
    j = len(matrix) - 1 - loop
    diagonal_string = ""
    while j >= 0:
        diagonal_string += matrix[i][j]
        i += 1
        j -= 1
    loop += 1
    xmas_occurences += sum_xmas_occurences(diagonal_string)
    #print("diagonal_string: " + str(diagonal_string)) 

print("xmas_occurences part one: " + str(xmas_occurences))

# part two
xmas_occurences = 0
for row_index in range(1, len(matrix)-1):
    for column_index in range(1, len(matrix[0])-1):
        result = matrix[row_index][column_index]
        if result == 'A':
            diag1 = matrix[row_index-1][column_index-1] + result + matrix[row_index+1][column_index+1]
            diag2 = matrix[row_index+1][column_index-1] + result + matrix[row_index-1][column_index+1]
            r1 = sum_altered_xmas_occurences(diag1)
            r2 = sum_altered_xmas_occurences(diag2)
            if(r1 == 1 and r2 == 1):
                xmas_occurences +=1
                #print("["+ str(row_index) + "," + str(column_index) +"] diagonal_string: " + str(diag1)+ "diagonal_string: " + str(diag2)) 
print("xmas_occurences part two: " + str(xmas_occurences))               