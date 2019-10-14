string = 'BANANA'
vowel = ['A', 'E', 'I', 'O', 'U']
vl = set()

for i, j in enumerate(string):
    s = ''
    if j not in vowel:
        for k in range(i, len(string)):
            s = j + str(string[i+1:k+1])
            print(s)
            vl.add(s)
print(vl)