from functools import cache

arr = [[int(x) for x in line.strip()] for line in open(0)]
rows, cols = len(arr), len(arr[0])
inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

@cache
def go(i, j):
    if arr[i][j] == 9: return {(i, j)}, 1

    aa, bb = set(), 0
    for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if not inbound(ii, jj): continue
        if arr[ii][jj] != arr[i][j] + 1: continue

        a, b = go(ii, jj)
        aa |= a; bb += b
    return aa, bb

part1 = part2 = 0
for i in range(rows):
    for j in range(cols):
        if arr[i][j] != 0: continue
        a, b = go(i, j)
        part1 += len(a)
        part2 += b

print(part1)
print(part2)
