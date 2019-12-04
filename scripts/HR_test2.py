def minimumMoves(a, m):
    # Write your code here
    out = 0
    for i in range(len(a)):
        x = str(a[i])
        y = str(m[i])
        for j in range(len(x)):
            out += abs(int(x[j]) - int(y[j]))
    return out