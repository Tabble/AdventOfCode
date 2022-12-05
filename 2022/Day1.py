# reindeer magical food
# magical energy
# min 50 stars till december 25th
# Elves inventory: Calories carried by Elfes
# one item by line
# each elf seperates their own from the previous elfs by a blank line

raw_data = []
with open("Day1ElfInventory.txt", mode="r") as file:
    raw_data = file.readlines()
    #print("raw data count: " + str(len(raw_data)))

sum_data = []
sum = 0
for item in raw_data:
    temp = item.strip()
    if(len(temp)== 0):
        sum_data.append(sum)
        sum = 0
    else:
        sum += int(temp)
sum_data.sort(reverse=True)
# most calories
print("elf with top calories:" + str(sum_data[0]))

# top 3 elfs calories in total
top_three = sum_data[:3]
sum_top = 0
for item in top_three:
    sum_top += item
print("calories of top 3 elfes:" + str(sum_top))
