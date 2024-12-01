raw_data = []
with open("C:\\Workspace\AdventOfCode\\2022\\Day7Input.txt", mode="r") as file:
    raw_data = file.readlines()

strip_data = []
for item in raw_data:
    strip_data.append(item.strip())

class file_data:
    size : int
    name : str

class directory:
    name : str
    file_datas = []
    direcoties = []

main_directory = directory()
main_directory.name = "/"
cur_directory : directory
for row in strip_data:
    cur_directory = main_directory
    if row == "$ cd /":
        # go up to main directory
        cur_directory = main_directory
    elif row == "$ ls":
        # list under
        cur_directory = main_directory
    elif row.startswith("dir"):
         dir_name = row[4: len(row)]
         new_dir = directory()
         new_dir.name = dir_name
         cur_directory.direcoties.append(new_dir)
    elif row.startswith("cd"):
        i = 0
    else:
        new_file = file_data()
        d = row.split(" ")
        new_file.size = d[0]
        new_file.name = d[1]
        cur_directory.file_datas.append(new_file)
    