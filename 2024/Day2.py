from enum import Enum

class Direction(Enum):
    Undefined = 0
    Ascending = 1
    Descending = 2

raw_data = []
with open("C:\\Workspace\AdventOfCode\\2024\\Day2Input.txt", mode="r") as file:
    raw_data = file.readlines()

# part one
safeReports = 0
for line in raw_data:
     splitItems = list(map(int, line.strip().split()))
     i = 0
     currenDirection = Direction.Undefined
     while i < len(splitItems) - 1:
         if currenDirection == Direction.Undefined:
             if  splitItems[i] <  splitItems [i +1]:
                 currenDirection = Direction.Ascending
             elif  splitItems[i] >  splitItems [i +1]:
                 currenDirection = Direction.Descending
             else:
                 i += 1
                 #print("index: "+ str(i) + " splititems: " + str(splitItems) + " direction: " + str(currenDirection))
                 break
             #print("index: "+ str(i) + " splititems: " + str(splitItems) + " direction: " + str(currenDirection))
         
         if currenDirection == Direction.Ascending:
            diff = splitItems[i + 1] - splitItems [i]
            if diff < 1 or diff > 3:
                i +=1
                break
         elif currenDirection == Direction.Descending:
             diff = splitItems[i] - splitItems [i + 1]
             if diff < 1 or diff > 3:
                i +=1
                break        
         if i == len(splitItems)-2:
             safeReports += 1
         i += 1
          
print("safe reports part one: " + str(safeReports))

# part two

def is_safe_report(levels):
    # get all diffs of each level
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # if all are bigger 0
    if any(diff == 0 for diff in diffs):
        return False
    
    # check for all sequence
    if all( 1 <= diff <= 3 for diff in diffs): 
        return True
    elif all( -3 <= diff <= -1 for diff in diffs): 
        return True
    else:
        return False

safeReports = 0
for line in raw_data:
     levels = list(map(int, line.strip().split()))
     if is_safe_report(levels):
         safeReports += 1
     else:
         # remove each level and check if it is valid
         for i in range(len(levels)):
             # create a list by remove an element from a list without changing the existing one
             new_levels = levels[:i] + levels[i+1:]
             if(is_safe_report(new_levels)):
                 safeReports += 1
                 break
print("safe reports part two: " + str(safeReports))