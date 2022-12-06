# detect a start of packet marker => indicated by a sequence of four characters that are all different
# first character that was not used before and has 4 different characters in front

raw_data = []
with open("C:\\Workspace\AdventOfCode\\2022\\Day6Input.txt", mode="r") as file:
    raw_data = file.readlines()

def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False;
    return True;

input = raw_data[0]

def find_unique_charachters_count(amount: int):
    i = 0
    while i < len(input):
        c = input[i]
        if i > amount - 1:
            compare_data = input[i - amount:i]
            #print("character: " + c + " sequenz: " + str(compare_data))
            if uniqueCharacters(compare_data):
                print("index: " + str(i) + " character: " + c + " sequenz: " + str(compare_data))
                break       
        i+=1   
find_unique_charachters_count(4)
find_unique_charachters_count(14)