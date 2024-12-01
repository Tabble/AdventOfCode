# create list of items

# part one
# order each list by number
# calculate distance between each item
# add upp all distances

# part two
# check how entry from list 1 exists in list 2 and accumulate

raw_data = []
with open("C:\\Workspace\AdventOfCode\\2024\\Day1Input.txt", mode="r") as file:
    raw_data = file.readlines()

list1 = []
list2 = []
for item in raw_data:
    list1.append(int(item.split('   ')[0]))
    list2.append(int(item.split('   ')[1]))

list1.sort()
list2.sort()

distance = 0
similarity = 0
for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    distance += diff

    amount = list2.count(list1[i])
    similarity += (list1[i] * amount)
 
print("distance: " + str(distance))
print("similarity: " + str(similarity))