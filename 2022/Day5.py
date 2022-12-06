import numpy as np
raw_data = []
with open("C:\\Workspace\AdventOfCode\\2022\\Day5Input.txt", mode="r") as file:
    raw_data = file.readlines()

crane_movement = []
isCraneMovement = False

for item in raw_data:
    if len(item.strip()) == 0:
        isCraneMovement = True
    elif isCraneMovement:       
        crane_movement.append(item.strip().split(' '))

ship = [
    "QWPSZRHD",
    "VBRWQHF",
    "CVSH",
    "HFG",
    "PGJBZ",
    "QTJHWFL",
    "ZTWDLVJN",
    "DTZCJGHF",
    "WPVMBH"
]

for command in crane_movement:
    count = int(command[1])
    fromRow = int(command[3])-1    
    toRow = int(command[5])-1
    while count > 0:
        c = ship[fromRow][len(ship[fromRow]) - 1]
        ship[fromRow] = ship[fromRow][:-1]
        ship[toRow] += c
        #print("move " +  c + " from " + str(fromRow + 1) + " to " + str(toRow + 1))
        #print(ship)
        count -=1

result =""
for item in ship:
    result += item[len(item)- 1]

print("crates on top: " + result)

## crane mover 9001
ship = [
    "QWPSZRHD",
    "VBRWQHF",
    "CVSH",
    "HFG",
    "PGJBZ",
    "QTJHWFL",
    "ZTWDLVJN",
    "DTZCJGHF",
    "WPVMBH"
]

for command in crane_movement:
    count = int(command[1])
    fromRow = int(command[3])-1    
    toRow = int(command[5])-1
    c = ship[fromRow][len(ship[fromRow]) - count:]
    ship[fromRow] = ship[fromRow][:-count]
    ship[toRow] += c
    #print(ship)


result =""
for item in ship:
    result += item[len(item)- 1]

print("crates on top with mover 9001: " + result)