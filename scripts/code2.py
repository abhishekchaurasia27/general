data = {}
inp = input("Enter a input string: ")
for i in inp:
    if i not in data:
        data[i] = inp.count(i)
print(data)
max_value = max(data.values())
for key, value in data.items():
    if value == max_value:
        print(f"char {key} is coming {value} times.")
