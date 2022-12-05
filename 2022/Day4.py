raw_data = []
with open("Day4Regions.txt", mode="r") as file:
    raw_data = file.readlines()

region_data = []
for item in raw_data:
    region_data.append(item.strip())

def calculate_sequenz(region):
    start = int(region.split('-')[0])
    end = int(region.split('-')[1])
    sequenz = []
    while start <= end:
        sequenz.append(start)
        start += 1
    return sequenz

## same regions
sum = 0
for r in region_data:
    region = r.split(',')
    firstSequenz = calculate_sequenz(region[0])
    secondSequenz = calculate_sequenz(region[1])
    if(len(firstSequenz)<= len(secondSequenz)):
        if(set(firstSequenz).issubset(secondSequenz)):
            sum +=1
    else:
        if(set(secondSequenz).issubset(firstSequenz)):
            sum +=1
        
print("list that are subset: " + str(sum))

sum = 0
## intersect regions
for r in region_data:
    region = r.split(',')
    firstSequenz = calculate_sequenz(region[0])
    secondSequenz = calculate_sequenz(region[1])
    if(len(set(firstSequenz).intersection(secondSequenz)) > 0 or len(set(secondSequenz).intersection(firstSequenz))> 0):
        sum +=1
print("list that intersect: " + str(sum))