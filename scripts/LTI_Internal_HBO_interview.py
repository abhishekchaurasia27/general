x = input("Enter a number")
xlist = list(x)
xlist = [int(x) for x in xlist]
print(f"Entered list is {xlist}")

avg_list = []
for i in range(len(xlist)):
    if i == len(xlist) - 1:
        avg = (xlist[i] + xlist[0] + xlist[1]) / 3
    elif i == len(xlist) - 2:
        avg = (xlist[i] + xlist[i+1] + xlist[0]) / 3
    else:
        avg = (xlist[i] + xlist[i+1] + xlist[i+2]) / 3
    avg_list.append(avg)

print(f'Max avg of 3 consecutive numbers is {max(avg_list)}')