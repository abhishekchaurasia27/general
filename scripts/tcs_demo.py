n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
N = int(input("Index prime number index: "))

if n1 < 0 or n1 > 1500000 or n2 < 0 or n2 > 1500000 or N < n1 or N > n2 or N == 0:
    print("Invalid Input")
    exit(0)

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
try:
    prime_list=[]
    for i in range(n1, n2+1):
        if prime(i):
            prime_list.append(i)
    N = N-1
    if prime_list[N]:
        print("Output: {}".format(prime_list[N]))
except IndexError:
    print("No Prime Number is there at this index")
