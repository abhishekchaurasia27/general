inp = input("Enter a starting number")
linp = list(inp)
endrange = int('1' + '0' * len(inp)) + 1
print(endrange)
print(f"Entered list is: {linp}")
for i in range(int(inp), endrange):
    print(list(str(i)))
