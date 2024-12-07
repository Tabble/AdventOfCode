strip_data = [line.strip("\n") for line in open("C:\\Workspace\AdventOfCode\\2024\\Day7Input.txt", mode="r").readlines()]

matrix = [[*map(str, line.split(': '))] for line in strip_data]
result = 0

def evaluate_recursive(numbers, target, current_value=0, current_expression=""):
    global result
    #print(f"Called with: numbers={numbers}, current_value={current_value}, current_expression='{current_expression}'")
    if not numbers:
        if current_value == target:
            result += target
            print(f"found solution: {current_expression} = {target}")
            return True
        return False

    next_number = numbers[0]
    remaining_numbers = numbers[1:]

    if evaluate_recursive(
        remaining_numbers,
        target,
        current_value + next_number,
        f"{current_expression} + {next_number}" if current_expression else f"{next_number}"
    ):
        return True

    if evaluate_recursive(
        remaining_numbers,
        target,
        current_value * next_number if current_expression else next_number,
        f"{current_expression} * {next_number}" if current_expression else f"{next_number}"
    ):
        return True

    return False

for row in matrix:
    test_value = int(row[0])
    numbers = list(map(int, row[1].split()))
    evaluate_recursive(numbers, test_value)

print("result part one: " + str(result))