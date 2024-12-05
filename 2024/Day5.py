import math
strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2024\\Day5Input.txt", mode="r").readlines()]


commands = []
rows = []
for item in strip_data:
    if "|" in item:
        commands.append(item)
    elif "," in item:
        rows.append(item)

commands_of_numbers = [list(map(int, c.split('|'))) for c in commands]
rows_of_numbers = [list(map(int, r.split(','))) for r in rows]

valid_rows = []
invalid_rows = []
for row in rows_of_numbers:
    valid = True
    for command in commands_of_numbers:
        c1, c2 = command
        first = row.index(c1) if c1 in row else -1
        second = row.index(c2) if c2 in row else -1
        if first >= 0 and second >= 0 and second < first:
            valid = False
            break
    if valid:
        valid_rows.append(row)
    else:
        invalid_rows.append(row)

def calculate_sum(valid_rows):
    total = 0
    for items in valid_rows:
        total += items[math.floor(len(items) / 2)]
    return total

print("sum part one: " + str(calculate_sum(valid_rows)))

for row in invalid_rows:
    swapped = True
    while swapped:  
        swapped = False  
        for command in commands_of_numbers:
                c1, c2 = command
                first = row.index(c1) if c1 in row else -1
                second = row.index(c2) if c2 in row else -1

                if first >= 0 and second >= 0 and second < first:
                    # Swap elements to correct order
                    row[first], row[second] = row[second], row[first]
                    swapped = True  # A swap was made, so we need to check again

print("sum part two: " + str(calculate_sum(invalid_rows)))