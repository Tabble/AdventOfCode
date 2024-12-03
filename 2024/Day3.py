import re
with open("C:\\Workspace\AdventOfCode\\2024\\Day3Input.txt", mode="r") as file:
    raw_data = file.readlines()


def sum_mul_in_substring(subsstring):
    total = 0
    # find pattern = mul\(\d{1,3},\d{1,3}\) and extract numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, subsstring)
    for entry in matches:
        num1, num2 = map(int, entry)  # Each entry is a tuple of two numbers (because of the capturing groups)
        total += num1 * num2
    return total  

# part one
result = 0
for line in raw_data:
    result += sum_mul_in_substring(line)
print("result part one: " + str(result))
 
# part two
# no do or don't in front = enabled
# don't in front = disabled until do in front
result = 0
long_string = ''.join(raw_data) # we need to check in between all lines
#test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
substringPattern = r"(?=(?:don't\(\)|do\(\)))"
substrings = re.split(substringPattern, long_string)
for item in substrings:
    if item.startswith("don't()"):
        continue
    else:
        result += sum_mul_in_substring(item)
print("result part two: " + str(result))