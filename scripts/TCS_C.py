n = int(input())
global best_case
global worst_case
best_case = 0
worst_case = 0

def best_rec(n):
    global best_case
    if n > 2:
        best_case = best_case + 1
        best_rec(n-2)
def worst_rec(n):
    global worst_case
    if n > 2:
        worst_case = worst_case + 1
        worst_rec(n-3)

worst_rec(n)
best_rec(n)
print(worst_case)
print(best_case)

