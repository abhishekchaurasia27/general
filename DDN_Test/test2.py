def solution(A):
    # write your code in Python 3.6
    results = []
    for face in A:
        rotations = 0
        for die in A:
            if (face == 1 and die == 6) or (face == 6 and die == 1):
                rotations += 2
            elif (face == 2 and die == 5) or (face == 5 and die == 2):
                rotations += 2
            elif (face == 3 and die == 4) or (face == 4 and die == 3):
                rotations += 2
            elif face != die:
                rotations += 1
        results.append(rotations)
    return min(results)

print(solution([1,2,3]))