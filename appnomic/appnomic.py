with open("input.txt") as f:
    file_list = f.readlines()
try:
    sum = 0
    for i in range(7):
        sum += int(file_list[i])
    print(sum)
except:
    print("Error")
