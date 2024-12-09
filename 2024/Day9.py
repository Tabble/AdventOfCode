strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2024\\Day9Input.txt", mode="r").readlines()]

def generate_initial_string(strip_data):
    list_result = []
    strip_data = strip_data[0]
    files = strip_data[0::2]
    free_space = strip_data[1::2]
    for i in range(0, len(files)):
        count_files = int(files[i])
        list_result.extend([str(i)] * count_files)
        if i < len(free_space):
            count_free_space = int(free_space[i])
            list_result.extend('.' * count_free_space)
    return list_result

def find_last_number(list_result, end):
    for i, char in enumerate(reversed(list_result[:end])):
        if char.isdigit():
            index_last_number = end - 1 - i
            last_number = char
            break
    else:
        return None, None
    return index_last_number, last_number

def find_first_point(list_result, start=0):
    for j in range(start, len(list_result)):
        if list_result[j] == '.':
            return j
    return None

def calculate_checksum(list_result):
    total = 0
    for i, char in enumerate(list_result):
        if char.isdigit():
            total += i * int(char)
        else:
            break
    return total

list_result = generate_initial_string(strip_data)
finished = False
index_first_point = 0
end_index = len(list_result)

while not finished: 
    index_last_number, last_number = find_last_number(list_result, end_index)
    index_first_point = find_first_point(list_result, index_first_point)

    if index_first_point is not None:
        if index_first_point < index_last_number:
            list_result[index_last_number], list_result[index_first_point] = '.', last_number
            end_index = index_last_number
        else:
            finished = True
    else:
        finished = True

checksum = calculate_checksum(list_result)
# result = ''.join(list_result)                          
#print("result:" + str(result))
print("checksum part one: "+ str(checksum))