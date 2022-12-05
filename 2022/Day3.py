# rucksack has two large compartments
# all items of a given type should go into exactly one of the two compartments
# failed for exactly one item type per rucksack
# lower and upper case are different items
# compartment 1 and two lenght is same string split in the middle is first and second compartment

import string
az_upper = string.ascii_uppercase
az_lower = string.ascii_lowercase

priority = {}

p = 1
for item in az_lower:
    priority[item] = p
    p += 1

for item in az_upper:
    priority[item] = p
    p += 1

raw_data = []
with open("Day3Backpacks.txt", mode="r") as file:
    raw_data = file.readlines()

## find doublicate characters and sum priority
sum = 0
for backpack in raw_data:
    backpack = backpack.strip()
    front = backpack[:int(len(backpack)/ 2)]
    back = backpack[int(len(backpack)/ 2):]
    for c in front:
        if c in back:
            # print("doublicate character: " + c)
            sum += priority[c]
            break
print("total priority: " + str(sum))

## find groups
strip_backpack = []
for data in raw_data:
    strip_backpack.append(data.strip())

i = 0
sum = 0
for backpack in strip_backpack:
    if i % 3 == 0:
        firstBackpack = backpack
        secondBackpack = strip_backpack[i + 1]
        thirdBackpack = strip_backpack[i + 2]
        for c in firstBackpack:
            if c in secondBackpack and c in thirdBackpack:
                # print("doublicate character in the 3: " + c)
                sum += priority[c]
                break
    i += 1
               
print("total priority of the 3: " + str(sum))              