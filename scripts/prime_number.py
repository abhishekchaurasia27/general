x = int(input("Enter a number: "))
out = []


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(x+1):
    if isprime(i):
        out.append(i)

print(out)

var = 0
count = 0
for i in range(x):
    if isprime(i):
        var = var + i
        if var != 2 and var <= x:
            if isprime(var):
                count = count + 1
print(count)
