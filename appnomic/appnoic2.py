with open("input2.txt") as f:
    file_list = f.readlines()
for line in file_list:
    if len(line.strip()) == 28:
        print(line)